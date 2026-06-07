---
type: entity
title: Elvis Sun
aliases:
  - Elvis Sun
definition: "前 Google Firebase 团队工程师（8年），独立创业者，Agent Swarm 架构实践者和一人团队模式倡导者"
created: 2026-04-10
updated: 2026-05-27
tags:
  - person
  - AI-Agent
  - entrepreneurship
  - Google
  - developer-tools
related_entities:
  - "[[Dan-Shipper]]"
  - "[[Simon-Willison]]"
  - "[[Agent-Orchestration]]"
  - "[[Agent-Swarm]]"
  - "[[OpenClaw-Agent-System]]"
source_raw:
  - "[[OpenClaw + CodexClaudeCode Agent Swarm The One-Person Dev Team Full Setup]]"
validated_source: "https://www.linkedin.com/in/elvissun/"
validated_at: "2026-04-14"
---

# Elvis Sun

> [!definition] 定义
> **Elvis Sun** 曾在 Google 工作 8 年，参与 Firebase 构建。现为独立创业者，专注于构建 AI 驱动的 PR 工具和开发者产品，是 Agent Swarm 架构的早期实践者和"一人即团队"创业模式的倡导者。

## 可验证履历

| 时间 | 事件 |
|------|------|
| ~2014-2022 | Google Firebase 团队工程师（8 年） |
| 2022+ | 独立创业，构建 Medialyst.ai |
| 2026 | 发表 OpenClaw + Codex/Claude Code Agent Swarm 完整架构文章 |

## 核心观点

### Agent Swarm 架构

Sun 是 [[Agent-Swarm|Agent Swarm]] 架构的早期实践者。他的 OpenClaw 系统展示了如何将 Orchestrator（Zoe）和多个 Coding Agent（Codex/Claude Code）组合成一个完整的开发团队。

核心架构原则：

| 层次 | 角色 | 职责 |
|------|------|------|
| Orchestrator (Zoe) | 业务上下文持有者 | 持有客户数据、会议记录、历史决策和失败经验 |
| Coding Agents | 代码执行者 | 只看代码任务，不接触业务上下文 |
| Registry | 状态追踪器 | 追踪任务状态、轮询 tmux/PR/CI |

### 两层上下文分工

Sun 的核心洞察是 context window 是 zero-sum：把代码和客户历史放进同一个模型会互相挤压。他的解决方案是两层分工——Orchestrator 负责高层策略与业务上下文，Coding Agent 负责代码执行。这与 [[Thin-Harness-Fat-Skills]] 的架构哲学一致。

### 一人即团队

Sun 展示了 AI 时代"一人可以构建并与 50 人团队竞争"的可能性。他的系统实现了 94 commits/天、7 PRs/30 分钟的生产力，但更重要的是完整的 PR 生命周期自动化：每个 agent 独立 worktree 和 tmux session；Definition of Done 包括 PR 创建、main 同步、CI、三模型审查、UI 截图；人类只在 Telegram 提示后做 5-10 分钟最终 review。

## 关联概念
| 本库主题 | Sun 的贡献 |
|---------|-----------|
| [[OpenClaw-Agent-System]] | 提供 Agent Swarm 的完整架构实践 |
| [[Agent-Swarm]] | 展示 Orchestrator + Coding Agents 的组合模式 |
| [[Agent-Orchestration]] | Zoe 作为 Orchestrator 的设计模式 |
| [[AI-Labor-Bottleneck-Shift]] | 一人团队的瓶颈从"执行"迁移到"验证、资源和编排" |

## 外部链接

- [个人网站](https://elvis.so/)
- [Twitter/X](https://x.com/elvissun)
- [LinkedIn](https://ca.linkedin.com/in/elvissun)