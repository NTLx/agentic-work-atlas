---
type: entity
title: Bounded Context (限界上下文)
aliases:
  - 限界上下文
  - Bounded Context
definition: "领域驱动设计（DDD）中的核心模式，定义了一个特定模型和词汇表有效的地理/逻辑边界。"
created: 2026-05-13
updated: 2026-05-13
tags:
  - domain-driven-design
  - software-architecture
source_raw:
  - "[[What Is Code?]]"
---

# Bounded Context

> **核心洞察**：词汇只有在特定的边界内才具有唯一且精确的含义。

## 定义

**限界上下文**（Bounded Context）是 Eric Evans 在《领域驱动设计》中提出的概念。它通过为模型划定一个明确的边界，解决了大型系统由于词汇含义模糊（Polysyemy，一词多义）导致的混乱。

[[Unmesh-Joshi]] 强调，由于词汇在不同实例中是不稳定的，通用、大而全的抽象往往要么太通用而无用，要么太武断而难以适配。因此，词汇必须在本地（Local）的限界上下文中被发现。

## 为什么需要限界上下文？

在复杂的企业软件中，“词汇”往往具有语境依赖性。例如：
- **订单上下文 (Ordering)**：`Product` 指的是价格和库存项。
- **物流上下文 (Shipping)**：`Product` 指的是尺寸、重量和包装。
- **财务上下文 (Billing)**：`Product` 指的是税率和会计科目。

强行将这些含义合并为一个单一的 `Product` 类会导致设计灾难。限界上下文允许每个部分拥有自己的模型。

## AI 时代的影响

对于 LLM 而言，限界上下文是极佳的“上下文锚点”：
1. **减少歧义**：明确当前代码处于哪个上下文，可以显著提高 LLM 生成代码的语义准确性。
2. **模块化生成**：AI 可以专注于构建一个上下文内的词汇表，而无需担心全局一致性问题。

---

## 关键数据点

- 限界上下文标记了特定词汇有效的“真相边界”。
- 它是构建 [[Ubiquitous-Language]] 的前提。

## 前提与局限性

- **前提**: 业务领域足够复杂，以至于单一模型无法涵盖。
- **局限性**: 过多细碎的上下文会增加集成（Context Mapping）的复杂度。

## 关联概念

- [[Ubiquitous-Language]] - 限界上下文内的共享语言
- [[Vocabulary-Building]] - 在上下文内构建词汇
- [[Conceptual-Model]] - 上下文内的特定模型
