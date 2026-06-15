---
type: entity
title: Bounded Context (限界上下文)
aliases:
  - 限界上下文
  - Bounded Context
definition: "领域驱动设计中限定某套模型和词汇有效范围的边界，用来防止同一词在不同语境中被错误合并"
created: 2026-05-13
updated: 2026-05-26
tags:
  - domain-driven-design
  - software-architecture
related_entities:
  - "[[Ubiquitous-Language]]"
  - "[[Vocabulary-Building]]"
  - "[[Conceptual-Model]]"
  - "[[Code-as-Conceptual-Infrastructure]]"
  - "[[Integration-Wall]]"
source_raw:
  - "[[What Is Code?]]"
evidence_level: medium
claim_type: mixed
---

# Bounded Context

> [!definition] 定义
> 领域驱动设计中限定某套模型和词汇有效范围的边界，用来防止同一词在不同语境中被错误合并

## 为什么重要

限界上下文的核心洞察是：词汇不是全局稳定的。一个词只有在特定业务边界内才有精确含义。

在复杂企业软件里，强行追求一个统一的 `Product`、`Customer` 或 `Order` 往往会制造假一致。订购、物流、计费、风控和客服可能都使用同一词，但关心的属性、规则和生命周期不同。限界上下文允许它们保留本地模型，并通过显式映射交互。

对 coding agent 来说，限界上下文是防止语义漂移的真相边界。没有边界，Agent 会把一个目录里的词义迁移到另一个目录，生成局部能跑但概念上错位的代码。

## 为什么需要限界上下文？

在复杂系统中，词汇往往具有语境依赖性：

| 上下文 | `Product` 可能意味着什么 |
|--------|--------------------------|
| Ordering | 可售卖项目、价格、库存状态 |
| Shipping | 重量、尺寸、包装、承运限制 |
| Billing | 税率、收入确认、会计科目 |
| Support | 用户看到的购买对象和问题分类 |

如果团队为了复用而强行合并成一个超级 Product 模型，后果通常是字段爆炸、规则混杂、接口变脆和 Agent 误用上下文。限界上下文把问题改成：每个边界内模型保持清楚，边界之间通过映射和协议交互。

## AI 时代的影响

1. **减少歧义**：告诉 Agent 当前任务属于哪个上下文，比提供一堆全局说明更有效。
2. **限制迁移**：防止 Agent 把 billing 的规则套到 shipping，把 support 的词义套到 ordering。
3. **支持局部生成**：Agent 可以在一个上下文内补测试、改模型、重构命名，而不假设全局一致。
4. **暴露集成问题**：边界之间的映射是显式设计点，不再隐藏在自然语言或偶然字段名里。

## 关键数据点

- 限界上下文标记特定词汇有效的真相边界。
- 它是构建 [[Ubiquitous-Language]] 的前提，因为通用语言只在某个上下文内真正通用。
- [[What Is Code?]] 将 bounded context 视为代码作为 [[Conceptual-Model]] 的关键组成。
- 在 AI 时代，目录结构、模块边界、CLAUDE.md 和测试都可以帮助 Agent 识别上下文。

## 前提与局限性

- **复杂度前提**：只有当一个词在不同场景下确实有不同含义时，限界上下文才有价值。
- **沟通前提**：上下文边界需要被团队共享，不能只是架构图里的框。
- **集成成本**：上下文越多，context mapping 越重要，集成协议和翻译层成本也越高。
- **过度切分风险**：过细边界会让系统碎片化，增加跨服务调用和数据同步负担。
- **AI 风险**：边界如果只存在于人脑中，Agent 不会知道。边界必须反映在代码结构、文档、测试和工具提示中。

## 关联概念

- [[Ubiquitous-Language]]：限界上下文内的共享语言
- [[Vocabulary-Building]]：在上下文内发现和打磨词汇
- [[Conceptual-Model]]：上下文内的特定模型
- [[Code-as-Conceptual-Infrastructure]]：限界上下文在 AI 时代的主题承载
- [[Integration-Wall]]：边界之间的语义集成成本
