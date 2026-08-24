#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALID_STATUS = {"pending", "compiled", "skipped"}
VALID_RAW_STATE = {"full", "index", "removed"}
CANDIDATE_SEVERITY = {
    "body-changed": "blocking",
    "missing-summary": "blocking",
    "skip-review-needed": "warning",
}


def registry_path(root: Path = ROOT) -> Path:
    return root / "state" / "raw-registry.json"


def now_iso() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def is_binary_raw(raw_path: Path) -> bool:
    return raw_path.suffix.lower() in (".pdf",)


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
    if is_binary_raw(raw_path):
        return hashlib.sha256(raw_path.read_bytes()).hexdigest()
    return hashlib.sha256(raw_body_text(raw_path).encode("utf-8")).hexdigest()


def raw_files(root: Path = ROOT) -> list[Path]:
    """Return all trackable raw files (markdown + supported binary formats)."""
    raw_dir = root / "raw"
    files = sorted(raw_dir.glob("*.md"))
    files.extend(sorted(raw_dir.glob("*.pdf")))
    return files


def expected_summary_path(raw_file: str) -> str:
    return f"wiki/sources/{Path(raw_file).stem}.md"


def is_sha256_digest(value: str) -> bool:
    return len(value) == 64 and all(char in "0123456789abcdef" for char in value)


def is_http_url(value: str) -> bool:
    return value.startswith(("https://", "http://")) and len(value.split("://", 1)[1]) > 0


def is_iso_timestamp(value: str) -> bool:
    try:
        datetime.fromisoformat(value)
    except (TypeError, ValueError):
        return False
    return True


def candidate_severity(reason: str) -> str:
    return CANDIDATE_SEVERITY.get(reason, "blocking")


def make_candidate(raw_file: str, reason: str) -> dict:
    return {"raw_file": raw_file, "reason": reason, "severity": candidate_severity(reason)}


def raw_state(entry: dict) -> str:
    """Return the retention state, preserving compatibility with v1 entries."""
    return entry.get("raw_state", "full")


def has_blocking_findings(candidates: list[dict], anomalies: list[dict]) -> bool:
    return bool(anomalies) or any(item.get("severity") == "blocking" for item in candidates)


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
        state = raw_state(entry)
        if state not in VALID_RAW_STATE:
            raise ValueError(f"invalid registry file: {path}")
        if state == "index":
            if status != "compiled":
                raise ValueError(f"invalid registry file: {path}")
            if not is_sha256_digest(entry.get("body_sha256", "")):
                raise ValueError(f"invalid registry file: {path}")
            if not isinstance(entry.get("summary_path"), str) or not entry["summary_path"]:
                raise ValueError(f"invalid registry file: {path}")
            if not isinstance(entry.get("canonical_url"), str) or not is_http_url(entry["canonical_url"]):
                raise ValueError(f"invalid registry file: {path}")
            if not isinstance(entry.get("indexed_at"), str) or not is_iso_timestamp(entry["indexed_at"]):
                raise ValueError(f"invalid registry file: {path}")
        elif state == "removed":
            if status == "pending" or not is_sha256_digest(entry.get("body_sha256", "")):
                raise ValueError(f"invalid registry file: {path}")
            if not isinstance(entry.get("retired_at"), str) or not is_iso_timestamp(entry["retired_at"]):
                raise ValueError(f"invalid registry file: {path}")
            if not isinstance(entry.get("retire_reason"), str) or not entry["retire_reason"].strip():
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
        "raw_state": "full",
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
        "raw_state": "full",
        "body_sha256": body_sha256,
        "skip_reason_code": reason_code,
        "skip_note": note,
        "updated_at": now,
    }
    registry["items"][raw_file] = entry
    registry["updated_at"] = now
    return entry


def ensure_entry(registry: dict, raw_file: str, body_sha256: str, now: str) -> dict:
    entry = registry["items"].get(raw_file)
    if entry is None:
        entry = {
            "raw_file": raw_file,
            "status": "pending",
            "raw_state": "full",
            "body_sha256": body_sha256,
            "updated_at": now,
        }
        registry["items"][raw_file] = entry
    elif raw_state(entry) != "full":
        raise ValueError(f"raw lifecycle record already exists: {raw_file}={raw_state(entry)}")
    elif entry.get("status") == "pending":
        entry["body_sha256"] = body_sha256
        entry["updated_at"] = now
    registry["updated_at"] = now
    return entry


def list_pending(registry: dict) -> list[str]:
    return sorted(
        raw_file
        for raw_file, entry in registry.get("items", {}).items()
        if entry.get("status", "pending") == "pending"
    )


