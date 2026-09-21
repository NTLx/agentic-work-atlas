import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_entity_audit():
    spec = importlib.util.spec_from_file_location("entity_audit", ROOT / "tools" / "entity-audit.py")
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def make_entity(entity_audit, stem: str, title: str, aliases=None):
    return entity_audit.Entity(
        stem=stem,
        path=Path(f"wiki/entities/{stem}.md"),
        title=title,
        aliases=aliases or [],
        definition="",
        tags=["concept"],
        source_count=1,
        related_count=0,
        body_len=100,
        graph_in=0,
        topic_in=0,
        comparison_in=0,
        entity_in=0,
        reasons=[],
        score=50,
        bucket="review",
    )


def test_duplicate_candidates_detect_alias_and_token_overlap():
    entity_audit = load_entity_audit()
    rows = [
        make_entity(entity_audit, "Prompt-Injection", "Prompt Injection", ["Indirect Prompt Injection"]),
        make_entity(entity_audit, "Indirect-Prompt-Injection", "Indirect Prompt Injection", []),
        make_entity(entity_audit, "Knowledge-Graph", "Knowledge Graph", []),
    ]

    candidates = entity_audit.duplicate_candidates(rows)

    assert len(candidates) == 1
    assert candidates[0].left.stem == "Prompt-Injection"
    assert candidates[0].right.stem == "Indirect-Prompt-Injection"
    assert candidates[0].reason == "alias cross-match"


def test_duplicate_candidates_ignore_generic_domain_token_overlap():
    entity_audit = load_entity_audit()
    rows = [
        make_entity(entity_audit, "AI-Factory", "AI Factory", []),
        make_entity(entity_audit, "AI-Washing", "AI Washing", []),
        make_entity(entity_audit, "Agent-Harness", "Agent Harness", []),
        make_entity(entity_audit, "Agent-Verification", "Agent Verification", []),
    ]

    candidates = entity_audit.duplicate_candidates(rows)

    assert candidates == []


def test_duplicate_candidates_ignore_empty_normalized_non_latin_aliases():
    entity_audit = load_entity_audit()
    rows = [
        make_entity(entity_audit, "AI-Amish", "AI Amish", ["阿米什"]),
        make_entity(entity_audit, "Automated-Criteria", "Automated Criteria", ["自动化判据"]),
    ]

    candidates = entity_audit.duplicate_candidates(rows)

    assert candidates == []


def test_duplicate_candidates_ignore_aliases_that_only_share_generic_tokens():
    entity_audit = load_entity_audit()
    rows = [
        make_entity(entity_audit, "AI-Amish", "AI Amish", ["AI 阿米什"]),
        make_entity(entity_audit, "AI-Factory", "AI Factory", ["AI 工厂"]),
    ]

    candidates = entity_audit.duplicate_candidates(rows)

    assert candidates == []


def test_duplicate_candidates_ignore_single_meaningful_token_alias_collision():
    entity_audit = load_entity_audit()
    rows = [
        make_entity(entity_audit, "Agent-Harness", "Agent Harness", ["Harness"]),
        make_entity(entity_audit, "EnvHarness", "EnvHarness", ["Harness"]),
        make_entity(entity_audit, "Sleep-Token", "Sleep Token", ["Token"]),
        make_entity(entity_audit, "Token-Maxing", "Token Maxing", ["Token"]),
    ]

    candidates = entity_audit.duplicate_candidates(rows)

    assert candidates == []


def test_render_summary_counts_duplicate_candidates():
    entity_audit = load_entity_audit()
    rows = [
        make_entity(entity_audit, "Prompt-Injection", "Prompt Injection", ["Indirect Prompt Injection"]),
        make_entity(entity_audit, "Indirect-Prompt-Injection", "Indirect Prompt Injection", []),
    ]

    summary = entity_audit.render_summary(rows)

    assert "疑似重复: 1" in summary


def test_render_report_lists_strengthen_entities():
    entity_audit = load_entity_audit()
    row = make_entity(entity_audit, "Needs-Strengthening", "Needs Strengthening", [])
    row.bucket = "strengthen"
    row.score = 42
    row.source_count = 2
    row.graph_in = 3
    row.topic_in = 1
    row.comparison_in = 0
    row.reasons = ["来源较少"]

    report = entity_audit.render_report([row])

    assert "## 增强队列" in report
    assert "| [[Needs-Strengthening]] | 42 | 2 | 3 | 1 | 0 | 来源较少 |" in report


def test_render_report_lists_legacy_provenance_gaps_but_skips_people():
    entity_audit = load_entity_audit()
    concept = make_entity(entity_audit, "Legacy-Concept", "Legacy Concept", [])
    concept.score = 36
    concept.graph_in = 7
    concept.topic_in = 1

    person = make_entity(entity_audit, "Example-Person", "Example Person", [])
    person.tags = ["person"]

    report = entity_audit.render_report([concept, person])

    assert "## Legacy provenance 队列" in report
    assert "| [[Legacy-Concept]] | 36 | 1 | 7 | 1 | 缺 evidence_level, 缺 claim_type |" in report
    assert "[[Example-Person]]" not in report.split("## Legacy provenance 队列", 1)[1].split("## 复核队列", 1)[0]


def test_render_report_accepts_valid_entity_provenance():
    entity_audit = load_entity_audit()
    row = make_entity(entity_audit, "Provenanced-Concept", "Provenanced Concept", [])
    row.evidence_level = "medium"
    row.claim_type = "mixed"

    report = entity_audit.render_report([row])
    provenance_section = report.split("## Legacy provenance 队列", 1)[1].split("## 复核队列", 1)[0]

    assert "[[Provenanced-Concept]]" not in provenance_section


def test_identity_page_detection_is_conservative_for_actor_entities():
    entity_audit = load_entity_audit()

    person = {"tags": ["author"], "validated_source": "https://example.com", "validated_at": "2026-01-01"}
    organization = {
        "tags": ["organization"],
        "validated_source": "https://example.com/about",
        "validated_at": "2026-01-01",
    }
    substantive_organization = {
        **organization,
        "evidence_level": "medium",
        "claim_type": "mixed",
    }

    assert entity_audit.is_identity_page(person)
    assert entity_audit.is_identity_page(organization)
    assert not entity_audit.is_identity_page(substantive_organization)
