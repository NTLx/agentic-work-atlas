---
title: "Building headless automation with Claude Code | Code w/ Claude"
channel: Anthropic
speaker: Sid Bidasaria (Member of Technical Staff, Anthropic)
event: Code w/ Claude
location: San Francisco, CA, USA
date: 2025-05-22
publish_date: 2025-07-31
url: https://www.youtube.com/watch?v=dRsjO-88nBs
duration_seconds: 1258
language: en
tags:
  - Claude-Code
  - SDK
  - headless-automation
  - CI-CD
  - GitHub-Action
  - agentic-engineering
clipped: 2026-06-30T14:53:17
---

# Building headless automation with Claude Code | Code w/ Claude

Presented at Code w/ Claude by @anthropic-ai on May 22, 2025 in San Francisco, CA, USA.

**Speaker:** Sid Bidasaria, Member of Technical Staff @ Anthropic
**Duration:** 20:58
**YouTube:** https://www.youtube.com/watch?v=dRsjO-88nBs

## Table of Contents
- [00:00:05] Introduction and Agenda
- [00:01:43] What is Claude Code SDK?
- [00:03:11] Basic SDK Examples
- [00:04:45] GitHub Action Live Demo
- [00:09:38] Advanced SDK Features
- [00:13:14] Demo Review and Results
- [00:17:02] Summary and Installation

---

## 中文摘要

Anthropic 工程师 Sid Bidasaria 在 Code w/ Claude 活动上演示了 Claude Code SDK 的 headless 模式——一种全新的 agentic 构建原语：

1. **Claude Code SDK** = 通过 `claude -p`（headless 模式）程序化调用 Claude Code agent 的能力。支持结构化 JSON 输出、工具权限预配置、会话状态恢复
2. **GitHub Action** = SDK 之上构建的开源 CI/CD 集成：通过 issue comment 触发 agent 实现 feature、review PR、回答代码问题，完全运行在 GitHub runners 上
3. **三层架构**：SDK 基础层 → Base Action（薄封装）→ PR Action（评论/to-do list/PR 链接渲染）
4. **关键设计原则**：工具权限预配置（`--allowedTools`）、结构化输出（`--output-format JSON`）、会话状态持久化（session ID）、外部权限管理（MCP server `--permission-prompt-tool`）
5. **即将推出**：Python/TypeScript SDK 绑定

---

## Introduction and Agenda [00:00:05]

**Sid Bidasaria:** Good afternoon everybody. My name is Sid. I am an engineer on the Claude Code team. And today we're going to be talking a little bit about the Claude Code SDK and the Claude GitHub action that was just announced today.

So a little bit about the agenda. We'll do a little quick start for the SDK just to give some examples of how to get started and how to use the SDK. We will then dive into a live demo of the GitHub action which should be fun. The GitHub action was built on top of the SDK, so it's meant to be a source of inspiration for the kind of things that you can do using the Claude Code SDK. We'll then dive into some more advanced features of the SDK, and then we'll end with having all of you set up the Claude GitHub action on your repo so you guys can start using it and build on top of it.

Actually, before we get started, can I get a show of hands here? How many people have used Claude Code? Okay, it's a lot of people. And of the people who have used Claude Code, how many have used CLA or know what that is? Okay, far fewer people.

If you guys don't have Claude Code installed in your laptop, that's how you get it. I'd encourage you to install it in your laptops and follow along. There will be parts of this talk that will be beneficial to follow along.

## What is Claude Code SDK? [00:01:43]

So what is the Claude Code SDK? It is a way to programmatically access the power of the Claude Code agent in **headless mode**. This is powerful because it's a new kind of primitive and a new kind of building block that allows you to build applications that just weren't possible before.

Things that you can do with the SDK are super simple things to get started. For example, you can use it like a Unix tool. The Unix tool philosophy is what really makes Claude Code powerful because you can plug it in anywhere where you can run bash or a terminal. You can pipe stuff into it, pipe stuff out of it, have complex chains out of it. You can then build CI automation on it — have Claude review your code. Some people actually get Claude to write new linters for them too. If there are specific things that you can't define programmatically, you can get Claude Code to do it.

And then we get into fancier applications as well. If you want to build your own chatbot that's powered by Claude Code, that's certainly possible. If you want Claude Code to write you code in a new environment or a separate remote environment, you can build those kinds of applications. Finally, we have Python and TypeScript SDKs or bindings for the Claude Code SDK coming up soon — that should make it much easier for you guys to consume it and build on top of it.

## Basic SDK Examples [00:03:11]

Calling the Claude Code SDK is as simple as doing `claude -p` and following it up with the string that you want to ask Claude. For example: telling Claude to write a Fibonacci sequence generator. You also give it `--allow-tools write` which is a way to proactively give it access to the right tool so it can write files to your file system.

