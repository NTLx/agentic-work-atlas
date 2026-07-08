---
title: "Intelligence is Free, Now What? Data Systems for, of, and by Agents"
author: "Aditya G. Parameswaran, Shubham Agarwal, Kerem Akillioglu, Shreya Shankar, Sepanta Zeighami, Rishabh Iyer, Matei Zaharia, Alvin Cheung, Natacha Crooks, Joseph Gonzalez, Joseph Hellerstein, Ion Stoica"
source: "Berkeley AI Research (BAIR) Blog"
url: "https://bair.berkeley.edu/blog/2026/07/07/intelligence-is-free-now-what/"
created: 2026-07-07
tags:
  - raw
  - agentic-engineering
  - data-systems
  - agent-infrastructure
  - memory
---

# Intelligence is Free, Now What? Data Systems for, of, and by Agents

The cost of AI is dropping rapidly. GPT-4-class capabilities cost roughly $30 per million tokens in early 2023; today the same runs under $1, and some providers are pushing costs below $0.10. Across benchmarks, inference prices have fallen between 9x and 900x per year, with a median decline near 50x. Even frontier models are getting dramatically cheaper each generation, with open-source models following closely behind. And crucially, even if "Nobel-Prize-winning genius-level" intelligence isn't here yet, the intelligence that suffices for the vast majority of knowledge work is here today, and getting cheaper by the month. **At this rate, we are soon entering the era of virtually free intelligence**—the kind that is more than enough for everyday knowledge work.

So, what does this new era of near-free intelligence mean for data systems? We believe three new challenges—and opportunities—stem from near-zero inference costs:

**Data Systems *For* Agents.** Agents will soon become the dominant workload for data systems—with swarms of agents spun up in response to each end-user request. Given differences in characteristics between agents and humans—or applications acting on their behalf—*how should we redesign data systems for such agentic users?*

**Data Systems *Of* Agents.** As agents start taking on the bulk of knowledge work, a new substrate is needed for thousands of agents to manage state over long-running tasks, coordinate and reach consensus, and deal with failures. *What do data systems that reliably and efficiently run and manage agent swarms look like?*

**Data Systems *By* Agents.** Agents are rapidly becoming capable of synthesizing entire data systems in one go—meaning we can rebuild custom systems for each new workload. Verifying that such systems match intended behavior is a challenge. *What does it take to let agents synthesize data systems we can actually trust?*

## Data Systems For Agents

An agent querying a database doesn't behave like a person or a BI tool. It performs what we call **agentic speculation**: a high-volume, heterogeneous stream of work spanning schema introspection, columnar exploration, partial and then full query formulation. With multiple agents each exploring portions of the hypothesis space, each user request could amount to 1000s of individual SQL queries.

The requests from these agents have various opportunities for optimization. On a text-to-SQL benchmark with multiple agents attempting each task, only 10-20% of the sub-plans are distinct. Thus, 80-90% of sub-queries perform duplicate work. The same experiments show task success rates significantly increasing with more agentic attempts—so the redundancy is actually helpful. But from the data system perspective it's wasted work.

An agent-first data system can exploit such properties to help agents make progress faster:
- **Reuse results across overlapping sub-plans**, drawing on multi-query optimization and shared scans literature
- **Satisfice**: returning approximate answers that are good enough for agents to make progress (AQP literature)
- **Streaming results** of final or intermediate operators to help agents decide if seeing the rest is necessary
- **Rethink query interface**: instead of single SQL queries, agents could issue batches with approximation requirements; DBT-style Jinja macros for looping-based primitives
- **Proactive data systems**: instead of passive query executors, systems could steer agents, provide related query results, latency estimates, and prepare materialized/virtual views in advance

## Data Systems Of Agents

The **agentic substrate** is separate from the inference stack powering raw intelligence. So far, it has been managed through harnesses like Claude Code and Codex, coupled with various mechanisms to store and retrieve memory.

### Memory: Beyond "Files Are All You Need"

The current wisdom is that files are all you need; agents write to unstructured markdown files, which can then be searched using grep or embedding-based retrieval. At scale, this approach will no longer be effective:
- Limited context windows will break when retrieving all relevant MD fragments
- Even with growing context windows, there are latency benefits to selective retrieval
- In many cases (large databases, code bases), it's infeasible to serialize all relevant data into context

Knowledge graphs suffer from the same limitations due to their lack of structured search. What one needs is to retrieve only memory pertinent to the task, across multiple attributes (or facets) of interest.

### Structured Memory

The authors recently explored **structured memory** (arxiv:2602.13521), where memory is organized across various attributes, each set as `*` for universal applicability or a list of values to match. For a data agent, dimensions could include columns, tables, type of operation, and open-ended corrective instructions.

Example: "when performing date-time operations, use fiscal year as opposed to calendar year conventions" — this memory only applies to a given type of operation.

Open question: defining application-specific structured memory (world models for memory) — perhaps agents themselves can help define and refine the schema over time.

### Coordination and Shared State

Challenges when thousands of agents attempt to edit shared state:
- **Concurrent edits**: multiversioning and copy-on-write semantics may not suffice at scale
- **Rollback**: vast majority of agent transactions need to be rolled back, only the "correct" one persisting
- **CRDTs and operational transformation**: relevant for exactly-once semantics
- **Livelock**: incessant compensating actions preventing meaningful progress

Other concerns:
- Agent failure handling
- Communication mechanisms (direct vs shared state)
- Straggler agents
- Durable multi-agent execution (e.g., Temporal)
- Consensus mechanisms (e.g., four developer agents reaching consensus on a shared schema)

## Data Systems By Agents

If intelligence is effectively free, we can employ it to **synthesize new data systems from scratch**. General-purpose data systems may be overkill for specific workloads.

### Bespoke/Disposable Data Systems

Recent work (Bespoke OLAP, GenDB) shows one can use an agentic pipeline to synthesize a complete, workload-specific analytical engine in minutes to hours, at a cost of a few dollars. The engines are **disposable**: when the workload shifts, simply regenerate them. Similarly, custom key-value stores can be synthesized from scratch targeted to the workload.

### Verification Challenges

Specifications are typically imperfect and don't cover all corner cases. Present-day agents will exploit missing specifications to reward-hack their way to high performance metrics. Mitigation approaches:
- **Auxiliary verification agents** generating test cases to catch exploitation of corner cases (expanding the specification)
- **Generating system and proof together** — early success but more work needed
- **Iterative human-in-the-loop specifications** rather than one-shot

### Composability and Blending

- Starting from mature systems (e.g., Postgres) and removing components for higher performance
- Composable design with verified components mixed and matched per workload
- Moving away from traditional stack with clearly-defined interfaces — agents can "blend" components for new optimization opportunities
- Agents filling in missing functionality gaps or refining open-source systems in response to feature requests

## Looking Further Ahead

The boundaries between agents and data systems will likely blur:
- Agents may design the data systems they themselves run on (recursive self-improvement)
- Data systems as holistic source of truth: raw data + memory + coordination state
- Data systems incorporating agentic components — evolving from passive computation engines into intelligent, proactive, self-optimizing architectures
