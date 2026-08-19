---
type: raw
title: "Designing AI Evals: Clarity Now and Visualization Next"
source: "https://dev.to/googleai/designing-ai-evals-clarity-now-and-visualization-next-4eii"
author:
  - "Google AI"
published: "2026-08-18"
created: "2026-08-19"
description: "Google AI 团队用 Inspect AI 评估 Gemini agent skill 的实操系列：decoupled grader 架构（cheap 模型做 strict-binary 评分）、multidimensional rubric（multi_scorer + quadratic curving）、matrix 视图与 sample-level 诊断、5 种 skill vs baseline 诊断结果分类。"
tags:
  - "clippings"
  - "evals"
  - "verification"
  - "inspect-ai"
  - "agent-skills"
---

# Designing AI Evals: Clarity Now and Visualization Next

> Source: https://dev.to/googleai/designing-ai-evals-clarity-now-and-visualization-next-4eii
> Author: Google AI (DevRel Demos)
> Published: 2026-08-18

## AI evals and analysis

Let's say you're testing out new AI tools. Perhaps you implement and run analytics for an Ad Agency and hope to automate deploying your standard event schema, or are a podcast producer automating generating social copy from your newest ep. While modern, newly trained LLMs can likely one-shot a lot of these tasks – this specificity might necessitate wasting tokens and time repeatedly prompting them with the same resources, descriptions and scripts. With this in mind, you investigate tooling whether that be an MCP server, an agent skill or an agent plugin.

