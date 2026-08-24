import importlib.util
import hashlib
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_compile_registry():
    spec = importlib.util.spec_from_file_location("compile_registry", ROOT / "tools" / "compile_registry.py")
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def write_raw(root: Path, name: str, frontmatter: str, body: str) -> Path:
    path = root / "raw" / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"---\n{frontmatter}---\n\n{body}", encoding="utf-8")
    return path


def write_summary(root: Path, raw_name: str) -> Path:
    path = root / "wiki" / "sources" / raw_name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "---\ntype: source-summary\ntitle: Example\nsource_raw:\n  - \"[[example]]\"\n---\n\n## 编译摘要\n",
        encoding="utf-8",
    )
    return path


def body_sha256(body: str) -> str:
    return hashlib.sha256(body.encode("utf-8")).hexdigest()


def test_body_digest_ignores_frontmatter_changes(tmp_path):
    compile_registry = load_compile_registry()
    raw_path = write_raw(tmp_path, "example.md", "type: raw\ncreated: 2026-06-28\n", "alpha\nbeta\n")

    first = compile_registry.compute_body_sha256(raw_path)
    raw_path.write_text(
        "---\ntype: raw\ncreated: 2026-06-29\nauthor:\n  - Someone\n---\n\nalpha\nbeta\n",
        encoding="utf-8",
    )
    second = compile_registry.compute_body_sha256(raw_path)

    assert first == second


def test_body_digest_ignores_frontmatter_when_body_starts_with_mapping_like_text(tmp_path):
    compile_registry = load_compile_registry()
    raw_path = tmp_path / "raw" / "example.md"
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    raw_path.write_text(
        "---\n"
        "notes: |\n"
        "  one\n"
        "---\n"
        "title: x\n"
        "body\n",
        encoding="utf-8",
    )

    first = compile_registry.compute_body_sha256(raw_path)
    raw_path.write_text(
        "---\n"
        "notes: |\n"
        "  changed\n"
        "---\n"
        "title: x\n"
        "body\n",
        encoding="utf-8",
    )
    second = compile_registry.compute_body_sha256(raw_path)

    assert first == second


def test_mark_compiled_and_mark_skipped_update_registry_entries():
    compile_registry = load_compile_registry()
    registry = {"version": 1, "updated_at": "2026-06-28T10:30:00+08:00", "items": {}}

    compiled = compile_registry.mark_compiled(
        registry,
        raw_file="compiled.md",
        summary_path="wiki/sources/compiled.md",
        body_sha256=body_sha256("compiled body"),
        now="2026-06-28T10:30:00+08:00",
    )
    skipped = compile_registry.mark_skipped(
        registry,
        raw_file="skipped.md",
        reason_code="off-topic",
        note="不服务于主线问题",
        body_sha256=body_sha256("skipped body"),
        now="2026-06-28T10:35:00+08:00",
    )

    assert compiled["status"] == "compiled"
    assert compiled["raw_state"] == "full"
    assert compiled["summary_path"] == "wiki/sources/compiled.md"
    assert compiled["compiled_at"] == "2026-06-28T10:30:00+08:00"
    assert skipped["status"] == "skipped"
    assert skipped["raw_state"] == "full"
    assert skipped["skip_reason_code"] == "off-topic"
    assert skipped["skip_note"] == "不服务于主线问题"
    assert compile_registry.list_pending(registry) == []


def test_save_and_load_registry_round_trip(tmp_path):
    compile_registry = load_compile_registry()
    registry = {
        "version": 1,
        "updated_at": "2026-06-28T10:30:00+08:00",
        "items": {
            "example.md": {
                "raw_file": "example.md",
                "status": "pending",
                "body_sha256": body_sha256("body"),
                "updated_at": "2026-06-28T10:30:00+08:00",
            }
        },
    }

    compile_registry.save_registry(tmp_path, registry)
    loaded = compile_registry.load_registry(tmp_path)

    assert loaded == registry
    assert compile_registry.raw_state(loaded["items"]["example.md"]) == "full"
    assert json.loads((tmp_path / "state" / "raw-registry.json").read_text(encoding="utf-8"))["version"] == 1


