---
type: raw
title: "How Genie Ontology powers product development at Databricks"
source: "https://www.databricks.com/blog/how-genie-ontology-powers-product-development-databricks"
author:
  - "Nicole Esibov"
published: "2026-10-05"
created: "2026-10-21"
tags:
  - clippings
---

# How Genie Ontology powers product development at Databricks

Genie Ontology equips product managers with the enterprise context needed to seamlessly analyze adoption data, forecast emerging trends, and automate weekly workflows.

by Nicole Esibov

## Summary

- Genie Ontology understands your business through human-curated semantics and learned knowledge across your first- and third-party sources.
- The Databricks product team uses Genie One to analyze adoption data, forecast trends, prepare for executive reviews and more.
- Genie One also supports custom skills, scheduled tasks, shareable agents, MCP writes to external tools and more.

General-purpose AI agents are good at searching the web, reasoning, and writing code. But ask a question about your business, and you’ll likely get an incorrect answer. The problem isn’t the model's intelligence. It’s the missing enterprise context required to interpret your data correctly: which tables are authoritative, what business rules apply to your data, and who the trusted experts are.

That institutional knowledge is scattered across dashboards, queries, documents, applications, and even people—and it changes constantly as data, definitions, and teams evolve.

[Genie Ontology](https://docs.databricks.com) gives [Genie](https://www.databricks.com/product/ai-assistant) a continuously updated understanding of that institutional knowledge, including the business definitions, rules, relationships, and trusted sources that make your organization unique. It starts with the core concepts that your teams govern and certify in Unity Catalog.

It then scales that to the entire organization by supplementing this curated context with learned knowledge from your organization’s dashboards, documents, queries, notebooks, and connected applications. OntoRank then ranks that context by authority, using signals such as certification, usage, and authorship, so Genie can ground its answers in the most trusted and relevant sources for each question.

This post shows Genie Ontology in action for a real use case: our product team's weekly review of Genie One user adoption. Read on to learn how Genie’s PMs use Genie in our day-to-day work.

## Run my weekly adoption review with a simple prompt

I start my week by opening Genie One either [on my phone](https://docs.databricks.com), in the [desktop app](https://docs.databricks.com), or [on the web](https://www.databricks.com/product/ai-assistant). To help me prioritize my week, I’ll ask Genie to create my weekly adoption review using our team's standardized template, which lives in a Google Doc. The goal is to find any hotspots that might need attention.

*[Image: Prompt Genie One with an existing template]*

This task sounds simple, but it's not. Our users work across web, desktop, mobile, Slack, and Teams. Some dashboards are authoritative, while others are stale and should be ignored. And the relevant business context extends beyond the Lakehouse: plans live in Google Docs, bug reports in Jira, and field feedback in Slack. Genie needs to understand the correct business definitions, identify the most trusted sources, query the appropriate data, and retrieve relevant context across these systems.

And it does that through Genie Ontology.

## Genie finds the right data

I can see Genie Ontology at work as Genie thinks.

*[Image: Genie One searches for relevant data]*

It starts with relevant data assets (dashboards, agents, tables), then looks at curated Pages, and finally explores a few potentially relevant ontology snippets that it’s pulled from our dashboards, notebooks, SQL queries and so on. For example, I can see that we found our certified weekly active users metric view, a governed KPI that the whole company defines consistently.

Then it uses MCP to search our live Google Drive documents and Jira tickets. Finally, it runs SQL against our usage tables, combining context from those sources with fresh analysis of our data. That combination is what makes Genie powerful: Genie brings together search and live analysis to answer questions that neither could resolve on its own.

With that, I have a document ready for review:

*[Image: Reviewing a document in Genie One]*

And it creates that document very quickly. After all, a general-purpose AI agent has to compensate for not understanding your business. To find the context it needs, it may crawl schemas, sample tables, read documents, and run repeated queries to determine which definitions, data, and sources are relevant. That agentic exploration consumes time and tokens, and it can still lead to the wrong source or interpretation. Genie Ontology changes that by giving Genie business context before and during reasoning.

Genie can identify which sources are authoritative, understand how your company uses its data, and retrieve the most relevant context for the question, rather than starting from scratch. And because that context is permission-aware, Genie only uses data and knowledge the user is authorized to access through Unity Catalog and connected sources.

## Review Genie’s citations

I want to make sure I understand the source data, so I click into the citations to see everything Genie used. I see that it did use several of the metric views (certified KPIs with one governed definition the whole company shares) and pages (governed wikis in Unity Catalog) that it looked at in the thinking trace. This isn’t surprising; Genie favors human-certified assets before it explores on its own.

*[Image: Reviewing Genie Ontology snippets]*

But it's impossible to curate every concept by hand. That's why we also have [ontology snippets](https://docs.databricks.com): facts about our business that Genie has automatically learned and evaluated. I can click into any snippet to see its full definition, where it came from, who authored it, and its authority score (powered by OntoRank). I can even check the author's profile to see which domains they work across and what other snippets Genie has learned from them.

*[Image: Expanding a Genie Ontology snippet]*

## Ask a follow-up question and forecast the trend

While reading through the document, I have a follow-up question: why did new users spike so much in the past few months? Normally, I would query the usage tables to break the spike down by surface and account, then dig through roadmap docs, Jira tickets and Slack threads to investigate possible causes. Instead, I just ask Genie about the spike.

*[Image: Asking Genie One a follow-up question]*

I also want to know where this trend is headed. Normally, this means filing a request with our data science team, aligning on assumptions and waiting days for a model. However, forecasting is built right into Genie One, so I simply asked Genie to forecast and flag the accounts to watch.

*[Image: Forecasting with Genie One]*

## Schedule the workflow

I don't want to have to remember to run this every week. So, I put this adoption review on a schedule.

*[Image: Scheduling a report]*

## Turn the conversation into a shareable agent

These reviews aren’t the only time I need to answer questions about Genie performance; coworkers ask me for data points all the time.

Luckily, this conversation serves as a great starting point for a Genie Agent. In seconds, I have an expert coworker that my team and our leadership can use to ask follow-up questions and take action on Genie's performance—building on the data sources that we used in this conversation, as well as prior conversations about this topic.

*[Image: Creating and sharing a Genie Agent]*

## Get started today

In just a few steps, I was able to prepare an executive-ready review, investigate and forecast emerging trends, kick off a follow-up ticket, and build an agent that my team and I can continue to use. This was only possible because Genie understands our business through Genie Ontology, computes results rather than just reciting docs, and enforces our organization's governance along the way.

We'd encourage you to try this on your own data and share your feedback as we continue to shape this roadmap together.

Watch the full session on-demand: [Closing the AI Context Gap](https://www.databricks.com).
