---
type: raw
source: "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents"
author:
  - "Anthropic Applied AI Team"
published: "2026-06-01"
created: "2026-07-02"
tags:
  - clippings
  - context-engineering
  - agent-engineering
  - AI-Agent
---

# Effective context engineering for AI agents

**Source**: Anthropic Engineering Blog
**Authors**: Prithvi Rajasekaran, Ethan Dixon, Carly Ryan, Jeremy Hadfield (Anthropic Applied AI team)

---

After a few years of prompt engineering being the focus of attention in applied AI, a new term has come to prominence: **context engineering**. Building with language models is becoming less about finding the right words and phrases for your prompts, and more about answering the broader question of "what configuration of context is most likely to generate our model's desired behavior?"

**Context** refers to the set of tokens included when sampling from a large-language model (LLM). The **engineering** problem at hand is optimizing the utility of those tokens against the inherent constraints of LLMs in order to consistently achieve a desired outcome. Effectively wrangling LLMs often requires *thinking in context* — in other words: considering the holistic state available to the LLM at any given time and what potential behaviors that state might yield.

## Context engineering vs. prompt engineering

At Anthropic, we view context engineering as the natural progression of prompt engineering. **Context engineering** refers to the set of strategies for curating and maintaining the optimal set of tokens (information) during LLM inference, including all the other information that may land there outside of the prompts.

As we move towards engineering more capable agents that operate over multiple turns of inference and longer time horizons, we need strategies for managing the entire context state (system instructions, tools, Model Context Protocol (MCP), external data, message history, etc).

An agent running in a loop generates more and more data that *could* be relevant for the next turn of inference, and this information must be cyclically refined. Context engineering is the art and science of curating what will go into the limited context window from that constantly evolving universe of possible information.

## Why context engineering is important to building capable agents

Despite their speed and ability to manage larger and larger volumes of data, LLMs, like humans, lose focus or experience confusion at a certain point. Studies on needle-in-a-haystack benchmarking have uncovered the concept of **context rot**: as the number of tokens in the context window increases, the model's ability to accurately recall information from that context decreases.

Like humans, who have limited working memory capacity, LLMs have an "attention budget" that they draw on when parsing large volumes of context. Every new token introduced depletes this budget by some amount, increasing the need to carefully curate the tokens available to the LLM.

This attention scarcity stems from architectural constraints of LLMs. LLMs are based on the transformer architecture, which enables every token to attend to every other token across the entire context. This results in n^2 pairwise relationships for n tokens. As context length increases, a model's ability to capture these pairwise relationships gets stretched thin.

These realities mean that thoughtful context engineering is essential for building capable agents.

## The anatomy of effective context

Given that LLMs are constrained by a finite attention budget, *good* context engineering means finding the **smallest possible set of high-signal tokens** that maximize the likelihood of some desired outcome.

**System prompts** should be extremely clear and use simple, direct language that presents ideas at the *right altitude* for the agent. The right altitude is the Goldilocks zone between two common failure modes: hardcoding complex brittle logic (creates fragility), and vague high-level guidance (fails to give concrete signals). The optimal altitude: specific enough to guide effectively, flexible enough to provide strong heuristics.

We recommend organizing prompts into distinct sections (like `<background_information>`, `<instructions>`, `## Tool guidance`, `## Output description`) and using XML tagging or Markdown headers to delineate these sections.

**Tools** should promote efficiency, both by returning token-efficient information and by encouraging efficient agent behaviors. Tools should be self-contained, robust to error, and extremely clear with respect to their intended use. A common failure mode: bloated tool sets that cover too much functionality or lead to ambiguous decision points. If a human engineer can't definitively say which tool should be used, an AI agent can't be expected to do better.

**Examples (few-shot prompting)** remain a best practice. But instead of stuffing a laundry list of edge cases, curate a set of diverse, canonical examples that effectively portray expected behavior. For an LLM, examples are the "pictures" worth a thousand words.

## Context retrieval and agentic search

Today, many AI-native applications employ embedding-based pre-inference time retrieval. As the field transitions to more agentic approaches, teams increasingly augment these with "just in time" context strategies.

Rather than pre-processing all relevant data up front, agents built with the "just in time" approach maintain lightweight identifiers (file paths, stored queries, web links) and use these references to dynamically load data into context at runtime using tools. Claude Code uses this approach: the model writes targeted queries, stores results, and leverages Bash commands like `head` and `tail` to analyze large volumes of data without ever loading the full data objects into context.

This approach mirrors human cognition: we generally don't memorize entire corpuses of information, but rather introduce external organization and indexing systems like file systems, inboxes, and bookmarks to retrieve relevant information on demand.

Letting agents navigate and retrieve data autonomously also enables **progressive disclosure** — agents incrementally discover relevant context through exploration. File sizes suggest complexity; naming conventions hint at purpose; timestamps can be a proxy for relevance. Agents can assemble understanding layer by layer, maintaining only what's necessary in working memory.

There's a trade-off: runtime exploration is slower than retrieving pre-computed data. In certain settings, the most effective agents might employ a **hybrid strategy**: retrieving some data up front for speed, and pursuing further autonomous exploration at its discretion.

### Context engineering for long-horizon tasks

Long-horizon tasks require agents to maintain coherence over sequences where the token count exceeds the LLM's context window. Three techniques:

**Compaction**: Taking a conversation nearing the context window limit, summarizing its contents, and reinitiating a new context window with the summary. In Claude Code, the model summarizes and compresses the most critical details — architectural decisions, unresolved bugs, implementation details — while discarding redundant tool outputs. The art lies in selecting what to keep vs. discard. Start by maximizing recall, then iterate to improve precision.

**Structured note-taking (agentic memory)**: The agent regularly writes notes persisted to memory outside the context window. These notes get pulled back into context at later times. Claude playing Pokemon demonstrates this: the agent maintains precise tallies across thousands of game steps, develops maps of explored regions, and maintains strategic notes — all persisted across context resets.

**Sub-agent architectures**: Rather than one agent maintaining state across an entire project, specialized sub-agents handle focused tasks with clean context windows. The main agent coordinates at high level while subagents perform deep work, returning condensed summaries (often 1,000-2,000 tokens). This pattern showed substantial improvement over single-agent systems on complex research tasks.

## Conclusion

Context engineering represents a fundamental shift in how we build with LLMs. As models become more capable, the challenge isn't just crafting the perfect prompt — it's thoughtfully curating what information enters the model's limited attention budget at each step. The guiding principle: find the smallest set of high-signal tokens that maximize the likelihood of your desired outcome.
