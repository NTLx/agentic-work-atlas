---
type: entity
title: Laziness Virtue
aliases:
  - Laziness Virtue
  - 懒惰美德
  - Three Virtues of a Programmer
definition: "程序员用有限时间倒逼抽象、删除和简化的工程美德，使系统以更低认知负担承载更多能力"
created: 2026-04-21
updated: 2026-05-25
tags:
  - software-engineering
  - philosophy
  - programming
related_entities:
  - '[[Martin-Fowler]]'
  - '[[AI-Lacks-Laziness]]'
  - '[[YAGNI]]'
  - '[[Cognitive-Debt]]'
  - '[[Agentic-Engineering-Patterns]]'
source_raw:
  - "[[20260414-martin-fowler-fragments]]"
---

# Laziness Virtue

> [!definition] 定义
> 程序员用有限时间倒逼抽象、删除和简化的工程美德，使系统以更低认知负担承载更多能力。

## 三美德

Larry Wall（Perl 设计者）定义的程序员三美德：

| 美德 | 含义 | 驱动行为 |
|------|------|---------|
| **Hubris** (傲慢) | 相信自己能做得更好 | 追求卓越 |
| **Impatience** (急躁) | 不愿等待 | 追求效率 |
| **Laziness** (懒惰) | 不愿做重复工作 | 追求抽象和简化 |

## 关键数据点

- **提出者**: Larry Wall (Perl 设计者，*Programming Perl* 作者)
- **核心洞察**: "It takes a lot of work to be lazy." 懒惰不是省掉思考，而是先付出设计成本，让未来工作变少。
- **设计哲学**: 懒惰驱动我们建立"最简但不过简"的抽象，减少重复、降低认知负担，并让系统在长期演化中保持可理解。
- **AI 时代的新意义**: 当代码生成变便宜，懒惰美德不再只是程序员趣谈，而是抵抗无意义代码膨胀和 [[Cognitive-Debt|认知债务]] 的质量约束。

## 为什么是美德

懒惰美德的价值不在于"少干活"，而在于重新排列工作：今天多花一点时间理解问题、删掉多余路径、命名正确概念，换取未来更少的重复劳动和更低的维护负担。

它与普通偷懒的区别在于结果方向不同。普通偷懒把成本推给未来；工程上的懒惰把未来成本拉回现在处理，让系统更小、更清楚、更容易继续构建。

## 前提与局限性

- **前提**: 人类时间有限 → 懒惰成为约束 → 驱动简化
- **局限性**: 过度懒惰可能导致过度抽象（增加而非减少复杂度）
- **AI 时代边界**: 如果团队只奖励生成速度和代码量，懒惰美德会被吞掉；如果团队奖励删除、合并、验证和清晰概念，agent 也可以被流程塑造成更"懒惰"的协作者。

## 关联概念

- [[Martin-Fowler]] — 讨论 AI 对懒惰美德的影响
- [[AI-Lacks-Laziness]] — AI 不具备此美德的问题
- [[YAGNI]] — 懒惰美德的具体实践（不要实现未需要的功能）
- [[Cognitive-Debt]] — 懒惰失败时留下的长期理解成本

## Bryan Cantrill 的扩展

Cantrill 的扩展把懒惰从个人习惯提升为抽象美学：好的懒惰不是拒绝工作，而是拒绝被低质量抽象长期奴役。

核心观点：
- 懒惰不是"不做"，而是"聪明地做"
- 懒惰驱动抽象 → 抽象带来杠杆
- 人类时间有限 → 懒惰成为约束 → 系统保持简洁

## AI 协作中的用法

在 coding agent 工作流中，懒惰美德应被翻译成明确的审查问题：

- 这个需求是否应该实现，还是应该被删除、推迟或合并？
- 是否存在比当前 diff 更小的行为变更？
- 新抽象是否减少了未来理解成本，还是只是把代码分散到更多文件？
- Agent 是否解释过为什么没有选择更简单方案？
