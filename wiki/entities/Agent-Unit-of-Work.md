---
type: entity
title: Agent Unit of Work
aliases:
  - agent unit of work
  - unit of work
  - Agent 工作单元
definition: "组织愿意交给 Agent 处理的任务单元——其大小、覆盖范围、交接准备、返回值检查和边界约束构成了 Agent delegation 的核心控制参数。Kief Morris (2026) 发现这是跨团队、跨场景反复出现的同一组选择。"
created: 2026-07-14
updated: 2026-07-14
evidence_level: medium
claim_type: synthesized
tags:
  - organization
  - delegation
  - governance
related_entities:
  - "[[Agent-Harness]]"
  - "[[Harness-Engineering]]"
  - "[[Agent-Verification]]"
  - "[[AI-Era-Career-Skills]]"
source_raw:
  - "[[20260713-martin-fowler-fragments-july-2026]]"
---

# Agent Unit of Work

> [!definition] 定义
> **Agent Unit of Work** 是组织愿意交给 Agent 处理的任务单元——其大小、覆盖范围、交接准备、返回值检查和边界约束构成了 Agent delegation 的核心控制参数。Kief Morris (2026) 在 Thoughtworks FOSE retreat 跨多个 session 发现：**"people were making the same handful of choices over and over about a single thing: the unit of work they were prepared to hand to an agent."**

## 五个控制参数

| 参数 | 问题 | 对标 delegation theory |
|------|------|----------------------|
| **大小** | 交给 Agent 的工作有多大？ | 任务粒度 |
| **覆盖** | 覆盖了多少工作？ | 职责范围 |
| **交接准备** | 如何准备交接给 Agent？ | 上下文传递 |
| **返回值检查** | 如何检查 Agent 的产出？ | 验证策略 |
| **边界约束** | 用什么包围 Agent 保持在界内？ | guardrails |

## 核心争议

### Code Review 是否仍然重要？

传统 code review 的严谨性正在转移到其他形式——但转移到了什么形式？

### Agent 处理生产事故的信任边界

团队在多大程度上信任 Agent 识别和修复生产事故？分歧很大，取决于操作上下文。

### 谁可以驾驭 Agent？

"Non-engineers steering agents"的担忧——Sam Ruby 的回应：这不是权限问题，而是 **manage by objective vs manage by method** 的问题。当 manager 使用 LLM 时，不是拿起工具，而是做了一个 hire。

## Unstated Objectives

Fowler 指出的关键风险：人类可以外包执行，但**不能外包验收标准**。真正的危险在于重要的 unstated objectives——未被言说，可能因为甚至未被想象到。

Conformance tests（sensors）比 specifications（guides）更有价值——但很难想象所有需要的 conformance tests。

## 与 Manage by Objective 的映射

Drucker (1959)：当工作者比管理者更了解具体细节时，管理方式是 **manage by objective, not by method**。非工程师驾驭 Agent 正是这个 manager——被自己指挥的东西所超越。

| 框架 | 适合场景 | Agent 语境 |
|------|---------|-----------|
| Manage by method | 管理者了解具体工作 | 工程师精细控制 Agent |
| Manage by objective | 工作者比管理者更专业 | 非工程师给 Agent 目标 |

## 前提与局限性

- "工作单元"框架可能过于静态——未捕获 Agent 信任度随使用而动态扩大的过程
- Drucker MBO 在实践中常退化为 KPI 微管理，LLM 版 MBO 是否也会退化？
- Unstated objectives 被识别但没有系统化解决方案

## 关联概念

- [[Agent-Harness]] — Unit of Work 的边界由 harness 实现
- [[Harness-Engineering]] — 设计和维护工作单元边界是 harness engineering 的核心
- [[Agent-Verification]] — 返回值检查是 verification 的一种形式
- [[AI-Era-Career-Skills]] — 非工程师驾驭 Agent 扩展了 AI 时代的技能边界
