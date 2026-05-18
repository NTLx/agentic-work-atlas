#!/usr/bin/env python3
"""
Audit entity value in the Clips LLM Wiki.

This is intentionally separate from wiki-lint.py. Lint catches rendering and
schema failures; entity audit produces review queues for judgment-heavy cleanup.

Usage:
  python3 tools/entity-audit.py
  python3 tools/entity-audit.py --write-report
"""

from __future__ import annotations

import argparse
import re
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
ENTITY_DIR = ROOT / "wiki" / "entities"


@dataclass
class Entity:
    stem: str
    path: Path
    title: str
    definition: str
    tags: list[str]
    source_count: int
    related_count: int
    body_len: int
    graph_in: int
    topic_in: int
    comparison_in: int
    entity_in: int
    reasons: list[str]
    score: int
    bucket: str


def read_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    try:
        data = yaml.safe_load(text[4:end]) or {}
    except yaml.YAMLError:
        return {}
    return data if isinstance(data, dict) else {}


def as_list(value) -> list:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def wikilink_targets(text: str) -> list[str]:
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    targets: list[str] = []
    for match in re.finditer(r"!?\[\[([^\]]+)\]\]", text):
        target = match.group(1).replace(r"\|", "|").split("|", 1)[0].split("#", 1)[0].strip()
        if target.endswith(".md"):
            target = target[:-3]
        if target.startswith("wiki/entities/"):
            target = target.split("/")[-1]
        targets.append(target)
    return targets


def inbound_maps(entity_stems: set[str]) -> tuple[dict[str, set[str]], dict[str, set[str]], dict[str, set[str]], dict[str, set[str]]]:
    graph: dict[str, set[str]] = defaultdict(set)
    topics: dict[str, set[str]] = defaultdict(set)
    comparisons: dict[str, set[str]] = defaultdict(set)
    entities: dict[str, set[str]] = defaultdict(set)

    for path in (ROOT / "wiki").rglob("*.md"):
        if path.name == "lint-report.md":
            continue
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8", errors="replace")
        for target in wikilink_targets(text):
            if target not in entity_stems or path == ENTITY_DIR / f"{target}.md":
                continue
            graph[target].add(rel)
            if "/topics/" in rel:
                topics[target].add(rel)
            elif "/comparisons/" in rel:
                comparisons[target].add(rel)
            elif "/entities/" in rel:
                entities[target].add(rel)

    return graph, topics, comparisons, entities


def classify(data: dict, body_len: int, graph_in: int, topic_in: int, comparison_in: int, entity_in: int) -> tuple[int, str, list[str]]:
    tags = [str(t) for t in as_list(data.get("tags"))]
    tags_lower = {t.lower() for t in tags}
    source_count = len(as_list(data.get("source_raw")))
    related_count = len(as_list(data.get("related_entities")))
    is_person = "person" in tags_lower

    score = 35
    reasons: list[str] = []

    if is_person:
        score += 25
        reasons.append("actor/person entity")
    if source_count >= 2:
        score += 20
        reasons.append("multi-source")
    if topic_in > 0:
        score += 25
        reasons.append("topic-backed")
    if comparison_in > 0:
        score += 15
        reasons.append("comparison-backed")
    if entity_in >= 3:
        score += 10
        reasons.append("entity hub")
    elif entity_in >= 1:
        score += 5
        reasons.append("entity-linked")
    if related_count >= 3:
        score += 8
        reasons.append("rich related_entities")
    if body_len >= 1800:
        score += 5
        reasons.append("substantive body")

    if not is_person and source_count <= 1:
        score -= 10
        reasons.append("single-source")
    if not is_person and topic_in == 0 and comparison_in == 0:
        score -= 12
        reasons.append("no topic/comparison backing")
    if not is_person and graph_in == 0:
        score -= 18
        reasons.append("no graph inbound")

    score = max(0, min(100, score))

    if is_person:
        bucket = "keep-actor"
    elif graph_in == 0 and source_count <= 1:
        bucket = "merge-or-demote"
    elif source_count <= 1 and topic_in == 0 and comparison_in == 0:
        bucket = "review"
    elif score >= 55:
        bucket = "keep"
    else:
        bucket = "strengthen"

    return score, bucket, reasons


