---
type: entity
title: Mythical Man Month
aliases:
  - Mythical Man Month
  - Mythical Man-Month
  - The Mythical Man-Month
  - 人月神话
definition: "Fred Brooks 1975 年出版的软件工程经典；提出 Brooks 法则（adding manpower to a late software project makes it later）与 communication overhead 二次方增长定律；在 AI 时代被 [[Horn]] 重新映射为「spinning up ten agents 的挑战」"
validated_source: "https://en.wikipedia.org/wiki/The_Mythical-Man-Month"
validated_at: "2026-08-19"
created: "2026-08-19"
updated: "2026-08-19"
tags:
  - entity
  - software-engineering
  - classic
  - communication-overhead
related_entities:
  - "[[Horn]]"
  - "[[Agent-Harness-Engineering]]"
  - "[[Multi-Agent-System]]"
source_raw:
  - "[[20260815-engineers-history-reinvention]]"
---

# Mythical Man-Month（《人月神话》）

Fred Brooks 1975 年出版的软件工程经典，源自其 1964 年 IBM System/360 操作系统管理经验。

## 核心命题

1. **Brooks 法则**：向一个已经延期的软件项目增加人手只会让它更延期——新成员需要学习、培训、产生更多沟通开销，原成员还要分出时间教他们。
2. **Communication overhead 二次方**：n 个工程师之间的沟通路径数 = n(n-1)/2——增加人手导致沟通开销以 headcount 平方增长。
3. **外科手术式团队**：少数精干成员比大量平庸成员产出更高。

## AI 时代的回归

[[Horn]] 在 2026-08 的文章中重新映射：

> "It's about how communication overhead scales quadratically with headcount and, if you read between the lines, the challenges you'll have spinning up ten agents"

**Multi-agent 系统的核心挑战**：当 agent 数量 n 增加，agent 间通信路径 = n(n-1)/2——这与 Brooks 1975 的二次方定律同构。Multi-agent framework（如 AutoGen、CrewAI）的协调成本是 scaling 的核心瓶颈。

## 与库中概念的对标

- 与 [[Agent-Harness-Engineering]] 同构：harness 设计需要管理 multi-agent 通信
- 与库中 multi-agent 主题（如有 entity）同构
- 与 Geoffrey Litt "Understanding is the new bottleneck"（forward reference）间接同构——agent 协调是新瓶颈

## 经典地位

- 软件工程领域被引用最频繁的著作之一
- Fred Brooks 后来在《人月神话》20 周年纪念版（1995）增补了"没有银弹"反思
- 仍是程序员/工程师必读书目

## 可验证链接

- Wikipedia: https://en.wikipedia.org/wiki/The_Mythical-Man-Month
- Essay: https://web.archive.org/web/20200713185401/http://worrydream.com/whatever/sources/Brooks-MythicalManMonth.pdf

## 关键数据点

- Fred Brooks 1975 年出版，源自 1964 年 IBM System/360 操作系统管理经验
- Brooks 法则：向已延期项目增加人手只会让它更延期
- 沟通路径数公式：n(n-1)/2——沟通开销随 headcount 平方增长
- "外科手术式团队"——少数精干成员比大量平庸成员产出更高
- 1995 年 20 周年纪念版增补"没有银弹"反思
- 被 Horn 2026-08 重新映射为 "spinning up ten agents" 的 multi-agent 挑战
- 多 agent framework（AutoGen、CrewAI）协调成本是 scaling 核心瓶颈

## 前提与局限性

- 1975 年观察基于大型机时代，与 AI 时代 multi-agent 通信成本同构但未必同机制——agent 通信可能通过 handoff/memory 而非实时交互
- Brooks 法则的"增加人手延期"假设团队成员需要培训——AI agent 即时部署可能减轻此效应
- 沟通开销二次方在结构化通信协议（如 ACP、三态协议）下可能压缩
- 经典理论未必能解释"agent 池"模式（如 GitHub Copilot 大规模并行 agent）
- [[Orchestrators-Tax]] 重新定义"外科手术式团队"——编排者承担 cognitive locality 切分责任

## 关联概念

- [[Horn]] — 重新映射人月神话到 AI agent 时代
- [[Agent-Harness-Engineering]] — Harness 管理 multi-agent 通信
- [[Multi-Agent-System-Pathology]] — multi-agent 群体的组织病理
- [[Agent-Orchestration]] — 编排层处理 Brooks 沟通开销
- [[Orchestrators-Tax]] — 编排者承担 cognitive locality 切分
- [[Peter-Naur]] — 与人月神话并称的软件工程哲学经典
- [[Software-Development-Autonomy-Levels]] — 不同自治级别下 Brooks 法则表现不同