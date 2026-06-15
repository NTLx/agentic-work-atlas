---
type: topic
title: "Agentic AI 生态结构"
description: "从 LLM 工具链到 Agentic AI 三层执行栈的生态演化——Agent Infra / Model Infra / Model 三层互相倒逼，token 从消耗品变成生产资料，开发者从执行层移动到定义层"
created: 2026-05-29
updated: 2026-06-15
evidence_level: medium
claim_type: mixed
tags:
  - topic
  - agentic-ai
  - developer-ecosystem
related_entities:
  - "[[Agent-Infra]]"
  - "[[Token-Supply-Chain]]"
  - "[[Carbon-Silicon-Division]]"
  - "[[Coding-Agents]]"
  - "[[Agent-Harness]]"
  - "[[Model-Context-Protocol-MCP]]"
source_raw:
  - "[[20260528-agentic-ai-2026-landscape]]"
---

# Agentic AI 生态结构

> 从 LLM 工具链到 Agentic AI 三层执行栈的生态演化。

## 核心论点

2025 年的 Agentic AI 生态还围绕 LLM SDK、RAG、Agent Framework、应用平台、推理基础设施分层。到 2026 年中，生态结构已重排为 **三层执行栈**：

```
┌─────────────────────────────────────┐
│  Agent Infra（任务入口 + 运行时）    │  ← 决定 AI 能替谁做事
├─────────────────────────────────────┤
│  Model Infra（token 供应链）        │  ← 决定能不能规模化
├─────────────────────────────────────┤
│  Model（能力边界）                  │  ← 决定能力上限在哪里
└─────────────────────────────────────┘
```

三层不是简单上下游，更像互相推着往前走：Agent 想做更长的任务 → 逼 Model Infra 降低推理成本 → Model Infra 变强让专用模型进入生产 → 模型提升又把 Agent 推出聊天框。

## 三条主线

### 1. Agent 成为软件的新用户

过去软件默认使用者是人（UI、按钮、表单）。Agent 时代，软件多了一个新使用者——它不需要漂亮界面，但需要稳定 API、工具协议、权限边界、可读状态、可执行命令、可验证结果、可回滚操作。

[[Agent-Infra]] 做的事，就是把"硅基执行者"接进软件世界。GitHub 数据佐证：bot/app actor 从 2017 年的 112 个增长到 2026 年的 17,285 个，十年 154 倍。

### 2. Token 从消耗品变成生产资料

当 Agent 从"回答一句话"扩展到"连续读代码、查资料、调用工具、等待反馈再继续执行"，token 就从聊天消耗变成了生产资料。[[Token-Supply-Chain]] 成为 Agent 时代真正的生产基础设施——推理调度、KV cache 管理、成本路由、可观测性和治理。

SGLang 路线图明确命名 "Distributed KVCache System For Agentic Workload"。Agent 改变了 token 的消费结构。

### 3. 碳基定义、硅基执行

开发者从"亲自完成每个动作"迁移到"定义目标、约束行动、验证结果、承担责任"。[[Carbon-Silicon-Division]] 是这个分工范式的核心表达。

## 生态信号数据

| 指标 | 数据 | 来源 |
|------|------|------|
| GitHub 开发者总数 | 1.8 亿+ | Octoverse 2025 |
| 2025 年新增开发者 | 3,600 万 | Octoverse 2025 |
| GitHub bot/app actor（2026 前 4 月） | 17,285 | OpenDigger |
| HuggingFace 公开模型 | 200 万 | HuggingFace Hub |
| Agentic AI landscape 项目数 | 226 | 蚂蚁 InclusionAI |
| Coding Agent 项目 / 参与者 | 78 / 14,019 | 蚂蚁 OpenDigger |
| MCP 项目 / 参与者 | 59 / 6,651 | 蚂蚁 OpenDigger |
| Top 100 项目使用 coding agent 比例 | 92% | 蚂蚁 OpenDigger |
| 平均每个项目使用 coding agent 种类 | 2.8 | 蚂蚁 OpenDigger |

## 项目自述迁移路径（description 变化）

226 个项目中 96 个改过 description，沿七条路径向 Agent 执行栈靠拢：

1. Workflow Builder → Agent Orchestrator
2. RAG / Data / Vector DB → Context / Memory Infra
3. Chatbot / AI Client → Agent Workspace / Personal Assistant
4. Dev Tool / IDE / Terminal → Agentic Dev Environment
5. Framework → Agent Harness
6. Tool Integration → Agent Control Plane
7. RL / Inference / Training → Agent Workload Infra

## 关键问题

- **模型会不会吞噬软件和开源？** 答案更像重分工。模型接管搜索、填写、整理等动作，但吃不掉软件背后的秩序。越让模型接近真实工作，越需要软件定义边界、保存状态、连接系统。
- **开源在 AGI 时代的位置？** 开源不会自动胜利，但仍有不可替代的位置：开发者参与、项目可审计、标准共同制定、工具可本地部署、知识可共享。

## 相关 Topic

- [[Agentic-Engineering-Patterns]] — 开发者层面的 Agentic 实践
- [[Organization-as-Agent-Harness]] — 组织层面的 Agent 化
- [[AI-Labor-Bottleneck-Shift]] — 劳动瓶颈从生产转向分配和集成
- [[AI-Era-Economy-Shift]] — 经济层面的范式转变

## 来源

- [[20260528-agentic-ai-2026-landscape]] — 蚂蚁开源技术委员会 2026 年 Agentic AI 生态报告