def test_save_registry_rejects_invalid_status(tmp_path):
    compile_registry = load_compile_registry()
    registry = {
        "version": 1,
        "updated_at": "2026-06-28T10:30:00+08:00",
        "items": {
            "broken.md": {
                "raw_file": "broken.md",
                "status": "bogus",
                "body_sha256": body_sha256("body"),
                "updated_at": "2026-06-28T10:30:00+08:00",
            }
        },
    }

    try:
        compile_registry.save_registry(tmp_path, registry)
    except ValueError as exc:
        assert "invalid registry file" in str(exc)
    else:
        raise AssertionError("expected invalid status to be rejected on save")


def test_save_registry_rejects_invalid_raw_state(tmp_path):
    compile_registry = load_compile_registry()
    registry = {
        "version": 1,
        "updated_at": "2026-06-28T10:30:00+08:00",
        "items": {
            "broken.md": {
                "raw_file": "broken.md",
                "status": "compiled",
                "raw_state": "archived",
                "body_sha256": body_sha256("body"),
                "summary_path": "wiki/sources/broken.md",
                "updated_at": "2026-06-28T10:30:00+08:00",
            }
        },
    }

    try:
        compile_registry.save_registry(tmp_path, registry)
    except ValueError as exc:
        assert "invalid registry file" in str(exc)
    else:
        raise AssertionError("expected invalid raw state to be rejected on save")


def test_save_registry_validates_index_metadata_and_status(tmp_path):
    compile_registry = load_compile_registry()
    base = {
        "raw_file": "indexed.md",
        "status": "compiled",
        "raw_state": "index",
        "body_sha256": body_sha256("body"),
        "summary_path": "wiki/sources/indexed.md",
        "canonical_url": "https://example.com/indexed",
        "indexed_at": "2026-06-28T10:30:00+08:00",
        "updated_at": "2026-06-28T10:30:00+08:00",
    }
    registry = {"version": 1, "updated_at": base["updated_at"], "items": {"indexed.md": base}}
    compile_registry.save_registry(tmp_path, registry)
    assert compile_registry.load_registry(tmp_path)["items"]["indexed.md"]["raw_state"] == "index"

    for field in ("canonical_url", "indexed_at"):
        invalid = dict(base)
        invalid.pop(field)
        with_error = {"version": 1, "updated_at": base["updated_at"], "items": {"indexed.md": invalid}}
        try:
            compile_registry.save_registry(tmp_path, with_error)
        except ValueError as exc:
            assert "invalid registry file" in str(exc)
        else:
            raise AssertionError(f"expected missing {field} to be rejected")

    invalid_status = dict(base)
    invalid_status["status"] = "skipped"
    with_error = {"version": 1, "updated_at": base["updated_at"], "items": {"indexed.md": invalid_status}}
    try:
        compile_registry.save_registry(tmp_path, with_error)
    except ValueError as exc:
        assert "invalid registry file" in str(exc)
    else:
        raise AssertionError("expected non-compiled index to be rejected")


def test_save_registry_validates_removed_metadata(tmp_path):
    compile_registry = load_compile_registry()
    base = {
        "raw_file": "removed.md",
        "status": "skipped",
        "raw_state": "removed",
        "body_sha256": body_sha256("body"),
        "retired_at": "2026-06-28T10:30:00+08:00",
        "retire_reason": "重复来源",
        "updated_at": "2026-06-28T10:30:00+08:00",
    }
    registry = {"version": 1, "updated_at": base["updated_at"], "items": {"removed.md": base}}
    compile_registry.save_registry(tmp_path, registry)
    assert compile_registry.load_registry(tmp_path)["items"]["removed.md"]["raw_state"] == "removed"

    for field in ("retired_at", "retire_reason"):
        invalid = dict(base)
        invalid.pop(field)
        with_error = {"version": 1, "updated_at": base["updated_at"], "items": {"removed.md": invalid}}
        try:
            compile_registry.save_registry(tmp_path, with_error)
        except ValueError as exc:
            assert "invalid registry file" in str(exc)
        else:
            raise AssertionError(f"expected missing {field} to be rejected")


