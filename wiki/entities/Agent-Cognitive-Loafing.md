---
type: entity
title: Agent Cognitive Loafing
aliases:
  - "Agent Cognitive Loafing"
  - "Agent 认知偷懒"
  - "多 Agent 旁观者效应"
definition: "多 Agent 协作中单个 Agent 因为群体在场而降低推理投入、放弃坚持正确答案或默认其他 Agent 会补位的责任稀释现象"
created: 2026-05-23
updated: 2026-05-23
tags:
  - AI-Agent
  - multi-agent
  - evaluation
related_entities:
  - "[[Multi-Agent-System-Pathology]]"
  - "[[Agent-Orchestration]]"
  - "[[Agent-Dissociation]]"
  - "[[Verifiability]]"
source_raw:
  - "[[Multi-Agent 火了，但 AI 的组织病还没人治｜Hao好聊趋势]]"
---

# Agent Cognitive Loafing（Agent 认知偷懒）

> [!definition] 定义
> **Agent Cognitive Loafing** 是多 Agent 协作中单个 Agent 因为群体在场而降低推理投入、放弃坚持正确答案或默认其他 Agent 会补位的责任稀释现象。它类似人类组织中的旁观者效应，但在这里表现为推理责任被系统结构稀释。

## 关键数据点

- 文章引用 Dahlia Shehata 和 Ming Li 的 multi-agent reasoning 研究，将这种现象称为 cognitive loafing。
- 该问题不同于从众：从众是 Agent 被多数意见牵引，认知偷懒是 Agent 默认“群体会修正”，从而不再独立承担完整推理责任。
- 文章指出，早期 multi-agent debate 的乐观假设是多模型互相批评可以抵消幻觉，但认知偷懒意味着“多一个 Agent”不必然等于“多一份责任”。

## 前提与局限性

- 该概念来自研究型实验和文章转述，仍需更多生产系统证据。
- 认知偷懒不意味着多 Agent 一定比单 Agent 差；它提示系统必须明确责任边界、独立判断要求和验证机制。
- 仅靠增加 reviewer 或 critic 角色可能无效，因为如果所有角色都默认别人会兜底，责任仍会被稀释。

## 关联概念

- [[Multi-Agent-System-Pathology]] — 认知偷懒是多 Agent 系统病理的群体认知层症状。
- [[Agent-Orchestration]] — 编排者必须定义谁负责独立判断、谁负责最终验收。
- [[Agent-Dissociation]] — 当责任压力和公开表达分离时，认知偷懒可能继续下沉为内态断裂。
- [[Verifiability]] — 明确的外部验证能降低“别人会补上”的模糊责任。
