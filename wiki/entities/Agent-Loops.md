---
type: entity
title: Agent Loops
aliases:
  - Agent Loops
  - Agent 循环调度
  - 时间驱动 Agent
definition: "让 Agent 按时间或事件持续运行、检查状态、修复问题和汇总反馈的自动化编排模式"
created: 2026-05-08
updated: 2026-07-08
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
  - "[[Loss-Function-Development]]"
  - "[[Agent-Verification]]"
  - "[[Human-Governor-Agent-Operator]]"
source_raw:
  - "[[Anthropic's Boris Cherny: Why Coding Is Solved, and What Comes Next]]"
  - "[[20260630-loop-engineering-andrew-ng]]"
  - "[[20260706-getting-started-with-loops-claude-code]]"
  - "[[20260624-loops-rediscovering-cybernetics]]"
  - "[[20260611-loss-function-development]]"
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

## Claude Code 官方四种循环分类法（2026-07）

Anthropic Claude Code 团队（delba_oliveira）按**触发机制和停止条件**将 Loop 分为四种类型，与 Andrew Ng 按时间尺度的分类互补：

| Loop 类型 | 触发方式 | 停止条件 | Claude Code Primitive | 适用场景 |
|-----------|---------|---------|----------------------|---------|
| **Turn-based** | 用户 prompt | Claude 判断任务完成 | 手动 prompt | 探索性或一次性短任务 |
| **Goal-based** | 实时 prompt | 目标达成 OR 最大 turn 数 | `/goal` | 有可验证退出标准的任务 |
| **Time-based** | 时间间隔 | 用户取消 OR 工作完成 | `/loop`, `/schedule` | 周期性工作、对接外部系统 |
| **Proactive** | 事件或计划 | 每次任务目标达成 | `/schedule` + `/goal` + auto mode + dynamic workflows | 持续的、定义明确的工作流 |

**关键设计原则**：

- **Loop 输出质量取决于围绕 loop 的系统**：保持代码库整洁、编码验证步骤为 SKILL.md（让 Agent 自验证）、文档易达、独立 agent 做代码审查（fresh context 避免自我偏见）
- **Token 管理分层策略**：选择正确的 primitive 和模型、定义清晰成功/停止条件、pilot before large run、脚本化确定性工作、匹配 routine 频率与被监控对象变化频率
- **编码异常为系统改进**：当单个结果不达标时，不只修复单个问题，而是编码为系统改进，惠及所有未来迭代

**与 Andrew Ng 三层模型的关系**：Ng 按角色和时间尺度划分（coding / developer feedback / external feedback），ClaudeDevs 按操作原语划分。Turn-based 和 Goal-based 对应 Ng 的 Agentic Coding Loop，Time-based 对应 Developer Feedback Loop 的自动化版本，Proactive 对应 External Feedback Loop 的持续运行版本。

## 控制论视角：Loop Engineering 即 Cybernetics（2026-06）

PeyMonee 指出 Loop Engineering 并非新学科，而是 Norbert Wiener 1948 年**控制论（Cybernetics）** 在 AI Agent 时代的重新发现。词源是希腊语 steersman（舵手）——Agent 就是需要被驾驭的决策者。

从控制论提取的五条结构原则：

| 原则 | 控制论对应 | Agent 工程映射 |
|------|-----------|---------------|
| Loop 是工作单元，不是任务 | 系统视角 | 人从 loop 内执行者升级为 loop 作者，模型是子程序 |
| Permission ≠ Correctness | 独立观测器 | guardrails（是否被允许）和 verification（是否正确）是不同问题 |
| 无停止条件 = 无限回归 | Governor / 调速器 | 设上限、检测停滞、超出包络时升级到人类 |
| Skills 复合，prompts 蒸发 | 模块化设计 | 命名良好的 skills 持续增值，每次重新推导只消耗 token |
| Encode the what not the how | 目标导向控制 | 指定目标、边界和完成定义，让模型选择路径 |

**核心洞察**：Agent 自动化（编码、合规、客户运营）始终是同一个动作——**定义目标、画包络线、检查结果、命名负责人**（"Define the goal, draw the envelope, check the result, name the owner"）。这与 [[Human-Governor-Agent-Operator]] 和 [[Escalation-Based-Human-Oversight]] 中的升级机制形成理论呼应。

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
- [[Loss-Function-Development]] - LFD 将 /goal loop 推向外层梯度下降，超越 spec-driven development
- [[Agent-Verification]] - 控制论视角下 verification 是独立于 permission 的必要检查
- [[Human-Governor-Agent-Operator]] - Governor 概念：设上限、检测停滞、超出包络时升级