def test_load_registry_rejects_invalid_persisted_status(tmp_path):
    compile_registry = load_compile_registry()
    registry_path = tmp_path / "state" / "raw-registry.json"
    registry_path.parent.mkdir(parents=True, exist_ok=True)
    registry_path.write_text(
        json.dumps(
            {
                "version": 1,
                "updated_at": "2026-06-28T10:30:00+08:00",
                "items": {
                    "broken.md": {
                        "raw_file": "broken.md",
                        "status": "bogus",
                        "body_sha256": body_sha256("body"),
                        "updated_at": "2026-06-28T10:30:00+08:00",
                    }
                },
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    try:
        compile_registry.load_registry(tmp_path)
    except ValueError as exc:
        assert "invalid registry file" in str(exc)
    else:
        raise AssertionError("expected invalid persisted status to be rejected")


def test_bootstrap_registry_reads_legacy_compiled_signals(tmp_path):
    compile_registry = load_compile_registry()
    write_raw(tmp_path, "compiled.md", "type: raw\n", "body\n")
    write_summary(tmp_path, "compiled.md")
    write_raw(tmp_path, "pending.md", "type: raw\n", "todo\n")

    registry = compile_registry.bootstrap_registry(tmp_path, now="2026-06-28T11:00:00+08:00")

    assert registry["items"]["compiled.md"]["status"] == "compiled"
    assert registry["items"]["compiled.md"]["summary_path"] == "wiki/sources/compiled.md"
    assert registry["items"]["pending.md"]["status"] == "pending"


def test_bootstrap_registry_preserves_existing_index_and_removed_entries(tmp_path):
    compile_registry = load_compile_registry()
    registry_path = tmp_path / "state" / "raw-registry.json"
    registry_path.parent.mkdir(parents=True, exist_ok=True)
    existing = {
        "version": 1,
        "updated_at": "2026-06-28T10:30:00+08:00",
        "items": {
            "indexed.md": {
                "raw_file": "indexed.md",
                "status": "compiled",
                "raw_state": "index",
                "body_sha256": body_sha256("indexed body"),
                "summary_path": "wiki/sources/indexed.md",
                "canonical_url": "https://example.com/indexed",
                "indexed_at": "2026-06-28T10:00:00+08:00",
                "updated_at": "2026-06-28T10:00:00+08:00",
            },
            "removed.md": {
                "raw_file": "removed.md",
                "status": "skipped",
                "raw_state": "removed",
                "body_sha256": body_sha256("removed body"),
                "retired_at": "2026-06-28T10:05:00+08:00",
                "retire_reason": "重复来源",
                "updated_at": "2026-06-28T10:05:00+08:00",
            },
        },
    }
    registry_path.write_text(json.dumps(existing, ensure_ascii=False), encoding="utf-8")
    write_raw(tmp_path, "current.md", "type: raw\n", "body\n")

    bootstrapped = compile_registry.bootstrap_registry(tmp_path, now="2026-06-28T11:00:00+08:00")

    assert bootstrapped["items"]["indexed.md"] == existing["items"]["indexed.md"]
    assert bootstrapped["items"]["removed.md"] == existing["items"]["removed.md"]
    assert bootstrapped["items"]["current.md"]["raw_state"] == "full"


def test_reconcile_adds_new_raw_and_reports_recompile_candidates(tmp_path):
    compile_registry = load_compile_registry()
    compiled_raw = write_raw(tmp_path, "compiled.md", "type: raw\n", "original\n")
    write_summary(tmp_path, "compiled.md")
    registry = compile_registry.bootstrap_registry(tmp_path, now="2026-06-28T11:00:00+08:00")

    write_raw(tmp_path, "fresh.md", "type: raw\n", "new article\n")
    compiled_raw.write_text("---\ntype: raw\n---\n\nmutated\n", encoding="utf-8")

    reconciled, anomalies, candidates = compile_registry.reconcile_registry(
        tmp_path,
        registry=registry,
        now="2026-06-28T12:00:00+08:00",
    )

    assert reconciled["items"]["fresh.md"]["status"] == "pending"
    assert anomalies == []
    assert candidates == [{"raw_file": "compiled.md", "reason": "body-changed", "severity": "blocking"}]


def test_reconcile_surfaces_malformed_compiled_digest(tmp_path):
    compile_registry = load_compile_registry()
    write_raw(tmp_path, "compiled.md", "type: raw\n", "body\n")
    write_summary(tmp_path, "compiled.md")
    registry = {
        "version": 1,
        "updated_at": "2026-06-28T11:00:00+08:00",
        "items": {
            "compiled.md": {
                "raw_file": "compiled.md",
                "status": "compiled",
                "body_sha256": "abc",
                "summary_path": "wiki/sources/compiled.md",
                "compiled_at": "2026-06-28T11:00:00+08:00",
                "updated_at": "2026-06-28T11:00:00+08:00",
            }
        },
    }

    _, anomalies, candidates = compile_registry.reconcile_registry(
        tmp_path,
        registry=registry,
        now="2026-06-28T12:00:00+08:00",
    )

    assert {"raw_file": "compiled.md", "reason": "invalid-body-sha256"} in anomalies


def test_reconcile_allows_missing_index_and_removed_raw_files(tmp_path):
    compile_registry = load_compile_registry()
    write_summary(tmp_path, "indexed.md")
    registry = {
        "version": 1,
        "updated_at": "2026-06-28T11:00:00+08:00",
        "items": {
            "indexed.md": {
                "raw_file": "indexed.md",
                "status": "compiled",
                "raw_state": "index",
                "body_sha256": body_sha256("indexed body"),
                "summary_path": "wiki/sources/indexed.md",
                "canonical_url": "https://example.com/indexed",
                "indexed_at": "2026-06-28T10:00:00+08:00",
                "updated_at": "2026-06-28T10:00:00+08:00",
            },
            "removed.md": {
                "raw_file": "removed.md",
                "status": "skipped",
                "raw_state": "removed",
                "body_sha256": body_sha256("removed body"),
                "retired_at": "2026-06-28T10:05:00+08:00",
                "retire_reason": "重复来源",
                "updated_at": "2026-06-28T10:05:00+08:00",
            },
        },
    }

    reconciled, anomalies, candidates = compile_registry.reconcile_registry(
        tmp_path, registry=registry, now="2026-06-28T12:00:00+08:00"
    )

    assert reconciled["items"]["indexed.md"]["raw_state"] == "index"
    assert anomalies == []
    assert candidates == []


def test_reconcile_blocks_raw_files_present_for_index_or_removed_state(tmp_path):
    compile_registry = load_compile_registry()
    write_raw(tmp_path, "indexed.md", "type: raw\n", "body\n")
    write_raw(tmp_path, "removed.md", "type: raw\n", "body\n")
    registry = {
        "version": 1,
        "updated_at": "2026-06-28T11:00:00+08:00",
        "items": {
            "indexed.md": {
                "raw_file": "indexed.md",
                "status": "compiled",
                "raw_state": "index",
                "body_sha256": body_sha256("body"),
                "summary_path": "wiki/sources/indexed.md",
                "canonical_url": "https://example.com/indexed",
                "indexed_at": "2026-06-28T10:00:00+08:00",
                "updated_at": "2026-06-28T10:00:00+08:00",
            },
            "removed.md": {
                "raw_file": "removed.md",
                "status": "skipped",
                "raw_state": "removed",
                "body_sha256": body_sha256("body"),
                "retired_at": "2026-06-28T10:05:00+08:00",
                "retire_reason": "重复来源",
                "updated_at": "2026-06-28T10:05:00+08:00",
            },
        },
    }

    _, anomalies, candidates = compile_registry.reconcile_registry(
        tmp_path, registry=registry, now="2026-06-28T12:00:00+08:00"
    )

    assert candidates == []
    assert anomalies == [
        {"raw_file": "indexed.md", "reason": "raw-state-drift", "raw_state": "index"},
        {"raw_file": "removed.md", "reason": "raw-state-drift", "raw_state": "removed"},
    ]
    assert compile_registry.has_blocking_findings(candidates, anomalies)


def test_reconcile_keeps_skipped_digest_and_surfaces_review_candidate_on_body_change(tmp_path):
    compile_registry = load_compile_registry()
    skipped_raw = write_raw(tmp_path, "skipped.md", "type: raw\n", "original\n")
    original_digest = compile_registry.compute_body_sha256(skipped_raw)
    registry = {
        "version": 1,
        "updated_at": "2026-06-28T11:00:00+08:00",
        "items": {
            "skipped.md": {
                "raw_file": "skipped.md",
                "status": "skipped",
                "body_sha256": original_digest,
                "skip_reason_code": "off-topic",
                "skip_note": "skip it",
                "updated_at": "2026-06-28T11:00:00+08:00",
            }
        },
    }

    skipped_raw.write_text("---\ntype: raw\n---\n\nmutated\n", encoding="utf-8")

    reconciled, anomalies, candidates = compile_registry.reconcile_registry(
        tmp_path,
        registry=registry,
        now="2026-06-28T12:00:00+08:00",
    )

    assert anomalies == []
    assert candidates == [{"raw_file": "skipped.md", "reason": "skip-review-needed", "severity": "warning"}]
    assert reconciled["items"]["skipped.md"]["body_sha256"] == original_digest


def test_cli_ensure_and_mark_compiled_round_trip(tmp_path, capsys):
    compile_registry = load_compile_registry()
    write_raw(tmp_path, "article.md", "type: raw\n", "body\n")

    assert compile_registry.main(["--root", str(tmp_path), "ensure", "article.md"]) == 0
    assert compile_registry.main(
        [
            "--root",
            str(tmp_path),
            "mark-compiled",
            "article.md",
            "--summary-path",
            "wiki/sources/article.md",
        ]
    ) == 0

    registry = compile_registry.load_registry(tmp_path)
    captured = capsys.readouterr().out

    assert registry["items"]["article.md"]["status"] == "compiled"
    assert registry["items"]["article.md"]["summary_path"] == "wiki/sources/article.md"
    assert "article.md" in captured


def test_cli_mark_skipped_persists_reason_and_note(tmp_path):
    compile_registry = load_compile_registry()
    write_raw(tmp_path, "skip-me.md", "type: raw\n", "body\n")

    assert compile_registry.main(["--root", str(tmp_path), "ensure", "skip-me.md"]) == 0
    assert compile_registry.main(
        [
            "--root",
            str(tmp_path),
            "mark-skipped",
            "skip-me.md",
            "--reason-code",
            "off-topic",
            "--note",
            "不服务于 AI / Agent 工作主线",
        ]
    ) == 0

    registry = compile_registry.load_registry(tmp_path)

    assert registry["items"]["skip-me.md"]["status"] == "skipped"
    assert registry["items"]["skip-me.md"]["skip_reason_code"] == "off-topic"
    assert registry["items"]["skip-me.md"]["skip_note"] == "不服务于 AI / Agent 工作主线"


def test_set_raw_state_updates_registry_without_deleting_raw(tmp_path, capsys):
    compile_registry = load_compile_registry()
    raw_path = write_raw(tmp_path, "article.md", "type: raw\n", "body\n")
    summary_path = write_summary(tmp_path, "article.md")

    assert compile_registry.main(["--root", str(tmp_path), "ensure", "article.md"]) == 0
    assert compile_registry.main(
        [
            "--root",
            str(tmp_path),
            "mark-compiled",
            "article.md",
            "--summary-path",
            "wiki/sources/article.md",
        ]
    ) == 0
    original_digest = compile_registry.load_registry(tmp_path)["items"]["article.md"]["body_sha256"]

    assert compile_registry.main(
        [
            "--root",
            str(tmp_path),
            "set-raw-state",
            "article.md",
            "index",
            "--canonical-url",
            "https://example.com/article",
            "--indexed-at",
            "2026-06-28T12:00:00+08:00",
        ]
    ) == 0

    registry = compile_registry.load_registry(tmp_path)
    assert raw_path.exists()
    assert summary_path.exists()
    assert registry["items"]["article.md"]["raw_state"] == "index"
    assert registry["items"]["article.md"]["body_sha256"] == original_digest
    assert "set raw state article.md=index" in capsys.readouterr().out


def test_set_raw_state_removed_requires_metadata_and_does_not_touch_file(tmp_path):
    compile_registry = load_compile_registry()
    raw_path = write_raw(tmp_path, "article.md", "type: raw\n", "body\n")
    registry = {
        "version": 1,
        "updated_at": "2026-06-28T11:00:00+08:00",
        "items": {
            "article.md": {
                "raw_file": "article.md",
                "status": "compiled",
                "body_sha256": compile_registry.compute_body_sha256(raw_path),
                "summary_path": "wiki/sources/article.md",
                "updated_at": "2026-06-28T11:00:00+08:00",
            }
        },
    }
    compile_registry.save_registry(tmp_path, registry)

    try:
        compile_registry.main(["--root", str(tmp_path), "set-raw-state", "article.md", "removed"])
    except ValueError as exc:
        assert "invalid registry file" in str(exc)
    else:
        raise AssertionError("expected removed state metadata to be required")
    assert raw_path.exists()

    assert compile_registry.main(
        [
            "--root",
            str(tmp_path),
            "set-raw-state",
            "article.md",
            "removed",
            "--retired-at",
            "2026-06-28T12:00:00+08:00",
            "--retire-reason",
            "重复来源",
        ]
    ) == 0
    assert raw_path.exists()
    assert compile_registry.load_registry(tmp_path)["items"]["article.md"]["raw_state"] == "removed"


def test_render_status_includes_compile_and_raw_lifecycle_counts():
    compile_registry = load_compile_registry()
    registry = {
        "version": 1,
        "updated_at": "2026-06-28T11:00:00+08:00",
        "items": {
            "full.md": {"raw_file": "full.md", "status": "compiled"},
            "pending.md": {"raw_file": "pending.md", "status": "pending"},
            "indexed.md": {"raw_file": "indexed.md", "status": "compiled", "raw_state": "index"},
            "removed.md": {"raw_file": "removed.md", "status": "skipped", "raw_state": "removed"},
        },
    }

    status = compile_registry.render_status(registry, [], [])

    assert "pending=1 compiled=2 skipped=1" in status
    assert "raw_state=full:2 index:1 removed:1" in status


def test_cli_status_and_reconcile_exit_nonzero_for_blocking_compiled_candidates(tmp_path):
    compile_registry = load_compile_registry()
    compiled_raw = write_raw(tmp_path, "compiled.md", "type: raw\n", "body\n")
    write_summary(tmp_path, "compiled.md")

    assert compile_registry.main(["--root", str(tmp_path), "ensure", "compiled.md"]) == 0
    assert compile_registry.main(
        [
            "--root",
            str(tmp_path),
            "mark-compiled",
            "compiled.md",
            "--summary-path",
            "wiki/sources/compiled.md",
        ]
    ) == 0

    compiled_raw.write_text("---\ntype: raw\n---\n\nmutated\n", encoding="utf-8")

    assert compile_registry.main(["--root", str(tmp_path), "status"]) == 1
    assert compile_registry.main(["--root", str(tmp_path), "reconcile"]) == 1
