---
type: raw
source: "https://www.langchain.com/blog/how-similarweb-evaluates-long-form-agent-research-reports-with-langsmith"
title: "How Similarweb Evaluates Agent Reports with LangSmith"
author:
  - "Liora Korni"
published: 2026-07-29
created: 2026-07-30
description: "SimilarWeb 高级 AI 工程师 Liora Korni 发表于 LangChain 博客的一线评估工程实践：Data Studio（自然语言驱动的 agentic 数据分析层，agent 自主规划、调工具、检索、回写答案）的长文研究报告评估体系。两类检查器并行：确定性检查（必需工具是否调用、是否触碰禁用工具、结构化输出有效性，无模型参与）+ LLM-as-a-judge（评判 prompt 三输入：用户问题、agent 输出、评判标准；标准可为 golden answer 或带显式评分锚点的 rubric，返回分数 + 评语）。场景分流：常规 chat 有期望答案 → golden answer 语义比对 + 工具检查即可；Deep Research 长文报告（同一问题可有多份合格报告）→ 每质量维度独立 rubric（如 source_integration 的 0.0/0.3/0.8/1.0 锚点）+ faithfulness 检查（每条论断是否由检索数据支持，捕捉'自信但无根据'陈述）+ A/B 基线比较（与已接受的历史版本并排裁判，基线是参考点而非 ground truth）。核心教训——校准陷阱：两个标准（source breadth vs attribution quality）互相拉扯，聚合分数掩盖冲突，一次完全没问题的更新（引用更多来源但来源模糊）被误判为回归、反复回滚浪费近一周，直到打开逐标准评语才发现；修复方式是把 rubric 锚点从奖励数量改为奖励'命名、可验证的来源'，同一份报告分数从 0.7 落到 0.3，数字终于与评语一致。命题：'校准错误的评估比没有评估更糟，因为它递给你虚假的信心'（分数移动不是有用部分，评语与 trace 才是）。工作流六步：假设 → 小规模评估取信号 → 检查评语与 trace → 带重复的完整基准 → 基线/A-B 比较 → 合并/迭代/重校准。定位：评估不是发布检查清单项，而是工程工作流——score 告诉你往哪看，trace 告诉你发生了什么，feedback 告诉你评判者为什么这样打分；评估不取消人类判断，而是让判断可检查、可重复、与 agent 实际行为相连。"
tags:
  - clippings
  - agentic-engineering
  - evaluation
---

# How Similarweb Evaluates Agent Reports with LangSmith

*Liora Korni (Senior AI Engineer, SimilarWeb) · LangChain Blog · 2026-07-29*

---

*Author: Liora Korni, Senior AI engineer at SimilarWeb*

How many times have you shipped an agent prompt, model, or tool update, liked the first output you checked, and still felt uneasy? One output can look better while another loses source attribution, drops an important caveat, or starts relying too heavily on one data source.

This is an agent builder's problem. In traditional software, a change passes its tests or it does not, and the behavior is repeatable. An agentic system is different: the same input can take a different path, call different tools, and produce a different but still valid answer. Every update is a bet on whether the system got better or if you just moved the failure somewhere else.

That was the problem we faced while building Similarweb Data Studio. Similarweb measures the digital world, estimating how much traffic websites and apps receive, where that traffic comes from, how competitors perform, and where audience attention is shifting. Data Studio is the agentic layer on top of that data. Instead of navigating dashboards and filters, a user asks a question in plain language, and the agent plans the work, calls the right data tools, retrieves the numbers, and writes the answer back. It might handle a quick lookup (like "how much of spotify.com's traffic is direct?"), a competitor comparison, or a full multi-step research report. For each request, it decides how to get there instead of following a fixed script.

An agentic system does more than produce text. It chooses tools, retrieves data, and synthesizes evidence, so a regression can hide in any of those steps. That is why evaluation had to become part of the product architecture. We needed a workflow that could show which cases changed, which quality dimensions moved, what the evaluator said, and what happened in the trace.

LangSmith gave us that workflow in one place, and kept every result inspectable, from a score all the way down to the trace behind it.

**What you'll get from this post.** If you build agents, RAG pipelines, or any LLM feature whose output is open-ended, subjective, or long-form, and you have ever hesitated before shipping a change, this is written for you. By the end you will know:

- how to evaluate an agent when there is no single correct answer to compare against;
- how LLM-as-judge with rubric prompts works, and where it fits next to deterministic checks;
- how to wire datasets, feedback, traces, and A/B comparisons together in LangSmith so a score always leads back to the reasoning and behavior behind it;
- why a miscalibrated evaluation is worse than none, and how to avoid the calibration trap that cost us a week.

