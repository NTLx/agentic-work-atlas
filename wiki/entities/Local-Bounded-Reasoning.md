---
type: entity
title: Local-Bounded Reasoning
aliases:
  - Local-Bounded Reasoning
  - local-bounded reasoning
  - 局部有界推理
definition: "通过工作流结构、图谱、程序分析和策略约束，把 LLM 的推理限制在局部相关状态空间内的 Agent 设计原则"
created: 2026-06-02
updated: 2026-06-16
evidence_level: medium
claim_type: mixed
tags:
  - AI-Agent
  - reasoning
  - context-engineering
  - enterprise-ai
related_entities:
  - "[[Agent-Logic]]"
  - "[[Context-Engineering]]"
  - "[[Agentic-Workflow-Token-Efficiency]]"
  - "[[Verifiable-Agent-Engineering]]"
source_raw:
  - "[[20260602-ibm-agent-logic-scalable-ai-adoption]]"
---

# Local-Bounded Reasoning

> [!definition] 定义
> **Local-Bounded Reasoning** 是一种 Agent 设计原则：通过工作流结构、知识图谱、程序分析和策略约束，把 LLM 的推理限制在局部相关状态空间内，而不是让模型在整个企业上下文中自由搜索。

## 为什么需要它

企业系统的上下文空间很大：遗留代码、微服务依赖、监控指标、权限策略、合规规则、工单历史和业务流程都可能相关。把这些全部塞进上下文窗口，会同时放大成本、噪声和错误关联。

局部有界推理的目标不是让模型知道更多，而是让模型少看但看对。

## 典型机制

- 先用程序分析或图遍历找出相关模块、服务、事件或规则。
- 再把局部证据组织成模型可消费的上下文。
- 让模型在被约束的候选空间内解释、规划或生成。
- 用测试、规则、策略或证据链验证输出。

## 与 Context Engineering 的关系

[[Context-Engineering|Context engineering]] 关心“模型应该看到什么”。Local-bounded reasoning 进一步提出选择原则：上下文不只是压缩出来的，而是被工作流结构裁剪出来的。

这让上下文管理从 token 优化变成结构优化。

## 关键数据点

- IBM 主机代码理解案例显示，先用深度静态分析和预索引数据库缩小代码理解空间，可以在最高 1M 行代码、1K 程序任务中把 token 消耗降到约 1/30。
- Aster 测试生成通过程序分析和数据前后处理，把测试生成从开放式生成收缩为围绕代码结构和变更边界的局部任务。
- IT incident investigation 案例用知识图谱和 observability 信息引导调查，而不是让模型直接遍历全量日志和服务上下文。

## 前提与局限性

如果局部边界切错，Agent 会错过真正原因。IT incident、复杂代码缺陷和跨部门流程问题都可能存在远距离依赖。因此 local-bounded reasoning 必须配合重新扩展搜索空间的机制，而不能把第一次裁剪当成真理。

这个原则更适合强结构任务。对战略判断、组织政治、创意探索等低结构任务，局部边界可能只能降低噪声，不能保证判断正确。

## 关联概念

- [[Agent-Logic]] — 产生局部边界的 harness 逻辑层。
- [[Agentic-Workflow-Token-Efficiency]] — 局部化推理降低 token 成本。
- [[Verifiable-Agent-Engineering]] — 局部边界需要被验证和回退。
