---
type: lint-report
title: "Agentic Work Atlas Lint 报告"
date: "2026-06-13"
score: 98
status: "FAIL"
tags:
  - lint-report
  - wiki-maintenance
---

# Agentic Work Atlas Lint 报告 - 2026-06-13

> [!summary] 状态
> 门禁: **FAIL**
> 分数: **98/100**
> 阻断问题: **2**

## 统计

| 类别 | 数量 |
|------|------|
| Raw 来源 | 125 |
| Raw 已编译 | 121 |
| Raw 待编译 | 4 |
| Entity | 262 |
| Topic | 28 |
| Comparison | 18 |
| Output | 4 |

## 待编译 Raw

- `raw/20260603-lessons-from-building-claude-code-how-we-use-skills.md`
- `raw/20260605-how-anthropic-uses-claude-gtm-engineering.md`
- `raw/20260608-connector-observability-directory.md`
- `raw/20260609-whats-new-in-claude-managed-agents.md`

## 检查项

| 检查项 | 问题数 |
|--------|--------|
| `frontmatter` | 1 |
| `date` | 0 |
| `hidden-char` | 0 |
| `mathjax` | 0 |
| `wikilink` | 1 |
| `source_raw` | 0 |
| `entity` | 0 |
| `comparison` | 0 |
| `index` | 0 |

## 问题明细

### frontmatter

- `wiki/entities/Progressive-Disclosure.md:1` - `YAML 解析失败: while parsing a block collection
  in "<unicode string>", line 22, column 3:
      - "[[深度解析LLM Wiki  Obsidian-Wiki ... 
      ^
expected <block end>, but found '<scalar>'
  in "<unicode string>", line 22, column 55:
     ... bsidian-Wiki  GBrain：Agent时代知识的"自组织"与"自进化"]]"
                                         ^`

### wikilink

- `wiki/lint-report.md:59` - `链接目标不存在: [[深度解析LLM Wiki  Obsidian-Wiki ... 
      ^
expected <block end>, but found '<scalar>'
  in "<unicode string>", line 22, column 55:
     ... bsidian-Wiki  GBrain：Agent时代知识的"自组织"与"自进化"]]`

## 运行命令

```bash
uv run --with pyyaml python tools/wiki-lint.py --fix-index --write-report
```

*本报告由 `tools/wiki-lint.py` 生成。*
