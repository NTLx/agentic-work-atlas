---
type: entity
title: RDF
aliases:
  - RDF
  - Resource Description Framework
  - 资源描述框架
definition: "用主语、谓语、宾语三元组表达资源关系的 W3C 标准，是语义网和本体事实层的基础数据模型"
created: 2026-04-20
updated: 2026-05-25
tags:
  - Ontology
  - W3C-Standard
  - Semantic-Web
related_entities:
  - '[[Ontology]]'
  - '[[OWL]]'
  - '[[ABox]]'
  - '[[SPARQL]]'
  - '[[Knowledge-Graph]]'
  - '[[GraphDB]]'
source_raw:
  - '[[20260420-build-first-business-ontology]]'
  - '[[20260420-ontology-enterprise-ai-agent]]'
---

# RDF（Resource Description Framework）

> [!definition] 定义
> 用主语、谓语、宾语三元组表达资源关系的 W3C 标准，是语义网和本体事实层的基础数据模型

## 关键数据点

- **基本单位**：三元组，由 Subject、Predicate、Object 组成，用来表达"某资源与某对象之间存在某种关系"。
- **图结构**：多个三元组自然组成 RDF 图，适合表达 [[Knowledge-Graph]] 中的实体和关系。
- **本体位置**：RDF 更贴近 [[ABox]] 的事实表达，也可作为 [[OWL]] 本体的底层序列化基础。
- **查询方式**：RDF 数据通常存入三元组库或 RDF store，再用 [[SPARQL]] 查询。
- **业务示例**：`Order001 rdf:type Order`、`Order001 hasAllocation Alloc001`、`Alloc001 qcPassed true` 可以共同描述订单事实。
- **与属性图区别**：RDF 强调标准化语义、URI 标识、三元组和推理兼容；Neo4j 一类属性图更强调工程化图遍历和图算法。

## 为什么重要

RDF 给企业本体一个统一的事实表达底座。没有 RDF 这样的标准，ABox 事实很容易退化成每个系统自己的表结构、字段名和 JSON 片段，Agent 只能通过 prompt 临场解释。

RDF 的价值不是让所有数据都变成三元组，而是在需要跨系统语义对齐、可追溯关系和推理兼容时，提供一种机器可读的中间表示。它让"订单 A 有库存占用 B"、"客户 C 是 VIP"这类事实可以被本体工具、三元组库和查询语言共同处理。

在 Agent 架构中，RDF 通常不直接面向用户，而是作为语义工具链的基础格式。LLM 不需要生成复杂 RDF；它更适合选择工具、解释 SPARQL 或推理结果，并把结论转回业务语言。

## 前提与局限性

- **建模前提**：资源、关系和标识符需要先设计好。没有统一 URI 或命名策略，RDF 图会迅速碎片化。
- **语义边界**：单独 RDF 主要表达事实关系，不足以表达复杂类约束、等价类和推理规则，通常需要 OWL 或 RDFS 增强。
- **工程边界**：三元组模型和传统关系表差异很大，团队需要学习 SPARQL、RDF store、命名空间和推理配置。
- **性能边界**：大规模多跳查询、推理和图遍历可能需要索引、缓存和专门的三元组库优化。
- **适用边界**：如果只是单系统内简单 CRUD，RDF 可能过重；它更适合跨系统语义层、知识图谱和可推理事实表示。

## 关联概念

- [[Ontology]]：RDF 是本体的基础数据标准
- [[OWL]]：RDF 的语义增强层
- [[ABox]]：RDF 通常用于表达 ABox
- [[SPARQL]]：RDF 的查询语言
- [[Knowledge-Graph]]：由 RDF 三元组构成的事实图
- [[GraphDB]]：存储和查询 RDF 的生产级三元组库
