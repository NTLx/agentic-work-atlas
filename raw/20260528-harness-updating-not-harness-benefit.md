---
type: raw
title: "Harness Updating Is Not Harness Benefit: Disentangling Evolution Capabilities in Self-Evolving LLM Agents"
source: "https://arxiv.org/abs/2605.30621"
author:
  - "Minhua Lin"
  - "Juncheng Wu"
  - "Zijun Wang"
  - "Zhan Shi"
  - "Yisi Sang"
  - "Bing He"
  - "Zewen Liu"
  - "Tianxin Wei"
  - "Zongyu Wu"
  - "Zhiwei Zhang"
  - "Dakuo Wang"
  - "Xiang Zhang"
  - "Benoit Dumoulin"
  - "Cihang Xie"
  - "Yuyin Zhou"
  - "Suhang Wang"
  - "Hanqing Lu"
published: "2026-05-28"
created: "2026-09-19"
description: "将 harness-updating 与 harness-benefit 分成两个能力轴，显示能写出有用更新与执行 Agent 能调用、遵循并从更新获益并不是同一能力。"
tags:
  - clippings
  - verification
  - agent-evaluation
---

# Harness Updating Is Not Harness Benefit

> Canonical source: https://arxiv.org/abs/2605.30621

## Source locator

- Defines harness-updating: producing useful persistent harness updates from execution evidence.
- Defines harness-benefit: the task-solving agent actually benefiting from updated harnesses.
- Crosses evolver and task-solving model roles rather than treating an end-to-end gain as one capability.
- Across the reported settings, harness-updating is comparatively flat across base-capability tiers; the paper reports at most a 3.1 percentage-point evolver gain difference within any benchmark.
- Harness-benefit is non-monotonic: weak-tier models benefit little, mid-tier models most, and stronger models less than the mid tier.
- SkillsBench analysis separates harness activation from harness adherence; reported Qwen3-32B rates are 0.251 / 0.142 and Claude Opus 4.6 rates 0.957 / 0.757.

## Evidence boundary

The experiments isolate updater and beneficiary roles more cleanly than end-to-end self-evolution scores, but remain benchmark studies. A useful update can still be unsafe, and activation/adherence metrics do not replace independent safety review or deployment rollback.
