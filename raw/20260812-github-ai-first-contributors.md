---
type: raw
source: "https://github.blog/open-source/maintainers/your-contributors-are-ai-first-now-is-your-project/"
author:
  - "Andrea Griffiths"
published: "2026-08-12"
created: "2026-08-13"
tags:
  - clippings
  - github
  - open-source
  - agent-generated-prs
  - maintainers
---

# Your contributors are AI-first now. Is your project?

> Source: [github.blog](https://github.blog/open-source/maintainers/your-contributors-are-ai-first-now-is-your-project/)
> Author: Andrea Griffiths（受访者 Nicholas Tindle, AutoGPT 创始 AI 工程师）
> Date: 2026-08-12

## 正文

The same question keeps coming up in maintainer conversations: what do you do when the pull request queue fills with work written by agents?

It’s something Nicholas Tindle, founding AI engineer at AutoGPT, also deals with every day. [I spoke with him in May](https://www.youtube.com/watch?v=Ro_VMXWbLt8&list=PL0lo9MOBetEFmtstItnKlhJJVmMghxc0P&index=14) for Maintainer Month. At the time of the interview, AutoGPT had over 180,000 stars and around 150 open pull requests. A big chunk of those pull requests were written by agents, including Copilot, OpenClaw, and AutoGPT’s own internal tooling, among others. Most maintainers I talk to have the same reaction: close the door. Turn off pull requests. Don’t tax the team with reviewing slop.

Nicholas saw an upside:

> It’s basically somebody else paying for your compute.
>
> Nicholas Tindle, founding AI engineer at AutoGPT

The way he sees it, if a contributor wants to spend their tokens improving your project, let them. Just make it so the only way through the door is the way that works for you.

## Your docs aren’t the problem. Discovery is.

AutoGPT tried the obvious thing first. Better contributor guidelines. Better docs. A whole wiki dedicated to working with the repo.

None of it moved the needle. It turns out the tools aren’t going to go read your docs unless they’re told to. That’s the part a lot of us get wrong. We treat documentation like the agent will go find it. It won’t. Agents read what’s in front of them, at the level of the directory they’re working in.

So AutoGPT started putting instructions where agents look. First `CLAUDE.md` files, because Claude was generating pull requests without enough repository-specific context. The commit trailer made each one easy to spot, because they announced themselves in the commit trailer. Then they hit the next wall: Copilot and Codex ignore Claude files, because they’re not Claude. So they centralized the standard `AGENTS.md` and pointed Claude files at it.

Here’s the nuance I found most useful. `AGENTS.md` is scoped to a directory. A skill can be discovered outside that directory. (If you haven’t shipped one: a skill is an instruction file with a description that tells the agent when to load it. The agent scans descriptions up front and pulls in the full instructions when the task matches.)

AutoGPT’s `AGENTS.md` sits beside the code it governs. That placement matters as much as the instructions themselves.

> If you’re writing backend tests and you think about doing front-end stuff, a skill may load dynamically. It’s not going to know what directory to go look in for an AGENTS.md file, but the skill can tell it that.

Their front-end engineer got tired of the same class of broken pull request, so they wrote a guide, and shipped it as a skill in the repo. The description contained trigger phrasing: write a Storybook test if your component lives in these folders. Now every harness that touches the repo discovers it automatically. The backend enforces its own version of the rule the same way: hit 80% coverage or don’t open the pull request.

## Gates that actually work

These are the gates you can adapt for your project.

**Enforce the pull request template, loudly.** AutoGPT tells agents that pull requests not matching the template get closed automatically with zero hesitation. They built the tooling to actually do it, then found they didn’t need to run it. At AutoGPT, the rule changed agent behavior before the automation ever ran. The agents followed the template. Human contributors sometimes needed more room, which Nicholas treats as a feature:

> If you don’t follow the template, I know you’re probably a person, and I’m going to be kinder.

**The test plan trick.** The template requires a test plan, and its wording casually mentions testing the pull request. That phrase triggers a skill called `test PR`, which installs agent browser (with permission), spins up the app, and executes the change. The agent set out to fill in a checkbox and ended up running the code.

They almost never get pull requests that don’t work anymore. What they get now is pull requests that work but don’t fit the roadmap, which is a much better problem to have.

**Make CI a wall, not a suggestion.** Codecov coverage thresholds are required checks. The agent opens the pull request, checks back a few minutes later, sees it can’t merge, loads the testing skill, and writes the tests. Nobody had to ask.

**Use the CLA as a human detector.** AutoGPT is dual licensed, but Nicholas argues every project should do this, MIT included. Signing requires a browser and a GitHub OAuth flow on a separate domain. Agents are bad at that today, and for good reason: most maintainers do not want an agent logged into GitHub in a browser with broad account access.

> If your CLA is not signed after a week, we close the pull request with a comment that says sign the CLA, reopen when you’re done.

That gate works because it puts a human back in the loop. A CLA is one option. A code-of-conduct checkbox can do the same job.

**Require a commit SHA before resolving a review thread.** Some agents mark every review thread as resolved without touching the code. AutoGPT’s fix is a `pr-address` skill in the repo that declares the only valid sequence: fix, commit, push, reply, then resolve. The reply has to link the fixing commit, with the full SHA pulled from `git rev-parse HEAD` after committing, so the agent can’t recycle an old one. The skill even names the anti-patterns: “Acknowledged” is not a fix, and neither is citing a commit that doesn’t touch the flagged line.

## The gate they turned off

When a check fails, AutoGPT had an agent read the run and comment on what broke. Their first version wired Claude Code into GitHub Actions and authenticated it inside the workflow, which meant one more broad credential living in CI. Running Copilot in the workflow gets the same result without that. Nicholas is a fan:

> It’s unbelievable. I’m so happy I never had to bother with YAML ever again. I’m never writing a workflow for an action ever.

Then they turned the commenting off anyway. Their CI fails a lot, and a bot narrating every failure all day is not much better than the failure itself. The lesson is the restraint: keep what lowers the maintainer burden, shut off what becomes noise.

## Four gotchas worth writing down

**A bad AGENTS.md file is worse than no AGENTS.md.** AutoGPT littered them everywhere at first and ended up polluting context, pulling the agent’s attention toward files that didn’t matter. If behavior gets worse, go read what you wrote.

**The GraphQL API will rate limit you.** When every tool on your team hits the CLI as an individual user, you hit the ceiling fast. Create a GitHub App and authenticate the CLI through it.

**The heavy review tooling costs real money.** Their pull request test rig clones the branch, spawns eight agents with different jobs, runs the whole stack, and uploads screenshots. It’s great. It’s also expensive enough that they now run it only on very small or very large pull requests.

**Go audit your authorized apps.** AutoGPT is part of the Secure [Open Source Fund](https://github.com/open-source/github-fund), and this was one of Nicholas’s takeaways from that work. Every tool they trialed and dropped left an authorization behind.

> If you stop using a GitHub app, remove it from the authorized apps. Do a little audit right now after this stream and go see what you have. You’ll be surprised.

Logging in with GitHub is so automatic at this point that most of us have never gone back to look. I opened my settings during the stream. He was right.

## Not everything is a gate

Two takeaways from Nicholas had almost nothing to do with tooling.

First: you don’t have to accept every pull request. Merging someone else’s LLM output is asymmetric. You do the upkeep, forever. Closing the pull request and building the fix yourself is a legitimate choice.

You can [disable pull requests entirely](https://github.blog/changelog/2026-02-13-new-repository-settings-for-configuring-pull-request-access/). You can [restrict issue creation to collaborators](https://github.blog/changelog/2026-06-29-restrict-issue-creation-to-collaborators-only/). Nicholas tied those controls back to the thing he kept coming back to in the interview: maintainers need knobs. Sometimes the right answer is fewer drive-by pull requests. Sometimes it’s issues only. Sometimes it’s “talk to us first.”

SQLite doesn’t take external code contributions. They take bug reports. That’s a valid open source boundary. Your project can have one too.

Second: when you close a pull request you’re going to rebuild yourself, add the contributor as a co-author if it makes sense. AutoGPT has around 800 contributors, so one more costs them nothing. For most people, the thing that matters is that their problem got fixed and somebody noticed they showed up.

## What I’m taking back

Open source has always evolved by making collaboration explicit. Licenses made permissions explicit. Issues made work visible. Pull requests made review a shared practice. Instructions in the repo look like another step in that direction, though I’d hold that loosely. Nobody’s landed on the right shape yet. AutoGPT is on its third version, and it got there by shipping bad versions first and watching what agents did with them.

You still decide what belongs. You still set the bar. The difference is that more of that judgment can live next to the code, where your contributors and their agents already are.

Go look at the [AutoGPT repo](https://github.com/Significant-Gravitas/AutoGPT) and read how they structured their agent files.

Then go join [maintainers.github.com](https://maintainers.github.com/). I’d tell you that anyway because I work here, so take it from Nicholas instead:

> You’ve got to go there. You’ve got to sign up. It gets you all the connections you want at GitHub. That’s where I learned about all this stuff, and where I share it.

It’s also where Tiny Wins gets prioritized, the weekly drip of small maintainer-requested improvements. Some of those asks have already shown up in the controls GitHub highlighted during [Maintainer Month](https://github.blog/open-source/maintainers/welcome-to-maintainer-month-celebrating-the-people-behind-the-code/). It’s also where our product managers and engineers read feedback before anything ships. If you want a say in what the platform does for maintainers next, that’s the room. Your contributors are already AI-first. Put the rules next to the code
 before the next pull request lands.