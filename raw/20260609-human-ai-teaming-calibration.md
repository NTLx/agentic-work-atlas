---
type: raw
title: "Human-AI Teaming Through the Lens of Calibration"
source: "https://arxiv.org/abs/2606.10906"
author:
  - "Eric Nalisnick"
  - "Chi Zhang"
  - "Sophia Qian"
  - "Yixin Wang"
published: "2026-06-09"
created: "2026-09-19"
description: "把 human-AI delegation 的校准负担转移到 rejector；当人类使用系统不可见的额外特征时，路由存在不可约 excess risk。"
tags:
  - clippings
  - governance
  - verification
---

# Human-AI Teaming Through the Lens of Calibration

> Canonical source: https://arxiv.org/abs/2606.10906

## Source locator

- Studies human-AI teaming through statistical calibration.
- Delegation preserves downstream predictor calibration only if the rejector can identify where human vs model is superior.
- The rejector needs increasingly fine calibration as human expertise becomes more heterogeneous.
- When the human uses additional information unavailable to the system, the rejector cannot observe the features needed to perfectly route cases.
- Empirical evaluations include ImageNet-16H and HAM10000 conditions.

## Evidence boundary

This is a formal and empirical delegation result, not a production handoff study. It establishes an information-identifiability limit for routing: a facilitator cannot perfectly infer comparative human advantage from features it cannot observe. It does not prove that escalation is ineffective or that human-only context always dominates model evidence.
