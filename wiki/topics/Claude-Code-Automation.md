---
type: topic
title: Claude Code Automation
created: 2026-04-09
updated: 2026-06-15
evidence_level: medium
claim_type: mixed
tags:
  - Claude-Code
  - Automation
  - OpenClaw
related_entities:
  - '[[Agent-Orchestration]]'
  - '[[Claude-Code-CLI]]'
  - '[[OpenClaw-Agent-System]]'
  - '[[Agent-Swarm]]'
  - "[[Agent-Loops]]"
source_raw:
  - '[[OpenClaw + CodexClaudeCode Agent Swarm The One-Person Dev Team Full Setup]]'
  - '[[OpenClaw + 6 个 Agent 运转半个月，从聊天到干活的完整工程实践]]'
  - "[[Anthropic's Boris Cherny: Why Coding Is Solved, and What Comes Next]]"
---

# Claude Code Automation

> [!summary] 概要
> Claude Code 自动化不是单纯把 `claude -p` 包成脚本，而是把 Claude Code 放进更大的编排系统：由 OpenClaw/Zoe 分配任务、注入业务上下文、创建隔离工作区、监控 PR 与 CI，并在结果达到验收标准后再通知人类合并。

## 核心架构

从 Elvis Sun 的 OpenClaw 实践看，Claude Code 自动化依赖四个支柱：

```
┌─────────────────────────────────────────────────────────────┐
│              Claude Code 自动化调用架构                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  业务上下文层：Obsidian / 客户记录 / 历史决策                │
│        ↓                                                    │
│  编排层：Zoe 写 prompt、选 agent、监控进展、重试修正         │
│        ↓                                                    │
│  执行层：worktree + tmux session + Claude Code / Codex       │
│        ↓                                                    │
│  验收层：CI、AI review、截图、人工合并                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## 三个关键判断

### 1. 自动化重点不是调用，而是上下文分工

原文的核心判断是：OpenClaw 和 Claude Code 不应该装进同一个上下文窗口。

| 层级 | 放什么上下文 | 负责什么 |
|------|--------------|----------|
| OpenClaw / Zoe | 客户历史、会议记录、业务决策、失败经验 | 任务选择、prompt 编写、路由、重试 |
| Claude Code | 代码库、任务说明、测试反馈 | 具体编码、修复、提交 PR |

这种分工避免把业务记忆和代码细节塞进同一窗口。编排层保持高层策略，Claude Code 保持代码焦点。

### 2. tmux 比一次性 headless 更适合长任务

Elvis 早期用过 `claude -p` 和 `codex exec`，后来转向 tmux。理由不是 headless 不能用，而是长任务需要中途重定向：

```bash
tmux send-keys -t codex-templates "Stop. Focus on the API layer first, not the UI." Enter
```

关键不是“驱动 TUI”，而是给每个 agent 一个可恢复、可观察、可干预的运行槽位。

### 3. 完成定义必须外置

自动化的目标不是“生成代码”，而是让 PR 达到可合并状态。原文中的 Definition of Done 包括：

- PR 已创建。
- 分支已同步主干，无冲突。
- CI 通过：lint、类型检查、单元测试、E2E。
- Codex、Claude Code、Gemini 等 reviewer 给出结果。
- UI 改动附截图。

这说明 Claude Code 自动化必须配套确定性的外部检查。没有 CI、review 和截图，自动化只会把未验证代码更快地推到人面前。

## OpenClaw 闭环

英文 setup 文章给出的闭环是：

```
客户请求或系统错误
  ↓
Zoe 结合 Obsidian 业务上下文做 scoping
  ↓
创建 worktree + tmux session
  ↓
Claude Code / Codex 执行编码任务
  ↓
PR + CI + 多模型 review + 截图
  ↓
Telegram 通知人类做最后合并判断
  ↓
合并后清理 worktree 和任务注册表
```

中文半个月实践补充了另一层：不要让分析 Agent 直接编码。分析 Agent 负责判断、调研和任务拆解，编码通过 ACP 委派给 Claude Code、Codex、Gemini 等专业工具。

## Agent Loops：时间驱动的后台自动化

[[Agent-Loops]] 补上 Claude Code 自动化的时间维度。OpenClaw 式编排解决“来了一个任务，如何派给 coding agent 并验收”；Agent Loops 解决“某类状态是否应该持续被检查、修复和汇总”。

典型 loop 包括 PR 看护、CI 修复、flaky test 维护、定期抓取用户反馈并聚类。它把 Claude Code 从一次性执行器推进到后台维护者，但也要求更严格的权限、预算、日志和外部验收。没有这些护栏，循环调度会把小错误变成持续污染。

## 可复用模式

| 模式 | 价值 | 风险 |
|------|------|------|
| Worktree 隔离 | 多 agent 并发时避免互相污染 | 需要自动清理 |
| tmux session | 长任务可观察、可恢复、可中途干预 | 需要状态登记 |
| JSON registry | 让监控脚本低成本检查任务状态 | schema 变动会影响自动化 |
| CI + reviewer | 把“完成”从 agent 自述改成外部验收 | reviewer 仍可能误报 |
| 截图要求 | UI 改动可快速人工判断 | 只覆盖视觉层，不覆盖业务正确性 |

## 适用边界

Claude Code 自动化适合：

- 小到中等范围、验收标准清晰的任务。
- 可通过 CI、测试、截图或 reviewer 外部验证的改动。
- 已经有业务上下文和历史决策可供编排层调用的项目。

不适合：

- 没有明确完成标准的探索性产品判断。
- 需要大规模架构方向取舍、但缺少人类审查的改动。
- 直接把客户数据、生产权限和代码执行权限混在同一个 coding agent 里。

## 结论

Claude Code 自动化的核心不是某个 CLI 参数，而是把 coding agent 嵌入一个可观察、可恢复、可验证的系统。

单独的 Claude Code 是执行器。OpenClaw/Zoe 式编排层让它成为流水线中的工程师。

## 相关 Entity

- [[Claude-Code-CLI]] - Claude Code CLI 工具定义
- [[Agent-Orchestration]] - 编排层架构
- [[OpenClaw-Agent-System]] - OpenClaw 系统主题
- [[Agent-Loops]] - 时间驱动的后台 Agent 自动化
