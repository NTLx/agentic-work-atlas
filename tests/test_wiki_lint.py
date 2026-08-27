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
    assert {"raw_file": "compiled.md", "reason": "missing-summary", "severity": "blocking"} in candidates
    registry_issues = [issue for issue in issues if issue.category == "registry-consistency"]
    assert registry_issues
    assert any(issue.blocking for issue in registry_issues)
    assert 'status: "FAIL"' in wiki_lint.render_report(issues, stats, pending, skipped, candidates)


def test_registry_consistency_reports_blocking_compiled_body_drift(tmp_path, monkeypatch):
    wiki_lint = load_wiki_lint()
    write_note(tmp_path / "index.md", "type: index\ntitle: Test\nupdated: 2026-06-28\n", "")
    write_note(tmp_path / "README.md", "title: Readme\n", "")
    write_note(tmp_path / "raw" / "compiled.md", "type: raw\n", "mutated")
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
    assert {"raw_file": "compiled.md", "reason": "body-changed", "severity": "blocking"} in candidates
    registry_issues = [issue for issue in issues if issue.category == "registry-consistency"]
    assert registry_issues
    assert any(issue.blocking for issue in registry_issues)
    assert 'status: "FAIL"' in wiki_lint.render_report(issues, stats, pending, skipped, candidates)


def test_registry_consistency_reports_missing_registry_entry(tmp_path, monkeypatch):
    wiki_lint = load_wiki_lint()
    write_note(tmp_path / "index.md", "type: index\ntitle: Test\nupdated: 2026-06-28\n", "")
    write_note(tmp_path / "README.md", "title: Readme\n", "")
    write_note(tmp_path / "raw" / "orphan.md", "type: raw\n", "body")
    write_registry(
        tmp_path,
        {
            "version": 1,
            "updated_at": "2026-06-28T12:30:00+08:00",
            "items": {},
        },
    )

    monkeypatch.setattr(wiki_lint, "ROOT", tmp_path)
    monkeypatch.setattr(wiki_lint, "RAW", tmp_path / "raw")
    monkeypatch.setattr(wiki_lint, "WIKI", tmp_path / "wiki")
    monkeypatch.setattr(wiki_lint, "INDEX", tmp_path / "index.md")
    monkeypatch.setattr(wiki_lint, "LINT_REPORT", tmp_path / "wiki" / "lint-report.md")

    issues, stats, pending, skipped, candidates = wiki_lint.collect_issues()

    assert stats["raw_compiled"] == 0
    assert pending == [tmp_path / "raw" / "orphan.md"]
    assert skipped == []
    assert candidates == []
    assert any(
        issue.category == "registry-consistency" and issue.path == tmp_path / "raw" / "orphan.md"
        for issue in issues
    )


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


def test_registry_consistency_reports_malformed_registry_file(tmp_path, monkeypatch):
    wiki_lint = load_wiki_lint()
    write_note(tmp_path / "index.md", "type: index\ntitle: Test\nupdated: 2026-06-28\n", "")
    write_note(tmp_path / "README.md", "title: Readme\n", "")
    write_note(tmp_path / "raw" / "compiled.md", "type: raw\n", "body")
    registry_path = tmp_path / "state" / "raw-registry.json"
    registry_path.parent.mkdir(parents=True, exist_ok=True)
    registry_path.write_text('{"version": 1, "items": {"broken.md": {"status": "bogus"}}}\n', encoding="utf-8")

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
        issue.category == "registry-consistency" and issue.path == registry_path and "invalid registry file" in issue.message
        for issue in issues
    )


