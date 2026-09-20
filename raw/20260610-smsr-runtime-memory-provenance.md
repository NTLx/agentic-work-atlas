---
type: raw
title: "SMSR: Certified Defence Against Runtime Memory Poisoning in Persistent LLM Agent Systems"
source: "https://arxiv.org/abs/2606.12703"
author:
  - "Tarun Sharma"
published: "2026-06-10"
created: "2026-09-19"
description: "Signed Memory with Smoothed Retrieval：在 memory write boundary 加 HMAC provenance，并用随机 memory ablation + verdict voting 约束 authenticated injection。"
tags:
  - clippings
  - agent-security
  - verification
---

# SMSR: Certified Defence Against Runtime Memory Poisoning in Persistent LLM Agent Systems

> Canonical source: https://arxiv.org/abs/2606.12703

## Source locator

- Threat: Multi-Session Memory Poisoning in persistent agent memory.
- Component 1: HMAC-SHA256 provenance at write time blocks unsigned injection.
- Component 2: randomized memory ablation plus verdict-based majority voting bounds influence of authenticated adversaries.
- 15 enterprise scenarios / 3,150 repeated trials.
- Unsigned variants: attack success reduced from 93–100% to 0% under Component 1.
- Single authenticated injection: Component 2 reports 8.0% success (95% CI 5.8–10.9, n=450).
- End-to-end query-only attack on a live agent stack: 65.3% to 5.3% (n=150).
- Clean-query utility: 90% for Component 1 and 85% combined.

## Evidence boundary

SMSR authenticates the memory write path and provides a certified retrieval-time robustness construction for the paper's threat model. It does not prove that authenticated writers are trustworthy, nor that signed memory remains correctly bound to later authority changes or external action post-state.
