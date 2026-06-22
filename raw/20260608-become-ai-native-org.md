---
type: raw
title: "Become AI Native in less than 60 mins"
source: "https://www.youtube.com/watch?v=LztPaNmcWGU"
author:
  - "Greg Isenberg"
  - "Theo Taba"
published: "2026-06-08"
created: "2026-06-22"
tags:
  - clippings
  - AI-native-org
  - agent-autonomy
  - skill-chains
  - context-engineering
  - organizational-design
---

# Become AI Native in less than 60 mins

> In this episode I sit down with Theo to unpack what becoming AI native truly means. We define an AI native org as people managing agents, agents reading and writing to the company, and the company growing smarter over time. Theo opens his actual workflows, walking through a working prototype, an auto-generated client proposal microsite, and a live usability test that synthesizes feedback into a V2 in one session. We close with service-business startup ideas built on this same system, plus a free consultation offer for larger companies.

---

## 章节

| 时间 | 章节 |
|------|------|
| 00:00 | Intro |
| 04:09 | The Demis Hassabis origin story |
| 06:53 | Defining AI Native Organization |
| 08:19 | Mapping the system: people, agents, context |
| 09:18 | Why people lead: strategy, taste, trust |
| 13:23 | Agents: models using tools in a loop |
| 16:12 | Evals and defining "good" |
| 17:34 | Skill chains explained |
| 20:06 | Proposal skill-chain demo setup |
| 25:48 | Proposal microsite walkthrough |
| 30:46 | Building the Daily Blitz feature demo |
| 32:50 | Context as the foundational layer |
| 41:07 | Daily Blitz ships and the labs page |
| 43:47 | Bootstrapping context with a small team |
| 46:21 | Usability test and live feedback |
| 51:18 | Startup ideas: productize the system |
| 54:28 | Closing Thoughts |

---

## 核心要点

1. **AI Native Organization 三要素**: People（策略/品味/判断力）、Agents（模型+工具+循环）、Context（公司可读层/"大脑"）
2. **人人都是管理者**: 每个 agent 需要 clear goal、skills、tools、context 四个要素才能自主运行
3. **Skill Chains**: 多个技能顺序执行（如：构建微站 → 文案打磨 → QA 审查），产出质量更高且基于真实数据
4. **Context 层赋予 Agent "20/20 视觉"**: 活的上下文层让 agent 在几分钟内产出个性化提案
5. **Speed to Signal**: 即时原型 + 内置可用性测试 = 当天把想法转化为客户反馈

---

## 详细摘要

### 1. Defining AI Native

AI Native Organization 的定义：一个由三层组成的系统——**people manage agents, agents read and write to the company, and the company grows smarter over time**。这与"只是用 ChatGPT"有本质区别。

### 2. People Own The Bookends

AI 吃掉中间的执行层，人类聚焦两端的高价值工作：策略、品味、判断力和沟通。核心重构：**everyone becomes a manager of agents**，成功的衡量标准是团队的产出（引用 Andy Grove 的管理哲学）。

### 3. Agents And Autonomy

Agent 像新员工一样赢得自主性。自主性需要四个前提：**clear goal + right skills + right tools + rich context**。四者齐备时，agent 可以连续运行数天并产出达标的工作（通过 eval 可视化质量）。

Agent 自主性三阶段：
- **Level 1**: 与 ChatGPT/Claude 聊天
- **Level 2**: Agent 运行但人等待批准/确认
- **Level 3**: Agent 完全自主——连续运行数天无需监督

### 4. Skills And Skill Chains

**Skill chain** 是一个 macro skill，内部按顺序触发多个子技能。LCA 的实际案例：提案 skill chain 依次触发（构建微站 → 文案打磨 → QA 审查），确保每个声明都来自会议记录和数据，降低幻觉。

> "When people say AI hallucinates, imagine an eager new hire who wants to impress you and will just kind of do things to get the job done without considering that it might break trust. It's literally fake it until you make it."

### 5. The Proposal Demo

Theo 为假想的 Spotify 客户触发提案 skill chain。几分钟内生成品牌化提案微站，包含计划、团队、成本。关键细节：系统自动从过去的会议记录中提取个人化时刻（如 Maya 的唱片店隐喻、Greg 的纽约马拉松训练），将速度转化为信任和成交。

