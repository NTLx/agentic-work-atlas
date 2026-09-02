---
type: raw
title: "How to Design AI Evaluations You Can Actually Trust"
source: "https://dev.to/googleai/how-to-design-ai-evaluations-you-can-actually-trust-41c3"
author:
  - "Jan-Felix Schmakeit"
published: "2026-09-01"
created: "2026-09-02"
description: "Google Developer Relations 关于如何设计可信 AI evaluations 的五条实践规则。"
tags:
  - "clippings"
  - "evals"
  - "verification"
  - "agent-skills"
  - "rubric-design"
---

# How to Design AI Evaluations You Can Actually Trust

As part of my work at Google, we are publishing a suite of [Agent Skills for Google products and technologies on GitHub](https://github.com/google/skills). These [agent skills](https://agentskills.io/home) are designed to help AI agents interact with our technologies. But how do you test that these skills are useful and work as expected? My team in Developer Relations has been focused on this question, because having reliable signals on their performance is critical to help us improve them over time.

Just as you wouldn't deploy a production API without writing unit tests, you should apply the same standard to your AI agents. As Joe Spiro showed in the [*Designing AI Evals*](https://dev.to/googleai/designing-ai-evals-clarity-now-and-visualization-next-4eii) post series, scaling AI tools means moving beyond "vibe testing" in a terminal. Instead, you should set up a structured, automated evaluation pipeline to benchmark your integration. The evaluations (evals) are the *actions* you asked the agent to perform, which are graded using scorers (for example rubrics) that *assert* whether the agent succeeded. We'll focus on evaluations in this post and tackle tips for scoring rubrics in the next post.

However, AI evaluations cost real tokens. You need to make sure that you use these tokens as efficiently as possible. They need to provide real value that helps you build better tools. Writing good evaluations is critical. Poor evaluations provide false signals, waste your token budget, and create noise in your metrics.

Here are five rules we learned to design better evaluations you can trust. Follow them to ensure that every token you spend produces a useful metric.

## Know Your Evaluation Environment

Before writing evaluations, you need to understand the setup and limitations of your chosen framework. This includes systems like Harbor, Inspect AI, or integrations in development tools like in the [Agent Development Kit](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/evaluation/agent-evaluation). Does it use an ephemeral sandbox? What tools are available? How is the output captured?

- **Tailor your graders to the environment:** For example, if you can deterministically access the sandbox to evaluate code, that's an option. Alternatively, ask the agent to print its response to the console. Your framework can capture this output and pass it directly to your scorers. Adjust your grader to handle these environments.
- **Be aware of dependency limitations and access to "real" resources:** If an evaluation task requires access to "real" resources (for example an authenticated `gcloud` session with access to a Google Cloud project), create ephemeral resources or credentials that isolate and limit access so they don't impact other evaluations. Alternatively, you could provide mock tools instead of real test credentials.
- **Evaluate plans instead of tasks that are difficult to isolate:** An easier approach might be to evaluate the *plan* to accomplish the task, rather than the actual execution.
- **Avoid interactive prompts:** Multi-turn agent sessions are complex to evaluate. When getting started, design your evaluations using one-shot prompts.

## Avoid the Ceiling Effect

If your evaluations show a high baseline accuracy (i.e., without your agent tool), it might not prove its value, or the evaluation prompts are too easy.

- **Write harder prompts:** You cannot measure the impact of a new agent tool or skill if the baseline model already knows the answer.
- **Require multi-step reasoning:** Design prompts that reflect complex, real-world use cases where your tool can actually differentiate itself from the model's pre-training.
- **Revisit the scope of your tool:** If tests are repeatedly reporting a high accuracy without using your tool, it might be time to revisit it. The underlying model and agent may have improved and be able to accomplish the task without additional help. It might be time to refocus or deprecate your tool.

## The Prompt-Grader Mismatch

You cannot grade an agent on something you did not explicitly ask it to do. Your evaluation prompts and graders should be complementary. This means that they should only test for things included in the prompt.

- **Avoid scope creep:** If you asked a broad question, you can expect a similarly broad response. For example, if your prompt is *"How do I secure Google Cloud Run?"*, your grader cannot penalize the agent for missing a specific, unprompted IAM role.
- **Be explicit:** If you want to evaluate specific knowledge or exact implementation details, you must state those requirements clearly in the prompt.

## Grade the Destination, Not the Journey

Agents possess inherent model knowledge and might skip your custom tools entirely to arrive at the correct answer. (That on its own is some useful feedback!)

- **Do not evaluate the trajectory:** Avoid writing graders that check if the agent used a specific `help` command or followed a rigid sequence of steps.
- **Evaluate the final answer:** Grade the objective output. If you absolutely must evaluate the agent's planning phase, explicitly ask it to output a detailed execution plan and evaluate the plan instead.

## Curate Your Evaluation Dataset

A strong evaluation suite tests real, diverse use cases. But testing the same capability repeatedly causes overfitting and creates noisy metrics.

- **Use real-world examples:** Evaluations should include real user journeys and focus on goals users want to achieve. Consider including additional context, such as sanitized sample data, to ground the evaluations.
- **Maximize your signal:** Ensure every prompt in your evaluation suite tests a distinct concept or unique capability. Think of this like code coverage for traditional tests.
- **Remove overlap:** Consolidate redundant prompts. A smaller, more curated data set provides clearer metrics, prevents overfitting and saves tokens.

## Summary

You cannot improve AI tools if you can't measure them accurately. If you treat AI evaluations with the same focus as traditional unit tests, you improve the quality of your metrics and get more robust signals.

By applying these five rules, you eliminate false signals that waste your token budget. Instead of generating noise, your test suite gives you actionable feedback you can use to guide your engineering decisions and improve your tools.

Figuring out what to test is only the first step. A well-designed evaluation is only useful if the scorer grading answers is reliable and returns meaningful results. In my next post, we will look at how to test. You will learn how to write lean, atomic rubrics that minimize ambiguity for an LLM grader and make every token count.

*Photo by [William Warby](https://unsplash.com/@wwarby) on [Unsplash](https://unsplash.com/photos/gray-and-yellow-measures-WahfNoqbYnM)*
