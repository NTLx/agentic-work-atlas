---
type: lint-report
title: "Agentic Work Atlas Lint 报告"
date: "2026-07-16"
score: 100
status: "PASS"
tags:
  - lint-report
  - wiki-maintenance
---

# Agentic Work Atlas Lint 报告 - 2026-07-16

> [!summary] 状态
> 门禁: **PASS**
> 分数: **100/100**
> 阻断问题: **0**

## 统计

| 类别 | 数量 |
|------|------|
| Raw 来源 | 195 |
| Raw 已编译 | 194 |
| Raw 待编译 | 1 |
| Raw 已跳过 | 0 |
| Entity | 329 |
| Topic | 33 |
| Comparison | 19 |
| Output | 5 |

## 待编译 Raw

- `raw/vibe-coding成瘾之后重建AI与生活的边界.md`

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
| `low-evidence` | 0 |
| `stale-core` | 5 |
| `entity` | 0 |
| `comparison` | 0 |
| `index` | 0 |
| `registry-consistency` | 0 |

## 问题明细

### stale-core

- `wiki/entities/Agent-Workflow-Patterns.md` - `核心页 Agent-Workflow-Patterns 已 92 天未更新，入链 16 条`
- `wiki/entities/Dan-Shipper.md` - `核心页 Dan-Shipper 已 91 天未更新，入链 6 条`
- `wiki/entities/Discernment.md` - `核心页 Discernment 已 92 天未更新，入链 10 条`
- `wiki/entities/Memex.md` - `核心页 Memex 已 92 天未更新，入链 15 条`
- `wiki/entities/Specificity.md` - `核心页 Specificity 已 92 天未更新，入链 10 条`

### tag

- `wiki/sources/20260713-martin-fowler-fragments-july-2026.md` - `一次性 tag 仅出现 1 次: 'agent-management'`
- `wiki/research/research-logs/exploration-20260714.md` - `一次性 tag 仅出现 1 次: 'exploration'`
- `wiki/research/research-logs/exploration-20260714.md` - `一次性 tag 仅出现 1 次: 'external-signals'`
- `wiki/sources/20260713-microsoft-ships-ai-agents-enterprise-scale.md` - `一次性 tag 仅出现 1 次: 'microsoft'`
- `wiki/entities/Self-Hosted-Models.md` - `一次性 tag 仅出现 1 次: 'models'`
- `wiki/sources/20260709-github-durable-owner.md` - `一次性 tag 仅出现 1 次: 'organization-systems'`
- `wiki/sources/20260708-vercel-agent.md` - `一次性 tag 仅出现 1 次: 'production-ops'`
- `wiki/entities/Rubric-Based-Evaluation.md` - `一次性 tag 仅出现 1 次: 'quality'`
- `wiki/research/research-logs/research-snapshot-20260714.md` - `一次性 tag 仅出现 1 次: 'research-snapshot'`
- `wiki/sources/20260713-martin-fowler-fragments-july-2026.md` - `一次性 tag 仅出现 1 次: 'self-hosted-models'`
- `wiki/entities/Self-Hosted-Models.md` - `一次性 tag 仅出现 1 次: 'sovereignty'`
- `wiki/sources/20260713-martin-fowler-fragments-july-2026.md` - `一次性 tag 仅出现 1 次: 'thoughtworks'`

## 运行命令

```bash
uv run --with pyyaml python tools/wiki-lint.py --fix-index --write-report
```

*本报告由 `tools/wiki-lint.py` 生成。*
