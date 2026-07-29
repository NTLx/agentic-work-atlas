---
source: "https://www.langchain.com/blog/agent-data-stack"
title: "How LangChain Built an Agent-First Data Stack"
author:
  - "Emily Hawkins"
published: 2026-07-27
created: 2026-07-29
description: "LangChain 数据团队一手实践：从传统 BI 工具迁移到 agent-first 数据栈（Hex + dbt + 语义模型 + endorsements + workspace guides + GitHub 实现上下文）。data agent 承接 3 人数据团队约 40 倍请求量；数据团队角色从'回答每个问题'转为'改进系统'（建模型/context/护栏/反馈回路）。立场声明：框架厂商自述自家内部实践（文中推广 LangSmith/Hex），40x 等数字无第三方验证。"
tags:
  - clippings
  - enterprise-ai
  - context-engineering
  - organization
---

# How we built LangChain's agent-first data stack

*Emily Hawkins (LangChain) · 2026-07-27 · 14 min*

## Key Takeaways

* **Reliable data agents need more than access to tables.** They need clear models, metric definitions, business context, and signals about which sources to trust.
* **An agent-first stack can dramatically expand self-service.** Our data agent now handles roughly 40x the request volume our three-person data team could manage directly.
* **The data team's role has shifted from answering every question to improving the system.** The data team now focuses on building the models, context, guardrails, and feedback loops that help make agent answers more useful over time.

Over the past year, our data team has been rethinking how our stack needs to evolve to support agents. Most company data stacks are built around dashboards, reports, and SQL workflows. Those are still useful, but agents change what the data layer needs to provide.

An agent can answer more questions when it has clear definitions, trusted sources, business context, and access to the logic behind the data. Without that context, it can still generate SQL, but the answers are harder to trust. The agent might miss company-specific definitions, use the wrong table, or answer a question in a way that is technically valid, but not actually useful for the business.

We wanted to make data easier to access across the company, while giving agents enough context to answer questions accurately and explain how they got there.

We did a big architectural shift, moving from a data stack centered around a traditional BI tool to one designed for self-serve analysis, shared context, and agent use.

## Key results

* Our self-serve data agent now handles ~40x the volume of requests our 3-person data team could field directly.
* In the last 30 days, nearly 100% of provisioned users (a third of our company) used the data agent. We saw roughly 2,200 agent conversations in the period, or an average of 23 conversations per month per user.

## Where we started

Before this migration, almost every data ask went through the data team. At the time, that team was just one person.

The existing traditional BI tool worked for predefined reporting, but it was rigid. Exploratory analysis was hard to collaborate on, hard to share, and hard for anyone outside the data team to explore on their own unless the data had already been modeled and exposed in the BI layer.

This all created a bottleneck. People across the company had good questions, but answering them usually required a data team member to translate the question, find the right model, write or adjust the query, validate the result, and send back an answer. The data team spent a lot of time handling one-off requests instead of focusing on deeper analysis, modeling, and cross-functional projects.

We needed an agent-first stack that could support several different kinds of users at once.

Some people wanted polished dashboards. Some wanted notebooks and SQL. Some wanted a conversational interface that could help them answer a question without needing to know where the data lived. Engineers and technical operators needed flexibility, while many business users needed a safer and more guided way to explore.

We also wanted one central place for data work. We considered keeping our old BI tool and also adding a new one, but that would have split usage, context, and trust across two systems.

## How we evaluated our tooling

We were looking for more than a dashboard replacement.

When we evaluated different vendors, we wanted one that was building AI features directly into the product and treating the agent experience as part of the core workflow. We also wanted a notebook layout that would make it easy for more technical users and engineers to build what they needed without waiting on the data team for every iteration.

For non-technical users, we needed a place where someone could ask a business question, get a reasonable first answer, and understand which sources the agent used.

