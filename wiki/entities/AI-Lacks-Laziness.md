---
type: entity
title: AI Lacks Laziness
aliases:
  - AI Lacks Laziness
  - AI 缺乏懒惰美德
  - AI 不懒惰
definition: "LLM 缺少人类时间有限带来的简化压力，容易把任务完成理解为继续生成，而不是删除、合并或拒绝不必要复杂度"
created: 2026-04-21
updated: 2026-05-25
tags:
  - ai-limitation
  - software-engineering
  - design-philosophy
related_entities:
  - '[[Laziness-Virtue]]'
  - '[[AI-Restraint]]'
  - '[[Martin-Fowler]]'
  - '[[YAGNI]]'
  - '[[Cognitive-Debt]]'
  - '[[Agentic-Engineering-Patterns]]'
source_raw:
  - "[[20260414-martin-fowler-fragments]]"
---

# AI Lacks Laziness

> [!definition] 定义
> LLM 缺少人类时间有限带来的简化压力，容易把任务完成理解为继续生成，而不是删除、合并或拒绝不必要复杂度。

## 关键数据点

- **来源语境**: Martin Fowler 转述 Bryan Cantrill 对"懒惰美德丢失"的警告，用来讨论 AI 编程时代的抽象质量。
- **核心问题**: "Work costs nothing to an LLM." 这句话点出 AI 与人类工程师的约束差异：人会因为未来维护痛苦而主动简化，模型默认不会。
- **直接后果**: LLM 可能把系统做大，而不是做好；它能快速堆出功能、分层和胶水代码，却不会自然为未来认知负担付费。
- **Fowler 的例子**: 他在修改 playlist generator 时一度想让 agent 直接实现新能力，但进一步思考后发现应用 [[YAGNI]] 可以用更少代码解决。这说明"动手前重新理解问题"本身就是质量控制。

## 为什么重要

AI Lacks Laziness 是 [[Agentic-Engineering-Patterns]] 的反向约束：agent 能持续执行、快速生成、填补细节，但这些优点如果没有人类判断，会把系统推向更大、更满、更难理解。

它也解释了为什么 AI 时代的 review 不能只看"任务是否完成"。Reviewer 必须追问：这段代码是否本该存在？有没有更小的概念模型？是否引入了未来维护者必须理解的新抽象？这些问题不是模型速度能自动抵消的。

## 前提与局限性

- **前提**: 懒惰美德依赖"人类时间有限"和"未来维护痛感"两个约束；模型既不疲劳，也不会承担长期维护后果。
- **局限性**: 这描述的是当前常见默认行为，不是模型永恒属性。若训练目标、review 信号和 harness 明确奖励删除、合并、简化，模型可以被塑造成更接近"懒惰"的行为。
- **误用风险**: 不能把这个概念理解成"不要用 AI 写代码"。正确结论是：AI 生成必须被更强的简化标准和验证反馈包围。

## 关联概念

- [[Laziness-Virtue]] — AI 缺乏的美德
- [[AI-Restraint]] — AI 缺乏的另一能力（克制）
- [[Martin-Fowler]] — 讨论 AI 对懒惰美德的影响
- [[YAGNI]] — 把"少做"落成具体工程原则
- [[Cognitive-Debt]] — 过度生成最终沉淀为认知债务

## 工程控制方式

| 控制点 | 作用 | 失败时的症状 |
|--------|------|--------------|
| 先问是否需要 | 防止 agent 自动实现不必要功能 | 代码量增加，但问题定义没有变清楚 |
| 要求最小 diff | 限制生成范围，保留 review 可理解性 | PR 过大，维护者只能粗略通过 |
| 用测试和示例约束 | 让模型围绕行为而非想象扩展 | 生成看似完整但没有证据的方案 |
| 让 agent 解释删除方案 | 把"不写代码"也纳入任务空间 | 只会加层、加类、加配置 |

## 与人类懒惰的差异

| 维度 | 人类 | AI |
|------|------|---|
| **时间约束** | 有限 → 追求简化 | 无限 → 追求膨胀 |
| **懒惰美德** | 有（驱动抽象） | 无（驱动复杂化） |
| **系统设计** | 简洁优先 | 功能优先 |
