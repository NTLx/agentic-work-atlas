---
type: entity
title: "Agent 基础设施层"
aliases:
  - Agent Infra
  - Agent Infrastructure
definition: "将硅基执行者接进软件世界的运行时层，包含 Coding Agent 入口、Context/Memory/Tool Use/Sandbox/AgentOps 运行时组件，以及 Agent Builder/Orchestrator/Operator 编排层"
created: 2026-05-29
updated: 2026-09-13
evidence_level: medium
claim_type: mixed
tags:
  - agentic-ai
  - infrastructure
  - agent-infra
related_entities:
  - "[[Agent-Harness]]"
  - "[[Token-Supply-Chain]]"
  - "[[Model-Context-Protocol-MCP]]"
  - "[[Context-Engineering]]"
  - "[[Agentic-Speculation]]"
  - "[[Structured-Agent-Memory]]"
source_raw:
  - "[[20260528-agentic-ai-2026-landscape]]"
  - "[[20260613-aliyun-agent-infra-constraint-infrastructure]]"
  - "[[20260617-huggingface-agentic-resource-discovery]]"
  - "[[20260707-intelligence-is-free-data-systems-for-of-by-agents]]"
  - "[[20260911-openai-habitat-storage-scaling]]"
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

## 从组件库到平台控制面：Habitat（2026-09）

OpenAI 的 Habitat 提供了 Agent Infra 从“可复用组件”长成“组织级平台”的一个工程样本。它先以 Python client library 隐藏 Cosmos DB 的细节，随着产品和服务数量增加，再迁移为独立 service，把部署、路由、访问控制、审计、数据安全、可观测性和容量管理集中到一个控制点。

Habitat 的受限 NoSQL object/edge API 把在线请求约束为可预测的工作量；复杂查询通过 CDC 输出到各团队隔离的 Rockset 视图，保留扩展出口但不把不可控查询放进共享热路径。服务层还用 loop delay、profiling、连接池实验和 Envoy/Istio 处理尾延迟与网络反馈。Q2 2026 的 Rust 重写说明 Agent 可以降低基础设施迁移的实现成本，但平台边界、验证指标和流量切换仍是人的工程判断。

> **判断（综合判断）**：Agent Infra 的价值不只是提供更多工具，而是把调用者与共享状态之间的危险自由度压缩成可审计、可观测、可隔离的接口；平台通过“默认少做、例外另走”获得规模。
>
> **证据**：Habitat 的服务化、受限 API、CDC→Rockset 逃生舱与 Python→Rust 迁移（见 [[20260911-openai-habitat-storage-scaling]]）。
>
> **边界**：Habitat 是单一组织的第一方案例；其规模数据、性能收益和服务化选择不能直接外推到所有 Agent 基础设施。

## 关键数据点

- Claude Code 在 Top 100 Agentic AI 项目中覆盖率最高（81%），OpenAI Codex 69%
- Top 100 项目平均使用 2.8 种 coding agent 配置
- AGENTS.md、CLAUDE.md、.cursor/rules 成为"给 AI 的入职文档"
- 96 个 description 变化项目中，当前含 harness 的有 6 个（4 个为新增）
- **MCP 已成事实标准（2026-07）**：OpenAI/Google/Microsoft 全部采纳；10,000+ 公开服务器；SDK 月下载 9,700 万次；41% 高级软件负责人生产使用；Linux 基金会治理（Agentic AI Foundation）；MCP 2026-07-28 RC 实现无状态核心。来源：07-09 深度思考（联网验证）

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
- [[Agentic-Speculation]] — Agent 与数据系统交互的模式，要求数据系统作为 infra 新组件
- [[Structured-Agent-Memory]] — 多属性结构化记忆，Agent Infra 中 Memory 组件的演化方向
