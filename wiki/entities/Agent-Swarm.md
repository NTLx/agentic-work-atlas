---
type: entity
title: Agent Swarm
aliases:
  - Agent Swarm
definition: "多个 Agent 通过并行执行与通信共同扩展 test-time compute 的系统；固定 coordinator/worktree 编排与最小消息原语驱动的动态协作都是其实现形态"
created: 2026-04-09
updated: 2026-09-20
tags:
  - AI-Agent
  - OpenClaw
  - Multi-Agent-System
evidence_level: medium
claim_type: mixed
related_entities:
  - '[[Agent-Loops]]'
  - '[[Boris-Cherny]]'
  - '[[Agent-Orchestration]]'
  - '[[Context-Engineering]]'
  - "[[Multi-Agent-System-Pathology]]"
  - "[[Recursive-Self-Improvement]]"
source_raw:
  - "[[Anthropic's Boris Cherny: Why Coding Is Solved, and What Comes Next]]"
  - '[[OpenClaw + CodexClaudeCode Agent Swarm The One-Person Dev Team Full Setup]]'
  - "[[Multi-Agent 火了，但 AI 的组织病还没人治｜Hao好聊趋势]]"
  - "[[20260917-dwarkesh-noam-brown-agent-swarms-rsi]]"
---

# Agent Swarm

> [!definition] 定义
> Agent Swarm 是多个 Agent 通过并行执行与通信共同扩展 test-time compute 的系统。编码场景中的 Git worktree + tmux + 中央编排是一种实现；更一般的 swarm 也可以只提供消息等低层原语，让 Agent 在运行时形成协作结构。

## 为什么需要 Agent Swarm

直接用 Claude Code 或 Codex 的限制：
- **一次只能盯一个事**：开发后端 API 时没法同时调前端样式
- **上下文窗口是零和的**：填代码 → 无业务上下文；填业务 → 无代码库

Agent Swarm 通过**并行调度 + 上下文分离**解决这些问题。

## 从固定层级到消息原语（2026-09）

Noam Brown 对 OpenAI multi-agent 研究的描述提供了另一种 swarm 架构：与 coordinator → children 的固定委派树相比，系统尽量少预置组织结构，只给 Agent 基础 messaging primitive；Agent 可以在任意时刻互相提问、澄清和比较不同答案，协作 topology 在运行中形成。

Brown 将 multi-agent 的一阶价值解释为**并行扩展 test-time compute**：串行思考继续增加时会遇到 latency ceiling，多 Agent 用更高总 token/协调成本换取 wall-clock 缩短。

**判断**：Agent Swarm 的稳定抽象应从“某套 worktree/tmux 编排”提升为 **parallel compute + context separation + communication + conflict/verification control**。固定层级还是动态消息网络，是 workload-dependent 的设计选择。

- **证据**：[[20260917-dwarkesh-noam-brown-agent-swarms-rsi]]
- **边界**：该来源包含 OpenAI 未发布系统的一手参与者陈述，缺少公开可复现实验；不能据此断言 minimal scaffold 普遍优于显式 hierarchy。

## 架构设计

### Worktree + tmux 模式

每个 Agent 独立的工作环境：

```bash
# Create worktree + spawn agent
git worktree add ../feat-custom-templates -b feat/custom-templates origin/main
cd ../feat-custom-templates && pnpm install

tmux new-session -d -s "codex-templates" \
  -c "/Users/elvis/Documents/GitHub/medialyst-worktrees/feat-custom-templates" \
  "`$HOME/.codex-agent/run-agent.sh` templates gpt-5.3-codex high"
```

### 任务注册系统

```json
// .clawdbot/active-tasks.json
{
  "id": "feat-custom-templates",
  "tmuxSession": "codex-templates",
  "agent": "codex",
  "description": "Custom email templates for agency customer",
  "repo": "medialyst",
  "worktree": "feat-custom-templates",
  "branch": "feat/custom-templates",
  "startedAt": 1740268800000,
  "status": "running",
  "notifyOnComplete": true
}
```

## Agent 选择策略

| Agent | 优势 | 适用场景 |
|-------|------|---------|
| **Codex** | 推理强、跨代码库理解 | 后端逻辑、复杂 bug、多文件 refactor |
| **Claude Code** | 快速、前端好、权限问题少 | 前端工作、Git 操作 |
| **Gemini** | 设计 sensibility | UI 设计 → Claude 实现 |

