import importlib.util
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
        body_sha256="abc123",
        now="2026-06-28T10:30:00+08:00",
    )
    skipped = compile_registry.mark_skipped(
        registry,
        raw_file="skipped.md",
        reason_code="off-topic",
        note="不服务于主线问题",
        body_sha256="def456",
        now="2026-06-28T10:35:00+08:00",
    )

    assert compiled["status"] == "compiled"
    assert compiled["summary_path"] == "wiki/sources/compiled.md"
    assert compiled["compiled_at"] == "2026-06-28T10:30:00+08:00"
    assert skipped["status"] == "skipped"
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
                "body_sha256": "abc123",
                "updated_at": "2026-06-28T10:30:00+08:00",
            }
        },
    }

    compile_registry.save_registry(tmp_path, registry)
    loaded = compile_registry.load_registry(tmp_path)

    assert loaded == registry
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
                "body_sha256": "abc123",
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
                        "body_sha256": "abc123",
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
    assert candidates == [{"raw_file": "compiled.md", "reason": "body-changed"}]


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
