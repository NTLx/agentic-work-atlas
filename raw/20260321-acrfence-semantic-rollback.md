---
type: raw
title: "ACRFence: Preventing Semantic Rollback Attacks in Agent Checkpoint-Restore"
source: "https://arxiv.org/abs/2603.20625"
author:
  - "Yusheng Zheng"
  - "Yiwei Yang"
  - "Wei Zhang"
  - "Andi Quinn"
published: "2026-03-21"
created: "2026-09-19"
description: "Checkpoint-restore 不能撤销已提交到外部系统的副作用；LLM 恢复后重新生成不同请求可绕过传统幂等假设。"
tags:
  - clippings
  - agent-security
  - verification
---

# ACRFence: Preventing Semantic Rollback Attacks in Agent Checkpoint-Restore

> Canonical source: https://arxiv.org/abs/2603.20625

## Source locator

- Two attack classes: Action Replay and Authority Resurrection.
- 10/10 checkpoint-restore trials produced duplicate commits; no-checkpoint baseline produced 0/10.
- Stateless single-use-token reuse succeeded 2/2; stateful validation rejected all tested reuse attempts.
- Root cause: local checkpoint restore cannot undo external effects already committed to another service.
- Proposed ACRFence records irreversible effects and applies replay-or-fork semantics at the tool boundary.

## Evidence boundary

The paper experimentally validates the attacks, but explicitly states that the proposed ACRFence implementation itself was not yet evaluated. Its analyzer LLM introduces additional classification/evasion risks. The result supports an output-commit boundary, not a claim that ACRFence has already solved production rollback.
