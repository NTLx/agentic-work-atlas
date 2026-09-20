---
type: source-summary
title: "Are Solved Issues in SWE-bench Really Solved Correctly? An Empirical Study"
source_raw:
  - "[[20250319-patchdiff-swe-bench-correctness]]"
canonical_url: "https://arxiv.org/abs/2503.15223"
raw_state: full
source_locator:
  - "ICSE 2026 / SWE-bench Verified plausible patches"
  - "PatchDiff differential behavioral testing"
  - "7.8% test-validation miss; 29.6% behavioral divergence; 28.6% confirmed wrong among divergent; +6.2pp inflation"
created: 2026-09-20
updated: 2026-09-20
tags:
  - source-summary
  - verification
  - agent-evaluation
evidence_level: high
claim_type: mixed
---

# PatchDiff: test pass is not behavioral equivalence

## 编译摘要

### 1. Executable tests are necessary but not exhaustive

The study finds patches that pass SWE-bench's validation yet fail broader developer-written tests.

Therefore:

~~~text
benchmark tests pass
  ≠
behavioral correctness
~~~

### 2. Developer patch is useful as a differential reference, but not unique truth

PatchDiff finds 29.6% of plausible patches behave differently from the developer patch. Yet only a subset of divergent behavior is manually confirmed wrong.

So:

~~~text
behavior differs from developer patch
  ≠
automatically incorrect
~~~

The developer patch is a strong comparison anchor, not a complete semantic oracle.

### 3. Differential testing needs adjudication

PatchDiff's stable role is:

~~~text
test-pass candidate
  → differential behavior probe
  → discrepancy
  → semantic/manual adjudication
~~~

This adds a behavioral-equivalence layer between test execution and final reference truth.

### 4. 对标

- 对 [[Verifiable-Agent-Engineering]]：execution truth must not collapse into finite test-suite pass.
- 对 [[Evaluation-Integrity]]：a benchmark can overstate capability when tests under-specify behavior.

## 关联概念

- [[Verifiable-Agent-Engineering]]
- [[Evaluation-Integrity]]
