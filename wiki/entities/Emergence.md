---
type: entity
title: Emergence
aliases:
  - 涌现
  - 涌现行为
  - Emergent Behavior
definition: "复杂系统中从简单规则和交互中自发产生的宏观行为；在多 agent 系统中，emergent 行为是 agent 独立决策的副产品，而非直接编程的结果"
created: 2026-06-12
updated: 2026-11-28
evidence_level: medium
claim_type: mixed
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
- 作者重建为 5 角色 council（列举 4 类模型，其中自微调模型驱动两角色）并改变操作侧，观察到不同价格行为；未隔离模型异质性的因果作用。
- Emergence 的脆弱性: "Behavior you observe and write up from one population of agents can vanish when you change the population"
- 设计张力: Emergence for texture（让系统有活力）vs authored control for critical moments（保证关键时刻）

## 前提与局限性

- **不可复现性**: Emergent 行为可能只在特定条件下出现，换 population 或换条件后消失
- **控制边界**: 该游戏三次输入干预未达作者目标，不证明所有输入干预无效。
- **观察者偏差**: 单次 impressive run 可能只是 anecdote，不是 system property
- **与 authored control 的张力**: 硬编码约束与开放行为可以组合，需按实际规则、目标及副作用验证，不能保证所有关键结果。

## 关联概念

- [[Agent-Heterogeneity]] — 异质性可能改变涌现行为，不能先验确定方向
- [[Settlement-Mechanism]] — 游戏结算点的规则化结果覆盖；不等于生产系统正确性保证
- [[Multi-Agent-System-Pathology]] — Emergence 是多 agent 系统的核心特征和核心挑战