## Two Ways to Score an Output: Determinist Checks and LLM-as-a-Judge Scoring

We run two kinds of checks on agent outputs.

The first kind is **deterministic**. Did the agent call the tools it was required to? Did it avoid tools it should not have touched? Did it return valid structured output? These are mechanical pass/fail comparisons, with no model involved.

The second kind is an **LLM-as-a-judge**. Whenever the thing we care about is meaning or quality, deterministic rules fall short, so we hand the decision to a model. The judge prompt gives that model three things: 1.) the user question, 2.) the agent's output, and 3.) a standard to score against. It then returns a score and a comment explaining that score. The standard can be a golden answer ("does this say the same thing?") or a rubric with explicit scoring anchors ("how well does this meet each quality bar?").

We treat the judge as a scalable reviewer. It produces inspectable signals—a score, the reasoning behind it, and a link to the trace—so we can see what the agent actually did.

Both kinds of checks run in the same evaluation loop and land side by side as feedback in LangSmith. The harder question for us was, *what should the judge score against?*

## The Easy Case: Regular Chat

The simplest case to evaluate in an agentic system is regular chat.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a69092e91ce3285617d2afe_similarweb1.png)

**Caption**: Regular chat: a focused question with a more expected answer shape.

Each benchmark example has a fixed prompt, a golden answer, expected tool checks, and an agent output. We can compare the output to the golden answer, verify the agent called the required tools, and track scores over time.

```python
experiment_results = await aevaluate(
    target,
    data=dataset_id,
    evaluators=evaluators,
    experiment_prefix=experiment_prefix,
    num_repetitions=num_repetitions,
    max_concurrency=max_concurrency,
)
```

Both kinds of checks show up here. The tool checks are deterministic. Comparing the output to the golden answer, though, is a job for an LLM-as-judge, because a correct answer can be phrased many ways and exact text matching is too brittle. That judge is the `semantic` evaluator, anchored to the golden answer. Its only question is whether the output means the same thing.

Each evaluator returns one piece of feedback, a key, a score, and a comment. For the traffic-by-channel question above, the `semantic` judge returns something like this:

```json
{
    "key": "semantic",
    "score": 0.7,
    "comment": "Matches the reference on the top channels (direct and organic search) and gets the direct share right, but omits the referral traffic the golden answer calls out, so it is close but incomplete."
}
```

LangSmith turns that feedback into experiment columns. Instead of collecting scores in a spreadsheet, we can compare runs, click into a score, and inspect the trace behind it.

For regular chat, this is enough. There is an expected answer, so the deterministic checks and a semantic judge anchored to it cover most of what matters.

## The Hard Case: Deep Research

Deep Research outputs are long-form reports with sources, interpretation, recommendations, caveats, and narrative structure. There may be many good reports for the same question.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a6909fbc35bdb064f68d003_similarweb2.png)

**Caption**: Deep Research: an open-ended question where many good reports are possible.

One strong report might focus on traffic acquisition. Another might focus on competitive positioning. Another might focus on monetization risk. All can be valid if the claims are grounded and the reasoning is sound.

A golden answer doesn't work well for this case. There is no single reference to compare against, and matching a reference report would only reward similarity, not quality. So instead of a reference we give the judge a rubric: each quality dimension gets its own rubric with explicit scoring anchors, so the judge returns a score per dimension rather than one overall verdict. For example, the `source_integration` criterion asks whether the report uses external sources beyond raw platform data:

```markdown
source_integration:
Does the report effectively integrate external sources beyond raw platform data?
Evaluate both diversity AND quality of source integration.

Score 0.0: Relies purely on a single data API with no external context.
Score 0.3: Mentions external sources vaguely, e.g. "according to industry reports".
Score 0.8: Cites multiple named sources with dates, figures, and context.
Score 1.0: Uses extensive, attributed sources that are well-integrated into the narrative.

Return:
- source_integration: score from 0.0 to 1.0
- source_integration_gap: short summary of the gap
- source_integration_detail: one sentence explaining the score
```

Each criterion returns a score plus a short explanation, so a low number always comes with a reason we can inspect. A thinly-sourced report earns exactly that:

```json
{
    "source_integration": 0.3,
    "source_integration_gap": "External context gestured at, never attributed",
    "source_integration_detail": "Leans almost entirely on Similarweb traffic data and twice waves at 'industry reports' without naming a single source, date, or figure. The outside context is decorative, not evidential."
}
```

