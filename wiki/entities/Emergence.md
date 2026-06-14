---
type: entity
title: Emergence
aliases:
  - 涌现
  - 涌现行为
  - Emergent Behavior
definition: "复杂系统中从简单规则和交互中自发产生的宏观行为；在多 agent 系统中，emergent 行为是 agent 独立决策的副产品，而非直接编程的结果"
created: 2026-06-12
updated: 2026-06-12
tags:
  - multi-agent
  - emergence
related_entities:
  - "[[Agent-Heterogeneity]]"
  - "[[Settlement-Mechanism]]"
  - "[[Multi-Agent-System-Pathology]]"
source_raw:
  - "[[20260608-thousand-token-wood-v3]]"
---

> [!definition] 定义
> Emergence（涌现）是复杂系统中从简单规则和交互中自发产生的宏观行为。在多 agent 系统中，emergent 行为是 agent 独立决策的副产品——你设计了规则，但行为是"长出来的"。

## 关键数据点

- Thousand Token Wood: 单模型时 honey crash 自然发生（10→3），无人编程这个结果
- 异质性影响: 换成 5 个不同模型后，同样的 shock 不再产生同样的 emergent 行为
- Emergence 的脆弱性: "Behavior you observe and write up from one population of agents can vanish when you change the population"
- 设计张力: Emergence for texture（让系统有活力）vs authored control for critical moments（保证关键时刻）

## 前提与局限性

- **不可复现性**: Emergent 行为可能只在特定条件下出现，换 population 或换条件后消失
- **不可控性**: 不能通过 shock inputs 可靠地产生 emergent 行为
- **观察者偏差**: 单次 impressive run 可能只是 anecdote，不是 system property
- **与 authored control 的张力**: 过多 authored control 会杀死 emergence；过少则无法保证关键时刻

## 关联概念

- [[Agent-Heterogeneity]] — 异质性让 emergent 行为更不可预测
- [[Settlement-Mechanism]] — 用 authored control 保证 emergent 系统中的关键时刻
- [[Multi-Agent-System-Pathology]] — Emergence 是多 agent 系统的核心特征和核心挑战
