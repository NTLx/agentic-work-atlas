#!/usr/bin/env python3
from __future__ import annotations

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

    block_scalar_indent: int | None = None
    offset = len(lines[0])
    for line_index, line in enumerate(lines[1:], start=1):
        stripped = line.rstrip("\r\n")
        indent = len(line) - len(line.lstrip(" "))

        if block_scalar_indent is not None:
            if stripped == "---" and _block_scalar_separator_is_content(lines, line_index, block_scalar_indent):
                offset += len(line)
                continue
            if stripped and indent <= block_scalar_indent:
                block_scalar_indent = None
            else:
                offset += len(line)
                continue

        if stripped == "---":
            return text[offset + len(line) :].lstrip("\r\n")

        if _starts_block_scalar(stripped):
            block_scalar_indent = indent

        offset += len(line)
    return text


def compute_body_sha256(raw_path: Path) -> str:
    return hashlib.sha256(raw_body_text(raw_path).encode("utf-8")).hexdigest()


def expected_summary_path(raw_file: str) -> str:
    return f"wiki/sources/{Path(raw_file).stem}.md"


def empty_registry(now: str | None = None) -> dict:
    stamp = now or now_iso()
    return {"version": 1, "updated_at": stamp, "items": {}}


def _starts_block_scalar(line: str) -> bool:
    if ":" not in line:
        return False
    key, value = line.split(":", 1)
    if not key.strip() or "#" in key:
        return False
    value = value.lstrip()
    return value.startswith("|") or value.startswith(">")


def _block_scalar_separator_is_content(lines: list[str], separator_index: int, block_scalar_indent: int) -> bool:
    for line in lines[separator_index + 1 :]:
        stripped = line.rstrip("\r\n")
        if not stripped:
            continue
        indent = len(line) - len(line.lstrip(" "))
        if indent <= block_scalar_indent:
            return ":" in stripped and not stripped.startswith("#")
    return False


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
