---
type: entity
title: AI-Native SDLC
aliases:
  - AI-Native SDLC
  - AI Native SDLC
  - AI 原生 SDLC
  - Agentic SDLC
definition: "Anthropic 官方提出的六阶段 AI 时代软件开发生命周期范式（Plan/Design/Build/Test/Deploy/Maintain），以 intent.md / spec.md / plan.md 为阶段契约，以 CLAUDE.md / Skills / Hooks / Evals 为四大基础设施；把线性 pipeline 重构为非线性的 loop，治理手段从「人 review」转为「deterministic hooks + 多层 agentic review + 人工 review 保留给受监管代码」"
created: 2026-08-22
updated: 2026-08-22
evidence_level: high
claim_type: mixed
tags:
  - software-engineering
  - lifecycle
  - anthropic-official
  - agentic-engineering
related_entities:
  - "[[Agent-Development-Lifecycle]]"
  - "[[Knowledge-Compilation]]"
  - "[[AGENTS-md]]"
  - "[[Skills-as-Products]]"
  - "[[Secure-Paved-Path]]"
  - "[[Lessons-MD-Self-Improvement]]"
  - "[[Distinct-Principal-Identity]]"
  - "[[Alert-Closed-Loop]]"
  - "[[Evals-as-PRD]]"
  - "[[Claude-Tag]]"
  - "[[Claude-Code-CLI]]"
source_raw:
  - "[[20260822-the-ai-native-sdlc-playbook]]"
  - "[[20260822-claude-code-guide-for-startups]]"
---

# AI-Native SDLC（AI 原生 SDLC）

> [!definition] 定义
> **AI-Native SDLC** 是 Anthropic 官方（Louis Claxton，2026-08-21）提出的六阶段 AI 时代软件开发生命周期范式：**Plan / Design / Build / Test / Deploy / Maintain**。它把传统线性 pipeline 重构为非线性 loop，并把每个阶段的契约产物（intent.md / spec.md / plan.md）与四大基础设施（CLAUDE.md / Skills / Hooks / Evals）显式化——治理从「人 review」转为「deterministic hooks + 多层 agentic review + 受监管代码保留人工 review」。

## 与传统 SDLC 的核心差异

| 阶段 | 传统 SDLC | AI-Native SDLC |
|------|----------|----------------|
| **Plan** | 需求由委员会收集，通过 workshops 和 sign-off 提炼 | Claude 合成痛点并写入 `intent.md` |
| **Design** | 分析师写 spec，设计师解析 | 需求和设计坍缩为一次与 agent 的 session，产出 `spec.md` |
| **Build** | 测试和代码手写 | AI 生成测试和代码，配版本化 `CLAUDE.md` 和 skills |
| **Test** | QA 在阶段边界设门禁 | 持续 evals 织入实现过程 |
| **Deploy** | 人类逐行 review | 多层 agentic review，受监管代码保留人工 review |
| **Maintain** | 人类监控生产 bug | Agent 监控生产部署，把破线的控制回写为 `intent.md` |

**核心命题**：当 code 不再是瓶颈，瓶颈左移到 build 阶段**前后**——Plan、review/test、deploy。AI-native SDLC 的目标不是「让 AI 写更多代码」，而是**重新组织六阶段的契约产物与治理手段**。

## 三大契约产物（Plan / Design / Build 阶段）

### `intent.md` — AI-native SDLC 的第一公民

发起人用自己语言写成的「原型 spec」，作为后续所有阶段的 source of truth。结构：

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

三段式：**Problem / Proposed Outcome / Constraints**。意图的捕获在 Plan 阶段一次性完成，避免后续阶段重新发明需求。

### `spec.md` — Design 阶段产物

由 product owner 与 Claude 协作产出，叠加组织 skills（brand / security / compliance / UX）。spec.md 与 intent.md 配套提交。

### `plan.md` — Build 阶段产物

工程师在 Claude Code plan mode 中迭代生成。计划必须足够清晰——「工程师仅凭 plan 就能实现改动」是验收门槛。

## 四大基础设施

### CLAUDE.md — 新人 context

子目录化的 `CLAUDE.md` 沉淀约定、命令、架构、常见错误。已是知识库既有 entity，详见 [[AGENTS-md]]。

### Skills — 机构知识的版本化

Skills 是「explicit、版本化、广泛使用、集中更新」的机构知识单元。governance 视角详见 [[Skills-as-Products]]。

### Hooks — Build-time 硬门禁