正常流程：收到提案请求 → 回顾笔记 → 协调团队 → 几天后发出。AI Native 流程：**客户刚说完需求，提案就已经在 Slack 里等你审核了**。

### 6. The Context Layer ("The Brain")

上下文层是基础。它是一个 **folder 树结构**，内含 markdown 文件，agent 可以搜索、检索和写回。循环：**Capture → Curate → Store → Execute → Experience**，所有产出和信号回流进系统。

- **Capture**: 从 Slack、会议、邮件、Linear 等工具收集信息（cron job 定期运行）
- **Curate**: 像图书馆员一样决定什么该留、什么该忽略、什么该触发行动
- **Store**: 存入 Brain/Context 层
- **Execute**: Agent 利用 context 执行工作
- **Experience**: 客户体验 → 信号回流

**Traces/Exhaust**: 执行过程中产生的决策、探索和中间产物是"cutting room floor"素材，回流进 Brain 成为可复用知识，而不是留在无人查看的文件坟墓中。

### 7. Live Prototype And Signal

Theo 通过语音在 10 分钟内构建了 Spotify "Daily Blitz" 功能，部署到 labs page，并立即运行可用性测试。Signal tab 将用户反馈综合为经验教训，一键规划 V2 并在同一 session 内执行。

**速度对比**:
| 工作流 | 传统方式 | AI Native |
|--------|---------|-----------|
| 客户提案 | 最多 3 天 | 几分钟 |
| 可点击原型 | 1-2 周 | 几分钟（含反馈收集和 V2 规划） |

### 8. Productizing The System

将 People + Agents + Context 系统打包为服务创业机会。按三维度聚焦：**行业 × 职能 × 公司规模**。餐饮业当前特别热门（碎片化且急需此类系统）。

优先级矩阵：**niche + high frequency** 的工作流最有价值——在销售电话、提案、内容中反复展示这些工作流，形成竞争壁垒。

---

## 关键引用

> "Running 100 miles an hour in the wrong direction is worse than standing still." — Demis Hassabis at Google IO

> "An AI native org is one where people manage agents, agents can read and write to the company, and the company gets smarter over time." — Theo Taba

> "Everyone is a manager now... making sure your agents are set up for success like a manager would with their team." — Theo Taba

> "Just because you use ChatGPT does not make you an AI native company. That's like if you had a website and called yourself a tech company." — Greg Isenberg

> "When people say AI hallucinates, imagine an eager new hire who wants to impress you... It's literally fake it until you make it." — Theo Taba

---

## 关键人物与组织

- **Theo Taba** — LCA (Late Checkout Agency) 联合创始人，Fortune 500 AI 转型顾问
- **Greg Isenberg** — Startup Ideas Podcast 主持人，LCA 联合创始人
- **LCA (Late Checkout Agency)** — AI Native 咨询+设计+工程公司，服务 Warner Music、Fortnite、Dropbox 等
- **Demis Hassabis** — DeepMind 联合创始人，2024 诺贝尔奖得主（开场故事引用）

---

## 完整对话记录

<details>
<summary>点击展开完整转录文本</summary>

How do you become AI native? In this episode, it is an under 60 minute master class for how to become AI native. This is the type of content that people charge tens of thousands of dollars for. But on this channel, we're giving away for free. And we're giving it away for free because I believe that people who understand how to become AI native are going to be able to outperform 99.9% of people on the planet. These are the people that are going to get raises in an economy where job losses are prevalent. These are the people that are going to actually create the one person billion dollar companies. So in this episode we break it down in the most clear way possible. You'll learn everything you need to know about how to become AI native. What does a skill chain mean? What are skills mean? How do I think about context? How do I pipe things into Claude? And how it all works together.

I brought on my co-founder Theo Taba and Theo Taba leads the world around advising the best companies on the planet to become AI native. And in this episode, he spills the sauce. This is the stuff that he keeps for ourselves and our team. But I begged him to come on. He came on and he does an absolute master class for how to become AI native and explains it in the most clear way I've ever seen on the internet. So enjoy the episode and I can't wait to see what you build.

