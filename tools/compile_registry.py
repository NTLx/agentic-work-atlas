#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALID_STATUS = {"pending", "compiled", "skipped"}


def registry_path(root: Path = ROOT) -> Path:
    return root / "state" / "raw-registry.json"


def now_iso() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def raw_body_text(raw_path: Path) -> str:
    text = raw_path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].rstrip("\r\n") != "---":
        return text

    offset = len(lines[0])
    for line in lines[1:]:
        offset += len(line)
        if line.rstrip("\r\n") == "---":
            return text[offset:].lstrip("\r\n")
    return text


def compute_body_sha256(raw_path: Path) -> str:
    return hashlib.sha256(raw_body_text(raw_path).encode("utf-8")).hexdigest()


def expected_summary_path(raw_file: str) -> str:
    return f"wiki/sources/{Path(raw_file).stem}.md"


def empty_registry(now: str | None = None) -> dict:
    stamp = now or now_iso()
    return {"version": 1, "updated_at": stamp, "items": {}}


def _validate_registry(registry: dict, path: Path) -> None:
    if not isinstance(registry, dict) or not isinstance(registry.get("items"), dict):
        raise ValueError(f"invalid registry file: {path}")

    for raw_file, entry in registry["items"].items():
        if not isinstance(entry, dict):
            raise ValueError(f"invalid registry file: {path}")
        status = entry.get("status")
        if status not in VALID_STATUS:
            raise ValueError(f"invalid registry file: {path}")
        if entry.get("raw_file") != raw_file:
            raise ValueError(f"invalid registry file: {path}")


def load_registry(root: Path = ROOT) -> dict:
    path = registry_path(root)
    if not path.exists():
        return empty_registry()
    data = json.loads(path.read_text(encoding="utf-8"))
    _validate_registry(data, path)
    data.setdefault("version", 1)
    data.setdefault("updated_at", now_iso())
    return data


def save_registry(root: Path, registry: dict) -> None:
    path = registry_path(root)
    _validate_registry(registry, path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(registry, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def mark_compiled(registry: dict, raw_file: str, summary_path: str, body_sha256: str, now: str) -> dict:
    entry = {
        "raw_file": raw_file,
        "status": "compiled",
        "body_sha256": body_sha256,
        "summary_path": summary_path,
        "compiled_at": now,
        "updated_at": now,
    }
    registry["items"][raw_file] = entry
    registry["updated_at"] = now
    return entry


def mark_skipped(registry: dict, raw_file: str, reason_code: str, note: str, body_sha256: str, now: str) -> dict:
    entry = {
        "raw_file": raw_file,
        "status": "skipped",
        "body_sha256": body_sha256,
        "skip_reason_code": reason_code,
        "skip_note": note,
        "updated_at": now,
    }
    registry["items"][raw_file] = entry
    registry["updated_at"] = now
    return entry


def list_pending(registry: dict) -> list[str]:
    return sorted(
        raw_file
        for raw_file, entry in registry.get("items", {}).items()
        if entry.get("status", "pending") == "pending"
    )


def detect_legacy_compiled(raw_path: Path, root: Path) -> bool:
    text = raw_path.read_text(encoding="utf-8", errors="replace")
    compiled_note = root / "wiki" / "sources" / raw_path.name
    return "## 编译摘要" in text or compiled_note.exists()


def bootstrap_registry(root: Path = ROOT, now: str | None = None) -> dict:
    stamp = now or now_iso()
    registry = empty_registry(stamp)
    for raw_path in sorted((root / "raw").glob("*.md")):
        body_sha256 = compute_body_sha256(raw_path)
        if detect_legacy_compiled(raw_path, root):
            mark_compiled(
                registry,
                raw_file=raw_path.name,
                summary_path=expected_summary_path(raw_path.name),
                body_sha256=body_sha256,
                now=stamp,
            )
        else:
            registry["items"][raw_path.name] = {
                "raw_file": raw_path.name,
                "status": "pending",
                "body_sha256": body_sha256,
                "updated_at": stamp,
            }
    registry["updated_at"] = stamp
    return registry


def reconcile_registry(
    root: Path = ROOT, registry: dict | None = None, now: str | None = None
) -> tuple[dict, list[dict], list[dict]]:
    stamp = now or now_iso()
    registry = registry or load_registry(root)
    anomalies: list[dict] = []
    candidates: list[dict] = []
    raw_paths = {path.name: path for path in sorted((root / "raw").glob("*.md"))}

    for raw_file, raw_path in raw_paths.items():
        entry = registry["items"].get(raw_file)
        current_digest = compute_body_sha256(raw_path)
        if entry is None:
            registry["items"][raw_file] = {
                "raw_file": raw_file,
                "status": "pending",
                "body_sha256": current_digest,
                "updated_at": stamp,
            }
            continue
        if entry.get("status") == "compiled":
            if entry.get("body_sha256") != current_digest:
                candidates.append({"raw_file": raw_file, "reason": "body-changed"})
            summary_path = root / entry.get("summary_path", "")
            if not entry.get("summary_path") or not summary_path.exists():
                candidates.append({"raw_file": raw_file, "reason": "missing-summary"})
        else:
            entry["body_sha256"] = current_digest
            entry["updated_at"] = stamp

    for raw_file in sorted(registry["items"]):
        if raw_file not in raw_paths:
            anomalies.append({"raw_file": raw_file, "reason": "missing-raw"})

    registry["updated_at"] = stamp
    return registry, anomalies, candidates


def render_status(registry: dict, recompile_candidates: list[dict], anomalies: list[dict]) -> str:
    counts = {"pending": 0, "compiled": 0, "skipped": 0}
    for entry in registry.get("items", {}).values():
        status = entry.get("status", "pending")
        counts[status] = counts.get(status, 0) + 1

    lines = [
        "Raw Compile Registry",
        "=" * 60,
        f"pending={counts.get('pending', 0)} compiled={counts.get('compiled', 0)} skipped={counts.get('skipped', 0)}",
    ]
    if recompile_candidates:
        lines.append("recompile-candidates:")
        lines.extend(f"- {item['raw_file']} ({item['reason']})" for item in recompile_candidates)
    if anomalies:
        lines.append("anomalies:")
        lines.extend(f"- {item['raw_file']} ({item['reason']})" for item in anomalies)
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Manage raw compile registry")
    parser.add_argument("--root", type=Path, default=ROOT, help="Repository root")
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("bootstrap", help="Bootstrap registry from legacy raw/wiki signals")
    subparsers.add_parser("reconcile", help="Reconcile registry against filesystem")
    subparsers.add_parser("status", help="Show registry counts and recompile candidates")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "bootstrap":
        registry = bootstrap_registry(args.root)
        save_registry(args.root, registry)
        print(f"bootstrapped {len(registry['items'])} raw entries")
        return 0

    registry = load_registry(args.root)
    registry, anomalies, candidates = reconcile_registry(args.root, registry=registry)
    if args.command == "reconcile":
        save_registry(args.root, registry)
        print(render_status(registry, candidates, anomalies))
        return 1 if anomalies else 0

    print(render_status(registry, candidates, anomalies))
    return 1 if anomalies else 0


if __name__ == "__main__":
    raise SystemExit(main())
