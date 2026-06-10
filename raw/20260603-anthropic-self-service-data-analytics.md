---
type: raw
source: "https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude"
author:
  - "Chen Chang"
  - "Clement Peng"
  - "Justin Leder"
  - "Johanne Jiao"
  - "Josh Cherry"
published: "2026-06-03"
created: "2026-06-10"
tags:
  - clippings
  - data-analytics
  - agentic-analytics
  - semantic-layer
---

# How Anthropic enables self-service data analytics with Claude

At Anthropic, 95% of business analytics queries are automated via Claude, with ~95% accuracy in aggregate. By giving this often rote, repetitive work to Claude, our data science team can focus on more strategic work like causal modeling, forecasting, and machine learning.

**The Problem: Data is not software**
LLMs' generative abilities are a double-edged sword. For analytics use cases, there's often only a single correct answer using a single correct source. We've identified three failure modes:
1.  **Concept <> entity ambiguity:** The agent is unable to choose the correct fields (e.g., what defines an "active user"?).
2.  **Data staleness:** Sources and schemas change constantly.
3.  **Retrieval failure:** The agent simply doesn't find the right information in a vast search space.

**The Solution: Our agentic analytics stack**
1.  **Data foundations:** Creating canonical datasets and enforcing standards through CI and metadata.
2.  **Sources of truth:** Leveraging a semantic layer, lineage graphs, and business context.
3.  **Skills:** Procedural knowledge encoded in markdown that tells the agent how to navigate the data.
4.  **Validation:** Using offline evals and adversarial review to ensure accuracy.
