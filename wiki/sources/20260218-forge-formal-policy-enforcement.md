---
type: source-summary
title: "Formal Policy Enforcement for Real-World Agentic Systems"
source_raw:
  - "[[20260218-forge-formal-policy-enforcement]]"
canonical_url: "https://arxiv.org/abs/2602.16708"
raw_state: full
source_locator:
  - "Datalog policy + provenance substrate + reference monitor at action join points"
  - "assume/guarantee correctness under an explicit environment contract"
  - "controlled case studies: 5/5→0/5 prompt-injection success, 58%→98% tau2 compliance, 40→0 unauthorized FDA accesses"
created: 2026-09-20
updated: 2026-09-20
tags:
  - source-summary
  - agent-security
  - verification
evidence_level: medium
claim_type: mixed
---

# Formal Policy Enforcement for Real-World Agentic Systems

## 编译摘要

### 1. 浓缩

- **核心结论 1：reference monitor 可以把 policy enforcement 从 Agent 推理中剥离。**
  - FORGE 用 Datalog 描述策略，observability/provenance substrate 提供执行事实，reference monitor 在 policy-relevant action join point 前执行 Allow/Deny。
- **核心结论 2：形式保证是带前提的 assume/guarantee，而不是“系统天然安全”。**
  - 当 environment contract 成立、策略需要的事实 sound/sufficient 且相关动作都经过插装点时，作者证明 runtime decision 与 policy semantics 一致。
- **核心结论 3：受控任务显示 action-boundary enforcement 能消除被策略覆盖的违规，但 recovery 仍由模型承担。**
  - 作者报告 prompt-injection 5/5→0/5、tau2-bench compliance 58%→98%、MALADE 未授权 FDA access 40→0；同时明确被阻断后的 retry/recovery 可能因模型推理失败。

### 2. 质疑

- raw socket、stdio 和其他未插装通道不受 reference monitor 保证；action-surface coverage 是 guarantee 的前置条件。
- 方法内部并发可能让 authorization query 看到不完整的 substrate state。
- 自然语言到 Datalog 的策略仍由 LLM 翻译并人工复核；形式化执行不等于策略生成过程无误。
- 论文没有覆盖 revoke-after-send、unknown commit、compensation 或 provider-authoritative post-state reconciliation。

### 3. 对标

- 对 EX-005：补强 **independent execution point**：policy verdict 在 action join point 由 reference monitor 执行，而不是依赖模型自我遵守。
- 对 [[Agent-Security]]：安全声明必须绑定 policy → observed provenance → instrumented surface → decision → action，并显式记录未插装通道与 recovery failure。
- 对 EX-006：FORGE 的 environment contract 是 control-state soundness/sufficiency 的具体形式，但它仍假设 deployment substrate 可信，不能独立证明 authority provenance 或外部 effect 已恢复。

## 关联概念

- [[Agent-Security]]
- [[Verifiable-Agent-Engineering]]
- [[Least-Agency]]
- [[Agent-Containment]]