I beg Theo Taba to come on because I think that there's such a huge opportunity in becoming AI native and everyone's saying this word AI native this AI native that but how do you actually become AI native? So Theo is my number one call with this sort of stuff. So welcome Theo to the pod. By the end of this episode, what are people going to get out of it?

Nice to see you, Greg. They're going to get three things. One, how to become an AI native org. We all want to know. We're going to talk about it today. Number two are two workflows in action of how to turn this AI native system that we're going to talk through into speed that unlock signal from your customers which is what this is all about and Greg you're going to be our signal in this demo and these workflows and then number three we got to talk startup ideas right so let's talk about a few service based startup ideas I think I'm actually gonna go out on a limb and say this is one of the hottest and fastest growing markets in our lifetime in terms of this space for startup ideas. So, I don't want to come off as hyperbolic or overblowing anything, but I do think this is a huge opportunity for folks.

So, by the end of the episode, people are going to find out what does it mean to be AI native? What does that concretely mean? And they're also going to be able to figure out, okay, if I'm a if I want to be the one person billion dollar company or I'm working in a company, how can I turn that organization into AI native? And then for the first time ever, you're actually going to allow us to peek inside of some of the workflows that you are doing within the team that you know are things that used to cost millions of dollars to do that you're doing by just becoming AI native. And you're going to not hold back. You're going to share all the sauce. Give me an example of some of the workflows you're going to show just to give people the taste and then let's get right into it.

Sure. So here's a prototype. You see this looks a lot like Spotify cuz that was the system we used. This prototype cool feature idea. You can come and listen to music live with your friends. This is just a demo of course. This is just one workflow that we're going to show how to build this in minutes. This is fully functional coded up and then also have it in a full testing suite so you can get direct signal from customers. This is just one of a lot of the things we're going to talk about today. So that's one kind of hint of what we're going to be showing.

And the trick there is it's because you run an AI native org that you were able to get such a high-fidelity beautiful prototype. And we'll get into that later.

All right, let's go.

If you'll indulge me for a minute and everyone else, I want to just tell a very very quick story that ends with our dear friend Greg here. So rewind, we're going back to the 70s. As a four-year-old kid, starts playing chess in North London, becomes a master at age 13, absolutely crushing it, uses his chess winnings to buy a Commodore Amiga, which is an old computer, new at the time, teaches himself to code, builds this amazing game, is a lead developer on this amazing game called Theme Park. They sell over a million copies, makes money from that, goes to school for computer science. Goes to school for computer science, gets a job, runs a studio, building AI native games, goes back to school, does his PhD in cognitive neuroscience, is fascinated with the brain, wants to know how it works, starts a company, gets funded by none other than Peter Thiel. And they do some incredible stuff. They fold every protein on the planet. They create an AI that beats the world's best Go player. And I think Google then buys them in 2014. Fast forward to 2024, the dude gets knighted and wins a Nobel Prize. So underachiever. Thanks, buddy. Do you know who this person is, Greg?

Well, I know because look at him and I was just with him. That's Demis.

You were just with him. Amazing. Yes, you were just with him. So, this is you and Demis at Google IO. This is Demis Hassabis, co-founder of DeepMind.

Demis had a killer quote at Google IO, "Running 100 miles an hour in the wrong direction is worse than standing still." He did emphasize the importance of speed, but that again direction is super important. And that I think ties back to an AI native org or what this is all about. So you can't just run fast for the sake of running fast. You can't just have speed for the sake of speed. You have to do it in service of your customer and you have to know what you're running to. And this is the magic. When you can work so quickly, understand the signal, understand what you're working towards, and have this AI native system set up, you can deliver incredible value for your customers and quite frankly build a moat that makes you unstoppable.

So this is what I've broken down. **An AI native org is one where people manage agents, agents can read and write to the company, and the company gets smarter over time.** That's those are the three bullets. There's of course a lot of detail buried in these that we're going to talk about, but this is the system that allows companies to move with speed and get signal from the market and that creates their moat.

And just because you use ChatGPT does not make you an AI native company or an AI native person, right? That's like the thing, I speak to people and they say they're AI native and then I look into their workflows and they're just using ChatGPT.

