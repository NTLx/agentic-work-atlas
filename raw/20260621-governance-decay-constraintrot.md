---
type: raw
title: "Governance Decay: How Context Compaction Silently Erases Safety Constraints in Long-Horizon LLM Agents"
source: "https://arxiv.org/abs/2606.22528"
author:
  - "Shiyang Chen"
published: "2026-06-21"
created: "2026-09-19"
description: "ConstraintRot benchmark：上下文压缩可删除长期 Agent 的治理约束；Constraint Pinning 能在该 benchmark 中阻止普通 compaction decay，但仍存在 authority/impersonation 边界。"
tags:
  - clippings
  - agent-security
  - verification
---

# Governance Decay: How Context Compaction Silently Erases Safety Constraints in Long-Horizon LLM Agents

> Canonical source: https://arxiv.org/abs/2606.22528

## Source locator

- ConstraintRot evaluates long-horizon compaction-induced policy loss across seven model families.
- 1,323 episodes: violation increases from 0% with policy in full context to 30% after compaction, reaching 59% for some models.
- When the constraint survives the summary, violation remains 0%; when omitted, violation reaches 38%.
- Compaction-Eviction Attack biases the summarizer to omit legitimate policy and defeats all evaluated models in the reported optimized-injection condition.
- Constraint Pinning quarantines governance constraints from lossy compaction and restores violation to 0% in the benchmark.

## Evidence boundary

Constraint Pinning demonstrates protection against the studied compaction channel, not universal authority authenticity. A pinned but falsely introduced or impersonated policy still requires issuer/provenance validation outside ordinary token persistence.
