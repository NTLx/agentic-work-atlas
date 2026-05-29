---
type: source-summary
title: "Agentic AI 2026：当黑客松式的狂欢冷却下来"
source_raw:
  - "[[20260528-agentic-ai-2026-landscape]]"
created: 2026-05-29
updated: 2026-05-29
tags:
  - source-summary
  - agentic-ai
  - open-source
  - developer-ecosystem
  - agent-infrastructure
---

# Agentic AI 2026：当黑客松式的狂欢冷却下来

## 编译摘要

### 1. 浓缩

- **核心结论1**: Agentic AI 生态从 LLM 工具链演变为三层执行栈（Agent Infra / Model Infra / Model），Agent 正在成为软件的新用户，软件正在被重新包装为 Agent 可进入的运行环境
  - 关键证据: 226 个项目多标签分类显示 Coding Agent 78 个/14,019 参与者、MCP 59 个/6,651 参与者、Memory 70 个/7,609 参与者；GitHub bot/app actor 十年增长 154 倍（112→17,285）
- **核心结论2**: 开发者角色从"亲自完成每个动作"迁移到"定义目标、约束行动、验证结果、承担责任"——碳基定义任务，硅基承担执行
  - 关键证据: Top 100 Agentic AI 项目中 92 个使用 coding agent 配置（平均 2.8 种），Claude Code 覆盖率 81%；项目从写 CONTRIBUTING.md 转向为 Agent 写 AGENTS.md/CLAUDE.md
- **核心结论3**: Token 从聊天消耗变成生产资料，Token 供应链管理（推理调度、KV cache、成本路由、可观测性）成为 Agent 时代真正的生产基础设施
  - 关键证据: SGLang 路线图命名 "Distributed KVCache System For Agentic Workload"；LiteLLM 仓库中 cost/budget/spend 相关 issue/PR 合计 154 条；RouteLLM 实现 2x+ 成本节省，IPR 降低 43.9%

### 2. 质疑

- **关于"Agent 成为软件用户"的质疑**: 文章将 bot/app actor 增长等同于"Agent 成为软件用户"，但 17,285 个自动化账号中包含大量传统 CI/CD bot（dependabot、github-actions），真正的 AI Agent 占比可能远低于表面数字。自动化账号增长≠Agent 化
- **关于"碳基-硅基分工"的质疑**: 这个框架假设开发者能清晰地将任务定义为 Agent 可执行的形式，但大量软件工作涉及模糊需求沟通、政治协商、隐性判断——这些"定义层"工作本身难以形式化
- **关于数据可靠性的质疑**: 数据主要来自蚂蚁/InclusionAI 自家 OpenDigger 和 OpenRank 体系，分类方法（LLM 多标签分类 226 个 description/README）缺乏交叉验证，可能存在分类偏差

### 3. 对标

- **跨域关联1**: Token 供应链管理类似云计算早期的演化路径——从"能不能跑起来"到调度、弹性、观测、成本、SLA 的系统工程竞争，可迁移到企业 AI 基础设施决策
- **跨域关联2**: "项目重写 description"作为生态信号，类似生物学中的物种重新定义生态位（niche shift）——chatbot→agent workspace、RAG→context infra、framework→harness，反映选择压力变化
- **跨域关联3**: "AGENTS.md 是给 AI 的入职文档"类似 [[Lehrwerkstatt]] 和 [[Public-only-Constraint]]——隐性知识显性化是 Agent 可靠执行的前提

### 关联概念

- [[Agent-Infra]]
- [[Token-Supply-Chain]]
- [[Carbon-Silicon-Division]]
- [[Coding-Agents]]
- [[Agent-Harness]]
- [[Agentic-Engineering]]
- [[Model-Context-Protocol-MCP]]
- [[Context-Engineering]]
