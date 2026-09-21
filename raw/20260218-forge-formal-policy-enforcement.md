---
type: raw
title: "Formal Policy Enforcement for Real-World Agentic Systems"
source: "https://arxiv.org/abs/2602.16708"
author:
  - "Nils Palumbo"
  - "Sarthak Choudhary"
  - "Jihye Choi"
  - "Guy Amir"
  - "Prasad Chalasani"
  - "Somesh Jha"
published: "2026-02-18"
created: "2026-09-20"
description: "FORGE 用 Datalog policy、provenance/observability substrate 与 reference monitor 在 action join point 执行策略，并以 environment contract 给出 assume/guarantee 正确性；实验证明的是受插装执行面的合规，而非全系统安全或恢复。"
tags:
  - clippings
  - agent-security
  - verification
---

# Formal Policy Enforcement for Real-World Agentic Systems

> Canonical source: https://arxiv.org/abs/2602.16708

## Source locator

- Policies are expressed in Datalog; an observability service maintains execution/provenance predicates and a reference monitor mediates policy-relevant actions.
- Correctness is stated as an assume/guarantee theorem: when the deployment satisfies the environment contract, runtime decisions coincide with intended policy semantics.
- Reported case studies: prompt-injection attack success 5/5 to 0/5; tau2-bench compliance 58% to 98% across three frontier models; MALADE unauthorized FDA accesses 40 to 0, while task accuracy remains 15/15 in both MALADE conditions.
- End-to-end latency increases 19–38% in tau2-bench and MALADE; the paper attributes most overhead to blocked-action recovery/retry rather than authorization decision time.
- Guarantees cover only instrumented join points; raw sockets, stdio and other uninstrumented channels are outside scope, and intra-method concurrency can violate substrate completeness assumptions.

## Evidence boundary

FORGE guarantees policy compliance only under its environment contract and instrumented-surface assumptions. It does not guarantee that the policy is semantically correct, that recovery after a denial succeeds, or that already-committed external effects are reversible. Its natural-language-to-Datalog translation remains LLM-assisted and manually reviewed.
