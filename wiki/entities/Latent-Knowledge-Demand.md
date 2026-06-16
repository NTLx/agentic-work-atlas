---
type: entity
title: Latent Knowledge Demand
aliases:
  - "Latent Knowledge Demand"
  - "隐性知识需求"
  - "隐藏知识需求"
definition: "组织中长期存在但被检索摩擦、社交成本和流程门槛压住的知识需求；当 AI 降低访问摩擦后，需求会突然显现"
created: 2026-05-23
updated: 2026-06-16
evidence_level: medium
claim_type: mixed
tags:
  - knowledge-system
  - enterprise-AI
  - AI-adoption
related_entities:
  - "[[AI-Factory]]"
  - "[[Agent-Knowledge-Management]]"
  - "[[LLM-Wiki]]"
  - "[[Knowledge-Compilation]]"
  - "[[Progressive-Disclosure]]"
source_raw:
  - "[[From Strategy to Shelf How P&G Is Deploying AI]]"
  - "[[How Procter & Gamble Uses AI to Unlock New Insights From Data  Thomas H. Davenport and Randy Bean]]"
---

# Latent Knowledge Demand（隐性知识需求）

> [!definition] 定义
> **Latent Knowledge Demand** 是组织中长期存在但被检索摩擦、社交成本和流程门槛压住的知识需求。AI 的作用不是凭空制造需求，而是把原来“想问但懒得问、不敢问、找不到人问”的需求显性化。

## 关键数据点

- P&G 的一个中心团队用 AI 建立领域知识数据库，上线第一个月收到的查询量超过该团队过去 10 年收到的总查询量。
- Alfredo Colas 将这个现象解释为：知识一直在 P&G 内部，需求也一直存在，只是访问摩擦太高。
- P&G 的 askPG 将 curated internal unstructured data 提供给员工，insightsPG 则让业务人员用生成式前端直接和业务数据交互。
- Project Genie 汇总文章和帮助文档，为 800 多名客服代表提供信息，降低问题处理时间。
- 这个现象说明企业知识系统的瓶颈常常不是“没有知识”，而是知识没有处在可访问、可调用、可复用的形态。

## 前提与局限性

- 查询量暴增不等于所有查询都产生业务价值；仍需要质量评估、权限治理和反馈机制。
- AI 降低访问摩擦后，也可能放大旧知识、错误知识或上下文不完整的知识，因此需要 [[Knowledge-Compilation|知识编译]] 和来源追溯。
- 隐性知识需求只在组织有足够知识沉淀时成立。缺少高质量 source 的组织，AI 只会更快暴露知识空洞。

## 关联概念

- [[AI-Factory]] — factory 提供安全、权限和数据接入层，让隐性知识需求可以被规模化满足。
- [[Agent-Knowledge-Management]] — 将知识组织为 Agent 可检索、可使用的结构，是释放隐性需求的基础。
- [[LLM-Wiki]] — LLM Wiki 把原始材料编译成可复用语义层，降低未来查询成本。
- [[Knowledge-Compilation]] — 没有编译，AI 只是搜索；经过编译，知识才进入可复用状态。
- [[Progressive-Disclosure]] — 在需要时加载相关知识，避免把全部组织知识一次性塞进上下文。
