---
type: entity
title: Class
aliases:
  - Class
  - 类
  - Concept
definition: "本体 TBox 中用于定义业务对象类型的核心元素，规定哪些实例可以被视为同一类概念"
created: 2026-04-21
updated: 2026-05-25
tags:
  - ontology
  - knowledge-representation
related_entities:
  - '[[TBox]]'
  - '[[Individual]]'
  - '[[Ontology]]'
  - '[[OWL]]'
  - '[[ABox]]'
source_raw:
  - "[[20260420-build-first-business-ontology]]"
  - "[[20260420-ontology-enterprise-ai-agent]]"
---

# Class (Ontology)

> [!definition] 定义
> 本体 TBox 中用于定义业务对象类型的核心元素，规定哪些实例可以被视为同一类概念

## 关键数据点

- **所在层**：Class 属于 [[TBox]]，用于定义业务世界中的稳定概念类型。
- **与 Individual 的关系**：[[Individual]] 是具体实例，Class 是实例所属的概念类别。例如 `Order001` 是 `Order` 的 Individual。
- **常见关系**：Class 可以有子类、等价类、互斥类和限制条件。`VIPCustomer` 可以是 `Customer` 的子类。
- **规则承载**：Class 不只是标签。通过 [[OWL]]，一个 Class 可以由条件定义，例如"有库存占用并且质检通过的订单"自动属于 `ReadyToShipOrder`。
- **工程类比**：Class 类似数据库 schema 或编程语言中的类型，但更强调业务语义、关系约束和推理，而不只是字段集合。

## 为什么重要

Class 决定了本体能否成为真正的业务语义层。如果 Class 只是复制数据库表名，本体只是在技术结构上换了形式；如果 Class 能表达业务对象和业务状态，它就能帮助 Agent 分辨"订单"、"可发货订单"、"可加急订单"这些概念边界。

在企业 Agent 中，Class 的关键价值是把自然语言里的模糊类别变成可检查对象。LLM 可以说"这个订单看起来可以加急"，但本体可以要求订单必须满足某个 Class 的形式化条件。这样，业务判断从模型直觉转向可解释分类。

Class 设计也会影响后续维护。过粗的 Class 无法表达关键业务差异，过细的 Class 会造成概念爆炸。好的 Class 通常对应稳定、可复用、有判断价值的业务概念。

## 前提与局限性

- **概念稳定性**：Class 应表达相对稳定的业务类型，而不是临时状态、一次性标签或随报表变化的口径。
- **边界清晰度**：每个 Class 需要说明哪些 Individual 能属于它，哪些不能。边界不清会让推理结果不可解释。
- **建模成本**：Class 层级需要业务专家参与。仅按系统字段自动生成 Class，容易复制旧系统的混乱。
- **表达边界**：Class 擅长分类和约束，不适合承载长流程、动作序列或复杂数值计算。
- **演化风险**：一旦 Class 被多个 Agent、查询和规则复用，改名、合并或拆分都需要版本治理和回归测试。

## 关联概念

- [[TBox]]：Class 所属的术语与规则层
- [[Individual]]：Class 的具体实例
- [[Ontology]]：Class 所在的整体语义模型
- [[OWL]]：定义 Class 层级和限制条件的主要语言
- [[ABox]]：存放 Class 实例事实的层
