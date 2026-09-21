---
type: raw
title: "How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement"
source: "https://arxiv.org/abs/2607.13718"
author:
  - "Alexandra E. Michael"
  - "Franziska Roesner"
published: "2026-07-15"
created: "2026-09-20"
description: "对 21 个 Agent 权限系统与 5 个商业 Agent 的调查，将用户权限拆成 specification、derivation 与 runtime enforcement，并指出持续修改/撤销与用户负担的独立缺口。"
tags:
  - clippings
  - agent-security
  - verification
---

# How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement

> Canonical source: https://arxiv.org/abs/2607.13718

## Source locator

- Survey covers 21 agent-permissions proposals/systems and walkthroughs of five commercial agents.
- Taxonomy separates user-facing/internal policy specification, derivation from user input, and run-time enforcement.
- 12/21 surveyed systems use deterministic non-AI enforcement mechanisms; none of the surveyed proposals simultaneously achieve low user overhead, formally grounded specifications, and deterministic enforcement.
- Only six surveyed systems clearly support changing or revoking permissions after initial specification; some only permit changes between sessions.
- Commercial walkthroughs show a recurring trade-off between frequent user confirmation and less-transparent LLM auto-review.

## Evidence boundary

This is a survey plus closed-source product walkthrough, not a controlled causal safety experiment. Product behavior was observed in late May and early June 2026 and can change. The paper supports separating permission specification, derivation, enforcement, transparency and continued user control; it does not establish the safety effect of any single architecture or prove that deterministic enforcement is sufficient.
