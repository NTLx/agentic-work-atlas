---
type: entity
title: Agent-Native
aliases:
  - Agent-Native
  - Agent 原生
definition: "为 AI agent 而非人类设计的基础设施、文档、流程和交互界面——将系统分解为传感器（sensors）和执行器（actuators），让 agent 可以直接理解和操作"
created: 2026-05-08
updated: 2026-10-09
tags:
  - AI
  - agent
  - infrastructure
  - software-architecture
related_entities:
  - "[[Software-3.0]]"
  - "[[Agentic-Engineering]]"
  - "[[Agent-First-Enterprise]]"
  - "[[Andrej-Karpathy]]"
  - "[[Model-Context-Protocol-MCP]]"
  - "[[Lehrwerkstatt]]"
source_raw:
  - "[[Andrej Karpathy: From Vibe Coding to Agentic Engineering]]"
  - "[[Building an MCP Ecosystem at Pinterest]]"
  - "[[Learning on the Shop floor]]"
  - "[[20261004-lenny-openai-head-chatgpt-new-era]]"
evidence_level: high
claim_type: mixed
---

# Agent-Native（Agent 原生）

> [!definition] 定义
> **Agent-Native** 是 Andrej Karpathy 在 Sequoia AI Ascent 2026 上提出的概念：当前一切基础设施——文档、API、部署平台、DNS 配置——都是为人类阅读和操作设计的。Agent-Native 要求将这些系统重构为 agent 可直接消费和操作的形态，分解为传感器（sensors，感知世界）和执行器（actuators，作用于世界）。

## 关键实践案例

### Pinterest：标准化的执行器（MCP）
[[Pinterest-Engineering]] 通过部署 **[[Model-Context-Protocol-MCP|MCP]]** 生态系统，将内部复杂的 Presto、Spark 等数据系统封装为 Agent 可直接调用的“执行器（Actuators）”。这种标准化的连接协议使得 Agent 无需理解复杂的 API，只需通过统一协议即可操作生产系统。

### Shopify：原生透明的场域（Lehrwerkstatt）
Shopify 的 River Agent 强制在公开频道工作（[[Lehrwerkstatt]]），这是一种组织层面的 Agent-Native：它不仅让 Agent 融入工作流，还利用 Agent 的交互过程来重新塑造人类的协作与学习模式。

## 关键数据点

- **文档痛点**：Karpathy 的"pet peeve"——为什么文档还在告诉"你"去做什么？他想要的是"我应该复制粘贴给 agent 的文本"
- **部署摩擦**：MenuGen 项目的最大痛苦不是写代码，而是去 Vercell 后台配置 DNS、连接各种服务——这些都应该被 agent 接管
- **Agent-Native 测试标准**：Karpathy 提出——"给定一句 prompt，LLM 能否从零构建一个 app 并直接部署上网，中间不需要人触碰任何东西？"
- **Sensors（传感器）+ Actuators（执行器）框架**：这是 Karpathy 提出的 agent 交互架构隐喻，如同物联网中的传感器和执行器

## 需求侧：当 Agent 成为一等客户端（2026-10）

Karpathy 的 Agent-Native 主要从供给侧提出要求：基础设施必须让 Agent 能直接读取状态并执行动作。[[20261004-lenny-openai-head-chatgpt-new-era]] 补出另一半——**如果 Agent 本身成为高频调用者，产品还要为机器客户端的规模和经济行为而设计。**

Tibo Sottiaux 预测未来互联网中的多数 actions 会由 Agent 执行，并以 Notion MCP 开放给 Agent 后出现大量调用为例，指出系统很快会遇到 capacity 与 economics 问题。这个判断虽然仍是预测，但揭示了 Agent-Native 从“接口兼容性”走向“机器流量工程”的三个额外要求：

1. **Machine-callable action surface**：API / MCP / plugin 不只是暴露数据，还要有明确的 action schema、失败语义、权限和可发现性；
2. **Machine-scale capacity & economics**：Agent 可以比人类 UI 用户更高频、更并发地调用服务，因此 rate limit、配额、计费、缓存和容量规划必须把机器调用当作一等负载；
3. **Machine-oriented observability & guardrails**：自动调用需要结构化 trace、风险分层、异常检测、可撤销/升级路径，而不能只依赖给人看的报错页面。

**判断**：Agent-Native 的成熟度不应只问“Agent 能不能调用”，还要问：

```text
能调用
  → 能稳定高频调用
  → 能在明确经济边界内调用
  → 能被监控、限制、审计和恢复
```

这也意味着 human interface 与 agent interface 可能同时成为产品的一等入口：前者优化理解与体验，后者优化可执行性、吞吐、确定性和治理。

> [!warning] 边界
> “互联网多数 actions 将由 Agent 完成”是受访者的未来预测；Notion 的流量案例没有给出绝对量、增长率或独立核验，因此不能据此宣称 Agent traffic 已经普遍超过 human traffic。Agent-Native 也不意味着取消人类 UI——访谈同时强调应继续投资更自然的多模态 human experience。

## 前提与局限性

- Agent-Native 的前提是模型能力足够稳定，能可靠地在非确定性环境中操作
- 安全边界是核心挑战——给 agent 自动配置 DNS 的能力意味着巨大的权限风险
- 目前仍是早期阶段，Agent-Native 的标准和最佳实践尚未形成
- 与 [[Agent-First-Enterprise]] 是同一方向的不同层面——前者是基础设施范式，后者是企业组织范式

## 关联概念

- [[Software-3.0]] — Agent-Native 是 Software 3.0 的基础设施要求
- [[Agentic-Engineering]] — Agent-Native 环境下的开发实践
- [[Agent-First-Enterprise]] — 企业层面的 Agent-Native 组织设计
- [[Machine-Readable-Processes]] — 流程层面的 Agent-Native 化
