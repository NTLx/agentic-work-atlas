---
type: entity
title: Agent Loops
aliases:
  - Agent Loops
  - Agent 循环调度
  - 时间驱动 Agent
definition: "让 Agent 按时间或事件持续运行、检查状态、修复问题和汇总反馈的自动化编排模式"
created: 2026-05-08
updated: 2026-05-25
tags:
  - AI-agent
  - claude-code
  - automation
evidence_level: medium
claim_type: mixed
related_entities:
  - "[[Boris-Cherny]]"
  - "[[Claude-Code-CLI]]"
  - "[[Product-Overhang]]"
  - "[[Agent-Swarm]]"
  - "[[Agent-Workflow-Patterns]]"
  - "[[Claude-Code-Automation]]"
  - "[[Agent-Harness]]"
  - "[[Context-Advantage]]"
source_raw:
  - "[[Anthropic's Boris Cherny: Why Coding Is Solved, and What Comes Next]]"
  - "[[20260630-loop-engineering-andrew-ng]]"
---

# Agent Loops（Agent 循环调度）

> [!definition] 定义
> **Agent Loops** 是一种时间驱动的 Agent 自动化模式：让 Agent 以固定频率或持续监听方式运行，反复检查状态、执行修复、整理反馈、推进后台任务，并把结果交给人类或上层系统验收。

## 为什么重要

单次 Agent 调用解决的是“这个任务怎么做”。Agent Loops 解决的是“这个系统如何持续被照看”。当 coding agent 可以读代码、跑测试、修 CI、看 PR、聚类反馈时，最小可行自动化不再是复杂多 Agent 架构，而可能只是一个定时循环。

Boris Cherny 把 loops 描述为极简但有效的范式：让 Agent 每隔一段时间检查某个状态，并在发现问题时行动。这个模式把 Agent 从一次性助手变成持续运行的后台工作者。

## 关键数据点

- Boris 的使用场景包括 PR 看护、自动修 CI、auto rebase、flaky test 维护，以及定期抓取用户反馈并聚类。
- Loop 与 sub-agent 不同：sub-agent 是任务分派，loop 是时间或状态驱动的持续运行。
- Anthropic 后续将这一方向产品化为 Routines：即使本地电脑关闭，后台循环仍可继续运行。
- 当模型开始主动建议“我可以每 30 分钟检查一次并报告”时，说明 loop 正从人类手写 cron 变成模型可理解的工作模式。
- 这一模式是 [[Product-Overhang|产品能力溢出]] 的例子：模型已经能完成持续照看类任务，产品界面和权限模型才开始追上。

## 与自动化层的关系

| 层级 | 关注点 | Agent Loops 的位置 |
|------|--------|--------------------|
| 单次 prompt | 完成一次请求 | 不够，状态不会持续被检查 |
| Sub-agent | 并行拆分任务 | 可作为 loop 内部执行者 |
| Loop / Routine | 定期检查、修复、汇总 | 时间驱动的持续自动化 |
| Harness | 权限、状态、验证、日志和失败恢复 | 管理 loop 的边界和后果 |

因此，Agent Loops 不是替代 [[Agent-Harness|harness]]，而是 harness 内的一种调度形态。真正生产化时，loop 必须被权限、预算、日志、幂等性、回滚和外部验证包住。

## Andrew Ng 的三层循环模型（2026-06）

Andrew Ng 将 Loop Engineering 分解为三个不同时间尺度的循环：

| 循环 | 时间尺度 | 驱动者 | 核心活动 |
|------|---------|--------|---------|
| **Agentic Coding Loop** | 分钟级 | AI Agent | 写代码 → 测试 → 迭代直到无 bug |
| **Developer Feedback Loop** | 几十分钟到小时级 | 人类开发者 | 审查产品 → 引导 Agent → 做高层产品决策 |
| **External Feedback Loop** | 小时到周级 | 用户/市场 | 用户反馈 → A/B 测试 → 驱动产品愿景演化 |

关键洞察：随着 Agentic Coding Loop 的成熟（Agent 能自我测试），开发者角色从 QA 升级为产品决策者。Ng 的 coding agent 可以独立工作约 1 小时，多次用浏览器检查构建结果后才回来。

Ng 将人类在 Developer Feedback Loop 中的不可替代性归因于 **[[Context-Advantage]]**——人类比 AI 知道更多关于用户和产品运行上下文的信息，这不是"品味"而是信息不对称问题。只要人类知道 AI 不知道的东西，Human-in-the-loop 就是必需的。

## 前提与局限性

- **错误累积**：Agent 每 30 分钟犯一次小错，几天后可能变成系统性污染。
- **权限膨胀**：后台 agent 若拥有写权限、生产权限或自动合并权限，必须有更强审计。
- **上下文漂移**：长期运行的 loop 会遇到需求、代码和环境变化，需要重新加载真实状态。
- **成本不可见**：定时循环会持续消耗 token 和工具调用，必须有预算上限和效果指标。
- **验收外置**：修 CI、改 PR、聚类反馈都需要测试、review、日志或人工确认作为完成标准。

## 关联概念

- [[Claude-Code-Automation]] - Agent Loops 是 Claude Code 自动化的时间驱动层
- [[Product-Overhang]] - 模型能力已经能承担后台照看，产品正在补足界面
- [[Agent-Harness]] - 生产 loop 需要 harness 管理权限、状态和验证
- [[Agent-Swarm]] - 大量 loop 可能形成持续运行的 Agent 群
- [[Agent-Workflow-Patterns]] - Loop 是 agent workflow 的一种调度模式