I couldn't agree more. It's like if you had a website and called yourself a tech company. It's just the gap is massive. So you've good it's good that you're using that stuff, don't get me wrong, but we want to really build this moat. That's what an AI native org can actually unlock is this system which is comprised of people, agents, and context. We'll get into each one of those that produces incredible speed where you can produce anything in minutes. I flashed a little teaser of that. We're going to do a couple of those. And then signal where you actually get to hear from the market often really quickly and then all of that feeds back into the system and this gets smarter and better over time.

All tracking still let's rock.

Amazing. Okay. So let's get into the system. Let's break this down a little bit. So, you had this in your newsletter. I love this. And it mapped really well, of course, to what an AI native org is comprised of. So, you have people at the top. I'm very bullish on people. Get into that in a second for strategy, taste, judgment, and of course, that trust piece. You have agents interfacing with the context on behalf of those people. And that context is really key. I think you called out you have to make your company readable to agents like AI readable or agent readable. A lot of people use different terms consumable, legible, etc., but I like readable. Let's just stick with that. And this is that shared context layer where the agents essentially have perfect vision, 20/20 vision on what the company is comprised of. And that interface between you and that data becomes an incredible level up. And that really allows you to move with speed and again get that signal to deliver for customers.

All tracking still let's rock.

Okay. So let's talk about people. There's no AI native org without AI native people. Let's just be super clear. Obvious, but I think people jump right to like let's get the agents in the system. And if your people aren't using this and they're not understanding or do not understand how to use agents and how to use the system, it doesn't matter. You can put all the tech you want in your company. You can put all the agents, all the AI, all the tools. It's not going to matter.

And so the big reframe here is what the role of a person becomes. So we have this high level how things were pre-AI where a lot of your work was done in the middle on the execution part and a little of it was spent on either side figuring out what to do the strategy etc and then on the end reviewing the work is it good enough is it not good enough what needs to change who needs to see it communicating that work. The funny thing though is like these bookends are actually really important. That some might say is the work. That is like the really important meaty part of the work. The researching, the data all of that of course we had to do, but the bookends are really important.

So we have this thing where **AI actually eats the middle**. And now with AI, you're freed up to focus on the beginning and the end while AI quote unquote eats the middle. It does all of that execution work on your behalf and you get to focus on executing and deploying your judgment, your taste, all that accrued knowledge and all of the things that make you great as a professional at the beginning and at the end of the work.

Dream come true. Yeah, I think a lot of people know this now. I think a lot of people are like, "Okay, yes, I feel I understand that my new job is to manage agents, but they're not sure what that really means."

And I think that's a great point, and that's what we're going to get into with agents. But I think the main takeaway here is that **everyone is a manager now**. And that reframe of making sure your agents are set up for success like a manager would with their team is the unlock in terms of how you look at this. It's not I've got a new tool like Salesforce or I've got a new tool like Excel. It's very different than that because essentially you have unlimited employees at your disposal and you need to make sure they're set up for success because Andy Grove you know godfather of management once said the success of a manager is the success of their team or judge based on the output of their team and to me that is that is it.

Let's talk about agents. That second layer you have done, I think probably the most comprehensive job on the internet on breaking this down. Ross, Mike, Remy, you've had some killer folks on who explain agents. So, I'm not going to spend too much time here. I'm just going to do a quick refresher and then talk about why they're important. **Agents are models using tools in a loop.** This is from Barry Zhang at Anthropic, great engineer. You got to give them an environment. You got to give them tools and you got to give them goals. And coming back to everyone's a manager now and how to think about that.

If we look at this, you want your agents right now, there's probably three levels. You're just chatting with ChatGPT. That's kind of base level or Claude or whomever. Number two is you've actually got some agents running and you're sitting there clicking waiting for the next question to pop up or permission to be granted or prompt or check-in to happen in your Claude Code or in your Codex. Approve. Approve. Approve. Maybe you have auto edits on, but someone's just there waiting for an agent to ask you if the next step is okay. The next state is the agent autonomy. And think about it like a new hire, right? At the beginning, you're having to babysit them a little bit, giving them what they need, and then over time, they're actually coming to you with stuff, and they're running for days without your oversight, maybe weeks, and it's incredible because they're doing great work, and they understand everything, and they're absolutely nailing it. This is what you want your agents to get to.

