# Task 4 Report

## Scope

- Task: Make `wiki-lint.py` consume the raw compile registry and audit consistency.
- Worktree: `/home/lx/agentic-work-atlas/.worktrees/raw-compile-registry`
- Files changed:
  - `tools/wiki-lint.py`
  - `tests/test_wiki_lint.py`
  - `tools/compile_registry.py`
  - `tests/test_compile_registry.py`

## TDD Record

### RED

1. Added the two Task 4 lint tests from the brief to `tests/test_wiki_lint.py`.
2. Ran:

```bash
uv run --with pytest --with pyyaml pytest tests/test_wiki_lint.py -v
```

Observed failure:

- `test_registry_backed_raw_status_excludes_skipped_from_pending`
- `test_registry_consistency_reports_missing_summary`

Failure reason matched the brief:

- `collect_issues()` returned 3 values instead of 5.
- `wiki-lint.py` was still inferring raw status from raw/wiki scans instead of the registry seam.

3. During integration, a second RED appeared because the brief requires placeholder `body_sha256` values like `"abc"` and `"def"` verbatim, while `reconcile_registry()` treated those as content drift.
4. Added a narrow regression test in `tests/test_compile_registry.py`:

```bash
uv run --with pytest --with pyyaml pytest tests/test_compile_registry.py -k non_sha_placeholder -v
```

Observed failure:

- `test_reconcile_ignores_non_sha_placeholder_digests`

## GREEN

### Implementation

- Replaced `wiki-lint.py` raw compile inference with `check_registry_consistency()`.
- Wired in:
  - `compile_registry.load_registry()`
  - `compile_registry.bootstrap_registry()`
  - `compile_registry.reconcile_registry()`
- Changed `collect_issues()` to return:
  - `issues`
  - `stats`
  - `pending`
  - `skipped`
  - `candidates`
- Made lint stats registry-backed for:
  - `raw_compiled`
  - `raw_pending`
  - `raw_skipped`
- Added registry consistency issues:
  - blocking for missing registry entries and anomalies
  - non-blocking for recompile candidates
- Updated report rendering with:
  - `registry-consistency` category row
  - `已跳过 Raw`
  - `需重编译候选`
- Updated CLI summary output to include skipped raws and recompile candidates.
- Added a minimal support change in `tools/compile_registry.py` so `body-changed` is only emitted when the stored digest is a real 64-char lowercase SHA256. This preserves the brief’s verbatim placeholder values in tests without widening the seam.

### Verification

Intermediate green checks:

```bash
uv run --with pytest --with pyyaml pytest tests/test_compile_registry.py -k non_sha_placeholder -v
uv run --with pytest --with pyyaml pytest tests/test_wiki_lint.py -v
```

Final task command:

```bash
uv run --with pytest --with pyyaml pytest tests/test_compile_registry.py tests/test_wiki_lint.py -v
```

Result:

- `19 passed in 0.20s`

## Self Review

- The seam stayed narrow: registry remains the authority, lint only audits and reports.
- No docs were touched.
- Only task-owned files changed.
- The compile registry support change is intentionally small and only suppresses false `body-changed` signals for non-SHA placeholder digests used by the required tests.

## Commit

- Commit created after verification:
  - `fix(lint): read raw compile status from registry`

## Fix Round 2

### RED

1. Added a strict-authority lint regression:
   - `test_registry_consistency_reports_missing_registry_file`
2. Added a malformed compiled digest regression:
   - `test_reconcile_surfaces_malformed_compiled_digest`
3. Replaced normal-path placeholder digests in Task 4 tests with real SHA256 values so the regressions target production behavior instead of test shortcuts.

Ran:

```bash
uv run --with pytest --with pyyaml pytest tests/test_wiki_lint.py -k 'missing_registry_file or excludes_skipped_from_pending or missing_summary' -v
uv run --with pytest --with pyyaml pytest tests/test_compile_registry.py -k malformed_compiled_digest -v
```

Observed failures:

- `test_registry_consistency_reports_missing_registry_file`
  - actual: `stats["raw_compiled"] == 1`
  - expected: missing `state/raw-registry.json` should yield a `registry-consistency` issue and keep the raw out of compiled status
- `test_reconcile_surfaces_malformed_compiled_digest`
  - actual: `anomalies == []`
  - expected: malformed persisted `body_sha256` should surface as an anomaly instead of being silently ignored

### GREEN

Implementation changes:

- Removed the `wiki-lint.py` bootstrap fallback; missing `state/raw-registry.json` now emits a blocking `registry-consistency` issue and reads empty authority state via `load_registry()`.
- Changed `reconcile_registry()` so compiled entries with malformed persisted `body_sha256` emit `invalid-body-sha256` anomalies instead of being silently skipped.
- Kept normal-path Task 4 tests on real SHA256 digests so production logic stays strict.

Targeted verification:

```bash
uv run --with pytest --with pyyaml pytest tests/test_wiki_lint.py -k 'missing_registry_file or excludes_skipped_from_pending or missing_summary' -v
uv run --with pytest --with pyyaml pytest tests/test_compile_registry.py -k malformed_compiled_digest -v
```

Results:

- `3 passed, 6 deselected` in `tests/test_wiki_lint.py`
- `1 passed, 10 deselected` in `tests/test_compile_registry.py`

Final task verification:

```bash
uv run --with pytest --with pyyaml pytest tests/test_compile_registry.py tests/test_wiki_lint.py -v
```

Result:

- `20 passed in 0.22s`
