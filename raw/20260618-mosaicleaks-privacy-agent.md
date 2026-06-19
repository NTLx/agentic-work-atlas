---
type: raw
source: "https://huggingface.co/blog/ServiceNow/mosaicleaks"
author:
  - "Alexander Gurung"
  - "ServiceNow"
  - "Rafael Pardinas"
published: "2026-06-18"
created: "2026-06-18"
tags:
  - clippings
  - agent-safety
  - privacy
  - deep-research
  - RL
  - data-leakage
---

# MosaicLeaks: Can your research agent keep a secret?

Deep research agents increasingly combine private local documents with external tools like web retrieval, creating a privacy risk: an agent's external queries may leak sensitive information.

## TL;DR

MosaicLeaks proposes a new deep-research task with multi-hop questions that interleave public and private information. Across the models tested, agents frequently leaked private information, and training only for task performance made it worse. The proposed PA-DR (Privacy-Aware Deep Research) training method raises strict chain success from 48.7% to 58.7% while reducing answer/full-information leakage from 34.0% to 9.9%.

## Privacy Leakage in Deep-Research Agents

A research agent at a healthcare firm fires off ordinary-looking web searches. No single query gives away the whole secret. But anyone watching the agent's outbound traffic can reassemble the fragments: this is the mosaic effect.

MosaicLeaks treats web queries as the leakage channel: the adversary never sees the private documents or the agent's reasoning, only the cumulative query log.

Three leakage types:
- **Intent leakage**: adversary infers the private research questions from the query log
- **Answer leakage**: query log plus a question about private information enables answering without seeing documents
- **Full-information leakage**: adversary can state verifiably true private claims without being told what to look for

## Building MosaicLeaks

1,001 multi-hop research chains over local enterprise documents and a controlled web corpus. Each chain interleaves local and web sub-questions, creating explicit local-web dependencies.

Split: 559 training chains, 98 validation chains, 344 held-out-company test chains.

## Agent Harness

Simplified harness adapted from DRBench. Four tools at each iteration:
- **Plan**: produces local and web search queries
- **Choose**: selects which retrieved documents to read
- **Read**: attempts to answer the current hop
- **Resolve**: decides whether to answer, read more, or plan another search

## Can't you just tell the agent not to leak?

Adding a privacy-aware prompt helps slightly but inconsistently. For Qwen3-4B, the prompt lowers leakage from 34.0% to 25.5%, but strict chain success drops from 48.7% to 44.5%. The primary behavioral change is fewer web queries, not consistently safer query construction.

## Making the agent better made it leak more

Training only for task performance: strict chain success rises from 48.7% to 59.3%, but answer/full-information leakage climbs from 34.0% to 51.7%. The model learns to pack more context into web queries, helping retrieval but hurting privacy.

This is the central tension: a more informative query is often better for the task and worse for privacy.

## Teaching the agent to search safely: PA-DR

PA-DR combines two rewards:

1. **Situational task reward**: judges each call against other calls at the same stage and hop, with the same information available. Much more precise credit assignment.

2. **Learned privacy reward**: a Qwen3-4B classifier estimates whether current queries leak private information directly or create a new mosaic leak. PA-DR penalizes the larger of the two.

| Method | Strict chain success | Answer/full-info leakage |
|--------|---------------------|------------------------|
| Base Qwen3-4B | 48.7% | 34.0% |
| Task reward only | 59.3% | 51.7% |
| Task + PA-DR reward | 58.7% | 9.9% |

PA-DR issues more web queries than the base model, but those queries drop the revealing details. The agent still finds the right public documents but stops carrying private fragments in the query text.

## Sample efficiency

Situational rewards reach outcome-reward-level task success using roughly 5-6x fewer generated training samples. PA-DR keeps that efficiency while adding the privacy gain.

| Training reward | Generated samples | Strict success | Leakage | Samples to 55% success |
|----------------|------------------|----------------|---------|----------------------|
| Outcome reward | 963k | 55.4% | 49.0% | 963k |
| Situational task reward | 842k | 59.3% | 51.7% | 146k |
| Task + PA-DR reward | 706k | 58.7% | 9.9% | 183k |

## What this does and doesn't show

MosaicLeaks is a controlled benchmark, not a measurement of deployed systems. Enterprise documents are synthetic, web corpus is fixed, chains span three company contexts.

The takeaway: you can't prompt privacy in. You have to train it in. Rewarding how the agent constructs each query cuts leakage by more than 3x while leaving task success essentially intact.