And in order for an agent to have autonomy, they need these four things. They need **a clear goal. They need the skills. They need the tools. And they need the context.** All of those to succeed and be autonomous. Again, I will bring it back to your first day on the job. If I walked in to a new company and was expected to put a board deck together for the following week on day one with no management, what would I do? Maybe the goal is somewhat clear but a little bit fuzzy. Do I have the skills to do that? Maybe from a past job but not so much. Do I have the tools? I don't even know where to start. It's my first day. Do I have the context? I don't know what's going on with this company. I just started. I will fail at that job. And I think people get impatient with the models or AI because they don't get what they want right away with a very simple prompt or none of this baked in.

The other piece on that is the concept of an eval. An eval is essentially your visibility into the output of an agent. So what did the agent do and can you see how they got there and what was produced and does the thing that is produced meet a quality bar. If you have a standard, a quality bar, an SOP, this is what good looks like that can get folded into a skill. It can also be found in context, right? It can be a reference document of something that is the pinnacle and the goal clearly defines what success looks like, when something is great, how to measure if it's great, and when it needs to be great and when it needs to be done.

So we have a skills library because again, this isn't all single player. When you're an AI native org, you have to think about how the team will benefit from this. How can other folks use agents and how can those agents use skills? So, LCA has a skills library for our work. And inside you'll see something that has five skills together. That's an interesting skill and that's what we call a **skill chain**. Essentially allows you to fire a lot of skills sequentially to make sure that your output is even better.

As the agents get more autonomous and as the skills and the models get better and as skills can start to call another skill, you can start to have that agent autonomy really start to show up and play a huge role in how you do the work. And that's the difference again between that AI native org versus a one that's maybe more AI assisted or AI curious or aren't AI at all. You're just waiting there and essentially you're managing on hard mode. You're assuming every agent is like an ultra junior, super smart, but you can't unlock that intelligence and you're just constantly there trying to direct it, trying to steer it, and it actually just gets frustrating in the end and maybe you abandon it instead of really having that autonomy. **Skill chains allow you to have more autonomous agents.**

Skill chains, like I said, are running playbooks back-to-back. Essentially, it's a macro skill with skills inside of it. So skill one then fires calls skill two, skill two fires and then calls skill three. Skill three fires and then off we go.

So I'm going to give you a demo and a workflow of one thing that we use. This is a for SIP workflow. So normally I wouldn't have to touch anything for this to fire. This fires automatically on a trigger. We're going to pretend there's a new prospect out there. People have heard of Spotify. Let's just say Spotify is a new prospect. So, we're talking to them. We've spoken to them over months, but we haven't actually closed the deal yet. And now they're ready to get a proposal from us.

Normally this would fire only on the request for a proposal picked up in a meeting transcript or sent in my inbox. It would scan and pick up that trigger and then fire this skill chain. And in about three minutes, four minutes, we'll actually see the output of this proposal.

This proposal flow fires three skills. Number one creates a proposal microsite. Used to send proposals, emails, raw text. Sometimes that works but not always. You might want something a little more elevated. Number two is a copy skill. So it makes sure that it sounds really tight. It doesn't sound like AI. It doesn't sound like someone else. It sounds like me and in the conversations we've had. And number three, a QA skill. So it reviews it all. Make sure we're not overpromising anything. Make sure we're not saying something completely egregious. And make sure we're not making anything up that is not pulled directly from transcripts or from the data. And so once it's done, it deploys it live on a link and I can see it and then it pings me in Slack.

When people say AI hallucinates, imagine again like an eager new hire who wants to impress you and will just kind of do things to get the job done without considering that it might break trust. It's literally fake it until you make it. Your job is to make sure that they don't fake it or you minimize that as much as possible.

Another thing about this proposal is LCA works with literally most of the biggest companies on the planet building AI products, designing, engineering it, and also building AI native orgs. And a big piece of why we're able to close Fortune 2000s so frequently is this being, you know, LCA is competing against companies that aren't doing this, that aren't creating these personalized proposals, going the extra mile. And this has been the result of millions of dollars of revenue because of this.

What normally happens here for companies is someone says, "I'd like a proposal." You have to then go back, review all the notes in between meetings when you have the time. You have to get back to them, say you're on it, you'll get them something. Then you have to confirm with the team when there's availability. You have to talk through it. It might be days before you get them that proposal. They might have cooled off or gone somewhere else. And that's just the reality of sales and the reality of the market that we're in and the reality of the AI era that we're in.

