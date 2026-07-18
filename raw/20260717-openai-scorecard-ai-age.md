---
type: raw
source: "https://openai.com/index/a-scorecard-for-the-ai-age/"
author:
  - "Sarah Friar"
published: "2026-07-17"
created: "2026-07-18"
tags:
  - clippings
  - token-efficiency
  - enterprise
  - AI-economics
---

# A scorecard for the AI age | OpenAI

## Core Framework: Useful Intelligence per Dollar

OpenAI CFO Sarah Friar proposes a four-question scorecard for measuring AI value, centered on "Useful Intelligence per Dollar":

1. **How much useful work gets done?** — Tokens create value when they transform into work people can use. Start with one workflow, define "done", and measure that outcome in the system where the work happens.
2. **What does a successful task actually cost?** — Cost per successful task = (full cost of completing work) / (tasks that met the quality bar). The lowest price per token does NOT always produce the lowest cost per outcome. A frontier model may deliver best value even for routine tasks if it produces the right answer in one pass.
3. **How often does AI get the work right?** — Dependability = ready-to-use vs needs-correction vs needs-escalation rates. Before AI moves from drafting to taking action, organizations should define data access boundaries, system permissions, and human review thresholds.
4. **Does each AI dollar buy more work as usage grows?** — Track the same workflow over time. If completed work grows faster than total cost while quality holds or improves, each AI dollar produces more value.

## Key Data

- GPT-5.6 Sol with max reasoning: 72.7% on DeepSWE v1.1 (long-horizon engineering tasks), above Claude Fable 5's 69.9%, at **36.2% lower** estimated API cost
- GPT-5.6 Sol used 54% fewer output tokens than another leading model on the Artificial Analysis Coding Agent Index while setting a new state of the art

## Economics Insight

"Compute sits at the center of this equation": Better models, more efficient inference, purpose-built hardware, higher utilization, smarter routing, and stronger product design all improve the return on compute. The gains compound: better infrastructure → better research → more capable models → better products → drive adoption → support continued investment.

## Enterprise Context

ChatGPT Work builds on ChatGPT Enterprise security/compliance/workspace-management. Three action-readiness tiers: ready-to-use (met quality bar as delivered), needs-correction (required another attempt or human edits), needs-escalation (person needed to step in).

## Relevance to Knowledge Base

- Directly aligns with "架构质量=Token效率" and Token FinOps: cost-per-successful-task not cost-per-token
- Overlaps with Delegative UI: AI moving from drafting → taking action, with people providing judgment
- Connects to 多模型策略: tiered model family (Sol/Terra/Luna) for routing optimization
- Provides empirical data for Token FinOps pricing transparency (GPT-5.6 54% fewer output tokens, 36.2% lower cost)