def test_registry_consistency_reports_malformed_registry_json(tmp_path, monkeypatch):
    wiki_lint = load_wiki_lint()
    write_note(tmp_path / "index.md", "type: index\ntitle: Test\nupdated: 2026-06-28\n", "")
    write_note(tmp_path / "README.md", "title: Readme\n", "")
    write_note(tmp_path / "raw" / "compiled.md", "type: raw\n", "body")
    registry_path = tmp_path / "state" / "raw-registry.json"
    registry_path.parent.mkdir(parents=True, exist_ok=True)
    registry_path.write_text('{"version": 1, "items": {"broken.md": ', encoding="utf-8")

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
        issue.category == "registry-consistency" and issue.path == registry_path and "Expecting value" in issue.message
        for issue in issues
    )


def test_registry_lifecycle_states_are_counted_without_becoming_pending(tmp_path, monkeypatch):
    wiki_lint = load_wiki_lint()
    (tmp_path / "raw").mkdir()
    write_note(tmp_path / "index.md", "type: index\ntitle: Test\nupdated: 2026-06-28\n", "")
    write_note(tmp_path / "README.md", "title: Readme\n", "")
    write_note(tmp_path / "wiki" / "sources" / "indexed.md", "type: source-summary\n", "## 编译摘要")
    write_registry(
        tmp_path,
        {
            "version": 1,
            "updated_at": "2026-06-28T12:30:00+08:00",
            "items": {
                "indexed.pdf": {
                    "raw_file": "indexed.pdf",
                    "status": "compiled",
                    "raw_state": "index",
                    "body_sha256": body_sha256("indexed body"),
                    "summary_path": "wiki/sources/indexed.md",
                    "canonical_url": "https://example.com/indexed.pdf",
                    "indexed_at": "2026-06-28T12:10:00+08:00",
                    "updated_at": "2026-06-28T12:10:00+08:00",
                },
                "retired.md": {
                    "raw_file": "retired.md",
                    "status": "compiled",
                    "raw_state": "removed",
                    "body_sha256": body_sha256("retired body"),
                    "retired_at": "2026-06-28T12:20:00+08:00",
                    "retire_reason": "被一手来源替代",
                    "updated_at": "2026-06-28T12:20:00+08:00",
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
    assert skipped == []
    assert candidates == []
    assert stats["raw_full"] == 0
    assert stats["raw_indexed"] == 1
    assert stats["raw_removed"] == 1
    assert not [issue for issue in issues if issue.category == "registry-consistency"]
    report = wiki_lint.render_report(issues, stats, pending, skipped, candidates)
    assert "| Raw 索引化 | 1 |" in report
    assert "| Raw 已移除 | 1 |" in report


def test_source_raw_allows_indexed_evidence_and_blocks_removed_evidence(tmp_path, monkeypatch):
    wiki_lint = load_wiki_lint()
    (tmp_path / "raw").mkdir()
    write_note(tmp_path / "wiki" / "sources" / "indexed.md", "type: source-summary\n", "")
    write_note(tmp_path / "wiki" / "sources" / "removed.md", "type: source-summary\n", "")
    write_note(
        tmp_path / "wiki" / "entities" / "Example.md",
        """type: entity
title: Example
source_raw:
  - "[[indexed.pdf]]"
  - "[[removed.pdf]]"
""",
        "",
    )
    write_registry(
        tmp_path,
        {
            "version": 1,
            "updated_at": "2026-06-28T12:30:00+08:00",
            "items": {
                "indexed.pdf": {
                    "raw_file": "indexed.pdf",
                    "status": "compiled",
                    "raw_state": "index",
                    "body_sha256": body_sha256("indexed body"),
                    "summary_path": "wiki/sources/indexed.md",
                    "canonical_url": "https://example.com/indexed.pdf",
                    "indexed_at": "2026-06-28T12:10:00+08:00",
                    "updated_at": "2026-06-28T12:10:00+08:00",
                },
                "removed.pdf": {
                    "raw_file": "removed.pdf",
                    "status": "compiled",
                    "raw_state": "removed",
                    "body_sha256": body_sha256("removed body"),
                    "retired_at": "2026-06-28T12:20:00+08:00",
                    "retire_reason": "低质量来源",
                    "updated_at": "2026-06-28T12:20:00+08:00",
                },
            },
        },
    )

    monkeypatch.setattr(wiki_lint, "ROOT", tmp_path)
    monkeypatch.setattr(wiki_lint, "RAW", tmp_path / "raw")
    monkeypatch.setattr(wiki_lint, "WIKI", tmp_path / "wiki")
    monkeypatch.setattr(wiki_lint, "INDEX", tmp_path / "index.md")

    issues = wiki_lint.check_source_raw()

    assert len(issues) == 1
    assert issues[0].category == "source_raw"
    assert "已移除 Evidence" in issues[0].message
    assert "removed.pdf" in issues[0].message


def test_relations_valid_entity_to_entity_passes(tmp_path, monkeypatch):
    wiki_lint = load_wiki_lint()
    (tmp_path / "wiki" / "entities").mkdir(parents=True)
    write_note(tmp_path / "wiki" / "entities" / "Target-A.md", "type: entity\n", "")
    write_note(tmp_path / "wiki" / "entities" / "Target-B.md", "type: entity\n", "")
    path = write_note(
        tmp_path / "wiki" / "entities" / "Example.md",
        """type: entity
relations:
  depends_on:
    - "[[Target-A]]"
  enables:
    - "[[Target-B]]"
""",
        "",
    )
    monkeypatch.setattr(wiki_lint, "WIKI", tmp_path / "wiki")

    issues = wiki_lint.check_relations([path])

    assert issues == []


def test_relations_illegal_predicate_fails(tmp_path, monkeypatch):
    wiki_lint = load_wiki_lint()
    (tmp_path / "wiki" / "entities").mkdir(parents=True)
    write_note(tmp_path / "wiki" / "entities" / "Target-A.md", "type: entity\n", "")
    path = write_note(
        tmp_path / "wiki" / "entities" / "Example.md",
        """type: entity
relations:
  related_to:
    - "[[Target-A]]"
""",
        "",
    )
    monkeypatch.setattr(wiki_lint, "WIKI", tmp_path / "wiki")

    issues = wiki_lint.check_relations([path])

    assert any("非法 predicate" in i.message for i in issues)
    assert all(i.blocking for i in issues)


def test_relations_missing_target_fails(tmp_path, monkeypatch):
    wiki_lint = load_wiki_lint()
    (tmp_path / "wiki" / "entities").mkdir(parents=True)
    path = write_note(
        tmp_path / "wiki" / "entities" / "Example.md",
        """type: entity
relations:
  depends_on:
    - "[[Nonexistent-Target]]"
""",
        "",
    )
    monkeypatch.setattr(wiki_lint, "WIKI", tmp_path / "wiki")

    issues = wiki_lint.check_relations([path])

    assert any("目标必须指向实体 Entity" in i.message for i in issues)
    assert all(i.blocking for i in issues)


def test_relations_non_wikilink_target_fails(tmp_path, monkeypatch):
    wiki_lint = load_wiki_lint()
    (tmp_path / "wiki" / "entities").mkdir(parents=True)
    write_note(tmp_path / "wiki" / "entities" / "Target-A.md", "type: entity\n", "")
    path = write_note(
        tmp_path / "wiki" / "entities" / "Example.md",
        """type: entity
relations:
  depends_on:
    - "Target-A"
""",
        "",
    )
    monkeypatch.setattr(wiki_lint, "WIKI", tmp_path / "wiki")

    issues = wiki_lint.check_relations([path])

    assert any("必须是 wikilink" in i.message for i in issues)
    assert all(i.blocking for i in issues)


def test_relations_rejected_on_non_entity_pages(tmp_path, monkeypatch):
    wiki_lint = load_wiki_lint()
    (tmp_path / "wiki" / "entities").mkdir(parents=True)
    write_note(tmp_path / "wiki" / "entities" / "Target-A.md", "type: entity\n", "")
    path = write_note(
        tmp_path / "wiki" / "topics" / "Example.md",
        """type: topic
relations:
  depends_on:
    - "[[Target-A]]"
""",
        "",
    )
    monkeypatch.setattr(wiki_lint, "WIKI", tmp_path / "wiki")

    issues = wiki_lint.check_relations([path])

    assert any("只允许出现在 type: entity" in i.message for i in issues)
    assert all(i.blocking for i in issues)


def test_as_of_makes_report_deterministic(tmp_path, monkeypatch):
    wiki_lint = load_wiki_lint()
    (tmp_path / "raw").mkdir(parents=True)
    (tmp_path / "wiki" / "entities").mkdir(parents=True)
    index_path = write_note(tmp_path / "index.md", "type: index\ntitle: Test\nupdated: 2026-08-01\n", "")
    write_note(tmp_path / "README.md", "title: Readme\n", "")

    monkeypatch.setattr(wiki_lint, "ROOT", tmp_path)
    monkeypatch.setattr(wiki_lint, "RAW", tmp_path / "raw")
    monkeypatch.setattr(wiki_lint, "WIKI", tmp_path / "wiki")
    monkeypatch.setattr(wiki_lint, "INDEX", tmp_path / "index.md")
    monkeypatch.setattr(wiki_lint, "LINT_REPORT", tmp_path / "wiki" / "lint-report.md")

    # 相同 as-of：index 写出的 updated 取自 as-of 而非墙钟，重复运行幂等
    assert wiki_lint.fix_index_counts(as_of=date(2026, 8, 26))
    index_first = index_path.read_text(encoding="utf-8")
    assert "updated: 2026-08-26" in index_first
    assert not wiki_lint.fix_index_counts(as_of=date(2026, 8, 26))
    assert index_path.read_text(encoding="utf-8") == index_first

    # 相同 as-of：报告完全一致，且日期、运行命令都引用 as-of
    stats = {
        "raw": 1, "raw_compiled": 1, "raw_pending": 0, "raw_skipped": 0,
        "raw_full": 1, "raw_indexed": 0, "raw_removed": 0,
        "entities": 1, "topics": 0, "comparisons": 0, "outputs": 0, "research": 0,
    }
    report_first = wiki_lint.render_report([], stats, [], [], [], as_of=date(2026, 8, 26))
    assert 'date: "2026-08-26"' in report_first
    assert "# Agentic Work Atlas Lint 报告 - 2026-08-26" in report_first
    assert "--as-of 2026-08-26" in report_first
    assert wiki_lint.render_report([], stats, [], [], [], as_of=date(2026, 8, 26)) == report_first

    # 不同 as-of：报告日期随之变化（证明日期由 as-of 控制，而非其余状态）
    report_other = wiki_lint.render_report([], stats, [], [], [], as_of=date(2026, 8, 27))
    assert report_other != report_first
    assert 'date: "2026-08-27"' in report_other


def test_stale_core_respects_as_of(tmp_path):
    wiki_lint = load_wiki_lint()
    core = write_note(
        tmp_path / "wiki" / "entities" / "Core-Concept.md",
        "title: Core Concept\nupdated: 2026-05-29\ntags:\n  - ai-agent\n",
        "",
    )
    ref_a = write_note(tmp_path / "wiki" / "topics" / "A.md", "title: A\n", "[[Core-Concept]]")
    ref_b = write_note(tmp_path / "wiki" / "comparisons" / "B.md", "title: B\n", "[[Core-Concept]]")

    # 截止 2026-08-26 为 89 天，未达 90 天阈值
    assert not wiki_lint.check_stale_core_pages(
        [core, ref_a, ref_b], today=date(2026, 8, 26), stale_days=90, min_inbound=2
    )
    # 截止 2026-08-27 恰好 90 天，跨入 stale
    issues = wiki_lint.check_stale_core_pages(
        [core, ref_a, ref_b], today=date(2026, 8, 27), stale_days=90, min_inbound=2
    )
    assert len(issues) == 1
    assert issues[0].category == "stale-core"
    assert not issues[0].blocking
