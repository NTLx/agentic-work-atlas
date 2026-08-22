---
type: raw
source: "https://claude.com/blog/the-ai-native-sdlc-playbook"
author:
  - "Louis Claxton"
published: "2026-08-21"
created: "2026-08-22"
description: "Anthropic 官方 AI-Native SDLC Playbook——以 intent.md / spec.md / plan.md / CLAUDE.md / Skills / Hooks / Evals 重新组织软件开发六阶段（Plan / Design / Build / Test / Deploy / Maintain），把线性流程改成闭环 loop。"
tags:
  - clippings
  - ai-native-sdlc
  - claude-code
  - adlc
  - anthropic-official
---

# The AI-Native SDLC Playbook

> 来源：claude.com/blog，Louis Claxton，2026-08-21，5 min 阅读。Anthropic 官方 AI-Native SDLC Playbook——重新组织软件开发六阶段。

## Code is no longer the bottleneck

组织已开始用 AI 以一年前不可想象的速率写代码，但代码周围的流程没有同步变化。

很多工程团队仍维持同样的审批门禁、评审、交接、政策，使 agentic coding 解决方案（如 Claude Code）的生产力提升停滞。

SDLC 是把软件从想法带到生产的过程。大多数组织跑同一套六个阶段：plan / design / build / test / deploy / maintain。传统上每个阶段是离散 phase，由不同角色所有。

### 代码不再是瓶颈时的关键变化

- 瓶颈左移到 build 阶段**前后**（plan、review/test、deploy）
- 控制不再匹配现实，变得难处理
- 治理成本上升，因为例外仍走会议和委员会

## 什么是 AI-native SDLC？

AI-native SDLC 是重新构想的过程——把旧的**控制目标**与新的**强制手段**结合。流程从线性变成 loop，AI 嵌入每个点。

### 传统 vs AI-Native SDLC 对比

| 阶段 | 传统 SDLC | AI-Native SDLC |
|------|----------|----------------|
| **Plan** | 需求由委员会收集，通过 workshops 和 sign-off 提炼 | Claude 合成痛点并写入 `intent.md` |
| **Design** | 分析师写 spec，设计师解析 | 需求和设计被压进一次与 agent 的工作 session |
| **Build** | 测试和代码手写 | AI 生成测试和代码，配版本化的 `CLAUDE.md` 和 skills |
| **Test** | QA 在阶段边界设门禁 | 持续 evals 织入实现过程 |
| **Deploy** | 人类逐行 review | 多层 agentic review，受监管代码保留人类 review |
| **Maintain** | 人类监控生产的 bug | Agent 监控生产部署，把破线的控制回写为 `intent.md` |

## Plays 总览

六个非线性阶段：Plan / Design / Build / Test / Deploy / Maintain。

每个 play 涵盖：
- What changes
- Getting started
- 实施的具体步骤
- 治理考量
- 如何衡量是否奏效

## Stage 1: Plan

想法不再需要等人写下来。Intent 用发起人自己的语言被一次性捕获，作为下一阶段可操作的版本化产物。

### Capture as intent.md

`intent.md` 启动软件开发流程。发起人与 Claude 头脑风暴并产出 markdown 原型 spec。原 spec 保存为 `intent.md`。

- **传统**：想法经 backlog 条目、user story、story points、refinement meetings
- **AI-native**：发起人与 Claude 头脑风暴，用发起人自己的话写成 `intent.md`

### 执行步骤

1. 发起人用自己的话向 Claude 描述问题
2. 头脑风暴直到想法具体化
3. 让 Claude 按组织模板写成 `intent.md`
4. 发起人修正 Claude 误解的地方
5. 把 `intent.md` 提交到共享库

### 示例 intent.md

```markdown
# Intent: claims status self-service
Author: J. Ortiz (claims operations). Status: draft.

## Problem
Customers phone the contact center to ask where their claim is.

## Proposed outcome
Customers see claim status, next step and expected date in the portal.

## Constraints
No new PII in the portal session. Existing authentication only.
```

## Stage 2: Design

需求和设计坍缩为一个 session。Policy 在写 spec 时应用，而不是几周后的 review 中发现。

### Requirements and design

Claude 接收被接受的 `intent.md` 并产出 requirements 和 design spec。这由组织的 skills（brand、security、compliance、UX）指导。

