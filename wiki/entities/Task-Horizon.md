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
definition: "用于描述 AI 模型在给定评测设置下可端到端完成的人类可命名工作块时长的能力指标；结果依赖任务域、成功率阈值与测量方法，可补充其他 benchmark，但不宜作为跨领域的单一能力尺度。"
created: 2026-06-06
updated: 2026-11-28
evidence_level: medium
claim_type: mixed
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
  - "[[Agent-Adoption-Curve]]"
source_raw:
  - "[[20260604-anthropic-recursive-self-improvement]]"
  - "[[how-agents-are-transforming-work]]"
---

# Task Horizon（任务视野）

> [!definition] 定义
> **任务视野 (Task Horizon)** 是给定任务集及成功率阈值下，模型或 Agent 能完成的任务所对应的人类参考完成时长；不是 Agent 持续运行的墙钟时间。定义参照 [METR Task-Completion Time Horizons](https://metr.org/time-horizons/) 和 [Clarifying limitations](https://metr.org/notes/2026-01-22-time-horizon-limitations/)；此处用于纠正已有定义，未正式编译新来源或核验 Anthropic 估计与 METR 方法完全一致。Anthropic 2026-06 一手数据：从 Opus 3 的 4 分钟 (2024-03) 到 Sonnet 3.7 的 90 分钟 (2025-03) 到 Opus 4.6 的 12 小时 (2026-03)，每 4 月翻一倍。这组数据可作为观察长程执行能力变化的一个指标，但“每 4 个月翻倍”是经验拟合，不是物理定律，也不能脱离任务域、成功率阈值与测量方法解释。

## Task Horizon 如何补充 SWE-bench

| 度量 | 性质 | 弱点 |
|------|------|------|
| SWE-bench 分数 | 单任务通过率 | 可被针对性优化、过拟合 |
| 任务视野 | 给定成功率下的参考人类任务时长 | 依赖任务分布、时长估计、成功判定、拟合与执行设置，也可能受污染及针对性优化影响 |
| 公司 PR "SOTA" | 单一指标 | 公关噪音大 |

## 关键时间表（Anthropic 2026-06 公开）

| 模型 | 时间 | 任务视野 |
|------|------|----------|
| Claude Opus 3 | 2024-03 | 4 分钟 |
| Claude Sonnet 3.7 | 2025-03 | 90 分钟 |
| Claude Opus 4.6 | 2026-03 | 12 小时 |

机械外推可得到 12 个月 ×8、24 个月 ×64，但这只是延长当前经验趋势的情景计算，不是能力预测；“可完成某个时长的评测任务”也不能直接等同于替代一个岗位。

## 与其他 benchmark 的关系

2026-06 Anthropic 来源概括 SWE-bench 与 CORE-Bench 分别约两年、十五个月从低个位数到饱和；未在本轮复核其具体版本、难度、分母、时间序列或饱和标准。前者衡量软件问题解决率，后者衡量科学计算复现，均不能直接等同 Task Horizon 测量，也不能据饱和用时比较推理能力进步速度。

## 用户侧请求时长分布（OpenAI 2026-06 样本）

OpenAI 2026-06 经济研究论文使用 LLM-as-judge 估计 Codex 用户请求对应的人类工作时长，从用户侧提供了任务视野的分布数据。

| 阈值 | 截至 2026-05 样本个人用户至少一次请求比例 | 说明 |
|------|------------------------|---------|
| > 30 分钟 | 80.6% | 至少一次请求 |
| > 1 小时 | 70.2% | 不代表每日使用 |
| > 4 小时 | （未公布精确值） | — |
| > 8 小时 | 25.6% | 不代表完成或持续运行 |

**99 分位用户的日运行量**：到 2026 年 6 月，OpenAI 内部 99 分位日活用户每天产生 60+ 小时 agent turns（跨多个并行 agent）——用户从"一次问一个答案"转向"全天编排多个 agent 任务"。

与 [[20260604-anthropic-recursive-self-improvement|Anthropic 数据]] 的互补关系：
- Anthropic 数据是 **AI 能力侧**——来源报告的参考任务时长能力估计（Opus 4.6: 12 小时），并非连续运行时长
- OpenAI 数据是 **用户行为侧**——用户实际在让 AI 做多长的任务（25.6% 用户已提交 8+ 小时任务）
- 两组数据分别描述能力估计与用户请求；用户提交长任务不表示模型成功完成，不能作为同一指标的相互验证

## 前提与局限性
- **任务域限制** — 具体评测的任务分布与测量合同决定可解释范围；不能把软件任务估计直接外推到物理实验、销售谈判等
- **外推是经验** — 4 月翻倍不是物理定律；上下文长度、工具稳定性、算力上限都可能成为拐点
- **测量方法不公开** — Anthropic 没说"12 小时"具体怎么测的（独立任务？多步？带工具？）
- **OpenAI 数据为 LLM 估计** — OpenAI 的用户侧数据由 LLM-as-judge 估计，论文标注为"方向性"，且仅基于 0.1% 随机抽样用户
- **用户群选择偏差** — 内部员工与个人用户是不同样本；本文用户覆盖率来自样本个人用户，不能泛化为全体劳动者。

## 关联概念
| 本库主题 | Task Horizon 的连接 |
|---------|-----------------|
| [[Recursive-Self-Improvement]] | 任务视野可作为观察长程执行能力变化的一个外显指标 |
| [[Coding-Agents]] | 参考任务时长估计不保证任意十二小时开发任务可独立完成 |
| [[Agentic-Engineering]] | 能力估计变化可能改变可委派范围；不等于净产出同比增长 |
| [[AI-Capability-Gap]] | 校准"AI 究竟到了什么程度" |
| [[AI-Psychosis]] | 任务视野是避免"震撼错位"的最直观锚点 |
| [[Allocation-Economy]] | 任务视野延长会扩大可委托工作块，但不直接等同于岗位替代 |
| [[AI-Labor-Bottleneck-Shift]] | 可能改变执行与选题的相对瓶颈，须按实际工作流验证 |

## 关联 Benchmark

- [[SWE-Bench]] — 软件工程任务基准
- [[CORE-Bench]] — 科学计算复现基准

## 关键数据点

以上历史数字为已有来源的报告值，本轮只修正指标定义与推断边界，未重新核验完整时间序列及 OpenAI 用户侧样本。
