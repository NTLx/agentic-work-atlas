---
type: raw
title: "The five components of building a company harness"
source: "https://www.langchain.com/blog/components-building-company-harness"
author:
  - "Harrison Chase"
  - "Caspar Broekhuizen"
published: 2026-10-24
created: 2026-10-28
description: "Bounded evidence clipping from LangChain's first-party account of recurring primitives across its internal company agents. Full public source remains recoverable at the canonical URL."
language: en
tags:
  - "clippings"
---

# The five components of building a company harness

Canonical source: https://www.langchain.com/blog/components-building-company-harness

## Evidence clipping

LangChain reports that its internal GTM, engineering and content agents converged on five recurring runtime primitives:

1. The Agent lives where people already work, mainly Slack, with custom UI used where message-based review becomes awkward.
2. Identity is explicit: some actions run on behalf of the invoking user while other tools/background tasks use a fixed service/application identity; tool availability can change by context such as DM vs shared channel.
3. Memory is scoped globally and/or per user rather than treated as one undifferentiated store.
4. Code executes in sandboxes while authenticated service access is mediated through connection/secret infrastructure.
5. A large fraction of useful runs are scheduled or event-triggered rather than explicitly invoked by a person.

The article grounds these primitives in three internal agents—GTM Agent, OpenSWE and Content Studio—and describes different identity choices by tool and execution context. It frames the result as a general company-harness recipe, but the evidence comes from LangChain's own deployment experience.

## Source locators

- Opening list: five recurring primitives.
- “Problem: Identity”: on-behalf-of vs fixed identities and context-dependent tool availability.
- “Problem: Memory”: global and user-scoped memory.
- “Problem: Code Execution”: sandbox plus authenticated service access/secret proxy.
- “Problem: Scheduled Runs”: developer- or user-defined background/event-triggered execution.

## Evidence boundary

This is a first-party vendor/operator case study, not a comparative benchmark. It supports the existence of recurring design primitives in LangChain's internal deployments, but not the claim that every enterprise needs the same five components or that these choices are uniquely optimal.