确定性 script 在 Claude 行动前/后跑，可做：
- 阻止编辑受保护路径
- 文件编辑后跑 formatter 和 linter
- 把 credentials 挡在 diff 之外

### Evals — AI-native 的 stage-gate QA

20-50 真实任务写为 eval（prompt + checks），CI 按 schedule 非交互跑，配置变更门禁，每个 production incident 都产出一个 eval。

## Maintain 阶段：闭环回到 Plan

确定性 script 监控生产，控制带破线时调用 Claude。响应 tier 在版本化 config 中定义：

| 偏离度 | 响应 |
|--------|------|
| **1σ** | 只 log |
| **2σ** | 只读模式调用 Claude 诊断 |
| **3σ** | Claude 可以行动 |

每个事故 → 写回 `intent.md`（loop 闭合），形成 Lessons → Spec 反哺机制。

## 关键数据点

- **发布方**：Anthropic 官方（Louis Claxton），2026-08-21
- **六阶段**：Plan / Design / Build / Test / Deploy / Maintain
- **三大契约产物**：`intent.md`（Plan 阶段，发起人原话）/ `spec.md`（Design 阶段，含组织 skills）/ `plan.md`（Build 阶段，工程师可凭此实现）
- **四大基础设施**：CLAUDE.md（context）+ Skills（机构知识）+ Hooks（硬门禁）+ Evals（stage-gate QA）
- **Maintain 阶段分级响应**：1σ log / 2σ 只读诊断 / 3σ Claude 可行动
- **Evals 任务量**：20-50 真实任务，每 production incident 产出一个 eval
- **配套工具**：Claude Code（Build 阶段）、Claude Tag（Maintain 阶段，Slack 频道成员）、OpenTelemetry monitoring

## 与 [[Agent-Development-Lifecycle|ADLC]] 的关系

| 维度 | ADLC（Cloudflare 2026-08） | AI-Native SDLC（Anthropic 2026-08） |
|------|---------------------------|-------------------------------------|
| **核心命题** | SDLC 是软件团队用的；ADLC 是软件工厂用的 | Code 不再是瓶颈，重新组织六阶段契约 |
| **Agent 覆盖范围** | 全生命周期（含 generate + 决策） | 全生命周期（六阶段全栈） |
| **阶段契约产物** | 未具体化 | intent.md / spec.md / plan.md 显式化 |
| **治理机制** | Workflow 取代 CI/CD | CLAUDE.md / Skills / Hooks / Evals |
| **代表实施** | Cloudflare 自家工程实践 | Anthropic 官方 playbook + 14+ startup 实证 |

两者互为补充：ADLC 是范式命题，AI-Native SDLC 是落地 playbook。

## 前提与局限性

- **「intent.md 作为 source of truth」依赖发起人的语言表达能力**——如果发起人不能用 AI 清晰表达问题，intent.md 会成为系统性噪声的源头
- **「Hooks 作为硬门禁」只能解决 syntactic concerns**——语义级约束（架构原则、领域模型）仍需多层 agentic review + 人工 review
- **「Continuous evals」依赖真实任务的样本代表性**——20-50 任务的采样方法、时间窗口、多样性保证如果不严谨，evals 会成为 Goodhart target
- **「Maintain → 写回 intent.md」的 loop 触发条件未明示**——什么样的事件触发回到 Plan？事故、模型升级、用户反馈、季度 review？

## 关联概念

- [[Agent-Development-Lifecycle|ADLC]] — Cloudflare 的对应范式命题，互为补充
- [[Knowledge-Compilation]] — intent.md → spec.md → plan.md 三步编译链
- [[AGENTS-md|AGENTS.md / CLAUDE.md]] — 四大基础设施之一
- [[Skills-as-Products]] — Skills 的 governance 视角
- [[Secure-Paved-Path|安全铺装路径]] — Hooks 的安全哲学基础
- [[Lessons-MD-Self-Improvement|Lessons-MD 自我改进]] — Maintain 闭环反哺
- [[Distinct-Principal-Identity|独立主体身份]] — Claude Tag 在 Slack 频道的身份
- [[Alert-Closed-Loop|告警闭环]] — 1σ/2σ/3σ 分级响应
- [[Claude-Tag]] — Maintain 阶段的代表 agent
- [[Claude-Code-CLI]] — Build 阶段的核心工具
- [[Evals-as-PRD|评测即需求文档]] — evals 的更高地位
- [[Sample-Efficiency]] — evals 采样方法论
