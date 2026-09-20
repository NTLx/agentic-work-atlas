---
type: source-summary
title: "Rethinking the Evaluation of Harness Evolution for Agents"
source_raw:
  - "[[20260827-rethinking-harness-evolution-evaluation]]"
canonical_url: "https://arxiv.org/abs/2607.12227"
raw_state: full
source_locator:
  - "matched feedback/inference budget against test-time search baselines"
  - "Terminal-Bench 2.1 pass@1/pass@5 comparisons"
  - "45 train / 10 validation / 34 held-out task generalization split"
created: 2026-09-19
updated: 2026-09-19
tags:
  - source-summary
  - verification
  - agent-evaluation
evidence_level: high
claim_type: mixed
---

# Rethinking the Evaluation of Harness Evolution for Agents

## 编译摘要

### 1. 浓缩

- **核心结论 1：harness evolution 是搜索过程，因此必须和搜索基线在相同预算下比较。**
  - 关键证据：论文把 parallel sampling、sequential refinement、harness scaling 与 harness evolution 放进 matched feedback/inference budget 对照。
- **核心结论 2：同 benchmark 上搜索出来的提升可能不是可复用 harness capability。**
  - 关键证据：在多个 Terminal-Bench 2.1 对照中，harness evolution 并未稳定优于简单 test-time scaling。
- **核心结论 3：held-out 泛化是能力归因的必要附加证据。**
  - 关键证据：45 train / 10 validation / 34 held-out tasks 中，两个 frontier model 的平均增益只有 0.6 个百分点。

### 2. 质疑

- 这是特定 benchmark、模型与方法的反例，不能外推为“harness evolution 无效”。
- matched compute 能排除一类搜索混淆，但不能排除 evaluator/reference 本身的问题。
- held-out task 增益低仍不回答生产环境中的 canary、safety regression 与 rollback。

### 3. 对标

- 对 EX-007：把 **search gain** 与 **persistent reusable capability delta** 强制拆开。
- 对 [[Verifiable-Agent-Engineering]]：candidate score 提升只有在 matched-search 与 disjoint held-out 后才更接近可归因改进。
- 对 [[Recursive-Self-Improvement]]：递归改进若反复查询同一 benchmark，可能只是把 test 变成 validation。

## 关联概念

- [[Recursive-Self-Improvement]]
- [[Verifiable-Agent-Engineering]]
- [[Meta-Harness-Optimization]]
- [[Agent-Harness]]
