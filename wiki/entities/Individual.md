---
type: entity
title: Individual
aliases:
  - Individual
  - 个体
  - Instance
definition: "本体 ABox 中表示具体业务对象或事实对象的实例，是 Class 在现实数据中的落点"
created: 2026-04-21
updated: 2026-05-25
tags:
  - ontology
  - knowledge-representation
related_entities:
  - '[[ABox]]'
  - '[[Ontology]]'
  - '[[Class]]'
  - '[[RDF]]'
  - '[[Knowledge-Graph]]'
source_raw:
  - "[[20260420-build-first-business-ontology]]"
  - "[[20260420-ontology-meets-agent-case-study]]"
---

# Individual (Ontology)

> [!definition] 定义
> 本体 ABox 中表示具体业务对象或事实对象的实例，是 Class 在现实数据中的落点

## 关键数据点

- **所在层**：Individual 属于 [[ABox]]，代表当前业务世界里的具体对象、事件或状态。
- **与 Class 的关系**：[[Class]] 定义概念类型，Individual 是类型的成员。例如 `Customer_123` 属于 `Customer`，也可能因为规则推理属于 `VIPCustomer`。
- **事实承载**：Individual 可以带有属性值，也可以通过关系连接其他 Individual，例如 `Order001 hasCustomer Customer123`。
- **表达方式**：在 [[RDF]] 中，Individual 常以 URI 或标识符出现，并通过三元组记录类型、属性和关系。
- **Agent 场景**：Ontology Agent 通常从数据库取出当前订单、客户、库存占用等事实，临时创建 Individual，再交给推理机分类。

## 为什么重要

Individual 是本体从抽象规则进入实际业务判断的入口。没有 Individual，TBox 只能说明规则应该如何成立；有了 Individual，推理机才能判断某个具体订单、客户或商品是否满足这些规则。

例如 TBox 可以定义 `ReadyToShipOrder`，但是否有某个订单属于它，取决于 ABox 中是否存在订单实例、库存占用实例、质检状态以及这些实例之间的关系。Individual 让"规则"接触"事实"。

在 Agent 系统里，Individual 的设计也影响可解释性。若实例只叫 `row_17`，人很难追溯结论；若它能回链到真实订单号、客户号和数据来源，Agent 的回答就可以解释"为什么这个订单被判定为可加急"。

## 前提与局限性

- **身份前提**：Individual 需要稳定标识，否则跨系统事实无法合并，也无法追踪推理来源。
- **类型前提**：Individual 至少要能映射到某个 Class，否则它只是孤立数据点。
- **数据质量边界**：错误属性、重复实例、过期状态会直接污染推理结论。
- **规模边界**：不是所有数据库行都应变成持久 Individual。高频、海量、低价值事实通常只在运行时按需注入。
- **语义边界**：Individual 本身不包含规则。它只有在 TBox 的约束下，才会产生新的业务含义。

## 关联概念

- [[ABox]]：Individual 所属的事实断言层
- [[Class]]：Individual 所属的概念类型
- [[Ontology]]：定义 Individual 语义的整体模型
- [[RDF]]：表达 Individual 事实和关系的基础格式
- [[Knowledge-Graph]]：由大量 Individual 与关系构成的事实图
