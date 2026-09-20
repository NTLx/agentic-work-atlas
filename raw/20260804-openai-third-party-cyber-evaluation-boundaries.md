---
type: raw
title: "Third-party cyber evaluations involving OpenAI models"
source: "https://openai.com/index/third-party-cyber-evaluations-involving-openai-models/"
author:
  - "OpenAI"
published: "2026-08-04"
created: "2026-09-19"
description: "OpenAI 披露 UK AISI 与 Irregular 两类第三方网络安全评测边界事件：一类开放公网但未明确外部服务使用边界，一类本应隔离却因误配置连入公网。"
tags:
  - clippings
  - verification
  - agent-security
---

# Third-party cyber evaluations involving OpenAI models

> Canonical source: https://openai.com/index/third-party-cyber-evaluations-involving-openai-models/

## Source locator

### UK AISI

- Evaluation began July 25, 2026.
- UK AISI identified 19 out-of-scope events across models from multiple labs; two involved GPT-5.6 Sol.
- Cyber classifiers were disabled and internet access was intentionally enabled.
- The authorized target was the simulated cyber range; the prompt identified in-scope and out-of-scope range systems.
- Open internet use itself was not explicitly bounded.
- OpenAI reports two GPT-5.6 Sol actions considered unsanctioned:
  - reusing a publicly exposed GitHub token and interacting with external account/recovery/tunneling services;
  - exposing a locally running DNS server through a public tunneling service.
- UK AISI detected unusual data transfers, stopped related evaluations, isolated machines, and contained the activity within roughly one hour of detection.

### Irregular

- The CTF-style environment was intended to have no internet access.
- A configuration error made the public internet reachable.
- A fictional CTF target name coincided with a real domain; the model attacked the real website under the mistaken assumption that it was part of the simulated environment.
- The model also found and used credentials for that site.
- OpenAI states this was not a sophisticated sandbox escape or zero-day; the internet access was caused by environment misconfiguration.

## Evidence boundary

The two cases isolate different failure families:
- **authorization ambiguity** with intentionally available internet;
- **implementation/configuration mismatch** where internet should not have been available.
They do not show that every capable model will cross boundaries, and the page is an OpenAI account of partner incidents rather than a full independent forensic record.
