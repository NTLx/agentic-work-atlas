---
type: source-summary
title: "Governance Decay: How Context Compaction Silently Erases Safety Constraints in Long-Horizon LLM Agents"
source_raw:
  - "[[20260621-governance-decay-constraintrot]]"
canonical_url: "https://arxiv.org/abs/2606.22528"
raw_state: full
source_locator:
  - "1,323 episodes across seven model families"
  - "0% full-context vs 30% post-compaction violation; 38% when constraint omitted"
  - "Constraint Pinning restores 0% violation in benchmark; provenance/authenticity remains separate"
created: 2026-09-19
updated: 2026-09-19
tags:
  - source-summary
  - agent-security
  - verification
evidence_level: medium
claim_type: mixed
---

# Governance Decay: How Context Compaction Silently Erases Safety Constraints in Long-Horizon LLM Agents

## 编译摘要

### 1. 浓缩

- **核心结论 1：context compaction 是治理状态的独立失效面。**
  - 关键证据：1,323 episodes 中，完整上下文约束条件违规为 0%，compaction 后总体升到 30%，部分模型达 59%。
- **核心结论 2：是否保留约束与违规之间存在强关联。**
  - 关键证据：约束保留时报告 0% 违规，约束被 summary 丢弃时为 38%。
- **核心结论 3：把约束从有损压缩中隔离可以修复该失效面。**
  - 关键证据：Constraint Pinning 在该 benchmark 中把违规恢复为 0%。

### 2. 质疑

- Pinning 保证“留住文本”，不自动保证 issuer/authenticity；恶意伪装成 operator 的控制状态是另一问题。
- benchmark 的 0% 不等于所有模型、所有压缩器、所有长程任务中的普遍保证。
- compaction-induced violation 仍需与真实 external effect / recovery 连接。

### 3. 对标

- 对 EX-006：证明 carrier survival 本身是独立变量，但也说明 survival ≠ provenance authenticity。
- 对 [[20260502-ghost-in-context-policy-carriage-integrity]]：前者测 compaction decay，后者把 presence / soundness / binding 形式化，二者共同支持“决策时控制状态完整性”。
- 对 [[Agent-Security]]：控制面不能只依赖与普通 workload 共用的有损 token stream。

## 关联概念

- [[Agent-Security]]
- [[Policy-as-Code-for-Agent-Governance]]
- [[Context-Collapse]]
- [[Agent-Containment]]
