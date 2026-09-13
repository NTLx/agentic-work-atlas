---
type: raw
title: "Marketing ops as code: Automating events from planning to follow-up on GitHub"
source: "https://github.blog/ai-and-ml/github-copilot/marketing-ops-as-code-automating-events-from-planning-to-follow-up-on-github/"
author:
  - "Tomoko Tanaka"
publisher: "The GitHub Blog"
published: "2026-09-11"
created: "2026-09-13"
description: "GitHub APAC marketing team将活动策划、注册筛选和会后跟进写成由 Issue、Labels、Actions 与 Skills 驱动的可审查自动化流程。"
tags:
  - "clippings"
  - "agentic-engineering"
  - "machine-readable-processes"
  - "agent-harness"
  - "ai-ready-organization"
  - "marketing-operations"
---

# Marketing ops as code: Automating events from planning to follow-up on GitHub

I run marketing for GitHub in Japan and Korea, and events are the heartbeat of it: a recurring webinar series for enterprise developers, community meetups in Tokyo, invite-only executive sessions in Seoul. What does a developer in this market actually need right now? Which topics are worth an hour of their time, and who should be in the room? I’d happily spend all day on those questions.

What follows the decisions is another matter. Once an event is greenlit, a fixed sequence begins:

- Duplicate a landing page on our event platform.
- Generate a set of UTM-tagged links: one for each channel, each formatted just so.
- Draft the invitation email and file a request with the team that sends it.
- Add the event to two project boards.
- Every morning until the event: download the registrant list, clean it up, post a status update for stakeholders.
- After the event: export the attendees, reshape the list for a CRM upload, tag the right records, and write a report.

While none of these tasks are hard on their own, they’re an opportunity to paste the wrong link, skip a day, or misspell a campaign name that 15 downstream reports depend on.

