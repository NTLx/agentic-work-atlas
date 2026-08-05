---
type: raw
source: "https://blog.cloudflare.com/agent-development-lifecycle/"
author:
  - "Brendan Irvine-Broque"
published: "2026-08-04"
created: "2026-08-05"
tags:
  - clippings
  - cloudflare
  - agents-week
  - adlc
  - software-factory
  - sdlc
  - workflows
---

# The Agent Development Lifecycle has arrived on Cloudflare

> Source: [blog.cloudflare.com/agent-development-lifecycle/](https://blog.cloudflare.com/agent-development-lifecycle/)
> Author: Brendan Irvine-Broque
> Date: 2026-08-04

> Agents can write code faster than teams can review, deploy, and maintain it. Today we're introducing the Agent Development Lifecycle and the Cloudflare primitives that underpin it.

## 正文

Engineering managers spent the past few decades figuring out ways for many programmers to work together on a shared codebase. This work dates all the way back to the "Systems Development Lifecycle" (RAND, 1975) - today commonly referred to as the "Software Development Lifecycle" (SDLC), which defines the following phases:

- Plan
- Design
- Implement
- Test
- Deploy
- Maintain
- Retire

AI has made the step that was previously the slowest and most expensive — implementation — the fastest and cheapest. That, in turn, has had an impact downstream: overwhelming the people responsible for all the other steps in the SDLC. This ranges from open-source maintainers bombarded with thousands of pull requests and issues, to production engineers trying to save production from falling over as the rate of software delivery increases orders of magnitude.

> "We are all trying to save our systems, our customers, and ourselves from slop."

The answer — paradoxically — is to empower agents to do more. It's only fair! You'd never let an engineer on your team write code, expect someone else to validate it, merge it, deploy it, hold the pager in production, and triage incoming bugs. But that's what most companies are doing right now with agents. Models have improved remarkably, and agents are running over longer time horizons, able to take on much larger tasks. But they are not yet used evenly across the SDLC.

Cloudflare treats agents as our customers. They can buy domains, create temporary accounts and use the entire Cloudflare API. We know that agents need APIs and tools to be able to manage the full SDLC on behalf of our customers — not just the start of it.

And so today we're introducing the start of a new set of tools that let agents step beyond just generating code and take on more of the SDLC:

- **@cloudflare/ci** — a new way to run CI/CD across millions of repos, that can self-heal and spawn agents to do much more complex tasks, build on Cloudflare Workflows.
- **OpenTelemetry traces in local dev** — giving agents the same observability they have in production, built into Wrangler and the Cloudflare Vite plugin.
- **Introducing: Cloudflare Agents and Agent Traces** — a new home for observing, maintaining and improving agents, centered around OpenTelemetry traces from agents.
- **How Cloudflare enforces engineering standards using AI** — our own experience enforcing best practices across all of our products' and systems' repositories and specs.
- **How we built a software factory to drive Astro's GitHub issue count to zero** — our own experience building systems to automatically triage, reproduce, verify and fix issues for a large and growing open source project.

There's something bigger here though. When we look at the SDLC, even with the best automation, its assumptions do not scale for the volume of code agents can write and the pace at which software teams must move to compete. We think it's time to replace the SDLC with the ADLC — the Agent Development Lifecycle.

## The SDLC is for software teams. The ADLC is for software factories.

Right now, everyone is talking about building "software factories" — agent-driven systems that take input and autonomously build, improve, deploy and manage software. Take an input, whether it's a production error, a bug report from a customer, or an idea for a new feature, and delegate it entirely to an agent.

Even with agents, most software projects are constrained by human-in-the-loop steps. Humans prompting agents, telling them to keep going, instructing agents to apply feedback from a code review, constantly babysitting many agents and giving them instruction. On most software teams, the human still manages each step in the SDLC model — the only change is that they delegate tasks within each step to an agent.

And so the dream behind software factories is: what if you reimagined this approach and built a factory for the entire process of building software? How can we shift more human time towards the things that truly require human inspiration, taste, and judgement? It would leave us more time to design, to talk to customers, and to dream bigger.

A software factory has to manage the same steps in the SDLC, but it demands much more from the platform it is built on. Because when you hand over the keys and let the agent drive, every manual step that previously relied on a human must be adapted to be:

- **Programmatic** — "ClickOps" was bad practice for humans, but it's a non-starter for agents. Every last operation needs APIs that agents can call, debug, and rely on.
- **Horizontally scalable** — preview deployments were a nice-to-have when humans stared at the screen while building or manually took over a staging server to catch issues before production. For agents to drive, every agent must have its own preview that matches production.
- **Reproducible** — what happens if there's a bug that you can only reproduce when simulating 4G on an iPhone 15? Or from an IP in a certain country? Typical unit testing and integration testing tools aren't going to help here.
- **Real-time, push based** — relying on humans to look at the right dashboard has always been a bad way to know if things are working, but it completely breaks down with agents. You need an event that triggers an agent to do work.
- **Atomic** — every change needs to be independently testable, releasable, observable, and reversible without affecting unrelated behavior.
- **Permissioned** — you know you probably shouldn't, but today you give a few trusted engineers the keys to SSH into prod in case things really go haywire. There's no way you let an agent do that — but without the ability to escalate and get more permissions, how can it do its job?
- **Self-improving** — people learn from experience. The first week ship or the first on-call rotation, humans are slow and need to shadow someone else, but then get better and faster. Agents, too, need ways to learn from experience.

We need something new if we are going to make software factories safe to use for real production software. Software factories face the same challenge that other autonomous systems like self-driving cars do — the challenge of going from working successfully 80% of the time, to some number of nines past 99%.

## To give agents the keys to drive the SDLC, you can't give them a car designed for humans

An autonomous vehicle is loaded with sensors and technology that a regular car doesn't have. Lidar sensors, cameras, powerful compute to run inference, and connectivity to a central command system that can take over remotely if needed.

For an autonomous vehicle to be 80% as good as a human at driving, we probably don't need all of this. Self-driving got to around 80% as good as humans 10 years ago. But that's not the bar to clear — the bar is to be much better and safer than a human driver. That's what we expect when we hand over the keys to a machine, in order to feel safe taking a nap driving down the 101 at 60 mph. And that's why autonomous vehicles have technology that is purpose-built for self-driving — it's what builds trust and handles the edge cases that cannot be designed for upfront.

The same is true of self-driving software. Ask yourself — why _haven't_ you yet just let your agent auto-approve and merge its own PRs to your production services? The higher the stakes of what you build, the longer your list of reasons almost surely is.

When you start to unpack not only all the things that can go catastrophically wrong in this process, but also that are necessary to building the right thing for customers, it is remarkably complex. It doesn't fit into a linear set of steps in a GitHub Actions YAML file, and it goes way beyond running traditional automated tests. Even a small change to a dashboard can span roles, specializations and org structures, and subjective changes are the hardest to test and to delegate. Most of these things are probably not part of your CI/CD pipeline at all today. But they will need to be, if you want them to still happen, while giving full control to the agents running the software factory.

To let agents drive the whole process, we need a better way to orchestrate these dynamic series of steps. We think that is a Workflow, with the capability to spawn containers, agents and browsers. A Workflow that can set feature flags and enable them for a test user, investigate logs and traces, observe production metrics as a change gradually rolls out, and do everything else that is needed in order to ship safely.

## A CI/CD pipeline is just a Workflow. But a Workflow can be so much more than a CI/CD pipeline.

Cloudflare Workflows let you chain together multiple steps, automatically retry failed tasks, and persist state for minutes, hours, or even weeks. They are designed to encode complex and dynamic business processes in a logical and well-understood program. This blog post breaks down why Workflows, in tandem with Artifacts, make defining and triggering CI/CD pipelines fundamentally simpler. For example:

```typescript
import { CIWorkflow } from `@cloudflare/ci`

const deps: CiRunnerResult = await ci.runner({
      name: 'install',
      command: 'bun install --frozen-lockfile',
      cache: { inputs: ['package.json', 'bun.lock'] },
    });

    await Promise.all([
      deps.runner({ name: 'lint', command: 'bun run lint' }),
      deps.runner({ name: 'test', command: 'bun run test' }),
      deps.runner({ name: 'typecheck', command: 'bun run typecheck' }),
      deps.runner({ name: 'build', command: 'bun run build' }),
    ]);

    await deps.runner({
      name: 'deploy',
      command: 'bun wrangler deploy',
      cloudflareCredentials: {
        accountId: this.env.CLOUDFLARE_DEPLOY_ACCOUNT_ID,
      },
    });
```

Workflows go beyond a series of linear steps though. They can be defined dynamically, and they can spawn agents or other Workflows. This example shows a Workflow that reviews new data from the past day. The Workflow has full control over when and how the agent is prompted, and can pass along context between steps:

```typescript
import { WorkflowEntrypoint, type WorkflowEvent, type WorkflowStep } from 'cloudflare:workers';
import { init } from '@flue/runtime';
import { Reviewer } from './agents/reviewer.ts';
import { collectFindings } from './shared/nightly.ts';

type Params = { date: string };

export class NightlyReview extends WorkflowEntrypoint {
  async run(event: WorkflowEvent<Params>, step: WorkflowStep) {
    const findings = await step.do('collect findings', () => collectFindings(event.payload.date));

    const agent = init(Reviewer, { id: `nightly-${event.payload.date}` });

    const receipt = await step.do('dispatch review', () =>
      agent.dispatch(`Review these findings:\n${findings}`),
    );

    const review = await step.do('read review', async () => {
      const reply = await agent.read(receipt);
      return { text: reply.text, data: reply.data };
    });

    // ...
  }
}
```

Once you see this pattern, and are "Workflow-pilled" as Cloudflare is, you start to ask: what else could I have a Workflow handle for me? What other human-bottlenecked steps could I delegate to this combination of Workflow + Flue agents?

## The full ADLC, on the Cloudflare stack

With Workflows able to orchestrate complex steps, and Artifacts as the storage layer for code, when you look at the SDLC stages, everything an agent needs to own the whole process of building, shipping, and maintaining software is on Cloudflare:

| SDLC stage | Cloudflare |
| --- | --- |
| Plan / Design / Implement | Vite, Rolldown, and Oxc — the fastest toolchain for your agent; Local dev for everything — what your agent sees locally, is the same runtime and environment that will run in production; Local Explorer, Local Traces — your agent has the same APIs to debug locally as it does in production; Remote bindings — let agents run code locally, while using real production resources running on Cloudflare; Preview URLs — give every pull request a preview for the agent to validate and use |
| Test | Browser Run — programmable headless browsers in the cloud; Vitest — run tests in the Workers runtime |
| Deploy | Flagship — every change gets its own feature flag; Gradual Deployments — roll out code changes to a percentage of traffic, ramp up over time |
| Maintain / Retire | Workers Logs — let agents tail live logs or query adhoc to identify issues to automatically fix; Agent Traces — capture every agent session and use it to improve; Cloudflare MCP Server — powered by Code Mode and Dynamic Workers; Analytics Engine — high cardinality analytics built on Clickhouse, to let agents query who is using what |

## Primitives to build your software factory

Right now, the people on the bleeding edge are building the software factories of the future. Eventually software factories will become, just like agents and AI, the normal way people build software. But for most people and most organizations, we're not there yet.

We want to change that.

In order to do so, the questions we've asked ourselves are: how can we make things simple and accessible so that everyone on the Internet can benefit from a paradigm shift like this? And what are the base layer primitives that we can open up to everyone, from the smallest startup to the largest platforms in the world?

In this case, we think the primitives are here. There's more to do to connect them, to keep building our own software factory and learn from it, but right now, today, we're ready for you to build your machine that builds the machine, on Cloudflare. Get started with @cloudflare/ci, build an agent, and see how much of the SDLC you can make autonomous.

## 关键引用

> "We are all trying to save our systems, our customers, and ourselves from slop."

> "The SDLC is for software teams. The ADLC is for software factories."

> "To give agents the keys to drive the SDLC, you can't give them a car designed for humans"

> "A CI/CD pipeline is just a Workflow. But a Workflow can be so much more than a CI/CD pipeline."

## 关键论断

1. **SDLC → ADLC 的范式跃迁**：SDLC 假设是"人协作写代码"，ADLC 假设是"agent 驱动流水线"。文章给出七个软件工厂的硬性需求（programmatic / scalable / reproducible / real-time / atomic / permissioned / self-improving）。
2. **AI 让最慢最贵的 implement 变成最快最便宜，下游所有环节超载**：开源 maintainer 被 PR/issue 淹没，生产工程师被交付速率压垮——这是 OpenAI/Anthropic 之后一年里浮出水面的"实现加速悖论"。
3. **Cloudflare 把 agent 当一等公民客户**：它们可以买域名、建临时账号、调整个 Cloudflare API。"agents as customers" 是把 ADLC 推到产品层的具体动作。
4. **80% → 99%+ 的桥 = 自治系统（自驾车类比）**：不能拿人类车给 agent 跑，要给它 lidar/compute/remote takeover——这不是修辞，是 Cloudflare 拿来类比 Agent Traces、Remote Bindings、Permission escalation 的真实架构图。
5. **Workflow 是新 CI/CD**：CI/CD 是 workflow 的子集；Cloudflare Workflows 持久化状态、可嵌套、动态生成，可 spawn agents/containers/browsers，配合 Artifacts 构成新的存储层。
6. **ADLC × Cloudflare 全栈映射**：从 Vite/Rolldown（最快工具链）→ Browser Run/Vitest（测试）→ Flagship/Gradual Deployments（部署）→ Workers Logs/Agent Traces/MCP/Analytics Engine（运维）——一张端到端的"agent 自己开车"栈图。
7. **Astro 案例是 ADLC 的现实注脚**：上篇文章里的 Flue + triagebot-action + 状态机 + 隔离子代理，就是 ADLC 在 OSS 维护场景的落地。

## 相关标签

Agent Development Lifecycle, Agents, Agents Week, AI, Browser Run, Cloudflare Workers, Developer Platform, DevOps, MCP, Observability, Product News, Tracing, Workflows