We ended up choosing [Hex](https://hex.tech/). It worked for dashboards, notebooks, and conversational analysis, which made it easier to choose a single central data workspace.

People now interact with the Hex agent through several surfaces:

* The Hex UI, including Threads and notebooks
* Slack
* CLI workflows
* MCP
* LangSmith Fleet, through MCP and CLI integrations

Having a wide surface area is important for adoption. Agent access is most useful when people can use it where they already work. A product manager may want to ask about user behavior in Hex. A GTM teammate may want to ask a pipeline question from Slack. A technical user may want to interact through the CLI or MCP.

We have already seen a wide range of use cases across teams:

* Marketing uses the agent for weekly pipeline analysis
* Product uses it to understand user behavior and usage trends
* Sales and deployment engineering use it for customer health and usage questions
* Customer engineering uses it to analyze churn, expansion, and account trends

These are the kinds of questions that used to create a queue for the data team. Now the first pass can often happen directly in the tool, with the data team available for validation, deeper analysis, or decisions that need more rigor.

## What changed after we migrated

We migrated 100% off our old BI tool in six weeks.

Today, 100% of the company uses our agent-first data stack, via Hex, in some form.

Roughly 70% of users have read-only access, and about 30% have agent access. Those roles are self-serve through IT, so anyone can request agent access when they need it.

A lot of those conversations represent questions that previously would have gone through the data team. However, the data team has not disappeared from the workflow entirely. The questions that reach us are more complex and higher leverage. We spend more time on the work that needs deeper business context, stronger data modeling, or cross-functional alignment.

This was our goal. We wanted self-service to handle more of the straightforward analysis, while making it easier for the data team to focus on the work that makes business impact.

## How we think about context

The agent experience depends on context.

The more clearly we can describe our business, data, metrics, and internal processes, the better the agent can answer questions about the company. Providing context is what helps agents generate useful analysis from raw table access.

For us, context comes from several places. Each layer gives the agent a different kind of information.

### How we define the data models

[dbt](https://www.getdbt.com/) is one of the main places where we manage context about our data models. That context exists in both SQL and written definitions.

Every table and column should help a person understand what the data represents, how it should be used, and where the edge cases are. Those same definitions also help the agent.

A weak column definition might say:

> `account_status:` The status of the account.

That is technically accurate, but it does not tell the reader much.

A stronger definition would say:

> `account_status`: The current lifecycle status of the account in Salesforce. `Active` means the customer has an active paid contract. `Churned` means the customer previously had a paid contract that has ended. `Prospect` means the account has not yet become a customer. For customer reporting, filter to `Active` unless the analysis explicitly includes churned or prospective accounts.

This definition gives the agent business context, allowed values, interpretation guidance, and a default filtering rule. It also reduces the chance that someone gets a technically correct answer based on the wrong business interpretation.

We apply the same approach at the table level. A good table definition should explain what grain the table represents, what kinds of questions it is designed to answer, and where people should be careful.

### The semantic model defines metrics and relationships

The semantic model gives the agent context about metrics and how models relate to each other.

This is where we define concepts like ARR, pipeline, active usage, customer health, and other metrics that people ask about repeatedly. The semantic layer helps keep those definitions consistent, so the agent does not need to infer metric logic from scratch every time someone asks a question.

A semantic model is most useful when it sits on top of solid data modeling. If the underlying models are unclear, duplicative, or poorly documented, the semantic layer can only do so much. We found that the foundations still matter. Clean models, clear grains, and good definitions lead to higher quality at every downstream layer.

### Capturing business context

Some context might not belong neatly in a table or metric definition.

There are company processes, team-specific workflows, reporting conventions, and business rules that need more room. These would be like skills for the data agent. We use Hex workspace guides for this. They give the agent written instructions about parts of the business, specific metrics, common workflows, and how people should interpret certain data. We manage these guides in a GitHub repo that syncs directly into Hex. That lets us version them, review changes, and keep the context close to the rest of our data documentation.

A guide might explain:

* How we define pipeline for weekly GTM reporting
* Which dashboards are considered canonical for a given metric
* How to interpret product usage across different deployment types
* What filters to apply when analyzing customer health
* When a question should be routed to the data team for validation

This layer has been especially useful because it lets us write business context in plain language, without forcing every detail into a model or column description.

### Endorsements tell the agent what to trust

Endorsements help the agent understand which data sources and assets are trusted.

For example, if the ARR dashboard is endorsed, the agent can use that dashboard and the logic behind it when answering a question about ARR. Endorsement is an important signal because companies often have multiple tables, dashboards, or historical queries that touch the same concept. Without a trust signal, the agent may choose an asset that looks relevant but is not the best source.

We keep guardrails around endorsements so they stay meaningful. Only the data team can mark something as endorsed. Endorsed dashboards also require data team review before changes go live. Our review process keeps endorsed assets trustworthy. If everything is endorsed, the signal stops being useful.

### GitHub provides deeper implementation context

The agent can also look at our dbt repo for deeper context about how a data point is sourced.

The dbt repo gives it access to the SQL and logic that define a column or metric from start to finish. This is useful when a question requires more than a surface-level definition. The agent can inspect the underlying model logic, understand joins and transformations, and trace how a field is produced.

For more technical users, this is one of the most important parts of the setup. The agent can move between business-level context and implementation-level context, which makes it more useful for debugging, validation, and deeper analysis.

## How we improve the system

Context needs a feedback loop. We wanted a way to see how people are using the agent and where the agent needs more help. Observability tools help with this. We leverage Context Studio from Hex, but teams can use LangSmith if their data agent is built in-house. We can look at trends in conversation topics, common warnings, issues, and context gaps. This data helps us decide where to improve the stack.

If people keep asking similar questions, we may need a better dashboard. If the agent repeatedly struggles with a metric, we may need a clearer semantic model definition. If users ask questions that require internal business context, we may need a workspace guide. If the agent uses the wrong source, we may need to adjust endorsements or improve dbt documentation.

This loop has changed how we think about data enablement, and we've learned that agent conversations are a great signal about what the company is trying to understand. When we see patterns in conversations, we can identify gaps in reporting, documentation, and modeling. We can also see where a dashboard would serve people better than repeated one-off questions.

The feedback loop:

1. Users ask questions through Hex, Slack, CLI, MCP, or LangSmith Fleet
2. Agent uses dbt definitions, semantic model, workspace guides, endorsements, dashboards, and GitHub context
3. Observability surfaces gaps, warnings, and repeated topics
4. Data team reviews patterns and suggestions
5. Data team updates models, definitions, guides, metrics, endorsements, or dashboards
6. Agent responses improve over time

## Where we're going next

We are still early in this workflow, and the tooling is changing quickly. Over the next few months, we are focused on a few improvements.

### Evaluating context changes

Next, we want to start leveraging evals, which will help us understand whether context changes are improving agent responses.

Today, we can look at usage patterns, warnings, and qualitative feedback. Evals will give us a more structured way to test changes. If we update a metric definition, add a guide, or change an endorsement, we want to know whether the agent produces better answers as a result.

This will make context management feel more like software development. We can make a change, test it, and build more confidence before rolling it out broadly.

### Improving our context workflow

We also want to automate more of the process around context suggestions.

Observability already helps us find gaps. The next step is making it easier to turn those gaps into reviewed changes across dbt definitions, workspace guides, semantic model updates, and endorsements.

We are exploring ways to make context improvements easier to track, review, and ship.

### Continuing to learn

Agent workflows are evolving quickly, and we are still learning what works, what needs guardrails, and where the product should improve.

Small improvements in context retrieval, trust signals, evaluation, and user experience can make a big difference in whether people use the agent confidently.

## What we've learned

A few lessons have stood out in our journey thus far.

### Solid data modeling foundations make everything easier

Agent access does not remove the need for good data modeling. It raises the value of good data modeling.

Clear grains, well-named models, consistent definitions, and reliable transformations make the agent more useful. If the data model is confusing to humans, it will be confusing to agents too.

### Good context is one of the highest leverage investments

The agent performs better when it understands the business. That means writing clear definitions, explaining company vocabulary, documenting metric logic, and giving guidance on how data should be interpreted.

The best context is specific. It explains how the business works, what values mean in practice, which filters are expected, and where the data should or should not be used.

### The semantic model works best on top of strong foundations

A well-defined semantic model is important, especially for common metrics. But it depends on the quality of the underlying models and documentation.

If you are starting this work, fix the foundations first. Then use the semantic layer to make the most important metrics consistent and easier for the agent to use.

### Start with the questions that matter most

You do not need perfect context everywhere on day one.

Start with the questions people ask most often. Identify the models they hit most often. Go deep on those areas first.

If you can cover roughly 80% of the questions people ask, you'll create a much better experience for most users. Then you can work through the long tail over time.

### Self-service still needs data education

Self-service works best when users understand both the power and the limits of the system.

We are clear that agent responses should be treated with judgment, especially when the answer will inform an important decision. Data team members should always be looped in when questions need validation. We also share periodic reminders and best practices in Slack as we learn more about how to best interact with the agent and our tooling.

Our goal is not to make every person a data expert, but we want to give people better access to data while preserving trust.

## Closing

Building an agent-first data stack is mostly about making context explicit.

The agent needs to know what the data means, which sources to trust, how the business works, and when a question requires extra care. The better we describe those things across our stack, the better the agent becomes.

For us, that has meant investing in dbt definitions, semantic models, workspace guides, endorsements, GitHub-based context, and a feedback loop through observability of behavior. The reliability of a data agent comes from the context we put around the data.

Our work is ongoing. As evals, CLI workflows, and context management tools improve, we expect this process to become more systematic. However, it's already clear that data teams will spend less time answering every question manually and more time designing the context, models, and trust systems that help the rest of the company answer questions well.