Zoe 根据任务类型选择 Agent：
- Billing system bug → Codex
- Button style fix → Claude Code
- New dashboard design → Gemini 设计 → Claude 实现

## 监控系统

### Cron 级监控脚本

每 10 分钟运行 `.clawdbot/check-agents.sh`：
- 检查 tmux sessions 是否存活
- 检查 tracked branches 的 open PRs
- 检查 CI 状态（via gh cli）
- 自动 respawn 失败 agent（max 3 attempts）
- 只在需要人工介入时 alert

### Definition of Done

Agent 完成任务的标准：

- PR created
- Branch synced to main（no merge conflicts）
- CI passing（lint, types, unit tests, E2E）
- Codex review passed
- Claude Code review passed
- Gemini review passed
- Screenshots included（if UI changes）

## 并行开发效率

Elvis 的实战数据：
- **94 commits in one day**：有 3 个 client calls，没打开编辑器
- **7 PRs in 30 minutes**：编码和验证大部分自动化
- **Commits → MRR**：实时 B2B SaaS，当天交付大部分 feature requests

## 系统瓶颈

**RAM 是天花板**：

每个 Agent 需要：
- 独立 worktree
- 独立 node_modules
- 独立 TypeScript compiler、test runner

5 个 Agent 同时运行 → 5 组并行进程 → Mac Mini 16GB 开始 swapping。

解决方案：Mac Studio M4 max 128GB RAM。

## ACP 编码专家阵型

6 种编码 Agent，最大 6 并发，120min TTL：

| Agent | 模型 | 特点 |
|-------|------|------|
| Claude Code | claude-opus-4.5 | 快速、前端强 |
| Codex | gpt-5.3-codex | 推理强、后端复杂任务 |
| Gemini | gemini-pro | 设计 sensibility |
| Pi | - | - |
| OpenCode | - | - |
| GPT-5.3-Codex | gpt-5.3-codex | 高推理 |

分析 Agent 不写代码，编码全部通过 `sessions_spawn` 委派给专家。

## 关键数据点

- Elvis 实战数据：94 commits in one day（有 3 个 client calls，没打开编辑器）、7 PRs in 30 minutes
- RAM 是天花板：5 个 Agent 同时运行 → 5 组并行进程 → Mac Mini 16GB 开始 swapping，解决方案是 Mac Studio M4 max 128GB RAM
- Definition of Done：PR created + Branch synced + CI passing + review passed + screenshots included（UI changes）
- Cron 级监控每 10 分钟运行，自动 respawn 失败 agent（max 3 attempts），只在需要人工介入时 alert
- ACP 编码专家阵型：6 种编码 Agent，最大 6 并发，120min TTL
- OpenAI multi-agent 研究提供另一种形态：用消息原语让 Agent 动态协调，把 swarm 用作并行 test-time compute（见 [[20260917-dwarkesh-noam-brown-agent-swarms-rsi]]）

## 前提与局限性

- 每个 Agent 需要独立 worktree、node_modules、TypeScript compiler、test runner，RAM 是并发瓶颈
- Agent 选择需根据任务类型：Codex 适合后端/复杂 bug，Claude Code 适合前端/Git 操作，Gemini 适合设计
- 直接用 Claude Code/Codex 的限制：一次只能盯一个事、上下文窗口是零和博弈
- Definition of Done 必须严格定义，否则 Agent 可能产出未验证的代码
- 分析和编码应分离——分析 Agent 不写代码，编码通过 ACP 委派给专业工具
- Agent Swarm 不只是并发调度系统。Agent 数量增加后，还会出现从众、责任稀释、不可见编排和内态解离等 [[Multi-Agent-System-Pathology|多 Agent 组织病理]]。
- 高 AI-AI cooperation 不等于 human alignment；协作训练可能迁移到未预期环境，因此 coordination quality 与 safety/alignment 必须分开评估。

## 关联概念

- [[Agent-Orchestration]] — 编排层调度 Agent 群体
- [[Headless-Mode]] — Agent 运行的无头模式基础
- [[Three-State-Protocol]] — Swarm 成员间通信协议
- [[Context-Engineering]] — Swarm 需要专业的上下文工程
- [[Multi-Agent-System-Pathology]] — Swarm 规模化后的组织认知风险

## 来源
