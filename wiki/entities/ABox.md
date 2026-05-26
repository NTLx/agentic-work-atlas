---
type: entity
title: ABox
aliases:
  - ABox
  - Assertional Box
  - 断言集
definition: "本体中的事实断言层，用具体实例和关系描述当前业务世界中已经发生或被观测到的事实"
created: 2026-04-20
updated: 2026-05-25
tags:
  - Ontology
  - Knowledge-Engineering
related_entities:
  - '[[Ontology]]'
  - '[[TBox]]'
  - '[[RDF]]'
  - '[[Individual]]'
  - '[[Class]]'
  - '[[Knowledge-Graph]]'
  - '[[Ontology-Agent]]'
source_raw:
  - '[[20260420-build-first-business-ontology]]'
  - '[[20260420-ontology-meets-agent-case-study]]'
---

# ABox（断言集）

> [!definition] 定义
> 本体中的事实断言层，用具体实例和关系描述当前业务世界中已经发生或被观测到的事实

## 关键数据点

- **核心内容**：[[Individual]]、实例所属的 [[Class]]、实例之间的关系，以及具体属性值。
- **与 TBox 的关系**：[[TBox]] 定义业务世界中有哪些类型和规则，ABox 提供当前有哪些事实。推理机把两者放在一起，才能判断某个对象是否满足某类业务条件。
- **表达方式**：ABox 常用 [[RDF]] 三元组表达，例如"Order001 是订单"、"Order001 有库存占用 Alloc001"、"Alloc001 质检通过"。
- **运行时角色**：在 [[Ontology-Agent]] 架构中，ABox 往往不是长期存放所有企业数据，而是从数据库按需取事实、注入推理环境、得到结论后释放或缓存。
- **与知识图谱关系**：[[Knowledge-Graph]] 可以看作规模化、可查询的事实图。若它遵守本体定义的类型和关系，就可以作为 ABox 的事实来源。

## 为什么重要

ABox 是本体推理落到业务现场的入口。没有 ABox，本体只是概念模型；没有 TBox，ABox 只是事实表或关系图。企业 Agent 真正需要的是两者结合：稳定规则加当前事实。

以订单加急为例，TBox 定义"可发货订单"和"可加急订单"的条件；ABox 注入某个订单的客户等级、库存占用、质检状态和发货依赖。推理机由此判断该订单是否属于 `ExpediteEligibleOrder`。这个判断不依赖 LLM 猜测，而来自显式事实和规则。

因此 ABox 的质量直接决定推理结果的可信度。事实缺失、字段延迟、系统口径不一致，都会让形式上正确的规则推出业务上错误的结论。

## 前提与局限性

- **映射前提**：业务系统字段必须能映射到本体概念。若 ERP 中的 `ALLOCATED` 和 MES 中的 `ALLOCATED` 含义不同，必须先消歧。
- **数据前提**：实例事实要有来源、时间和状态，否则推理结果无法解释，也难以审计。
- **规模边界**：ABox 不应无差别承载海量交易数据。生产系统通常让数据库保留明细，只向推理机注入必要事实。
- **时效边界**：高频变化的库存、排产和审批状态需要明确同步策略。过期 ABox 会产生过期结论。
- **治理边界**：ABox 数据越自动化，越需要数据质量检查、实体解析、冲突处理和溯源机制。

## 关联概念

- [[Ontology]]：ABox 是本体的组成部分
- [[TBox]]：ABox 的对应部分（概念框架）
- [[RDF]]：表达 ABox 的主要语言
- [[Individual]]：ABox 的核心元素（见本体 6 积木）
- [[Knowledge-Graph]]：ABox 事实的图化和规模化承载方式
- [[Ontology-Agent]]：运行时注入 ABox 并调用推理机的 Agent 架构
