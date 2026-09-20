---
type: source-summary
title: "τ³-Bench: Fixing Airline + Retail"
source_raw:
  - "[[202602-tau3-task-fixes]]"
canonical_url: "https://taubench.com/blog/tau3-task-fixes.html"
raw_state: full
source_locator:
  - "27 airline + 26 retail task fixes"
  - "expected-action / ambiguity / constraint / fallback / loophole repairs"
  - "airline pass^1 +14–20pp; selected pass^4 +22pp example"
created: 2026-09-20
updated: 2026-09-20
tags:
  - source-summary
  - verification
  - agent-evaluation
evidence_level: high
claim_type: mixed
---

# τ³ task-reference fixes

## 编译摘要

### 1. Wrong expected actions can make correct behavior score as failure

The official audit documents tasks whose expected actions contradicted the domain policy or available tools.

This is direct benchmark-maintenance evidence that a false negative can originate in the reference contract, not the agent.

### 2. Task validity and reference validity interact

Other fixes changed ambiguity, impossible constraints, fallback behavior and policy loopholes.

Therefore the before/after score shift cannot be attributed only to a corrected answer key.

### 3. Versioning matters

A benchmark score without task/evaluator version can become uninterpretable after task definitions change.

The minimum comparison identity should therefore bind:

~~~text
benchmark version
  + task id
  + policy / environment version
  + evaluator / expected-action version
  + model / trial
~~~

### 4. 对标

- 对 [[Verifiable-Agent-Engineering]]：reference truth needs versioned task/policy lineage.
- 对 [[Evaluation-Integrity]]：benchmark maintenance can materially change measured capability without changing the model.

## 关联概念

- [[Verifiable-Agent-Engineering]]
- [[Evaluation-Integrity]]
