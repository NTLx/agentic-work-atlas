---
type: raw
source: "https://blog.cloudflare.com/cloudflare-one-stack/"
author:
  - "AJ Gerstenhaber"
  - "Abe Carryl"
published: "2026-06-17"
created: "2026-06-18"
tags:
  - clippings
  - zero-trust
  - agent-skills
  - MCP
  - cloudflare
  - security
  - agent-harness
---

# Introducing the Cloudflare One stack: agent-powered deployment

The Cloudflare One stack is a library of agent skills that gives any AI agent the knowledge it needs to plan, deploy, and manage a Zero Trust environment — no migration calls required.

## The agent gap in network security

Teams are already using agents to write code, triage alerts, and automate workflows. Organizations are increasingly asking for Cloudflare-provided tooling to help agents execute on security workflows. On their own, agents are not trained on the nuances of an organization's specific network topology or vendor configurations.

By providing prescriptive and authoritative guidance, organizations can layer this context into their existing toolkit to make better use of the security products they are already deploying.

Cloudflare has long been the easiest-to-deploy SASE vendor in the market. The stack extends that philosophy to agents: it gives them the context, tools, and structured reasoning they need to operate on your security infrastructure.

## What is the Cloudflare One stack?

The Cloudflare One stack is a collection of skills that can be used with any agent. As with any skill, you can use them standalone, layer in your own context, or build tooling on top. It was purpose-built to help security practitioners across the entire lifecycle of evaluating, deploying, and managing Cloudflare One.

The stack was built by synthesizing hand-curated knowledge from employees with tens of thousands of hours of experience working with customers on Cloudflare One products. It contains tools for planning, managing, and implementing your user and agent security infrastructure on Cloudflare. It also contains handpicked logic for migrating from legacy vendors like Zscaler and Palo Alto Networks.

When used in conjunction with the Cloudflare code mode MCP server, the stack gives agents a typed interface to the Cloudflare API. Agents can query your live account, inspect configurations, and make changes through a curated set of Cloudflare-recommended workflows rather than ad-hoc API calls.

## What's in the stack?

The Cloudflare One stack ships as two lightweight skill files: cloudflare-one and cloudflare-one-migration. Together they cover migrating to, building an implementation for, managing, and troubleshooting your Cloudflare One deployment:

- Remote access and VPN replacement with Cloudflare Access
- User, network, device, and data security with Cloudflare Gateway
- Connectivity with Cloudflare Tunnel, Cloudflare Mesh, and Cloudflare WAN
- Migration guidance with explicit detail for moving from other SASE vendors
- Network diagram interpretation and generation
- Vendor concept translation, which maps concepts between SASE vendors
- Troubleshooting and operations, with the Digital Experience Monitoring (DEX) toolkit

## How it works

The stack is available in the Cloudflare Skills repository. Each skill file contains structured knowledge, decision trees, and tool definitions that agents load automatically when the context matches.

The cloudflare-one skill covers general product guidance. For example, if you ask an agent for the best way to replace your VPN infrastructure with Cloudflare Tunnel or Cloudflare Mesh, the skill knows how to:

1. Inventory your existing VPN applications and identify which connectivity model each requires
2. Map each application to the appropriate Cloudflare primitive
3. Generate a recommended deployment sequence that minimizes disruption during cutover
4. Produce a configuration summary your team can review before making any changes

The cloudflare-one-migration skill covers vendor-to-vendor translation. For example, if you ask an agent to migrate your Zscaler Private Access applications to Cloudflare Access, the skill knows how to:

1. Map Zscaler application definitions to Cloudflare Access application definitions
2. Transform Zscaler user groups and policies into Cloudflare Access policies
3. Use the Cloudflare API to create the equivalent resources in your account
4. Generate a summary of what was migrated and what requires manual review

The migration logic in the stack is the same logic used in Cloudflare's Descaler and Deskope programs. Those programs have already moved enterprise customers from Zscaler and Netskope to Cloudflare One in hours rather than months.

## More ways to use the stack

The Cloudflare One stack can also:

- Recommend security rules based on traffic seen in your live account
- Automatically migrate your existing Zscaler Private Access applications into self-hosted Cloudflare Access applications
- Investigate anomalies in your secure web gateway HTTP logs and build rules to resolve issues users are seeing
- Report on user stability with the DEX toolkit and take actions to improve user latency in key scenarios

## For partners, too

While this simplifies ongoing management for customers who have already adopted the Cloudflare One product suite, it is also a tool for the Cloudflare partner network. Partners can use it to help their customers deploy faster, manage more effectively, troubleshoot with increased accuracy, and drive issues to resolution.

## What's next

You can start using the Cloudflare One stack today. To get the most out of the stack, pair it with the Cloudflare code mode MCP server. The MCP server gives your agent live access to the Cloudflare API through a single, compressed interface that keeps authentication credentials out of the model context.
