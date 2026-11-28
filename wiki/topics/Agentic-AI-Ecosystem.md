---
type: topic
title: "Agentic AI 生态结构"
description: "2026年5月生态报告的Agent Infra/Model Infra/Model三层视角，及软件接口、推理供给与任务分工的候选变化"
created: 2026-05-29
updated: 2026-11-28
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

2025 年的 Agentic AI 生态还围绕 LLM SDK、RAG、Agent Framework、应用平台、推理基础设施分层。2026年5月原作者提出**三层执行栈**的分析视角（非唯一行业标准或已验证的固定迁移）：

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

[[Agent-Infra]] 做的事，就是把"硅基执行者"接进软件世界。原报告OpenDigger同期前四月活跃bot/app actor为112（2017）→17,285（2026），约154倍，含CI/依赖更新等传统自动化，不是AI Agent人数、任务量或生产率。

### 2. Token 从消耗品变成生产资料

当 Agent 从"回答一句话"扩展到"连续读代码、查资料、调用工具、等待反馈再继续执行"，token 就从聊天消耗变成了生产资料。[[Token-Supply-Chain]] 成为 Agent 时代真正的生产基础设施——推理调度、KV cache 管理、成本路由、可观测性和治理。

SGLang 路线图明确命名 "Distributed KVCache System For Agentic Workload"。Agent 改变了 token 的消费结构。

### 3. 碳基定义、硅基执行

部分开发工作可以增加定义、委托、验证及责任治理；不代表全体开发者固定角色迁移或执行技能消失。[[Carbon-Silicon-Division]] 是这个分工范式的核心表达。

## 生态信号数据（历史快照，非当前实时统计）

2025 Octoverse官方确认180M+及过去一年新增36M+；[2026 Octoverse](https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/) 是后续同平台披露，不能将新增账号、活动、提交或PR等同人类就业或质量。原226项目是作者选定的landscape，LLM多标签分类可重叠；参与者可能含机器人及跨项目重复。Top100是OpenRank筛选，配置/忽略项痕迹并非实际调用或持续使用。未重跑OpenDigger。

| 指标 | 数据 | 来源 |
|------|------|------|
| GitHub 开发者总数 | 1.8 亿+ | Octoverse 2025 |
| 2025 年新增开发者 | 3,600 万 | Octoverse 2025 |
| GitHub bot/app actor（2026 前 4 月） | 17,285 | OpenDigger |
| HuggingFace 公开模型 | 200 万 | HuggingFace Hub |
| Agentic AI landscape 项目数 | 226 | 蚂蚁 InclusionAI |
| Coding Agent 项目 / 参与者 | 78 / 14,019 | 蚂蚁 OpenDigger |
| MCP 项目 / 参与者 | 59 / 6,651 | 蚂蚁 OpenDigger |
| OpenRank Top100项目出现coding agent相关配置痕迹 | 92/100 | 蚂蚁文件树扫描，非实际使用率 |
| Top100每项目平均相关配置/标记种类 | 2.8 | 原报告，非运行测量 |

## 项目自述迁移路径（description 变化）

原报告226个项目中96个修改description，作者归纳七条路径；自述变化不证明功能完成、真实用户需求或行业整体转型：

1. Workflow Builder → Agent Orchestrator
2. RAG / Data / Vector DB → Context / Memory Infra
3. Chatbot / AI Client → Agent Workspace / Personal Assistant
4. Dev Tool / IDE / Terminal → Agentic Dev Environment
5. Framework → Agent Harness
6. Tool Integration → Agent Control Plane
7. RL / Inference / Training → Agent Workload Infra

## 关键问题

- **模型会不会吞噬软件和开源？** 答案更像重分工。模型接管搜索、填写、整理等动作，但吃不掉软件背后的秩序。越让模型接近真实工作，越需要软件定义边界、保存状态、连接系统。
- **开源在 AGI 时代的位置？** 开源可在特定许可、治理及部署条件下提供价值：开发者参与、项目可审计、标准共同制定、工具可本地部署、知识可共享。

## 相关 Topic

- [[Agentic-Engineering-Patterns]] — 开发者层面的 Agentic 实践
- [[Organization-as-Agent-Harness]] — 组织层面的 Agent 化
- [[AI-Labor-Bottleneck-Shift]] — 劳动瓶颈从生产转向分配和集成
- [[AI-Era-Economy-Shift]] — 经济层面的范式转变

## 来源

- [[20260528-agentic-ai-2026-landscape]] — 蚂蚁开源技术委员会 2026 年 Agentic AI 生态报告
