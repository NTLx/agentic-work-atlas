---
type: entity
title: TBox
aliases:
  - TBox
  - Terminological Box
  - 术语集
definition: "本体中的术语与规则层，用类、关系、属性和约束定义业务世界的稳定语义结构"
created: 2026-04-20
updated: 2026-05-25
tags:
  - Ontology
  - Knowledge-Engineering
related_entities:
  - '[[Ontology]]'
  - '[[ABox]]'
  - '[[OWL]]'
  - '[[Class]]'
  - '[[RDF]]'
  - '[[Ontology-Agent]]'
source_raw:
  - '[[20260420-build-first-business-ontology]]'
  - '[[20260420-ontology-enterprise-ai-agent]]'
  - '[[20260420-ontology-meets-agent-case-study]]'
---

# TBox（术语集）

> [!definition] 定义
> 本体中的术语与规则层，用类、关系、属性和约束定义业务世界的稳定语义结构

## 关键数据点

- **核心组成**：[[Class]]、Object Property、Data Property、Axiom、类层级、等价类和限制条件。
- **与 ABox 的关系**：TBox 定义"有哪些概念和规则"，[[ABox]] 提供"当前有哪些事实"。推理机把事实放进规则框架，生成新的分类或一致性检查结果。
- **表达语言**：[[OWL]] 是建模 TBox 的主要语言，[[RDF]] 可以承载底层三元组表示，但单独 RDF 不足以表达复杂约束。
- **业务示例**：`VIPCustomer` 是 `Customer` 的子类；`ReadyToShipOrder` 可以定义为有库存占用且质检通过的订单；`ExpediteEligibleOrder` 可以定义为可发货且客户为 VIP 的订单。
- **Agent 价值**：TBox 把业务规则从 prompt、workflow 和代码分支中抽出，变成可测试、可复用、可解释的语义模型。

## 为什么重要

企业 Agent 最危险的错误之一，是把字段名或自然语言描述当成真实业务语义。TBox 的作用是给 Agent 一个稳定的概念框架，使"客户"、"订单"、"占用库存"、"可发货"这些词不再依赖模型临场解释。

TBox 也让规则维护从散落状态变成集中状态。新增一个加急条件、调整一个商品分类、改变一个合规约束，不必把同一规则复制进多个 prompt、Skills、代码路径和流程节点，而是在语义层修改，并通过推理测试验证影响。

这并不意味着 TBox 替代所有规则系统。它更擅长概念分类、约束、层级和一致性判断；动作编排、审批流和外部系统调用仍需要 workflow、规则引擎或普通服务配合。

## 前提与局限性

- **稳定性前提**：TBox 适合表达相对稳定的业务概念和规则，不适合承载每天变化的交易事实。
- **形式化前提**：业务专家必须能说明规则成立的条件。若组织内部口径本身混乱，TBox 会暴露冲突，而不是自动解决冲突。
- **表达边界**：OWL 对分类和约束强，但对时间序列、流程状态机、例外审批和复杂计算不一定自然。
- **维护边界**：TBox 需要版本管理、回归测试和变更评审。规则集中后，错误变更的影响范围也会扩大。
- **协作成本**：好的 TBox 需要业务、数据、工程共同建模。只由技术团队按字段名抽象，容易把系统实现误当成业务现实。

## 关联概念

- [[Ontology]]：TBox 是本体的组成部分
- [[ABox]]：TBox 的对应部分（事实数据）
- [[OWL]]：建模 TBox 的主要语言
- [[Class]]：TBox 的核心元素（见本体 6 积木）
- [[RDF]]：TBox 底层可被序列化为 RDF 图
- [[Ontology-Agent]]：依赖 TBox 进行可解释规则判定的 Agent