One thing I like doing: piping logs to Claude. You can do `cat app.log` and then pipe that into `claude -p` — "looking at logs manually." Similarly, if you're anything like me, I just can't get myself to understand the output of `ifconfig`. I still don't know what it means, but Claude does.

Finally, this is what makes the SDK tick: we have an output format. If you do `--output-format JSON`, Claude Code will actually output its response in JSON as opposed to plain text. And you can parse this JSON and build on top of it.

## GitHub Action Live Demo [00:04:45]

Let's get into a significantly more complex example: the Claude GitHub action. It was built on top of the SDK and can be used to review code, create new features, triage bugs, and so on. This is also open source.

**Demo setup:** Sid cloned a popular open-source quiz app. He opened two GitHub issues with sparse details — just wishlist features:
1. Add power-ups for 50/50 elimination of options and skip questions
2. Add per-question timer

For each issue, he commented `@claude please implement this feature and comment on it`. Claude responded on each thread with a comment saying it's working, with a link to the GitHub Action job run.

**Observed behavior:** Claude created a to-do list, went through it item by item, implemented the features, and opened pull requests. The power-up feature added a checkbox config and 50/50/skip buttons in the quiz UI — working correctly in the live demo. Claude also reviewed another existing PR (change background to blue) and was told to change it to green instead — it pushed a commit switching all three hex color definitions.

**Key insight:** You can literally comment on a thread saying "please build this for me." It uses your GitHub action runners and just does the thing.

## Advanced SDK Features [00:09:38]

**`--allowed-tools`**: When you call `claude -p`, it has no edit or destructive permission access by default — safe, but not useful. The `--allowed-tools` flag pre-configures Claude with whatever permissions you think it might need. Example: giving it bash permissions for `npm run build`, `npm test`, and the write tool — allowing Claude to self-verify what it's writing, build the project, test it, and continue.

**MCP tools**: If you have MCP servers configured, you can allow-list those MCP tools as well — very similar process.

**Structured output**: Two modes — Stream JSON (streams messages as they're available) and JSON (one giant blob at the end). Parsing this JSON and building on top of it is how you create features for your users.

**`--system-prompt`**: Configure the system prompt — e.g., `--system-prompt "talk like a pirate"`.

**Session state**: When you call `claude -p` in structured output or JSON mode, it returns a session ID. You can reference this session ID to go back to the same context state that Claude had when it finished that process. Preserving these session IDs enables user-interactive features — user says something → pass to Claude → Claude responds → user gives feedback → continue.

**`--permission-prompt-tool`**: The newest feature. Instead of pre-configuring which tools Claude can use (you might not know in advance), you can offload permission management to an MCP server. Users can accept/reject tools in real-time through the MCP server. This is fairly recent and they'd love feedback.

## Demo Review and Results [00:13:14]

Going back to the demo: the power-up issue — Claude went through its to-do list, created a PR, implemented 50/50 elimination button and skip question button. In the live test, both features worked correctly. Sid noted there's definitely more that could be done (showing which questions power-ups were used on, etc.), but at the most basic level Claude did the task it was assigned.

The "change blue to green" PR — Claude added a commit to switch all three hex color definitions from blue to green.

**Key insight:** "This is kind of the power of the GitHub action because you didn't really have to run this on your own infra. You can just literally comment on a thread saying please build this for me. It uses your GitHub action runners and just does the thing."

## Summary and Installation [00:17:02]

**What the GitHub Action can do today:**
- Read your code
- Create PRs from GitHub issues
- Add commits to existing PRs/branches
- Answer questions ("Hey Claude, how does this work?")
- Review your code
- All running on existing GitHub runners — no infra to manage

**Architecture — three layers:**
1. **Claude Code SDK** — foundation, the primitives
2. **Claude Code Base Action** — thin layer, implements the piece that talks to Claude Code and returns the response
3. **PR Action** — responsible for all the fancy things: making comments, the to-do list, rendering, adding PR links

Both the base action and the PR action are open source.

**Installation:** The easiest way is to open Claude Code in a terminal in the repo you want it in, and do `/install-github-action`. This presents a flow that guides you through configuring your GitHub action and merging it. The end result is a PR with a YAML file for the GitHub action. Once you merge it and configure your API keys, you're off to the races. For Bedrock/Vertex users, instructions are a bit more manual — check the docs.

**Resources:**
- Open source repos for both the base action and the Claude Code action
- Public Claude Code GitHub repo for filing issues and feedback on the SDK, GitHub action, or Claude Code

---

## 关键引用

> "The Claude Code SDK is a way to programmatically access the power of the Claude Code agent in headless mode. It's a new kind of primitive and a new kind of building block that allows you to build applications that just weren't possible before."

> "The Unix tool philosophy is what really makes Claude Code powerful because you can plug it in anywhere where you can run bash or a terminal."

> "This is kind of the power of the GitHub action because you didn't really have to run this on your own infra. You can just literally comment on a thread saying please build this for me."

> "We have Python and TypeScript SDKs or bindings for the Claude Code SDK coming up soon."
