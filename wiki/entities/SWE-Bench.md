---
type: entity
title: SWE-Bench
aliases:
  - SWE-Bench
  - SWE-bench
  - Software Engineering Benchmark
definition: "软件工程任务的标准化评测基准——给 agent 一段 GitHub issue + 代码库，评估它能多快修好 bug；从 2024 的低个位数涨到 2026 接近饱和"
created: 2026-06-06
updated: 2026-06-16
evidence_level: medium
claim_type: mixed
tags:
  - benchmark
  - software-engineering
  - AI-evaluation
related_entities:
  - "[[CORE-Bench]]"
  - "[[Task-Horizon]]"
  - "[[Coding-Agents]]"
  - "[[Agentic-Engineering]]"
source_raw:
  - "[[20260604-anthropic-recursive-self-improvement]]"
---

# SWE-Bench

> [!definition] 定义
> **SWE-Bench (Software Engineering Benchmark)** 是软件工程任务的标准化评测基准——给 agent 一段 GitHub issue + 代码库，评估它能多快修好 bug。从 2024 的低个位数涨到 2026 接近饱和（约 2 年周期）。

## 关键数据点

- 起点（2024）：个位数通过率
- 终点（2026）：接近饱和
- 周期：约 2 年
- 与 Task Horizon 的关系：SWE-Bench 饱和 = agent 能独立完成 issue 级任务
- 是 [[Task-Horizon]] 度量的核心 benchmark

## 前提与局限性

- 前提：任务可被清晰切环（bug 描述 + 代码库 + 测试）
- 局限：单一 benchmark 可被针对性优化、过拟合
- 配合 [[CORE-Bench]] 一起看更全面

## 关联概念

- [[CORE-Bench]] — 复杂推理任务基准
- [[Task-Horizon]] — 任务视野度量
- [[Coding-Agents]] — 评测对象
- [[Agentic-Engineering]] — 工程范式
