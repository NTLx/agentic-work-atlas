---
type: lint-report
title: "Agentic Work Atlas Lint 报告"
date: "2026-06-13"
score: 100
status: "PASS"
tags:
  - lint-report
  - wiki-maintenance
---

# Agentic Work Atlas Lint 报告 - 2026-06-13

> [!summary] 状态
> 门禁: **PASS**
> 分数: **100/100**
> 阻断问题: **0**

## 统计

| 类别 | 数量 |
|------|------|
| Raw 来源 | 125 |
| Raw 已编译 | 125 |
| Raw 待编译 | 0 |
| Entity | 262 |
| Topic | 28 |
| Comparison | 18 |
| Output | 4 |

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
| `stale-core` | 0 |
| `entity` | 0 |
| `comparison` | 0 |
| `index` | 0 |

## 问题明细

### tag

- `wiki/entities/Andrej-Karpathy.md` - `tags 超过 5 个: 7`
- `wiki/sources/20260529-ceo-ai-psychosis-equity-podcast.md` - `tags 超过 5 个: 8`
- `wiki/sources/20260529-gemini-co-leads-origins.md` - `tags 超过 5 个: 8`
- `wiki/sources/20260530-ceo-knee-deep-building-ai.md` - `tags 超过 5 个: 6`
- `wiki/sources/20260604-anthropic-recursive-self-improvement.md` - `tags 超过 5 个: 6`
- `wiki/sources/20260604-dwarkesh-agi-scarcity.md` - `tags 超过 5 个: 6`
- `wiki/sources/20260604-mollick-coexistence.md` - `tags 超过 5 个: 7`
- `wiki/sources/20260604-openai-dreaming-memory.md` - `tags 超过 5 个: 6`
- `wiki/sources/20260608-reflecting-on-year-of-claude-code.md` - `tags 超过 5 个: 6`
- `wiki/sources/20260610-ai-exponential-policy.md` - `tags 超过 5 个: 6`
- `wiki/sources/building-effective-agents-complete.md` - `tags 超过 5 个: 7`

## 运行命令

```bash
uv run --with pyyaml python tools/wiki-lint.py --fix-index --write-report
```

*本报告由 `tools/wiki-lint.py` 生成。*