**执行步骤**：
1. Product owner 打开一个 session，挂上可用的组织 skills 和 `intent.md`
2. 提示指向 `intent.md`，列出 constraints，要求 flagged concerns
3. 对照原始想法 review spec
4. 先处理 flagged concerns
5. 提交 `spec.md` 紧邻 `intent.md`

## Stage 3: Build

没有可接受的 plan 就不实现。机构知识变成 agent 读取的文件。

### Claude Code plan mode 作为默认起点

工程师在 plan mode 中启动 Claude Code session，给 Claude 批准的 `spec.md`，让 Claude 面试他们，迭代 plan。

**执行步骤**：
1. 工程师在 plan mode 启动 session
2. 把 `intent.md` 和 `spec.md` 给 Claude
3. 通过问「这次改动可能破坏什么」质询 plan
4. 迭代到工程师仅凭 plan 就能实现改动
5. 把批准的 plan 提交为 `plan.md`
6. 接受 plan 并让 Claude 实现

### The CLAUDE.md

`CLAUDE.md` 给 Claude 一个新员工需要的 context——约定、命令、架构、常见错误。

### Skills as institutional knowledge

Skills 是组织让机构知识可操作的方式。它们是 explicit、版本化的、广泛应用的、集中更新的。

### Hooks as build-time guardrails

Build 阶段的 hooks 可以：
- 阻止编辑受保护路径
- 文件编辑后运行 formatter 和 linter
- 把 credentials 挡在 diff 之外

### Parallel sessions and subagents

一个工程师可以同时驱动多个工作流。**Parallel session** 是另一个完整的 Claude Code 实例，在独立的 git worktree 中工作独立任务。**Subagent** 在单个 session 内作为 scoped helper 运行。

### Give Claude a feedback loop

始终给 Claude 验证自己工作的方式——无论是 tests、build、还是 screenshot diff。

### Continuous evals in CI

Evals 是 AI-native 等价的 stage-gate QA。agent 的配置改变时套件就跑。

## Stage 4: Test

agent 配置改变时 evals 跑。换新模型或重写 prompt 时，eval 套件告诉你 agent 是否仍以同等标准工作。

### Continuous evals in CI

1. 平台工程师从最近工作收集 20–50 个真实任务
2. 把每个任务写成 eval（prompt + checks）
3. 套件在 CI 中按 schedule 非交互运行
4. 用结果作为配置变更的门禁
5. 每个生产事故都产出一个 eval

## Stage 5: Deploy

Review 双向运行，治理在 agent 行动时被强制。

### AI in the PR review loop

Claude 既给出也接收 review。它对照组织 policies 审 incoming PR，并处理自己 PR 上的 review comments。

### Hooks as approval gates

Hook 可以暂停动作直到特定人批准。平台工程师把每个门禁表达为 hook——一个在 Claude 行动前跑的脚本。

### CI/CD integration and deployment

在 CI/CD 管线里以非交互模式跑 Claude Code，sandbox 执行，通过 MCP 集成暴露部署。

## Stage 6: Maintain

闭环合上。触发器调用 Claude，调用链中没有人。

### Closing the loop

deterministic script 监控生产，控制带破线时调用 Claude。响应 tier 在版本化 config 中定义：1σ 时只 log；2σ 时以只读模式调用 Claude 诊断；3σ 时 Claude 可以行动。

### Claude on call with Claude Tag

事故也可以通过 Slack 或 Teams 等工作沟通应用到达。Claude Tag 让 Claude 以自己的身份成为这些频道的成员。

## Closing thoughts

模型和 harness 变得更强，让组织不仅能改造生产代码的方式，而是改造整个软件开发生命周期。

> 「The loop keeps running. Human judgement stays above it.」

## Resources and Documentation

- Set up Claude Code for your organization
- Settings reference and precedence
- Server-managed settings
- Permissions
- Sandboxing
- Hooks guide
- Skills
- Plugins and private marketplaces
- Managed MCP
- Enterprise deployment overview
- Monitoring (OpenTelemetry)
- Compliance API
- Security model

## 相关链接

- Self-service data analytics in Slack: how Anthropic deploys Claude Tag（2026-08-13）
- The new rules of context engineering for Claude 5 generation models（2026-07-24）
- The Claude Code guide for startups（2026-08-20）
- Build production agents with computer use, the Skills API, and the Files API（2026-08-20）
