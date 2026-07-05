---
type: lint-report
title: "Agentic Work Atlas Lint 报告"
date: "2026-07-05"
score: 96
status: "FAIL"
tags:
  - lint-report
  - wiki-maintenance
---

# Agentic Work Atlas Lint 报告 - 2026-07-05

> [!summary] 状态
> 门禁: **FAIL**
> 分数: **96/100**
> 阻断问题: **4**

## 统计

| 类别 | 数量 |
|------|------|
| Raw 来源 | 176 |
| Raw 已编译 | 154 |
| Raw 待编译 | 22 |
| Raw 已跳过 | 0 |
| Entity | 302 |
| Topic | 31 |
| Comparison | 19 |
| Output | 5 |

## 待编译 Raw

- `raw/2026-ai-agent-evaluation-pipeline-methodology.md`
- `raw/2026-ai-agent-protocol-ecosystem-map-mcp-a2a-acp-ucp.md`
- `raw/2026-eu-ai-act-compliance-autonomous-agents.md`
- `raw/202602-ai-agent-frameworks-langgraph-crewai-autogen-comparison.md`
- `raw/20260330-reward-hacking-equilibrium-finite-evaluation.md`
- `raw/20260512-finops-for-ai-token-level-visibility.md`
- `raw/202606-finops-x-2026-ai-tokenomics.md`
- `raw/20260623-ibm-cuga-agent-harness.md`
- `raw/20260623-qwen-agentworld-language-world-models.md`
- `raw/20260624-gemini-3-5-flash-computer-use.md`
- `raw/20260630-loop-engineering-andrew-ng.md`
- `raw/20260702-agent-assisted-sglang-development.md`
- `raw/20260702-ai-layoffs-reversed.md`
- `raw/20260702-anthropic-context-engineering.md`
- `raw/20260702-anthropic-harnesses-long-running-agents.md`
- `raw/20260702-qwen-agent-harness-practice.md`
- `raw/20260703-anthropic-skill-engineering-practices.md`
- `raw/20260703-fable-field-guide-finding-unknowns.md`
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
| `wikilink` | 4 |
| `source_raw` | 0 |
| `tag` | 3 |
| `evidence` | 0 |
| `low-evidence` | 0 |
| `stale-core` | 0 |
| `entity` | 0 |
| `comparison` | 0 |
| `index` | 0 |
| `registry-consistency` | 0 |

## 问题明细

### tag

- `wiki/sources/20260703-fable-field-guide-finding-unknowns.md` - `一次性 tag 仅出现 1 次: 'fable-5'`
- `wiki/sources/20260703-fable-field-guide-finding-unknowns.md` - `一次性 tag 仅出现 1 次: 'human-agent-collaboration'`
- `wiki/sources/20260703-fable-field-guide-finding-unknowns.md` - `一次性 tag 仅出现 1 次: 'unknowns'`

### wikilink

- `wiki/sources/20260703-fable-field-guide-finding-unknowns.md:42` - `链接目标不存在: [[Unknowns-Framework]]`
- `wiki/sources/20260703-fable-field-guide-finding-unknowns.md:43` - `链接目标不存在: [[Agentic-Coding]]`
- `wiki/sources/20260703-fable-field-guide-finding-unknowns.md:45` - `链接目标不存在: [[Human-Agent-Collaboration]]`
- `wiki/sources/20260703-fable-field-guide-finding-unknowns.md:46` - `链接目标不存在: [[Skill-Engineering]]`

## 运行命令

```bash
uv run --with pyyaml python tools/wiki-lint.py --fix-index --write-report
```

*本报告由 `tools/wiki-lint.py` 生成。*
