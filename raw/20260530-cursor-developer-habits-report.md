---
type: raw
source: "https://cursor.com/cn/insights"
author:
  - "Cursor Team"
published: "2026-05-30"
created: "2026-05-30"
tags:
  - clippings
  - agentic-engineering
  - developer-productivity
  - coding-agents
  - data-report
---

# The Cursor Developer Habits Report — Spring 2026

## A field transformed

The change sweeping through software development is astounding. This inaugural Developer Habits Report, based on Cursor data, captures that transformation across five themes:

1. **Developer acceleration**. We chart how coding speed has doubled year-over-year, PRs are getting larger and deeper, and agent-generated code is surviving review at higher rates than ever.
2. **The economics of intelligence**. We benchmark seven model families on cost per line and cost per submit, revealing wide heterogeneity in unit economics.
3. **The power user gap**. We find that while AI is leading to broad productivity gains, the change is most pronounced in the top 1% of developers.
4. **The rise of context**. We show the dramatic increase in input tokens, and the shift toward cache-read tokens, which is giving agents the working memory to take on more complex tasks and produce higher-quality code.
5. **The shift to automation**. Finally, we look at how coding agents are evolving from a tool used by individual developers into an entire system for building and maintaining software, often automatically.

This report provides a data-driven fixed point for understanding where agentic software development stands today, and where it appears to be headed next.

## 1. Developer Acceleration

### Code is moving faster
Developers are adding more code per week, with growth accelerating since the start of 2026. While this is not a perfect metric, it provides a directionally interesting baseline for understanding how developer work is changing.

### Code additions are growing per PR
Lines added per PR are up roughly 2.5x year over year and the growth rate is accelerating.

### Developers are taking on larger units of work
Mega PRs, defined as PRs with at least 1,000 lines changed, are becoming more common as developers use AI to take on larger units of work in a single PR. It's interesting to see the jump in mega PRs in January 2026, when many developers were trying out the latest improvements in coding agents and models.

### Agent sessions are getting deeper
In just the last two months, average tool calls per session have risen roughly 30%. Coding agents are taking on more complex work, reading and editing files, searching code, running shell commands, and browsing the web more frequently.

### AI-generated code is surviving longer
Since the start of 2026, the share of accepted AI lines still present after 60 minutes has risen from roughly 76% to 81%.

## 2. The Economics of Intelligence

### Request costs differ widely by model family
Cost per agent request varies by nearly 9x across model families, showing that the same workflow can have very different cost profiles depending on the model behind it.

### Cost per accepted line narrows the model gap
Cost per accepted line varies by roughly 7x across model families, compared with nearly 9x for cost per request, suggesting that higher-cost models partially make up the difference by producing more accepted code per request.

### The cost-quality frontier is shifting
This benchmark view plots model performance on Cursor's internal eval suite, [CursorBench](https://cursor.com/blog/cursorbench), against average task cost, showing where models sit on the cost-quality frontier.

## 3. The Power User Gap

### Power users account for a large share of AI activity
AI usage is highly concentrated, with a small share of developers accounting for a large share of AI lines, spend, and token consumption.

The [Lorenz curves](https://en.wikipedia.org/wiki/Lorenz_curve) show this concentration, with [Gini scores](https://en.wikipedia.org/wiki/Gini_coefficient) of 0.77, 0.75, and 0.72 across the three metrics, where higher scores on a 0-to-1 scale mean activity is more concentrated among fewer users.

- AI Lines · Gini 0.77
- AI Spend · Gini 0.75
- Tokens · Gini 0.72

### The output gap is widening
We see p90 developers pulling farther away from median developers in absolute lines added per week, with p99 users even farther out in the tail.

### Inequality steepens at the tail
Here's another view of how dramatically the power-user gap widens at the tail.

P99 developers produce 46x more lines than the median active user and merge 15x more PRs than the median active PR author, while p90 users show large but much smaller gaps.

## 4. The Rise of Context

### Input tokens now dominate non-cache token volume
The same relative shift toward input tokens shows up in the token mix. Input now accounts for more than 90% of input-output token volume, making context the dominant part of non-cache model usage.

### Input context is becoming the main token cost
Input tokens dominate token consumption, but their effect on cost is moderated by their lower unit price.

Even so, input tokens have become the majority of price-equivalent token costs, rising since the start of the year from roughly half of input/output token costs to nearly 70%.

### Cache-reads dominate token activity
The context story becomes even larger once cache is included. Cache-read tokens dominate total token activity, showing how much agent work now depends on reusing prior context rather than reading everything from scratch. We [continually improve](https://cursor.com/blog/continually-improving-agent-harness) our agent harness to best cache tokens across models and providers.

## 5. The Shift to Automation

### Automation is spreading across workflows
It is still early, but the first autonomy patterns are coming into focus. Adoption of Cursor Automations is growing quickly, with security review emerging as a strong automation use case.

Even more recently, SDK runs show early demand for turning Cursor's agent infrastructure into a programmable platform customized to how each company builds software.

---

### Methodology Note

This report is based on aggregated Cursor product and engineering data, including agent usage, token consumption, accepted AI diffs, and merged PR activity.

Most time-series charts use trailing 7-day, 28-day, or 30-day averages to reduce short-term noise and make directional trends easier to see. Metrics are reported in aggregate and are intended to show broad patterns in how developers use AI to build software.

This report does not include data that users under Privacy Mode have chosen to opt-out from, including zero data retention with model providers.
