---
type: entity
title: Public-only Constraint
aliases:
  - Public-only Constraint
  - 公开频道约束
definition: "要求 AI Agent 只在公开协作空间工作、拒绝私聊的组织约束，用透明交互换取知识扩散和渗透式学习"
created: 2026-05-18
updated: 2026-05-26
tags:
  - organization
  - AI-Agent
  - culture
related_entities:
  - "[[Lehrwerkstatt]]"
  - "[[Osmosis-Learning]]"
  - "[[River-Agent]]"
  - "[[Agent-Native]]"
  - "[[Organization-as-Agent-Harness]]"
  - "[[Agent-Knowledge-Management]]"
source_raw:
  - "[[Learning on the Shop floor]]"
  - "[[OpenClaw + 6 个 Agent 运转半个月，从聊天到干活的完整工程实践]]"
---

# Public-only Constraint

> [!definition] 定义
> **Public-only Constraint** 是一种组织设计约束：AI Agent 默认只在公开频道工作，拒绝私聊或封闭对话。它把人与 Agent 的协作过程变成可被观察、搜索和复用的公共知识资产。

## 关键数据点

- Shopify 的 River Agent 被设计为只在公开频道中工作，员工可以围观、搜索和复用他人的 Agent 交互。
- 公开交互让 prompt、纠偏方式、审查标准和本地知识自然沉淀到组织层面。
- 该约束把 AI 使用从个人效率工具转化为组织学习基础设施。

## 前提与局限性

- 需要足够高的心理安全感，否则公开交互会抑制试错。
- 不适用于包含个人隐私、商业机密或合规限制的任务。
- 公开频道会制造噪音，必须配合搜索、标签和知识整理机制。

## 组织学习的三个转变

Public-only Constraint 不是"把聊天搬到公开频道"那么简单。它改变了组织知识的三个维度：

| 维度 | 私聊模式 | 公开频道模式 |
|------|---------|------------|
| 知识存储 | 个人记忆和聊天记录 | 可搜索、可引用、可复用的组织资产 |
| 学习路径 | 培训课程和文档 | 观察真实工作流中的 Agent 使用方式 |
| 知识类型 | 显性知识（写下来的） | 隐性知识（拆任务、写指令、纠错的方式） |

Shopify 的 River Agent 数据说明了这一点：过去 30 天，5,938 名员工在 4,450 个频道中使用或观察 River。River 的 PR merge rate 在两个月内从 36% 提升到 77%，不是因为底层模型切换，而是因为员工持续改进 River 的 instructions、memory 与 skills——这些改进都发生在公开频道中，成为全组织可观察的进化过程。

## 与组织 Harness 的连接

Public-only Constraint 本质上是把组织通信规则变成了 Agent harness 的一部分。传统 harness 写在代码里（权限、路由、调度），Public-only Constraint 把 harness 写进了**组织交互协议**里：不让 Agent 私聊，就是把学习、审计和知识扩散嵌入运行环境。

这与 [[Organization-as-Agent-Harness|组织即 Agent Harness]] 的理念一致：组织的通信规则、知识管理流程和协作模式本身就是 Agent 的运行时约束。约束不只保护安全，还创造了 [[Osmosis-Learning|渗透式学习]] 和 [[Lehrwerkstatt|教学工坊]] 的制度条件。

## 关联概念

- [[Lehrwerkstatt]] — Public-only Constraint 是教学工坊的核心制度条件。
- [[Osmosis-Learning]] — 公开过程让员工通过观察自然学习。
- [[River-Agent]] — Shopify 实践该约束的 Agent 载体。
- [[Agent-Native]] — 面向 Agent 重新设计组织流程。
- [[Organization-as-Agent-Harness]] — 组织通信规则本身就是 Agent harness 的一部分。
- [[Agent-Knowledge-Management]] — 公开交互沉淀为可复用的组织知识资产。
