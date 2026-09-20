---
type: source-summary
title: "Separating signal from noise in coding evaluations"
source_raw:
  - "[[20260708-openai-swe-bench-pro-audit]]"
canonical_url: "https://openai.com/index/separating-signal-from-noise-coding-evaluations/"
raw_state: full
source_locator:
  - "731 tasks → 286 flagged"
  - "agent audit 200 / human audit 249; five engineers per flagged task"
  - "strict / underspecified / low-coverage / misleading prompt taxonomy"
created: 2026-09-20
updated: 2026-09-20
tags:
  - source-summary
  - verification
  - agent-evaluation
evidence_level: high
claim_type: mixed
---

# OpenAI SWE-Bench Pro audit

## 编译摘要

### 1. Coding benchmark quality is itself an evaluation problem

The audit pipeline separately inspects task prompt, tests, gold patch, model attempts and repository/environment context.

This makes the evaluation target explicit: a model failure should reflect capability failure, not a broken measurement instrument.

### 2. Agent audit and human audit are complementary, not interchangeable

The agent pipeline found 200 breaking tasks; the five-engineer campaign found 249. Human reviewers more often identified overlapping categories and low-coverage tests.

That supports using automated audit to scale inspection while retaining an independent human adjudication layer for benchmark construction.

### 3. Preserve the denominator

The source reports 200/249 findings as 27.4%/34.1% of all 731 tasks, but deep review was concentrated on the 286 tasks flagged by the initial screen.

The safe interpretation is therefore audit result under this selection pipeline, not an unbiased prevalence estimate for every unseen task.

### 4. 对标

- 对 [[Verifiable-Agent-Engineering]]：reference/specification correctness belongs inside the truth gate.
- 对 [[Evaluation-Integrity]]：the benchmark itself needs provenance, review and versioning.

## 关联概念

- [[Verifiable-Agent-Engineering]]
- [[Evaluation-Integrity]]
