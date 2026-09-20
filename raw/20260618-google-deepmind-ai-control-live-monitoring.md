---
type: raw
title: "Securing the future of AI agents"
source: "https://deepmind.google/blog/securing-the-future-of-ai-agents/"
author:
  - "Rohin Shah"
  - "Four Flynn"
published: "2026-06-18"
created: "2026-09-19"
description: "Google DeepMind AI Control 官方博客：把 monitoring assurance 拆成 coverage、recall、time-to-response，并披露异步监控原型已分析约一百万 coding-agent tasks、用于 Gemini Spark live monitor。"
tags:
  - clippings
  - observability
  - agent-security
---

# Securing the future of AI agents

> Canonical source: https://deepmind.google/blog/securing-the-future-of-ai-agents/

## Source locator

- Introduces Google DeepMind's AI Control Roadmap for internally deployed agents.
- Monitoring is described as the backbone of AI control.
- Performance is framed with three metrics:
  - coverage — fraction of traffic monitored;
  - recall — fraction of misaligned behaviours caught;
  - time-to-response.
- Risk determines response mode:
  - low-risk / reversible behaviour can be handled asynchronously;
  - high-risk behaviour requires real-time synchronous prevention.
- Google reports an internal asynchronous-monitoring prototype that has analyzed about one million coding-agent tasks.
- Findings from that work are said to inform a live monitor for the Gemini Spark agent, including issues such as unintentional data deletion.
- Blog explicitly notes that most flagged events do not reflect adversarial intent; misinterpretation/overeagerness can generate similar observable behavior.

## Evidence boundary

The million-task figure establishes operational monitoring scale, not monitor accuracy. The blog does not publish deployment-level coverage, recall, false-positive rate, per-case blocking rate or time-to-containment. It also warns against inferring adversarial intent from flagged behavior alone.
