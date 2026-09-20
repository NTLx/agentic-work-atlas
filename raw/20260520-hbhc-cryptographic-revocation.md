---
type: raw
title: "Heartbeat-Bound Hierarchical Credentials: Cryptographic Revocation for AI Agent Swarms"
source: "https://arxiv.org/abs/2605.20704"
author:
  - "Saurabh Deochake"
published: "2026-05-20"
created: "2026-09-19"
description: "把子 Agent 凭据有效性绑定到父节点持续 heartbeat；在受控实验中给出确定性 zombie-window 上界与层级撤销结果。"
tags:
  - clippings
  - agent-security
  - verification
---

# Heartbeat-Bound Hierarchical Credentials: Cryptographic Revocation for AI Agent Swarms

> Canonical source: https://arxiv.org/abs/2605.20704

## Source locator

- Credential validity is bound to recent parent heartbeat proofs.
- Deterministic bound: W_z <= W_max + Delta_h + epsilon, under bounded clock skew and secure parent-key assumptions.
- Protocol evaluation reports 90x zombie-window reduction over OAuth 2.0, 0.26 ms full authentication, and 18,000+ verifications/s.
- LLM-backed swarm evaluation reports 0.71% tool-call overhead and zero post-revocation tool calls in the tested prompt-injection condition.
- Cascading revocation evaluated across a 49-agent, four-level hierarchy.

## Evidence boundary

HBHC bounds future credential use; it does not undo effects that were already accepted before credential expiry. Its guarantee depends on bounded clock skew, key protection, verifier enforcement and the tested hierarchy assumptions.
