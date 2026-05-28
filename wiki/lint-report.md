---
type: lint-report
title: "Agentic Work Atlas Lint 报告"
date: "2026-05-28"
score: 93
status: "FAIL"
tags:
  - lint-report
  - wiki-maintenance
---

# Agentic Work Atlas Lint 报告 - 2026-05-28

> [!summary] 状态
> 门禁: **FAIL**
> 分数: **93/100**
> 阻断问题: **7**

## 统计

| 类别 | 数量 |
|------|------|
| Raw 来源 | 75 |
| Raw 已编译 | 75 |
| Raw 待编译 | 0 |
| Entity | 199 |
| Topic | 26 |
| Comparison | 14 |
| Output | 5 |

## 检查项

| 检查项 | 问题数 |
|--------|--------|
| `frontmatter` | 0 |
| `date` | 1 |
| `hidden-char` | 0 |
| `mathjax` | 0 |
| `wikilink` | 0 |
| `source_raw` | 6 |
| `entity` | 0 |
| `comparison` | 0 |
| `index` | 0 |

## 问题明细

### date

- `raw/How we contain Claude across products.md` - `published 不能为空`

### source_raw

- `wiki/entities/Agentic-Engineering.md` - `source_raw 必须使用 wikilink 短链接: '‘[[Using Git with coding agents - Agentic Engineering Patterns]]’'`
- `wiki/entities/Agentic-Engineering.md` - `source_raw 必须使用 wikilink 短链接: '‘[[What is agentic engineering? - Agentic Engineering Patterns]]’'`
- `wiki/entities/Agentic-Engineering.md` - `source_raw 必须使用 wikilink 短链接: '‘[[20260413-why-ai-first-strategy-wrong]]’'`
- `wiki/entities/Agentic-Engineering.md` - `source_raw 必须使用 wikilink 短链接: '‘[[20260409-ai-capability-gap-ai-psychosis]]’'`
- `wiki/entities/Agentic-Engineering.md` - `source_raw 必须使用 wikilink 短链接: '‘[[工程师抗拒被"蒸馏"，企业的Skills从何而来？五大招破局]]’'`
- `wiki/entities/Agentic-Engineering.md` - `source_raw 必须使用 wikilink 短链接: '‘[[The Anatomy of an Agent Harness]]’'`

## 运行命令

```bash
uv run --with pyyaml python tools/wiki-lint.py --fix-index --write-report
```

*本报告由 `tools/wiki-lint.py` 生成。*
