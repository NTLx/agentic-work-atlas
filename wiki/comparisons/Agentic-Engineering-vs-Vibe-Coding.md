---
type: comparison
title: "Agentic Engineering vs Vibe Coding"
entity_a: "[[Agentic-Engineering]]"
entity_b: "[[Vibe-Coding]]"
created: 2026-05-24
updated: 2026-05-24
tags:
  - comparison
  - AI-Agent
  - Software-Engineering
related_entities:
  - "[[Agentic-Engineering]]"
  - "[[Vibe-Coding]]"
  - "[[Verifiability]]"
  - "[[Agent-Harness]]"
  - "[[Agent-PR-Review]]"
  - "[[Essential-Complexity]]"
  - "[[Friction-as-Design-Signal]]"
source_raw:
  - "[[Andrej Karpathy: From Vibe Coding to Agentic Engineering]]"
  - "[[What is agentic engineering? - Agentic Engineering Patterns]]"
  - "[[Why I Don’t Vibe Code]]"
  - "[[Improving token efficiency in GitHub Agentic Workflows]]"
---

# Agentic Engineering vs Vibe Coding

> [!summary] 对比概述
> Vibe Coding 抬高软件创造的能力底线，让人可以用自然语言、运行反馈和直觉快速做出原型；Agentic Engineering 则保留这种速度，但把代码放回测试、审查、可验证性、成本观测和责任承担的工程系统中。

## 核心维度对比

| 维度 | Vibe Coding | Agentic Engineering |
|------|-------------|---------------------|
| 核心目标 | 快速把想法变成可运行原型 | 用 coding agents 交付可维护、可验证的软件 |
| 质量层级 | 原型级、未经审查 | 生产级、需要证据 |
| 人类角色 | 用提示、运行和复制粘贴驱动结果 | 设定目标、设计验证、审查取舍、承担后果 |
| 验证方式 | 凭感觉、看起来能跑 | 测试、linter、类型检查、运行截图、审查证据 |
| 适用场景 | 个人实验、一次性脚本、低风险探索 | 团队协作、长期系统、安全敏感或客户可见软件 |
| 风险来源 | 代码膨胀、抽象失控、死代码、责任空洞 | harness 复杂度、token 成本、错误验证信号、过度自动化 |
| 核心约束 | 不要把它误称为生产工程 | 不要把生成成本下降转嫁为 review 成本 |

## 本质区别

Vibe Coding 是一种**探索模式**。它的价值在于降低从想法到原型的摩擦，让非专业开发者和专业工程师都能更快试错。它的关键特征不是“用了 AI 写代码”，而是人类有意降低对代码细节的关注，把重点放在交互反馈和结果感觉上。

Agentic Engineering 是一种**交付模式**。它把 coding agent 视为能运行工具循环的工程参与者，但不把模型输出当作完成。完成标准从“代码生成了”转为“结果被验证、变更可审查、系统仍可维护”。

> [!warning] 术语边界
> 不应把所有 LLM 生成代码都叫 Vibe Coding。Vibe Coding 指向未经审查、原型质量的生成代码；Agentic Engineering 指向被测试、审查和治理后的软件工程实践。

## 分工关系

两者不是简单的高低之分，而是位于不同阶段。

| 阶段 | 更适合的模式 | 原因 |
|------|--------------|------|
| 想法探索 | Vibe Coding | 快速形成可交互样品，降低试错成本 |
| 方案筛选 | Vibe Coding + 人类判断 | 通过多个原型比较方向，但不能直接进入生产 |
| 工程化 | Agentic Engineering | 加入测试、结构、边界、评审和交付证据 |
| 长期维护 | Agentic Engineering | 需要可复现验证、可读历史、成本观测和责任链 |

这意味着一个健康流程可以先使用 Vibe Coding 发现方向，再通过 Agentic Engineering 把方向变成可承担后果的软件。危险做法是把原型阶段的低摩擦误认为交付阶段的低风险。

## 可验证性是分水岭

[[Verifiability|可验证性]]解释了为什么代码是 agent 能力增长最快的领域：代码可以运行，测试可以判断，错误可以反馈给模型继续修正。

Vibe Coding 往往只使用最低限度的运行反馈：“它大概能跑”。Agentic Engineering 则把验证反馈系统化：

- 测试和类型检查提供确定性反馈。
- Git diff、PR 描述和变更范围让人类能审查。
- token usage artifact、日志和工具调用记录让成本可观测。
- Playwright 截图、lint、Semgrep、dependency-cruiser 等 sensor 让 agent 的行为进入工程仪表盘。

因此，Agentic Engineering 的关键不是“让 agent 多写代码”，而是“让 agent 在可观察边界内迭代”。

## 人类责任没有消失

Vibe Coding 容易制造一种错觉：如果代码来自模型，人类就只是操作者。但在真实软件系统中，故障、隐私、性能、可访问性和维护成本都不会由模型承担。

Agentic Engineering 重新定义人类责任：

- 人类不一定亲手写每行代码，但必须能说明为什么这是正确问题。
- 人类不一定亲手跑每个命令，但必须定义什么证据足以证明完成。
- 人类不一定亲手修每个 bug，但必须决定哪些摩擦是设计信号，不能被自动化抹掉。
- 人类不一定拒绝 AI 生成，但必须拒绝未经审查的合并。

这也是 [[Ownership|Ownership]] 与 [[Agent-PR-Review|Agent PR Review]] 进入工程流程的原因：AI 降低生产摩擦，但不会替代责任承担。

## 反模式

### 把 Vibe Coding 当成生产级交付

最常见的失败模式是：原型看起来能跑，于是直接进入团队仓库或客户系统。短期速度来自未支付的审查成本，长期会表现为代码膨胀、抽象混乱、测试缺失和责任不清。

### 把 Agentic Engineering 做成形式主义

另一种失败模式是：虽然加了 agent、CI、测试和 PR 模板，但人类不再理解变更。此时工具链只是把 Vibe Coding 包装得更正式，并没有真正提高质量。

### 消除所有摩擦

[[Why I Don’t Vibe Code]] 提供的反向提醒是：并非所有摩擦都该被移除。阅读陌生代码、写 ADR、暂停实现和重新审视边界，常常是在处理 [[Essential-Complexity|本质复杂性]]。如果 agent 把这些全部视为低效，就会更快地产生错误抽象。

## 选择指南

选择 Vibe Coding，当：

- 失败成本低。
- 目标是探索想法，而非稳定交付。
- 代码可以被丢弃或重写。
- 使用者明确知道这是原型，不是生产系统。

选择 Agentic Engineering，当：

- 代码会进入团队协作、客户交付或长期维护。
- 需要测试、审查、运行证据和可复现行为。
- 变更会影响安全、隐私、成本、可访问性或业务流程。
- 你需要降低生产成本，同时不降低质量上限。

## 相关概念

- [[Agentic-Engineering]] — 用 coding agents 辅助开发软件，并保持生产级质量上限的工程实践。
- [[Vibe-Coding]] — Software 3.0 的普及化原型实践。
- [[Verifiability]] — Agentic Engineering 能成立的关键条件。
- [[Agent-Harness]] — 让 agent 行为可执行、可观察、可治理的运行环境。
- [[Agent-PR-Review]] — Agent 生成代码进入协作系统时的证据门槛。
- [[Friction-as-Design-Signal]] — 提醒工程流程不要把所有阻力都自动化掉。
