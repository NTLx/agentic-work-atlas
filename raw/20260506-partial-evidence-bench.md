---
type: raw
title: "Partial Evidence Bench: Benchmarking Authorization-Limited Evidence in Agentic Systems"
source: "https://arxiv.org/abs/2605.05379"
author:
  - "Krti Tallam"
published: "2026-05-06"
created: "2026-09-19"
description: "72-task deterministic benchmark；把授权视图、完整答案、完整性判断和 gap report 分开，测量 agent 在证据不完整时是否误报完整。"
tags:
  - clippings
  - verification
  - agent-evaluation
---

# Partial Evidence Bench: Benchmarking Authorization-Limited Evidence in Agentic Systems

> Canonical source: https://arxiv.org/abs/2605.05379

## Source locator

- Three scenario families: due diligence, compliance audit, security incident response.
- 72 tasks with ACL-partitioned corpora.
- Separate oracles for complete answers, authorized-view answers, completeness judgments, and structured gap reports.
- Four evaluation surfaces: answer correctness, completeness awareness, gap-report quality, unsafe completeness behavior.
- Checked-in baselines: silent filtering is unsafe; explicit fail-and-report removes unsafe completeness in the shipped deterministic scenarios without reducing the task to blanket abstention.

## Evidence boundary

The benchmark uses deterministic synthetic corpora and preliminary real-model runs. It directly isolates authorization-limited evidence, but it does not by itself show how the same failure behaves under open-web retrieval, dynamic permissions, or different verifier families.
