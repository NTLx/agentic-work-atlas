---
type: entity
title: CLAUDE.md
aliases:
  - CLAUDE.md
  - Claude 项目上下文文件
  - 项目级 Agent 记忆
  - 架构上下文文档
definition: "让 Claude Code 等编码 Agent 在项目中持续继承架构决策、业务规则、范围边界和工作流约束的 Markdown 上下文合约"
created: 2026-05-13
updated: 2026-05-25
tags:
  - AI-Agent
  - Documentation
  - Software-Engineering
related_entities:
  - "[[Claude-Code-CLI]]"
  - "[[Agentic-Engineering]]"
  - "[[AI-Native-Startup]]"
  - "[[Context-Engineering]]"
  - "[[Agent-Harness]]"
  - "[[Multi-Layer-Memory]]"
  - "[[Compound-Engineering]]"
  - "[[Technical-Debt-Avoidance]]"
source_raw:
  - "[[The-Founders-Playbook-05062026_v3]]"
  - "[[20260127-claude-coding-notes]]"
  - "[[The Anatomy of an Agent Harness]]"
  - "[[20260413-llm-wiki]]"
---

# CLAUDE.md

> [!definition] 定义
> **CLAUDE.md** 是项目级 Agent 上下文合约：它把架构原则、业务规则、范围边界、禁止项、验证方式和会话惯例写成可被 Claude Code 自动读取的文件，让每次 coding-agent 会话不必从零重新猜测系统应该如何演化。

## 为什么重要

AI 编码降低了“写代码”的摩擦，也放大了“系统漂移”的风险。没有持久上下文时，每次新会话都可能重新推导技术选择、目录结构、业务边界和实现风格；单个改动看似能运行，多个会话叠加后就会形成互相冲突的局部设计。

CLAUDE.md 的价值不在于给模型更多提示词，而在于把人类已经做过的判断固定成项目可读的外部记忆。它把“为什么这样设计”“哪些东西不要做”“什么证据才算完成”从口头上下文移动到代码库内部，成为 [[Context-Engineering|上下文工程]] 和 [[Agent-Harness|agent harness]] 的一部分。

## 关键数据点

- 《The Founder's Playbook》把 CLAUDE.md 视为 AI-native MVP 的第一批构建产物：先定义架构原则、依赖取舍和阶段性约束，再让 Claude Code 在这些边界内执行。
- 同一来源指出，缺少 specs、architectural decisions 和 context files 时，创始人会在每次会话中反复解释代码库，AI 生成的变更也会偏离原始愿景。
- Karpathy 的 Claude Coding Notes 提醒，简单把偏好写进 CLAUDE.md 并不能消除模型的概念性错误；它是必要的上下文层，不是验证层的替代品。
- 《The Anatomy of an Agent Harness》把 CLAUDE.md 归入长期记忆：短期记忆是会话历史，长期记忆则跨会话保存项目事实、规则和指令。
- LLM Wiki 方法把 CLAUDE.md / AGENTS.md 视为 schema：它规定知识库结构、工作流和维护约束，使 LLM 从通用聊天者变成受约束的知识维护者。

## 应该写什么

| 层面 | 内容 | 作用 |
|------|------|------|
| 架构原则 | 框架选择、模块边界、依赖取舍、弃用方案 | 防止 Agent 重新发明不一致的结构 |
| 业务规则 | 领域词汇、边缘案例、权限规则、不可违反的不变量 | 把领域专知转成可执行约束 |
| 范围边界 | 当前阶段做什么、不做什么、何时允许扩展 | 抑制零摩擦范围蔓延 |
| 工作流约束 | 分支、测试、lint、review、提交惯例 | 让 Agent 的产出可验证、可接收 |
| 会话日志 | 本轮引入的决策、假设、后续风险 | 让上下文随代码库共同演化 |

## 反模式

- **把 CLAUDE.md 当万能 prompt**：它能改善上下文，但不能替代测试、类型检查、代码审查和安全扫描。
- **只写做法，不写原因**：如果只记录“用 X 框架”，Agent 仍不知道何时不能换框架；真正有价值的是 trade-off 和放弃路径。
- **无限堆积规则**：上下文文件过长会变成噪声源。稳定约束应进入 CLAUDE.md，临时任务细节应进入 issue、计划文件或会话记录。
- **单文件覆盖一切**：大型项目需要目录级 CLAUDE.md 或局部规范，否则全局规则会过粗，局部代码仍会漂移。
- **写后不维护**：过期的上下文比没有上下文更危险，因为 Agent 会把旧规则当成当前事实。

## 与相邻概念的边界

| 概念 | 区别 |
|------|------|
| [[Claude-Code-CLI]] | Claude Code 是执行环境；CLAUDE.md 是它读取的项目上下文 |
| [[Context-Engineering]] | Context Engineering 是整体信息架构；CLAUDE.md 是其中的项目级、文件化载体 |
| [[Agent-Harness]] | Harness 管理工具、记忆、验证和安全；CLAUDE.md 是长期记忆和 prompt construction 的输入 |
| [[Compound-Engineering]] | Compound Engineering 强调经验沉淀复用；CLAUDE.md 是把沉淀写回代码库的常见机制 |
| [[Technical-Debt-Avoidance]] | 技术债预防依赖验证和设计判断；CLAUDE.md 负责让这些判断跨会话可见 |

## 前提与局限性

- CLAUDE.md 的有效性依赖团队持续维护；它不是一次性初始化文件。
- 它适合记录稳定约束、重要权衡和可复用惯例，不适合承载所有临时任务上下文。
- 它只能减少 Agent 猜测，不能保证模型理解正确；关键行为仍需要测试、lint、review 和运行时验证闭环。
- 在多人或多 Agent 项目中，CLAUDE.md 还需要权限、变更审查和版本控制，否则会成为新的治理盲区。

## 关联概念

- [[Claude-Code-CLI]] - 主要读取和执行这类项目上下文的编码 Agent
- [[Context-Engineering]] - 设计 Agent 每次推理看到什么、何时看到
- [[Agent-Harness]] - 将长期记忆、工具、验证和安全护栏组织成可运行系统
- [[AI-Native-Startup]] - CLAUDE.md 是 AI 原生 MVP 防止架构漂移的基础设施
- [[Compound-Engineering]] - 把有效做法写回系统，形成复利
