---
type: source-summary
title: "Establishing Best Practices for Building Rigorous Agentic Benchmarks"
source_raw:
  - "[[20250703-agentic-benchmark-checklist]]"
canonical_url: "https://arxiv.org/abs/2507.02825"
raw_state: full
source_locator:
  - "task validity / outcome validity / benchmark reporting"
  - "semantic equivalence + GT correctness/isolation + Oracle solver"
  - "cross-benchmark flaw impact; CVE-Bench correction"
created: 2026-09-20
updated: 2026-09-20
tags:
  - source-summary
  - verification
  - agent-evaluation
evidence_level: high
claim_type: mixed
---

# Agentic Benchmark Checklist

## 编译摘要

### 1. Benchmark validity precedes model scoring

ABC treats the benchmark as a measurement system that must itself be audited:

~~~text
task validity
  ×
outcome validity
  ×
reporting / provenance
~~~

A high-quality grader cannot rescue a task whose allowed solutions, environment or reference are wrong.

### 2. Semantic equivalence is part of reference integrity

A reference should not encode one implementation path as the only truth when multiple outputs are functionally valid.

This makes reference truth broader than a static answer key.

### 3. Oracle/human checks are construction controls

Oracle solvers, human baselines and judge-human agreement are useful checks, but the framework does not imply that every evaluated run has an external oracle.

### 4. 对标

- 对 [[Verifiable-Agent-Engineering]]：expands reference truth into task/outcome validity.
- 对 [[Evaluation-Integrity]]：provides a reusable audit contract rather than another leaderboard.

## 关联概念

- [[Verifiable-Agent-Engineering]]
- [[Evaluation-Integrity]]