The problem is, how do you know if a skill (whether developed by you or open sourced by someone else) is worth your time or, perhaps more importantly, your tokens and quota? How can one go about designing these (more) objective evaluations of AI tools and, from there, collecting and analyzing relevant metrics? That is exactly the context for using open source eval frameworks, like [Inspect AI](https://inspect.aisi.org.uk/) and [Harbor](https://github.com/harbor-framework/harbor) to [evaluate agent skills using open source frameworks](https://codelabs.developers.google.com/codelabs/evaluate-agent-skills-using-open-source-frameworks). But how do you ["extend the evaluation"](https://codelabs.developers.google.com/codelabs/evaluate-agent-skills-using-open-source-frameworks#4), use visualizations to spot trends and collaboratively explore alternative paths forward using Google Sheets and Data Studio?

These questions and more are exactly what I'm hoping to demonstrate for you in this series!

While you are more than welcome to simply read about how and why I conducted my own investigation, you can alternatively follow my lead and [run the benchmark scripts](https://github.com/GoogleCloudPlatform/devrel-demos/blob/main/agents/inspect-agent-skills-eval/README.md#reproduction-guide).

So, if you're hoping to play along, take a moment to [complete the aforementioned codelab](https://codelabs.developers.google.com/codelabs/evaluate-agent-skills-using-open-source-frameworks) and come back when you're done. Don't worry, we'll still be here when you get back!

**Note**: This blog series contains AI-generated diagrams alongside actual screenshots and hand-drawn edits of both. AI also assisted in minor copy editing.

## Level up your evals

In the codelab, we learned how to run evals with Gemini CLI, Inspect and Inspect SWE in an isolated Docker Sandbox to understand how well each skill aids the agent in answering the same question.

For those playing along at home, please additionally install `inspect view` now before you need it to run the evals below; be prepared to have to wait for a couple minutes for evals to finish depending on your machine and quota usage.

Regarding our new [source files](https://github.com/GoogleCloudPlatform/devrel-demos/tree/main/agents/inspect-agent-skills-eval#downloading-the-demo-giget) while they are heavily commented and hopefully written in a self describing way, I'll explain further subsequently.

### A note on models

For the purpose of my investigation demo, I used three different models: `google/gemini-3.5-flash-lite` and `google/gemini-3.6-flash` as "solvers" (the models under evaluation), and `google/gemini-3.1-flash-lite` as a "grader" (the model rating the runs). The three of them (and models more broadly) differ in many ways but more specifically on [problem solving ability, speed and cost](https://ai.google.dev/gemini-api/docs/models).

We intentionally offloaded grading for this demo to a previous-generation model because by changing rubric criteria to strict binary decisions and applying a reduction programmatically, it delivers sufficiently robust evaluations without burning through solver quota. For a *production* evaluation system, consider investigating using newer and more capable models as graders because they will likely have narrower confidence intervals.

For a full technical breakdown of this decoupled grader architecture and to find out how you could substitute in your own choice of models, see the README section on [Decoupled Grader & Multidimensional Rubrics](https://github.com/GoogleCloudPlatform/devrel-demos/blob/main/agents/inspect-agent-skills-eval/README.md#3-decoupled-grader--multidimensional-rubrics).

## Setting up the eval

**Reproducibility & Local Setup Note**: If you are following along locally, clone the domain skill definitions into `google-skills/` before running benchmark sweeps:

`git clone https://github.com/google/skills.git google-skills`

All evaluations in this series were benchmarked on **Python 3.13** using `inspect-ai` (`v0.3.247`), `inspect-swe` (`v0.2.66`), `inspect-viz` (`v0.4.1`), and `pandas` (`v3.0.3`). If upstream PyPI releases introduce breaking changes, check the README's [Environment & Dependencies specification](https://github.com/GoogleCloudPlatform/devrel-demos/blob/main/agents/inspect-agent-skills-eval/README.md#environment--dependencies) for exact version pins and instructions on how to reproduce the configuration.

For this investigation I used a [new eval script](https://github.com/GoogleCloudPlatform/devrel-demos/blob/main/agents/inspect-agent-skills-eval/skills-eval.py); while the specifics of the script are important for anyone who hopes to make make their own evals or run the code as we go, if you're primarily interested in analysis and visualization, feel free to skip to the [next section](#running-the-eval).

The original script ran a small batch of tests on a local machine. While this version can be and was run on a local machine, it prioritizes three architectural dimensions needed for running automated tests as part of a larger scale development flow:
- External Configs (providing the evals and solver system prompt as external files for separation of concerns).
- Quota Management (for the GenAI API and package management).
- Multidimensional Evaluations (expanding to arbitrary fact counts for graders).

For a complete technical breakdown of these architectural pillars—including external configuration schemas (`questions.json`, `thrifty_system_prompt.txt`), solver rate-limiting defenses (`version="0.51.0"` pinning), grader quota decoupling, and score curving math formulas see the README's [Evaluation Pipeline Architecture & Technical Reference](https://github.com/GoogleCloudPlatform/devrel-demos/blob/main/agents/inspect-agent-skills-eval/README.md#1-external-configurations).

## Running the eval

These commands create a matrix of evals subject to model x skill condition x sample x epoch. For a quick visual (that I'll repeatedly reference throughout this), take a look below.

**Caption**: Visualization of the eval matrix that will be scored and compared. In Inspect AI, rubric elements, represented here as Facts, are graded Correct (C) or Incorrect (I).

With all that said, it's finally time for the rubber to meet the road. I ran our evals with the following command

```
inspect eval skills-eval.py \
  --model google/gemini-3.5-flash-lite,google/gemini-3.6-flash \
  --time-limit 300 \
  --epochs 2 \
  --max-tasks 4 \
  -T web_access=false
```

This command runs a 4-way parallel sweep across models and skill conditions while enforcing a 300-second task timeout and disabling web search to minimize token spend. See the README for a complete [CLI Parameter Reference](https://github.com/GoogleCloudPlatform/devrel-demos/blob/main/agents/inspect-agent-skills-eval/README.md#cli-parameter-reference) and details on [External Configuration Template Mechanics](https://github.com/GoogleCloudPlatform/devrel-demos/blob/main/agents/inspect-agent-skills-eval/README.md#1-external-configurations).

### Run and wait

If you intend to and haven't done so already, **run the command line**. If you're interested in how to read over and interact with the Terminal User Interface, please refer to the [previous codelab](https://codelabs.developers.google.com/codelabs/evaluate-agent-skills-using-open-source-frameworks).

Watch the running command line long enough to determine it hasn't crashed or hit an obvious error and then maybe take a moment to make some food, grab some water or take a walk around the block. Enjoy the small things in life, okay? Worst case, you get a 20 minute walk out of it, not so bad eh!?

## Viewing the evals

With that said and done, reading the terminal output is only the most basic way of understanding the evals. Now that you have the raw eval logs, what do you need to do to begin to use these analytically and, more importantly, persuasively?

To start off, I simply ran

```
inspect view
```

and clicked the link to open the browser to the GUI.

For step-by-step diagnostic trace analysis in the browser GUI, see the README section on [Local Diagnostic Trace Analysis (inspect view)](https://github.com/GoogleCloudPlatform/devrel-demos/blob/main/agents/inspect-agent-skills-eval/README.md#local-diagnostic-trace-analysis-inspect-view).

### Macro view: Comparing runs

While LLM's are inherently stochastic (and given floating point hardware, nondeterministic), when running evals we are trying to use sampling to characterize the average observable metrics (e.g. correctness, latency and token usage) which our particular configuration model x skill scores on relevant questions. As such, the eval tasks were set up to characterize how a change to an independent variable (model or skill) affect dependent variables (the aforementioned metrics).

#### A. Comparing models head to head

Grouping evaluation runs by model in `inspect view` allows for a direct "eyeball" inspection of how skill inclusion alters accuracy across baseline controls—**given a specific model, what is the impact of adding a skill?**

The above shows that
- In all cases, the addition of a skill improved or tied scores relative to the same model's baseline.
- All of these cases **also** increased duration

Another simple measurement that can be done is to look at the `TOKENS` column where gemini-api actually led to a decrease in usage relative to its baseline in `3.6-flash`.

While the general relationship between tokens and score is difficult to parse visually, one notable result: for 3 out of 4 task x model configurations, gemini-3.6-flash used more tokens than the comparable 3.5-flash-lite run.

#### B. Comparing skill conditions (skill vs. baseline)

Now to analyze the inverse; in more concrete terms: **given a particular skill, what is the effect of changing the underlying model?**

What was the effect of the change from `3.5-flash-lite` to `3.6-flash`?

For 3 out of 4 of these, the changes between the two models amounted to an up to 45% increase in accuracy. For whatever reason, however, changing the `gcloud` skill from using one model to another led to a slight decrease.

While these are both valuable findings, they warrant further questions:
- Are these representative samples?
- If these findings are repeatable, how can we characterize the relationship between the existing metrics?

For the first of those, if you want to make more representative samples, know that you should conduct further research using more questions, samples and epochs and compare those metrics with these. For the sake of this blog series though, I'll leave that for you to do.

For the second though, we can and will endeavor to do so. That said, it might help in designing follow up analysis to think a little bit about common patterns encountered during evals. This is especially true for those running evals themselves (possibly on different skills or rubrics); you are likely to encounter very different metrics than mine, and thus I'll lay out some common patterns and follow up actions to investigate them further.

### Mental models for eval comparison (skill vs. baseline)

When analyzing evaluation runs, comparing skilled execution against baseline controls typically maps to five distinct diagnostic outcomes—ranging from **High-Efficiency Capability Lift** (best) to **Context Overload & Skill Regression** (worst).

For a complete breakdown of this diagnostic taxonomy and actionable audit steps for each outcome, see the README breakdown of [Diagnostic Mental Models for Eval Comparison](https://github.com/GoogleCloudPlatform/devrel-demos/blob/main/agents/inspect-agent-skills-eval/README.md#diagnostic-mental-models-for-eval-comparison-skill-vs-baseline).

### Micro view: Sample-level diagnostics

While high-level metric summaries alert you to outcomes like cost bloat or skill regression, opening an individual sample surfaces the **Sample Details** panel for granular trace analysis:

#### Transcript tab: How to read the LLM's conversation as it happened

This tab shows the exact multi-turn conversation between the solver agent, the sandbox shell, and external tools. Use it to diagnose model reasoning versus environment noise:
- **System Prompt Verification**: Confirm that web search rules (`-T web_access=false`) and automated time limits (`300 seconds`) were correctly injected into the container environment.
- **Skill Ingestion Check**: Verify whether the agent activated the skill. If activation didn't occur, your eval is *mostly* testing baseline model knowledge rather than skill utility.

**This means:** The agent actually ingested `gemini-api` instead of relying on baseline pre-training memory.

Of note though, some of the tasks where skills were made available did NOT activate the skill. If you're a skill author, you may want to rewrite the "activation criteria" (aka what situation calls for using the skill) such that it's more applicable to the specifics of relevant tasks.

##### Errors and reasoning loops

Auditing transcript details allows you to distinguish model reasoning loops (e.g., repeated redundant tool calls) from sandbox environment noise (e.g., container timeouts or missing binary dependencies). For step-by-step diagnostic trace auditing procedures, see the README reference on [Sandbox Noise vs. Model Reasoning](https://github.com/GoogleCloudPlatform/devrel-demos/blob/main/agents/inspect-agent-skills-eval/README.md#sandbox-noise-vs-model-reasoning).

#### Scoring tab: Multi-fact verification breakdown

Clicking the **Scoring Tab** displays the empirical breakdown of our custom `multi_scorer` on a sample:

The `multi_scorer` aggregates the results of checking the sample's answer against individual binary yes/no Facts using `model_graded_qa`. The generated list of scores in the range [0.0, 1.0] is supplied to our `custom_reducer` which calculates their arithmetic mean. From there, it applies quadratic score curving (mean²) to ensure that the further from correct the mean of the supplied answers are, the lower the score is pulled. This allows the most correct answers to stand out immediately. In the **Scoring Tab**, this downward curve maps a raw 5/6 fact score (≈0.8333) down to a normalized 0.65 sample score. For complete formulas and math derivations, see the README section on [Atomic Fact Verification & Quadratic Curving](https://github.com/GoogleCloudPlatform/devrel-demos/blob/main/agents/inspect-agent-skills-eval/README.md#3-decoupled-grader--multidimensional-rubrics).

## Visual milestone: The transition to cohort analytics

While `inspect view` provides outstanding deep-dive diagnostics for individual sample traces, evaluating dozens of models across multiple skill domains gets confusing fast (as you may have seen above). Weighing the correlations between skill inclusion vs exclusion and model changes against each other can be confounding and more art than science if we don't find better ways to reason over them; it requires a structured matrix overview.

Remember that mess of sectors of a 3d space I showed you earlier representing all the configs? Well, unless we find numeric ways to collapse that or quantify deeper comparison, you won't get the granular information you need to choose between two similarly capable alternatives. Worse yet, you won't be able to communicate this to the people with their hands at the purse strings (unless of course, that's you too).

To make this easier, next time we'll start down the road of understanding and displaying these things visually: As visualized in the cohort matrix linked above, understanding agent capability factor-by-factor requires cohort slicing across multi-dimensional metrics.

In **Part 2**, we scale our analysis from single log UI inspection to aggregate scoreboards with `inspect viz`!