def audit_entities() -> list[Entity]:
    paths = sorted(ENTITY_DIR.glob("*.md"))
    stems = {p.stem for p in paths}
    graph, topics, comparisons, entities = inbound_maps(stems)
    rows: list[Entity] = []

    for path in paths:
        data = read_frontmatter(path)
        text = path.read_text(encoding="utf-8", errors="replace")
        score, bucket, reasons = classify(
            data,
            len(text),
            len(graph[path.stem]),
            len(topics[path.stem]),
            len(comparisons[path.stem]),
            len(entities[path.stem]),
        )
        rows.append(
            Entity(
                stem=path.stem,
                path=path,
                title=str(data.get("title") or path.stem),
                definition=str(data.get("definition") or ""),
                tags=[str(t) for t in as_list(data.get("tags"))],
                source_count=len(as_list(data.get("source_raw"))),
                related_count=len(as_list(data.get("related_entities"))),
                body_len=len(text),
                graph_in=len(graph[path.stem]),
                topic_in=len(topics[path.stem]),
                comparison_in=len(comparisons[path.stem]),
                entity_in=len(entities[path.stem]),
                reasons=reasons,
                score=score,
                bucket=bucket,
            )
        )
    return rows


def render_report(rows: list[Entity]) -> str:
    today = datetime.now().strftime("%Y-%m-%d")
    buckets = defaultdict(list)
    for row in rows:
        buckets[row.bucket].append(row)

    lines = [
        "---",
        "type: audit-report",
        'title: "Entity Value Audit"',
        f'date: "{today}"',
        "tags:",
        "  - audit-report",
        "  - wiki-maintenance",
        "---",
        "",
        f"# Entity Value Audit - {today}",
        "",
        "## Summary",
        "",
        "| Bucket | Count | Meaning |",
        "|--------|-------|---------|",
    ]
    meanings = {
        "keep": "multi-source, topic-backed, or structurally central",
        "keep-actor": "person/actor entity, keep if validated",
        "strengthen": "valid concept but needs more links or sources",
        "review": "single-source concept without topic/comparison backing",
        "merge-or-demote": "single-source and no graph inbound; likely source-level detail",
    }
    for bucket in ("keep", "keep-actor", "strengthen", "review", "merge-or-demote"):
        lines.append(f"| `{bucket}` | {len(buckets[bucket])} | {meanings[bucket]} |")

    lines.extend(
        [
            "",
            "## Review Queue",
            "",
            "These pages are not automatically wrong. They need a human/agent decision: link into a topic, merge into a broader page, or demote to source summary.",
            "",
            "| Entity | Score | Sources | Graph In | Topic In | Reason |",
            "|--------|-------|---------|----------|----------|--------|",
        ]
    )
    for row in sorted(buckets["review"], key=lambda r: (r.score, r.stem)):
        lines.append(
            f"| [[{row.stem}]] | {row.score} | {row.source_count} | {row.graph_in} | {row.topic_in} | {', '.join(row.reasons)} |"
        )

    lines.extend(
        [
            "",
            "## Merge Or Demote Queue",
            "",
            "| Entity | Score | Sources | Definition |",
            "|--------|-------|---------|------------|",
        ]
    )
    for row in sorted(buckets["merge-or-demote"], key=lambda r: (r.score, r.stem)):
        definition = row.definition.replace("|", "/")
        lines.append(f"| [[{row.stem}]] | {row.score} | {row.source_count} | {definition} |")

    lines.extend(
        [
            "",
            "## Controls",
            "",
            "- New Entity should satisfy at least two positive signals: multi-source reuse, topic/comparison need, cross-source contradiction, stable named concept, or high future query value.",
            "- Single-source details should default to source summary or topic section, not Entity.",
            "- Tool/product/org names require recurring use or direct architectural importance.",
            "- Review queue items should either gain topic/comparison backing or be merged/demoted during maintenance.",
            "",
            "```bash",
            "python3 tools/entity-audit.py --write-report",
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def report_path() -> Path:
    today = datetime.now().strftime("%Y-%m-%d")
    return ROOT / "docs" / f"entity-audit-{today}.md"


def print_summary(rows: list[Entity]) -> None:
    buckets = defaultdict(list)
    for row in rows:
        buckets[row.bucket].append(row)
    print("Entity value audit")
    print("=" * 60)
    print(f"Entities: {len(rows)}")
    for bucket in ("keep", "keep-actor", "strengthen", "review", "merge-or-demote"):
        print(f"{bucket}: {len(buckets[bucket])}")
    print("\nMerge/demote candidates:")
    for row in sorted(buckets["merge-or-demote"], key=lambda r: (r.score, r.stem))[:20]:
        print(f"- {row.stem} (score={row.score}, sources={row.source_count}, graph_in={row.graph_in})")
    print("\nReview candidates:")
    for row in sorted(buckets["review"], key=lambda r: (r.score, r.stem))[:30]:
        print(f"- {row.stem} (score={row.score}, sources={row.source_count}, graph_in={row.graph_in}, topic_in={row.topic_in})")


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit entity value in Clips LLM Wiki")
    parser.add_argument("--write-report", action="store_true", help="Write docs/entity-audit-2026-05-18.md")
    args = parser.parse_args()

    rows = audit_entities()
    print_summary(rows)
    if args.write_report:
        path = report_path()
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(render_report(rows), encoding="utf-8")
        print(f"\nwrote {path.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
