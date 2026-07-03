---
type: raw
source: "https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills"
author:
  - "Thariq Shihipar"
published: "2026-06-03"
created: "2026-07-03"
tags:
  - clippings
  - skill-engineering
  - agentic-engineering
  - claude-code
---

# Lessons from building Claude Code: How we use skills

Thariq Shihipar, Anthropic, June 3, 2026

Skills have become one of the most used extension points in Claude Code. They're flexible, easy to make, and easy to distribute. But this flexibility also makes it hard to know what works best. What type of skills are worth making? How do you structure a skill? When do you share them with others?

We've been using skills in Claude Code extensively at Anthropic with hundreds of them in active use. These are the lessons we've learned about using skills to accelerate our development.

## What are skills?

Skills are folders of instructions, scripts, and resources that agents can discover and use to do things more accurately and efficiently. A common misconception is that they are "just markdown files." They're actually folders that can include scripts, assets, data, etc. that the agent can discover, explore and manipulate.

In Claude Code, skills also have a wide variety of configuration options including registering dynamic hooks. Some of the most effective skills use these configuration options and folder structure effectively.

## Types of skills

After cataloging all internal skills at Anthropic, they cluster into nine categories. The best skills fit cleanly into one; the ones that try to do too much straddle several and confuse the agent.

### 1. Library and API reference

Skills that explain how to correctly use a library, CLI, or SDKs. Often include a folder of reference code snippets and a list of gotchas. Examples: billing-lib (internal billing library edge cases), internal-platform-cli (subcommand examples), sandbox-proxy (egress gateway configuration).

### 2. Product verification

Skills that describe how to test or verify code is working. Often paired with playwright, tmux, or other external tools. These have had the **most measurable impact on Claude's output quality** internally. It can be worth having an engineer spend a week just making verification skills excellent. Techniques: recording video of output, enforcing programmatic assertions on state at each step. Examples: signup-flow-driver, checkout-verifier, tmux-cli-driver.

### 3. Data fetching and analysis

Skills that connect to data and monitoring stacks. Include libraries to fetch data with credentials, specific dashboard IDs, and instructions on common workflows. Examples: funnel-query (event joins for signup→activation→paid), cohort-compare (retention/conversion comparison with statistical significance), grafana (datasource UIDs, cluster names), datadog (field reference, service list).

### 4. Business process and team automation

Skills that automate repetitive workflows into one command. Usually simple instructions but may depend on other skills or MCPs. Saving previous results in log files helps the model stay consistent. Examples: standup-post (aggregates ticket tracker + GitHub + Slack), create-ticket (enforces schema + post-creation workflow), weekly-recap.

### 5. Code scaffolding and templates

Skills that generate framework boilerplates. Especially useful when scaffolding has natural language requirements that can't be purely covered by code. Examples: new-framework-workflow, new-migration, create-app.

### 6. Code quality and review

Skills that enforce code quality and help review code. Can include deterministic scripts or tools. May run automatically as part of hooks or GitHub Actions. Examples: adversarial-review (spawns fresh-eyes subagent to critique, iterates until findings degrade to nitpicks), code-style, testing-practices.

### 7. CI/CD and deployment

Skills that help fetch, push, and deploy code. May reference other skills to collect data. Examples: babysit-pr (monitors PR → retries flaky CI → resolves merge conflicts → enables auto-merge), deploy-service (build → smoke test → gradual rollout with error-rate comparison → auto-rollback), cherry-pick-prod.

### 8. Runbooks

Skills that take a symptom (Slack thread, alert, error signature), walk through multi-tool investigation, and produce a structured report. Examples: service-debugging (maps symptoms → tools → query patterns), oncall-runner (fetches alert → checks usual suspects → formats finding), log-correlator.

### 9. Infrastructure operations

Skills that perform routine maintenance and operational procedures, some involving destructive actions that benefit from guardrails. Examples: resource-orphans (finds orphaned pods/volumes → Slack → soak → confirm → cleanup), dependency-management, cost-investigation.

## Tips for making skills

### Don't state the obvious

Claude already knows how to code and can read your codebase. A skill that restates what Claude would do by default adds context without adding value. Focus on information that pushes Claude out of its normal way of thinking. The frontend design skill is a great example — built by iterating with customers on improving Claude's design taste, avoiding classic patterns like Inter font and purple gradients.

### Build a gotchas section

The **highest-signal content** in any skill is the Gotchas section. Built up from common failure points Claude runs into. Update over time to capture new gotchas. Examples: "The subscriptions table is append-only. The row you want is the one with the highest version, not the most recent created_at." "This field is called @request_id in the API gateway and trace_id in the billing service. They're the same value." "Staging returns 200 even when the Stripe webhook didn't actually process. Check payment_events for the real state."

### Use the file system and progressive disclosure

Think of the entire file system as a form of context engineering and progressive disclosure. Tell Claude what files are in your skill, and it will read them at appropriate times. Simplest form: point to other markdown files (e.g., `references/api.md`). Can have folders of references, scripts, examples, etc.

### Avoid railroading Claude

Give Claude the information it needs, but give it the flexibility to adapt to the situation. Skills are reusable — being too specific in instructions limits adaptability.

### Think through the setup

Some skills need setup context from the user. Store setup information in a config.json file in the skill directory. If config is not set up, the agent can ask the user. For structured multiple-choice questions, instruct Claude to use the AskUserQuestion tool.

### Write descriptions for the model, not for humans

When Claude Code starts a session, it builds a listing of every available skill with its description. This listing is what Claude scans to decide "is there a skill for this request?" The description field is not a summary — it's a description of **when to trigger** this skill. Include triggers (like "babysit") in the description.

### Help Claude remember

Some skills can include a form of memory by storing data within them — append-only text log files, JSON files, or SQLite databases. A standup-post skill might keep a standups.log with every post it's written, so next time Claude reads its own history and can tell what's changed since yesterday. Use `${CLAUDE_PLUGIN_DATA}` for a stable data directory.

### Store scripts and generate code

One of the most powerful tools you can give Claude is **code**. Scripts and libraries let Claude spend its turns on composition — deciding what to do next rather than reconstructing boilerplate. Example: a data-science skill with helper functions for fetching event data, enabling Claude to generate scripts on the fly for complex analysis.

### Use on-demand hooks

Skills can include hooks that are only activated when the skill is called, and only last for the session. Useful for opinionated hooks you don't want running all the time. Examples: `/careful` — blocks rm -rf, DROP TABLE, force-push via PreToolUse matcher (only when touching prod); `/freeze` — blocks any Edit/Write not in a specific directory (useful during debugging).

## Distributing skills

Two ways to share:
- Check skills into repo (under `./.claude/skills`) — works for smaller teams
- Make a **plugin** and use a Plugin Marketplace — better at scale, lets teams decide which to install, includes setup flow

## Managing a skills marketplace

At Anthropic, no centralized team decides which skills go in. Instead, skills emerge organically. Someone uploads to a sandbox folder in GitHub, points people to it in Slack. Once a skill gets traction, they PR it into the marketplace.

## Composing skills

Skills can depend on each other (e.g., file upload skill + CSV generation skill). Dependency management isn't natively built into marketplaces yet, but you can reference other skills by name and the model will invoke them if installed.

## Measuring skills

Use a PreToolUse hook to log skill usage within the company. This reveals which skills are popular or undertriggering compared to expectations.