def set_raw_state(
    registry: dict,
    raw_file: str,
    state: str,
    *,
    canonical_url: str | None = None,
    indexed_at: str | None = None,
    retired_at: str | None = None,
    retire_reason: str | None = None,
    archive_uri: str | None = None,
    retention_note: str | None = None,
    now: str,
) -> dict:
    """Update retention metadata without touching the raw file on disk."""
    if state not in VALID_RAW_STATE:
        raise ValueError(f"invalid raw state: {state}")
    entry = registry["items"].get(raw_file)
    if entry is None:
        raise ValueError(f"raw registry entry not found: {raw_file}")

    entry["raw_state"] = state
    if canonical_url is not None:
        entry["canonical_url"] = canonical_url
    if indexed_at is not None:
        entry["indexed_at"] = indexed_at
    if retired_at is not None:
        entry["retired_at"] = retired_at
    if retire_reason is not None:
        entry["retire_reason"] = retire_reason
    if archive_uri is not None:
        entry["archive_uri"] = archive_uri
    if retention_note is not None:
        entry["retention_note"] = retention_note
    entry["updated_at"] = now
    registry["updated_at"] = now
    return entry


def detect_legacy_compiled(raw_path: Path, root: Path) -> bool:
    compiled_note = root / expected_summary_path(raw_path.name)
    if compiled_note.exists():
        return True
    if is_binary_raw(raw_path):
        return False
    text = raw_path.read_text(encoding="utf-8", errors="replace")
    return "## 编译摘要" in text


def bootstrap_registry(root: Path = ROOT, now: str | None = None) -> dict:
    stamp = now or now_iso()
    existing = load_registry(root) if registry_path(root).exists() else None
    registry = empty_registry(stamp)
    for raw_path in raw_files(root):
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
                "raw_state": "full",
                "body_sha256": body_sha256,
                "updated_at": stamp,
            }
    if existing:
        for raw_file, entry in existing.get("items", {}).items():
            if raw_state(entry) in {"index", "removed"}:
                registry["items"][raw_file] = dict(entry)
    registry["updated_at"] = stamp
    return registry


def reconcile_registry(
    root: Path = ROOT, registry: dict | None = None, now: str | None = None
) -> tuple[dict, list[dict], list[dict]]:
    stamp = now or now_iso()
    registry = registry or load_registry(root)
    anomalies: list[dict] = []
    candidates: list[dict] = []
    raw_paths = {path.name: path for path in raw_files(root)}

    for raw_file, raw_path in raw_paths.items():
        entry = registry["items"].get(raw_file)
        current_digest = compute_body_sha256(raw_path)
        if entry is None:
            registry["items"][raw_file] = {
                "raw_file": raw_file,
                "status": "pending",
                "raw_state": "full",
                "body_sha256": current_digest,
                "updated_at": stamp,
            }
            continue
        if raw_state(entry) != "full":
            anomalies.append(
                {
                    "raw_file": raw_file,
                    "reason": "raw-state-drift",
                    "raw_state": raw_state(entry),
                }
            )
            continue
        if entry.get("status") == "compiled":
            stored_digest = entry.get("body_sha256", "")
            if not is_sha256_digest(stored_digest):
                anomalies.append({"raw_file": raw_file, "reason": "invalid-body-sha256"})
            elif stored_digest != current_digest:
                candidates.append(make_candidate(raw_file, "body-changed"))
            summary_path = root / entry.get("summary_path", "")
            if not entry.get("summary_path") or not summary_path.exists():
                candidates.append(make_candidate(raw_file, "missing-summary"))
        elif entry.get("status") == "pending":
            entry["body_sha256"] = current_digest
            entry["updated_at"] = stamp
        elif entry.get("status") == "skipped":
            stored_digest = entry.get("body_sha256", "")
            if is_sha256_digest(stored_digest) and stored_digest != current_digest:
                candidates.append(make_candidate(raw_file, "skip-review-needed"))

    for raw_file in sorted(registry["items"]):
        if raw_file not in raw_paths:
            entry = registry["items"][raw_file]
            state = raw_state(entry)
            if state == "index":
                summary_path = root / entry.get("summary_path", "")
                if not entry.get("summary_path") or not summary_path.exists():
                    candidates.append(make_candidate(raw_file, "missing-summary"))
            elif state != "removed":
                anomalies.append({"raw_file": raw_file, "reason": "missing-raw"})

    registry["updated_at"] = stamp
    return registry, anomalies, candidates


