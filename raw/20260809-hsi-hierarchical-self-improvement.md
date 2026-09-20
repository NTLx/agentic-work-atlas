---
type: raw
title: "Hierarchical Self-Improvement: A Framework for Task-Specific Evolvable Agent Harnesses"
source: "https://arxiv.org/abs/2608.08466"
author:
  - "Tailin Zhou"
published: "2026-08-09"
created: "2026-09-19"
description: "HSI 将 task harness、evolver strategy 与 frozen outer anchor 分层，研究固定 backbone 下 task-specific harness 的持续自演化及 held-out 泛化。"
tags:
  - clippings
  - verification
  - agent-evaluation
---

# Hierarchical Self-Improvement: A Framework for Task-Specific Evolvable Agent Harnesses

> Canonical source: https://arxiv.org/abs/2608.08466
> Code: https://github.com/TailinZhou/hsi

## Source locator

- A single frozen LLM operates across task-harness, evolver and meta-evolver scopes.
- Task harness and evolver strategy are editable at different layers; the outer meta-evolution execution logic remains frozen.
- Scope isolation rejects edits outside each layer's authorized surface.
- Thinking is disabled during task execution and enabled during self-modification to reduce task-time reasoning as a confound.
- Reported BALROG gains with DeepSeek-V4-Flash-Preview include +39.3 BabyAI, +33.0 Crafter, +25.0 TextWorld and +15.0 MiniHack raw progress.
- BabaIsAI uses a 20% unseen split; strong results are reported for BreakStop and GoTo, while other tasks remain much weaker.
- NLE shows no improvement, illustrating a backbone-capability bound.

## Evidence boundary

HSI provides a useful structural boundary between editable scopes and a frozen outer anchor. The scopes still share one frozen LLM, and the work does not establish an external safety evaluator, production policy approval, online canary or post-deployment rollback guarantee.
