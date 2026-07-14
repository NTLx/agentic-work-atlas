---
type: raw
source: "https://blog.bytebytego.com/p/how-microsoft-ships-ai-agents-at"
author:
  - "ByteByteGo"
  - "Marco Casalaina (interviewee, VP of Products, Microsoft Core AI)"
published: "2026-07-13"
created: "2026-07-14"
tags:
  - clippings
  - agent-harness
  - agentic-engineering
  - microsoft
  - production-agents
  - evaluation
  - context-layer
---

# How Microsoft Ships AI Agents at Enterprise Scale

Microsoft operates at an enormous scale. More than 80,000 enterprises now build on Microsoft Foundry, the company's platform for building, deploying, and running AI agents and applications. Microsoft's own copilots run on the same platform, including Microsoft 365 Copilot, which alone serves over 20 million users and has a monthly active usage of first-party agents growing 6x year-to-date.

To understand what it actually takes to ship agents at that scale, we spoke with Marco Casalaina, VP of Products for Microsoft Core AI. He walked us through what his team has learned from running these systems in production, the engineering challenges that come with it, and where he thinks enterprise AI is headed next.

## What Breaks When Agents Hit Production

Production agents fail for reasons that aren't visible in a prototype. The model is rarely the problem. What breaks is everything around the model, including the data the agent retrieves, the tools it calls, the way it handles real users, and the way quality drifts as the world around it changes. Enterprises trying to ship agents this year are running into a different engineering problem than the one they were solving last year.

A production agent is more than a model. Most of the system is the machinery built around it.

> We are leaving the question-answering phase of AI. In 2026, we are seeing a huge increase in the number of our customers that are using voice as a front-end, so we're also leaving the chatbot era of AI.

The old shape was a chatbot. The user types, the agent types back, and it can only answer questions. The new shape is an agent that does meaningful work on the user's behalf. It books the meeting, runs the analysis, sends the email, files the ticket. The user might not type at all because the front end can be voice. For example, Foundry's Voice Live lets a team turn an existing text agent into a voice agent without rebuilding it.

This shift is what makes the engineering problem different. A chatbot returning a wrong answer is a bad experience. An agent taking the wrong action is a business incident. The bar for what's good enough to ship has moved.

That's where the gap between a prototype and a production agent opens up. The first prototype is easy. You can vibe-code one in an afternoon. The model is smart, your test prompts work, the demo is impressive, and the pilot ships in a week.

Production is where the cracks open. Real users ask things you didn't anticipate. Documents the agent depends on go stale. New edge cases emerge that never appeared in your eval dataset. A model update changes the agent's behavior subtly, and nobody notices until a customer complains. Without identity controls, the agent runs as a shared system principal and there's no audit trail when something goes wrong. Without guardrails, it confidently says something it shouldn't. Without observability, you can't tell whether quality is improving or degrading. None of these problems showed up in the prototype. All of them show up in production.

When we asked Marco for the single biggest lesson the Foundry team has learned from running these systems at scale, his answer was "the harness matters as much as the model."

The harness is everything around the model. The runtime, the tools, the context retrieval, the identity layer, the guardrails, the evaluators, the deployment pipeline. Models change constantly, and you cannot treat them like database versions. With Postgres, you change versions and you pretty much expect it to straight up work. Models are not like that. Each one has different properties that the harness has to adjust to. When Anthropic released Claude Opus 4.8, Microsoft's GitHub Copilot CLI team had to re-tune their harness and re-run their evaluations before they could ship it.

## What's in a Production Agent Harness

If the harness matters as much as the model, the next question is what's in it. Walking the harness from the bottom up shows why each layer exists and what breaks if you try to do without it.

### 1. Inference Layer

At the bottom is the inference layer, the single interface the harness uses to reach the models. The models themselves sit outside the harness and stay swappable. Different agents need different models, and the right one changes every few weeks. Foundry supports more than 11,000 of them, from OpenAI, Anthropic, xAI, DeepSeek, and Microsoft's own MAI family.

### 2. Agent Runtime

Above the model is the agent runtime, which is what turns a model into an agent. The runtime handles the orchestration loop, the tool calls, the conversation state, and the protocol the rest of the harness speaks.

Not every step in that loop should run through the model. A well-built agent sends only the parts that need reasoning to the LLM and leaves the rest to ordinary code, since a database lookup or a purpose-built extraction model is faster, cheaper, and more reliable than asking a model to do the same work.

