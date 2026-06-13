---
type: entity
title: "Agent 基础设施层"
aliases:
  - Agent Infra
  - Agent Infrastructure
definition: "将硅基执行者接进软件世界的运行时层，包含 Coding Agent 入口、Context/Memory/Tool Use/Sandbox/AgentOps 运行时组件，以及 Agent Builder/Orchestrator/Operator 编排层"
created: 2026-05-29
updated: 2026-05-29
tags:
  - agentic-ai
  - infrastructure
  - agent-runtime
related_entities:
  - "[[Agent-Harness]]"
  - "[[Token-Supply-Chain]]"
  - "[[Model-Context-Protocol-MCP]]"
  - "[[Context-Engineering]]"
source_raw:
  - "[[20260528-agentic-ai-2026-landscape]]"
  - "[[20260613-aliyun-agent-infra-constraint-infrastructure]]"
---

> [!definition] 定义
> 将硅基执行者接进软件世界的运行时层，包含 Coding Agent 入口、Context/Memory/Tool Use/Sandbox/AgentOps 运行时组件，以及 Agent Builder/Orchestrator/Operator 编排层。

Agent Infra 决定 AI 能替谁做事。它是 [[Agent-Harness]] 概念的生态化扩展——当单个 Harness 从服务一个开发者扩展到服务一个组织、一个行业时，就长出了 Agent Infra 这个层次。

## 多标签分类数据（226 个项目）

| 标签 | 项目数 | 参与者 |
|------|--------|--------|
| Coding Agent | 78 | 14,019 |
| Memory | 70 | 7,609 |
| Observability | 71 | 5,463 |
| MCP | 59 | 6,651 |
| Gateway | 31 | 2,637 |

## 项目自述迁移路径

226 个项目中有 96 个改过 description，沿七条典型路径向 Agent 执行栈靠拢：

1. **Workflow Builder → Agent Orchestrator** — Dify、Flowise、Langflow
2. **RAG / Data / Vector DB → Context / Memory Infra** — RAGFlow、Chroma、Letta
3. **Chatbot / AI Client → Agent Workspace / Personal Assistant** — LobeChat
4. **Dev Tool / IDE / Terminal → Agentic Dev Environment** — Warp、Daytona、Cline
5. **Framework → Agent Harness** — LangChain、deepagents、Mastra
6. **Tool Integration → Agent Control Plane** — Composio、LiteLLM
7. **RL / Inference / Training → Agent Workload Infra** — AReaL、verl、SGLang

## README 否定句信号

当项目反复说 "not a..."，意味着在摆脱上一代生态标签：

- **退潮标签**: chatbot framework、LLM wrapper、workflow builder、prompt manager
- **涌入标签**: agent runtime、harness、context、MCP、control plane

> [!quote] OpenFang README
> "Not a chatbot framework. Not a Python wrapper around an LLM. Not a multi-agent orchestrator." → 自我定位为 Agent Operating System。

## 关键数据点

- Claude Code 在 Top 100 Agentic AI 项目中覆盖率最高（81%），OpenAI Codex 69%
- Top 100 项目平均使用 2.8 种 coding agent 配置
- AGENTS.md、CLAUDE.md、.cursor/rules 成为"给 AI 的入职文档"
- 96 个 description 变化项目中，当前含 harness 的有 6 个（4 个为新增）

## 前提与局限性

- Agent Infra 的分类边界仍在快速变化，今天的标签可能很快过时
- description 变化可能包含"蹭热点"噪音，不全是真实需求驱动
- 多标签分类使用 LLM 自动标注，存在误分类风险

## 关联概念

- [[Agent-Harness]] — Agent Infra 的核心组件之一
- [[Token-Supply-Chain]] — Agent Infra 依赖的下游基础设施
- [[Model-Context-Protocol-MCP]] — Agent Infra 中的工具协议标准
- [[Context-Engineering]] — Agent Infra 中 Context/Memory 组件的理论基础
- [[CLAUDE-md]] — Agent Infra 中"给 AI 写入职文档"的具体实现
- [[Carbon-Silicon-Division]] — Agent Infra 支撑的分工模式
- [[Constraint-Infrastructure]] — Agent Infra 中治理和安全能力域的约束基建具体实现
