---
type: raw
title: "Success Is Not Self-Explanatory: Auditing Success Provenance in Agent Evaluation"
source: "https://arxiv.org/abs/2607.24054"
author:
  - "Jingkun Luo"
  - "Da-Tian Peng"
published: "2026-07-27"
created: "2026-09-19"
description: "AcquaBench 以 CLEAN/GOLD/SHAM matched value substitution 审计 agent success provenance，区分正确结果与因信息暴露而成功。"
tags:
  - clippings
  - verification
  - agent-evaluation
---

# Success Is Not Self-Explanatory: Auditing Success Provenance in Agent Evaluation

> Canonical source: https://arxiv.org/abs/2607.24054

## Source locator

- Introduces success provenance as a missing evaluation object when agents can alter their information state.
- AcquaBench uses matched CLEAN, GOLD, and SHAM value substitution across four standardized surfaces with qid-clustered analysis.
- CLEAN retains benchmark-authorized information.
- GOLD makes the correct target available.
- SHAM preserves source structure and exposure opportunity but substitutes a matched incorrect value.
- GOLD minus CLEAN estimates score response to correct-target availability.
- GOLD minus SHAM tests whether score response tracks target correctness beyond matched exposure.
- In D0, GOLD exceeds SHAM by 19.1–25.9 percentage points.
- In D2, GOLD still exceeds SHAM under distributed sufficiency; coloc ceases to transfer as a high-score marker (reported AUROC 0.376 and 0.142).
- A supported 5.0-point CLEAN model gap compresses to a raw GOLD difference of -0.6 points without establishing rank inversion.

## Evidence boundary

AcquaBench is a targeted causal-style benchmark of information-state interventions. It shows that observed task success can depend on target-value availability and that raw scores can distort model comparison. It does not establish that every benchmark exposure has the same effect, and its four standardized surfaces remain controlled evaluation environments.
