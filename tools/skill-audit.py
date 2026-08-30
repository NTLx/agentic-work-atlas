#!/usr/bin/env python3
"""Read-only audit for installed Agent Skills and their supply-chain lock.

The audit reports installation, metadata, lock, folder-hash, and Claude
compatibility drift. It never edits a skill, the lock file, or a symlink.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath
from typing import TextIO

import yaml


ROOT = Path(__file__).resolve().parents[1]
AGENTS_SKILLS_DIRNAME = ".agents/skills"
CLAUDE_SKILLS_DIRNAME = ".claude/skills"
LOCK_FILENAME = "skills-lock.json"
HASH_PATTERN = re.compile(r"^[0-9a-fA-F]{64}$")


@dataclass(frozen=True)
class InstalledSkill:
    """A discovered installed skill directory."""

    directory_name: str
    directory: Path
    skill_file: Path
    metadata: dict
    folder_hash: str | None


@dataclass
class AuditReport:
    """Collected audit facts and human-readable findings."""

    installed: dict[str, InstalledSkill] = field(default_factory=dict)
    locked: dict[str, dict] = field(default_factory=dict)
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    claude_valid: list[str] = field(default_factory=list)
    claude_invalid: list[str] = field(default_factory=list)
    claude_missing: list[str] = field(default_factory=list)


def _read_frontmatter(path: Path) -> tuple[dict, list[str]]:
    """Read Skill frontmatter and return metadata plus structural findings."""

    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return {}, [f"无法读取 {path}: {exc}"]

    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, [f"{path} 缺少 YAML frontmatter"]

    end = next((index for index, line in enumerate(lines[1:], start=1) if line.strip() == "---"), None)
    if end is None:
        return {}, [f"{path} 的 YAML frontmatter 没有结束标记"]

    try:
        data = yaml.safe_load("\n".join(lines[1:end])) or {}
    except yaml.YAMLError as exc:
        return {}, [f"{path} 的 YAML frontmatter 无法解析: {exc}"]
    if not isinstance(data, dict):
        return {}, [f"{path} 的 YAML frontmatter 必须是对象"]

    findings: list[str] = []
    name = data.get("name")
    description = data.get("description")
    if not isinstance(name, str) or not name.strip():
        findings.append(f"{path} 缺少非空 frontmatter.name")
    if not isinstance(description, str) or not description.strip():
        findings.append(f"{path} 缺少非空 frontmatter.description")
    return data, findings


def compute_skill_folder_hash(skill_dir: Path) -> str:
    """Match the local skills CLI folder hash algorithm.

    The hash includes every regular file and its POSIX relative path, while
    excluding ``.git`` and ``node_modules`` directories.
    """

    files: list[tuple[str, bytes]] = []
    for path in skill_dir.rglob("*"):
        if path.is_symlink() or not path.is_file():
            continue
        relative_path = path.relative_to(skill_dir).as_posix()
        if {".git", "node_modules"}.intersection(PurePosixPath(relative_path).parts):
            continue
        files.append((relative_path, path.read_bytes()))

    digest = hashlib.sha256()
    for relative_path, content in sorted(files):
        digest.update(relative_path.encode("utf-8"))
        digest.update(content)
    return digest.hexdigest()


def _discover_installed(repo: Path, report: AuditReport) -> None:
    skills_dir = repo / AGENTS_SKILLS_DIRNAME
    if not skills_dir.is_dir():
        report.errors.append(f"缺少 Runtime Skill 目录: {skills_dir}")
        return

    for directory in sorted(skills_dir.iterdir(), key=lambda item: item.name):
        if not directory.is_dir():
            continue
        skill_file = directory / "SKILL.md"
        if not skill_file.is_file():
            report.errors.append(f"已安装目录缺少 SKILL.md: {directory.name}")
            continue

        metadata, findings = _read_frontmatter(skill_file)
        report.errors.extend(findings)
        metadata_name = metadata.get("name")
        if isinstance(metadata_name, str) and metadata_name.strip() and metadata_name != directory.name:
            report.warnings.append(
                f"Skill name 与目录名不一致: {directory.name} vs {metadata_name}"
            )

        try:
            folder_hash = compute_skill_folder_hash(directory)
        except OSError as exc:
            folder_hash = None
            report.errors.append(f"无法计算 Skill 目录哈希 {directory.name}: {exc}")

        report.installed[directory.name] = InstalledSkill(
            directory_name=directory.name,
            directory=directory,
            skill_file=skill_file,
            metadata=metadata,
            folder_hash=folder_hash,
        )


def _load_lock(repo: Path, report: AuditReport) -> None:
    path = repo / LOCK_FILENAME
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        report.errors.append(f"无法读取 {path}: {exc}")
        return

    if not isinstance(data, dict):
        report.errors.append(f"{path} 顶层必须是对象")
        return
    if not isinstance(data.get("version"), int):
        report.errors.append(f"{path} 缺少整数 version")
    skills = data.get("skills")
    if not isinstance(skills, dict):
        report.errors.append(f"{path} 缺少对象 skills")
        return

    report.locked = skills
    for skill_name, entry in sorted(skills.items()):
        label = f"lock 条目 {skill_name}"
        if not isinstance(skill_name, str) or not skill_name.strip():
            report.errors.append("skills-lock.json 存在空 Skill 名称")
            continue
        if not isinstance(entry, dict):
            report.errors.append(f"{label} 必须是对象")
            continue

        source = entry.get("source")
        if not isinstance(source, str) or not source.strip():
            report.errors.append(f"{label} 缺少非空 source")
        source_type = entry.get("sourceType")
        if not isinstance(source_type, str) or not source_type.strip():
            report.errors.append(f"{label} 缺少非空 sourceType")

        skill_path = entry.get("skillPath")
        if not isinstance(skill_path, str) or not skill_path.strip():
            report.errors.append(f"{label} 缺少非空 skillPath")
        else:
            parsed_path = PurePosixPath(skill_path)
            if parsed_path.is_absolute() or ".." in parsed_path.parts or parsed_path.name != "SKILL.md":
                report.errors.append(f"{label} 的 skillPath 不是安全的相对 SKILL.md 路径: {skill_path}")
            elif len(parsed_path.parts) < 2:
                report.errors.append(f"{label} 的 skillPath 缺少 Skill 目录: {skill_path}")
            elif parsed_path.parts[-2] != skill_name:
                report.errors.append(
                    f"{label} 的 skillPath 目录与名称不一致: {skill_path}"
                )

        computed_hash = entry.get("computedHash")
        if not isinstance(computed_hash, str) or not HASH_PATTERN.fullmatch(computed_hash):
            report.errors.append(f"{label} 缺少合法的 64 位十六进制 computedHash")

        ref = entry.get("ref")
        if ref is not None and not isinstance(ref, str):
            report.errors.append(f"{label} 的 ref 必须是字符串")

        installed = report.installed.get(skill_name)
        if installed is None:
            report.errors.append(f"已锁定但未安装: {skill_name}")
        elif isinstance(computed_hash, str) and HASH_PATTERN.fullmatch(computed_hash):
            if installed.folder_hash and installed.folder_hash.lower() != computed_hash.lower():
                report.errors.append(
                    f"Skill 目录哈希漂移: {skill_name} "
                    f"(lock={computed_hash}, actual={installed.folder_hash})"
                )


def _audit_claude_links(repo: Path, report: AuditReport) -> None:
    links_dir = repo / CLAUDE_SKILLS_DIRNAME
    if not links_dir.is_dir():
        report.errors.append(f"缺少 Claude Skill 兼容目录: {links_dir}")
        report.claude_missing = sorted(report.installed)
        return

    agents_root = (repo / AGENTS_SKILLS_DIRNAME).resolve()
    seen_names: set[str] = set()
    for entry in sorted(links_dir.iterdir(), key=lambda item: item.name):
        if not entry.is_symlink():
            report.claude_invalid.append(entry.name)
            report.errors.append(f"Claude 入口不是软链接: {entry.name}")
            continue

        target = entry.resolve(strict=False)
        try:
            relative_target = target.relative_to(agents_root)
        except ValueError:
            report.claude_invalid.append(entry.name)
            report.errors.append(f"Claude 入口未指向 .agents/skills/: {entry.name} -> {entry.readlink()}")
            continue

        if len(relative_target.parts) != 1 or not target.is_dir() or not (target / "SKILL.md").is_file():
            report.claude_invalid.append(entry.name)
            report.errors.append(f"Claude 入口目标无效或悬空: {entry.name} -> {entry.readlink()}")
            continue
        target_name = relative_target.parts[0]
        if target_name != entry.name:
            report.claude_invalid.append(entry.name)
            report.errors.append(f"Claude 入口名称与目标不一致: {entry.name} -> {entry.readlink()}")
            continue

        seen_names.add(entry.name)
        report.claude_valid.append(entry.name)

    report.claude_missing = sorted(set(report.installed) - seen_names)
    for name in report.claude_missing:
        report.warnings.append(f"已安装 Skill 缺少 Claude 兼容软链接: {name}")


def audit_repo(repo: Path = ROOT) -> AuditReport:
    """Audit *repo* without changing any filesystem state."""

    resolved_repo = repo.resolve()
    report = AuditReport()
    _discover_installed(resolved_repo, report)
    _load_lock(resolved_repo, report)

    installed_names = set(report.installed)
    locked_names = set(report.locked)
    for name in sorted(installed_names - locked_names):
        report.warnings.append(f"已安装但未锁定: {name}")

    _audit_claude_links(resolved_repo, report)
    return report


def _print_findings(title: str, findings: list[str], stream: TextIO) -> None:
    print(f"{title}:", file=stream)
    if findings:
        for finding in findings:
            print(f"- {finding}", file=stream)
    else:
        print("- 无", file=stream)


def print_report(report: AuditReport, stream: TextIO = sys.stdout) -> None:
    """Print a stable, Chinese, read-only audit report."""

    print("Agent Skills 审计", file=stream)
    print(file=stream)
    print(f"已安装: {len(report.installed)}", file=stream)
    print(f"已锁定: {len(report.locked)}", file=stream)
    print(file=stream)
    _print_findings("错误", report.errors, stream)
    _print_findings("警告", report.warnings, stream)
    print(file=stream)
    print("Claude 兼容入口:", file=stream)
    print(f"- 有效软链接: {len(report.claude_valid)}", file=stream)
    print(f"- 无效或损坏: {len(report.claude_invalid)}", file=stream)
    print(f"- 缺失: {len(report.claude_missing)}", file=stream)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="只读审计 Agent Skills 安装状态与供应链漂移")
    parser.add_argument("--repo", type=Path, default=ROOT, help="仓库路径（默认当前工具所属仓库）")
    args = parser.parse_args(argv)

    report = audit_repo(args.repo)
    print_report(report)
    return 1 if report.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
