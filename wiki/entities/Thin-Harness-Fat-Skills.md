---
type: entity
title: Thin-Harness-Fat-Skills
aliases:
  - Thin Harness Fat Skills
definition: "Agent 架构哲学——Harness 做薄、主要精力放在丰富 Skills 上，让功能通过 Skill 实现而非在 Harness 层堆砌逻辑"
created: 2026-05-13
updated: 2026-05-26
tags:
  - AI
  - agent
  - architecture
evidence_level: medium
claim_type: mixed
related_entities:
  - "[[GBrain]]"
  - "[[Harness-Engineering]]"
  - "[[Agent-Harness]]"
  - "[[Progressive-Disclosure]]"
  - "[[LLM-Wiki]]"
  - "[[Agent-Workflow-Patterns]]"
  - "[[Latent-Space-vs-Deterministic]]"
source_raw:
  - "[[深度解析LLM Wiki  Obsidian-Wiki  GBrain：Agent时代知识的“自组织”与“自进化”]]"
  - "[[The Anatomy of an Agent Harness]]"
---

# Thin-Harness-Fat-Skills

> [!definition] 定义
> **Thin Harness, Fat Skills（薄 Harness 厚 Skill）** 是一种 Agent 架构哲学：Harness（Agent 基础设施层）只做最少必要的事——调度、路由、基础安全，复杂逻辑和领域知识封装在 Skill 中。这与主流将重点放在 Harness Engineering 上的路径形成对照。

## 关键数据点

- **核心理念**: Harness 只做最少必要的事（调度、路由、基础安全），复杂逻辑和领域知识封装在 Skill 中
- **与主流的对比**: 主流 Agent 框架（如 OpenClaw、Claude Code）将大量工程精力投入 Harness Engineering（Context 管理、多 Agent 编排、工具调度），GBrain 反其道而行
- **实现方式**: 通过 "Skillify" 将非结构化知识转化为可被 Agent 高效调用的结构化资产——万物皆可为 Skill，处处皆可存记忆
- **设计动机**: 避免 Harness 层过度膨胀导致维护成本激增，同时让知识/Skill 层独立演化

## 前提与局限性

- Thin Harness 的前提是 Skill 体系足够丰富和完善——如果 Skill 质量差，薄 Harness 反而暴露短板。
- 在复杂多 Agent 协作场景中，过薄的 Harness 可能导致编排能力不足。
- Skill 之间的冲突和优先级管理需要额外机制。
- 该哲学更适用于知识密集型 Agent 系统，对于需要强实时控制和硬件交互的场景可能不够。

## 两种架构路径的对比

Thin Harness 和 [[Harness-Engineering|Harness Engineering]] 不是"谁对谁错"，而是针对不同系统类型的架构选择：

| 维度 | Thin Harness, Fat Skills | Heavy Harness |
|------|-------------------------|---------------|
| 复杂度位置 | Skill 层 | Harness 层 |
| 演化单位 | 单个 Skill 独立迭代 | Harness 整体升级 |
| 典型代表 | GBrain、Obsidian 插件生态 | Claude Code、OpenClaw |
| 适用场景 | 知识密集型、Skill 可独立验证 | 多 Agent 编排、强一致性要求 |
| 风险 | Skill 质量参差、冲突管理弱 | Harness 膨胀、维护成本高 |
| 扩展方式 | 增加 Skill | 增加 Harness 组件 |

GBrain 选择 Thin Harness 的核心原因是：知识密集型 Agent 的能力瓶颈不在调度和路由，而在 Skill 层的知识覆盖度和结构化程度。把工程精力投入 Harness 层的边际收益递减——Harness 做到"够用"后，每新增一个高质量 Skill 的系统价值远大于每优化一次 Harness 编排。

## 与 Latent Space vs Deterministic 的连接

Thin Harness 的底层逻辑与 [[Latent-Space-vs-Deterministic|潜在空间与确定性分工]] 一致：Harness 层处理的是确定性任务（路由、调度、安全校验），这些任务的输入输出可预测，适合用规则实现；Skill 层处理的是需要语义理解的任务（知识检索、内容生成、推理），这些任务需要 LLM 的潜在空间能力。

薄 Harness 的本质是把确定性任务留给确定性系统，把语义任务留给语义系统。如果 Harness 层开始承担语义判断（比如"这个 Skill 是否适用于当前任务"），它就从薄变厚了——同时承担了它不该承担的判断风险。

## 关联概念

- [[GBrain]] — Thin Harness, Fat Skills 的主要实践案例。
- [[Harness-Engineering]] — 主流的 Harness 重型化路径，Thin Harness 的对照面。
- [[Agent-Harness]] — Agent 基础设施的 12 组件模型；Thin Harness 只实现其中的最小必要子集。
- [[Progressive-Disclosure]] — Skills 实现渐进式披露的技术基础。
- [[LLM-Wiki]] — LLM Wiki 的设计也体现了"让 LLM 做维护、人做策展"的薄层哲学。
- [[Agent-Workflow-Patterns]] — 不同 Workflow Pattern 对 Harness 厚度的要求不同。
- [[Latent-Space-vs-Deterministic]] — Thin Harness 的底层分工原则：确定性任务给 Harness，语义任务给 Skill。
