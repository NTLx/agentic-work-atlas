---
type: raw
title: "Turning Database Grading into RL Rewards: Post-Training Agents with ThinkingBox"
source: "https://huggingface.co/blog/microsoft/thinkingbox-training"
author:
  - "Tuhin Kundu"
  - "Microsoft"
published: 2026-10-22
created: 2026-10-28
description: "Bounded evidence clipping from the Microsoft/Hugging Face ThinkingBox training article. Full public source remains recoverable at the canonical URL."
language: en
tags:
  - "clippings"
---

# Turning Database Grading into RL Rewards: Post-Training Agents with ThinkingBox

Canonical source: https://huggingface.co/blog/microsoft/thinkingbox-training

## Evidence clipping

- ThinkingBox-Bench evaluates tool-using agents by comparing the final database state with the expected state, rather than trusting the agent's own completion claim.
- The authors reuse executable final-state checks from ThinkingBox-format tasks outside the benchmark as binary rewards for post-training.
- The reported experiment fine-tunes Qwen3.8-27B with GRPO for 50 steps. Across 507 benchmark tasks evaluated 20 times each, pass@1 rises from 51.70% to 60.78%, while observed 20/20 rises from 38 tasks to 107; pass@20 falls from 453 to 446 tasks.
- The authors interpret this as stronger repeatable success with a small loss in at-least-once coverage, making the reliability/coverage trade-off visible instead of collapsing performance into one score.
- One hotel-booking example tests whether the agent preserves booking/payment state when manager approval is required, illustrating that the oracle checks business-state invariants rather than surface-form answers.
- Training-task selection uses an offline estimate of policy-relative difficulty so the fixed training pool avoids tasks that are already trivial or effectively impossible for the base policy.

## Source locators

- Article opening / “What happened after training”: final-state grading and headline result.
- Table 1: Base vs RL-fine-tuned Qwen3.8-27B metrics.
- “What earns a reward” / training-loop sections: executable terminal-state checks as rewards.

## Evidence boundary

This is a Microsoft/Hugging Face first-party technical report about their own benchmark and training stack. The numeric gains are evidence for this specific model/task/training setup, not a general proof that database-state rewards improve every Agent or that GRPO universally increases reliability. The decline in pass@20 is a material counter-signal and must be preserved.