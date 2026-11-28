---
type: entity
title: Agent Heterogeneity
aliases:
  - Agent 异质性
  - 异构 Agent
definition: "多 Agent 系统中模型、角色、上下文或策略存在差异；这种差异可能改变相关错误、协调成本及系统行为，实际影响需按任务验证。"
created: 2026-06-12
updated: 2026-11-28
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
> Agent 异质性指多 agent 系统中使用不同架构、不同厂商的模型驱动不同 agent。模型与角色差异可能改变行为分布，但不能推出独立决策、错误不相关或整体必然更不可预测。

## 关键数据点

- Thousand Token Wood 作者描述 5 个游戏角色，列举 OpenAI、NVIDIA、OpenBMB 和自微调模型（后者驱动两个角色）；不能当作 5 个独立模型或 5 家厂商的证据。
- 作者报告单模型设置价格 10→3，重建为异构 council 后价格上涨；同文还描述操作界面与玩法重建，非单变量受控实验。
- 异构 agent 的"拒绝权": 在该游戏实现中，模型未按作者预期响应输入；不是独立意志或普遍不服从的证据。
- 测试策略失效: rule-based test policy 在异构环境下与真实 agent 行为不一致

## 前提与局限性

- **实验规模小**: 只有 5 个 agent，是否能推广到更大规模存疑
- **游戏化环境**: Woodland 经济是简化的游戏环境，真实世界更复杂
- **模型版本依赖**: 实验使用特定模型版本，换模型可能结果不同
- **"拒绝"的模糊性**: Agent "拒绝"执行可能是因为 prompt 问题，而非原则性拒绝

## 关联概念

- [[Multi-Agent-System-Pathology]] — 异质性是多 agent 系统的核心特征之一
- [[Emergence]] — 异质性可能改变涌现行为，方向与幅度待验证
- [[Settlement-Mechanism]] — 该游戏在结算点硬编码指定结果，不能由此推出异构系统必需覆盖结果
