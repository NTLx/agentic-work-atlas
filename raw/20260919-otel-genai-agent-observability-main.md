---
type: raw
title: "OpenTelemetry GenAI Agent and Framework Semantic Conventions — current main"
source: "https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-agent-spans.md"
author:
  - "OpenTelemetry"
created: "2026-09-19"
description: "OTel GenAI current main：agent/framework 与 GenAI spans 仍为 Development；已覆盖 create/invoke/workflow/plan/tool、retrieval 与 memory 等结构，但 current main 不定义 authorization decision、canonical post-state 或 revoke/recovery 语义。"
tags:
  - clippings
  - observability
  - verification
---

# OpenTelemetry GenAI Agent and Framework Semantic Conventions — current main

> Canonical agent spans: https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-agent-spans.md
> GenAI spans: https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-spans.md
> Accessed: 2026-09-19.

## Source locator

- Repository: open-telemetry/semantic-conventions-genai.
- Current agent/framework semantic conventions are marked Development.
- Agent/framework spans cover:
  - create agent;
  - invoke agent client;
  - invoke agent internal;
  - invoke workflow;
  - plan;
  - execute tool.
- Broader GenAI spans additionally cover inference, embeddings, retrievals, fetch response, memory and execute-tool operations.
- Conventions carry agent identity/name/version, conversation and operation metadata where applicable.
- Current main therefore provides a structured trace vocabulary for declared Agent/framework operations and local lineage.
- The current agent/framework and GenAI span pages contain no normative fields named for:
  - authorization decision;
  - canonical external post-state;
  - revoke;
  - recovery/compensation completion.

## Evidence boundary

OpenTelemetry semantic conventions standardize telemetry emitted by instrumented code. They do not prove that every reachable runtime path is instrumented, that emitted spans correspond to provider-authoritative effects, or that a missing span means an action did not occur. Development status also means schema details can still change.
