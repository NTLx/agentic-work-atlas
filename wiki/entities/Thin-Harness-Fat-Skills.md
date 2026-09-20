---
type: entity
title: Thin-Harness-Fat-Skills
aliases:
  - Thin Harness Fat Skills
definition: "一种 Agent 架构取向：把领域知识和可复用工作方法尽量封装为 Skills，同时让 Harness 聚焦跨任务的上下文、权限、工具、验证与运行时控制；‘薄/厚’是复杂度放置的权衡，不是普遍定律。"
created: 2026-05-13
updated: 2026-09-19
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
  - "[[20260803-google-agent-skills-build-test-scale]]"
  - "[[2608.19880-envharness-agent-learning]]"
---

# Thin-Harness-Fat-Skills

> [!definition] 定义
> **Thin Harness, Fat Skills（薄 Harness 厚 Skill）** 是一种复杂度放置策略：领域知识、流程经验和可复用方法尽量封装为 Skill；Harness 保留跨任务都需要的上下文管理、工具接入、权限、安全、验证和运行时控制。这里的“薄”是避免把领域逻辑硬编码进平台层，而不是把 Harness 缩到只剩调度器。

## 关键数据点

- **核心理念**: Harness 只做最少必要的事（调度、路由、基础安全），复杂逻辑和领域知识封装在 Skill 中
- **与主流的对比**: 主流 Agent 框架（如 OpenClaw、Claude Code）将大量工程精力投入 Harness Engineering（Context 管理、多 Agent 编排、工具调度），GBrain 反其道而行
- **实现方式**: 通过 "Skillify" 将非结构化知识转化为可被 Agent 高效调用的结构化资产——万物皆可为 Skill，处处皆可存记忆
- **设计动机**: 避免 Harness 层因领域逻辑不断膨胀，同时让知识/Skill 层独立演化。
- **2026-08 新证据**: Google Agent Skills 的公开实践显示，“Fat Skills”本身需要 OWNERS、EVAL、lint、link check、on-submit/weekly regression 等治理；把复杂度移到 Skill 并不会消除工程成本，只是改变维护边界。
- **环境侧补充**: EnvHarness 表明 Harness 还可以通过 Stage/Contract 等包装层改变 Agent 与环境的交互条件，同时保持原 verifier；这说明“Harness 应尽量薄”必须让位于可验证的跨任务控制需求。

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

更稳妥的边界是：**跨任务且需要一致执行的保证留在 Harness，领域特定且可独立维护的知识留在 Skill。** Skill 路由本身可以包含语义判断，但高影响权限、预算、schema、验证和失败关闭不应仅由 Skill 自己决定。

## 关联概念

- [[GBrain]] — Thin Harness, Fat Skills 的主要实践案例。
- [[Harness-Engineering]] — 主流的 Harness 重型化路径，Thin Harness 的对照面。
- [[Agent-Harness]] — Agent 基础设施的 12 组件模型；Thin Harness 只实现其中的最小必要子集。
- [[Progressive-Disclosure]] — Skills 实现渐进式披露的技术基础。
- [[LLM-Wiki]] — LLM Wiki 的设计也体现了"让 LLM 做维护、人做策展"的薄层哲学。
- [[Agent-Workflow-Patterns]] — 不同 Workflow Pattern 对 Harness 厚度的要求不同。
- [[Latent-Space-vs-Deterministic]] — Thin Harness 的底层分工原则：确定性任务给 Harness，语义任务给 Skill。
