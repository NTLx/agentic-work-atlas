---
type: lint-report
title: "Agentic Work Atlas Lint 报告"
date: "2026-07-14"
score: 95
status: "FAIL"
tags:
  - lint-report
  - wiki-maintenance
---

# Agentic Work Atlas Lint 报告 - 2026-07-14

> [!summary] 状态
> 门禁: **FAIL**
> 分数: **95/100**
> 阻断问题: **5**

## 统计

| 类别 | 数量 |
|------|------|
| Raw 来源 | 194 |
| Raw 已编译 | 194 |
| Raw 待编译 | 0 |
| Raw 已跳过 | 0 |
| Entity | 328 |
| Topic | 33 |
| Comparison | 19 |
| Output | 5 |

## 检查项

| 检查项 | 问题数 |
|--------|--------|
| `frontmatter` | 0 |
| `date` | 0 |
| `hidden-char` | 0 |
| `mathjax` | 0 |
| `wikilink` | 1 |
| `source_raw` | 0 |
| `tag` | 9 |
| `evidence` | 0 |
| `low-evidence` | 0 |
| `stale-core` | 4 |
| `entity` | 4 |
| `comparison` | 0 |
| `index` | 0 |
| `registry-consistency` | 0 |

## 问题明细

### entity

- `wiki/entities/Agent-Unit-of-Work.md` - `概念 Entity 缺少章节: ## 关键数据点`
- `wiki/entities/Retrieval-as-a-Subagent.md` - `概念 Entity 缺少章节: ## 关键数据点`
- `wiki/entities/Rubric-Based-Evaluation.md` - `概念 Entity 缺少章节: ## 关键数据点`
- `wiki/entities/Self-Hosted-Models.md` - `概念 Entity 缺少章节: ## 关键数据点`

### stale-core

- `wiki/entities/Agent-Workflow-Patterns.md` - `核心页 Agent-Workflow-Patterns 已 90 天未更新，入链 16 条`
- `wiki/entities/Discernment.md` - `核心页 Discernment 已 90 天未更新，入链 10 条`
- `wiki/entities/Memex.md` - `核心页 Memex 已 90 天未更新，入链 15 条`
- `wiki/entities/Specificity.md` - `核心页 Specificity 已 90 天未更新，入链 10 条`

### tag

- `wiki/sources/20260713-martin-fowler-fragments-july-2026.md` - `一次性 tag 仅出现 1 次: 'agent-management'`
- `wiki/sources/20260713-microsoft-ships-ai-agents-enterprise-scale.md` - `一次性 tag 仅出现 1 次: 'microsoft'`
- `wiki/entities/Self-Hosted-Models.md` - `一次性 tag 仅出现 1 次: 'models'`
- `wiki/sources/20260709-github-durable-owner.md` - `一次性 tag 仅出现 1 次: 'organization-systems'`
- `wiki/sources/20260708-vercel-agent.md` - `一次性 tag 仅出现 1 次: 'production-ops'`
- `wiki/entities/Rubric-Based-Evaluation.md` - `一次性 tag 仅出现 1 次: 'quality'`
- `wiki/sources/20260713-martin-fowler-fragments-july-2026.md` - `一次性 tag 仅出现 1 次: 'self-hosted-models'`
- `wiki/entities/Self-Hosted-Models.md` - `一次性 tag 仅出现 1 次: 'sovereignty'`
- `wiki/sources/20260713-martin-fowler-fragments-july-2026.md` - `一次性 tag 仅出现 1 次: 'thoughtworks'`

### wikilink

- `wiki/sources/20260713-microsoft-ships-ai-agents-enterprise-scale.md:53` - `链接目标不存在: [[Agent-Identity]]`

## 运行命令

```bash
uv run --with pyyaml python tools/wiki-lint.py --fix-index --write-report
```

*本报告由 `tools/wiki-lint.py` 生成。*
