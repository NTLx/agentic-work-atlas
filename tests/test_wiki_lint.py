import importlib.util
import hashlib
import json
import sys
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_wiki_lint():
    spec = importlib.util.spec_from_file_location("wiki_lint", ROOT / "tools" / "wiki-lint.py")
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def write_note(path: Path, frontmatter: str, body: str = "") -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"---\n{frontmatter}---\n\n{body}", encoding="utf-8")
    return path


def write_registry(root: Path, payload: dict) -> None:
    path = root / "state" / "raw-registry.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def body_sha256(body: str) -> str:
    return hashlib.sha256(body.encode("utf-8")).hexdigest()


def test_tag_quality_reports_non_blocking_tag_hygiene_issues(tmp_path):
    wiki_lint = load_wiki_lint()
    path = write_note(
        tmp_path / "wiki" / "entities" / "Example.md",
        """title: Example
tags:
  - ai-agent
  - AI-Agent
  - AI Agent
  - workflow
  - tooling
  - agentic_engineering
  - misc
""",
    )

    issues = wiki_lint.check_tag_quality([path])

    assert issues
    assert {issue.category for issue in issues} == {"tag"}
    assert all(not issue.blocking for issue in issues)
    assert any("超过 5 个" in issue.message for issue in issues)
    assert any("非 kebab-case" in issue.message for issue in issues)
    assert not any("'AI-Agent'" in issue.message for issue in issues)


def test_singleton_tags_are_non_blocking_hygiene_signals(tmp_path):
    wiki_lint = load_wiki_lint()
    first = write_note(
        tmp_path / "wiki" / "entities" / "First.md",
        """title: First
tags:
  - stable-tag
  - one-off-tag
""",
    )
    second = write_note(
        tmp_path / "wiki" / "entities" / "Second.md",
        """title: Second
tags:
  - stable-tag
""",
    )

    issues = wiki_lint.check_singleton_tags([first, second])

    assert len(issues) == 1
    assert issues[0].category == "tag"
    assert not issues[0].blocking
    assert "one-off-tag" in issues[0].message


def test_evidence_schema_blocks_invalid_values(tmp_path):
    wiki_lint = load_wiki_lint()
    path = write_note(
        tmp_path / "wiki" / "topics" / "Example.md",
        """title: Example
evidence_level: certain
claim_type: guessed
tags:
  - ai-agent
""",
    )

    issues = wiki_lint.check_evidence_schema([path])

    assert len(issues) == 2
    assert all(issue.category == "evidence" for issue in issues)
    assert all(issue.blocking for issue in issues)


def test_low_evidence_pages_are_non_blocking_review_signals(tmp_path):
    wiki_lint = load_wiki_lint()
    path = write_note(
        tmp_path / "wiki" / "entities" / "Weak.md",
        """title: Weak
evidence_level: low
claim_type: synthesized
""",
    )

    issues = wiki_lint.check_low_evidence_pages([path])

    assert len(issues) == 1
    assert issues[0].category == "low-evidence"
    assert not issues[0].blocking
    assert "Weak" in issues[0].message


def test_single_quoted_frontmatter_allows_inner_double_quotes(tmp_path):
    wiki_lint = load_wiki_lint()
    path = write_note(
        tmp_path / "wiki" / "entities" / "Quoted.md",
        """title: Quoted
source_raw:
  - '[[文章标题里的"第一处"与"第二处"]]'
""",
    )

    issues = wiki_lint.check_frontmatter_and_dates([path])

    assert not issues


def test_stale_core_pages_are_non_blocking_maintenance_signals(tmp_path):
    wiki_lint = load_wiki_lint()
    core = write_note(
        tmp_path / "wiki" / "entities" / "Core-Concept.md",
        """title: Core Concept
updated: 2025-01-01
tags:
  - ai-agent
""",
    )
    ref_a = write_note(tmp_path / "wiki" / "topics" / "A.md", "title: A\n", "[[Core-Concept]]")
    ref_b = write_note(tmp_path / "wiki" / "comparisons" / "B.md", "title: B\n", "[[Core-Concept]]")

    issues = wiki_lint.check_stale_core_pages(
        [core, ref_a, ref_b],
        today=date(2026, 6, 13),
        stale_days=90,
        min_inbound=2,
    )

    assert len(issues) == 1
    assert issues[0].category == "stale-core"
    assert not issues[0].blocking
    assert "Core-Concept" in issues[0].message


