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
        make_entity(entity_audit, "AI-Agent", "AI Agent", ["Agentic AI"]),
        make_entity(entity_audit, "Agentic-AI", "Agentic AI", []),
        make_entity(entity_audit, "Knowledge-Graph", "Knowledge Graph", []),
    ]

    candidates = entity_audit.duplicate_candidates(rows)

    assert len(candidates) == 1
    assert candidates[0].left.stem == "AI-Agent"
    assert candidates[0].right.stem == "Agentic-AI"
    assert candidates[0].reason == "alias cross-match"
