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
| `tag` | 38 |
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
- `wiki/entities/Vocabulary-Building.md` - `一次性 tag 仅出现 1 次: 'software-development-process'`
- `wiki/entities/Layered-AI-Sourcing.md` - `一次性 tag 仅出现 1 次: 'sourcing'`
- `wiki/entities/Model-Context-Protocol-MCP.md` - `一次性 tag 仅出现 1 次: 'standard'`
- `wiki/sources/The-Founders-Playbook-05062026_v3.md` - `一次性 tag 仅出现 1 次: 'startups'`
- `wiki/entities/Unified-Model-Strategy.md` - `一次性 tag 仅出现 1 次: 'strategy'`
- `wiki/entities/Tool-Use-Architecture.md` - `一次性 tag 仅出现 1 次: 'system-architecture'`
- `wiki/entities/Integration-Wall.md` - `一次性 tag 仅出现 1 次: 'systems-integration'`
- `wiki/entities/Cross-Disciplinary-Generalist.md` - `一次性 tag 仅出现 1 次: 'team-building'`
- `wiki/entities/Collingridge-Dilemma.md` - `一次性 tag 仅出现 1 次: 'technology-governance'`
- `wiki/sources/Harness, Scaffold, and the AI Agent Terms Worth Getting Right.md` - `一次性 tag 仅出现 1 次: 'terminology'`
- `wiki/entities/Andrej-Karpathy.md` - `一次性 tag 仅出现 1 次: 'tesla'`
- `wiki/topics/Karpathy-AI-Thought.md` - `一次性 tag 仅出现 1 次: 'thought-leader'`
- `wiki/entities/Martin-Fowler.md` - `一次性 tag 仅出现 1 次: 'thoughtworks'`
- `wiki/entities/ACI-Agent-Computer-Interface.md` - `一次性 tag 仅出现 1 次: 'tool-design'`
- `wiki/sources/Designing the hf CLI as an agent-optimized way to work with the Hub.md` - `一次性 tag 仅出现 1 次: 'tooling'`
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
