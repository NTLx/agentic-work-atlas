---
type: entity
title: Ubiquitous Language (通用语言)
aliases:
  - 通用语言
  - Ubiquitous Language
definition: "由开发者和领域专家共同构建、并在代码和日常沟通中一致使用的共享语言。"
created: 2026-05-13
updated: 2026-05-13
tags:
  - domain-driven-design
  - communication
  - software-engineering
source_raw:
  - "[[What Is Code?]]"
---

# Ubiquitous Language

> **核心洞察**：如果业务专家和程序员说的是两套话，软件就注定会失败。

## 定义

**通用语言**（Ubiquitous Language）是 DDD 中的另一核心支柱。它要求在特定的 [[Bounded-Context]] 内，团队的所有成员（包括非技术人员）都使用同一套词汇表，这套词汇表直接映射到代码中的类、方法和变量名。

[[Unmesh-Joshi]] 认为，这种语言通过持续的反馈（Working Software）和协作来完善，它是 [[Vocabulary-Building]] 的社会化成果。

## 为什么是“通用”的？

- **跨角色**：它消除了“业务语言”到“代码实现”之间的翻译层。
- **跨媒介**：它在口头交流、文档、图表和代码中都是一样的。
- **跨环境**：这种语言直接约束了系统的 [[Conceptual-Model]]。

## AI 时代的重要性

Ubiquitous Language 是人机协作的“元协议”：
1. **Prompt 的基础**：当你使用通用语言编写 Prompt 时，LLM 生成的输出将更容易与现有代码库对齐。
2. **知识沉淀**：它将模糊的业务共识固化为精确的代码词汇，减少了 [[Cognitive-Debt]]。

---

## 关键数据点

- 通用语言是在开发者和领域专家的迭代协作中“发现”的，而非由一方单向强制。
- 它必须在代码中得到体现（如使用业务名词作为变量名）。

## 前提与局限性

- **前提**: 需要领域专家与开发团队之间的高度信任和频繁沟通。
- **局限性**: 建立通用语言需要时间，对于周期极短的项目可能显得成本过高。

## 关联概念

- [[Bounded-Context]] - 通用语言的有效范围
- [[Vocabulary-Building]] - 构建通用语言的技术过程
- [[Conceptual-Model]] - 通用语言描述的对象
