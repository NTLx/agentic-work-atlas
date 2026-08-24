---
type: entity
title: Build First Business Ontology
aliases:
  - Build First Business Ontology
  - Business Ontology
  - 业务本体
definition: "在构建 AI 系统前先建立业务本体的方法论——区分 TBox（概念框架：类、关系、约束）与 ABox（事实数据：具体实例）；让推理机自动推导业务结论，避免硬编码规则"
created: "2026-08-17"
updated: "2026-08-17"
tags:
  - entity
  - ontology
  - enterprise-AI
  - method
related_entities:
  - "[[Ontology-Meets-Agent]]"
  - "[[Harness-Engineering]]"
source_raw:
  - "[[20260420-build-first-business-ontology]]"
  - "[[20260420-ontology-enterprise-ai-agent]]"
  - "[[20260420-ontology-meets-agent-case-study]]"
  - "[[20260613-ontology-for-agent-optimization]]"
  - "[[20260613-ontology-tokenmaxxing]]"
---

# Build First Business Ontology（先建业务本体）

> [!definition] 定义
> **Build First Business Ontology** 是在构建 AI 系统前先建立业务本体的方法论——区分 TBox（概念框架：类、关系、约束，类似数据库 schema）与 ABox（事实数据：具体实例，类似表数据）；推理机在两者结合处运行，自动推导业务结论（如"订单可加急"）。

## 核心要点（跨源综合）

### TBox vs ABox 分离

- TBox = 类层级 + 属性 + 约束 = schema 层面
- ABox = 具体实例 + 实例间事实 = data 层面
- 推理发生在 TBox 给"什么条件成立" + ABox 给"现在有什么事实" 的结合处

### 工具链

- RDF（主谓宾三元组）适合 ABox 表达
- OWL（RDF 之上）适合 TBox（类层级、属性约束、等价类、逻辑限制）
- HermiT/Pellet 等 reasoner 自动推导
- GraphDB/Jena 适合 RDF/OWL/SPARQL；Neo4j 更适合显式关系分析

### 运行时加载

- Owlready2 示例：本体不是停留在建模工具的图，可在运行时加载、注入事实、调用推理机、返回结论
- 业务规则从自然语言改写为可推理模型（如 ReadyToShipOrder = "存在库存占用且质检通过"）

## 跨域同构

- **Just do less ↔ 复用 TBox primitives**：Ian Silber 的"Just do less"在数据/规则层的对应是"复用 ontology primitives 而非硬编码规则"
- **Build-First vs Build-Later**：ontology 优先于 UI；类似"schema 优先于 view"在传统软件工程中的位置
- **Harness-Engineering ↔ Harness Schema**：harness 中 agent 调用工具的 schema 定义，本质上是 ontology 的工程化

## 立场偏见提醒

- ontology 工程的成本/收益比在不同业务规模下差异大
- 简单业务场景可能不需要完整 ontology（用硬编码规则就够）
- 该方法论对推理机性能有依赖，需评估 query 延迟

## Source

- [[20260420-build-first-business-ontology]] — 核心 raw
- [[20260420-ontology-enterprise-ai-agent]]
- [[20260420-ontology-meets-agent-case-study]]
- [[20260613-ontology-for-agent-optimization]]
- [[20260613-ontology-tokenmaxxing]]

## 关键数据点

- TBox = 类层级 + 属性 + 约束（schema 维度）；ABox = 具体实例（data 维度）；推理发生在两者结合处
- 工具链分工：RDF 适合 ABox、OWL 适合 TBox、reasoner（HermiT/Pellet）自动推导、GraphDB/Jena 适合 RDF/OWL/SPARQL、Neo4j 适合显式关系分析
- Owlready2 示例：本体可运行时加载、注入事实、调用推理机、返回结论——业务规则从自然语言改写为可推理模型
- 5 个一手 raw 支撑该方法论（20260420 × 3 + 20260613 × 2）

## 前提与局限性

- ontology 工程成本/收益比随业务规模非线性——简单业务场景可能不需要完整 ontology（硬编码规则就够）
- 对推理机性能有依赖——query 慢时延迟不可接受
- 模型/规则的边界判定需要本体工程专家——团队需要特定技能
- 与 vector DB/RAG 路线有方法论竞争；不必然互斥，但优先级冲突需要选边

## 关联概念

- [[Ontology]] — 本体论的一般概念
- [[Harness-Engineering]] — Harness schema 与 ontology 工程同源
- [[Systems-Thinking]] — ontology 是系统 schema 的形式化
- [[Enterprise-AI-Model-Sourcing]] — 企业 AI 落地中 ontology 是数据底座
- [[Just-Do-Less]] — "复用 ontology primitives 而非硬编码规则" 是 Just do less 在数据层
- [[Knowledge-Work]] — 知识工作中"理解系统全貌"的需求与 ontology 共建