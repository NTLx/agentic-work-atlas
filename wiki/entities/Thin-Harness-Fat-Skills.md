---
type: entity
title: Thin-Harness-Fat-Skills
aliases:
  - Thin Harness Fat Skills
definition: "GBrain 的架构哲学——Harness 做薄、主要精力放在丰富 Skills 上，让各种功能尽可能通过 Skill 实现，而非在 Harness 层堆砌逻辑"
created: 2026-05-13
updated: 2026-05-13
tags:
  - AI
  - agent
  - architecture
related_entities:
  - "[[GBrain]]"
  - "[[Harness-Engineering]]"
  - "[[Agent-Harness]]"
  - "[[Progressive-Disclosure]]"
source_raw:
  - "[[深度解析LLM Wiki  Obsidian-Wiki  GBrain：Agent时代知识的“自组织”与“自进化”]]"
---

# Thin-Harness-Fat-Skills

> [!definition] 定义
> **Thin Harness, Fat Skills** 是 GBrain 提出的 Agent 架构哲学：建议把 Harness（Agent 基础设施层）做得薄一些，把主要精力放在丰富 Skills（技能/知识模块）上，让各种功能尽可能通过 Skill 来实现。这与主流将重点放在 Harness Engineering 上的思想形成对比。

## 关键数据点

- **核心理念**: Harness 只做最少必要的事（调度、路由、基础安全），复杂逻辑和领域知识封装在 Skill 中
- **与主流的对比**: 主流 Agent 框架（如 OpenClaw、Claude Code）将大量工程精力投入 Harness Engineering（Context 管理、多 Agent 编排、工具调度），GBrain 反其道而行
- **实现方式**: 通过 "Skillify" 将非结构化知识转化为可被 Agent 高效调用的结构化资产——万物皆可为 Skill，处处皆可存记忆
- **设计动机**: 避免 Harness 层过度膨胀导致维护成本激增，同时让知识/Skill 层独立演化

## 前提与局限性

- Thin Harness 的前提是 Skill 体系足够丰富和完善——如果 Skill 质量差，薄 Harness 反而暴露短板
- 在复杂多 Agent 协作场景中，过薄的 Harness 可能导致编排能力不足
- Skill 之间的冲突和优先级管理需要额外机制
- 该哲学更适用于知识密集型 Agent 系统，对于需要强实时控制和硬件交互的场景可能不够

## 关联概念

- [[GBrain]] — Thin Harness, Fat Skills 是 GBrain 的核心架构哲学
- [[Harness-Engineering]] — 主流的 Harness 重型化路径，GBrain 的对照面
- [[Agent-Harness]] — Agent 基础设施的 12 组件模型
- [[Progressive-Disclosure]] — Skills 实现渐进式披露的技术基础
- [[LLM-Wiki]] — LLM Wiki 的设计也体现了"让 LLM 做维护、人做策展"的薄层哲学
