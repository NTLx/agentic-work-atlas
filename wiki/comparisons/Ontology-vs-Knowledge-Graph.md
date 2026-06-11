---
type: comparison
title: "Ontology vs Knowledge Graph"
entity_a: "[[Ontology]]"
entity_b: "[[Knowledge-Graph]]"
created: 2026-05-24
updated: 2026-05-24
tags:
  - comparison
  - knowledge-system
  - ontology
related_entities:
  - "[[Ontology]]"
  - "[[Knowledge-Graph]]"
  - "[[Ontology-Agent]]"
  - "[[Enterprise-Ontology-Application]]"
source_raw:
  - "[[20260420-ontology-enterprise-ai-agent]]"
  - "[[20260420-build-first-business-ontology]]"
  - "[[20260420-ontology-meets-agent-case-study]]"
---

# Ontology vs Knowledge Graph

> [!summary] 对比概述
> Knowledge Graph 是事实关系网络，主要回答“有哪些对象以及它们如何连接”；Ontology 是概念、规则和约束层，主要回答“这些对象按什么类型、边界和规则被理解”。企业 Agent 需要的不只是图谱事实，还需要本体提供稳定语义。

## 核心维度对比

| 维度 | Ontology | Knowledge Graph |
|------|----------|-----------------|
| 核心对象 | 概念类型、关系定义、约束、推理规则 | 实体、事实、属性、关系边 |
| 主要问题 | 业务世界如何被定义和约束 | 事实之间如何连接和查询 |
| 类比 | Schema + 规则系统 + 语义契约 | 数据库中的实例数据 + 关系网络 |
| 典型结构 | TBox 定义概念和规则，ABox 承载实例 | 节点、边、属性、三元组 |
| 强项 | 语义一致、规则推理、边界约束、可解释性 | 关联发现、实体检索、路径查询、事实聚合 |
| 主要风险 | 建模过重、脱离业务、维护成本高 | 只有连接没有语义约束，容易变成大号关系表 |
| 对 Agent 的价值 | 限制 Agent 如何理解业务对象和规则 | 给 Agent 提供可查询的事实上下文 |

## 本质区别

Knowledge Graph 更接近**事实层**。它把客户、订单、产品、合同、风险事件等对象连接起来，让系统能查到“谁和谁相关”“某个对象有哪些属性”“路径上发生过什么”。

Ontology 更接近**语义层**。它定义什么叫客户、订单、风险、可发货、合规、例外审批；也定义这些概念之间的合法关系和推理规则。

在企业 AI 场景里，二者的关键差异是：

- Knowledge Graph 帮 Agent 找到事实。
- Ontology 告诉 Agent 如何理解事实。

只有图谱而没有本体，Agent 可能能查到很多连接，却不知道不同系统里的“客户”“账户”“联系人”是否是同一个业务概念。只有本体而没有事实，规则很漂亮，但不能支撑真实操作。

## TBox 与 ABox 的分界

[[Enterprise-Ontology-Application]] 中最关键的分界是 TBox 和 ABox。

| 层 | 作用 | 更接近 |
|----|------|--------|
| TBox | 定义类、关系、约束和规则 | Ontology |
| ABox | 存储具体实例和事实 | Knowledge Graph |

这个区分能避免一个常见误解：Ontology 不是 Knowledge Graph 的高级叫法。更准确地说，Ontology 提供概念骨架，Knowledge Graph 承载事实网络。企业 Agent 真正需要的是二者组合。

## 对企业 Agent 的影响

Agent 进入企业后遇到的很多问题不是模型不聪明，而是业务语义不稳定。

例如：

- CRM 里的“客户”和财务系统里的“付款方”是不是同一个对象？
- “可发货”需要同时满足库存、信用、合同、合规和地区限制中的哪些规则？
- 销售能看到的客户字段，客服是否也能看到？
- 风险等级是事实字段，还是由多个规则推理出来的状态？

Knowledge Graph 可以把相关事实接出来，但 Ontology 才能定义这些事实的解释边界。没有本体，Agent 往往只能临时猜业务规则；有了本体，Agent 才能被业务概念约束。

## 反模式

### 把知识图谱当作语义治理

如果只是把更多实体和关系塞进图数据库，却没有定义概念边界、权限规则和业务约束，系统只是在积累连接，不是在积累理解。

### 把本体做成脱离业务的哲学分类

本体不是为了追求完美分类，而是为了让人、系统和 Agent 对关键业务对象达成稳定共识。脱离真实流程的本体会变成维护负担。

### 让 Agent 自己发明业务语义

如果没有本体或稳定词汇层，每个 Agent 都可能在上下文里临时解释业务名词。短期看似灵活，长期会制造语义漂移和不可审计决策。

## 选择指南

优先建设 Knowledge Graph，当：

- 主要问题是事实分散、实体关联弱、检索困难。
- 已有业务概念较稳定，只缺统一查询和关系发现。
- 目标是增强检索、推荐、路径分析或事实聚合。

优先建设 Ontology，当：

- 多个系统对同一业务概念定义不一致。
- Agent 需要执行规则判断、权限判断或合规解释。
- 组织希望把隐性业务规则转成可维护语义层。
- AI 幻觉主要来自概念混淆，而不是事实缺失。

成熟企业 AI 系统通常需要两者配合：Ontology 约束语义，Knowledge Graph 承载事实。

## 相关概念

- [[Ontology]] — 对现实业务世界的数字化建模。
- [[Knowledge-Graph]] — 事实数据的图结构集合。
- TBox — 概念与规则部分。
- ABox — 具体事实实例部分。
- RDF — 用三元组表达事实关系的基础标准。
- OWL — 定义复杂概念和规则的本体语言。
- [[Ontology-Agent]] — 基于本体语义层工作的 Agent。