Alongside the quality rubrics, we run faithfulness checks to verify, *does each claim actually follow from the retrieved data, or did the agent overstate what the sources support?* This is where confident but ungrounded statements show up, which matters most when the output is long and persuasive.

Rubrics and faithfulness checks score a report on its own terms. To decide whether a new version is actually better, we also run A/B comparisons against a baseline: a saved, accepted previous run we treat as a reference point, not as ground truth. The judge sees the new report beside the baseline and says which is stronger, instead of scoring in isolation.

## LangSmith Connected Evaluator Scores to Traces and Baseline Comparisons

Writing an evaluator prompt is only part of the workflow. The harder part is running the loop repeatedly and deciding whether a change is real.

LangSmith made that possible because nothing was siloed. aevaluate ran the loop over a fixed dataset, with repetitions and concurrency; every evaluator score landed as a column, every score carried its comment, and every run linked straight to the trace and to a baseline for comparison. The differentiator was the connection between the number, the evaluator reasoning, and the agent behavior behind it.

Instead of asking only, "Did the average score move?", we could ask:

> Which cases moved, which criteria moved, what did the evaluator say, and what happened in the trace?

That is the difference between evaluation as a scoreboard and evaluation as an engineering workflow for building agentic systems.

## Miscalibrated Rubrics Can Make Good Updates Look Like Regressions

The first version of the Deep Research evaluation slowed us down instead of speeding us up as intended.

We made a small prompt change, re-ran the benchmark, and the overall score dropped. So we treated it as a regression: revert, tweak, re-run. Then again. The reports looked good to us every time, but the number kept disagreeing, and we trusted the number over our own reading.

We lost the better part of a week fighting our own evaluation before anyone opened the per-criterion comments. When we finally did, the answer was almost embarrassing…the new reports cited more sources, which lifted source breadth, but those sources were vague, which sank attribution. Two criteria were pulling against each other, and the aggregate score hid the conflict. The change had been fine the whole time. We had spent a week arguing with a miscalibrated ruler.

One issue was conflicting criteria, the exact one that cost us the week. From a product perspective, we learned that we did not want more sources for their own sake. We wanted named, relevant sources tied to specific claims.

You could watch the miscalibration in the comments. Before we fixed the rubric, a report stuffed with vague references still scored well just for reaching outside the platform:

```
{
    "source_integration": 0.7,
    "source_integration_detail": "Broad outside context, nine references, but most are unnamed ('industry reports', 'analysts expect'), so the attribution is thin."
}
```

The score rewarded breadth; the comment already knew the attribution was thin. Once we rewrote the anchor to prize named, verifiable sources over raw count, that same report settled at 0.3, and the number finally matched what the reasoning had been saying all along.

Another issue was wrong incentives. If conciseness was rewarded more clearly than completeness, reports became shorter even when the user asked for strategic research that needed caveats, methodology, and broader context.

In both cases, the moving score was not the useful part. The comments and traces behind each score were what let us see which criterion was miscalibrated and why. We could debug the rubric instead of guessing from the aggregate score.

A miscalibrated evaluation is worse than no evaluation, because it hands you false confidence. Before trusting an evaluation result, we had to ask whether the evaluator was measuring the behavior we actually cared about.

## The Workflow That Worked

Once the criteria were calibrated, the loop we settled into was:

1. Start with a hypothesis.
2. Run a small evaluation for a signal.
3. Inspect feedback comments and traces.
4. Run the full benchmark with repetitions.
5. Compare against a baseline or A/B output.
6. Decide whether to merge, iterate, or recalibrate.

## Final Takeaways: Golden Answers, Rubrics, Traces, and Baselines Serve Different Parts of Agent Evaluation

Golden answers are enough when there is an expected answer. Long-form agent outputs are not, so they need rubric prompts, faithfulness checks, and A/B judgment instead.

Evaluation and observability should live together. The score tells you where to look. The trace tells you what happened. The feedback tells you why the evaluator scored it that way.

That changed how we build agentic systems. We no longer treat evaluation as a release checklist item. We use it to shape product decisions such as *which behavior is worth optimizing, which regressions are real, which prompts are miscalibrated, and where does the agent need better tool use or better synthesis.*

Evaluation does not remove human judgment. It makes judgment inspectable, repeatable, and connected to the agent's actual behavior, so every update is based on evidence instead of one good-looking output.
