---
source: "https://huggingface.co/blog/ibm-research/cuga-apps"
title: "Build real agentic apps using CUGA: two dozen working examples on a lightweight harness"
author: "IBM Research (Anupama Murthi, Hamid Adebayo, Sami Marreed, Praveen Venkateswaran, Asaf Adi, Ayhan Sebin et al.)"
date: 2026-06-23
tags:
  - agent-harness
  - agentic-engineering
  - enterprise-ai
  - open-source
  - governance
  - multi-agent
---

# Build real agentic apps using CUGA: two dozen working examples on a lightweight harness

**TL;DR** — Building an agent is mostly plumbing: tools, state, guardrails, scaling from one agent to many. CUGA (pip install cuga), short for Configurable Generalist Agent, the Agent Harness for the Enterprise from IBM handles that, so you write just a tool list and a prompt. They built two-dozen single-file apps to prove it.

## Why a harness, not a framework

CUGA handles the orchestration around a model that you'd otherwise rebuild every time. It plans before it acts, then executes with a mix of tool calls and generated code (CodeAct). On long tasks, it holds state and runs a reflection step that can catch a bad call and re-plan instead of barreling ahead. This machinery is why it has topped agent benchmarks like AppWorld and WebArena.

Key differentiators:
- **Harness carries the load**: planning, reflection, variable-tracking — lets smaller open-weight models hold up where they normally wouldn't
- **Config-driven cost/latency**: Fast, Balanced, Accurate reasoning modes with configurable sandbox (local, Docker/Podman, E2B cloud)
- **Model-agnostic**: one-env-var provider switching (OpenAI, watsonx, Ollama, etc.)
- **Small API surface**: build a `CugaAgent` with a tool list and a prompt, then `await agent.invoke(...)`

## Policy system (six types)

CUGA ships a policy system in the runtime:

1. **Intent Guard** — checks requests before the agent picks a tool
2. **Tool Approval** — runs after agent generates code, inspects which tools are used
3. **Output Formatter** — fires only once the final message exists
4. **Tool Guide** — steers tool selection
5. **Rate Limiter** — controls invocation frequency
6. **CustomPolicy** — escape hatch

Triggers go past keyword matching: they use `sqlite-vec` for semantic matching. Policies live in the `.cuga` folder, versioned next to code.

## Multi-agent: CugaSupervisor

When one agent would drown in its own context, split the work. A `CugaSupervisor` delegates to specialist `CugaAgent`s, each with its own tools, prompt, and isolated context. Adding a capability means adding a specialist, not rewriting a coordinator.

**Ouroboros** — a seven-agent lead-gen system with supervisor over seven specialists (scout, site auditor, voice-of-customer, person finder, stack scanner, revenue estimator, pitch-email writer).

## Agent Skills

A folder with a `SKILL.md` playbook the agent pulls into context only when a task calls for it. With ALTK-Evolve, an agent refines a skill from its own runs — learning accumulates.

## Production: IBM Sovereign Core

CUGA agents run under Boundary Isolation: data, control plane, and execution engine inside the same logical boundary, with agents running in transient, isolated containers. Deployments default to `gpt-oss-120b` running fully air-gapped. Every reasoning step emits OpenTelemetry traces into Grafana Tempo — all in-tenant.

## Significance

CUGA represents a concrete instantiation of the **Harness-as-a-Service (HaaS)** concept, with governance built into the runtime from day one rather than retrofitted. The policy system demonstrates that **Agent Control Plane** functionality can be embedded in open-source harnesses, not just proprietary platforms. The "governed by construction" approach — where the governed path is the default — is a design pattern worth tracking.
