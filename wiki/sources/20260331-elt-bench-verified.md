---
type: source-summary
title: "ELT-Bench-Verified: Benchmark Quality Issues Underestimate AI Agent Capabilities"
source_raw:
  - "[[20260331-elt-bench-verified]]"
canonical_url: "https://arxiv.org/abs/2603.29399"
raw_state: full
source_locator:
  - "100 tasks; 81 transformation-failure tasks audited"
  - "82.7% contain benchmark-attributable error"
  - "Fleiss kappa 0.851 / 0.755; 30 unreliable GT columns removed"
  - "same agent/model transformation success 22.66% → 32.51%"
created: 2026-09-20
updated: 2026-09-20
tags:
  - source-summary
  - verification
  - agent-evaluation
evidence_level: high
claim_type: mixed
---

# ELT-Bench-Verified

## 编译摘要

### 1. Evaluator/reference correction can change measured capability while agent output is held fixed

The audit isolates benchmark-side defects including rigid comparison logic, ambiguous specifications and incorrect ground truth.

After correcting evaluation logic and removing unreliable ground-truth columns, the same SWE-Agent + Claude Sonnet 4.5 setup moves from 22.66% to 32.51% transformation success.

This is direct evidence that:

~~~text
measured capability
  = f(agent output, reference, evaluator)
~~~

not agent output alone.

### 2. Human disagreement can imply that no authoritative replacement exists

For 30 suspect GT columns, three independent engineers achieved only 57.8% average pairwise exact-match agreement.

The correct response was removal, not majority-vote fabrication of a new answer key.

### 3. Semantic equivalence belongs in the evaluator contract

The verified evaluator normalizes booleans, floating-point tolerance, percentage/decimal formats, NULL representation and row order where order is unspecified.

Therefore a strict string/value representation match can create false failures even when transformation semantics are acceptable.

### 4. Corrected benchmark scores need version identity

A result should bind at least:

~~~text
task/spec version
  + GT/reference version
  + evaluator normalization rules
  + agent/model version
~~~

Otherwise pre/post-correction results can be mistaken for model progress or regression.

### 5. 对标

- 对 [[Verifiable-Agent-Engineering]]：directly strengthens versioned reference/evaluator contract.
- 对 [[Evaluation-Integrity]]：shows benchmark correction alone can materially change reported capability.

## 关联概念

- [[Verifiable-Agent-Engineering]]
- [[Evaluation-Integrity]]
