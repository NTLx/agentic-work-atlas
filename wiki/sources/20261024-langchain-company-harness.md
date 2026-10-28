---
type: source-summary
title: "The five components of building a company harness"
source_raw:
  - "[[20261024-langchain-company-harness]]"
canonical_url: "https://www.langchain.com/blog/components-building-company-harness"
canonical_key: "company-harness-control-plane"
promotion_id: "kp-20261026-company-harness"
work_id: "wiki_compile:company-harness-control-plane:20261026:recovery-v1"
correlation_id: "knowledge-promotion:week-of-2026-10-26"
raw_state: full
created: 2026-10-28
updated: 2026-10-28
tags:
  - source-summary
  - agent-harness
  - enterprise-ai
evidence_level: medium
claim_type: mixed
source_locator:
  - "Opening list: five recurring company-harness primitives"
  - "Problem: Identity: OBO vs fixed identity and context-dependent tool availability"
  - "Problem: Memory: global and per-user scopes"
  - "Problem: Code Execution: sandbox plus authenticated service access"
  - "Problem: Scheduled Runs: background/event-triggered execution"
---

# The five components of building a company harness

> LangChain 对 GTM Agent、OpenSWE、Content Studio 三类内部 Agent 的一手经验总结。它提供的是公司级 Agent runtime primitives 的案例证据，不是跨企业比较或最优架构证明。

## 编译摘要

### 1. 浓缩

#### 核心结论 1：company harness 的共性正在从“prompt 规范”转向运行时 primitives

LangChain 将三类内部 Agent 的共同基础归纳为五项：工作发生处的交互界面、identity、分层 memory、sandboxed code execution + authenticated service access、scheduled/background runs。

**判断**：当 Agent 进入多人、多系统、长期运行场景后，真正稳定复用的架构单元更多是 identity/memory/execution/scheduling 等 runtime primitive，而不是某个具体 prompt。

#### 核心结论 2：identity 不是单一 service account，而是按动作与上下文选择 delegation model

文章同时使用 on-behalf-of 与 fixed identity；同一个 Agent 甚至会按工具、DM/shared channel、foreground/background execution 切换身份模式。

**判断**：企业 Agent 的 identity contract 至少需要回答“谁触发、以谁身份、在什么上下文、哪些工具可见、谁承担结果”，不能把 authentication 简化为一个长期 token。

#### 核心结论 3：ambient work 是 harness 的一等能力

大量运行来自 schedule/event，而不是用户主动发消息。这意味着 company harness 必须把 background identity、权限、context、memory 与观察/通知一起设计，不能只优化同步对话体验。

### 2. 质疑与边界

- 三个样本都来自 LangChain 自己的产品/内部运行环境，不能据此证明五项 primitives 对所有企业都充分或必要。
- memory 仍被作者称为探索较少的区域；“global + user memory”是当前实现形态，不等于已经解决 memory governance/provenance。
- sandbox + secret proxy 说明执行与凭据需要隔离，但没有给出独立攻击测试或完整 side-effect control 证据。
- scheduled/background run 增加 autonomy，也增加 stale context、权限生命周期、重复执行、预算与观测责任；文章主要讲能力，不是完整治理模型。

### 3. 对标与约束

- 与 [[Organization-as-Agent-Harness]]：该 Topic 的目标/流程/权限/学习是组织层抽象；LangChain 五项更像其下的运行时实现 primitives，两者互补而不是替代。
- 与 [[Agent-Harness]]：补充 company/multiplayer 语境中的 identity、memory、sandbox、scheduling 组合。
- 与 [[Agent-Security]]：OBO/fixed identity、context-dependent tool availability 与 secret mediation 都直接落到授权和执行边界。
- 与自动化控制面：scheduled/background work 说明企业 Agent 不只是交互产品，还需要 durable state、幂等、重试、通知和可观测的控制面。

## 重要判断

- **判断**：公司级 Agent harness 可以被拆成组织抽象层与 runtime primitive 层：组织层定义目标/流程/权限/学习，runtime 层提供 interaction surface、identity、memory、sandboxed execution 与 background scheduling。把两层混成“一个更好的 prompt”会同时丢失治理和执行边界。
  - **证据**：[[20261024-langchain-company-harness]]；现有 [[Organization-as-Agent-Harness]] 的跨案例综合。
  - **边界**：LangChain 的五项是内部经验归纳，不是普适必要条件；不同组织仍需按 action surface、监管、数据与运营模式裁剪。

### 关联概念
- [[Organization-as-Agent-Harness]]
- [[Agent-Harness]]
- [[Agent-Security]]
