---
type: entity
title: Ubiquitous Language (通用语言)
aliases:
  - 通用语言
  - Ubiquitous Language
definition: "在同一限界上下文内由业务专家、工程师和代码共同使用的共享词汇系统"
created: 2026-05-13
updated: 2026-05-26
tags:
  - domain-driven-design
  - communication
  - software-engineering
evidence_level: medium
claim_type: mixed
related_entities:
  - "[[Bounded-Context]]"
  - "[[Vocabulary-Building]]"
  - "[[Conceptual-Model]]"
  - "[[Cognitive-Debt]]"
  - "[[Code-as-Conceptual-Infrastructure]]"
source_raw:
  - "[[What Is Code?]]"
---

# Ubiquitous Language

> [!definition] 定义
> 在同一限界上下文内由业务专家、工程师和代码共同使用的共享词汇系统

## 为什么重要

通用语言的目标不是统一口号，而是消除业务语言和代码语言之间的隐性翻译层。

如果业务专家说"占用库存"，代码里却叫 `reservation`、`allocation`、`hold`、`lock` 混用，团队表面上在讨论同一件事，实际上每个人脑中都是不同模型。Agent 进入这种代码库后，只会放大混乱。

通用语言要求词汇同时出现在对话、文档、测试、类型、函数名和界面上。它把沟通共识固化为可执行、可检索、可审查的代码结构。

## 为什么是“通用”的？

- **跨角色**：领域专家、工程师、产品和 reviewer 使用同一组词。
- **跨媒介**：口头交流、文档、图表、代码、测试和 prompt 中词义一致。
- **跨执行层**：这套语言约束 [[Conceptual-Model]]，也为 Agent 提供稳定语义锚点。
- **有边界**：通用语言不是全公司唯一语言，而是在一个 [[Bounded-Context]] 内通用。

## AI 时代的重要性

Ubiquitous Language 是人机协作的元协议：

1. **Prompt 基础**：用户用代码库通用语言描述需求时，Agent 更容易命中正确对象。
2. **上下文压缩**：稳定词汇减少解释成本，不必每次 prompt 都重新定义业务世界。
3. **审查依据**：reviewer 可以检查新代码是否引入了偏离通用语言的新词。
4. **债务预警**：同一概念出现多个名字，常常是 [[Cognitive-Debt]] 正在累积。

这也是 [[Code-as-Conceptual-Infrastructure]] 的核心：代码不是只给机器跑，也是给未来的人和 Agent 继续理解。

## 关键数据点

- 通用语言是在开发者和领域专家的迭代协作中发现的，不是由一方单向命名。
- 它必须进入代码：类名、函数名、测试名、错误消息和文档都要使用同一词汇。
- [[What Is Code?]] 将这种语言视为代码概念模型的社会化成果。
- LLM 擅长把自然语言映射到已有词汇，但前提是代码库已经有稳定词汇。

## 前提与局限性

- **协作前提**：需要领域专家和开发团队持续反馈。只靠工程师命名，容易复制技术实现而不是业务现实。
- **边界前提**：通用语言必须绑定上下文。跨上下文强行统一会产生假一致。
- **时间成本**：建立通用语言需要对话、重命名、测试和代码演化，不适合所有一次性项目。
- **演化成本**：业务词汇会变，语言需要重构。旧词不清理会让 Agent 和新人误解系统。
- **政治风险**：组织里不同团队可能争夺词义，语言治理本身也是组织治理。

## 关联概念

- [[Bounded-Context]]：通用语言的有效范围
- [[Vocabulary-Building]]：构建通用语言的过程
- [[Conceptual-Model]]：通用语言描述的对象
- [[Cognitive-Debt]]：语言混乱导致的理解债务
- [[Code-as-Conceptual-Infrastructure]]：通用语言在 AI 时代的系统意义
