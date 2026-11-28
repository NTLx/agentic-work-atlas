---
type: entity
title: Dreaming
aliases:
  - Dreaming
  - Dreaming V0
  - Dreaming V3
  - ChatGPT Dreaming
  - 后台记忆整理
definition: "OpenAI于2025-04引入、2026-06发布V3的ChatGPT后台记忆综合机制；从获授权的历史及其他可用来源提炼记忆，非模型参数学习或完整用户状态。"
created: 2026-06-06
updated: 2026-11-28
evidence_level: medium
claim_type: mixed
tags:
  - memory-system
  - context-engineering
  - openai
  - personal-ai-assistant
related_entities:
  - "[[OpenAI]]"
  - "[[Memory-Architecture]]"
  - "[[Memory-Synthesis]]"
  - "[[Memory-Summary-Page]]"
  - "[[Staleness-Problem]]"
  - "[[Context-Engineering]]"
  - "[[Multi-Layer-Memory]]"
  - "[[Three-Layer-Agent-Memory]]"
  - "[[Personal-AI-Assistant]]"
  - "[[Memex]]"
source_raw:
  - "[[20260604-openai-dreaming-memory]]"
---

# Dreaming（ChatGPT 后台记忆整理）

> [!definition] 定义
> OpenAI的ChatGPT记忆综合机制，通过后台处理生成、整理和更新跨会话相关信息。睡眠记忆巩固只是命名类比，不是相同生物机制或神经学习证明。

## 演化时间表

| 时间 | 历史阶段 | 证据边界 |
|---|---|---|
| 2024-04 | Saved memories | 会话内强信号触发，包括显式请求；非仅手动记录 |
| 2025-04 | 初版Dreaming | 从聊天历史后台综合，补充saved memories |
| 2026-06-04 | Dreaming V3 | 更高效的记忆架构，开始向美国Plus/Pro推出，其他地区与Free/Go逐步推出；非所有账号同日切换 |

## 设计目标与验证

官方发布将有用上下文的跨会话延续、偏好/约束遵循、时效作为三项评测目标。系统可自动综合不显式要求记录的信息，但仍须区分授权、事实、偏好、计划和实际发生的事件；计划时间过去不证明完成。当前记忆摘要可帮助用户审视和纠正部分状态，非全量来源或内部实现视图。

## 关键数据点

- [OpenAI 2026-06-04官方发布](https://openai.com/index/chatgpt-memory-dreaming/)报告面向Free用户的dreaming计算需求约降至原先1/5；不等于所有套餐、全部记忆操作或总体服务成本降至1/5。原文未披露完整内部算法、存储、任务调度及评测样本，本轮不从图形估算分数。
- [Memory in ChatGPT](https://help.openai.com/en/articles/8590148-memory-in-chatgpt)（2026-11-28回核）明确记忆来源可包括历史聊天、其他可用来源；功能随账号、地区、平台和工作区而异。摘要不穷尽来源，纠正或不再提及与删除不同，完整移除需处理相关摘要和原始来源。训练使用取决于数据控制，并非纠正即提供训练标签。
- [[20260604-openai-dreaming-memory]]已于第53轮校准；当前实体沿用其条件化证据。

## 前提与局限性

后台综合不意味着持续占用GPU或固定频率；成本、错误率、覆盖与更新时间依实际系统。用户画像变化和知识过时需要按证据更新，避免误合并与越权持久化。敏感信息可能进入记忆，应按用途、访问权限、保留与删除策略治理。未运行内部评测或验证具体账号行为。不是模型权重持续学习的证据。

**本库综合**：将后台知识消化理解为状态维护与可验证的编译，而非无限积累；有效性由后续实际使用、来源回查、错误更正和正常知识保留决定。

## 关联概念

- [[Memory-Architecture]]、[[Memory-Synthesis]]、[[Memory-Summary-Page]] — 存储、综合与用户控制。
- [[Staleness-Problem]]、[[Shared-Memory-Contamination]] — 时效与治理。
- [[Context-Engineering]]、[[Agent-Harness]] — 任务上下文组织。
- [[Multi-Layer-Memory]]、[[Three-Layer-Agent-Memory]] — 不同记忆组织方案。
- [[Continual-Learning]] — 需区分外部状态更新与模型权重学习。
- [[Memex]]、[[Personal-AI-Assistant]]、[[OpenAI]] — 历史范式、产品场景与发布者。
