---
type: raw
source: "https://www.anthropic.com/research/claude-code-expertise"
author:
  - "[[Zoe-Hitzig]]"
  - "[[Anthropic]]"
published: "2026-06-16"
created: "2026-06-17"
tags:
  - clippings
  - agentic-engineering
  - coding-agents
  - domain-expertise
  - labor-market
---

# Agentic coding and persistent returns to expertise

## Key findings

- Building on prior work, we introduce a framework for studying interactive agentic coding based on a privacy-preserving analysis of ~400,000 Claude Code sessions from between October 2025 and April 2026. We evaluate the composition of tasks, human-AI collaboration, and success rates.
- In a typical session, people make most of the planning decisions (what to do) and Claude makes most of the execution decisions (how to do it). The greater domain expertise a person brings to a session, the more work Claude does per instruction. On coding tasks, every major occupation succeeds at nearly the same rate as software engineers, on average.
- The more domain expertise a person has, the more often the session ends in success—though the gap between intermediate and expert users is modest. Over the seven months we observe, the share of sessions spent debugging fell by nearly half, and usage shifted toward more end-to-end agentic use: deploying and running code, analyzing data, and writing non-code documents.
- Over those seven months, the value of the typical task, which we estimate through a comparison to freelance job postings, rose in almost every kind of work—about 25% on average.

## Introduction

Agentic coding has taken off. The share of GitHub projects with coding agent activity has more than doubled since late 2025, and Claude Code users now spend an average of 20 hours per week using the tool. Can people without formal coding experience successfully direct an agent through complex technical work? And what will rapid adoption and improvement of these tools mean for knowledge work broadly?

This report provides evidence on how Claude Code is used in practice, based on a privacy-preserving analysis of ~400,000 interactive sessions from ~235,000 people between October 2025 and April 2026.

What happens on Claude Code may be a preview of where knowledge work is headed, as agents become embedded in non-coding work. We find that Claude is handling more complex and more valuable tasks. At the same time, there remains a clear division of labor in agentic coding: People decide what to build, and the agent decides how to build it.

We also see evidence that domain expertise, and not coding proficiency, amplifies effective use of the tool. In particular, domain experts succeed more often, and more easily recover from errors and misunderstandings. However, the gap between experts and intermediates is modest—suggesting that proficiency in a domain is enough to use the tool almost as effectively as those with deep mastery.

## The division of labor

### What people use Claude Code for

To understand what people are using Claude Code for, we classify each session into one of nine work modes. Four modes involve writing or maintaining code directly: building something new, fixing something broken, testing code, and orchestrating other agents or automated pipelines. Another category is operating software—deploying, configuring, running pipelines, monitoring systems. Two categories are more about working out what to do: understanding how an existing system works, and planning a change before making it. And two take actions unrelated to code, or where code is incidental to the final product: analyzing data, and communicating via presentations and other prose-based documents.

About 56% of sessions consist of writing (25%), fixing (26%), or testing and orchestrating code (5%). Operating software comprises 17%, while 14% of sessions are planning or exploring, and 13% produce analysis or prose.

### Who decides what

On average, people make about 70% of the planning decisions but only 20% of the execution decisions. In practice, there is a clear division of labor in agentic coding—people decide what to build, and the agent decides how to build it.

In a typical session, there are about four turns. Each prompt the user sends sets off a chain of around 10 actions taken by Claude on average—and sometimes over 100. In each turn, Claude reads files, edits code, runs commands, and writes on average 2,400 words of output.

When the user keeps control of execution (i.e. makes over 80% of execution decisions), Claude takes fewer actions per turn (about eight actions). And when Claude takes control of planning (i.e. makes over 80% of planning decisions), it takes on the highest number of actions (about 16).

### Level of expertise

