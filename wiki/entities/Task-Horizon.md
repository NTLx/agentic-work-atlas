---
type: entity
title: Task Horizon
aliases:
  - Task Horizon
  - 任务视野
  - Horizon Length
  - AI Task Horizon
  - Long-Horizon Execution
  - 长程任务执行
definition: "AI 模型能端到端完成的人类可命名工作块的连续时间长度；从 2024 的 4 分钟涨到 2026 的 12 小时，每 4 个月翻一倍，是 AI 时代最可信的能力度量"
created: 2026-06-06
updated: 2026-06-06
tags:
  - ai-capability
  - AI-frontier
  - agentic-engineering
related_entities:
  - "[[Recursive-Self-Improvement]]"
  - "[[Anthropic]]"
  - "[[Coding-Agents]]"
  - "[[Agentic-Engineering]]"
  - "[[SWE-Bench]]"
  - "[[CORE-Bench]]"
  - "[[AI-Capability-Gap]]"
source_raw:
  - "[[20260604-anthropic-recursive-self-improvement]]"
---

# Task Horizon（任务视野）

> [!definition] 定义
> **任务视野 (Task Horizon)** 是 AI 模型在无人介入情况下能端到端完成的人类可命名工作块的连续时间长度。Anthropic 2026-06 一手数据：从 Opus 3 的 4 分钟 (2024-03) 到 Sonnet 3.7 的 90 分钟 (2025-03) 到 Opus 4.6 的 12 小时 (2026-03)，每 4 月翻一倍。这是 AI 时代最可信的"摩尔定律"——它把单一 benchmark 的脆弱性和 PR 噪音都过滤掉，只剩"AI 真的能独立完成多长的任务"。

## 为什么 Task Horizon 比 SWE-bench 更可信

| 度量 | 性质 | 弱点 |
|------|------|------|
| SWE-bench 分数 | 单任务通过率 | 可被针对性优化、过拟合 |
| 任务视野 | 端到端可命名工作块的连续时长 | 难在 benchmark 里"刷分"，因为是连续时间 |
| 公司 PR "SOTA" | 单一指标 | 公关噪音大 |

## 关键时间表（Anthropic 2026-06 公开）

| 模型 | 时间 | 任务视野 |
|------|------|----------|
| Claude Opus 3 | 2024-03 | 4 分钟 |
| Claude Sonnet 3.7 | 2025-03 | 90 分钟 |
| Claude Opus 4.6 | 2026-03 | 12 小时 |

外推：12 月 ×8、24 月 ×64 —— 突破"一个人一天的工作"（AI 顶一个初级岗位）→ 突破"一个人一周的工作"（AI 顶一个独立贡献者）。

## 配套 benchmark 进展

| Benchmark | 起点 | 2026 状态 | 周期 |
|-----------|------|----------|------|
| SWE-bench | 个位数 | 接近饱和 | 约 2 年 |
| CORE-Bench | 个位数 | 接近饱和 | 约 15 月 |

## 前提与局限性
- **仅限软件类任务** — Task Horizon 在 SWE-bench 类任务上度量，不能直接外推到物理实验、销售谈判等
- **外推是经验** — 4 月翻倍不是物理定律；上下文长度、工具稳定性、算力上限都可能成为拐点
- **测量方法不公开** — Anthropic 没说"12 小时"具体怎么测的（独立任务？多步？带工具？）

## 关联概念
| 本库主题 | Task Horizon 的连接 |
|---------|-----------------|
| [[Recursive-Self-Improvement]] | 任务视野是 RSI 的最可信外显指标 |
| [[Coding-Agents]] | 12 小时视野 ≈ Agent 可独立完成一个完整开发任务 |
| [[Agentic-Engineering]] | 视野涨 180 倍 = 单人产出结构改写 |
| [[AI-Capability-Gap]] | 校准"AI 究竟到了什么程度" |
| [[AI-Psychosis]] | 任务视野是避免"震撼错位"的最直观锚点 |
| [[Allocation-Economy]] | 视野 12 小时 = AI 顶一个初级员工，成本结构重写 |
| [[AI-Labor-Bottleneck-Shift]] | 瓶颈从"完成任务"迁到"决定做哪个任务" |

## 关联 Benchmark

- [[SWE-Bench]] — 软件工程任务基准
- [[CORE-Bench]] — 复杂推理任务基准

## 关键数据点

（关键事实、统计、时间线从原 raw 源沉淀，见 source_raw 字段）
