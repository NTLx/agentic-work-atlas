---
type: raw
title: "Ghost in the Context: Policy-Carriage Integrity in LLM Agents"
source: "https://arxiv.org/abs/2605.12535"
author:
  - "Igor Santos-Grueiro"
published: "2026-05-02"
created: "2026-09-19"
description: "研究 policy-carriage integrity：适用策略在动作前决策状态中必须仍然存在、语义健全并正确绑定；提出 ControlCapsule 参考模式。"
tags:
  - clippings
  - agent-security
  - verification
---

# Ghost in the Context: Policy-Carriage Integrity in LLM Agents

> Canonical source: https://arxiv.org/abs/2605.12535
> Version used: v3, revised 2026-07-01.

## Source locator

- Defines policy-carriage integrity as presence, semantic soundness and correct binding of applicable trusted policy in the decision state immediately before action.
- Controlled pressure replay uses AutoGen/tau3 and OpenHands/SWE-bench traces.
- Protected-placement configurations preserve policy across the tested pressure sweep; task-local placement shows eviction, weakening or over-budget continuation depending on context manager.
- Behavioral calibration reports 0/90 unsafe-action proposals and 0/90 unguarded policy violations despite state-level policy loss.
- Design guidance: typed provenance, isolated control budget, fit preflight, fail closed on overload, action-boundary enforcement.
- ControlCapsule is presented as a reference pattern; exact active-policy replay + preflight remains the key baseline.

## Evidence boundary

The strongest result is state-level policy-carriage integrity, not a demonstrated reduction in harmful external actions. The paper explicitly keeps the 0/90 behavioral result as a negative boundary: missing policy state alone did not prove unsafe model behavior.