I got a little note from my Slack bot. I click on this, and here we go. This is the proposal that gets created. So, you've got the outline. You've got the opportunity. You've got the whole breakdown. A week by week plan of what we're going to do, the team, how we're going to do the work. A little bit about LCA and why us, the cost.

So I'll give you a few things. One, it looks pretty good. It's pretty well organized. It's pretty dialed. It's in the Spotify branding mixed with LCA's branding. The spacing, the hierarchy, it all looks pretty dialed, which I love.

I asked it to make sure that we bake in some context from the past calls that we've had with Spotify. So, you'll see a line here: "A home that works feels like a record store clerk who knows you again. And the one hands you a record says, Trust me." So, why is this line important? This is a cool line that Maya said to me in a meeting that I probably would never really remember when I'm crafting the proposal later on and coordinating with the team. What's good about this omniscient AI who sees everything, has the perfect context, is it whips up this proposal and bakes in those little moments of connection that I would love to do given more time.

And then you can see here "good luck in November save something for mile 8." This is because we know she runs training for the NYC marathon in November and mile eight is the toughest mile. So again, you're baking this stuff in on top of a great proposal on top of doing it in literally under five minutes from the moment it was requested. So that's kind of the magic here.

Normally I just fired this in Claude, but it's magic for me when I don't even know a proposal was asked for because I'm on the road, I'm in meetings, I'm doing something else. An email comes into my inbox and someone says, "Okay, we'd love to learn a little bit more. I'd love to see a proposal." The brain will understand that, pull in that trigger and fire this all without me ever having to lift a finger or even know that I needed to do this. So, it's crazy to get that Slack ping and then be like, "Oh, proposal's ready. What are they talking about? I already have a proposal." And then I go back and see what the reference of the breadcrumbs were and I'm like, "Oh, amazing. I have it." Review, send it off. And they're amazed because they're like, "How'd you get this to me? I just asked for it."

I'm actually going to start another one quickly as I talk. I'm going to speak to it. I want to create a feature for Spotify. I want it to help increase retention. I think it should be a daily mini playlist or a daily blitz of three songs. I should be able to access it from the homepage. And when I get in, there are three handpicked songs for me. I know why they were picked. I'm able to save that playlist, share it with a friend, or play the music. The goal is to build this in under 10 minutes, use all the context you have, make sure it's beautiful and matches the design system, and make sure that I can test retention.

While this is building, let's talk about context.

This is that foundational layer that powers the agents to make you truly AI native and therefore your org. Before Greg, could you tell me what LCA's SOP is for getting back to clients?

No, I cannot.

No. Could you walk into StumbleUpon and know what their strategy was for 2014?

No, I can't. Even though I was in those board meetings.

Exactly. And could you tell me who just got hired at LCA two weeks ago?

I could... No, I can't.

No. So, even I struggle with some of these things, right? Because there's so much going on and everyone's doing this and then multiply that when you're at a bigger company by n number of teams and people. You're essentially blind to the organization and the context layer literally allows you to see everything. You're essentially giving agents **20/20 vision on your company.** And so when you have these questions, when you want to know these things, when you're building stuff that requires this type of intel, you have it. You don't have to wonder. You don't have to send 14 messages or wait days for the answer. You have it.

High level. Let me take you through it. There's a capture stage, a curation stage, storing in your brain or this context layer, using it to execute, and then having customers experience it and that all flowing back into itself.

Let's talk about capture. You have a bunch of stuff going on in your company from a bunch of different tools, places. We have Slack messages, we have meeting recordings, we have emails, we have boards in Linear, we have on and on and on it goes. All of this information contains context and a lot of it is actually really helpful in producing what you need to produce for customers. So I have a routine that runs to collect this and bring it into almost like an inbox for my brain. Every hour takes it in maybe every two takes it in and leaves it there.

You don't want everything in your brain, right? You don't want all of the information from everywhere piling up. You want to curate it to a degree. So before you file it, you have like a curator, almost like a librarian. Okay, cool. What actually needs to be in here? What do we want in here? So it reads it, cleans it up, files it, decides what to ignore, and then some of those things might be triggers like the proposal I spoke to you about.

