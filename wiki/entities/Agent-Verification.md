---
type: entity
title: Agent Verification
aliases:
  - Agent 自主验证
  - Agentic Verification
definition: "Agent 能自主运行验证循环的能力——不是 lint/type check，而是 agent 能自己启动测试环境、执行操作、观察结果并判断是否通过"
created: 2026-06-12
updated: 2026-07-28
evidence_level: medium
claim_type: mixed
tags:
  - agentic-engineering
  - verification
  - claude-code
related_entities:
  - "[[Claude-Code-CLI]]"
  - "[[Agent-Loops]]"
  - "[[Auto-Mode]]"
  - "[[Validation-Pipeline]]"
  - "[[Captain-Mindset]]"
  - "[[Rubric-Based-Evaluation]]"
  - "[[Software-Development-Autonomy-Levels]]"
source_raw:
  - "[[20260713-microsoft-ships-ai-agents-enterprise-scale]]"
  - "[[20260608-reflecting-on-year-of-claude-code]]"
  - "[[20260620-l8-principal-agentic-workflow]]"
  - "[[20260702-anthropic-harnesses-long-running-agents]]"
  - "[[20260727-github-harness-is-all-you-need]]"
  - "[[20260726-berkeley-auto-software-dev]]"
  - "[[20260708-towards-autonomous-software-dev.pdf]]"
---

> [!definition] 定义
> Agent 验证不是传统意义上的自动化测试（lint、type check、unit test），而是 agent 能**自主运行验证循环**——自己启动测试环境、执行操作、观察结果、判断是否通过，并在失败时自行修复。

## 关键数据点

- Claude Code 的 verification 路径: agent 打开 CLI → 测试自己写的 feature → 观察结果 → 修复
- Desktop development skill: Claude 启动本地 desktop app → 用 computer use 点击测试 UX → 测试 edge cases → 修复并重新检查
- 验证循环示例: iOS simulator / Android simulator / desktop computer use
- 从 Opus 4 开始实现 self-testing，到今天已成常态

## 异构验证与保障对象转移（07-28 扩展）

两篇同窗口来源（GitHub 2026-07-27 / Berkeley RDI 2026-07-26）从实践和理论两侧扩展了验证命题：

**实践侧：Rubber Duck 跨模型评审**（GitHub Copilot 机制）：请求**不同模型家族**审查实现——用 GPT 5.6 Terra 写的代码请 Sonnet 审查。原理：不同训练数据 → 不同盲点，单模型自审是盲点自洽。可与 Autopilot 组合成循环，直到双方同意只剩边际收益。这是异构验证的轻量工业形态。

**理论侧：保障对象从产物转移到 agent**（Berkeley position paper）：

> **CORE RISK**：当同一个 agent 既写实现又写测试，通过测试只证明**一致性**，不证明**正确性**。

自治 agent 会同时生成实现、测试、文档和理由——创造跨越所有"互相验证的产物"的**关联失败**。因此验证软件产物不再足够，还必须审计产出它的 agent（规格、技能、记忆、决策溯源、执行轨迹）。独立验证者 agent 只有在具备**真正独立的目标**、可信的评估机制、有原则的分歧解决协议时才有效。

**两侧配对的关键张力**：跨模型家族评审只是**训练数据级独立**——完整论文给出两个具体失败机制：verifier 与 generator 可能 **talk past each other**（互不理解、无法收敛），或 **co-adapt**（共同适应，直到测试仅仅背书实现的 bug）。这正是"不同模型家族不同盲点"不够的原因：Berkeley 要求的是**目标级独立**。Rubber duck 降低了自洽盲区风险，但未满足完全独立验证的条件——自治程度越高（[[Software-Development-Autonomy-Levels|Level II/III]]），这一缺口越致命。

## 前提与局限性

- **依赖工具使用能力**: Agent 必须能访问运行环境（terminal、simulator、browser），无法访问时 verification 仍然是外部的
- **内部案例为主**: 当前最佳实践来自 Anthropic 内部，外部企业是否同样适用存疑
- **需要 skill 支撑**: 复杂验证（如 desktop app 测试）需要专门的 skill 教 agent 如何操作

## 关联概念

- [[Claude-Code-CLI]] — Agent verification 的主要载体
- [[Agent-Loops]] — Verification 是 loop 的核心环节
- [[Auto-Mode]] — Auto mode 让 verification 循环可以无人值守运行
- [[Validation-Pipeline]] — 系统化验证管线：对抗审查 + e2e 测试 + 证据生成 + PR babysitting
- [[Captain-Mindset]] — 验证能力的组织意义：人类从审 diff 转向看证据
- [[Software-Development-Autonomy-Levels]] — 自治级别越高，保障对象越从产物转向 agent（CORE RISK：一致性 ≠ 正确性）
