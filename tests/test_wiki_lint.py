import importlib.util
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
