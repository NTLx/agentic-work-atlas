---
type: entity
title: Graph-Guided Agent Investigation
aliases:
  - Graph-Guided Agent Investigation
  - graph-guided agent investigation
  - 图引导 Agent 调查
definition: "用知识图谱、依赖图或 DAG 引导 Agent 调查复杂系统故障、证据链和根因路径的工程模式"
created: 2026-06-02
updated: 2026-06-16
evidence_level: medium
claim_type: mixed
tags:
  - AI-Agent
  - observability
  - enterprise-ai
related_entities:
  - "[[Agent-Logic]]"
  - "[[Knowledge-Graph]]"
  - "[[Local-Bounded-Reasoning]]"
  - "[[ITBench]]"
  - "[[Verifiable-Agent-Engineering]]"
source_raw:
  - "[[20260602-ibm-agent-logic-scalable-ai-adoption]]"
---

# Graph-Guided Agent Investigation

> [!definition] 定义
> **Graph-Guided Agent Investigation** 是用知识图谱、依赖图或 DAG 引导 Agent 调查复杂系统故障、证据链和根因路径的工程模式。它让 Agent 沿结构化关系探索，而不是在日志、指标和文档中自由漫游。

## 核心问题

企业 IT、工业资产和代码系统的故障通常不是单点文本问题，而是网络问题：服务依赖、调用链、事件传播、配置变更、代码路径和资产状态共同决定结果。

LLM 擅长解释和综合，但不擅长在大规模图结构中稳定、低成本地搜索。因此图引导调查把“找相关节点和路径”的工作交给图结构，把“解释这些证据意味着什么”的工作交给模型。

## 典型流程

```text
告警 / 问题
  -> 图结构定位相关节点
  -> 收集局部证据
  -> LLM 解释候选根因
  -> 验证 / 追加查询 / 升级
```

## 价值

- **缩小搜索空间**: 从全量日志和服务列表收缩到局部依赖子图。
- **保留证据链**: 调查路径可以回溯到节点、边和观测数据。
- **降低幻觉**: 模型不必凭语言猜测系统关系。
- **支持复用**: 一次 incident 形成的路径和规则可反哺后续调查。

## 与 Knowledge Graph 的区别

[[Knowledge-Graph|Knowledge graph]] 是结构化事实层；graph-guided investigation 是使用这层事实指导 Agent 行动的工作流模式。

前者回答“系统里有什么关系”，后者回答“Agent 应该沿哪些关系调查”。

## 关键数据点

- IBM Instana I3 / IT incident investigation 使用知识图谱、程序分析和 observability 驱动 orchestration。
- 在 ITBench 上，I3 agent 相比 ReAct agent with GPT-5.1 最高提升 4 倍。
- IBM 文章还称，代码分析和 bug 修复 agent 在定位 culpable microservice 与 bug repair 上优于 state-of-the-art coding agent，并显著降低 token。
- Maximo Condition Insights 用 DAG、结构化证据和验证循环处理工业资产维护，内部 pilot 将资产分析时间从 15-20 分钟降到 15-30 秒。

## 前提与局限性

图结构不会自动保证正确。依赖图可能过期，观测数据可能缺失，边权也可能无法表达真实因果。因此图引导调查需要与重新采样、人工升级和反事实验证配合。

该模式最适合依赖关系明确、观测数据足够、证据链可结构化的环境。如果图谱长期不维护，Agent 只是沿着过期地图更快地走错路。

## 关联概念

- [[Agent-Logic]] — 图遍历是 agent logic 的重要组成。
- [[Local-Bounded-Reasoning]] — 图结构提供局部推理边界。
- [[ITBench]] — 企业 IT Agent 能力评估场景。
- [[Verifiable-Agent-Engineering]] — 图路径让调查过程更可观察和可复现。
