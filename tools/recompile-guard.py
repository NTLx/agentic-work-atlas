#!/usr/bin/env python3
"""Guards and serializes unattended recompile runs.

The default command checks the complete working tree against a git revision,
including staged, unstaged, and untracked files.  The ``lock`` subcommand is
an intentionally small lease lock for schedulers that may overlap runs.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass
from datetime import date
from pathlib import Path, PurePosixPath
from typing import Iterable, Sequence


DEFAULT_LOCK_PATH = Path(f"/run/user/{os.getuid()}/agentic-work-atlas-recompile.lock")
AGENDA_PATH = "wiki/research/research-agenda.md"
LINT_PATHS = {"index.md", "wiki/lint-report.md"}
STABLE_PREFIXES = ("wiki/entities/", "wiki/topics/", "wiki/comparisons/")
AGENDA_MAX_BYTES = 60 * 1024
AGENDA_MAX_LINES = 300
AGENDA_MAX_LINE_LENGTH = 600
AGENDA_MAX_ACTIVE_CLAIMS = 12
LOG_MAX_ADDED_LINES = 80
LOG_MAX_ADDED_BYTES = 16 * 1024
LOG_MAX_ADDED_LINE_LENGTH = 600


@dataclass(frozen=True)
class Change:
    path: str
    status: str
    old_path: str | None = None


class GuardError(RuntimeError):
    """An expected guard or lock failure."""


def _run_git(repo: Path, args: Sequence[str], *, check: bool = True) -> bytes:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=repo,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
    except OSError as exc:
        raise GuardError(f"无法执行 git: {exc}") from exc
    if check and result.returncode != 0:
        detail = result.stderr.decode("utf-8", errors="replace").strip()
        raise GuardError(f"git {' '.join(args)} 失败{': ' + detail if detail else ''}")
    return result.stdout


def resolve_repo(repo_arg: str | Path) -> Path:
    requested = Path(repo_arg).resolve()
    output = _run_git(requested, ["rev-parse", "--show-toplevel"])
    return Path(output.decode("utf-8").strip()).resolve()


def _parse_diff_z(data: bytes) -> list[Change]:
    tokens = data.split(b"\0")
    changes: list[Change] = []
    index = 0
    while index < len(tokens) and tokens[index]:
        status = tokens[index].decode("utf-8", errors="replace")
        index += 1
        if index >= len(tokens):
            break
        first = tokens[index].decode("utf-8", errors="surrogateescape")
        index += 1
        if status.startswith(("R", "C")):
            if index >= len(tokens):
                raise GuardError("git diff 返回了不完整的 rename/copy 记录")
            second = tokens[index].decode("utf-8", errors="surrogateescape")
            index += 1
            changes.append(Change(path=second, status=status, old_path=first))
        else:
            changes.append(Change(path=first, status=status))
    return changes


def collect_changes(repo: Path, base: str = "HEAD") -> list[Change]:
    """Return tracked changes from *base* plus untracked non-ignored files."""

    changes = _parse_diff_z(
        _run_git(repo, ["diff", "--name-status", "--find-renames", "-z", base, "--"])
    )
    tracked = {change.path for change in changes}
    untracked = _run_git(repo, ["ls-files", "--others", "--exclude-standard", "-z"])
    for raw_path in untracked.split(b"\0"):
        if not raw_path:
            continue
        path = raw_path.decode("utf-8", errors="surrogateescape")
        if path not in tracked:
            changes.append(Change(path=path, status="A"))
    return changes


def _base_contains(repo: Path, base: str, path: str) -> bool:
    try:
        result = subprocess.run(
            ["git", "cat-file", "-e", f"{base}:{path}"],
            cwd=repo,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
    except OSError as exc:
        raise GuardError(f"无法检查 git 基线: {exc}") from exc
    return result.returncode == 0


def _is_stable(path: str) -> bool:
    return path.startswith(STABLE_PREFIXES) and path.endswith(".md")


def _is_transcript(path: str) -> bool:
    lowered = path.lower()
    parts = [part.lower() for part in PurePosixPath(path).parts]
    return (
        "documents/notes" in lowered
        or any(part in {"transcript", "transcripts"} for part in parts)
        or "transcript" in PurePosixPath(path).name.lower()
    )


def validate_changes(
    repo: Path,
    changes: Iterable[Change],
    *,
    base: str = "HEAD",
    log_date: str | None = None,
    max_stable: int = 0,
    allow_maintenance: bool = False,
) -> list[str]:
    """Return policy violations for a recompile change set."""

    if max_stable < 0:
        raise GuardError("max-stable 不能为负数")
    expected_date = log_date or date.today().isoformat()
    try:
        date.fromisoformat(expected_date)
    except ValueError as exc:
        raise GuardError(f"日志日期格式无效，应为 YYYY-MM-DD: {expected_date}") from exc

    expected_log = f"wiki/research/research-logs/{expected_date}.md"
    errors: list[str] = []
    stable_paths: set[str] = set()
    seen: set[tuple[str, str, str | None]] = set()

    for change in changes:
        key = (change.path, change.status, change.old_path)
        if key in seen:
            continue
        seen.add(key)
        paths = [change.path]
        if change.old_path:
            paths.append(change.old_path)

        for path in paths:
            if path.startswith("raw/"):
                errors.append(f"禁止修改 raw/: {path}")
            if _is_transcript(path):
                errors.append(f"禁止将 transcript/Notes 纳入仓库 diff: {path}")

        path = change.path
        if _is_stable(path):
            stable_paths.add(path)
            if not _base_contains(repo, base, path):
                errors.append(f"禁止新增稳定 Wiki 页面: {path}")
            elif change.status != "M":
                errors.append(f"稳定 Wiki 只能修改已有页面，禁止 {change.status}: {path}")
            continue

        allowed = path in {expected_log, AGENDA_PATH} or (
            allow_maintenance and path in LINT_PATHS
        )
        if not allowed:
            errors.append(f"本轮不允许修改路径: {path}")
        elif path == expected_log:
            if change.status not in {"A", "M"}:
                errors.append(f"当日日志只能新增或修改，禁止 {change.status}: {path}")
        elif change.status not in ({"A", "M"} if path in LINT_PATHS else {"M"}):
            errors.append(f"维护文件只能新增或修改，禁止 {change.status}: {path}")

        if change.old_path:
            errors.append(f"禁止 rename/copy 文件: {change.old_path} -> {change.path}")

    if len(stable_paths) > max_stable:
        errors.append(
            f"稳定 Wiki 本轮最多修改 {max_stable} 个页面: "
            + ", ".join(sorted(stable_paths))
        )
    return errors


def _read_utf8(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise GuardError(f"无法按 UTF-8 读取 {path}: {exc}") from exc


def _added_lines(repo: Path, base: str, path: str) -> list[str]:
    target = repo / path
    if not _base_contains(repo, base, path):
        return _read_utf8(target).splitlines()

    diff = _run_git(
        repo,
        ["diff", "--no-ext-diff", "--no-color", "--unified=0", base, "--", path],
    ).decode("utf-8", errors="replace")
    added: list[str] = []
    in_hunk = False
    for line in diff.splitlines():
        if line.startswith("@@"):
            in_hunk = True
        elif line.startswith("diff --git"):
            in_hunk = False
        elif in_hunk and line.startswith("+"):
            added.append(line[1:])
    return added


def validate_research_shape(
    repo: Path,
    changes: Iterable[Change],
    *,
    base: str,
    expected_log: str,
) -> list[str]:
    """Validate compactness constraints that keep scheduled output bounded."""

    changed_paths = {change.path for change in changes}
    errors: list[str] = []

    if AGENDA_PATH in changed_paths and (repo / AGENDA_PATH).is_file():
        try:
            agenda_bytes = (repo / AGENDA_PATH).read_bytes()
        except OSError as exc:
            raise GuardError(f"无法读取 {AGENDA_PATH}: {exc}") from exc
        try:
            agenda = agenda_bytes.decode("utf-8")
        except UnicodeError as exc:
            raise GuardError(f"无法按 UTF-8 读取 {AGENDA_PATH}: {exc}") from exc
        lines = agenda.splitlines()
        if len(agenda_bytes) > AGENDA_MAX_BYTES:
            errors.append(
                f"research agenda 超过 {AGENDA_MAX_BYTES // 1024} KB: "
                f"{len(agenda_bytes)} bytes"
            )
        if len(lines) > AGENDA_MAX_LINES:
            errors.append(
                f"research agenda 超过 {AGENDA_MAX_LINES} 行: {len(lines)} 行"
            )
        longest = max((len(line) for line in lines), default=0)
        if longest > AGENDA_MAX_LINE_LENGTH:
            errors.append(
                f"research agenda 单行超过 {AGENDA_MAX_LINE_LENGTH} 字符: "
                f"最长 {longest} 字符"
            )
        active_claims = sum(
            1 for line in lines if re.match(r"^### CR-\d+\b", line)
        )
        if active_claims > AGENDA_MAX_ACTIVE_CLAIMS:
            errors.append(
                f"Claim Recompile Queue 超过 {AGENDA_MAX_ACTIVE_CLAIMS} 条: "
                f"{active_claims} 条"
            )

    if expected_log in changed_paths and (repo / expected_log).is_file():
        added = _added_lines(repo, base, expected_log)
        added_bytes = sum(len(line.encode("utf-8")) + 1 for line in added)
        longest = max((len(line) for line in added), default=0)
        if len(added) > LOG_MAX_ADDED_LINES:
            errors.append(
                f"本轮研究日志新增超过 {LOG_MAX_ADDED_LINES} 行: {len(added)} 行"
            )
        if added_bytes > LOG_MAX_ADDED_BYTES:
            errors.append(
                f"本轮研究日志新增超过 {LOG_MAX_ADDED_BYTES // 1024} KB: "
                f"{added_bytes} bytes"
            )
        if longest > LOG_MAX_ADDED_LINE_LENGTH:
            errors.append(
                f"本轮研究日志新增单行超过 {LOG_MAX_ADDED_LINE_LENGTH} 字符: "
                f"最长 {longest} 字符"
            )

    return errors


def run_guard(
    repo_arg: str | Path = ".",
    *,
    base: str = "HEAD",
    log_date: str | None = None,
    max_stable: int = 0,
    allow_maintenance: bool = False,
) -> tuple[list[Change], list[str]]:
    repo = resolve_repo(repo_arg)
    changes = collect_changes(repo, base)
    errors = validate_changes(
        repo,
        changes,
        base=base,
        log_date=log_date,
        max_stable=max_stable,
        allow_maintenance=allow_maintenance,
    )
    expected_date = log_date or date.today().isoformat()
    errors.extend(
        validate_research_shape(
            repo,
            changes,
            base=base,
            expected_log=f"wiki/research/research-logs/{expected_date}.md",
        )
    )
    return changes, errors


def _owner_path(lock_path: Path) -> Path:
    return lock_path / "owner.json"


def _read_owner(lock_path: Path) -> dict[str, object]:
    path = _owner_path(lock_path)
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise GuardError(f"锁存在但缺少已知 owner 文件: {lock_path}") from exc
    except (OSError, json.JSONDecodeError) as exc:
        raise GuardError(f"锁 owner 文件损坏或不可读: {path}") from exc
    if (
        not isinstance(data, dict)
        or not isinstance(data.get("run_id"), str)
        or not data["run_id"]
    ):
        raise GuardError(f"锁 owner 文件格式无效: {path}")
    if not isinstance(data.get("acquired_at"), (int, float)):
        raise GuardError(f"锁 owner 缺少有效 acquired_at: {path}")
    return data


def _write_owner(lock_path: Path, owner: dict[str, object]) -> None:
    owner_path = _owner_path(lock_path)
    fd, temp_name = tempfile.mkstemp(prefix="owner.", dir=lock_path)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            json.dump(owner, stream, ensure_ascii=False, sort_keys=True)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temp_name, owner_path)
    finally:
        try:
            os.unlink(temp_name)
        except FileNotFoundError:
            pass


def _safe_remove_expired(lock_path: Path, owner: dict[str, object]) -> None:
    entries = {entry.name for entry in lock_path.iterdir()}
    if entries != {"owner.json"}:
        raise GuardError(f"过期锁包含未知文件，拒绝清理: {lock_path}")
    try:
        _owner_path(lock_path).unlink()
        lock_path.rmdir()
    except OSError as exc:
        raise GuardError(f"清理过期锁失败: {lock_path}: {exc}") from exc


def acquire_lock(lock_path: Path, run_id: str, ttl_minutes: int = 90) -> dict[str, object]:
    if not run_id.strip():
        raise GuardError("run-id 不能为空")
    if ttl_minutes <= 0:
        raise GuardError("ttl-minutes 必须为正整数")
    lock_path = lock_path.expanduser().resolve()
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    for attempt in range(2):
        try:
            lock_path.mkdir()
        except FileExistsError:
            owner = _read_owner(lock_path)
            age = time.time() - float(owner["acquired_at"])
            if age <= ttl_minutes * 60:
                raise GuardError(f"已有运行持有锁: {owner['run_id']} ({max(0, int(age))}s)")
            if attempt:
                raise GuardError(f"无法重建过期锁: {lock_path}")
            _safe_remove_expired(lock_path, owner)
            continue
        except OSError as exc:
            raise GuardError(f"创建锁失败: {lock_path}: {exc}") from exc
        owner = {"run_id": run_id, "pid": os.getpid(), "acquired_at": time.time()}
        try:
            _write_owner(lock_path, owner)
        except OSError as exc:
            try:
                lock_path.rmdir()
            except OSError:
                pass
            raise GuardError(f"写入锁 owner 失败: {exc}") from exc
        return owner
    raise GuardError(f"无法获取锁: {lock_path}")


def release_lock(lock_path: Path, run_id: str) -> None:
    lock_path = lock_path.expanduser().resolve()
    if not lock_path.exists():
        return
    owner = _read_owner(lock_path)
    if owner["run_id"] != run_id:
        raise GuardError(f"run-id 不匹配，拒绝释放他人锁: {owner['run_id']}")
    _safe_remove_expired(lock_path, owner)


def lock_status(lock_path: Path) -> dict[str, object] | None:
    lock_path = lock_path.expanduser().resolve()
    if not lock_path.exists():
        return None
    return _read_owner(lock_path)


def _print_guard_result(changes: list[Change], errors: list[str], base: str) -> int:
    if errors:
        print("recompile guard 失败", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"recompile guard 通过（基线 {base}，检查 {len(changes)} 个变更）")
    return 0


def _add_lock_path(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--lock-path", type=Path, default=argparse.SUPPRESS)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Agentic Work Atlas recompile guard")
    parser.add_argument("--repo", default=".", help="git repository, default: current directory")
    parser.add_argument("--base", default="HEAD", help="git baseline, default: HEAD")
    parser.add_argument("--log-date", help="expected log date, YYYY-MM-DD; default: today")
    parser.add_argument(
        "--max-stable",
        type=int,
        default=0,
        help="maximum modified existing stable Wiki pages; default: 0",
    )
    parser.add_argument(
        "--allow-maintenance",
        action="store_true",
        help="also allow index.md and wiki/lint-report.md; disabled by default",
    )
    _add_lock_path(parser)
    subparsers = parser.add_subparsers(dest="command")
    lock = subparsers.add_parser("lock", help="acquire/release/status an atomic lease lock")
    _add_lock_path(lock)
    lock_subparsers = lock.add_subparsers(dest="lock_command", required=True)
    acquire = lock_subparsers.add_parser("acquire")
    _add_lock_path(acquire)
    acquire.add_argument("--run-id", required=True)
    acquire.add_argument("--ttl-minutes", type=int, default=90)
    release = lock_subparsers.add_parser("release")
    _add_lock_path(release)
    release.add_argument("--run-id", required=True)
    status = lock_subparsers.add_parser("status")
    _add_lock_path(status)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    lock_path = getattr(args, "lock_path", DEFAULT_LOCK_PATH)
    try:
        if args.command == "lock":
            if args.lock_command == "acquire":
                owner = acquire_lock(lock_path, args.run_id, args.ttl_minutes)
                print(f"lock acquired: {owner['run_id']} ({lock_path})")
                return 0
            if args.lock_command == "release":
                release_lock(lock_path, args.run_id)
                print(f"lock released: {lock_path}")
                return 0
            owner = lock_status(lock_path)
            if owner is None:
                print(f"lock free: {lock_path}")
            else:
                age = max(0, int(time.time() - float(owner["acquired_at"])))
                print(f"lock held: {owner['run_id']} ({age}s, {lock_path})")
            return 0
        changes, errors = run_guard(
            args.repo,
            base=args.base,
            log_date=args.log_date,
            max_stable=args.max_stable,
            allow_maintenance=args.allow_maintenance,
        )
        return _print_guard_result(changes, errors, args.base)
    except GuardError as exc:
        print(f"recompile guard 错误: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
