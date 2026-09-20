---
type: raw
title: "An Empirical Analysis of Calibration and Selective Prediction in Multimodal Clinical Condition Classification"
source: "https://proceedings.mlr.press/v333/lopez26a.html"
author:
  - "L Julian Lechuga Lopez"
  - "Farah E Shamout"
  - "Tim G J Rudner"
published: "2026-06-29"
created: "2026-09-19"
description: "PMLR 333 / CHIL 2026：多模态 ICU 多标签任务中，聚合指标会掩盖类别依赖的误校准，uncertainty-based deferral 甚至可能降低表现。"
tags:
  - clippings
  - governance
  - verification
---

# An Empirical Analysis of Calibration and Selective Prediction in Multimodal Clinical Condition Classification

> Canonical source: https://proceedings.mlr.press/v333/lopez26a.html

## Source locator

- Published in PMLR 333, CHIL 2026.
- Evaluates uncertainty-based selective prediction for multimodal multilabel clinical condition classification using ICU data.
- Reports that selective prediction can substantially degrade performance despite strong aggregate evaluation metrics.
- Failure is driven by class-dependent miscalibration: some correct predictions receive high uncertainty while incorrect predictions receive low uncertainty, especially for underrepresented conditions.
- Aggregate metrics can obscure per-class failure behavior.

## Evidence boundary

This is a clinical classification benchmark, not an agentic handoff or human queue experiment. It supports a calibration warning: global confidence/coverage metrics can hide subgroup-specific deferral failure. It does not establish the same magnitude or direction in other domains.