From each transcript, Claude rates the user's apparent expertise at the task on a five-point scale from novice to expert. The expertise classifier looks for three signals: how precisely the user frames their directions, what they ask Claude to verify, and whether the user tends to correct Claude or Claude tends to correct the user. Note that expertise is capturing something quite different from job title or general ability, and, crucially, it is task-specific. A senior engineer asking their first Rust question is a beginner at Rust. An accountant who has never used Python, but tells Claude exactly which reconciliation rules a Python script must enforce and catches the edge case it mishandles at month-end close, is an expert at that task.

In typical novice sessions, each prompt sets off about five Claude actions and roughly 600 words of output, while expert sessions set off action chains more than twice as long (12 actions) carrying five times the output (3,200 words).

## Who uses Claude Code, and for what

### The users

To understand who is doing this work, we infer each user's occupation from the session transcript, mapping it to one of 23 major groups in the Bureau of Labor Statistics' Standard Occupational Classification (SOC) taxonomy. The classifier is instructed to rely only on signals such as the project context the agent loads at the start of a session, the names and structure of their files, any artifacts they reference, and vocabulary they use. It is explicitly instructed not to treat the act of coding as evidence of a coding profession.

Within this set, Computer and Mathematical Occupations is the largest group. The next largest are Business and Financial Operations; Arts, Design, and Media; Management; and Life, Physical, and Social Sciences. The fastest-growing non-software occupation groups are management, sales, and legal occupations.

### The work

The composition of the work done with Claude Code changed substantially between October 2025 and April 2026. The clearest change is that the share of sessions spent fixing broken code fell from 33% to 19%. In its place, we saw a greater share of the work that surrounds code. Operating software grew from 14% to 21% of sessions. Writing and data analysis roughly doubled, from about 10% to 20% of sessions.

The tasks themselves also grew more valuable. The estimated value of the average session rose by 27% between October and April. The rise holds across many kinds of work. Building, operating, and fixing-type tasks all grew more valuable by roughly a third or more (about 43%, 34%, and 32% respectively).

## Success depends on what the user brings

### The returns to expertise

Across all of our success measures, the more expertise a person exhibits in a session, the more likely it is that the session succeeds. A novice-rated session reaches verified success 15% of the time and at least partial success 77% of the time. A session rated intermediate or up reaches verified success 28-33% of the time and partial success 91-92% of the time.

In each measure, most of the gain comes from moving from novice to intermediate; between intermediate and expert, the slope decreases.

A similar gradient appears in sessions that run into challenges along the way. Among sessions that hit trouble, the share that are verified successes rises from 4% for novice-rated sessions to 15% for expert-rated ones. 19% of sessions where the user appears to be a novice end abandoned, against 5-7% for everyone else.

### Occupation may matter less than expertise

People in software-related occupations reach verified success in about 30% of their sessions overall, while users from other professions reach verified success about 26% of the time. Among sessions that produce code, those numbers are 34% and 29% respectively. In code-producing sessions, every one of the ten largest occupations in our dataset lands within seven points of software engineers in terms of their success. Management occupations are highest on verified success, slightly above the software engineering occupations.

## Looking ahead

The results in this report offer an emerging picture of how agentic coding amplifies some forms of knowledge and skills, while substituting for others. In sessions that produce code, every major occupation succeeds at rates within a few points of those in software-related occupations. It appears that coding agents are making a coding background less relevant to successful programming.

At the same time, successful sessions are more likely to exhibit domain expertise. Sessions rated expert reach verified success more than twice as often as those rated novice, and when a session hits trouble, novices abandon the session at several times the rate of everyone else. The ability to steer Claude toward success comes more from command of a domain than from the ability to write code.

These findings are preliminary. As in most of our research, we cannot measure real-world outcomes, like whether code written in a session is actually used or discarded thereafter, or whether it produces an economically valuable artifact. In addition, the non-interactive usage this report excludes is a substantial share of activity.

### Citation

```
@online{hitzig2026agentic,
 author = {Zoe Hitzig and Maxim Massenkoff and Eva Lyubich and Ryan Heller and Peter McCrory},
 title = {Agentic coding and persistent returns to expertise},
 date = {2026-06-16},
 year = {2026},
 url = {https://www.anthropic.com/research/claude-code-expertise},
}
```
