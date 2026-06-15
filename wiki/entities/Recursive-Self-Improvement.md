---
type: entity
title: Recursive Self-Improvement
aliases:
  - Recursive Self-Improvement
  - 递归自我改进
  - RSI
  - AI 改 AI
definition: "AI 系统设计、训练或验证其下一代或同代继任者的能力；当这一回路达到某临界点，AI 进步速度由机器而非人类决定"
created: 2026-06-06
updated: 2026-06-16
evidence_level: medium
claim_type: mixed
tags:
  - AI-frontier
  - ai-capability
  - AI-policy
  - AI-safety
related_entities:
  - "[[Anthropic]]"
  - "[[Anthropic-Institute]]"
  - "[[Task-Horizon]]"
  - "[[Verifiability]]"
  - "[[AI-Capability-Gap]]"
  - "[[AI-Psychosis]]"
  - "[[Coding-Agents]]"
  - "[[Agentic-Engineering]]"
source_raw:
  - "[[20260604-anthropic-recursive-self-improvement]]"
---

# Recursive Self-Improvement（递归自我改进）

> [!definition] 定义
> **递归自我改进 (Recursive Self-Improvement, RSI)** 指 AI 系统设计、训练或验证其下一代或同代继任者的能力。当这一回路达到某临界点，AI 进步速度由机器而非人类决定，Anthropic 在 2026-06 用 frontier 实验室一手数据公开宣告这一进程"已经发生"。

## 关键数据点

Anthropic 2026-05 一手数据：

| 指标 | 数值 | 含义 |
|------|------|------|
| Anthropic 合并代码由 Claude 写的比例 | 80%+ | AI 在改 AI 自身的代码 |
| 工程师人均合并量 vs 2024 | 8x | AI 加速 AI 工程师产出 |
| Code quality parity | 2025 末"差于人类" → 2026 中"对齐" | AI 写的代码质量进入可生产区间 |
| 任务视野（4 月翻倍） | 4 分钟 (Opus 3, 2024-03) → 12 小时 (Opus 4.6, 2026-03) | AI 能独立完成的工作块涨 180 倍 |
| 实验执行加速 | Mythos 52x vs 人类 baseline | AI 优化 AI 训练 pipeline |
| 研究判断胜率 | Mythos 64% | AI 选"哪个问题值得做"开始反超人类 |
| 员工自评生产率 | 4x | 主观体感一致 |

## 演化阶段（Anthropic 自述）

| 阶段 | 时间 | 特征 |
|------|------|------|
| 1 | 2021-2023 | 人类在笔记本上手写代码，AI 不参与 |
| 2 | 2023-2025 | Chatbot 辅助短代码片段 |
| 3 | 2025-2026 | Coding agent 独立读写整文件 |
| 4 | 今天 | Agent 跑代码、互相委派 |
| 5 | 未来 | Agent 训练下一模型（recursive 闭环） |

## 三种未来（Anthropic 框架）

1. **Stall** — 指数轨迹变成 S 曲线，算力/能量约束先到。即使能力冻在 2026 水平也已足以颠覆
2. **Compounding efficiency** — AI 开发高度自动化，人类设方向，100 人公司干 10 万人活
3. **Full recursive** — AI 设计自己的继任者，节奏由算力决定

公共子集：无论哪个 case，"verification 必须现在做"。

## 前提与局限性
- **80% ≠ 100%** — 80% 是 commit-level 不是 deploy-level；merge 不等于 production
- **Code quality parity 是评估侧** — 内部评审打分，主观度未披露
- **任务视野是软件类任务** — 不能直接外推到物理实验、销售谈判
- **Mythos Preview 是未公开** — 公开复现性缺
- **Verifiable pause 难** — 作者自承 training run 比导弹井更易隐藏

## 关联概念
| 本库主题 | RSI 的连接 |
|---------|------------|
| [[Task-Horizon]] | 4 分钟 → 12 小时是 RSI 的最可信度量 |
| [[Verifiability]] | "verifiable pause" 是 RSI 时代的协调机制提议 |
| [[AI-Capability-Gap]] | 80% / 8x / parity 数据校准能力感知 |
| [[AI-Psychosis]] | 一手数据可校准深度用户与外行的认知鸿沟 |
| [[Allocation-Economy]] | 工程师 8x 但团队规模不变 → R&D 成本结构重写 |
| [[AI-Labor-Bottleneck-Shift]] | 瓶颈从"生产代码"迁到"验证 + 集成 + 部署" |

## 前提与局限性
1. **数据来自单一机构** — Anthropic 是工具链、人才、评测集都在极端右尾的 frontier lab；外推到中位公司前必须打折
2. **作者把对齐放在脚注** — "机构克制"是有意为之，让监管者读起来觉得"他们在自我反思"，让算力扩张派读出来"反正还是要扩"
3. **代际对齐漂移** — 当 AI 输出被用来训练下一代，对齐问题从"单代"变成"代际 compounding"；脚注低估了这个放大

## 关联概念
- [[Anthropic]] — 一手数据提供方
- [[Anthropic-Institute]] — 政策发布平台
- Marina-Favaro — 主笔
- Jack-Clark — 联合署名 + 编辑支持
