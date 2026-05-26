---
type: entity
title: Accessibility-Complexity-Evaluation
aliases:
  - Accessibility Complexity Evaluation
  - 无障碍代码复杂度评估
definition: "用确定性启发式评分决定无障碍 Agent 能否自动修改前端代码的门控机制"
created: 2026-05-18
updated: 2026-05-25
tags:
  - accessibility
  - AI-Agent
  - code-quality
related_entities:
  - "[[Accessibility-Agent]]"
  - "[[Accessibility-High-Risk-Patterns]]"
  - "[[Verifiable-Agent-Engineering]]"
  - "[[Bias-to-Action-LLM]]"
  - "[[WCAG]]"
source_raw:
  - "[[Building a general-purpose accessibility agent—and what we learned in the process]]"
---

# Accessibility-Complexity-Evaluation

> [!definition] 定义
> **无障碍代码复杂度评估** 是 Accessibility Agent 中的一项机制：用一个小型 shell 脚本，基于一组基本启发式规则分析目标代码的相对复杂度，生成评分。评分超过阈值时，Agent 不执行代码变更，而是通知使用者联系无障碍团队咨询。

## 设计动机

避免高成本返工：如果 Agent 对一个复杂代码块生成了"自以为无障碍但实际上不可用"的方案，后续需要大量时间重新审查和修复。复杂度评估是一种前置保护机制。

## 工作流程

1. 脚本分析目标代码 → 生成复杂度评分
2. 评分 < 阈值 → Agent 正常执行修改
3. 评分 ≥ 阈值 → Agent 切换到"仅指导"模式，建议人工介入

## 关键数据点

- 使用 shell 脚本 + 启发式规则（非 LLM 自身判断），避免循环依赖
- 复杂度评估与高风险模式检测配合使用，形成两层保护
- 评分超过阈值时，Agent 不写代码，只输出 guidance 并建议咨询无障碍团队
- 复杂度评估发生在 implementer 写入前，是防止“先生成再返工”的前置闸门

## 为什么必须用确定性脚本

无障碍 Agent 面临一个典型风险：LLM 有强烈的 [[Bias-to-Action-LLM|行动偏差]]，会倾向于“给出一个看起来能修的方案”。但复杂前端组件的无障碍质量不只取决于局部代码，还取决于状态管理、焦点流、键盘交互、屏幕阅读器公告和设计意图。

因此复杂度评估不能由同一个 LLM 自己判断。GitHub 的做法是把门控交给 shell script 和启发式规则，让 Agent 在进入代码修改前先接受外部约束。这个结构类似 [[Verifiable-Agent-Engineering]] 中的确定性骨架：模型可以建议，但能不能动手必须由可审计机制决定。

## 与高风险模式的分工

复杂度评估解决“这段代码太复杂，不应自动改”的问题；[[Accessibility-High-Risk-Patterns]] 解决“这个交互类型本身太危险，不应自动生成”的问题。两者组合后，Agent 有三种行为：

- 低复杂度、非高风险：可以自动修复并输出证据。
- 高复杂度、非高风险：进入指导模式，不写代码。
- 命中高风险模式：拒绝自动修复，建议人工无障碍专家介入。

## 前提与局限性

- 启发式规则的质量决定了评估的准确性——过于简单可能误判，过于复杂本身也需要维护
- 复杂度评分是二元的（通过/不通过），实际复杂度是连续谱，边界情况可能被误判
- 需要与高风险模式检测配合使用，单独使用不足以覆盖所有 Agent 不该碰的场景
- 复杂度脚本本身需要持续回放失败案例，否则阈值会和真实代码库演化脱节
- 低复杂度不代表修复一定正确，仍需要 reviewer、测试和必要时的辅助技术验证

## 关联概念

- [[Accessibility-Agent]] — 复杂度评估是无障碍 Agent 的核心约束机制
- [[Accessibility-High-Risk-Patterns]] — 与复杂度评估配合，形成两层保护
- [[Verifiable-Agent-Engineering]] — 复杂度评估是“行动前验证”的实例
- [[Bias-to-Action-LLM]] — 复杂度门控抑制模型过度动手
- [[WCAG]] — 复杂度评估不能替代 WCAG 和真实辅助技术体验