What do we act on? So it detects some language, acts on it. So it's a curation step and then you store it in this brain or this company readable agent readable context layer this memory layer.

So the brain here is just a series of folders with a bunch of different files in those folders organized in a way that agents can search and retrieve and then write back to and improve over time. That's in your brain. You have agents, people managing those agents pulling from that to execute and do the work. So they leverage the context.

You want to bring in the context. You want to file the context. You want to make the context legible. And then you want to leverage the context. You can direct the agents and set goals for them. You can ideate and prototype. You can create these artifacts. You can run skills and tasks. You can review this work, ship it, and then all of that flows back into the work into the system itself.

One little note I'll add is a lot of the work that gets done or produced, let's say that proposal or let's say this prototype, there are a lot of decisions made along the way which is tough in big orgs or even in small orgs to keep track of why did we make that decision. There's a lot of work that happens along the way, a lot of documents, explorations etc. that are actually really valuable so that's like cutting room floor stuff. **Those are the traces. Some people call the exhaust.** That's really important to come back in and then make new artifacts based on that. Maybe there's a learning or a lesson in how to get to a decision like this or how to create something. And your brain can act on all of these traces to create this and store it instead of leaving it in this graveyard of files that no one ever looks at again.

What you don't want to have happen is you're bringing in the wrong context. So you basically don't want to have output that agents are doing and it flowing back into the capture because you want to make sure that the human has basically said like this is good, this is bad, edit this. The experience is what is the human layer that basically allows the right type of context to flow back into the capture section and the brain section.

The humans still manage the agents. So you still have to have some human in the loop and some judgment on what is good and what isn't. And when you do, whenever you're chatting, whenever you're managing that agent, you will be telling it stuff, and it will be remembering it and writing it back, updating the skills, making sure it knows what's good and what's not, updating the memory, and maybe even packaging up into lessons.

And this is more from your customers and from the market. So, you're going to see stuff on how they're reacting. Are they buying more because of the new feature that you just dropped? Are they churning faster because of your new landing page? All that stuff. And that signal is what'll flow back into your tools and then therefore it will flow back into your brain and then update accordingly.

Let's check in on Claude. It's built. What I didn't cover briefly is the labs page. This was part of a labs page. We should see... there it is. The daily blitz. This is what we spoke about. This didn't exist before. It's here now, which is awesome.

This is actually pretty nice. This is like pretty clean card. It's right on the homepage like I asked. And we can click in now. You have this playlist. Why we built this for you? Great. It tells me why. One you love with two fresh picks. Love that on a little playlist. And I can play this blitz. I actually have the music playing live right now, which is super cool. And I can also share it, which is awesome.

The reason why LCA is building these things is, you have two parts of the business. There's the how to make AI native org stuff and the other part of the business is designing the next iterations of apps, websites that are AI native. A big part of your proposal process is using all the amazing context from the team and all the years of six years of work of working with the world's largest companies and putting it in there and that's helping inspire what these prototypes look like.

Totally right. And the new unlock here is how fast you can get feedback from some of the stuff you're producing, which is actually, as you know, in the game of product, the whole game, right? Is you want to produce things and check them out and see how they feel. As much as you'd want to write a however many page PRD and slowly build it and get it out there over weeks or months, if you can build a prototype in under 10 minutes that looks like this, allows people to feel it, get real reactions, that's like the game.

For people who don't have that context but who want good outputs, how do you bootstrap context?

The world is a large and lovely place my friend. So we are not the only people who have produced beautiful work. For net new stuff we're among the best in the world of thinking about AI flows, conversational UX, how to design for trust, especially with agents. Not a lot of people have done that. If you're looking back on this, go to Mobbin. Mobbin has an MCP now. Mobbin is a library of a bunch of beautiful apps, their flows and all of the different permutations. Get Spotify's design system or another one that's similar. Create a skill around it. Plug into a Mobbin MCP and all of a sudden you can create this in minutes as well.

So this isn't only LCA stuff. Maybe the ideas are easier to come by for us or faster to come by from us and maybe our agents are more plugged into that. But in terms of producing something like this, people can do it just by using the right tools and creating the right skills and then slowly loading in the right context over time.

