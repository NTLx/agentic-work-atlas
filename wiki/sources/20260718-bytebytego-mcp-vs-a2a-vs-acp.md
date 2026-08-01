---
type: source-summary
title: "MCP vs A2A vs ACP: How AI Agents Actually Talk to Each Other"
source_raw:
  - "[[20260718-bytebytego-mcp-vs-a2a-vs-acp]]"
created: 2026-07-27
updated: 2026-07-27
tags:
  - source-summary
  - infrastructure
evidence_level: medium
claim_type: extracted
---

# MCP vs A2A vs ACP: How AI Agents Actually Talk to Each Other

> ByteByteGo 对三种 Agent 通信协议（MCP / A2A / ACP）的功能定位与互补关系的概览。证据等级：medium（技术博客，描述性整理，无原创数据）。

## 编译摘要

### 1. 浓缩
- **核心结论1**: 三种协议覆盖两个通信层：MCP 是 agent→tool（工具调用），A2A 是 agent→agent（任务委派），ACP 是 REST-first 的 agent→agent（已合并入 A2A）
  - 关键证据: MCP 流程：Host app → MCP client → MCP server → 工具执行 → 结构化响应；A2A 流程：Agent Card 发现 → 任务委派 → input-required 暂停/循环；ACP 流程：Agent Manifest → HTTP 调用 → 同步响应或 SSE 流
- **核心结论2**: MCP 与 A2A 在生产中互补——MCP 处理工具访问，A2A 处理 agent 间通信，不存在替代关系
  - 关键证据: 文中明确陈述 "MCP 和 A2A 在生产中是互补的"；与 [[2026-ai-agent-protocol-ecosystem-map-mcp-a2a-acp-ucp|协议生态图]] 结论一致
- **核心结论3**: Agent 通信协议标准化被类比为 "HTTP 早期"——当前是建立互操作生态的窗口期
  - 关键证据: 评注引用 "feels like the early days of establishing HTTP for the web"

### 2. 质疑
- **关于"互补而非竞争"的质疑**: MCP 可以调用另一个 agent 的 MCP server 来间接实现 agent→agent 通信，A2A 的 Agent Card 也可包含工具描述——两个协议的边界在实践中可能模糊。"互补"是协议设计者的定位叙事，未经大规模生产验证
- **关于 ACP 合并的质疑**: ACP "已合并入 A2A"被一句带过，但合并意味着什么？是 ACP 的 REST-first 设计被 A2A 吸收，还是 ACP 团队放弃独立路线？合并后 ACP 的 REST 优势（低延迟同步调用）是否在 A2A 中保留？这些关键问题未被讨论
- **关于 HTTP 类比的质疑**: HTTP 标准化发生在单一组织（CERN/W3C）主导下，而 Agent 协议由多个竞争厂商（Anthropic/Google）分别主导——权力结构不同，标准化路径可能更像 IM 协议（XMPP vs 专有）而非 HTTP

### 3. 对标
- **跨域关联1**: Agent 协议分层（tool 层 / agent 层）与网络协议栈（传输层 / 应用层）同构。MCP 类似 RPC/gRPC（结构化远程调用），A2A 类似服务发现 + 编排（Consul/Kubernetes Service Mesh）。这意味着 agent 生态可能复现微服务生态的演化路径：先统一调用协议，再解决发现/路由/治理
- **跨域关联2**: A2A 的 "input-required 暂停状态"与 [[Three-State-Protocol|三态协议]] 的人机交互模式结构相似——agent 在需要外部输入时暂停而非猜测，是 [[Agent-Containment|Agent 容器化]] 理念在协议层的体现
- **跨域关联3**: ACP 被 A2A 吸收的案例验证了技术标准的 "协议达尔文主义"——生态位重叠的协议最终合并或消亡，与 [[Model-Context-Protocol-MCP]] 实体中记录的 "标准战争基本结束" 判断一致

### 关联概念
- [[Model-Context-Protocol-MCP]]
- Agent-to-Agent Protocol (A2A)
- [[Agent-Orchestration]]
- [[Three-State-Protocol]]
- [[Agent-Containment]]
