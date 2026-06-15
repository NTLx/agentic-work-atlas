---
type: lint-report
title: "Agentic Work Atlas Lint 报告"
date: "2026-06-15"
score: 100
status: "PASS"
tags:
  - lint-report
  - wiki-maintenance
---

# Agentic Work Atlas Lint 报告 - 2026-06-15

> [!summary] 状态
> 门禁: **PASS**
> 分数: **100/100**
> 阻断问题: **0**

## 统计

| 类别 | 数量 |
|------|------|
| Raw 来源 | 129 |
| Raw 已编译 | 127 |
| Raw 待编译 | 2 |
| Entity | 263 |
| Topic | 28 |
| Comparison | 18 |
| Output | 4 |

## 待编译 Raw

- `raw/20260615-normaltech-ai-hasnt-replaced-software-engineers.md`
- `raw/20260615-satyanadella-frontier-ecosystem.md`

## 检查项

| 检查项 | 问题数 |
|--------|--------|
| `frontmatter` | 0 |
| `date` | 0 |
| `hidden-char` | 0 |
| `mathjax` | 0 |
| `wikilink` | 0 |
| `source_raw` | 0 |
| `tag` | 12 |
| `evidence` | 0 |
| `low-evidence` | 2 |
| `stale-core` | 0 |
| `entity` | 0 |
| `comparison` | 0 |
| `index` | 0 |

## 问题明细

### low-evidence

- `wiki/entities/Jevons-Paradox-for-Knowledge-Work.md` - `低证据页面 Jevons-Paradox-for-Knowledge-Work 只能作为补 source 或探索线索`
- `wiki/entities/Wisdom-Work.md` - `低证据页面 Wisdom-Work 只能作为补 source 或探索线索`

### tag

- `index.md` - `一次性 tag 仅出现 1 次: 'MOC'`
- `wiki/research-agenda.md` - `一次性 tag 仅出现 1 次: 'agentic-work-atlas'`
- `wiki/entities/Societal-Resilience.md` - `一次性 tag 仅出现 1 次: 'biodefense'`
- `wiki/sources/20260608-paving-the-way-for-agents-in-biology.md` - `一次性 tag 仅出现 1 次: 'biology'`
- `index.md` - `一次性 tag 仅出现 1 次: 'index'`
- `wiki/entities/Collingridge-Dilemma.md` - `一次性 tag 仅出现 1 次: 'policy'`
- `wiki/outputs/deploy-obsidian-wiki-with-quartz.md` - `一次性 tag 仅出现 1 次: 'quartz'`
- `wiki/research-agenda.md` - `一次性 tag 仅出现 1 次: 'research-agenda'`
- `wiki/entities/Societal-Resilience.md` - `一次性 tag 仅出现 1 次: 'resilience'`
- `wiki/sources/20260608-paving-the-way-for-agents-in-biology.md` - `一次性 tag 仅出现 1 次: 'scientific-agents'`
- `wiki/entities/Collingridge-Dilemma.md` - `一次性 tag 仅出现 1 次: 'technology-governance'`
- `wiki/outputs/deploy-obsidian-wiki-with-quartz.md` - `一次性 tag 仅出现 1 次: 'tutorial'`

## 运行命令

```bash
uv run --with pyyaml python tools/wiki-lint.py --fix-index --write-report
```

*本报告由 `tools/wiki-lint.py` 生成。*