The takeaway there is once you figure out what your output is you want to see, like which MCP exists for that output and then see how you can scrape some of these ideas and things that are working or trending and stuff like that such that the output is good.

On the labs page, what we didn't show is this test, right? This is just the labs experiment is part one. The test is part two. I'm going to show you what this test looks like, and I'm going to Slack you the URL. And what we're going to do, I'm going to complete this test. So, right now, this is part of the skill chain that I was talking about earlier. So, we have a skill chain firing for this that essentially looks like these five skills. There's a hypothesis we're trying to test. Then the build prototype skill, then a usability test skill, which we're going to show right now, a feedback synthesis skill, and then a V2 skill. This was cool. Imagine getting feedback right away and building it on the spot.

If you have it open on your screen right now, you can start it. And this is essentially what you're going to go to. There's a little bit of a usability test. This is like what a researcher might do with someone. And it asks you a few questions. How often you listen to Spotify? How do you find new music? I go through the workflow. It asks me questions along the way. How much did you want to listen to these after looking at the songs? A lot more. I go through it. How valuable? Let's just give it a seven. I need new music always. How easy is it to open? Great recommendations. Can you say more? No, I can't.

Okay. So that was the prototype. I just filled in essentially a research report. You can see this signal tab right now. There's one completed. That was me. I just completed it. In theory, you could send this link to five people, 15 people, 40 people, whatever you want. Maybe you have a community on Discord or Slack that you want early testers. You send this out, people complete it, and then all you have to do is click this. This is another skill, and it'll synthesize the results. And imagine when there's 50 results or 100. Here's some lessons. It generates some lessons on expectation, discovery, validation, and right there I could click plan V2 and then execute it and I could have a V2 done in the same session.

I think the fidelity of the insights that you get, again that perfect 20/20 vision because of the context is awesome. So you can go to results and eventually you can see everyone here. This is a little custom thing that we built but again did it all with Claude. Wasn't that challenged. It was all elite engineers doing this, we were able to do it and then you can have a report generated and when 50 people, 20 people, 10 people have kind of gone in and tested, you've got that.

There's a little grid here showing the speed impact. A proposal might have taken up to three days and now takes minutes. A clickable prototype, not a prototype in Figma, not a design prototype, a functional prototype could take one to two weeks to figure out what to build, do it, get it out in people's hands, took minutes, not only to get the prototype done, but also collect feedback and then potentially synthesize into the second version.

If we have five minutes, do you want to jam startup ideas?

I want your feedback here. My take is based on what we just showed you and based on what we just talked about. This AI native system of people, agents, and context that unlocks speed for companies that gets them signal in real time, allows them to build better things and create a moat. This is a framework that we love, that we created, that we use. You can now go deploy this if you want in what I think is the hottest best market right now for startup ideas if you're into services and eventually you could create products.

The game here is to niche down and the three vectors is industry, function, and company size. So industry could be pick your niche. Commercial real estate, dentistry, whatever it is, pick it. Restaurants are a very, very hot niche right now because they are especially fragmented and can really use this. Now, you can't go too small, they won't have the budget, but as you go up. Function, who do you want to support in that industry? Which team? And then company size. And then get incredibly good at understanding those workflows. You might already have an unfair advantage in one of these and producing the right service offering to help bring the system to those companies.

For a way to prioritize it, I had a similar two-up grid in your newsletter, which I loved. I changed it just slightly to go from niche to general and then low frequency, high frequency. So if you can find niche workflows, so for very specific niche, industry, function, company size that are high frequency and you can create those workflows and show people those on a sales call, in a brief, in a proposal, in content, keep doing that over and over, you will have a layup ahead of you. And then you can go to general, but still very important because once they get the niche stuff, they're going to want the stuff that they do all the time that's a little less niche. And then you can go into the high value niche, but low frequency, but might have higher ROI.

I think like all this stuff about AI native and AI everything can be overwhelming and can sound like a lot and it feels like you have to be a technical guru and genius to just get started and just kind of make dents in this progress. But really to become an AI native org think through the lens of managing agents and what those agents need to succeed and you will be well on your way to being ahead of most companies in the world. So I think just get started don't be scared, scrape your knee and get stuff done.

</details>
