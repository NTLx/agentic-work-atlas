---
type: entity
title: Conceptual Model (概念模型)
aliases:
  - 概念模型
  - Conceptual Model
definition: "代码作为人类和工具理解问题领域的结构化表达。在 AI 时代，它是代码中除机器指令外最核心的资产。"
created: 2026-05-13
updated: 2026-05-13
tags:
  - programming-theory
  - software-design
  - abstraction
source_raw:
  - "[[What Is Code?]]"
---

# Conceptual Model

> **核心洞察**：代码是开发者对现实世界问题的“数字镜像”。

## 定义

在软件工程中，**概念模型**（Conceptual Model）是指代码中体现的关于业务领域（Domain）的概念、命名、边界和关系。

[[Unmesh-Joshi]] 认为代码具有双重属性：
1. **指令属性** (Instructions): 告诉机器如何执行（计算、存储、传输）。
2. **模型属性** (Conceptual Model): 告诉人类（和其他工具）系统是如何思考和组织的。

## AI 时代的重要性

随着 LLM（大语言模型）使得生成“指令”变得廉价甚至免费，代码的“模型属性”变得前所未有的重要。

| 维度 | 指令属性 (Instructions) | 模型属性 (Conceptual Model) |
|-----|-----------------------|--------------------------|
| **执行者** | 机器 | 人类 + AI Agent |
| **价值趋势** | 正在商品化/平庸化 | 核心资产，价值上升 |
| **错误后果** | 逻辑错误、崩溃 | 认知负担、系统不可维护 |
| **关注点** | 性能、资源、并发 | 命名、抽象、边界、词汇 |

## 概念模型的组成要素

1. **词汇表 (Vocabulary)**: 定义系统中的核心实体（如 Customer, Order, TransactionLog）。
2. **关系 (Relationships)**: 定义实体如何互动（如 Order contains Products）。
3. **边界 (Boundaries)**: 定义逻辑在何处终止，新逻辑在何处开始（见 [[Bounded-Context]]）。
4. **不变量 (Invariants)**: 系统必须始终满足的规则。

---

## 关键数据点

- Unmesh Joshi (2026) 提出：在 LLM 时代，代码作为概念模型的角色比作为指令的角色更重要。
- 代码结构、类型系统和测试本身构成了 AI 的“上下文框架”（Harness）。

## 前提与局限性

- **前提**: 假设系统复杂度高到人类无法仅凭直觉理解，必须依赖结构化代码作为认知中介。
- **局限性**: 对于极其简单的、一次性的脚本，构建复杂的概念模型可能过早优化。
- **边界条件**: 当系统演变为完全的黑盒（如神经网络权重）时，概念模型可能在代码层消失。

## 关联概念

- [[Vocabulary-Building]] - 构建概念模型的过程
- [[Bounded-Context]] - 概念模型的有效边界
- [[Ubiquitous-Language]] - 概念模型的语言表达
- [[Cognitive-Debt]] - 概念模型模糊导致的后果
