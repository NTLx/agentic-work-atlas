---
type: comparison
title: "Agent Harness vs Agent Workflow Patterns"
entity_a: "[[Agent-Harness]]"
entity_b: "[[Agent-Workflow-Patterns]]"
created: 2026-05-24
updated: 2026-05-24
tags:
  - comparison
  - AI-Agent
  - agent-engineering
related_entities:
  - "[[Agent-Harness]]"
  - "[[Agent-Workflow-Patterns]]"
  - "[[Building-Effective-Agents]]"
  - "[[ACI-Agent-Computer-Interface]]"
  - "[[Verifiability]]"
  - "[[Agent-Orchestration]]"
  - "[[Bias-to-Action-LLM]]"
source_raw:
  - "[[building-effective-agents]]"
  - "[[The Anatomy of an Agent Harness]]"
  - "[[Validating agentic behavior when “correct” isn’t deterministic]]"
---

# Agent Harness vs Agent Workflow Patterns

> [!summary] 对比概述
> Agent Workflow Patterns 是组织 LLM 与工具调用的编排模式；Agent Harness 是让这些模式在生产环境中可执行、可观察、可验证、可恢复的运行时系统。前者回答“流程怎么走”，后者回答“系统如何承受真实运行”。

## 核心维度对比

| 维度 | Agent Harness | Agent Workflow Patterns |
|------|---------------|-------------------------|
| 核心问题 | 如何让 Agent 在生产环境可靠运行 | 如何组织 LLM、工具和中间步骤 |
| 层级 | 运行时基础设施 | 架构与编排模式 |
| 典型组成 | 工具权限、状态、日志、上下文、验证、恢复、审计 | Prompt chaining、routing、parallelization、orchestrator-workers、evaluator-optimizer |
| 成功标准 | 行为可观察、错误可恢复、权限可控、结果可验证 | 任务被合理拆分，模型调用路径有效 |
| 主要风险 | 运行时过重、隐藏复杂性、错误信任自动化 | 模式选择错误、过度 agent 化、缺少治理 |
| 与生产的距离 | 直接面对生产约束 | 仍需 harness 承接 |
| 人类角色 | 定义边界、审批、审查证据、处理升级 | 选择模式、设计任务拆解、评估结果 |

## 本质区别

Agent Workflow Patterns 是**怎么编排**。它关注任务如何拆成多个模型调用和工具步骤：先链式处理，还是路由到不同专家，还是并行生成候选，再由 evaluator 优化。

Agent Harness 是**怎么运行**。它关注 Agent 真正进入系统后需要什么边界：能调用哪些工具、能读写哪些文件、状态如何保存、失败如何恢复、成本如何记录、什么时候必须拒绝或转人工。

如果没有 workflow patterns，Agent 可能只是一轮 prompt。  
如果没有 harness，workflow patterns 只能停留在 demo。

## 从模式到运行时

[[Building-Effective-Agents]] 中的模式适合回答“这类任务需要多复杂的流程”。但一旦系统进入真实使用，就会出现模式本身不处理的问题：

- 工具权限如何限制？
- 中间状态如何保存？
- 失败后能否 replay？
- 上下文是否过期？
- 输出是否通过验证？
- token 成本是否可观测？
- 高风险动作是否需要审批？

这些问题属于 [[Agent-Harness|Agent Harness]]，不是单个 workflow pattern 能解决的。

## 何时只是 Workflow，何时需要 Harness

| 场景 | 更接近 Workflow Pattern | 更需要 Agent Harness |
|------|-------------------------|----------------------|
| 一次性文档改写 | 是 | 否 |
| 简单客服分类 | 是 | 视权限而定 |
| 自动修改代码并开 PR | 否 | 是 |
| 多 Agent 长程协作 | 否 | 是 |
| 读取敏感数据后执行动作 | 否 | 是 |
| 低风险内容生成流水线 | 是 | 轻量 harness 即可 |

判断标准不是“有没有 Agent”，而是系统是否需要承受权限、状态、验证、恢复和责任链。

## 反模式

### 把模式图当生产架构

画出 orchestrator-workers 不等于系统可运行。没有状态管理、日志、权限、验证和恢复机制，模式图只是控制流草图。

### 为简单任务上重 Harness

不是所有任务都需要完整 Agent Harness。低风险、短链路、可人工检查的任务，用简单 workflow 可能更稳。

### 用 Harness 掩盖任务不适合 Agent

如果任务本身规则明确、输入输出稳定、确定性代码能完成，就不应为了“Agent 化”而引入模型循环。Harness 不能把不该交给 LLM 的工作变成好选择。

## 选择指南

优先思考 Workflow Patterns，当：

- 任务仍处在原型阶段。
- 主要问题是如何拆分模型调用。
- 风险低，状态短，失败可接受。
- 人类可以快速检查最终输出。

优先建设 Agent Harness，当：

- Agent 会写入系统、修改代码、调用生产工具或处理敏感信息。
- 任务持续运行、可重复触发或跨多步状态。
- 需要审计、replay、成本记录、权限控制和拒绝机制。
- 多个 Agent 或多个工具之间存在协调风险。

## 相关概念

- [[Agent-Harness]] — 包装 LLM 的生产级软件基础设施。
- [[Agent-Workflow-Patterns]] — 构建 Agentic 系统的模式集合。
- [[Building-Effective-Agents]] — Anthropic 的 Agent 构建原则与模式。
- [[ACI-Agent-Computer-Interface]] — 为 Agent 设计可操作接口。
- [[Verifiability]] — 判断 Agent 输出能否自动验证的关键维度。
- [[Bias-to-Action-LLM]] — Harness 需要约束的模型行动偏差。

