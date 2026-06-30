---
type: lint-report
title: "Agentic Work Atlas Lint 报告"
date: "2026-06-30"
score: 100
status: "PASS"
tags:
  - lint-report
  - wiki-maintenance
---

# Agentic Work Atlas Lint 报告 - 2026-06-30

> [!summary] 状态
> 门禁: **PASS**
> 分数: **100/100**
> 阻断问题: **0**

## 统计

| 类别 | 数量 |
|------|------|
| Raw 来源 | 155 |
| Raw 已编译 | 153 |
| Raw 待编译 | 2 |
| Raw 已跳过 | 0 |
| Entity | 293 |
| Topic | 30 |
| Comparison | 19 |
| Output | 5 |

## 待编译 Raw

- `raw/The Tokenpocalypse Is Here Companies Are Scrambling To Stop Spending So Much on AI.md`
- `raw/the-ai-jobs-transition-framework-for-the-eu.md`

## 检查项

| 检查项 | 问题数 |
|--------|--------|
| `frontmatter` | 0 |
| `date` | 0 |
| `hidden-char` | 0 |
| `mathjax` | 0 |
| `wikilink` | 0 |
| `source_raw` | 0 |
| `tag` | 11 |
| `evidence` | 0 |
| `low-evidence` | 1 |
| `stale-core` | 0 |
| `entity` | 0 |
| `comparison` | 0 |
| `index` | 0 |
| `registry-consistency` | 0 |

## 问题明细

### low-evidence

- `wiki/topics/AI-Management-Mindset-Transfer.md` - `低证据页面 AI-Management-Mindset-Transfer 只能作为补 source 或探索线索`

### tag

- `wiki/entities/SDK-Design.md` - `一次性 tag 仅出现 1 次: 'api-design'`
- `wiki/entities/AI-Autonomy.md` - `一次性 tag 仅出现 1 次: 'autonomy'`
- `wiki/entities/SDK-Design.md` - `一次性 tag 仅出现 1 次: 'developer-tools'`
- `wiki/sources/20260626-anthropic-economic-index-june-2026-report.md` - `一次性 tag 仅出现 1 次: 'economic-index'`
- `wiki/entities/Labor-Market-Impact.md` - `一次性 tag 仅出现 1 次: 'economics'`
- `wiki/sources/20260630-building-headless-automation-claude-code.md` - `一次性 tag 仅出现 1 次: 'github-action'`
- `wiki/entities/Headless-Automation.md` - `一次性 tag 仅出现 1 次: 'headless'`
- `wiki/sources/20260630-building-headless-automation-claude-code.md` - `一次性 tag 仅出现 1 次: 'headless-automation'`
- `wiki/entities/AI-Artifact-Classification.md` - `一次性 tag 仅出现 1 次: 'output-analysis'`
- `wiki/entities/AI-Perception-Survey.md` - `一次性 tag 仅出现 1 次: 'survey'`
- `wiki/entities/AI-Use-Rhythm.md` - `一次性 tag 仅出现 1 次: 'usage-patterns'`

## 运行命令

```bash
uv run --with pyyaml python tools/wiki-lint.py --fix-index --write-report
```

*本报告由 `tools/wiki-lint.py` 生成。*
