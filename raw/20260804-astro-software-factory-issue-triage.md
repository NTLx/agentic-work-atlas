---
type: raw
source: "https://blog.cloudflare.com/astro-issue-triage/"
author:
  - "Matthew Phillips"
published: "2026-08-04"
created: "2026-08-05"
tags:
  - clippings
  - cloudflare
  - agents-week
  - software-factory
  - issue-triage
  - open-source-maintenance
  - flue-framework
---

# How we built a software factory to drive Astro's GitHub issue count to zero

> Source: [blog.cloudflare.com/astro-issue-triage/](https://blog.cloudflare.com/astro-issue-triage/)
> Author: Matthew Phillips
> Publisher: The Cloudflare Blog
> Date Published: 2026-08-04
> Tags: Agents, Agents Week, AI, Cloudflare Workers, Developer Platform, GitHub, Open Source

> By replacing manual issue verification with isolated AI subagents running in GitHub Actions, the Astro maintainers reduced open issue count by 85%. This post explores the architecture behind automated bug reproduction, patch verification, and preview releases.

## Introduction

Everyone is talking about software factories: the idea that AI agents can be assembled into a pipeline that produces working software on their own, the way a factory turns raw materials into finished goods. There's endless debate over whether that's actually possible, how far the automation can really go, and whether the "loops" people are demoing count for anything. Some have already written them off as a failure.

Running alongside that is a quieter, more worried conversation: open source maintainers are burning out. The AI boom has made it nearly free to generate issues, pull requests, and security reports, and enormously expensive for a maintainer to read through them all. The old ways of keeping a project healthy are buckling under the volume.

Everyone has a hot take on both topics. We think we have something rarer to offer: real results. For the past several months we've run an automated triage pipeline on the Astro repository. It reads incoming bug reports, reproduces them in sandboxes, diagnoses the root cause, and ships preview releases for the reporter to verify. The engine underneath it grew into [Flue](https://flueframework.com/), an open framework for building this kind of agent automation, and it's the same tool you could use to build your own.

### Key Results

> It wasn't an instant success. But through a lot of iteration, we've used it to bring our open issues down from over 200 to about 30, and we expect to hit zero sometime in the next month. That would be the first time this repository has seen zero open issues in its 5+ year history.

> We didn't get there by declaring "issue bankruptcy," auto-closing cold tickets, or ignoring reports. We did it by automating issue triage with a team of isolated AI subagents running right inside GitHub Actions.

## Section: Starting with an agent skill

At the start of the year, we focused on automating one specific area of development: issue triage. As an open source project, manual issue triage can be one of the more time-consuming, least-rewarding parts of the job. A single issue can sometimes take hours just to reproduce, let alone fix. It was a natural (yet often overlooked) place for us to start our automation journey.

We began by developing an agent skill. This allowed us to develop and test the automation locally as maintainers, running a coding harness on our own machines. We could then run that same harness in a GitHub Action on our repo, and get total reuse of that exact same triage workflow skill.

**The triage skill mirrors the exact steps we take during manual issue resolution:**

1. **Reproduce**: Clone the provided reproduction repository to verify the reported issue.
2. **Diagnose**: Instrument the codebase and introduce logging to pinpoint the root cause of the bug.
3. **Verify**: Review relevant test suites, code comments, and documentation to determine if the behavior is genuinely a bug or intended functionality.
4. **Fix**: Convert the reproduction into failing unit tests, identify the appropriate solution via the architecture guide, and deploy the fix.

> To prevent the frequent LLM bias toward forcing a solution when a bug might not actually exist, each phase is executed by an isolated subagent. These subagents pass information forward sequentially by compiling their discoveries into a **report.md** file.

## Section: Turning the skill into an automation

Following initial internal testing of the triage skill, our focus shifted toward building a fully automated pipeline. We specifically wanted to integrate this logic directly into a GitHub workflow, ensuring complete transparency so that anyone could easily audit the agent's sequential reasoning and operational steps.

As we wired it up, we realized the whole pipeline was really just a state machine **driven by issue labels**. Every new submission starts with the label `triage needed`, and once a user confirms a fix it moves to `fix verified`. Beyond those label transitions the pipeline holds no state of its own; it simply reads back through the issue's existing comments to work out where a given issue is and what should happen next.

> When the agents land on a fix, the pipeline spins up a preview release with pkg.pr.new and posts everything back to the issue: a summary of what it found, the full logs, and instructions for installing the preview. The original reporter can then try the patch against their own project, and if they confirm it works, the automation opens a pull request linked to the issue.

## Section: From triage to a framework

As we built this out, we kept noticing that nothing about it was really specific to GitHub. Reacting to an event, running a sequence of isolated subagents, and separating their reasoning from the actions they're allowed to take — it's all just a workflow. One that could run just as well from a Slack message, a cron job, or a webhook as from a GitHub issue. Generalizing that realization into a runtime that works the same way regardless of where it's deployed, or which model it's driving, is what became [Flue](https://flueframework.com/): an open, platform-agnostic framework for building durable agents and workflows.

## Section: Benefits of agent automation

When we first launched this automated system, we had shared concerns about its efficacy and the potential negative impacts it might have on our developer community. There was a valid fear that relying on automated bot responses might feel impersonal and create just one more disconnect between us as maintainers and our user base.

That did not happen. If anything, we talk to users more now, just in more useful places:

- Engaging directly with our community members within Discord.
- Actively participating in RFC discussions and addressing new feature requests.
- Collaborating closely with contributors to help integrate their ideas into the framework.

Regarding the quality of automated patches, our core philosophy is that our AI agents should successfully resolve the vast majority of incoming issues. When an agent fails to identify a correct solution, we interpret that failure as an indicator of an underlying architectural or documentation issue within the codebase, pointing to one of three areas:

- **Opaque Abstractions**: If an agent cannot interpret the boundaries between components, human developers likely struggle with the code structure as well.
- **Missing Documentation**: Critical code segments lack explicit comments explaining the rationale behind their implementation.
- **Insufficient Testing**: The repository suffers from a lack of comprehensive test coverage, particularly unit tests.

### Concrete Example (HMR bugs)

> A clear example occurred with a series of related Hot Module Replacement (HMR) bugs. The triage bot repeatedly attempted to modify a specific if condition to resolve the issue. While this change fixed the targeted bug, it introduced regressions elsewhere due to a lack of test coverage for that specific condition. Once we added a descriptive comment explaining the exact logic governing that statement, the bot adapted and stopped attempting incorrect modifications in that area.

> Every time we chase down one of these failures and add the missing comment, test, or clearer boundary, the bot gets noticeably better at that part of the codebase, and so does the next human who works on it.

## Section: Turning the workflow into a GitHub Action

Initially, our triage logic lived directly within the Astro monorepo. This coupling made iteration difficult; upgrading Flue or modifying the workflow felt like performing surgery on live infrastructure without a safety net. To solve this, we decoupled the logic into a standalone, testable repository: [triagebot-action](https://github.com/withastro/triagebot-action). This isolation allowed us to introduce automated testing and ensure stability before ever touching our primary codebase.

Today, this action powers issue management in Astro, and it has spread from there. Several other teams have picked it up, some using it directly, and others forking it to build their own automated "factories" tailored to their projects. That second path is really the point: triagebot-action is young and still actively evolving, so we're sharing it less as a finished product and more as a working reference you can read, learn from, and adapt.

**The wiring for the action itself looks like this:**

```yaml
- uses: withastro/triagebot-action@v1
  with:
    read-token: ${{ secrets.GITHUB_TOKEN }}
    write-token: ${{ secrets.BOT_GITHUB_TOKEN }}
    cloudflare-api-key: ${{ secrets.CLOUDFLARE_API_KEY }}
    cloudflare-account-id: ${{ secrets.CLOUDFLARE_ACCOUNT_ID }}
    triage-model: cloudflare-workers-ai/@cf/moonshotai/kimi-k2.7-code
    verification-model: cloudflare-workers-ai/@cf/moonshotai/kimi-k2.6
    triage-skill: .agents/skills/triage
```

Or point your own agent at the repository and have it read through the setup, including adding the labels the state machine relies on.

> Whichever route you take, the underlying idea matters more than our specific implementation: a sustainable feedback loop that frees maintainers to focus on the framework itself instead of administering a backlog. The code is open. Fork it, strip it down, or just borrow the parts that fit your project.

## Call to Action

**Want to build something like this?** Dig into the code of the [triagebot-action](https://github.com/withastro/triagebot-action) to see how it works, or fork it as a starting point for your own repository's automation. And if you're building agent-based infrastructure more seriously, that's exactly what Flue is for: dive into the [Flue framework](https://flueframework.com/) to build your own. We'd love to see what you build. Come share your "factory" stories in the [Astro Discord](https://discord.cloudflare.com/).

## Key Mechanism Summary

| Stage | Description |
|-------|-------------|
| **Trigger** | New GitHub issue with label `triage needed` |
| **Reproduce** | Clone repro repo, isolated subagent verifies bug |
| **Diagnose** | Instrument code, isolated subagent finds root cause |
| **Verify** | Subagent checks if behavior is bug or intended |
| **Fix** | Subagent writes failing tests + implements fix |
| **Preview** | Pipeline spins up preview release via pkg.pr.new |
| **Confirmation** | Reporter verifies fix; pipeline opens linked PR |
| **State Tracking** | GitHub issue labels + comment history (stateless pipeline) |
| **Communication** | Isolated subagents pass findings via report.md |

## 关键论断

1. **状态机由 issue labels 驱动，pipeline 不保存自己的状态**——每一步靠读取现有 comments 推断位置。最大化可审计性。
2. **隔离子代理（isolated subagents）是为了反 LLM 的"必须解决问题"偏见**——每个阶段独立，串行通过 `report.md` 传递发现。
3. **Agent 失败被重新定义为架构信号**：失败指向三类问题——不透明抽象、缺失文档、测试不足；bot 变强 = 代码库变可读。
4. **Flue 抽象的核心**：从具体平台（GitHub issue）抽取 workflow 模式——触发 + 隔离子代理 + 推理/操作分离 + 跨平台 runtime。
5. **85% → 接近零，5+ 年来首次清零**——不是 issue bankruptcy，而是真自动化（隔离子代理 reproduce → diagnose → verify → fix → preview release → reporter 验证 → 开 PR）。