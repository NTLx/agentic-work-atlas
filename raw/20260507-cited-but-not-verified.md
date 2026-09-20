---
type: raw
title: "Cited but Not Verified: Parsing and Evaluating Source Attribution in LLM Deep Research Agents"
source: "https://arxiv.org/abs/2605.06635"
author:
  - "Hailey Onweller"
  - "Elias Lumer"
  - "Austin Huber"
  - "Pia Ramchandani"
  - "Vamse Kumar Subbiah"
  - "Corey Feld"
published: "2026-05-07"
created: "2026-09-19"
description: "以 AST parser 回收并验证 deep research 报告中的 citation；把 Link Works、Relevant Content、Fact Check 分开，并做 2→150 tool calls 的 research-depth ablation。"
tags:
  - clippings
  - verification
  - agent-evaluation
---

# Cited but Not Verified: Parsing and Evaluating Source Attribution in LLM Deep Research Agents

> Canonical source: https://arxiv.org/abs/2605.06635

## Source locator

- 14 closed- and open-source LLMs.
- Three citation dimensions: Link Works, Relevant Content, Fact Check.
- Rubric-based LLM evaluators calibrated through human review.
- Frontier models maintain link validity above 94% and relevance above 80%, while factual attribution accuracy spans roughly 39–77%.
- Research-depth ablation scales tool calls from 2 to 150 on two frontier models; Fact Check accuracy drops by about 42% on average while surface citation metrics remain much stronger.

## Evidence boundary

The paper studies source attribution in deep-research report generation, not environment-state verification. The depth ablation changes total research process complexity together with retrieved information volume, so the decline supports an evidence-synthesis interference hypothesis but does not identify a unique causal mechanism such as context length or attention dilution.
