# Task 5 Report

Date: 2026-06-29
Worktree: `/home/lx/agentic-work-atlas/.worktrees/raw-compile-registry`

## Verification Commands

### 1. `uv run python tools/compile_registry.py bootstrap`

Exit code: `0`

```text
bootstrapped 152 raw entries
```

### 2. `uv run python tools/compile_registry.py status`

Exit code: `0`

```text
Raw Compile Registry
============================================================
pending=1 compiled=151 skipped=0
```

### 3. `uv run --with pytest --with pyyaml pytest tests/test_compile_registry.py tests/test_wiki_lint.py tests/test_entity_audit.py -v`

Exit code: `0`

```text
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-9.1.1, pluggy-1.6.0 -- /home/lx/.cache/uv/builds-v0/.tmp5hJeqf/bin/python
cachedir: .pytest_cache
rootdir: /home/lx/agentic-work-atlas/.worktrees/raw-compile-registry
configfile: pyproject.toml
collecting ... collected 28 items

tests/test_compile_registry.py::test_body_digest_ignores_frontmatter_changes PASSED [  3%]
tests/test_compile_registry.py::test_body_digest_ignores_frontmatter_when_body_starts_with_mapping_like_text PASSED [  7%]
tests/test_compile_registry.py::test_mark_compiled_and_mark_skipped_update_registry_entries PASSED [ 10%]
tests/test_compile_registry.py::test_save_and_load_registry_round_trip PASSED [ 14%]
tests/test_compile_registry.py::test_save_registry_rejects_invalid_status PASSED [ 17%]
tests/test_compile_registry.py::test_load_registry_rejects_invalid_persisted_status PASSED [ 21%]
tests/test_compile_registry.py::test_bootstrap_registry_reads_legacy_compiled_signals PASSED [ 25%]
tests/test_compile_registry.py::test_reconcile_adds_new_raw_and_reports_recompile_candidates PASSED [ 28%]
tests/test_compile_registry.py::test_reconcile_surfaces_malformed_compiled_digest PASSED [ 32%]
tests/test_compile_registry.py::test_cli_ensure_and_mark_compiled_round_trip PASSED [ 35%]
tests/test_compile_registry.py::test_cli_mark_skipped_persists_reason_and_note PASSED [ 39%]
tests/test_wiki_lint.py::test_tag_quality_reports_non_blocking_tag_hygiene_issues PASSED [ 42%]
tests/test_wiki_lint.py::test_singleton_tags_are_non_blocking_hygiene_signals PASSED [ 46%]
tests/test_wiki_lint.py::test_evidence_schema_blocks_invalid_values PASSED [ 50%]
tests/test_wiki_lint.py::test_low_evidence_pages_are_non_blocking_review_signals PASSED [ 53%]
tests/test_wiki_lint.py::test_single_quoted_frontmatter_allows_inner_double_quotes PASSED [ 57%]
tests/test_wiki_lint.py::test_stale_core_pages_are_non_blocking_maintenance_signals PASSED [ 60%]
tests/test_wiki_lint.py::test_registry_backed_raw_status_excludes_skipped_from_pending PASSED [ 64%]
tests/test_wiki_lint.py::test_registry_consistency_reports_missing_summary PASSED [ 67%]
tests/test_wiki_lint.py::test_registry_consistency_reports_missing_registry_entry PASSED [ 71%]
tests/test_wiki_lint.py::test_registry_consistency_reports_missing_registry_file PASSED [ 75%]
tests/test_wiki_lint.py::test_registry_consistency_reports_malformed_registry_file PASSED [ 78%]
tests/test_wiki_lint.py::test_registry_consistency_reports_malformed_registry_json PASSED [ 82%]
tests/test_entity_audit.py::test_duplicate_candidates_detect_alias_and_token_overlap PASSED [ 85%]
tests/test_entity_audit.py::test_duplicate_candidates_ignore_generic_domain_token_overlap PASSED [ 89%]
tests/test_entity_audit.py::test_duplicate_candidates_ignore_empty_normalized_non_latin_aliases PASSED [ 92%]
tests/test_entity_audit.py::test_duplicate_candidates_ignore_aliases_that_only_share_generic_tokens PASSED [ 96%]
tests/test_entity_audit.py::test_render_summary_counts_duplicate_candidates PASSED [100%]

============================== 28 passed in 0.33s ==============================
```

### 4. `uv run --with pyyaml python tools/wiki-lint.py --write-report`

Exit code: `0`

```text
Agentic Work Atlas Lint
============================================================
Raw: 152（已编译 151，待编译 1，已跳过 0）
Entity: 286 | Topic: 30 | Comparison: 19 | Output: 5 | Research: 14
阻断问题: 0
- low-evidence: 1

待编译 Raw:
- raw/The Tokenpocalypse Is Here Companies Are Scrambling To Stop Spending So Much on AI.md

前几个问题:
- [low-evidence] wiki/topics/AI-Management-Mindset-Transfer.md: 低证据页面 AI-Management-Mindset-Transfer 只能作为补 source 或探索线索

已写入 wiki/lint-report.md
```

## Notes

- `bootstrap` initially revealed a legacy-summary detection bug in `tools/compile_registry.py`; fixed by resolving compiled summaries through `expected_summary_path(raw_path.name)`.
- Final registry authority state is `152` raw files total, with `151` compiled and `1` pending.
- `docs/` is removed from git tracking in the final commit, while local files remain on disk.
