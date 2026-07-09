---
type: lint-report
title: "Agentic Work Atlas Lint 报告"
date: "2026-07-10"
score: 86
status: "FAIL"
tags:
  - lint-report
  - wiki-maintenance
---

# Agentic Work Atlas Lint 报告 - 2026-07-10

> [!summary] 状态
> 门禁: **FAIL**
> 分数: **86/100**
> 阻断问题: **14**

## 统计

| 类别 | 数量 |
|------|------|
| Raw 来源 | 187 |
| Raw 已编译 | 187 |
| Raw 待编译 | 0 |
| Raw 已跳过 | 0 |
| Entity | 318 |
| Topic | 33 |
| Comparison | 19 |
| Output | 5 |

## 检查项

| 检查项 | 问题数 |
|--------|--------|
| `frontmatter` | 0 |
| `date` | 0 |
| `hidden-char` | 0 |
| `mathjax` | 1 |
| `wikilink` | 7 |
| `source_raw` | 0 |
| `tag` | 10 |
| `evidence` | 0 |
| `low-evidence` | 0 |
| `stale-core` | 0 |
| `entity` | 6 |
| `comparison` | 0 |
| `index` | 0 |
| `registry-consistency` | 0 |

## 问题明细

### entity

- `wiki/entities/Goodharts-Law.md` - `概念 Entity 缺少章节: ## 关键数据点`
- `wiki/entities/Incidental-Learning.md` - `概念 Entity 缺少章节: ## 关键数据点`
- `wiki/entities/Knowledge-Debt.md` - `概念 Entity 缺少章节: ## 关键数据点`
- `wiki/entities/Pro-Worker-AI.md` - `概念 Entity 缺少章节: ## 关键数据点`
- `wiki/entities/SHIELD.md` - `概念 Entity 缺少章节: ## 关键数据点`
- `wiki/entities/Task-Framework.md` - `概念 Entity 缺少章节: ## 关键数据点`

### mathjax

- `wiki/research/research-logs/inventory-20260709.md:164` - `发现裸露 $，需用反引号包裹或反斜杠转义`

### tag

- `wiki/topics/Skill-Atrophy-and-Knowledge-Debt.md` - `一次性 tag 仅出现 1 次: 'cognitive-offloading'`
- `wiki/sources/20260624-loops-rediscovering-cybernetics.md` - `一次性 tag 仅出现 1 次: 'conceptual-framework'`
- `wiki/sources/20260624-loops-rediscovering-cybernetics.md` - `一次性 tag 仅出现 1 次: 'control-theory'`
- `wiki/sources/20260624-loops-rediscovering-cybernetics.md` - `一次性 tag 仅出现 1 次: 'cybernetics'`
- `wiki/research/research-logs/inventory-20260709.md` - `一次性 tag 仅出现 1 次: 'deep-exploration'`
- `wiki/sources/20260611-loss-function-development.md` - `一次性 tag 仅出现 1 次: 'loss-function-development'`
- `wiki/entities/SHIELD.md` - `一次性 tag 仅出现 1 次: 'multi-agent-system'`
- `wiki/entities/Loss-Function-Development.md` - `一次性 tag 仅出现 1 次: 'product-strategy'`
- `wiki/sources/20260611-loss-function-development.md` - `一次性 tag 仅出现 1 次: 'reward-hacking'`
- `wiki/entities/SHIELD.md` - `一次性 tag 仅出现 1 次: 'shield'`

### wikilink

- `wiki/entities/Goodharts-Law.md:73` - `链接目标不存在: [[Reward-Hacking|reward hacking]]`
- `wiki/entities/Goodharts-Law.md:98` - `链接目标不存在: [[Reward-Hacking]]`
- `wiki/entities/Incidental-Learning.md:78` - `链接目标不存在: [[Cognitive-Offloading]]`
- `wiki/sources/20260706-goodharts-law-tyranny-of-metrics.md:27` - `链接目标不存在: [[Reward-Hacking|reward hacking]]`
- `wiki/sources/20260706-goodharts-law-tyranny-of-metrics.md:36` - `链接目标不存在: [[Reward-Hacking|reward hacking]]`
- `wiki/sources/20260706-goodharts-law-tyranny-of-metrics.md:44` - `链接目标不存在: [[Reward-Hacking]]`
- `wiki/sources/20260709-agents-that-teach-knowledge-debt.md:63` - `链接目标不存在: [[Cognitive-Offloading]]`

## 运行命令

```bash
uv run --with pyyaml python tools/wiki-lint.py --fix-index --write-report
```

*本报告由 `tools/wiki-lint.py` 生成。*
