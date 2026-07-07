#!/usr/bin/env python3
"""
Agentic Work Atlas 校验与同步门禁。

本脚本保证 LLM Wiki 作为普通 Obsidian/Quartz Markdown 可正常工作：
- 校验 YAML frontmatter 与 ISO 日期字段
- 检测会触发 Obsidian MathJax 的裸露美元符号（raw 原文正文除外）
- 用真实文件校验 wikilink 与 source_raw 目标
- 检查 index.md 统计漂移
- 检查 entity/comparison 必填元数据
- 报告仍缺少摘要覆盖的 raw 文件（历史 raw 编译摘要或同名 source summary 二者满足其一）

用法:
  uv run --with pyyaml python tools/wiki-lint.py
  uv run --with pyyaml python tools/wiki-lint.py --fix-index
  uv run --with pyyaml python tools/wiki-lint.py --write-report
  uv run --with pyyaml python tools/wiki-lint.py --fix-index --write-report
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Iterable

import yaml


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
RAW = ROOT / "raw"
INDEX = ROOT / "index.md"
LINT_REPORT = WIKI / "lint-report.md"

COUNT_LABELS = {
    "Entity 页面": ("entities", WIKI / "entities"),
    "Topic 页面": ("topics", WIKI / "topics"),
    "Comparison 页面": ("comparisons", WIKI / "comparisons"),
    "Raw 文章": ("raw", RAW),
    "Output 作品": ("outputs", WIKI / "outputs"),
    "Research 日志": ("research", WIKI / "research" / "research-logs"),
}

STANDARD_ENTITY_SECTIONS = (
    "## 关键数据点",
    "## 前提与局限性",
    "## 关联概念",
)

DATE_FIELDS = ("published", "created", "updated", "date", "validated_at")
ZERO_WIDTH = ("\ufeff", "\u200b", "\u200c", "\u200d", "\u2060")
TAG_PATTERN = re.compile(r"^[A-Za-z][A-Za-z0-9]*(?:[-/][A-Za-z0-9]+)*$")
EVIDENCE_LEVELS = {"high", "medium", "low"}
CLAIM_TYPES = {"extracted", "synthesized", "mixed"}


@dataclass(frozen=True)
class Issue:
    category: str
    path: Path
    line: int | None
    message: str
    blocking: bool = True

    def rel(self) -> str:
        return self.path.relative_to(ROOT).as_posix()


def load_compile_registry():
    spec = importlib.util.spec_from_file_location("compile_registry", ROOT / "tools" / "compile_registry.py")
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


COMPILE_REGISTRY = load_compile_registry()


def markdown_files() -> list[Path]:
    files = [INDEX, ROOT / "README.md"]
    files.extend(sorted(RAW.glob("*.md")))
    files.extend(sorted(WIKI.rglob("*.md")))
    return [p for p in files if p.exists()]


def wiki_link_files() -> list[Path]:
    files = [INDEX]
    files.extend(sorted(WIKI.rglob("*.md")))
    return [p for p in files if p.exists() and p != LINT_REPORT]


def wiki_targets() -> tuple[set[str], set[str]]:
    files = markdown_files()
    stems = {p.stem for p in files}
    rels = {p.relative_to(ROOT).with_suffix("").as_posix() for p in files}
    # Also include raw non-markdown files (e.g. PDFs) as valid source_raw targets
    for p in RAW.iterdir():
        if p.is_file() and p.suffix.lower() != ".md":
            stems.add(p.stem)
    return stems, rels


def frontmatter(text: str) -> tuple[str | None, int]:
    if not text.startswith("---\n"):
        return None, 0
    end = text.find("\n---", 4)
    if end == -1:
        return None, 0
    return text[4:end], text[:end].count("\n") + 1


def load_frontmatter(path: Path) -> tuple[dict, Issue | None]:
    text = path.read_text(encoding="utf-8", errors="replace")
    raw, _ = frontmatter(text)
    if raw is None:
        return {}, None
    try:
        data = yaml.safe_load(raw) or {}
    except yaml.YAMLError as exc:
        return {}, Issue("frontmatter", path, 1, f"YAML 解析失败: {exc}")
    if not isinstance(data, dict):
        return {}, Issue("frontmatter", path, 1, "frontmatter 必须是 YAML mapping")
    return data, None


def strip_code(text: str) -> str:
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"`[^`\n]*`", "", text)
    return text


def strip_fenced_code(text: str) -> str:
    return re.sub(r"```.*?```", "", text, flags=re.S)


def strip_code_preserve_lines(text: str) -> str:
    lines = []
    in_fence = False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            lines.append("")
            continue
        if in_fence:
            lines.append("")
        else:
            lines.append(remove_inline_code(line))
    return "\n".join(lines)


def remove_inline_code(line: str) -> str:
    out: list[str] = []
    in_code = False
    code_ticks = 0
    i = 0
    while i < len(line):
        if line[i] == "`":
            j = i
            while j < len(line) and line[j] == "`":
                j += 1
            run = j - i
            if not in_code:
                in_code = True
                code_ticks = run
            elif run >= code_ticks:
                in_code = False
                code_ticks = 0
            i = j
            continue
        if not in_code:
            out.append(line[i])
        i += 1
    return "".join(out)


def has_bare_dollar(line: str) -> bool:
    in_code = False
    code_ticks = 0
    i = 0
    while i < len(line):
        if line[i] == "`":
            j = i
            while j < len(line) and line[j] == "`":
                j += 1
            run = j - i
            if not in_code:
                in_code = True
                code_ticks = run
            elif run >= code_ticks:
                in_code = False
                code_ticks = 0
            i = j
            continue
        if line[i] == "$" and not in_code and (i == 0 or line[i - 1] != "\\"):
            return True
        i += 1
    return False


def split_wikilink(raw: str) -> str:
    value = raw.replace(r"\|", "|")
    target = value.split("|", 1)[0].strip()
    target = target.split("#", 1)[0].strip()
    if target.endswith(".md"):
        target = target[:-3]
    elif target.endswith(".pdf"):
        target = target[:-4]
    return target.strip("/")


def target_exists(target: str, stems: set[str], rels: set[str]) -> bool:
    if not target:
        return True
    return target in stems or target in rels


def line_number(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


def check_frontmatter_and_dates(paths: Iterable[Path]) -> list[Issue]:
    issues: list[Issue] = []
    iso = re.compile(r"^\d{4}-\d{2}-\d{2}$")

    for path in paths:
        text = path.read_text(encoding="utf-8", errors="replace")
        data, err = load_frontmatter(path)
        if err:
            issues.append(err)
            continue

        raw, _ = frontmatter(text)
        if raw:
            for i, line in enumerate(raw.splitlines(), 2):
                stripped = line.strip()
                if not stripped or stripped.startswith("#"):
                    continue
                value = ""
                if stripped.startswith("- "):
                    value = stripped[2:].lstrip()
                elif ":" in stripped:
                    value = stripped.split(":", 1)[1].lstrip()
                if value.startswith('"') and value.count('"') > 2 and not re.search(r'\\"', value):
                    issues.append(
                        Issue(
                            "frontmatter",
                            path,
                            i,
                            "双引号标量内疑似包含未转义双引号，Quartz/YAML 可能解析失败",
                        )
                    )

        for field in DATE_FIELDS:
            if field not in data:
                continue
            value = data[field]
            if value is None:
                issues.append(Issue("date", path, None, f"{field} 不能为空"))
            elif isinstance(value, (date, datetime)):
                continue
            elif not isinstance(value, str) or not iso.match(value):
                issues.append(Issue("date", path, None, f"{field} 必须为 YYYY-MM-DD: {value!r}"))

    return issues


def check_hidden_chars(paths: Iterable[Path]) -> list[Issue]:
    issues: list[Issue] = []
    for path in paths:
        if path.is_relative_to(RAW):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for char in ZERO_WIDTH:
            pos = text.find(char)
            if pos >= 0:
                issues.append(Issue("hidden-char", path, line_number(text, pos), f"发现隐藏字符 U+{ord(char):04X}"))
    return issues


def check_dollars(paths: Iterable[Path]) -> list[Issue]:
    issues: list[Issue] = []
    for path in paths:
        if path.is_relative_to(RAW):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        in_fence = False
        for i, line in enumerate(text.splitlines(), 1):
            if line.lstrip().startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            if has_bare_dollar(line):
                issues.append(Issue("mathjax", path, i, "发现裸露 $，需用反引号包裹或反斜杠转义"))
    return issues


def check_wikilinks(paths: Iterable[Path]) -> list[Issue]:
    issues: list[Issue] = []
    stems, rels = wiki_targets()

    for path in paths:
        text = path.read_text(encoding="utf-8", errors="replace")
        # Strip YAML frontmatter — source_raw check already validates those targets
        if text.startswith("---"):
            end = text.find("---", 3)
            if end != -1:
                # Replace frontmatter with blank lines to preserve line numbers
                fm_lines = text[: end + 3].count("\n") + 1
                text = "\n" * fm_lines + text[end + 3 :]
        stripped = strip_code_preserve_lines(text)
        for match in re.finditer(r"!?\[\[([^\]]+)\]\]", stripped):
            raw = match.group(1)
            target = split_wikilink(raw)
            if not target_exists(target, stems, rels):
                issues.append(
                    Issue(
                        "wikilink",
                        path,
                        line_number(stripped, match.start()),
                        f"链接目标不存在: [[{raw}]]",
                    )
                )
    return issues


def as_list(value) -> list:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def check_tag_quality(paths: Iterable[Path]) -> list[Issue]:
    issues: list[Issue] = []
    for path in paths:
        data, err = load_frontmatter(path)
        if err or not data:
            continue
        tags = as_list(data.get("tags"))
        if len(tags) > 5:
            issues.append(Issue("tag", path, None, f"tags 超过 5 个: {len(tags)}", blocking=False))
        for tag in tags:
            tag_text = str(tag)
            if tag_text.startswith("visibility/"):
                continue
            if not TAG_PATTERN.match(tag_text):
                issues.append(Issue("tag", path, None, f"非 kebab-case tag: {tag_text!r}", blocking=False))
    return issues


def check_singleton_tags(paths: Iterable[Path]) -> list[Issue]:
    tag_paths: dict[str, list[Path]] = {}
    for path in paths:
        data, err = load_frontmatter(path)
        if err or not data:
            continue
        for tag in as_list(data.get("tags")):
            tag_text = str(tag)
            if tag_text.startswith("visibility/"):
                continue
            tag_paths.setdefault(tag_text, []).append(path)

    issues: list[Issue] = []
    for tag, owners in sorted(tag_paths.items()):
        if len(owners) == 1:
            issues.append(
                Issue(
                    "tag",
                    owners[0],
                    None,
                    f"一次性 tag 仅出现 1 次: {tag!r}",
                    blocking=False,
                )
            )
    return issues


def check_evidence_schema(paths: Iterable[Path]) -> list[Issue]:
    issues: list[Issue] = []
    for path in paths:
        data, err = load_frontmatter(path)
        if err or not data:
            continue
        evidence_level = data.get("evidence_level")
        if evidence_level is not None and evidence_level not in EVIDENCE_LEVELS:
            issues.append(Issue("evidence", path, None, f"evidence_level 必须为 high/medium/low: {evidence_level!r}"))
        claim_type = data.get("claim_type")
        if claim_type is not None and claim_type not in CLAIM_TYPES:
            issues.append(Issue("evidence", path, None, f"claim_type 必须为 extracted/synthesized/mixed: {claim_type!r}"))
    return issues


def check_low_evidence_pages(paths: Iterable[Path]) -> list[Issue]:
    issues: list[Issue] = []
    for path in paths:
        data, err = load_frontmatter(path)
        if err or not data:
            continue
        if data.get("evidence_level") == "low":
            issues.append(
                Issue(
                    "low-evidence",
                    path,
                    None,
                    f"低证据页面 {path.stem} 只能作为补 source 或探索线索",
                    blocking=False,
                )
            )
    return issues


def inbound_wikilink_counts(paths: Iterable[Path]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for path in paths:
        text = path.read_text(encoding="utf-8", errors="replace")
        stripped = strip_code_preserve_lines(text)
        seen_in_file: set[str] = set()
        for match in re.finditer(r"!?\[\[([^\]]+)\]\]", stripped):
            target = split_wikilink(match.group(1))
            if target:
                seen_in_file.add(target.split("/")[-1])
        for target in seen_in_file:
            counts[target] = counts.get(target, 0) + 1
    return counts


def parse_iso_date(value) -> date | None:
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    if isinstance(value, str):
        try:
            return date.fromisoformat(value)
        except ValueError:
            return None
    return None


def check_stale_core_pages(
    paths: Iterable[Path],
    today: date | None = None,
    stale_days: int = 90,
    min_inbound: int = 5,
) -> list[Issue]:
    path_list = list(paths)
    counts = inbound_wikilink_counts(path_list)
    today = today or date.today()
    issues: list[Issue] = []

    for path in path_list:
        if path.name in {"index.md", "lint-report.md", "research-agenda.md"}:
            continue
        data, err = load_frontmatter(path)
        if err or not data:
            continue
        updated = parse_iso_date(data.get("updated"))
        if not updated:
            continue
        age = (today - updated).days
        inbound = counts.get(path.stem, 0)
        if age >= stale_days and inbound >= min_inbound:
            issues.append(
                Issue(
                    "stale-core",
                    path,
                    None,
                    f"核心页 {path.stem} 已 {age} 天未更新，入链 {inbound} 条",
                    blocking=False,
                )
            )
    return issues


def check_source_raw() -> list[Issue]:
    issues: list[Issue] = []
    stems, rels = wiki_targets()

    for path in sorted(WIKI.rglob("*.md")):
        data, err = load_frontmatter(path)
        if err or not data:
            continue
        for item in as_list(data.get("source_raw")):
            if not isinstance(item, str) or not item.startswith("[[") or not item.endswith("]]"):
                issues.append(Issue("source_raw", path, None, f"source_raw 必须使用 wikilink 短链接: {item!r}"))
                continue
            target = split_wikilink(item[2:-2])
            if not target_exists(target, stems, rels):
                issues.append(Issue("source_raw", path, None, f"source_raw 目标不存在: {item}"))
    return issues


def check_entities() -> list[Issue]:
    issues: list[Issue] = []
    for path in sorted((WIKI / "entities").glob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        data, err = load_frontmatter(path)
        if err:
            continue

        tags = {str(t) for t in as_list(data.get("tags"))}
        is_person = "person" in tags

        for field in ("title", "aliases", "definition", "source_raw"):
            if field not in data or data[field] in (None, "", []):
                issues.append(Issue("entity", path, None, f"Entity 缺少必填字段: {field}"))

        if is_person:
            for field in ("validated_source", "validated_at"):
                if field not in data or data[field] in (None, "", []):
                    issues.append(Issue("entity", path, None, f"作者 Entity 缺少字段: {field}"))
        else:
            for section in STANDARD_ENTITY_SECTIONS:
                if section not in text:
                    issues.append(Issue("entity", path, None, f"概念 Entity 缺少章节: {section}"))

    return issues


def check_comparisons() -> list[Issue]:
    issues: list[Issue] = []
    for path in sorted((WIKI / "comparisons").glob("*.md")):
        data, err = load_frontmatter(path)
        if err:
            continue
        if "updated" not in data or data["updated"] in (None, ""):
            issues.append(Issue("comparison", path, None, "Comparison 缺少 updated 字段"))
    return issues


def count_md(directory: Path) -> int:
    return len(list(directory.glob("*.md")))


def actual_counts() -> dict[str, int]:
    return {key: count_md(path) for _, (key, path) in COUNT_LABELS.items()}


def check_index_counts() -> list[Issue]:
    issues: list[Issue] = []
    if not INDEX.exists():
        return [Issue("index", INDEX, None, "index.md 不存在")]

    text = INDEX.read_text(encoding="utf-8", errors="replace")
    counts = actual_counts()
    for label, (key, _) in COUNT_LABELS.items():
        match = re.search(rf"\| {re.escape(label)} \| (\d+) 个 \|", text)
        if not match:
            issues.append(Issue("index", INDEX, None, f"索引概览缺少计数行: {label}"))
            continue
        current = int(match.group(1))
        if current != counts[key]:
            issues.append(Issue("index", INDEX, line_number(text, match.start()), f"{label} 计数漂移: index={current}, actual={counts[key]}"))
    return issues


def fix_index_counts() -> bool:
    text = INDEX.read_text(encoding="utf-8")
    original = text
    counts = actual_counts()

    for label, (key, _) in COUNT_LABELS.items():
        text = re.sub(rf"\| {re.escape(label)} \| \d+ 个 \|", f"| {label} | {counts[key]} 个 |", text)
    today = datetime.now().strftime("%Y-%m-%d")
    text = re.sub(r"^updated: \d{4}-\d{2}-\d{2}$", f"updated: {today}", text, count=1, flags=re.M)

    if text != original:
        INDEX.write_text(text, encoding="utf-8")
        return True
    return False


def check_registry_consistency() -> tuple[list[Issue], list[Path], list[Path], list[Path], list[dict]]:
    registry_path = ROOT / "state" / "raw-registry.json"
    issues: list[Issue] = []
    if not registry_path.exists():
        issues.append(
            Issue(
                "registry-consistency",
                registry_path,
                None,
                "缺少 authority registry 文件: state/raw-registry.json",
            )
        )
    try:
        registry = COMPILE_REGISTRY.load_registry(ROOT)
    except (json.JSONDecodeError, ValueError) as exc:
        issues.append(Issue("registry-consistency", registry_path, None, str(exc)))
        return issues, [], sorted(RAW.glob("*.md")), [], []
    recorded_raw_files = set(registry.get("items", {}))
    registry, anomalies, candidates = COMPILE_REGISTRY.reconcile_registry(ROOT, registry=registry)

    compiled: list[Path] = []
    pending: list[Path] = []
    skipped: list[Path] = []

    for raw_path in sorted(RAW.glob("*.md")):
        if raw_path.name not in recorded_raw_files:
            pending.append(raw_path)
            issues.append(Issue("registry-consistency", raw_path, None, "raw 缺少 registry 记录"))
            continue
        entry = registry["items"].get(raw_path.name)
        if entry is None:
            pending.append(raw_path)
            issues.append(Issue("registry-consistency", raw_path, None, "raw 缺少 registry 记录"))
            continue
        status = entry.get("status", "pending")
        if status == "compiled":
            compiled.append(raw_path)
        elif status == "skipped":
            skipped.append(raw_path)
        else:
            pending.append(raw_path)

    for anomaly in anomalies:
        issues.append(
            Issue(
                "registry-consistency",
                RAW / anomaly["raw_file"],
                None,
                f"registry 异常: {anomaly['raw_file']} ({anomaly['reason']})",
            )
        )

    for candidate in candidates:
        severity = candidate.get("severity", COMPILE_REGISTRY.candidate_severity(candidate["reason"]))
        issues.append(
            Issue(
                "registry-consistency",
                RAW / candidate["raw_file"],
                None,
                f"需重编译候选: {candidate['raw_file']} ({candidate['reason']})",
                blocking=severity == "blocking",
            )
        )

    return issues, compiled, pending, skipped, candidates


def collect_issues() -> tuple[list[Issue], dict[str, int], list[Path], list[Path], list[dict]]:
    paths = markdown_files()
    issues: list[Issue] = []
    issues.extend(check_frontmatter_and_dates(paths))
    issues.extend(check_hidden_chars(paths))
    issues.extend(check_dollars(paths))
    issues.extend(check_wikilinks(wiki_link_files()))
    issues.extend(check_source_raw())
    issues.extend(check_tag_quality(wiki_link_files()))
    issues.extend(check_singleton_tags(wiki_link_files()))
    issues.extend(check_evidence_schema(wiki_link_files()))
    issues.extend(check_low_evidence_pages(wiki_link_files()))
    issues.extend(check_stale_core_pages(wiki_link_files()))
    issues.extend(check_entities())
    issues.extend(check_comparisons())
    issues.extend(check_index_counts())

    registry_issues, compiled, pending, skipped, candidates = check_registry_consistency()
    issues.extend(registry_issues)

    stats = actual_counts()
    stats["raw_compiled"] = len(compiled)
    stats["raw_pending"] = len(pending)
    stats["raw_skipped"] = len(skipped)
    return issues, stats, pending, skipped, candidates


def group_issues(issues: Iterable[Issue]) -> dict[str, list[Issue]]:
    grouped: dict[str, list[Issue]] = {}
    for issue in issues:
        grouped.setdefault(issue.category, []).append(issue)
    return grouped


def md_escape_code(value: str) -> str:
    return value.replace("`", "'").replace("\n", " / ")


def render_report(
    issues: list[Issue],
    stats: dict[str, int],
    pending: list[Path],
    skipped: list[Path],
    candidates: list[dict],
) -> str:
    today = datetime.now().strftime("%Y-%m-%d")
    blocking = [i for i in issues if i.blocking]
    score = max(0, 100 - len(blocking))
    status = "PASS" if not blocking else "FAIL"
    grouped = group_issues(issues)

    lines = [
        "---",
        "type: lint-report",
        'title: "Agentic Work Atlas Lint 报告"',
        f'date: "{today}"',
        f"score: {score}",
        f'status: "{status}"',
        "tags:",
        "  - lint-report",
        "  - wiki-maintenance",
        "---",
        "",
        f"# Agentic Work Atlas Lint 报告 - {today}",
        "",
        f"> [!summary] 状态",
        f"> 门禁: **{status}**",
        f"> 分数: **{score}/100**",
        f"> 阻断问题: **{len(blocking)}**",
        "",
        "## 统计",
        "",
        "| 类别 | 数量 |",
        "|------|------|",
        f"| Raw 来源 | {stats['raw']} |",
        f"| Raw 已编译 | {stats['raw_compiled']} |",
        f"| Raw 待编译 | {stats['raw_pending']} |",
        f"| Raw 已跳过 | {stats['raw_skipped']} |",
        f"| Entity | {stats['entities']} |",
        f"| Topic | {stats['topics']} |",
        f"| Comparison | {stats['comparisons']} |",
        f"| Output | {stats['outputs']} |",
        "",
    ]

    if pending:
        lines.extend(["## 待编译 Raw", ""])
        for path in pending:
            lines.append(f"- `{md_escape_code(path.relative_to(ROOT).as_posix())}`")
        lines.append("")

    if skipped:
        lines.extend(["## 已跳过 Raw", ""])
        for path in skipped:
            lines.append(f"- `{md_escape_code(path.relative_to(ROOT).as_posix())}`")
        lines.append("")

    if candidates:
        lines.extend(["## 需重编译候选", ""])
        for item in candidates:
            lines.append(f"- `{item['raw_file']}` - `{item['reason']}`")
        lines.append("")

    lines.extend(["## 检查项", "", "| 检查项 | 问题数 |", "|--------|--------|"])
    for category in (
        "frontmatter",
        "date",
        "hidden-char",
        "mathjax",
        "wikilink",
        "source_raw",
        "tag",
        "evidence",
        "low-evidence",
        "stale-core",
        "entity",
        "comparison",
        "index",
        "registry-consistency",
    ):
        lines.append(f"| `{category}` | {len(grouped.get(category, []))} |")
    lines.append("")

    if issues:
        lines.extend(["## 问题明细", ""])
        for category, items in sorted(grouped.items()):
            lines.extend([f"### {category}", ""])
            for issue in items:
                loc = f"{issue.rel()}:{issue.line}" if issue.line else issue.rel()
                lines.append(f"- `{md_escape_code(loc)}` - `{md_escape_code(issue.message)}`")
            lines.append("")
    else:
        lines.extend(["## 问题明细", "", "未发现阻断问题。", ""])

    lines.extend(
        [
            "## 运行命令",
            "",
            "```bash",
            "uv run --with pyyaml python tools/wiki-lint.py --fix-index --write-report",
            "```",
            "",
            "*本报告由 `tools/wiki-lint.py` 生成。*",
            "",
        ]
    )
    return "\n".join(lines)


def print_summary(
    issues: list[Issue],
    stats: dict[str, int],
    pending: list[Path],
    skipped: list[Path],
    candidates: list[dict],
) -> None:
    blocking = [i for i in issues if i.blocking]
    print("Agentic Work Atlas Lint")
    print("=" * 60)
    print(f"Raw: {stats['raw']}（已编译 {stats['raw_compiled']}，待编译 {stats['raw_pending']}，已跳过 {stats['raw_skipped']}）")
    print(f"Entity: {stats['entities']} | Topic: {stats['topics']} | Comparison: {stats['comparisons']} | Output: {stats['outputs']} | Research: {stats['research']}")
    print(f"阻断问题: {len(blocking)}")

    grouped = group_issues(issues)
    for category in sorted(grouped):
        print(f"- {category}: {len(grouped[category])}")

    if pending:
        print("\n待编译 Raw:")
        for path in pending[:20]:
            print(f"- {path.relative_to(ROOT).as_posix()}")
        if len(pending) > 20:
            print(f"... 另有 {len(pending) - 20} 个")

    if skipped:
        print("\n已跳过 Raw:")
        for path in skipped[:20]:
            print(f"- {path.relative_to(ROOT).as_posix()}")
        if len(skipped) > 20:
            print(f"... 另有 {len(skipped) - 20} 个")

    if candidates:
        print("\n需重编译候选:")
        for item in candidates[:20]:
            print(f"- {item['raw_file']} ({item['reason']})")
        if len(candidates) > 20:
            print(f"... 另有 {len(candidates) - 20} 个")

    if issues:
        print("\n前几个问题:")
        for issue in issues[:30]:
            loc = f"{issue.rel()}:{issue.line}" if issue.line else issue.rel()
            print(f"- [{issue.category}] {loc}: {issue.message}")


def main() -> int:
    parser = argparse.ArgumentParser(description="检查并同步 Agentic Work Atlas")
    parser.add_argument("--fix-index", action="store_true", help="更新 index.md 计数和 updated 日期")
    parser.add_argument("--write-report", action="store_true", help="写入 wiki/lint-report.md")
    args = parser.parse_args()

    if args.fix_index:
        changed = fix_index_counts()
        if changed:
            print("已更新 index.md 计数")

    issues, stats, pending, skipped, candidates = collect_issues()
    print_summary(issues, stats, pending, skipped, candidates)

    if args.write_report:
        LINT_REPORT.write_text(render_report(issues, stats, pending, skipped, candidates), encoding="utf-8")
        print(f"\n已写入 {LINT_REPORT.relative_to(ROOT).as_posix()}")

    return 1 if any(i.blocking for i in issues) else 0


if __name__ == "__main__":
    sys.exit(main())
