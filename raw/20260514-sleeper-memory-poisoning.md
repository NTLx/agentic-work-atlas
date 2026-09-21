---
type: raw
title: "Hidden in Memory: Sleeper Memory Poisoning in LLM Agents"
source: "https://arxiv.org/abs/2605.15338"
author:
  - "Sidharth Pulipaka"
  - "Stanislau Hlebik"
  - "Leonidas Raghav"
  - "Sahar Abdelnabi"
  - "Vyas Raina"
  - "Ivaxi Sheth"
  - "Mario Fritz"
published: "2026-05-14"
created: "2026-09-20"
description: "持久记忆可把恶意外部内容跨会话保存并在未来任务中重新触发：论文完整测量 write → retrieve → use 链，成功检索后的攻击者意图 agentic action 在不同模型/设置中达到 60–89%。"
tags:
  - clippings
  - agent-security
  - verification
---

# Hidden in Memory: Sleeper Memory Poisoning in LLM Agents

> Canonical source: https://arxiv.org/abs/2605.15338
> Accessed: 2026-09-20.

## Source locator

- Threat model: adversarial document, webpage or repository causes a stateful assistant to store a fabricated user memory that survives into later independent conversations.
- Evaluation separates the full pipeline into poisoned-memory write, later retrieval, and downstream behavioral use.
- Reported memory-addition rate reaches 99.8% on GPT-5.5 and 95% on Kimi-K2.6.
- Conditional on successful retrieval, attacker-intended agentic actions occur in 60–89% of evaluations across models/settings.
- Post-injection evaluation removes the original malicious content and tests later sessions/workspaces, isolating persistent-memory carryover from immediate prompt injection.

## Evidence boundary

The study demonstrates a persistent-memory attack channel, not a universal compromise rate for all memory systems. Provider-specific memory pipelines are only partly observable, and the evaluated defenses do not establish a complete trusted editing lifecycle for provenance-aware write, correction, revocation, deletion and user review. The result supports treating memory write/retrieve/use as separate security stages; it does not show that every poisoned write is later retrieved or acted upon.