def test_registry_backed_raw_status_excludes_skipped_from_pending(tmp_path, monkeypatch):
    wiki_lint = load_wiki_lint()
    write_note(tmp_path / "index.md", "type: index\ntitle: Test\nupdated: 2026-06-28\n", "")
    write_note(tmp_path / "README.md", "title: Readme\n", "")
    write_note(tmp_path / "raw" / "compiled.md", "type: raw\n", "body")
    write_note(tmp_path / "raw" / "skipped.md", "type: raw\n", "body")
    write_note(tmp_path / "wiki" / "sources" / "compiled.md", "type: source-summary\n", "## 编译摘要")
    write_registry(
        tmp_path,
        {
            "version": 1,
            "updated_at": "2026-06-28T12:30:00+08:00",
            "items": {
                "compiled.md": {
                    "raw_file": "compiled.md",
                    "status": "compiled",
                    "body_sha256": body_sha256("body"),
                    "summary_path": "wiki/sources/compiled.md",
                    "compiled_at": "2026-06-28T12:00:00+08:00",
                    "updated_at": "2026-06-28T12:00:00+08:00",
                },
                "skipped.md": {
                    "raw_file": "skipped.md",
                    "status": "skipped",
                    "body_sha256": body_sha256("body"),
                    "skip_reason_code": "off-topic",
                    "skip_note": "skip it",
                    "updated_at": "2026-06-28T12:05:00+08:00",
                },
            },
        },
    )

    monkeypatch.setattr(wiki_lint, "ROOT", tmp_path)
    monkeypatch.setattr(wiki_lint, "RAW", tmp_path / "raw")
    monkeypatch.setattr(wiki_lint, "WIKI", tmp_path / "wiki")
    monkeypatch.setattr(wiki_lint, "INDEX", tmp_path / "index.md")
    monkeypatch.setattr(wiki_lint, "LINT_REPORT", tmp_path / "wiki" / "lint-report.md")

    issues, stats, pending, skipped, candidates = wiki_lint.collect_issues()

    assert pending == []
    assert [path.name for path in skipped] == ["skipped.md"]
    assert stats["raw_compiled"] == 1
    assert stats["raw_skipped"] == 1
    assert candidates == []
    assert not [issue for issue in issues if issue.category == "registry-consistency"]


def test_registry_consistency_reports_missing_summary(tmp_path, monkeypatch):
    wiki_lint = load_wiki_lint()
    write_note(tmp_path / "index.md", "type: index\ntitle: Test\nupdated: 2026-06-28\n", "")
    write_note(tmp_path / "README.md", "title: Readme\n", "")
    write_note(tmp_path / "raw" / "compiled.md", "type: raw\n", "body")
    write_registry(
        tmp_path,
        {
            "version": 1,
            "updated_at": "2026-06-28T12:30:00+08:00",
            "items": {
                "compiled.md": {
                    "raw_file": "compiled.md",
                    "status": "compiled",
                    "body_sha256": body_sha256("body"),
                    "summary_path": "wiki/sources/compiled.md",
                    "compiled_at": "2026-06-28T12:00:00+08:00",
                    "updated_at": "2026-06-28T12:00:00+08:00",
                }
            },
        },
    )

    monkeypatch.setattr(wiki_lint, "ROOT", tmp_path)
    monkeypatch.setattr(wiki_lint, "RAW", tmp_path / "raw")
    monkeypatch.setattr(wiki_lint, "WIKI", tmp_path / "wiki")
    monkeypatch.setattr(wiki_lint, "INDEX", tmp_path / "index.md")
    monkeypatch.setattr(wiki_lint, "LINT_REPORT", tmp_path / "wiki" / "lint-report.md")

    issues, stats, pending, skipped, candidates = wiki_lint.collect_issues()

    assert stats["raw_compiled"] == 1
    assert pending == []
    assert skipped == []
    assert {"raw_file": "compiled.md", "reason": "missing-summary"} in candidates
    assert any(issue.category == "registry-consistency" for issue in issues)


def test_registry_consistency_reports_missing_registry_file(tmp_path, monkeypatch):
    wiki_lint = load_wiki_lint()
    write_note(tmp_path / "index.md", "type: index\ntitle: Test\nupdated: 2026-06-28\n", "")
    write_note(tmp_path / "README.md", "title: Readme\n", "")
    write_note(tmp_path / "raw" / "compiled.md", "type: raw\n", "body")
    write_note(tmp_path / "wiki" / "sources" / "compiled.md", "type: source-summary\n", "## 编译摘要")

    monkeypatch.setattr(wiki_lint, "ROOT", tmp_path)
    monkeypatch.setattr(wiki_lint, "RAW", tmp_path / "raw")
    monkeypatch.setattr(wiki_lint, "WIKI", tmp_path / "wiki")
    monkeypatch.setattr(wiki_lint, "INDEX", tmp_path / "index.md")
    monkeypatch.setattr(wiki_lint, "LINT_REPORT", tmp_path / "wiki" / "lint-report.md")

    issues, stats, pending, skipped, candidates = wiki_lint.collect_issues()

    assert stats["raw_compiled"] == 0
    assert pending == [tmp_path / "raw" / "compiled.md"]
    assert skipped == []
    assert candidates == []
    assert any(
        issue.category == "registry-consistency" and "raw-registry.json" in issue.message
        for issue in issues
    )
