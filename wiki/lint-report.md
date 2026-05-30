---
type: lint-report
title: "Agentic Work Atlas Lint 报告"
date: "2026-05-30"
score: 97
status: "FAIL"
tags:
  - lint-report
  - wiki-maintenance
---

# Agentic Work Atlas Lint 报告 - 2026-05-30

> [!summary] 状态
> 门禁: **FAIL**
> 分数: **97/100**
> 阻断问题: **3**

## 统计

| 类别 | 数量 |
|------|------|
| Raw 来源 | 81 |
| Raw 已编译 | 81 |
| Raw 待编译 | 0 |
| Entity | 213 |
| Topic | 27 |
| Comparison | 14 |
| Output | 5 |

## 检查项

| 检查项 | 问题数 |
|--------|--------|
| `frontmatter` | 0 |
| `date` | 0 |
| `hidden-char` | 0 |
| `mathjax` | 0 |
| `wikilink` | 3 |
| `source_raw` | 0 |
| `entity` | 0 |
| `comparison` | 0 |
| `index` | 0 |

## 问题明细

### wikilink

- `wiki/sources/20260529-ceo-ai-psychosis-equity-podcast.md:65` - `链接目标不存在: [[Jevons-Paradox]]`
- `wiki/sources/20260529-ceo-ai-psychosis-equity-podcast.md:67` - `链接目标不存在: [[Anti-AI-Backlash]]`
- `wiki/sources/20260529-ceo-ai-psychosis-equity-podcast.md:68` - `链接目标不存在: [[Top-Down-vs-Bottom-Up-AI-Adoption]]`

## 运行命令

```bash
uv run --with pyyaml python tools/wiki-lint.py --fix-index --write-report
```

*本报告由 `tools/wiki-lint.py` 生成。*