The number of agent frameworks keeps growing, from open-source options like LangChain, LangGraph, and CrewAI to vendor-built runtimes. The principle that matters is framework neutrality. An agent built on one framework should be portable to another without rewriting the surrounding harness. Foundry, for example, lets agents run on any framework interchangeably.

### 3. Observability and Governance Layer

Once agents are in production, an organization needs observability and governance. It needs a single view of every agent running across every project, with health scoring, token usage, latency metrics, drift detection, and the kind of cross-project rollups that let a platform team govern a fleet. Without this layer, regressions are invisible and cost is uncontrolled. In Microsoft's case, this is Foundry Control Plane, which provides cross-project fleet visibility and routes agent telemetry into Azure Monitor and Application Insights, the same pipeline that already handles infrastructure alerts.

### 4. Identity Layer

Once agents start taking real actions inside an organization, they need their own identities. They need their own role assignments and their own audit trails, because a misbehaving agent has to be bounded by the same access controls that bound a misbehaving employee. The industry is still converging on how to do this well, and the answer most platforms are landing on is to extend an existing enterprise identity system to treat agents as a new class of principal rather than inventing a parallel system. For example, Foundry extends Entra, Microsoft's enterprise identity platform, to treat agents this way. This is the access-control primitive; later in the article, the section on giving agents a place to act shows what an agent does once it has one of these identities.

### 5. Context Layer

Once an agent can run reliably and act with its own identity, the question becomes whether it can answer correctly. That's the job of the context layer. While every other layer in the harness exists to let the agent run, context is what lets it run correctly. An agent without good context might hallucinate. It will give an answer, but the answer will be wrong in ways that are hard to detect because the agent itself doesn't know what it doesn't know. Marco was explicit that giving agents the context they need to actually work is one of the hardest problems his team is solving, and the one Microsoft is reasonably passionate about getting right.

## Building a Context Layer for Agents

The hard part of giving agents the right context isn't that the context is missing. Enterprises have enormous amounts of it. The hard part is that the context lives everywhere. It lives in unstructured documents in SharePoint and wikis. It lives in structured tables in OneLake and data warehouses. It lives in productivity apps like Outlook, Teams, and Word. No single retrieval method can reach all of it.

The standard answer of the last two years, classic retrieval-augmented generation (RAG), was never designed to. Classic RAG is a one-shot pattern. You take the user's question, embed it, search a single index, return the top-k results, and pass them to the model. It works for simple questions against a small, clean corpus. It breaks the moment the question is ambiguous, the corpus is heterogeneous, the right answer requires combining sources, or the first retrieval comes back empty. The agent has no way to recover from a bad retrieval, and as Marco put it, when RAG isn't working well, the whole agent isn't working well. One-shot is the wrong shape for the problem.

The fix is to treat retrieval as something the system can iterate on, the same way an agent iterates on a task.

Plan the query, try a source, evaluate the result, try a different source if the first one came back empty, and combine what you find. That's the central engineering idea behind a production context layer.

Microsoft's answer is to ship the context layer itself as a set of services. There are four of them, collectively called Microsoft IQ. Foundry IQ handles unstructured data, Fabric IQ handles structured data, Web IQ handles real-time web retrieval, and Work IQ handles the productivity surface of Microsoft 365, including email, calendar, documents, and Teams.

Each IQ is a headless service that agents call through MCP. Two engineering ideas run through them. The first, retrieval-as-a-subagent, is the pattern behind all four. The second, giving an agent an identity and a place to act, is specifically what Work IQ adds on top of retrieval so that an agent can do work, not just find information.

### Retrieval-as-a-Subagent

The technical idea behind a production context layer is to wrap retrieval in an agentic loop. Instead of a single function call that runs one query against one index and returns the top-k, retrieval becomes a small agent of its own. It plans which sources to query, executes the queries, evaluates the results against the original question, and decides whether to return them, refine the query, or try a different source. Retrieval stops being a lookup and becomes an iterative process that can recover from a bad first pass.

Foundry IQ is the cleanest example of this in production today.

The last step is the one most worth paying attention to. When iteration runs out, Foundry IQ returns a structured "I don't know" instead of forcing an answer. Classic RAG has no fallback and the model hallucinates something plausible. Foundry IQ gives the calling agent a clear signal that retrieval failed, which it can act on, rather than a confident wrong answer that's hard to detect.

