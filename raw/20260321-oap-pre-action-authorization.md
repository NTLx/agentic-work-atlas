---
type: raw
title: "Before the Tool Call: Deterministic Pre-Action Authorization for Autonomous AI Agents"
source: "https://arxiv.org/abs/2603.20953"
author:
  - "Uchi Uchibeke"
published: "2026-03-21"
created: "2026-09-20"
description: "Open Agent Passport 在 tool call 前同步执行 capability/policy 检查并签发审计记录；作者报告 1,151 sessions / 4,437 decisions 的 CTF 与约 53 ms 云端授权中位延迟，但实验、平台信任和覆盖面均有明确边界。"
tags:
  - clippings
  - agent-security
  - verification
---

# Before the Tool Call: Deterministic Pre-Action Authorization for Autonomous AI Agents

> Canonical source: https://arxiv.org/abs/2603.20953

## Source locator

- OAP intercepts each tool call synchronously before execution, evaluates a declarative policy, and returns ALLOW / DENY / ESCALATE with a signed decision record.
- Author-reported live testbed: 1,151 sessions and 4,437 authorization decisions; permissive condition reports 74.6% success, while the restrictive highest tier reports 0/879 successful breaches.
- Cloud API authorization benchmark reports about 53 ms p50 over N=1,000 per configuration, excluding client-side network round-trip.
- ESCALATE is specified but not implemented in the reference implementation.
- OAP evaluates calls at the tool boundary; direct output, retrieval, side channels and uninstrumented paths are out of scope, and per-call checks can miss aggregate/composability attacks.

## Evidence boundary

The CTF comparison is author-reported, single-domain and not a randomized controlled trial; participants and conditions are not a basis for a cross-domain causal estimate. OAP assumes the runtime hook and platform are trustworthy, and the implementation does not yet close multi-agent delegation or human escalation. The results support deterministic pre-action gating as a mechanism, not a claim of complete agent safety.
