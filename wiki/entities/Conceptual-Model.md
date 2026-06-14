---
type: entity
title: Conceptual Model (概念模型)
aliases:
  - 概念模型
  - Conceptual Model
definition: "代码中关于问题领域的词汇、对象、关系、边界和不变量，是人类与 Agent 共同理解系统的语义结构"
created: 2026-05-13
updated: 2026-05-26
tags:
  - programming-theory
  - software-design
  - conceptual-model
evidence_level: medium
claim_type: mixed
related_entities:
  - "[[Code-as-Conceptual-Infrastructure]]"
  - "[[Vocabulary-Building]]"
  - "[[Bounded-Context]]"
  - "[[Ubiquitous-Language]]"
  - "[[Cognitive-Debt]]"
  - "[[Essential-Complexity]]"
source_raw:
  - "[[What Is Code?]]"
---

# Conceptual Model

> [!definition] 定义
> 代码中关于问题领域的词汇、对象、关系、边界和不变量，是人类与 Agent 共同理解系统的语义结构

## 为什么重要

[[What Is Code?]] 的核心区分是：代码既是给机器执行的指令，也是关于问题领域的概念模型。LLM 让第一部分变便宜，却让第二部分更关键。

概念模型决定系统里哪些词存在、哪些对象被区分、哪些边界不可跨越、哪些规则必须保持。它不是注释层，而是体现在类型、函数、模块、测试、命名和数据结构里的共享理解。

在 AI coding 场景中，概念模型也是 Agent 的上下文骨架。代码词汇清楚，Agent 能把自然语言需求映射到正确对象；代码词汇混乱，Agent 会用流畅输出掩盖错误理解，并把错误抽象继续扩散。

## AI 时代的重要性

| 维度 | 指令属性 | 概念模型属性 |
|------|----------|----------------|
| 主要作用 | 让机器执行 | 让人和 Agent 理解 |
| AI 影响 | 生成成本下降 | 质量差异更显性 |
| 常见错误 | bug、崩溃、性能问题 | 词汇混乱、边界错、抽象失真 |
| 验证方式 | 测试、类型、运行 | review、领域反馈、不变量和长期维护 |
| 主要资产 | 代码量与实现技巧 | 词汇、边界、关系、规则 |

AI 越能快速生成实现，团队越需要问：这段代码是否强化了正确概念，还是只增加了看似合理的新名词。

## 概念模型的组成要素

1. **词汇**：系统允许哪些业务名词存在，例如 Customer、Order、Allocation。
2. **关系**：对象如何连接，例如订单属于客户，库存占用满足订单。
3. **边界**：一个词在哪个 [[Bounded-Context]] 内有效，何时需要换模型。
4. **不变量**：系统必须一直守住的规则，例如金额不可为负、已取消订单不可发货。
5. **反馈机制**：测试、类型、review、业务验收和文档如何纠正模型偏差。

## 关键数据点

- Unmesh Joshi 区分 code as instructions 与 code as conceptual model，指出 LLM 时代后者的稀缺性上升。
- 代码结构、类型系统、测试和命名本身构成 Agent 的 context 与 harness。
- DDD 中的 [[Ubiquitous-Language]]、[[Bounded-Context]] 和 [[Vocabulary-Building]] 都是在维护概念模型。
- 概念模型失败会累积为 [[Cognitive-Debt]]：代码能跑，但团队和 Agent 不知道它到底表达什么。

## 前提与局限性

- **复杂度前提**：系统有长期演化、多人协作或真实领域约束时，概念模型才成为核心资产。
- **协作前提**：模型必须被业务专家、工程师和 Agent 共同使用，不能只是某个人脑中的隐性理解。
- **边界局限**：一次性脚本、低风险自动化和短生命周期原型，不一定值得投入复杂建模。
- **演化风险**：模型一旦固化在代码和文档里，也可能压扁现实或遮蔽例外，需要持续反馈修正。
- **AI 风险**：LLM 容易生成看似成熟的概念名词，但如果团队没有真正理解，这些名词会制造认知债务。

## 关联概念

- [[Code-as-Conceptual-Infrastructure]]：概念模型在 AI 时代的软件主线定位
- [[Vocabulary-Building]]：构建概念模型的过程
- [[Bounded-Context]]：概念模型的有效边界
- [[Ubiquitous-Language]]：概念模型的共享语言表达
- [[Cognitive-Debt]]：概念模型模糊导致的后果
- [[Essential-Complexity]]：概念模型必须面对的现实复杂性
