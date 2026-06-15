---
type: entity
title: Agent Heterogeneity
aliases:
  - Agent 异质性
  - 异构 Agent
definition: "多 agent 系统中使用不同架构/厂商的模型驱动不同 agent，每个 agent 有独立的决策倾向；异质性让 emergent 行为更不可预测，但也更接近真实世界"
created: 2026-06-12
updated: 2026-06-16
evidence_level: medium
claim_type: mixed
tags:
  - multi-agent
  - emergence
  - small-models
related_entities:
  - "[[Multi-Agent-System-Pathology]]"
  - "[[Emergence]]"
  - "[[Settlement-Mechanism]]"
source_raw:
  - "[[20260608-thousand-token-wood-v3]]"
---

> [!definition] 定义
> Agent 异质性指多 agent 系统中使用不同架构、不同厂商的模型驱动不同 agent。每个模型有自己的决策倾向和行为模式，导致系统整体行为更不可预测。

## 关键数据点

- Thousand Token Wood 实验: 5 个 agent 分别由 OpenAI、NVIDIA、OpenBMB、自微调模型驱动
- 单模型 vs 异构: 单模型时 honey crash 自然发生（10→3），异构 council 后 crash 消失
- 异构 agent 的"拒绝权": 外部 shock（rumor、windfall）只 bias 选择，agent 可以不执行
- 测试策略失效: rule-based test policy 在异构环境下与真实 agent 行为不一致

## 前提与局限性

- **实验规模小**: 只有 5 个 agent，是否能推广到更大规模存疑
- **游戏化环境**: Woodland 经济是简化的游戏环境，真实世界更复杂
- **模型版本依赖**: 实验使用特定模型版本，换模型可能结果不同
- **"拒绝"的模糊性**: Agent "拒绝"执行可能是因为 prompt 问题，而非原则性拒绝

## 关联概念

- [[Multi-Agent-System-Pathology]] — 异质性是多 agent 系统的核心特征之一
- [[Emergence]] — 异质性让 emergent 行为更不可预测
- [[Settlement-Mechanism]] — 异质环境下需要 authored control 来保证关键时刻
