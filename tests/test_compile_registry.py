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
