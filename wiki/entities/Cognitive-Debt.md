---
type: entity
title: Cognitive Debt
aliases:
  - 认知债务
  - Cognitive Debt
definition: "代码库中的词汇、抽象和结构增长快于团队理解速度时积累的维护与判断债务"
created: 2026-05-13
updated: 2026-05-26
tags:
  - software-engineering
  - technical-debt
evidence_level: medium
claim_type: mixed
related_entities:
  - "[[Conceptual-Model]]"
  - "[[Vocabulary-Building]]"
  - "[[Technical-Debt-Avoidance]]"
  - "[[Code-as-Conceptual-Infrastructure]]"
  - "[[Ubiquitous-Language]]"
source_raw:
  - "[[What Is Code?]]"
  - "[[20260410-better-code]]"
---

# Cognitive Debt

> [!definition] 定义
> 代码库中的词汇、抽象和结构增长快于团队理解速度时积累的维护与判断债务

## 为什么重要

认知债务不是代码不能运行，而是团队不再真正理解代码在表达什么。AI coding 会加速这种债务，因为模型可以快速生成熟悉的架构词汇，例如 Controller、Repository、Factory、Policy、Orchestrator，但这些词背后的概念模型未必被团队掌握。

[[What Is Code?]] 的核心提醒是：代码是 [[Conceptual-Model]]，不是只有机器指令。LLM 让指令生成变便宜，却不会自动让团队获得理解。可运行代码如果没有共享词汇和边界，就会在未来 review、debug、重构和 onboarding 中持续收费。

认知债务尤其危险，因为它比技术债更难被测试直接发现。系统可能绿灯通过，团队却不敢改、不知道该删哪里，也无法判断 Agent 生成的新抽象是否合理。

## 与技术债务的区别

| 维度 | 技术债务 | 认知债务 |
|------|----------|----------|
| 表现 | 耦合、冗余、缺测试、结构腐化 | 难解释、不敢改、评审空转 |
| 产生原因 | 为速度牺牲结构 | 接受未理解的词汇和抽象 |
| AI 影响 | 可帮助清理一部分 | 容易加速生成新词和新结构 |
| 修复方式 | 重构、补测试、拆模块 | 学习、重命名、删抽象、重建模型 |
| 主要证据 | 代码异味和失败率 | 人无法解释系统为何如此设计 |

## 关键数据点

- [[What Is Code?]] 指出，LLM 时代代码的模型属性比指令属性更稀缺。
- 认知债务常见信号是同一概念多名、类名宏大但没人能解释、review 只看 diff 不看模型。
- [[20260410-better-code]] 的反向启发是：AI 降低改动成本后，更应该投资命名、边界、文档和测试。
- 认知债务和技术债会互相放大：模型不清导致结构腐化，结构腐化又让模型更难理解。

## 缓解策略

1. **参与而非只验收**：开发者要通过修改、重构和测试建立理解，而不是只看 Agent 输出。
2. **限制词汇膨胀**：新抽象必须解释它解决什么概念问题，否则宁可不用。
3. **用测试表达不变量**：测试不仅防 bug，也是概念边界的可执行说明。
4. **重命名和删除**：把多个同义词合并，删掉没有真实语义负载的层。
5. **写回 Wiki 和项目指令**：把有效概念沉淀到 [[Code-as-Conceptual-Infrastructure]] 的外部记忆中。

## 前提与局限性

- **维护前提**：认知债务只有在系统需要长期演化、多人协作或高责任场景中才特别重要。
- **经济边界**：一次性脚本、低风险原型和短期探索可以接受较高认知债。
- **测量难点**：认知债无法像测试失败那样直接量化，需要 review、onboarding 和修改速度等间接信号。
- **AI 边界**：Agent 可以帮助重命名和生成解释，但不能替团队承担最终理解。

## 关联概念

- [[Conceptual-Model]]：认知债务缺失的对象
- [[Vocabulary-Building]]：词汇生成过快会产生认知债
- [[Technical-Debt-Avoidance]]：清债不能只动结构，也要清理理解
- [[Ubiquitous-Language]]：共享语言可降低认知债
- [[Code-as-Conceptual-Infrastructure]]：认知债是概念基础设施失修的表现
