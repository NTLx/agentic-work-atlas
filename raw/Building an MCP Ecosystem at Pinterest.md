---
title: "Building an MCP Ecosystem at Pinterest"
source: "https://medium.com/pinterest-engineering/building-an-mcp-ecosystem-at-pinterest-d881eb4c16f1"
author:
  - "[[Pinterest Engineering]]"
published: 2026-03-20
created: 2026-05-12
description: "Tan Wang | Software Engineer, Agent Foundations"
tags:
  - "clippings"
---
Tan Wang | Software Engineer, Agent Foundations

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*NxS4wACf5xatHauDP_ExXQ.png)

Over the last year, Pinterest has gone from “MCP sounds interesting” to running a growing ecosystem of **Model Context Protocol (MCP) servers**, a **central registry**, and production integrations in our IDEs, internal chat surfaces, and AI agents. This post walks through what we’ve built so far, how we designed it, and where we’re taking MCP next.

## What Is MCP and Why Did We Care?

[**Model Context Protocol (MCP)**](https://modelcontextprotocol.io/docs/getting-started/intro) is an open-source standard that lets large language models talk to tools and data sources over a unified client-server protocol, instead of bespoke, one-off integrations for every model and every tool. At Pinterest, we’re using MCP as the substrate for AI agents that can safely automate engineering tasks, not just answer questions. That includes everything from “read some logs and tell me what’s wrong” to “look into a bug ticket and propose a fix PR.”

## The Initial Architecture: Internal MCP + Registry

### Hosted, Not Local

Although MCP supports local servers (running on your laptop or personal cloud development box, communicating over stdio), we explicitly optimized for **internal cloud-hosted MCP servers**, where our internal routing and security logic can best be applied.

Local MCP servers are still possible for experimentation, but the paved path is “write a server, deploy it to our cloud compute environment, list it in the registry.”

### Many Small Servers, Not One Giant One

We debated a **single monolithic MCP server** vs. multiple domain-specific servers. We chose the latter: **multiple MCP servers** (e.g., Presto, Spark, Airflow) each own a small, coherent set of tools. This lets us apply **different access controls** per server and avoid crowding the model’s context.

A common piece of feedback we received early on was that spinning up a new MCP server required too much work: deployment pipelines, service configuration, and operational setup before writing any business logic. To address this, we created a unified deployment pipeline that handles infrastructure for all MCP servers: teams define their tools and the platform handles deployment and scaling of their service. This lets domain experts focus on their business logic rather than figuring out deployment mechanics.

### The Internal MCP Registry

The **MCP** [**registry**](https://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview/) is the source of truth for which MCP servers are approved and how to connect to them. It serves two audiences. The **web UI** lets humans discover servers, the owning team, corresponding support channels, and security posture. The Web UI also shows the MCP server’s live status and visible tools. The **API** lets AI clients (e.g., our internal AI chat platform, AI agents on our internal communications platform, IDE integrations) discover and validate servers, and lets internal services ask “Is this user allowed to use server X?” before letting an agent call into it.

This is also the backbone for governance: only servers registered here count as “approved for use in production.”

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*aQrjPcAfUoIF-WUdyRIxBg.png)

Figure 1: architectural diagram of Pinterest’s MCP ecosystem.

## What We Shipped

### A Growing Fleet of MCP Servers

We started by seeding a small set of high-leverage MCP servers that solved real pain points, then let other teams build on top of that.

Representative examples (by usage):

- **Presto MCP server**: consistently our highest-traffic MCP server. Presto tools let agents (including AI-enabled IDEs) pull Presto-backed data on demand so agents can bring data directly into their workflows instead of context-switching into dashboards.
- **Spark MCP server**: underpins our AI Spark debugging experience, used to diagnose Spark job failures, summarize logs, and help record structured root-cause analyses, turning noisy operational threads into reusable knowledge.
- **Knowledge MCP server**: a general-purpose knowledge endpoint (used by our internal AI bot for company knowledge and Q&A and other agents to answer documentation and debugging questions across internal sources), so agents can reach for institutional knowledge with the same ease as calling a tool.

### Integrations Into Pinterest Surfaces

We didn’t want MCP to be a science project; it had to show up where engineers already work.

Our internal LLM web chat interface is used by the majority of Pinterest employees daily. The frontend automatically performs OAuth flows where required, and returns a list of usable tools for the current user, scoped to respect security policies. Once connected, our AI chat agent binds MCP tools directly into its agent toolset so invoking MCP feels no different from calling any other tool.

We also have AI bots embedded in our internal chat platform, which also exposes MCP tools. Like our LLM web chat interface, it handles authentication and authorization through the registry API. It also supports functionality such as restricting certain MCP tools to certain communication channels (for example, Spark MCP tools are only available in Airflow support channels).

An overview of the flow from starting to build an MCP server to when it’s consumed by an end user:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Y5mu5OeZuuUP5PTOuFBvhg.png)

Figure 2: end-to-end flow of developing an MCP server

## Security, Governance, and Policy

Letting AI agents call tools that **touch real systems and data** raises obvious security questions. We’ve treated MCP as a joint project with Security from day one.

### Security Standards and Review

We defined a dedicated **MCP Security Standard**. Every MCP server that is not a one-off experiment must be tied to an owning team, appear in the **internal MCP registry**, and go through review, yielding Security, Legal/Privacy, and (where applicable) GenAI review tickets that must be approved before production use. This set of reviews determines the security policies that are put in place around the MCP server, such as which user groups to limit access of the server to.

### AuthN and AuthZ

At runtime, almost every MCP call is governed by two layers of auth: **end-user JWTs** and **mesh identities**.

