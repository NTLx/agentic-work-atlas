---
type: raw
title: "How AI-native companies turn workflows into operating capability"
source: "https://openai.com/index/ai-native-company-workflows/"
author:
  - "OpenAI"
published: "2026-09-01"
created: "2026-09-02"
description: "OpenAI 通过 Basis、Clay 和 Exa 案例说明企业如何把 Agent 嵌入 onboarding、account management 和开发者集成，并将成功工作流变成可重复能力。"
tags:
  - "clippings"
  - "AI-adoption"
  - "workflows"
  - "agentic-engineering"
  - "organizational-design"
---

# How AI-native companies turn workflows into operating capability

Basis, Clay, and Exa Labs use agents for onboarding, account management, and developer integrations. Their examples show what enterprise leaders can borrow.

OpenAI’s latest [Enterprise Signals](https://openai.com/signals/enterprise-data/) shows enterprise AI moving from assistance to execution at sharply different speeds. Frontier firms (those with the top 10% of AI usage) now generate 8.3× as many output tokens per active user as typical firms, up from 2.6× in January. The widening gap points to a deeper operating shift: leading firms connect agents to company context and tools, delegate more substantive work, and make successful workflows easier to repeat.

For leaders, the challenge is to turn that depth into work people can trust, measure, and improve. Leaders should also leave room for experimentation, including use cases whose value is not obvious on the first try.

Startups [Basis](https://www.getbasis.ai/), [Clay](https://www.clay.com/), and [Exa Labs](https://exa.ai/) have built agents into employee onboarding, account management, and developer ecosystem growth. Their workflows differ, but the progression is instructive: teach an agent a stable process, give it persistent context as work changes, then let it carry opportunities into tested action.

Together, these examples show how teams can build agents into familiar work and improve the process over time.

## Basis: Make onboarding teachable with agents

Onboarding has long been cumbersome for employers and employees. At Basis, which builds AI agents for accounting firms, first-day onboarding now takes 30 minutes instead of two hours, giving HR more time for culture and support.

On day one, employees receive immediate access to Codex and a company-specific onboarding skill (a reusable set of instructions and resources for a specific workflow). Codex welcomes them, introduces key company concepts, and uses their computer to complete integration setup in the background. When recurring questions or exceptions appear, HR can update the skill before the next cohort.

Basis demonstrated the onboarding process once, then turned it into a reusable skill with a clear trigger, known steps, access to the right tools, and a clear definition of “done.” The process no longer depends on one person’s availability, yet the team can step in for exceptions or complex questions. Onboarding is now more consistent, repeatable, and easier to improve, and new employees gain an immediate model for working with AI.

## Clay: Give scattered work a persistent home base

Clay, a company building a self-learning revenue engine for go-to-market teams, faces a familiar sales challenge: critical deal context is scattered across CRM records, email, Slack, calls, presentations, text messages, and conversations with internal teams and customer champions.

To keep that context current, one of Clay’s GTM engineers experimented with a better approach—a persistent workspace and dedicated subagent for every account. Each subagent reviews primary sources and updates its deal folder overnight. Every morning, a coordinating agent turns those updates across all her accounts into a short list of priority moves: answer a lingering customer question, fill a gap in the buying committee, or give a prospect a reason to re-engage.

The workflow saves her roughly an hour of inbox triage each night, according to Clay. The daily priorities help her follow through on the small actions that can add up over a long enterprise sales cycle. The supporting evidence stays close to each recommendation, so sellers can inspect the primary sources before acting. Enterprises could extend that shared context to account executives, BDRs, solutions engineers, and sales leaders, subject to existing account permissions.

Clay shows what evolving work needs in order to scale: a consistent structure, a useful refresh cadence, shared evidence, and human judgment at the point of action.

## Exa: Carry an opportunity into tested action

Exa Labs, which builds web search infrastructure for AI agents, wants to make its search API available wherever developers could use it. The team calls this goal “Exa everywhere.” Pursuing it once required developer relations and account teams to monitor repositories and the wider ecosystem, identify promising integrations, gather context, and coordinate work across systems. Although the opportunities varied, the path from discovery to implementation followed a consistent sequence.

Exa turned that sequence into a defined workflow for Codex, with clear priorities, access to the necessary sources, and human review before anything ships.

Codex now monitors for high-priority integration opportunities, gathers the relevant context, creates pull requests, runs tests, and prepares weekly updates using sources such as Slack and Notion. When appropriate, it can also draft the next step, including an initial announcement, for the team to review. The workflow carries an opportunity from signal to tested artifact while reducing handoffs across research, engineering, and communication.

People still decide which opportunities matter, which commitments Exa should make, and how external relationships should be managed. Tests and review points make the agent’s work visible before it ships. Test results and human review can show the team where to adjust the workflow before the next run. As the work becomes more consequential, permissions, evidence, and decision rights become a larger part of the workflow design.

Together, Basis, Clay, and Exa put the patterns we see across Enterprise Signals into operational terms. Basis turns a proven process into a reusable skill. Clay gives an agent the context and persistence to keep an evolving body of work current. Exa adds tools, tests, and review so an agent can carry a signal into bounded execution.

All three make improvement part of the workflow: onboarding exceptions reveal where a skill needs refinement; new account activity and seller validation keep deal context current; and tests and human review sharpen the boundaries for future execution. Each starts with a specific job and enough room to test it. The division of labor becomes clearer through use, and responsibility expands as the workflow proves itself.

## Six steps to experiment now and scale what works

With the frontier gap widening, enterprise leaders need to give employees room to test consequential workflows, measure success, and turn the strongest experiments into repeatable practice.

- **Choose one consequential value surface.** Start with an end-to-end workflow where a strategic priority, systems, handoffs, controls, and measurable stakes meet. It should repeat often enough to learn from and matter enough to justify redesign.
- **Define the outcome and how you will measure it.** Name the accountable owner, KPI, baseline, and guardrails. Track depth through completed tasks, connected context and tools, exceptions, and review load. Track value through cycle time, quality, cost, revenue, or risk. Output volume can show that people are asking AI to do more; workflow outcomes show whether it matters.
- **Write the agent’s job description.** Define what triggers the work, the outcome, required context, tools, permissions, and how persistently the agent should work toward completion. Specify what evidence it must produce and where it must stop for human review.
- **Build the human system around the agent.** Put the people closest to the workflow in the design loop. Name who owns the business outcome, domain logic, access and controls, adoption, and daily use. Startups compress these responsibilities into a few people; enterprises need explicit decision rights as the workflow scales.
- **Make experimentation visible and reusable.** OpenAI [research](https://openai.com/index/how-enterprises-put-ai-to-work/) finds that six months after adoption, early-career employees sent 13 more messages per week than executives. Give employees room to test new use cases, then capture the process and evidence behind what works and package it as skills, Plugins, or shared workspaces.

[Chat, Work, and Codex](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex) support different modes: Chat for questions and quick collaboration, Work for multi-step knowledge work and finished deliverables, and Codex for technical execution.

- **Carry the operating pattern forward.** Preserve the context, permissions, evaluations, review points, owners, measures, and enablement that worked, then apply them to the next value surface. Each new experiment should give the next team a better place to start.

## Author

OpenAI