def render_status(registry: dict, recompile_candidates: list[dict], anomalies: list[dict]) -> str:
    counts = {"pending": 0, "compiled": 0, "skipped": 0}
    raw_state_counts = {state: 0 for state in VALID_RAW_STATE}
    for entry in registry.get("items", {}).values():
        status = entry.get("status", "pending")
        counts[status] = counts.get(status, 0) + 1
        state = raw_state(entry)
        raw_state_counts[state] = raw_state_counts.get(state, 0) + 1

    lines = [
        "Raw Compile Registry",
        "=" * 60,
        f"pending={counts.get('pending', 0)} compiled={counts.get('compiled', 0)} skipped={counts.get('skipped', 0)}",
        f"raw_state=full:{raw_state_counts['full']} index:{raw_state_counts['index']} removed:{raw_state_counts['removed']}",
    ]
    if recompile_candidates:
        lines.append("recompile-candidates:")
        lines.extend(
            f"- {item['raw_file']} ({item['reason']}, severity={item.get('severity', candidate_severity(item['reason']))})"
            for item in recompile_candidates
        )
    if anomalies:
        lines.append("anomalies:")
        lines.extend(f"- {item['raw_file']} ({item['reason']})" for item in anomalies)
    return "\n".join(lines)


def raw_path_for(root: Path, raw_file: str) -> Path:
    return root / "raw" / raw_file


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Manage raw compile registry")
    parser.add_argument("--root", type=Path, default=ROOT, help="Repository root")
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("bootstrap", help="Bootstrap registry from legacy raw/wiki signals")
    subparsers.add_parser("reconcile", help="Reconcile registry against filesystem")
    subparsers.add_parser("status", help="Show registry counts and recompile candidates")

    ensure = subparsers.add_parser("ensure", help="Ensure a raw file exists in the registry as pending")
    ensure.add_argument("raw_file")

    mark_compiled_parser = subparsers.add_parser("mark-compiled", help="Persist a compiled raw entry")
    mark_compiled_parser.add_argument("raw_file")
    mark_compiled_parser.add_argument("--summary-path", required=True)

    mark_skipped_parser = subparsers.add_parser("mark-skipped", help="Persist a skipped raw entry")
    mark_skipped_parser.add_argument("raw_file")
    mark_skipped_parser.add_argument("--reason-code", required=True)
    mark_skipped_parser.add_argument("--note", required=True)

    set_state_parser = subparsers.add_parser(
        "set-raw-state", help="Update raw retention state without modifying files"
    )
    set_state_parser.add_argument("raw_file")
    set_state_parser.add_argument("state", choices=("index", "removed"))
    set_state_parser.add_argument("--canonical-url")
    set_state_parser.add_argument("--indexed-at")
    set_state_parser.add_argument("--retired-at")
    set_state_parser.add_argument("--retire-reason")
    set_state_parser.add_argument("--archive-uri")
    set_state_parser.add_argument("--retention-note")
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
    if args.command == "ensure":
        raw_path = raw_path_for(args.root, args.raw_file)
        ensure_entry(registry, args.raw_file, body_sha256=compute_body_sha256(raw_path), now=now_iso())
        save_registry(args.root, registry)
        print(f"ensured {args.raw_file}")
        return 0

    if args.command == "mark-compiled":
        raw_path = raw_path_for(args.root, args.raw_file)
        mark_compiled(
            registry,
            raw_file=args.raw_file,
            summary_path=args.summary_path,
            body_sha256=compute_body_sha256(raw_path),
            now=now_iso(),
        )
        save_registry(args.root, registry)
        print(f"compiled {args.raw_file}")
        return 0

    if args.command == "mark-skipped":
        raw_path = raw_path_for(args.root, args.raw_file)
        mark_skipped(
            registry,
            raw_file=args.raw_file,
            reason_code=args.reason_code,
            note=args.note,
            body_sha256=compute_body_sha256(raw_path),
            now=now_iso(),
        )
        save_registry(args.root, registry)
        print(f"skipped {args.raw_file}")
        return 0

    if args.command == "set-raw-state":
        set_raw_state(
            registry,
            raw_file=args.raw_file,
            state=args.state,
            canonical_url=args.canonical_url,
            indexed_at=args.indexed_at,
            retired_at=args.retired_at,
            retire_reason=args.retire_reason,
            archive_uri=args.archive_uri,
            retention_note=args.retention_note,
            now=now_iso(),
        )
        save_registry(args.root, registry)
        print(f"set raw state {args.raw_file}={args.state}")
        return 0

    registry, anomalies, candidates = reconcile_registry(args.root, registry=registry)
    if args.command == "reconcile":
        save_registry(args.root, registry)
        print(render_status(registry, candidates, anomalies))
        return 1 if has_blocking_findings(candidates, anomalies) else 0

    print(render_status(registry, candidates, anomalies))
    return 1 if has_blocking_findings(candidates, anomalies) else 0


if __name__ == "__main__":
    raise SystemExit(main())
