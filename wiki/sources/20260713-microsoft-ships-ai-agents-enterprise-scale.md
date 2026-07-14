---
type: source-summary
title: "How Microsoft Ships AI Agents at Enterprise Scale"
source_raw:
  - "[[20260713-microsoft-ships-ai-agents-enterprise-scale]]"
created: 2026-07-14
updated: 2026-07-14
tags:
  - source-summary
  - agent-harness
  - production-agents
  - microsoft
  - evaluation
evidence_level: medium
claim_type: mixed
---

# How Microsoft Ships AI Agents at Enterprise Scale

## 编译摘要

### 1. 浓缩

- **核心结论1**: **Harness 与模型同等重要，甚至更重要**——生产 Agent 失败的原因几乎从不是模型本身，而是模型周围的一切：数据检索、工具调用、身份控制、质量漂移。Marco Casalaina 的核心判断是 "the harness matters as much as the model"。
  - 关键证据: Microsoft Foundry 服务 80,000+ 企业，Microsoft 365 Copilot 服务 2000 万用户。Claude Opus 4.8 发布后，GitHub Copilot CLI 团队必须重新调优 harness 并重新运行评估才能上线——模型不能像数据库版本那样直接切换。
- **核心结论2**: **生产级 Agent Harness 由五层组成**——推理层（Inference）、Agent 运行时（Runtime）、可观测性与治理层（Observability）、身份层（Identity）、上下文层（Context）。上下文层是决定 Agent 能否正确工作的核心难题。
  - 关键证据: Microsoft 将上下文层产品化为四个 IQ 服务（Foundry IQ 处理非结构化数据、Fabric IQ 处理结构化数据、Web IQ 实时网络检索、Work IQ 处理 Microsoft 365 生产力面），每个通过 MCP 被 Agent 调用。
- **核心结论3**: **检索应成为子 Agent（Retrieval-as-a-Subagent），而非一次性 RAG**——经典 RAG 是 one-shot 模式，无法从坏检索中恢复。生产级上下文层将检索包装在 agentic 循环中：规划查询 → 尝试多源 → 评估结果 → 失败时重试 → 穷尽后返回结构化 "I don't know"。
  - 关键证据: Foundry IQ 实现多源迭代检索；tool search 模式（而非全量工具列表）已被 OpenAI 和 Anthropic 的 Agent 收敛到同一方案。同一检索循环既拉取知识也拉取能力。

### 2. 质疑

- **关于"Harness 与模型同等重要"的质疑**: 结论来自 Microsoft 平台 VP 的访谈——有推广自有平台的激励。如果模型能力持续快速提升，harness 中某些层（如上下文管理、错误恢复）可能被模型内化，使这个结论的时效性有限。
- **关于"五层架构"的质疑**: 五层是 Microsoft 特定的产品架构还是通用的生产 Agent 架构？身份层（Identity Layer）是 Microsoft 企业生态（Entra/Active Directory）的特有需求，还是所有企业 Agent 部署的通用需求？中小团队是否需要完整五层？
- **关于"Retrieval-as-a-Subagent"的质疑**: 迭代检索增加了延迟和 token 消耗。对于时间敏感的实时场景，多次迭代是否可接受？"何时穷尽迭代"的阈值是静态的还是自适应的？
- **关于"Self-improving loop"（Agent Optimizer）的质疑**: 自动改写 system prompt、调整工具使用、并行生成候选修复——这个循环是否有失控风险？如果 rubric 本身有缺陷，优化器会不会收敛到错误行为？

### 3. 对标

- **对标微服务分层架构**: 推理层 ≈ 数据库层、运行时 ≈ 应用层、可观测性 ≈ APM 层、身份层 ≈ IAM 层、上下文层 ≈ 缓存/搜索层。从微服务到 Agent 的架构迁移路径清晰，企业基础设施团队可复用已有经验。
- **Rubric-based evaluation 对标教育领域 rubric assessment**: 用具体行为标准取代泛化评分（groundedness/coherence），已在教育领域验证有效。Foundry 可以从生产 traces 自动草拟 rubric——类似课程评估标准的半自动生成。
- **Agent Identity 对标组织行为学的 virtual employee 概念**: Agent 拥有自己的目录条目、经理汇报线、邮箱——实质是把 Agent 变成组织结构图中的虚拟员工。与 FDE（Forward Deployed Engineering）形成对照：FDE 是嵌入客户的人类工程师，Agent-as-employee 是嵌入组织的数字员工。
- **Self-improving loop 对标 evolutionary computing**: Agent Optimizer 自动生成多个候选修复、并行评分、提升最优版本——逻辑结构与遗传算法同构。

### 关联概念

- [[Agent-Harness]]
- [[Harness-Engineering]]
- [[Context-Engineering]]
- [[Retrieval-as-a-Subagent]]
- [[Rubric-Based-Evaluation]]
- [[Distinct-Principal-Identity]]
- [[Agent-Orchestration]]
- [[Agent-Verification]]
- [[Forward-Deployed-AI-Enablement]]
- [[Building-Effective-Agents]]
