---
type: entity
title: GraphDB
aliases:
  - GraphDB
  - GraphDB Free
definition: "生产环境中的 RDF 三元组库，用于存储知识图谱和本体事实，并提供 SPARQL 查询与推理能力"
created: 2026-04-20
updated: 2026-05-25
tags:
  - Ontology
  - Database
  - RDF-Store
related_entities:
  - '[[Ontology]]'
  - '[[RDF]]'
  - '[[OWL]]'
  - '[[SPARQL]]'
  - '[[Knowledge-Graph]]'
  - '[[ABox]]'
  - '[[Ontology-Agent]]'
source_raw:
  - '[[20260420-build-first-business-ontology]]'
  - '[[20260420-ontology-meets-agent-case-study]]'
---

# GraphDB

> [!definition] 定义
> 生产环境中的 RDF 三元组库，用于存储知识图谱和本体事实，并提供 SPARQL 查询与推理能力

## 关键数据点

- **架构位置**：GraphDB 是 [[RDF]] / [[OWL]] 技术栈中的 RDF store，用于存储三元组、知识图谱、本体模型和推理结果。
- **主要接口**：[[SPARQL]] 是 GraphDB 对外查询和集成的核心接口，应用服务或 Agent 工具通常不直接遍历文件，而是通过受控查询访问语义层。
- **与 ABox 的关系**：GraphDB 可以承载规模化 [[ABox]] 事实，也可以存储从业务系统抽取或同步出的实例关系。
- **与 TBox 的关系**：GraphDB 可以加载 OWL/RDFS 模型，并按配置进行推理，让查询看到显式事实之外的隐含分类。
- **与开发期工具的关系**：[[Protégé]] 更适合建模和调试，[[HermiT]] 更适合开发期一致性检查；GraphDB 更接近生产运行环境。
- **替代方案**：Apache Jena、Stardog、Ontotext 生态中的其他 RDF store，以及部分云端知识图谱服务。

## 为什么重要

企业本体如果只停留在 OWL 文件、Protégé 项目或 Python demo 中，就很难成为工作系统的一部分。GraphDB 的价值是把语义层放进可查询、可集成、可运维的服务环境。

在 [[Ontology-Agent]] 架构中，GraphDB 常承担两类职责：一是让 Agent 查询知识图谱和本体事实，二是把某些推理结果作为可审计事实提供给业务流程。这样，Agent 不需要在 prompt 里记住概念和规则，也不需要自己手写复杂推理。

不过 GraphDB 不应被误用成普通事务数据库。订单明细、库存流水、审批状态和客户互动仍应留在业务系统或关系数据库中。GraphDB 更适合承载语义索引、跨系统关系、规则可解释查询和需要推理的事实子集。

## 前提与局限性

- **模型前提**：需要稳定的 RDF/OWL 模型、命名空间和实体标识策略，否则三元组库会变成难维护的数据堆。
- **数据前提**：需要明确哪些事实同步到 GraphDB，哪些只在运行时临时注入推理，哪些仍留在业务数据库。
- **性能边界**：大规模多跳查询、实时推理和高频更新都可能带来成本，需要索引、缓存、预计算和查询限制。
- **治理边界**：GraphDB 中的事实和推理结果要能回溯来源系统、时间戳和版本，否则可解释性会下降。
- **工具边界**：GraphDB 和 Neo4j 等属性图数据库不是简单替代关系。前者偏 RDF/OWL 标准和语义推理，后者偏工程化图遍历和图算法。

## 关联概念

- [[Ontology]]：GraphDB 存储的对象
- [[RDF]]：GraphDB 的数据格式
- [[SPARQL]]：GraphDB 的查询语言
- [[OWL]]：GraphDB 可加载和推理的本体语言
- [[Knowledge-Graph]]：GraphDB 常承载的事实图
- [[ABox]]：GraphDB 可存储的实例事实层
- [[Ontology-Agent]]：可通过 GraphDB 工具访问语义层的 Agent
