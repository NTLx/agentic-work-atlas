---
type: lint-report
title: "Agentic Work Atlas Lint 报告"
date: "2026-06-14"
score: 100
status: "PASS"
tags:
  - lint-report
  - wiki-maintenance
---

# Agentic Work Atlas Lint 报告 - 2026-06-14

> [!summary] 状态
> 门禁: **PASS**
> 分数: **100/100**
> 阻断问题: **0**

## 统计

| 类别 | 数量 |
|------|------|
| Raw 来源 | 127 |
| Raw 已编译 | 127 |
| Raw 待编译 | 0 |
| Entity | 263 |
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
| `tag` | 24 |
| `evidence` | 0 |
| `low-evidence` | 0 |
| `stale-core` | 0 |
| `entity` | 0 |
| `comparison` | 0 |
| `index` | 0 |

## 问题明细

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
- `wiki/entities/Messy-Middle.md` - `一次性 tag 仅出现 1 次: 'transition'`
- `wiki/entities/Memory-Summary-Page.md` - `一次性 tag 仅出现 1 次: 'trust'`
- `wiki/outputs/deploy-obsidian-wiki-with-quartz.md` - `一次性 tag 仅出现 1 次: 'tutorial'`
- `wiki/sources/20260613-ontology-for-agent-optimization.md` - `一次性 tag 仅出现 1 次: 'umodel'`
- `wiki/entities/Konstantine-Buhler.md` - `一次性 tag 仅出现 1 次: 'venture-capital'`
- `wiki/entities/Guillermo-Rauch.md` - `一次性 tag 仅出现 1 次: 'vercel'`
- `wiki/sources/20260610-anthropic-ai-exploits-security-patches.md` - `一次性 tag 仅出现 1 次: 'vulnerability'`
- `wiki/entities/Intrinsic-Wealth-Accumulation.md` - `一次性 tag 仅出现 1 次: 'wealth-distribution'`
- `wiki/entities/LLM-Wiki.md` - `一次性 tag 仅出现 1 次: 'wiki'`
- `wiki/entities/Knowledge-Work.md` - `一次性 tag 仅出现 1 次: 'work'`
- `wiki/sources/building-effective-agents-complete.md` - `一次性 tag 仅出现 1 次: 'workflows'`
- `wiki/entities/Specificity.md` - `一次性 tag 仅出现 1 次: 'writing'`
- `wiki/sources/Inside PG AI Factory and the Push to Operationalize AI at Scale.md` - `一次性 tag 仅出现 1 次: 'youtube-transcript'`

## 运行命令

```bash
uv run --with pyyaml python tools/wiki-lint.py --fix-index --write-report
```

*本报告由 `tools/wiki-lint.py` 生成。*
