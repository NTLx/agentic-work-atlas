---
type: raw
source: "https://www.marktechpost.com/2026/06/17/vercel-releases-eve/"
author:
  - "Asif Razzaq"
  - "Vercel"
published: "2026-06-17"
created: "2026-06-18"
tags:
  - clippings
  - agent-framework
  - open-source
  - vercel
  - agent-harness
  - durable-execution
---

# Vercel Releases Eve: An Open-Source AI Agent Framework Where Each Agent is a Directory of Files Mapped to Capabilities

Vercel has released eve, an open-source framework for building, running, and scaling agents. The project is published as the npm package `eve`, licensed under Apache-2.0.

Building an agent should mean defining what it does. It should not mean assembling all the plumbing that an agent needs to run in production.

eve is the framework Vercel builds and runs its own agents on. According to Vercel, it runs more than a hundred agents in production today.

## What is eve?

eve is a filesystem-first framework for durable backend agents. You create an agent as a directory on disk. The directory is the contract.

Each file describes one component of the agent. At a glance, the tree shows what an agent is and does. It also shows where it lives and when it acts on its own.

The smallest agent that runs is two files. One sets the model. The other sets the instructions.

## An agent is a directory

Vercel's core idea is that agents have a shape. Every team kept rebuilding the same structure to meet the same needs. eve makes that shape into a framework.

The directory layout maps each capability to a folder. Here is the contract:

| Path | Role | Format |
|------|------|--------|
| `agent.ts` | The model it runs on, plus runtime config | TypeScript |
| `instructions.md` | Who it is, prepended to every model call | Markdown |
| `tools/` | What it can do; filename becomes the tool name | TypeScript |
| `skills/` | What it knows; loaded only when the topic comes up | Markdown |
| `connections/` | Secure links to MCP servers and OpenAPI APIs | TypeScript |
| `sandbox/` | Optional override of the agent's sandbox; seeds workspace files | Directory |
| `subagents/` | Specialist child agents it delegates to | Directory |
| `channels/` | Where it lives, like Slack or HTTP | TypeScript |
| `schedules/` | When it acts on its own, on a cron | TypeScript |
| `lib/` | Shared authored code used across the agent | TypeScript |

You add a tool, skill, channel, or schedule by adding a file. eve picks them up at build time and wires them in. There is no boilerplate to register them.

A tool is one TypeScript file with a Zod input schema. Its filename and place in the tree become its definition.

## What ships in the box

Vercel describes eve as 'batteries included.' Six production capabilities come with the framework:

- **Durable execution**: Every conversation is a durable workflow, with each step checkpointed. A session can pause, survive a crash or a deploy, and resume where it stopped. This is built on the open-source Workflow SDK.
- **Sandboxed compute**: Agent-generated code is treated as untrusted. Every agent gets its own sandbox for shell commands, scripts, and file reads and writes. The backend is an adapter, running on Vercel Sandbox when deployed and on Docker, microsandbox, or just-bash locally.
- **Human-in-the-loop approvals**: Any action can be set to require approval. The agent pauses there and waits, indefinitely if needed, without consuming compute. Once approved, eve continues from where it left off.
- **Secure connections**: A connection is a file pointing at an MCP server or an OpenAPI-compatible API. eve brokers the auth, and the model never sees the URL or credentials. At launch, agents can connect to Slack, GitHub, Snowflake, Salesforce, Notion, and Linear.
- **Channels**: The same agent serves every surface. The HTTP API is on by default, with Slack, Discord, Teams, Telegram, Twilio, GitHub, and Linear included. One channel can hand off to another.
- **Tracing and evals**: Every run produces a trace using standard OpenTelemetry spans. They export to Braintrust, Honeycomb, Datadog, or Jaeger. Evals are scored test suites you run locally or wire into CI.

## Use cases, with real examples

Vercel published six agents it runs internally on eve:

- **d0, the data analyst**: Its most-used internal tool, handling more than 30,000 questions a month. Every query is scoped to the asker's own permissions.
- **Lead Agent, the autonomous SDR**: It works every new lead and follows up on its own. Vercel says it costs about `$5,000` a year and returns 32 times that, maintained part-time by one engineer.
- **Athena, the sales cockpit**: RevOps built it in six weeks without engineers. It answers pipeline questions from Snowflake and Salesforce in plain language.
- **Vertex, the support engineer**: It handles tickets across the help center, docs, and Slack. Vercel reports it solves 92% of tickets on its own and escalates the rest.
- **draft0, the content agent**: It runs a review pipeline that catches glaring issues before a human editor sees the piece.
- **V, the routing agent**: Tasks go to V in Slack first. V routes each one to the agent that can answer it.

## eve versus a hand-rolled agent stack

| Capability | Typical DIY stack | eve |
|-----------|------------------|-----|
| Authoring | Custom loop, manual tool registration | Files in a directory, discovered at build |
| Durability | Bespoke state and retry handling | Checkpointed durable workflow per session |
| Code execution | Self-managed container or VM | Per-agent sandbox via swappable adapter |
| Approvals | Custom pause-and-resume logic | `needsApproval` field on any action |
| Surfaces | One integration per channel | One adapter file per channel |
| Observability | Stitched together from logs | OpenTelemetry traces and evals built in |
| Deploy | Provision infrastructure | `vercel deploy`, runs unchanged from local |

## Getting started

You can scaffold and start a new agent with one command. It installs dependencies, scaffolds the project, and starts a dev server.

```bash
npx eve@latest init my-agent
```

`eve dev` runs the agent locally with an interactive terminal UI. `eve eval` runs your test suites. `eve build` compiles inspectable artifacts under `.eve/`.

Because an eve agent is an ordinary Vercel project, `vercel deploy` ships it to production unchanged. The sandbox swaps to Vercel Sandbox without a code change.
