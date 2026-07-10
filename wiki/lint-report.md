---
type: lint-report
title: "Agentic Work Atlas Lint 报告"
date: "2026-07-11"
score: 100
status: "PASS"
tags:
  - lint-report
  - wiki-maintenance
---

# Agentic Work Atlas Lint 报告 - 2026-07-11

> [!summary] 状态
> 门禁: **PASS**
> 分数: **100/100**
> 阻断问题: **0**

## 统计

| 类别 | 数量 |
|------|------|
| Raw 来源 | 191 |
| Raw 已编译 | 187 |
| Raw 待编译 | 4 |
| Raw 已跳过 | 0 |
| Entity | 320 |
| Topic | 33 |
| Comparison | 19 |
| Output | 5 |

## 待编译 Raw

- `raw/20260708-agent-loop-bytebytego.md`
- `raw/20260708-bun-in-rust.md`
- `raw/20260708-vercel-agent.md`
- `raw/20260709-github-durable-owner.md`

## 检查项

| 检查项 | 问题数 |
|--------|--------|
| `frontmatter` | 0 |
| `date` | 0 |
| `hidden-char` | 0 |
| `mathjax` | 0 |
| `wikilink` | 0 |
| `source_raw` | 0 |
| `tag` | 0 |
| `evidence` | 0 |
| `low-evidence` | 0 |
| `stale-core` | 0 |
| `entity` | 0 |
| `comparison` | 0 |
| `index` | 0 |
| `registry-consistency` | 0 |

## 问题明细

未发现阻断问题。

## 运行命令

```bash
uv run --with pyyaml python tools/wiki-lint.py --fix-index --write-report
```

*本报告由 `tools/wiki-lint.py` 生成。*
