---
type: source-summary
title: "How to scale agentic applications without creating AI sprawl"
canonical_url: "https://www.databricks.com/blog/how-scale-agentic-applications-without-creating-ai-sprawl"
raw_state: index
original_raw_file: "20260930-databricks-agentic-apps-ai-sprawl.md"
body_sha256: "7a65ad52c54f236d6cf554c5eb90b6dbb9d4145ce15dedc49f368507372ef856"
indexed_at: "2026-10-12T17:18:03+08:00"
created: 2026-10-12
updated: 2026-10-12
tags:
  - source-summary
  - agent-infra
  - enterprise-ai
  - governance
  - observability
evidence_level: medium
claim_type: mixed
source_locator:
  - "opening and summary: AI sprawl as duplicated integrations, policies, context, cost and change friction"
  - "Context should be shared, not rebuilt"
  - "Choice should not create fragmentation"
  - "Control has to follow every action"
  - "Control also requires visibility into what happened"
  - "Shared infrastructure makes composition easier"
  - "Build for choice, context, and control"
---

# How to scale agentic applications without creating AI sprawl

> Databricks 第一方架构文章，讨论企业从单个 Agent 走向 Agent fleet 后，如何避免每个应用重复建设 context、model/tool access、governance、evaluation、observability 与 cost controls。稳定价值在架构分层，而不是具体 Databricks 产品组合；产品能力与优越性属于 vendor claim，按 medium / mixed 证据吸收。

## 1. 浓缩

### 1.1 AI sprawl 的核心不是 Agent 数量，而是 surrounding infrastructure 被重复复制

文章把问题定义得很准确：单个 Agent 越来越容易做，但企业里每个团队如果分别连接模型、数据、业务语义、工具、权限和 telemetry，就会出现 duplicated integrations、inconsistent policies、fragmented context、AI spend 增长和越来越高的 change cost。

因此可以区分：

```text
agent proliferation ≠ AI sprawl

AI sprawl
= duplicated integration surfaces
+ duplicated semantic definitions
+ inconsistent policy / identity handling
+ fragmented traces / evals / cost controls
```

**判断**：企业不应该把“减少 Agent 数量”作为治理目标。真正需要压缩的是每新增一个 Agent 所新增的基础设施副本数。

### 1.2 稳定层与易变层应该分离：上层保留 choice，下层统一 operating plane

作者明确不主张企业锁定一个 model、tool 或 harness。不同步骤对 reasoning quality、latency、cost 有不同需求，而 ecosystem 也会持续变化。

更稳定的架构是：

```text
volatile choice layer
  models / harnesses / tools / agent implementations
                 ↓
shared operating planes
  context + identity/permissions + policy
  + tracing/evaluation + budgets/cost
```

**判断**：标准化对象应从“统一模型/统一 Agent framework”转向**统一 surrounding contract**。模型与 harness 可以替换，但接入企业语义、权限、观测和成本控制的方式不应随每个 Agent 重做。

这是一种对多模型/多 harness 现实更友好的平台策略：把 diversity 留在 capability layer，把一致性放在 operating layer。

### 1.3 Context 是共享业务语义，不只是共享向量库

文章用 sales agent 与 customer-support agent 举例：两者都需要知道 active customer、customer-owned products、account hierarchy 等概念。如果每个 Agent 自己重建定义，同一个业务实体会在不同 workflow 中具有不同含义。

因此 enterprise context 至少包含：

- governed enterprise data；
- business definitions / ontology；
- documents / retrieval；
- tools / applications；
- interaction history / memory；
- identity-conditioned access。

**判断**：所谓 shared context layer 的核心是**语义复用 + 权限一致性**。仅仅让多个 Agent 指向同一个文档库，并没有解决“同一个指标在两个 workflow 中含义不同”的问题。

### 1.4 控制应随 action 走：delegator 的权限不应原样复制给 Agent

文章的 refund 示例很重要：发起请求的员工可能拥有较广账户权限，但执行退款的 Agent 只需要当前订单数据、退款政策，以及执行特定交易所需的权限。

可以抽象为：

```text
human principal authority
        ↓ delegation
current task envelope
        ↓ down-scope
agent data scope + tool scope + transaction scope
```

**判断**：Agent authorization 不应等于“继承调用者全部权限”，而应等于**调用者权限 ∩ 当前任务所需权限 ∩ policy action envelope**。

这把 least privilege 从 static identity 问题推进为 delegation-time capability shaping。

### 1.5 Final answer 不足以承担审计：控制面必须保留 execution trajectory

一个看似正确的最终答案可能来自错误 retrieval、错误 tool call 或意外 execution path。文章要求能回放：用了什么信息、哪个模型、哪些工具、哪些 policy、哪里偏离预期，并把 traces 与 evaluation 连接到下一轮迭代。

因此生产 Agent 的最低 operational evidence 更接近：

```text
request identity/context
+ retrieved evidence
+ concrete model/harness version
+ tool/action trajectory
+ policy decisions
+ usage/cost
+ eval outcome
```

**判断**：observability 是 governance 的证据面，而不是单独的运维 dashboard。没有 trajectory evidence，policy 是否真的执行、错误来自模型还是 retrieval/tooling 都难以判定。

## 2. 对现有知识的增量

### 对 [[Agent-Infra]]

现有 Agent Infra 已包含 runtime、context、memory、tool use、sandbox、AgentOps 和 control plane。本文补上一个更稳定的平台分层原则：**规模化的单位不应是“复制一个 Agent stack”，而是“让新 Agent 继承同一套 shared operating planes”。**

可以把 enterprise Agent Infra 分为：

1. **Choice plane**：允许 model / harness / tool 多样化；
2. **Context plane**：共享业务语义、数据与 identity-conditioned context；
3. **Control plane**：权限、policy、sandbox、budgets、rate limits；
4. **Evidence plane**：traces、evaluation、cost、tool activity。

文章自己用 choice/context/control 三分法；evidence plane 是根据其 observability/evaluation 段落做出的稳定拆解。

### 对 [[Policy-as-Code-for-Agent-Governance]]

本文最重要的治理增量不是又一个“统一 guardrails”口号，而是 **policy scope 与 delegation scope 必须绑定**。调用者有权做某事，不代表 Agent 应持有该调用者全部 authority；runtime 应把权限降到当前 task 所需范围，并在工具/action 层执行和留下 trace。

## 3. 证据边界

- 这是 Databricks 产品与架构观点，具体 Agent Bricks / Omnigent / Unity Gateway 能力与效果没有独立 benchmark。
- “choice/context/control”是有用的设计框架，但不是经比较试验证明唯一正确的企业 Agent 架构。
- 统一 control plane 自身会形成集中依赖、故障域和 vendor lock-in；来源没有展开这些反向成本。
- 共享 context 只有在语义定义、ownership 和更新责任清楚时才减少碎片化；集中平台并不会自动消除冲突定义。
- tracing 能增加可解释证据，但不能证明每个 action 都被 policy 完整拦截；observability ≠ enforcement coverage。

## 4. 关联概念

- [[Agent-Infra]]
- [[Policy-as-Code-for-Agent-Governance]]
- [[Agent-Harness]]
- [[Context-Engineering]]
- [[Agent-Containment]]
- [[Least-Agency]]
