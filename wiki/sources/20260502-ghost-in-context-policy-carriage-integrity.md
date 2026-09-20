---
type: source-summary
title: "Ghost in the Context: Policy-Carriage Integrity in LLM Agents"
source_raw:
  - "[[20260502-ghost-in-context-policy-carriage-integrity]]"
canonical_url: "https://arxiv.org/abs/2605.12535"
raw_state: full
source_locator:
  - "policy-carriage integrity definition: presence / soundness / correct binding before action"
  - "pressure replay across AutoGen/tau3 and OpenHands/SWE-bench traces"
  - "ControlCapsule guidance and exact replay + preflight baseline; 0/90 behavioral negative boundary"
created: 2026-09-19
updated: 2026-09-19
tags:
  - source-summary
  - agent-security
  - verification
evidence_level: medium
claim_type: mixed
---

# Ghost in the Context: Policy-Carriage Integrity in LLM Agents

## 编译摘要

### 1. 浓缩

- **核心结论 1：策略“曾经在上下文里”不等于策略在动作前仍然有效。**
  - 关键证据：论文把 policy carriage 拆成存在、语义健全、对象绑定，并在压力 replay 中观察到 task-local policy 的 eviction / weakening / over-budget continuation。
- **核心结论 2：控制状态需要独立预算与 preflight。**
  - 关键证据：作者建议 typed provenance、control-budget isolation、active-policy fit check、fail-closed overload 和 action-boundary enforcement。
- **核心结论 3：state failure 不能直接偷换成 behavioral harm。**
  - 关键证据：固定 assembler 行为校准中 0/90 unsafe-action proposals、0/90 unguarded policy violations。

### 2. 质疑

- ControlCapsule 是参考设计模式，不是已经证明优于 exact replay + preflight 的生产机制。
- state-level integrity 与 external-effect safety 尚未在同一实验中闭合。
- policy “存在且绑定正确”仍不保证 policy 本身正确或 verifier 判定正确。

### 3. 对标

- 对 EX-006：直接提供 carrier integrity × provenance binding × preflight 的实验和设计边界。
- 对 EX-005：只有 action-boundary enforcement 真正把 policy state 转化为外部行为约束；carriage 本身不是 actuation。
- 对 [[Agent-Security]]：policy owner 到 execution boundary 的链条必须有可检查的状态载体。

## 关联概念

- [[Agent-Security]]
- [[Policy-as-Code-for-Agent-Governance]]
- [[Agent-Containment]]
- [[Verifiable-Agent-Engineering]]
