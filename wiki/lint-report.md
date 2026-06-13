---
type: lint-report
title: "Agentic Work Atlas Lint 报告"
date: "2026-06-13"
score: 94
status: "FAIL"
tags:
  - lint-report
  - wiki-maintenance
---

# Agentic Work Atlas Lint 报告 - 2026-06-13

> [!summary] 状态
> 门禁: **FAIL**
> 分数: **94/100**
> 阻断问题: **6**

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
| `frontmatter` | 1 |
| `date` | 0 |
| `hidden-char` | 0 |
| `mathjax` | 0 |
| `wikilink` | 5 |
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
- `wiki/sources/20260603-lessons-from-building-claude-code-how-we-use-skills.md:39` - `链接目标不存在: [[Skills]]`
- `wiki/sources/20260603-lessons-from-building-claude-code-how-we-use-skills.md:40` - `链接目标不存在: [[Claude-Code]]`
- `wiki/sources/20260603-lessons-from-building-claude-code-how-we-use-skills.md:41` - `链接目标不存在: [[Agent-Harness-Engineering]]`
- `wiki/sources/20260605-how-anthropic-uses-claude-gtm-engineering.md:38` - `链接目标不存在: [[GTM-Engineering]]`

## 运行命令

```bash
uv run --with pyyaml python tools/wiki-lint.py --fix-index --write-report
```

*本报告由 `tools/wiki-lint.py` 生成。*