So far this is all about data. The same loop applies to tools. An agent with a few tools can list them all in its prompt. One with dozens can't. Listing them all burns context on every call and slows the model down as it scans the list. The fix is similar to agentic retrieval. Instead of exposing every tool, the agent searches for the right one, gets it back, and calls it. Foundry exposes this as tool search, and it's the pattern OpenAI's and Anthropic's agents have converged on too. So the same retrieval loop that pulls in knowledge also pulls in capability. The agent looks up what it needs at the moment it needs it instead of carrying everything up front.

Other IQs rely on the same pattern too. Fabric IQ runs agentic retrieval over structured data, with the loop planning queries against OneLake tables and the Fabric data agent rather than against text indexes. Web IQ runs the same loop over the open web at sub-second latency. The retrieval-as-subagent idea is the architectural commonality across all of them.

### An Identity and a Place to Act

Retrieval gets the agent the right information. But information alone doesn't finish a task. An agent that knows the customer is unhappy still has to write the apology email and refund the order. To do that responsibly, the agent needs two things. An identity the organization can see, and a surface where it can take action.

The identity is the access-control primitive from the identity layer earlier. Without it, every action is anonymous or on behalf of a user who lent the agent their identity. Logs show that "the AI did it" and the audit trail collapses, which is unworkable for any regulated enterprise. The fix is to treat agents as their own class of principal, sitting in the same directory as employees, with their own role assignments and their own audit trails. A misbehaving agent gets bounded by the same access controls that bound a misbehaving employee.

The action surface is what makes the identity meaningful. An agent that exists in the directory but has no way to send an email or update a document isn't doing work. The surface has to expose the same actions a person already takes inside the organization, so that an agent operating on top of it can read inboxes, send messages, schedule meetings, and edit shared documents. In Microsoft's case, identity is handled through Entra and the action surface is Work IQ. An agent can now have a named directory entry, report to a manager in the org chart, and own its mailbox.

Identity bounds what an agent is allowed to reach. Guardrails bound what flows through it once it acts. A chatbot only had to screen the user's prompt and the model's reply. An agent has more surface to defend, because it also reads tool outputs and retrieved documents, and any of those can carry an instruction the user never typed. That is how indirect prompt injection works. A line like "ignore your previous instructions" sits hidden inside a document the agent ingests, and the agent treats it as a command. The fix is to move guardrails to the tool boundary, screening tool inputs and tool outputs rather than just the model's input and output. In Microsoft's case, Foundry runs its own classifiers at the tool-call and tool-response level, on top of whatever safety the model already has. Since these controls live on a shared tool layer rather than inside each agent, a team configures them once and every agent that uses those tools inherits them, instead of re-implementing the same guardrails, credentials, and policies agent by agent.

The takeaway for any team building this is that retrieval, action, and the guardrails around both need to be designed as first-class layers. Retrieval should be a loop that recovers from bad lookups, action should run under an identity the organization recognizes with an audit trail to match, and guardrails should sit at the tool boundary rather than only at the model's edges.

## Evaluate Production Agents

Context is half of what determines whether an agent survives production. Evaluation is the other half. An agent with the right context can still drift, regress, or fail in new ways as traffic patterns change. Evaluation is what closes the loop. It's the system that tells you when something has changed, and the system that tells you whether the agent is doing what it's supposed to do.

### Continuous Evaluation

Most teams treat evaluation as a pre-ship checkbox. They run a test suite once, see green, and ship. That works for traditional software because traditional software is deterministic. An agent is not. The same prompt against the same model can produce different responses, the model itself changes when the provider releases an update, and the data the agent retrieves from changes daily. A pre-ship test suite catches a snapshot of behavior, not a guarantee of it.

Continuous evaluation closes that gap by running against live traffic, sampling real user interactions, scoring them on whatever criteria the team has defined, and surfacing results into the same observability pipeline that already handles infrastructure incidents. In Foundry, this is built in. When quality regresses, the team finds out from the same alerting system that pages them when a service goes down. The same evaluations can also run earlier, as a gate in the deployment pipeline, catching a regression before it ships.

### Rubric-Based Evaluation

Continuous evaluation tells you when something has changed. The harder problem is knowing whether what the agent is doing is right in the first place. Most evaluation systems today rely on generic metrics like groundedness, coherence, and task completion. The metrics are useful but they have a ceiling. As Marco put it, generic metrics tell you whether the agent works. They don't tell you whether the agent works right.

