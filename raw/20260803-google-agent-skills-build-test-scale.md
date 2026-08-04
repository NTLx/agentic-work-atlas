---
type: raw
source: "https://dev.to/googleai/behind-the-scenes-how-we-build-test-and-scale-google-agent-skills-1am5"
author:
  - "Remigiusz Samborski"
  - "[[Remigiusz-Samborski]]"
published: "2026-08-03"
created: "2026-08-04"
tags:
  - clippings
  - google-cloud
  - agent-skills
  - context-engineering
  - open-source
  - governance
  - eval
  - ci-cd
  - ai-infra
---

AI agents are only as good as the instructions and context you give them. When we launched [Google Agent Skills](https://github.com/google/skills), our goal was simple: encode Google Cloud domain knowledge into structured, open-source instructions that make AI coding agents significantly smarter, safer, and more accurate.

Today, I want to take you behind the scenes of Google Agent Skills. As a team member working directly on these skills, I will share how we started, how we maintain quality at scale, and how we handle governance for public and internal skills.

## How it started: The Next'26 kickoff swarm

The Google Agent Skills project didn't start in a vacuum. It kicked off as a fast-paced "swarm" effort leading up to Google Cloud Next 2026.

A cross-functional task force led by **Developer Advocates** and **Technical Writers** came together with a clear goal: package Google Cloud domain knowledge into structured, agent-readable instructions.

The launch was announced in the [official Google Agent Skills launch post](https://cloud.google.com/blog/topics/developers-practitioners/level-up-your-agents-announcing-googles-official-skills-repository?utm_campaign=CDR_0x87fa8d40_default_b539420191&utm_medium=external&utm_source=blog). The initial community reception exceeded our expectations with over 15,000 GitHub stars!

[![GitHub stars history for google/skills](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fopgd3rqcax644g29nqyv.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fopgd3rqcax644g29nqyv.png)

Once developers and engineering teams inside and outside Google saw how effectively skills guided AI agents (reducing hallucinations and enforcing best practices), many wanted in. Soon, a wave of product teams wanted to contribute skills for their own Google services (not limited to Cloud, i.e. Ads).

## The challenge: Scaling without losing quality

Popularity brings a major challenge: quality control.

When different teams contribute skills, keeping a consistent standard becomes tough. A poorly written skill with vague instructions, broken links, or missing edge cases degrades the entire agent experience.

To enable teams to publish skills while protecting the developer experience, we had to set a **very high bar**.

This meant the process was critical. Without clear standards and automated governance, an open-source skills repository quickly becomes chaotic.

So let's dive into details of how we maintain quality as we scale.

## The anatomy of an Agent Skill

To keep skills consistent across many Google services, every skill follows a standardized repository layout:

```
{skill-name}/
├── SKILL.md                 # Required: Main instructions & frontmatter metadata
├── OWNERS                   # Required: Skill maintainers (kept internal)
├── EVAL.yaml                # Required: Evaluation prompt suites & rubrics (kept internal)
├── reference/               # Optional: In-depth technical docs & schemas
├── scripts/                 # Optional: Executable helper scripts
├── assets/                  # Optional: Static resources & diagrams
└── _internal/               # Optional: Test mocks & internal data (kept internal)
```

### Architectural best practice: Prefer remote MCP tools

When designing skills, our guiding principle is: **Reference remote Model Context Protocol (MCP) tools whenever possible, falling back to CLI or API calls only when necessary.** Remote MCP servers are best suited for Agentic workloads by providing tools, while also offering built-in auth and IAM governance.

### Public export

We build and evaluate our skills internally first to make sure they work and are properly validated. Once ready to go public, we use automated export rules to publish to GitHub. This keeps public repos clean while stripping out internal assets, ownership information, and evaluation suites.

## Automated checks on check-in

Before any skill enters the repository, it must pass an automated CI/CD pipeline:

- **Linters:** We validate frontmatter metadata, line counts, directory layout, and strict naming conventions.
- **Link Checkers:** We test every URL using link-checking tools to eliminate 404s and hallucinated links before merge. *Hint: if you're building a similar solution I recommend trying out [lychee](https://lychee.cli.rs/).*
- **AI-Assisted Checklists:** We use automated validation checks to verify that instructions follow required structural patterns and guardrails.

### Example GitHub Action for skill linting

While our development relies on Google's internal tooling, public open-source skill repositories can use standard GitHub Actions for CI/CD.

If you are maintaining your own skill library on GitHub, linting is part of a larger check suite to keep a high quality bar. The following GitHub Action configuration demonstrates how to automatically run skill validation in your repository using [skills-ref](https://github.com/agentskills/agentskills/tree/main/skills-ref):

```
name: 'Validate Skills'

on:
  push:
    branches: ['main']
  pull_request:
    branches: ['main']
  workflow_dispatch:

defaults:
  run:
    shell: 'bash'

jobs:
  validate:
    runs-on: 'ubuntu-latest'
    permissions:
      contents: 'read'
    steps:
      - name: 'Checkout repository'
        uses: 'actions/checkout@34e114876b0b11c390a56381ad16ebd13914f8d5' # ratchet:actions/checkout@v4

      - name: 'Set up Python'
        uses: 'actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065' # ratchet:actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: 'Install skills-ref'
        run: |
          python3 -m pip install skills-ref
          echo "$HOME/.local/bin" >> $GITHUB_PATH

      - name: 'Validate skills'
        run: |
          shopt -s nullglob
          for skill_dir in skills/*/; do
            echo "Validating skill: $skill_dir"
            agentskills validate "$skill_dir"
          done
```

## Continuous evals (on submit & weekly)

Documentation and APIs evolve, and so do LLM models and agent harnesses. A skill that works today might break tomorrow if an underlying API, model, or agent harness changes.

To set an initial quality bar and prevent degradation, we run continuous evaluations:

- **On-submit evaluations:** Authors must provide explicit evaluation prompt suites and scoring rubrics. Every new skill that we launch is first evaluated internally to ensure its accuracy and efficiency.
- **Weekly quality checks:** We run continuous, scheduled evaluation jobs against the full skill library to catch regressions early.

Skill authors must supply multiple evaluation test cases, each containing a prompt and a set of expectations. With each evaluation suite, we compare the performance of agents with and without each skill.

And look at two main dimensions:

1. Accuracy - response quality and task completion rate
2. Efficiency - number of consumed tokens and time for completion

Moreover we run our evals multiple times against different agent frameworks to obtain statistically significant results.

Finally the 2x2 matrix proves whether a skill delivers a measurable accuracy and efficiency uplift.

[![2x2 evaluation matrix comparing efficiency and performance for agents with and without skills](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2F1zftd8j1g0ozhbsbm5ri.jpg)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2F1zftd8j1g0ozhbsbm5ri.jpg)

## Skills are products, not snippets

A key lesson learned from our work is that a skill is a living product, not a one-off document.

To ensure long-term reliability, we established strict ownership rules:

- **Repo maintainers** oversee repository health, CI pipelines, and architectural standards.
- **Skill owners** are responsible for maintaining their skills long-term. For example, if a product API changes, the skill owner updates the skill. The same applies to quality degradation found during evaluation runs.

## Supporting authors: Tools and agentic workflows

Writing effective instructions and evaluation suites requires practice and we don't expect skill authors to craft everything from scratch.

To support our contributors, we built several tools and agentic workflows:

- **Internal skills** designed specifically to assist authors building new skills and writing robust evaluations.
- **Agentic tools** built with the [ADK](https://adk.dev/) that run multi-agent loops for authoring and self-critique, with an easy export path to the main repository.

I will dive deeper into these authoring tools and agentic workflows in future articles.

## Internal efficiency with "DevRel Skills"

While [Google Agent Skills](https://github.com/google/skills) hosts public skills for external developers, we also launched a parallel internal initiative called **DevRel Skills**.

DevRel Skills focus on building agent skills specifically for internal team workflows. By encoding internal processes — such as content transformation, SEO optimization, internal reporting, etc. - into dedicated skills, we help our team work more effectively and consistently every day.

## Wrap-up and over to you

Building quality agent skills at scale requires combining clear standards, rigorous evaluation, automated CI/CD, and long-term ownership.

As agentic development grows, we'd love to hear from you:

- **How are you building and testing agent skills in your workflow?**
- **What checks or evals do you use to verify agent responses?**

Let us know in the comments or reach out on socials!

## Links and further reading

To get started with Google Agent Skills, check out:

- **Google Agent Skills Repo:** [github.com/google/skills](https://github.com/google/skills)
- **Part 1:** [Introduction: What Are Google Cloud Agent Skills?](https://medium.com/google-cloud/google-cloud-skills-tutorial-the-complete-guide-to-ai-powered-cloud-operations-7838fcc9541a)
- **Part 2:** [Practical Guide: Intermediate Agent Skills in Action](https://medium.com/google-cloud/google-cloud-skills-tutorial-part-2-intermediate-skills-in-action-dd599a32fb6c)

## What's next?

If you found this post helpful:

- Add reactions to this post by pressing the heart ❤️ button.
- Share this post with your friends on socials.
- Connect with me via [LinkedIn](https://www.linkedin.com/in/remigiusz-samborski/), [X](https://x.com/RemikSamborski) or [Bluesky](https://bsky.app/profile/rsamborski.bsky.social).

Thanks for reading!