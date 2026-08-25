---
type: raw
source: "https://magneticgrowth.substack.com/p/2026-the-year-of-the-forward-deployed"
author:
  - "Alex Furmansky"
published: "2026-03-03"
created: "2026-08-25"
tags:
  - clippings
  - forward-deployed-engineer
  - fde
  - ai-saas
  - agentic-ai
---

# 2026: The Year Forward Deployed Engineering Becomes Table Stakes for SaaS

I’m seeing AI SaaS companies send technical consultants to run discovery and build custom-ish solutions on-site for each client. We call these consultants “Forward Deployed Engineers,” a title popularized by Palantir in the early 2010s.

> **My take: the line between “SaaS company” and “services company” is blurring. The product and the deployment are becoming inseparable.**

Why? Agentic AI SaaS is less a defined product and more a value opportunity. Realizing that value requires getting good at customizing multipurpose tools for specific contexts. We’re still early in product discovery, and the delta between what you can deliver with AI versus what was possible before is enormous.

*(Thank you to [Lukas Egger](https://www.linkedin.com/in/lukas-np-egger) for helping shape this post.)*

## Why vendors can’t follow SaaS playbooks

It used to be formulaic: run customer discovery, build a high-value wedge product, offer the same product to tens of thousands of clients, mint 80%+ profit margins.

The pace of AI broke that formula. ChatGPT, Claude, and Gemini massively move the goalpost every six months in inference, connectivity, and user experience. Open-source projects like BabyAGI (agents) and OpenClaw (full autonomy) spread like wildfire on AI Twitter and push the boundaries of what’s possible on top of frontier models.

> **Whatever feature an AI SaaS point solution offers today has a coin-flip chance of being eclipsed within six months by a generalist agent.**

AI now addresses entirely new categories of work that deterministic software never could. The displacement potential is highest in probabilistic, judgment-heavy tasks, the kind of work that was always too messy, too contextual, too “human” for traditional automation. That’s a massive unlock, and it means the biggest prize isn’t automating existing workflows. It’s discovering workflows that weren’t possible before.

Then there’s the expectation problem. The instantly-adapting nature of chat-based AI bots, especially those that can build custom visual artifacts or apps on the fly, means clients now expect bespoke software that fits their specific needs. Why would any company want the headache of deploying a full ERP when they only use 20% of the features? Today, clients don’t have to settle for complexity and homogeneity.

> **Vendors respond by wrapping a thin agentic platform product with heavy customization for each client’s UX, workflows, and data pipelines.**

This model requires people on site, in the room, asking hard questions and wrangling with MCP / data / agentic layers.

Trying to spec out what clients want through traditional customer discovery is like asking someone before the iPhone what their favorite app would be. The question doesn’t have a clean answer yet.

It requires Forward Deployed Engineers.

## Why clients don’t know what to buy

On the customer side, there’s strong pressure from the C-Suite to sprinkle AI everywhere. In the CEO’s eyes, if her ChatGPT can turn CSVs into beautiful reports and draft an email of takeaways in her voice, then why aren’t her teams pouring in the latest AI vendor tech and running all core processes agentically?

One answer: it’s not clear what to buy or how to set it up. (The other answer is about alignment of incentives and dispersion, which I’ll cover in another post.)

## The systems thinking is hard

Before diving in here, let me ground what I mean by “systems thinking” in this context. I’m talking about the ability to look at a real business process, identify which steps require judgment versus which are mechanical, map the handoffs and edge cases, and design an AI system that handles the right parts while keeping humans in the loop where they need to be.

> **This work is genuinely difficult. It requires someone who can hold the entire system in their head while simultaneously understanding the messy reality of how humans actually operate within it.**

The jagged frontier of AI capability makes it even harder. Even people with strong technical intuitions routinely misjudge where models excel and where they fall apart. A task that seems trivially easy for AI might fail spectacularly, while something that seems impossibly complex works on the first try. This is part of why outside expertise matters so much. Someone who has tested these boundaries across multiple deployments has a fundamentally different intuition than someone approaching it for the first time.

> **Companies cannot spare their best people for this type of work.**

Their best lieutenants need to stay focused on revenue-generating projects. Can you imagine pulling a product pod away from client-facing work for a year? This makes sense if you have ten product pods. But what if you only have two?

Companies don’t know the reality of their own processes, let alone which are realistic to automate with LLMs. That makes it nearly impossible to define the specific AI product they need to buy.

## The knowledge is scattered and stale

Imagine you individually asked five people on a sales team how the team handles their leads. I’d bet each person would give a slightly different answer about which leads they toss away versus which ones they call a second time. The VP of Sales likely shares a different case study in response to an objection than the entry-level BDR. Ask a senior exec and you’ll get a sixth answer.

> **There is variance in any human organization because the real world is messy, and every node in an org compounds the mess geometrically. Variance in knowledge, variance in personalities, variance in incentives.**

For the knowledge work that LLMs excel at, rules are non-deterministic. Sometimes we do it this way, but other times we do it that way... and Jerry does it this whole other way. This is fundamentally different from the workflow automation tools of yesteryear, which assumed clean, repeatable inputs.

Professional-grade process management is genuinely expensive. As my friend Lukas Egger, VP of Strategy and Innovation at SAP Signavio, pointed out to me: maintaining clean, current process documentation, the kind of rigorous BPMNs and DMNs that would actually let you spec an AI system, is nearly prohibitive for most organizations. Unless your revenue is measured in small-country GDP, you’re not keeping that stuff up to date.

That context makes the Forward Deployed Engineer feel less like a luxury and more like a structural necessity. Someone has to come in and do the excavation work, because the organization was never going to do it on its own.

## What this actually looks like in practice

I’m living this right now. One of my clients is a real estate operations company going through an AI transformation. A part of my role is to deploy Anthropic’s Claude across their workflows.

The head of Strategy and I spend weeks interviewing stakeholders across operations, finance, and acquisitions. Each department has a different understanding of their own processes. The C-suite describes workflows that the analysts on the ground don’t recognize. Tribal knowledge lives in judgment calls and tastes.

**Once we map the actual workflows, I start building: custom AI skills, agent configurations, prompt architectures tailored to how their people actually work.** Now we’re training their team to use and maintain it. That’s embedded consulting with a technical backbone.

> **The work inevitably surfaces organizational questions that go beyond technology.**

Agentic AI doesn’t just improve existing workflows. It unbundles roles, rejiggers tasks, and restructures how work gets done. When you automate the data-gathering portion of an analyst’s job, you’re redefining what that analyst does all day. That’s an operating model decision. Companies that treat AI deployment as pure software implementation and skip the organizational reconfiguration don’t get the value.

The FDE role exists partly to force that reckoning.

It’s the FDE model, whether or not anyone calls it that. And it’s what my team does at every engagement: apply a malleable framework to the specific needs of each client. Discovery, architecture, build, train, hand off. We run this playbook for every client, whether it’s customer-facing AI agents or internal workflow automation.

## The big players are all in

The largest AI companies in the world are building entire organizations around this model.

> **The highest-value use cases can’t be discovered through a standard customer interview.**

Historically, the biggest disruptions from any new technology came from use cases that were only possible *because* of the technology, not incremental improvements to existing ones. Understanding what those are requires being in the room, especially when the frontier is moving every other week.

OpenAI just announced the Frontier Alliance, a structured enterprise program pairing OpenAI’s forward deployed engineers with four of the world’s largest management consulting firms: BCG, McKinsey, Accenture, and Capgemini. Their FDE team grew from 2 to 52 engineers in 2025 alone, embedding with customers like Morgan Stanley to solve high-value problems. Enterprises account for roughly 40% of OpenAI’s revenue, and their CFO expects that figure to approach 50% by the end of this year.

Anthropic is scaling its Applied AI team aggressively, hiring Forward Deployed Engineers, Technical Deployment Leads, and Solutions Architects to embed with strategic enterprise customers. These engineers build production applications on Claude, deliver technical artifacts like MCP servers, sub-agents, and agent skills, and provide white-glove deployment support. The team is reportedly growing 5x. This is how Anthropic plans to win enterprise.

Most large enterprises simply don’t have the in-house expertise or bandwidth to figure this out alone.

Why are all these players converging on the same model? Because the FDE who rotates across engagements gains something an internal team never can: pattern recognition at scale. This is what my team and I do across our clients.

Forward deployed engineering is, at its core, hands-on market research and adoption acceleration happening at the same time. Organizations are realizing, sometimes without being able to articulate it, that they need market intelligence and product discovery that they simply cannot generate from the inside.

FDE job postings soared by more than 800% between January and September 2025 ([Indeed / Financial Times](https://www.ft.com/content/forward-deployed-engineers)).

## What this means

If I’m right about this, there’s a real opportunity for a certain kind of person to build a very good career over the next one to five years.

Someone who can sell, who can speak technically, and who genuinely enjoys solving different problems at different companies. Someone who can hold space between an anxious C-Suite and a skeptical engineering team. Someone who can translate business outcomes into technical architecture and back again. Someone with a pedigree of rigor (e.g., consulting, ibanking, strategy at big tech, etc.).

But there’s one more dimension that might matter most of all: the ability to hold ambiguity about what’s technically possible *right now* while staying open to what might be possible in 90 days. Yesterday’s hard no can be tomorrow’s biggest unlock. The tools are changing faster than project timelines. That takes a specific kind of mind: someone with systems thinking, a tinkerer’s instinct, and enough intellectual humility to keep revisiting closed questions.

If that’s you, give me a shout here or on LinkedIn. We’re hiring. And if you’re a leader who knows your org needs this but can’t figure out where to start, that’s the exact conversation my team has every week.

**2026 belongs to the Forward Deployed Engineer.**