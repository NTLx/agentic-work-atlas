---
type: lint-report
title: "Agentic Work Atlas Lint 报告"
date: "2026-07-01"
score: 98
status: "FAIL"
tags:
  - lint-report
  - wiki-maintenance
---

# Agentic Work Atlas Lint 报告 - 2026-07-01

> [!summary] 状态
> 门禁: **FAIL**
> 分数: **98/100**
> 阻断问题: **2**

## 统计

| 类别 | 数量 |
|------|------|
| Raw 来源 | 158 |
| Raw 已编译 | 154 |
| Raw 待编译 | 4 |
| Raw 已跳过 | 0 |
| Entity | 299 |
| Topic | 31 |
| Comparison | 19 |
| Output | 5 |

## 待编译 Raw

- `raw/Building headless automation with Claude Code — Code w Claude.md`
- `raw/How to 10x Your Value in the AI Era — Kunal Shah.md`
- `raw/The Tokenpocalypse Is Here Companies Are Scrambling To Stop Spending So Much on AI.md`
- `raw/the-ai-jobs-transition-framework-for-the-eu.md`

## 检查项

| 检查项 | 问题数 |
|--------|--------|
| `frontmatter` | 0 |
| `date` | 0 |
| `hidden-char` | 0 |
| `mathjax` | 0 |
| `wikilink` | 2 |
| `source_raw` | 0 |
| `tag` | 25 |
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

- `wiki/sources/20260701-grant-sanderson-ai-math-future.md` - `tags 超过 5 个: 6`
- `wiki/sources/20260701-grant-sanderson-ai-math-future.md` - `一次性 tag 仅出现 1 次: 'AI-mathematics'`
- `wiki/entities/SDK-Design.md` - `一次性 tag 仅出现 1 次: 'api-design'`
- `wiki/research/research-logs/2026-06-30.md` - `一次性 tag 仅出现 1 次: 'archive'`
- `wiki/entities/AI-Autonomy.md` - `一次性 tag 仅出现 1 次: 'autonomy'`
- `wiki/sources/20260701-grant-sanderson-ai-math-future.md` - `一次性 tag 仅出现 1 次: 'autoregression'`
- `wiki/sources/20260701-grant-sanderson-ai-math-future.md` - `一次性 tag 仅出现 1 次: 'conceptual-breakthroughs'`
- `wiki/entities/SDK-Design.md` - `一次性 tag 仅出现 1 次: 'developer-tools'`
- `wiki/sources/20260626-anthropic-economic-index-june-2026-report.md` - `一次性 tag 仅出现 1 次: 'economic-index'`
- `wiki/entities/Labor-Market-Impact.md` - `一次性 tag 仅出现 1 次: 'economics'`
- `wiki/research/research-logs/2026-06-30.md` - `一次性 tag 仅出现 1 次: 'exploration'`
- `wiki/entities/AI-in-Mathematics.md` - `一次性 tag 仅出现 1 次: 'frontier'`
- `wiki/research/research-logs/2026-06-30.md` - `一次性 tag 仅出现 1 次: 'full-inventory'`
- `wiki/topics/AI-Mathematics-Future.md` - `一次性 tag 仅出现 1 次: 'future'`
- `wiki/entities/Autoregressive-Generation.md` - `一次性 tag 仅出现 1 次: 'generation'`
- `wiki/sources/20260630-building-headless-automation-claude-code.md` - `一次性 tag 仅出现 1 次: 'github-action'`
- `wiki/entities/Headless-Automation.md` - `一次性 tag 仅出现 1 次: 'headless'`
- `wiki/sources/20260630-building-headless-automation-claude-code.md` - `一次性 tag 仅出现 1 次: 'headless-automation'`
- `wiki/sources/20260701-grant-sanderson-ai-math-future.md` - `一次性 tag 仅出现 1 次: 'human-curation'`
- `wiki/entities/Human-Curation.md` - `一次性 tag 仅出现 1 次: 'information-overload'`
- `wiki/entities/Conceptual-Breakthroughs.md` - `一次性 tag 仅出现 1 次: 'innovation'`
- `wiki/entities/AI-Artifact-Classification.md` - `一次性 tag 仅出现 1 次: 'output-analysis'`
- `wiki/entities/Theory-of-Mind.md` - `一次性 tag 仅出现 1 次: 'psychology'`
- `wiki/entities/AI-Perception-Survey.md` - `一次性 tag 仅出现 1 次: 'survey'`
- `wiki/entities/AI-Use-Rhythm.md` - `一次性 tag 仅出现 1 次: 'usage-patterns'`

### wikilink

- `wiki/research/research-agenda.md:102` - `链接目标不存在: [[exploration-archive-20260630]]`
- `wiki/research/research-agenda.md:120` - `链接目标不存在: [[exploration-archive-20260630]]`

## 运行命令

```bash
uv run --with pyyaml python tools/wiki-lint.py --fix-index --write-report
```

*本报告由 `tools/wiki-lint.py` 生成。*
