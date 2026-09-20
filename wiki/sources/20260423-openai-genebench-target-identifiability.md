---
type: source-summary
title: "GeneBench: Assessing AI Agents for Multi-Stage Inference Problems in Genomics and Quantitative Biology"
source_raw:
  - "[[20260423-openai-genebench-target-identifiability]]"
canonical_url: "https://cdn.openai.com/pdf/6dc7175d-d9e7-4b8d-96b8-48fe5798cd5b/oai_genebench_benchmark.pdf"
raw_state: full
source_locator:
  - "103 evaluations / 10 domains"
  - "agent-visible-data recoverable target"
  - "target-identifiability + trace/leakage/shortcut/prompt-grader audits"
created: 2026-09-20
updated: 2026-09-20
tags:
  - source-summary
  - verification
  - agent-evaluation
evidence_level: high
claim_type: mixed
---

# GeneBench target identifiability

## 编译摘要

### 1. A reference target must be recoverable from the allowed evidence

GeneBench deliberately grades a realized-data quantity that an agent can recover from visible files, rather than an inaccessible hidden DGP parameter.

This gives a concrete target-identifiability rule:

~~~text
authorized visible evidence
  → recoverable estimand
  → defensible reference
~~~

### 2. Reference integrity includes admissible analytical variation

The benchmark accepts reasonable analysis variants while using ablations to reject paths that omit necessary correction or choose the wrong phenotype/estimand.

So reference truth is not match one hidden implementation.

### 3. Construction review is not run-level verification

Scientific, methodological and target-identifiability reviews validate benchmark construction. They do not provide an independent verdict for every agent trajectory.

### 4. 对标

- 对 [[Verifiable-Agent-Engineering]]：adds target identifiability before reference scoring.
- 对 scientific Agent evaluation：the grader must not demand a quantity that the provided data cannot identify.

## 关联概念

- [[Verifiable-Agent-Engineering]]
