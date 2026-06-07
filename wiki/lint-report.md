---
type: lint-report
title: "Agentic Work Atlas Lint 报告"
date: "2026-06-07"
score: 100
status: "PASS"
tags:
  - lint-report
  - wiki-maintenance
---

# Agentic Work Atlas Lint 报告 - 2026-06-07

> [!summary] 状态
> 门禁: **PASS**
> 分数: **100/100**
> 阻断问题: **0**

## 统计

| 类别 | 数量 |
|------|------|
| Raw 来源 | 108 |
| Raw 已编译 | 108 |
| Raw 待编译 | 0 |
| Entity | 271 |
| Topic | 27 |
| Comparison | 17 |
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
| `entity` | 0 |
| `comparison` | 0 |
| `index` | 0 |

## 问题明细

未发现阻断问题。

## 价值基线审查

### 本轮基线

- `raw` 必须直接服务于“AI / Agent 如何重写工作系统”，且优先提供机制、案例、约束或失败模式，而不是抽象价值抒情。
- `entity` 必须是可复用的概念节点，或在知识网络中承担稳定解释作用；只服务单篇来源的一次性人物页、作者页，不再默认保留。
- 已有更强 topic/实体能够承载的判断，不再保留一套更弱、更虚、重复的平行表达。

### 本轮清理

- 删除 1 篇偏离主线且与现有主题重复的 raw：`The Conscious 1% Leading a new renaissance in the era of AI`
- 连带删除其 source summary、1 个重复 topic，以及 4 个主要由该文派生的弱实体：`Conscious-Creators`、`Inner-World-Mastery`、`Resonance`、`Wes-Botman`
- 删除 4 个未进入知识网络、只承担单篇作者标注作用的人物实体：`Arnav-Gupta`、`Jacob-Harris`、`Joe-Hudson`、`Pimenta-de-Freitas-Cardoso`
- 保留但重写 `Decision-Quality`，将其从“内在状态”表述改为“任务分配、验收与追责”的工作系统表述，并改挂更强来源

### 处理原则

- 这次没有清理 `Wisdom-Work`、`AI-Amish`、`Choosing to Stay Human` 等边界内容，因为它们仍然能回到“人的判断、克制与工作方式”这一主线，且已有跨页复用。
- 低复用不自动等于低价值；只有当“低复用 + 单篇依附 + 弱机制/弱解释力”同时出现时，才作为明显低于基线处理。

## 运行命令

```bash
uv run --with pyyaml python tools/wiki-lint.py --fix-index --write-report
```

*本报告由 `tools/wiki-lint.py` 生成。*
