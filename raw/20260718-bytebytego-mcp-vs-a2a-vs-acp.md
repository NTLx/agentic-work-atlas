---
type: raw
source: "https://blog.bytebytego.com/p/mcp-vs-a2a-vs-acp-how-ai-agents-actually"
author:
  - "ByteByteGo"
published: "2026-07-18"
created: "2026-07-19"
tags:
  - clippings
  - agent-protocol
  - MCP
  - A2A
  - ACP
  - interoperability
---

# MCP vs A2A vs ACP: How AI Agents Actually Talk to Each Other

## 三种 Agent 通信协议

**MCP (Model Context Protocol): agent → tool 通信。**
Host app 接收用户请求 → 内嵌的 MCP client 格式化并路由到正确的 MCP server → server 执行工具调用并返回结构化响应 → agent 用结果继续推理。

**A2A (Agent-to-Agent): agent → agent 通信。**
无法独立完成任务的 agent 通过 Agent Card（发布在已知 URL 上）发现可用的 peer → 委派任务 → 接收结构化结果。如果第二 agent 在任务中途需要更多输入，暂停在 input-required 状态并循环回第一 agent。

**ACP (Agent Communication Protocol): 基于 REST 的 agent → agent 通信（已合并入 A2A）。**
ACP 采用 REST-first 方法。Peers 通过 Agent Manifest 发现 → 直接 HTTP 调用 → 同步响应（低延迟任务）或 async SSE 流。

## 生产中的互补关系

MCP 和 A2A 在生产中是互补的：MCP 处理工具访问，A2A 处理 agent 间通信。

## 评注中的关键洞察

"Standardizing agent-to-agent communication protocols feels like the early days of establishing HTTP for the web. Getting this right is going to be the difference between fragmented, siloed automation and a truly interoperable AI ecosystem."

## 知识库连接

- 与 [[MCP 治理风险]]（07-16）形成互补：MCP 是 agent→tool，治理风险在 Anthropic 控制单点
- A2A 引入了"agent-to-agent 委派"——连接 [[Agent 治理三层保证定理]]中的 L+ 层"agent-to-agent 委派治理的空白填补"
- 三协议竞争验证了"过程>模型"元原则：协议（过程编排）比模型能力更重要
- 与 [[Agent Identity 分层标准化]]形成对照：MCP/A2A 是通信协议层，Agent Identity 是身份层——两者正交且互补
- A2A 的"Agent Card"机制与 SPIFFE SVID 扩展（07-18 Agent Identity 路线）有结构同构性
