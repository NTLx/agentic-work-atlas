---
type: source-summary
title: "Why SWE-bench Verified no longer measures frontier coding capabilities"
source_raw:
  - "[[20260223-openai-swe-bench-verified-audit]]"
canonical_url: "https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/"
raw_state: full
source_locator:
  - "138 selected hard tasks / 64 o3 runs"
  - "at least six engineers per task + re-verification"
  - "59.4% material-issue rate inside the audited subset; contamination evidence"
created: 2026-09-20
updated: 2026-09-20
tags:
  - source-summary
  - verification
  - agent-evaluation
evidence_level: high
claim_type: mixed
---

# OpenAI SWE-bench Verified audit

## 编译摘要

### 1. Reference/test quality can dominate the remaining failures

OpenAI's audit found material prompt/test issues in 59.4% of the selected 138-task subset that o3 failed to solve consistently over 64 runs.

The relevant unit is therefore:

~~~text
selected hard-task subset
  → expert specification/test audit
  → benchmark-quality judgment
~~~

not the full 500-task benchmark.

### 2. Independent human review improves benchmark construction, not run-level truth

At least six engineers independently reviewed each selected task, with additional re-verification for flagged issues.

This is strong evidence that benchmark reference/test quality itself requires an oracle-audit layer. It is not evidence that every model run received an independent external verdict.

### 3. Contamination and reference validity are different failure modes

The same post reports models reproducing gold-patch/problem details for some tasks.

Therefore:

~~~text
bad tests / bad specification
        ≠
training contamination
~~~

Both can corrupt a score, but by different causal paths.

### 4. 对标

- 对 [[Verifiable-Agent-Engineering]]：reference truth 必须与 execution truth 分开。
- 对 [[Evaluation-Integrity]]：benchmark contamination and benchmark validity are distinct integrity dimensions.

## 关联概念

- [[Verifiable-Agent-Engineering]]
- [[Evaluation-Integrity]]