## Get Pinterest Engineering’s stories in your inbox

Join Medium for free to get updates from this writer.

**End-user flow (JWT-based)**

1. A user interacts with a surface like our web AI chat interface, an IDE plugin, or an AI bot.
2. The client performs an OAuth flow against our internal auth stack and sends the resulting JWT when it connects to the MCP registry and the target MCP server.
3. Envoy validates the JWT, maps it to `X-Forwarded-User`, `X-Forwarded-Groups`, and related headers, and enforces coarse-grained security policies (for example, “AI chat webapp in prod may talk to the Presto MCP server, but not to experimental MCP servers in dev namespaces”).
4. Inside the server, tools use a lightweight `@authorize_tool(policy=’…”)` decorator to enforce finer-grained rules (for example, only Ads-eng groups can call a `get_revenue_metrics`, even if the server itself is reachable from other orgs).

Note that since some MCP servers can execute queries against sensitive internal data systems (like the Presto MCP server), we implemented **business-group-based access gating**. Rather than granting access to all authenticated Pinterest employees and contractors, some servers will:

1. Extract business group membership from the user’s JWT token
2. Validate that the user belongs to an authorized group before accepting the connection (the list of approved groups is set during the initial review stage)
3. Selectively enable capabilities only for users whose roles require data access

At Pinterest, this means that even though the Presto MCP server is technically reachable from broad surfaces like our LLM web chat interface, only a specific set of approved business groups (for example, Ads, Finance, or specific infra teams) can establish a session and run the higher-privilege tools. Turning on a powerful, data-heavy MCP server in a popular surface therefore doesn’t silently expand who can see sensitive data.

Some servers require a valid JWT even for tool discovery. That gives us user-level attribution for every invocation and a clean way to reason about “who did what” when we look at logs.

**Service-only flows (SPIFFE-based)**

For low-risk, read-only scenarios, we can rely on **SPIFFE-based auth** (mesh identity only). Our internal service mesh still enforces security policies, but the server authorizes based on the calling service’s mesh identity instead of a human JWT. We reserve this pattern for cases where there’s no end user in the loop and the blast radius is tightly constrained.

**Contrast with the MCP OAuth Standard**

The MCP specification defines an [OAuth 2.0 authorization flow](https://modelcontextprotocol.io/specification/draft/basic/authorization) where users explicitly authenticate with each MCP server, typically involving consent screens and per-server token management. Our approach is different: users already authenticate against our internal auth stack when they open a surface like the AI chat interface, so we piggyback on that existing session. There is no additional login prompt or consent dialog when a user invokes an MCP tool. Envoy and our policy decorators handle authorization transparently in the background, giving us fine-grained control over who can call which tools without surfacing the complexity of per-server authorization flows to the end user.

### Human in the Loop

Because MCP servers enable automated actions, the blast radius is larger than if a human manually wielded these tools. Our agent guidance therefore mandates **human-in-the-loop** before any sensitive or expensive action: agents propose actions using MCP tools, and humans approve or reject (optionally in batches) before execution. We also use [**elicitation**](https://modelcontextprotocol.io/specification/draft/client/elicitation) to confirm dangerous actions. In practice, this looks like our AI agents asking for confirmation before applying a change to e.g. overwrite data in a table.

## Observability and Success Metrics

We didn’t want MCP to become a black box. From the start, we designed it to be **measured and observable**. All MCP servers at Pinterest use a set of library functions that provide logging for inputs/outputs, invocation counts, exception tracing, and other telemetry for impact analysis out of the box. At the ecosystem level, we measure the **number of MCP servers** and tools registered, the **number of invocations** across all servers, and the **estimated time-savings per invocation** provided as metadata by server owners.

These roll up into a single north-star metric: **time saved**. For each tool, owners provide a directional “minutes saved per invocation” estimate (based on lightweight user feedback and comparison to the prior manual workflow). Combined with invocation counts, we get an order-of-magnitude view of impact, which we treat as a directional signal of value. As of January 2025, MCP servers have ramped up to **66,000 invocations per month** across **844 monthly active users**. Using these estimates, MCP tools are saving on the order of **7,000 hours per month**.

## Conclusion

In the past year, Pinterest has successfully transitioned from an initial concept to a robust, production-ready ecosystem for the Model Context Protocol (MCP). By explicitly choosing an architecture of internal cloud-hosted, multiple domain-specific MCP servers connected via a central registry, we have built a flexible and secure substrate for AI agents. These high-leverage tools are integrated directly into employees’ daily workflows, meeting them where they work.

Crucially, this entire system was built with a security-first mindset. Our two-layer authorization model using end-user JWTs and mesh identities, combined with a dedicated MCP Security Standard and business-group-based access gating on sensitive servers like Presto, ensures that powerful AI agents operate with the principles of least privilege and full auditability.

The results are clear: the MCP ecosystem has already grown to over 66,000 invocations per month, delivering an estimated 7,000 hours of time saved monthly for our engineers. This success confirms the value of using an open-source standard to unify tool access for AI.

Looking ahead, we will continue to expand the fleet of MCP servers, deepen integrations across more engineering surfaces, and refine our governance models as we empower more AI agents to safely automate complex engineering tasks, further boosting developer productivity at Pinterest.

## Acknowledgements

This AI-enabled MCP ecosystem would not have been possible without:

- Nick Borgers, Kalpesh Dharwadkar, Amine Kamel from our security engineering team
- Scott Beardsley, James Fish from our traffic engineering team
- Leon Xu, Charlie Gu, Kingsley Ochu from our AI Agent Foundations team
- Scott Herbert, Anthony Suarez, Kartik Paramasivam for their engineering sponsorship and guidance