Consider an agent that helps users book restaurant reservations. A generic metric can tell you that the agent called the booking tool successfully and returned a reservation. But it can't tell you whether the agent did the right things along the way. Did it ask the user what time they wanted when the user only said "a table for two tomorrow"? Did it check the booking system to confirm the table was actually available before claiming a 6pm slot? A reservation that gets created without those checks is technically a success against generic metrics and a failure in the user's eyes.

The way to close that gap is to evaluate the agent against the specific behaviors it should be showing, not just generic metrics. The common approach is rubric-based evaluation. A rubric is a specific, use-case-tied check that asks a yes-or-no question about something the agent should be doing. For the restaurant agent, the rubrics might look like:

* When the user gives a partial request, does the agent ask for the missing information?
* Before claiming a reservation is available, does the agent verify availability against the booking system?
* After making a booking, does the agent confirm the details back to the user?

In practice, the eval system runs the agent against a set of test interactions, scores each rubric per interaction, and rolls the results up. The team sees not just whether the agent works but which specific behaviors it's getting right and which it isn't. Rubrics work better than generic metrics because the team that owns the agent writes them, so they reflect what the agent is actually supposed to do.

Writing them by hand isn't the only path. Foundry can draft a rubric by reading the agent's configuration and its production traces, proposing the dimensions worth scoring from how the agent actually behaves. The team still owns and edits the result, but it starts from real traffic instead of a blank page.

Microsoft has built rubric-based evaluation into its Agent Optimizer suite. The Optimizer handles the rubric side of the loop and also makes the rubrics actionable by automatically improving the agent itself when a rubric fails. It can rewrite the system prompt to make the missing behavior more explicit, adjust how the agent uses its tools, or change which sources the agent prioritizes.

What it tunes goes beyond the prompt. It can also swap the underlying model and tune the agent's skills. Rather than testing one fix at a time, it produces several candidates in parallel, scores each against the rubrics, and promotes the best one as a new agent version. The same loop that measures the agent now improves it. It becomes a self-improving loop.

For any team running agents in production, evaluation isn't a phase that ends. It's a layer that runs alongside the agent, with rubrics that evolve as the agent's job evolves and an optimizer that turns regressions into actionable changes instead of manual fixes. The team's job stops being to write the perfect agent on day one and starts being to keep the agent honest as the world around it changes. That's what production AI actually looks like, and it's the second half of the harness Foundry is built around.

## The Key Lesson for Other Teams

The harness mattering as much as the model is the thread that ran through the whole conversation. The reason context is hard, the reason evaluation is hard, the reason a working prototype doesn't survive production, is that the work most teams treat as "around the model" is actually what determines whether the agent works. Treating the harness as something you add later is the most common reason an enterprise agent never makes it to production.

The practical version of that lesson for a team building its own context layer is to take the two architectural ideas from earlier in this article seriously, even if you don't use Foundry. Retrieval should be agentic. Calls to your retrieval layer should hide a planner-driven, multi-source, retry-capable subagent that can recover from a bad lookup instead of breaking on one. And agents that take actions should have identities the organization recognizes, with audit trails that survive a compliance review. Both of these are buildable on top of any platform.

## What's Next

Marco thinks about the future of AI by watching what's about to become possible in the next year, not what's ten years away. He tracks the moment a capability stops being a research demo or a developer tool and becomes something an ordinary person can use. The pattern he watches most closely is the one where capabilities that used to require a CLI coding agent become available to everyone.

This pattern has been playing out for the last eight months. Capabilities that used to require a developer to wire up inside a coding agent, things like writing a document from natural language, managing a calendar, or running a custom workflow, are now showing up in tools. Skills, which started as a coding-agent concept, are now in Excel for tasks like financial analysis and private equity workflows. Marco's expectation is that this pattern keeps accelerating, with more developer-only capabilities crossing into general use over the next year.

The bigger shift he sees coming is toward agents that improve themselves. The architectural pieces are global and local memory, plus skills, plus the kind of behaviors that let an agent retain what it learns about a user and apply it automatically. Copilot CLI's new Chronicle feature is an early version. If Marco always commits his Git repos to GitHub immediately after creating them, Chronicle learns that and starts doing it for him without being asked. Marco's bet is that this combination, applied to the kinds of agents enterprises are already deploying, is the story of the next year. Not science fiction. Just the next set of capabilities crossing into general use.
