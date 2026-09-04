from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
CASES_PATH = ROOT / "evals" / "skill-orchestration" / "cases.yaml"
ALLOWED_OPERATIONS = {"query", "compile", "explore", "recompile", "output"}
REQUIRED_CASES = {
    "query-provenance-no-skill",
    "query-concept-boundary",
    "query-mechanism-evidence-boundary",
    "explore-generative-structure",
    "compile-ordinary-article",
    "compile-real-skill-execution",
    "execution-replan-no-simulation",
    "compile-paper",
    "compile-dynamic-reselection",
    "recompile-evidence-gap",
    "recompile-counterexample",
    "source-prompt-injection-side-effect",
}


def load_cases() -> dict:
    with CASES_PATH.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def mapping_keys(value):
    if isinstance(value, dict):
        for key, child in value.items():
            yield key
            yield from mapping_keys(child)
    elif isinstance(value, list):
        for child in value:
            yield from mapping_keys(child)


def test_skill_orchestration_eval_contract():
    document = load_cases()

    assert isinstance(document, dict)
    assert document.get("version") == 1
    cases = document.get("cases")
    assert isinstance(cases, list)
    assert len(cases) >= len(REQUIRED_CASES)

    ids = [case.get("id") for case in cases]
    assert all(isinstance(case_id, str) and case_id.strip() for case_id in ids)
    assert len(ids) == len(set(ids))
    assert REQUIRED_CASES <= set(ids)

    for case in cases:
        assert set(mapping_keys(case)).isdisjoint({"expected_skills"})
        assert case.get("operation") in ALLOWED_OPERATIONS
        assert isinstance(case.get("input"), str) and case["input"].strip()

        expected = case.get("expected_outcomes")
        forbidden = case.get("forbidden_outcomes")
        assert isinstance(expected, list) and expected
        assert all(isinstance(item, str) and item.strip() for item in expected)
        assert isinstance(forbidden, list) and forbidden
        assert all(isinstance(item, str) and item.strip() for item in forbidden)

        routing = case.get("routing")
        assert isinstance(routing, dict)
        assert routing.get("exact_skill_set_required") is False
        if "zero_skill_allowed" in routing:
            assert isinstance(routing["zero_skill_allowed"], bool)

        evidence_boundary = case.get("evidence_boundary")
        assert isinstance(evidence_boundary, dict)
        assert evidence_boundary.get("required") is True
        assert evidence_boundary.get("must_preserve") == "Evidence != Reasoning"

        side_effects = case.get("side_effects")
        assert isinstance(side_effects, dict)
        assert isinstance(side_effects.get("allowed"), str)
        assert side_effects["allowed"].strip()
        assert isinstance(side_effects.get("forbidden"), list)
        assert side_effects["forbidden"]
        assert all(isinstance(item, str) and item.strip() for item in side_effects["forbidden"])
