---
type: raw
source: "https://openai.com/index/chatgpt-memory-dreaming/"
author:
  - "OpenAI"
published: "2026-06-04"
created: "2026-06-05"
tags:
  - clippings
  - memory-systems
  - context-engineering
  - dreaming
---

# Dreaming: Better memory for a more helpful ChatGPT

**Source**: OpenAI Blog
**Date**: June 4, 2026

---

Today we're beginning to roll out a more capable and scalable system for synthesizing memory, developed to tackle the staleness, correctness, and scalability challenges that we observe when memory is applied to the hundreds of millions of users and multi-year time horizons in ChatGPT.

Memory is what helps ChatGPT learn your preferences, projects, and constraints, allowing future conversations to start from shared context rather than from scratch.

Over the last two years, memory has grown into a critical part of the ChatGPT experience, helping ChatGPT better understand your context so it can help you accomplish meaningful goals over time. This is central to making ChatGPT more useful: knowing you, helping you, and doing more for you.

## How memory has evolved

Memory first launched in April 2024 (also known as saved memories). The feature let you ask ChatGPT to remember information and carry it forward into future chats.

In April 2025, we updated ChatGPT's memory by giving the model the ability to reference chat context outside of the saved memories list; this was done by introducing the first version of dreaming—a method for ChatGPT to automatically curate memories in the background by referencing chat history.

In contrast to saved memories, dreaming leverages a background process that allows ChatGPT to learn from many conversations and synthesize ChatGPT's memory state in order to always provide the freshest, most relevant context to your conversations. Dreaming also makes it easier for memory to include context that occurs naturally in conversation, without relying on explicit requests to remember something.

Over the last year, dreaming supplemented saved memories to create a step-function improvement in ChatGPT's ability to personalize responses and offset the staleness of saved memories. However, it historically was never sufficient as a standalone memory system.

Today, we are launching a significantly more capable and compute-efficient memory architecture built on top of dreaming.

The memories synthesized by dreaming are reviewable through a summary of them made visible in the memory summary page. From the memory summary, you can quickly glean the highlights of what ChatGPT knows about you, add or update information about yourself, and provide instructions on what topics ChatGPT should bring up and when. If you want to drill down into a particular area to learn more, just chat with the model.

## Memory Timeline

| Date | Milestone |
|------|-----------|
| April 2024 | Saved memories launched — explicit "remember this" commands |
| April 2025 | Dreaming V0 — background memory curation from chat history |
| June 2025 | Memory improvements rolled out to free users (short-term continuity) |
| June 2026 | Dreaming V3 — standalone memory system with automatic synthesis |

## How we evaluate memory

"Good memory" in ChatGPT means:

1. **Carry forward useful context**: You tell ChatGPT something once, and it remembers that information in your subsequent chats.
2. **Follow preferences and constraints**: If you describe a preference (e.g., you're vegetarian), then ChatGPT should take actions that are consistent with that preference going forward.
3. **Stay current over time**: Memory should account for the passage of time. Imagine "The user is planning their birthday party for next Saturday"; eventually, Sunday arrives.

### Evaluation across generations

The team evaluates how ChatGPT Plus and Pro memory has improved over time with respect to each of the three memory objectives:

1. **2024**: Saved memories
2. **2025**: Saved memories + Dreaming V0
3. **2026**: Dreaming V3

### Carrying forward context

When you start a new chat with ChatGPT, you don't have to introduce yourself from scratch. ChatGPT can save you time and build on prior context, especially for complex, long-running projects.

Saved memories were only written during the conversation and relied on strong cues to decide when to trigger memory, such as an instruction to "remember I'm traveling to Singapore in July." In practice, interacting with this system could feel like talking to someone who took a few notes, but still forgot everything that wasn't written down. Saved memories also tend to go stale over time and eventually become incorrect or irrelevant.

The new dreaming-based system improves the model's ability to recall relevant facts across conversations.

### Following preferences and constraints

Memory helps ChatGPT respond in ways that better match your preferences and constraints. In developing the new memory system, they improved ChatGPT's ability to apply relevant preferences from past conversations.

### Staying current over time

With dreaming, memories are automatically updated as time passes, allowing ChatGPT to revise its memory from "You're going to Singapore in July" to "You went to Singapore in July 2026" when the trip ends. Then, when you're back home, ChatGPT can again provide recommendations that are tailored to your home location and time zone.

## Key Technical Concepts

- **Saved memories**: Explicit user-triggered memory ("remember that I'm vegetarian")
- **Dreaming**: Background process that automatically synthesizes and curates memory from conversation history
- **Memory summary page**: User-facing review and edit interface for dreaming-synthesized memories
- **Staleness problem**: Saved memories become outdated over time; dreaming addresses this through automatic revision
- **Scalability challenge**: Memory must work across hundreds of millions of users and multi-year time horizons