Here’s the thing: I used to be an engineer. My first career was keeping databases alive on Linux servers for enterprise customers. While my coding may be rusty, I can still see a pipeline begging to be automated. This is where I put [GitHub Copilot](https://github.com/features/copilot) to use and where you could too in your own work.

So I didn’t write the code. I wrote down my runbooks, handed them to GitHub Copilot, and grew the automation in conversation. Today, an event I used to assemble by hand over a couple of days sets itself up from a single GitHub Issue, screens its own registrants every morning, and cleans up after itself when it’s over.

This post walks through how that works, and why I think anyone whose job involves repetitive work across tools that offer any scriptable way in (an API, or even just a CLI) can do the same.

## An event is an issue

I can’t claim the foundational idea as my own. Marketing teams at GitHub already had a habit of opening one GitHub Issue per project. This becomes the place where the plan, the discussion, and the status live together. The issue was already our unit of work. What I did was make the issue do the work.

Three GitHub primitives carry the whole system:

- **Issue forms are the application form.** Instead of a blank text box, an [issue form](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms) presents structured fields: event title, date, region, campaign name, target audience. We have one form per event type, such as webinars and in-person events, and they feed the same machinery.
- **Labels are the switches.** A label like `event-setup` isn’t a tag, it’s a trigger. Each automation workflow starts with a condition that says, in effect, “only run when this label is present.”
- **Actions are the machinery.** [GitHub Actions](https://docs.github.com/en/actions) workflows fire when labels land, parse the form fields out of the issue body, and go do the work.

Everything a repository gives developers, it gave my marketing workflow for free: history, visibility, review, and a URL for every decision.

One thing made this possible, and it has nothing to do with events specifically: **our event management platform exposes an API**. Our CRM doesn’t even need one; its official CLI covers everything we do, and I never configured an API key for it, because the CLI signs in through the browser and handles authentication from there. API or CLI, the requirement is the same: a scriptable way in. If your repetitive work runs through a tool that offers either an event platform, a CRM, a form builder, an analytics service, the pattern in this post applies to you.

A developer reading this may already be composing the obvious objection: isn’t this reinventing the wheel? Marketing automation platforms exist, and a good one might have covered some of this out of the box. But APAC is less one market than a collection of very different ones, and even within my own team, workflows shift with each sub-region and each segment. The same webinar might run in Japanese for Tokyo one month and in Korean for Seoul the next, with different segments, different fields in the CRM, and a different definition of a good lead. Getting a packaged tool to absorb all of those variations means customization budgets, consulting hours, and waiting on someone else’s roadmap. Building it ourselves, from the tools already at hand, means a workflow change is a pull request: I describe what I want, a reviewer checks it, and it lands on the main branch through exactly the process developers use to change software.

## Planning an event is a conversation

The pipeline starts before the Issue exists. I open GitHub Copilot and say, roughly: “I want to run a webinar about AI-assisted development in November.”

What happens next is shaped by a file called `AGENTS.md` at the root of our repository. It’s our team runbook, written in plain Markdown, that defines how we name campaigns, how fiscal quarters map to dates, which time zone each region uses, and what a good invitation email looks like. GitHub Copilot reads it, and then, it finds a similar past event, proposes a campaign name that follows our naming rules, drafts two versions of the invitation email, and asks me the questions the runbook says to ask.

Putting a conversation at the front of the pipeline was itself a design decision, and it solved two problems at once. Automate everything, and you lose flexibility; the day you want this one event to be slightly different, a rigid pipeline has no place to say so. But if you let humans fill in everything, you get mistakes. The conversation sits exactly between the two. GitHub Copilot follows the template, so the data that lands in the Issue is the right data in the right format. And because it’s a conversation, I can bend the details for this one event without breaking the machinery downstream.

When we started, this conversation happened in [GitHub Copilot CLI](https://github.com/features/copilot/cli), in a terminal. That was fine for me, but “open a terminal” is a barrier for many people I’d love to bring into this workflow. With the [GitHub Copilot app](https://github.com/features/ai/github-app), the same conversation now happens in a regular desktop window. The barrier to entry dropped from “comfortable with a shell” to “can type.”

I want to be precise about the division of labor, because it’s the whole point: **GitHub Copilot drafts; I decide**. Every campaign name, every email subject line, every date gets my sign-off before anything moves. At the end of the conversation, GitHub Copilot files the GitHub Issue with the right labels, and that’s when the machines take over.

## One label, one event, fully staged

The moment the `event-setup` label lands on the issue, a GitHub Actions workflow picks it up and does, in a few minutes, what used to take me the better part of a day:

- Duplicates a past event on our event platform to create the new landing page
- Generates the full set of UTM-tagged URLs: one per channel, consistently formatted, every time
- Produces the invitation email as a Word document and commits it to the repository
- Opens request Issues with the teams that send emails and track regional marketing
- Adds the event to our project boards and fills in the fields
- Posts a summary comment back on the Issue, so the next human who opens it sees everything in one place

Registration screening runs on a schedule instead of a label. Every morning, a cron-triggered workflow fetches the latest registrants for every open event and shares the cleaned-up list. For invite-only events, it also screens the waitlist against our criteria (is this registrant a developer at an enterprise account, a student, or a competitor who would very much like to attend our executive briefing?) before anyone gets approved.

The design decision I’m most proud of is a single on/off switch called `DRY_RUN`, stored as a setting (in GitHub terms, a repository variable) that every workflow checks before it runs. Flip it on, and every workflow goes through the motions without touching any external system: no landing pages created, no issues filed in other repositories, no lists shared. When you’re a team of marketers automating your own job, you need a way to rehearse. `DRY_RUN` is the rehearsal switch, and it’s the reason I was never afraid to experiment.

## After the event, a slash command

Post-event work used to be the worst part: exporting attendees, reformatting columns for the CRM upload, matching company names against account records, and writing the report. Now it’s two commands.

`/lead-upload` fetches the attendee list, shapes it into the exact format our marketing operations team needs for a CRM upload, files the request Issue, and closes out the tracking issues. `/event-report` pulls attendance metrics and survey results and posts a report as a comment on the event’s Issue, back to the one URL where everything about this event lives.

These are [GitHub Copilot agent skills](https://docs.github.com/copilot), and here is the part I most want you to hear: a skill is a Markdown file. Each one is a `SKILL.md`: a written procedure, in prose, that tells GitHub Copilot what to do, in what order, and what to watch out for. Mine read like the runbooks I used to keep in my head, because that’s what they are.

If you can write a runbook, you can write a skill.

Skills are also what keeps the system flexible. No two markets in the Asia/Pacific (APAC) region run their follow-up identically. Audiences differ, segments differ, local conventions differ, and a hard-coded workflow would force every market into one shape. A procedure written in Markdown is flexible: each market can adapt the runbook to its own reality without touching the machinery underneath. That is precisely why the post-event steps live in GitHub Copilot skills rather than in fixed pipelines.

We treat skills like code in one respect: new ones arrive by pull request and get reviewed before they’re merged, with a `CODEOWNERS` file routing the review to a maintainer. Marketing automation with an approval process. The governance came free with the platform, too.

## Built-in guardrails let me experiment

I automated a workflow that touches customer data and API credentials, in a repository my whole team can see, while barely writing code myself. Six months ago I would have said that combination was reckless. What changed my mind was realizing how many guardrails were already in place before I showed up.

Some guardrails I built: the `DRY_RUN` switch, a test suite that runs on every pull request, and code review for every change. Standard developer habits. It turns out they protect marketing work just as well as they protect software.

But the guardrails that mattered most came with the platform:

- **Secret scanning with push protection.** The nightmare scenario for someone in my position is committing an API token by accident. GitHub’s [push protection](https://docs.github.com/code-security/secret-scanning/introduction/about-push-protection) blocks the push before the secret ever lands in the repository, and for GitHub’s own tokens, even one that does slip through gets revoked automatically.
- **GitHub Copilot’s data policies.** Registrant lists are business data, and the fixed scripts handle them in fixed ways. But real work is never entirely fixed; some days I need a one-off cut of the data that no script anticipates. Because GitHub Copilot’s business plans don’t retain prompts or use them to train models, I could ask for that one-off analysis directly, instead of doing what people all over the industry quietly do: pasting business data into whatever consumer chatbot is open in the next tab. The same goes for the models themselves: which ones I can use at all is set by organization policy, not left to my personal judgment, so even a one-off experiment runs inside boundaries the company has already decided. The safe path and the easy path were, for once, the same path.

One more thing the skills made possible, almost as a side effect: because each procedure is now a named, fixed unit of work, I can match the model to the job, choosing from the lineup our organization has approved. A fast, inexpensive model handles the daily list-cleaning; a stronger one drafts campaign copy.

And one honest failure, so you don’t repeat it: the morning screening workflow once failed silently for five days before anyone noticed the lists had gone stale. Automation you don’t monitor is more of a time bomb with a delay. Give every scheduled workflow a way to complain loudly so you don’t miss it.

## Start with one task

Here’s what I’d suggest, from one recovering manual-worker to another.

Pick the single most repetitive task in your week. Then check whether the tools it touches have an API or a CLI. You may be surprised how many do.

Then build the smallest possible version: an issue form that captures the inputs, a label that means “go,” and an Action that does one step of the work. Or skip straight to writing your runbook down as a `SKILL.md` and let GitHub Copilot execute it. Run it with a dry-run switch until you trust it. Grow it from there.

I didn’t write the code. I wrote down what I already knew (how the work gets done) and the platform did the rest. Whatever your version of the morning registrant list is, it’s probably one written-down runbook away from doing itself.

**Get started:**

- [Syntax for issue forms](https://docs.github.com/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms)
- [GitHub Actions documentation](https://docs.github.com/actions)
- [GitHub Copilot documentation](https://docs.github.com/copilot)
- And the blog post that convinced me this works: [I automated my job (and it made me a better leader)](https://github.blog/developer-skills/github/i-automated-my-job-and-it-made-me-a-better-leader/)

