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


def test_render_summary_counts_duplicate_candidates():
    entity_audit = load_entity_audit()
    rows = [
        make_entity(entity_audit, "Prompt-Injection", "Prompt Injection", ["Indirect Prompt Injection"]),
        make_entity(entity_audit, "Indirect-Prompt-Injection", "Indirect Prompt Injection", []),
    ]

    summary = entity_audit.render_summary(rows)

    assert "疑似重复: 1" in summary
