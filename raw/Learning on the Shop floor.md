---
title: "Learning on the Shop floor"
source: "https://x.com/tobi/status/2053121182044451016"
author:
  - "[[@tobi]]"
published: 2026-05-09
created: 2026-05-12
description: "Years ago I wrote about my apprenticeship in Germany. I dropped out of school at 16 and went to work at a Siemens subsidiary, where the most..."
tags:
  - "clippings"
---
Years ago I wrote about my [apprenticeship in Germany](https://tobi.lutke.com/blogs/news/11280301-the-apprentice-programmer). I dropped out of school at 16 and went to work at a Siemens subsidiary, where the most interesting people sat in the basement and used Delphi instead of the corporate-mandated Rosie SQL (both pretty much lost to time and progress). I learned to be a programmer by watching them. By making them coffee. By hanging around long enough that their judgment seeped into mine.

I have been thinking about that experience a lot in the last year, because we built something at Shopify that runs on the same principle.

She's called River. River is an AI agent that lives in our company's Slack. You talk to her the same way you would talk to a teammate: by mentioning River in a Slack channel. She can read code, run tests, write code, open pull requests, query our data warehouse, look at production traces, and a lot more. We use this constantly.

In the last 30 days, **5,938 Shopify employees worked with River across 4,450 different Slack channels**. It opened **1,870 pull requests in the last week alone** in our main monorepo. About one in eight pull requests merged into our codebase last week was authored by River, reviewed by us.

There are a lot of coding agents in the world right now. What makes River special is a constraint: **She only works in the open.**

## A constraint that became a feature

When we started building River, the obvious thing to do was let people use her in private. That is how many other AI assistants work. ChatGPT is a private window. Claude is a private window. Cursor is between you and the IDE.

We made the opposite decision. River lives in slack, our company chat. River does not respond to direct messages. She politely declines and suggests to create a public channel for you and her to start working in. I myself work with river in [#tobi\_river](https://x.com/search?q=%23tobi_river&src=hashtag_click) channel and many followed this pattern. Every conversation is therefore searchable. Anyone at Shopify can jump in. In my own channel, there are over 100 people who, react to threads, add color and add context, pick up the torch, help with the reviews, remind me how rusty I am, and importantly, learn from watching.

This was odd at first. People are used to private workspaces with their tools. Asking for help feels different when the whole company can see the question. But something happened that we hoped for but did not fully predict the impact of:

**People started learning from each other.**

A support engineer in [#help\_checkout](https://x.com/search?q=%23help_checkout&src=hashtag_click) would watch a backend engineer in another channel get River to find the right log query, and the next day she would do the same thing. A new hire would scroll back through [#river](https://x.com/search?q=%23river&src=hashtag_click) to see how senior people scope a request before they ever sent their first one.

As so often with German, there is a word for the kind of environment: Lehrwerkstatt. Literally: **A teaching workshop**. The whole shop floor is the classroom. You learn by being near the work. Being a constant learner is one of the core values of the firm.

Shopify wants to be a Lehrwerkstatt at scale and River has now gotten us closer to this ideal than ever. It’s osmosis learning, because it does not require a curriculum, a training plan, or a manager. It just requires everyone's work to be visible to the maximum extent possible. Everyone learns from each other.

I'm genuinely excited by this- somewhat accidental- discovery and thought I'd share.

## Why this matters more, not less, with AI

A common worry about AI is that it will make people stop thinking. Why would a junior developer learn to debug if the agent does it for them? Why would they read the codebase if they can just ask?

I think the worry is real but the framing is wrong. The risk is not that AI does the work. The risk is that AI does the work and we never learn from it. If every interaction with an agent happens in a private window, the only person who learns anything is the person at the keyboard. Everyone else is locked out of the apprenticeship.

When people work together with their agents in public, the opposite happens. The best prompt patterns spread, knowledge spreads. The clever way one developer investigated a Slack permissions bug becomes the template for how everyone else investigates. The skill someone wrote to teach River about the company's checkout data warehouse gets reused by twelve other teams. River herself learns: every channel can pre-load the zones, skills, and instructions its team needs, written by the people closest to the work. River also has a memory that is constantly learning and un-learning critical information about the company and the best way to do work.

The agent does not replace the apprentice, nor does it replace the mentor. The agent makes the whole company an apprentice because everyone is constantly watching the most experienced people work alongside it.

This is also why the merge rate keeps climbing. We did not retrain a model. We did not switch models. An improvement from 36% to 77% over two months came from people watching River work, noticing where it got stuck, and writing down what it should have known and helping make River itself a better teammate. Every team's accumulated taste flows into the agent. The agent gets better at being Shopify.

## The company moves at the speed of its slowest secret

When I think about why this matters, it comes back to something I have believed for a long time: the speed of an organization is determined by the speed of its lowest-bandwidth communication channel and rhythm. Meetings are slow. Email is slow. Private DMs are slow. Maybe not for the individuals involved in them, but for the organization. The information and decisions that come from them never fully diffuse into the rest of the organization without huge additional communication effort.

A public conversation between humans or with a competent agent is none of those things. It is fast, it is searchable, it is teachable, and it compounds. The next person who has the same question does not have to ask it.

I do not think the future of work is humans being replaced by agents. I wrote a piece in 2018 called [The Future Role of Human Excellence](https://tobi.lutke.com/blogs/news/the-future-role-of-human-excellence), about how chess got more popular, not less, after computers learned to play. The same lesson applies here. The right model is not human or machine. It is the apprentice and the master, both watching each other learn, both getting better on the shop floor.

That is what River is. This is our Lehrwerkstatt.
---

## 编译摘要

### 1. 浓缩
- **核心结论1**: Shopify 的 AI Agent "River" 通过**强制公开化（Public-only Constraint）**，将公司 Slack 变成了 **Lehrwerkstatt（教学工坊）**。
  - 关键证据: River 拒绝私聊（DM），所有交互都在公共频道。这使得 5,938 名员工可以通过“围观”高级工程师如何使用 Agent 来实现**渗透式学习（Osmosis Learning）**。
- **核心结论2**: 组织的速度取决于其**最慢秘密（Slowest Secret）**的流通速度。
  - 关键证据: 会议、邮件和私聊是低带宽且封闭的通信，阻碍了知识扩散。公开的 AI 交互是快速、可搜索、可复写的。
- **核心结论3**: AI 时代的学徒制是通过观察“主攻手”如何驾驭 Agent 实现的。
  - 关键证据: River 并非替代学徒，而是让全公司都变成了学徒，大家在公共频道观察专家如何 Scope 需求、如何纠偏、如何应用“品味”。

### 2. 质疑
- **关于"心理安全感"的质疑**: 虽然公开透明能促进学习，但对于初级员工或性格内向者，在全公司面前展示与 Agent 的笨拙交互（或错误提问）是否会产生巨大的心理压力，从而抑制他们的尝试？
- **关于"信息过载"的质疑**: 如果 4,450 个频道都在进行大规模的 AI 交互，员工如何从这种“公开放映”中筛选出真正有价值的学习样本，而不被海量的自动生成内容淹没？

### 3. 对标
- **跨域关联1**: 类似于**开源社区的 Pull Request 机制**。在开源世界，所有人都能看到顶级开发者如何 Code Review 和重构，GitHub 本身就是一个巨大的 Lehrwerkstatt。
- **跨域关联2**: 类似于**开放式厨房（Open Kitchen）**。厨师的操作过程（技巧、卫生、配合）对食客和学徒完全透明，这种可见性不仅是服务，更是信任和教育。

### 关联概念
- [[Lehrwerkstatt]]
- [[Osmosis-Learning]]
- [[Public-only-Constraint]]
- [[Agent-Native]]
- [[Knowledge-Work]]
- [[Wisdom-Work]]
- [[Tobi-Lütke]]
