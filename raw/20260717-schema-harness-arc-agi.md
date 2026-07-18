---
type: raw
source: "https://schema-harness.github.io/"
author:
  - "Schema Team"
published: "2026-07-17"
created: "2026-07-18"
tags:
  - clippings
  - agentic-engineering
  - agent-harness
  - AI-Agent
  - benchmark
---

# Frontier Models with Our Harness Achieve ~99% on ARC-AGI-3 Public — Schema

## Overview

Schema is a harness that reaches 99% on the ARC-AGI-3 Public set using Claude Opus 4.8 and Fable 5, and 95.35% using GPT-5.6 Sol. It does not change the underlying model weights. Instead, it changes the process around them: how observations are turned into a working model of the game, how predictions are tested against the interaction history, and how plans are executed and revised.

## ARC-AGI-3

ARC-AGI-3 gives an agent a game environment, without an explanation of what it is seeing. At each step, the agent receives a 64×64 grid of 16 color indices and a set of legal actions. The environment supplies no object list, rule sheet, stated goal, or shaped reward.

Its official metric, Relative Human Action Efficiency (RHAE), compares an agent's per-level action count with a first-exposure human baseline. 100% means completing every level at or above human-baseline action efficiency. On the Semi-private set, frontier-model performance rose from 0.51% at launch in March to 7.78% with GPT-5.6 Sol in July. Schema reaches ~99% on Public.

## Key Innovation: Two-Level Joint Reasoning

Schema formalizes intelligence as two problems solved jointly:

1. **State Grounding (Level 1)**: Turn raw observations into objects, variables, and relations that can be tracked. (Earlier system: VIGA)
2. **Mechanism Discovery (Level 2)**: Find how state changes under an action and write the rule as an executable program. (Earlier system: WorldCoder)

Schema's key insight: these two problems cannot be resolved independently. A state representation may prove inadequate when no consistent transition rule can explain subsequent experiments. In Schema, the state representation and transition rules are jointly encoded in the same editable program. When an observation contradicts a prediction, the agent can revise both its state model and its transition rules simultaneously.

## Takeaway

"How you use the model matters a lot." The harness changed the process around the models without touching their weights — achieving a ~14× improvement over the same models without the harness.
