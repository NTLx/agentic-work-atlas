---
type: raw
source: "https://www.lennysnewsletter.com/p/ais-third-era-the-rise-of-persistent?showTranscript=true"
transcript_source: "Substack CDN transcription.json，2026-08-31 从 canonical page 同会话解析"
title: "AI’s third era: the rise of persistent AI coworkers | Tara Seshan (OpenAI’s product lead)"
author:
  - "Tara Seshan"
  - "Lenny Rachitsky"
publisher: "Lenny's Podcast: Product | Career | Growth"
published: "2026-08-30"
created: "2026-08-31"
duration_seconds: 4904.255
transcript_segments: 945
transcript_text_characters: 81187
description: "Lenny Rachitsky 访谈 OpenAI Codex 与 ChatGPT Work 产品负责人 Tara Seshan，讨论 persistent AI coworker、steering vs. rowing、模型能力时间窗口、AI 时代 PM、产品实验、写作与知识工作验证。"
tags:
  - clippings
  - lennys-podcast
  - persistent-ai-coworker
  - ai-product
  - ai-org-design
  - product-management
  - knowledge-work
  - openai
---

# AI’s third era: the rise of persistent AI coworkers | Tara Seshan (OpenAI’s product lead)

**Source**: https://www.lennysnewsletter.com/p/ais-third-era-the-rise-of-persistent?showTranscript=true
**Hosts**: Lenny Rachitsky（Lenny's Podcast）
**Guest**: Tara Seshan，OpenAI Codex 与 ChatGPT Work 产品负责人
**Published**: 2026-08-30
**Duration**: 约 81 分 44 秒（Substack metadata: 4904.255 seconds）
**Listen**: [YouTube](https://youtu.be/zMvBMfj4cSQ) · [Spotify](https://open.spotify.com/episode/5vOt9MsvaQDIgpzN6tQMju) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/ais-third-era-the-rise-of-persistent-ai-coworkers/id1627920305?i=1000786817796)

> **Capture note**: 页面主体带有 paywall，但 showTranscript=true 页面 HTML 暴露了当前文章对应的带 speaker map 的 Substack transcription.json。以下 Transcript 保留全部 945 个非空片段的 text，并按时间戳与 speaker 重新排版；原始 JSON 的 word-level 数据未写入 Raw。

## Guest Bio

Tara Seshan leads product for Codex and ChatGPT Work at OpenAI（与此前节目嘉宾 Andrew Ambrosino 合作，后者是她的工程经理）。加入 OpenAI 前，她在 Stripe 工作六年多，是最早加入 Stripe 的五位产品经理之一；之后负责 Watershed 的产品，该公司被《Time》评为 2022 年最佳发明之一。她也是一位 founder、Thiel Fellow，以及 Lenny's Newsletter 最早三位 Fellows 之一。

## Discussion Topics（页面公开说明）

1. 从“划船（rowing）”转向“掌舵（steering）”，以及当 AI 接管执行后，人类判断力与雄心为何成为差异化因素
2. OpenAI 如何围绕未来两到三个月的模型能力构建产品
3. OpenAI 内部的产品文化梗：Is this maximally accelerated? 与 Are you mainlining it yet?
4. 为什么雄心成为公司的新瓶颈，以及提升他人雄心为何成为 PM 工作的关键部分
5. 写作作为思考（writing as thinking）与写作作为汇报（writing as reporting）的区别

## Transcript

[00:00] **Tara Seshan**: If you think about the first era of AI products as chat, the second era of these products working with agents, that third era that might come soon is how do you work with a persistent coworker who is able to get things done with you?
[00:14] **Lenny Rachitsky**: There's this idea of the overhang of what AI is capable of and what we're actually doing with it.
[00:19] **Tara Seshan**: So hard to understand what is going to emerge in the future.
[00:24] **Tara Seshan**: You fail if you build for where the models are now, you fail if you build for where you think the models will be in a year.
[00:30] **Tara Seshan**: Both outcomes are equally wrong.
[00:32] **Tara Seshan**: Only way to build is two to three months.
[00:34] **Lenny Rachitsky**: What have you had to most adapt to and adjust in how you operate as a PM in this world?
[00:38] **Tara Seshan**: Being prolific and empirical is way more important than being academic or theoretical.
[00:44] **Tara Seshan**: Rather than writing out some long reasoning doc, instead it's like, how do I get to something I can try out and test with users as fast as possible?
[00:51] **Lenny Rachitsky**: It feels like not only are we able to be more ambitious, we almost need to be more ambitious, which is not natural for a lot of people.
[00:58] **Tara Seshan**: Elevating others' ambitions or reminding them of what's possible here is a huge part of the product management role.
[01:03] **Lenny Rachitsky**: I'm curious what's most surprised you about what it's actually like to work at OpenAI.
[01:07] **Tara Seshan**: I came into the company expecting that there was a treasure trove of OpenAI secret strategy, and actually OpenAI is open.
[01:18] **Lenny Rachitsky**: Today my guest is Tara Seshan.
[01:19] **Lenny Rachitsky**: Tara leads product for both Codex and ChatGPT Work at OpenAI.
[01:24] **Lenny Rachitsky**: I believe this is the fastest growing and arguably most important AI product for knowledge workers today.
[01:29] **Lenny Rachitsky**: Tara works alongside Andrew Ambrosino, who was a recent podcast guest.
[01:33] **Lenny Rachitsky**: He's her engine manager.
[01:35] **Lenny Rachitsky**: Prior to OpenAI, Tara spent six years at Stripe where she joined as one of the first five product managers.
[01:40] **Lenny Rachitsky**: And for many of those years, she was named one of the top three stripes across the entire organization of Stripe.
[01:46] **Lenny Rachitsky**: She also led product at Watershed, was a founder, and a Thiel Fellow.
[01:50] **Lenny Rachitsky**: And most importantly of all, Tara was one of the three Lenny's Newsletter Fellows, which is a program that I ran a few years ago to highlight some of the most amazing up and coming product leaders.
[02:00] **Lenny Rachitsky**: I am so excited to see Tara in this new incredibly important and impactful role.
[02:05] **Lenny Rachitsky**: Before we get into it, don't forget to check out lennysproductpass.com for a free year of the hottest and most beautifully crafted AI products in the world available exclusively to Lenny's Newsletter subscribers.
[02:16] **Lenny Rachitsky**: With that, I bring you Tara Seshan.
[02:22] **Lenny Rachitsky**: Tara, thank you so much for being here and welcome to the podcast.
[02:25] **Tara Seshan**: Thank you, Lenny.
[02:26] **Tara Seshan**: I'm so glad to be here.
[02:27] **Tara Seshan**: It's so nice to see you.
[02:29] **Lenny Rachitsky**: I'm even more glad.
[02:30] **Lenny Rachitsky**: So you've been at OpenAI for just about a year now, which in most places would be a very short amount of time.
[02:37] **Lenny Rachitsky**: In AI time, that's like a lifetime.
[02:39] **Tara Seshan**: Yes.
[02:40] **Lenny Rachitsky**: I imagine when you joined OpenAI, you had a sense of what it was going to be like to work at a frontier lab.
[02:47] **Lenny Rachitsky**: I'm curious what's most surprised you about what it's actually like to work at OpenAI and ideally both good and bad stuff.
[02:53] **Tara Seshan**: So many things about working at OpenAI felt familiar to me because I had worked at other places that were high growth, high talent, high intensity, hyperscaling mode, places before.
[03:05] **Tara Seshan**: And so some of the things like, oh, my colleagues are so awesome or the urgency is really high felt very familiar.
[03:12] **Tara Seshan**: The part to me that actually felt the most surprising is that many companies I've worked for, in fact, all the companies I've worked for in the past have been founder led.
[03:22] **Tara Seshan**: And OpenAI is actually founders led, which is that everyone inside the company, especially in their area, is in essence a founder to some extent.
[03:34] **Tara Seshan**: The level of top-down direction at OpenAI is extremely limited relative to places I've worked for prior.
[03:43] **Tara Seshan**: And so I think when I first got to the company that was both delightful in that I had come from a founding journey before and I was like, yes, I can continue to feel like the founder of this product area or this team.
[03:58] **Tara Seshan**: And the distance between me and the market is very, very thin.
[04:02] **Tara Seshan**: And sometimes at a larger company feel insulated from what users want or feel insulated from what the market demands.
[04:09] **Tara Seshan**: But actually at OpenAI that you do not at all, you are doing everything it takes to get product market fit for your product akin to how a founder might.
[04:18] **Tara Seshan**: But the counter to this is that, or maybe the more surprising side of this is I came into the company expecting that there was a treasure trove of OpenAI secret strategy that I would be able to understand akin to how at past companies you come in and you're like, "Oh yes, this is the payments Bible and this is how we think about payments and operations."
[04:40] **Tara Seshan**: And actually OpenAI is open.
[04:43] **Tara Seshan**: Every sort of thought that exists in terms of this is how the world should look like or this is how products should be built or this is how the model should operate very, very quickly becomes a part of the public product or a part of the public messaging.
[05:00] **Tara Seshan**: And so that, to me, was incredibly both positively surprising and just a change in my operating mode for sure.
[05:09] **Lenny Rachitsky**: Telling us there's not the secret room with AGI running there with the master plan that has all the answers.
[05:14] **Tara Seshan**: Or at least I'm not in that room for sure.
[05:16] **Tara Seshan**: But I think the piece that is really inspiring to me is that so much of what OpenAI does immediately becomes something that users can touch and feel in the product and that cycle is faster than anywhere else I've seen.
[05:33] **Lenny Rachitsky**: This episode is brought to you by our season's presenting sponsor WorkOS.
[05:38] **Lenny Rachitsky**: What do OpenAI, Anthropic, Cursor, Replit, Sierra, Clay, and hundreds of other winning companies all have in common?
[05:45] **Lenny Rachitsky**: They are all powered by WorkOS.
[05:47] **Lenny Rachitsky**: If you're building a product for the enterprise, you felt the pain of integrating single sign-on, SCIM, RBAC, audit logs and other features required by large companies.
[05:57] **Lenny Rachitsky**: WorkOS turns those deal blockers into drop-in APIs with a modern developer platform built specifically for B2B SaaS.
[06:04] **Lenny Rachitsky**: Literally every startup that I'm an investor in that starts to expand upmarket ends up working with WorkOS, and that's because they are the best.
[06:12] **Lenny Rachitsky**: Whether you are a seed stage startup trying to land your first enterprise customer or a unicorn expanding globally, WorkOS is the fastest path to becoming enterprise ready and unblocking growth.
[06:23] **Lenny Rachitsky**: It's essentially Stripe for enterprise features.
[06:25] **Lenny Rachitsky**: Visit workos.com to get started or just hit up their Slack where they have actual engineers waiting to answer your questions.
[06:32] **Lenny Rachitsky**: WorkOS allows you to build faster with delightful APIs, comprehensive docs, and a smooth developer experience.
[06:38] **Lenny Rachitsky**: Go to workos.com to make your app enterprise ready today.
[06:43] **Lenny Rachitsky**: You've been a PM at a lot of different places, a long time PM leader.
[06:47] **Lenny Rachitsky**: What do you lose in this new world?
[06:49] **Tara Seshan**: When a market is more static or a market is more slow moving, you have the chance to actually do some grand strategy-esque work because it's more predictable or you can at least understand all of the pieces.
[07:01] **Tara Seshan**: As an example, payments is certainly a dynamic market to some extent, but it's also an established market and you're able to say, "Ah yes, if I take this batch, my competitor might take this other batch," or reason from first principles very rigorously through what all the next actions might be.
[07:17] **Tara Seshan**: And in fact, the nature of that market mandates that you do that.
[07:23] **Tara Seshan**: Winners will think more rigorously than everybody else.
[07:26] **Tara Seshan**: And if you aren't thinking rigorously, it shows up as carelessness because a lot of those decisions that you made could have been predicted.
[07:33] **Tara Seshan**: But in this market, it's so hard to understand what is going to emerge in the future.
[07:41] **Tara Seshan**: It's very emergent, it's very fast-changing, it's really dynamic, and most importantly, it's very, very important to stay tied to the research.
[07:48] **Tara Seshan**: And so actually being prolific and being more empirical is way more important than being maybe more academic or theoretical.
[07:59] **Tara Seshan**: And I think lots of the past companies I've worked at have been very academic and theoretical places.
[08:06] **Tara Seshan**: And it was a real switch to go from, rather than writing out some long reasoning doc, almost like a PhD thesis of what I think should be the plan for the next N amount of time, instead it's like, how do I get to something I can try out and test with users as fast as possible?
[08:23] **Tara Seshan**: And so yeah, that switch from theoretical to empirical felt very jarring at first.
[08:27] **Tara Seshan**: I was like, "Oh, am I not doing my due diligence here?
[08:30] **Tara Seshan**: Am I not being thoughtful enough?
[08:32] **Tara Seshan**: Shouldn't I be thinking through all of this in a ton of rigor?"
[08:35] **Tara Seshan**: But actually you got to try stuff and learn as much as possible.
[08:39] **Tara Seshan**: And what that means is the thinking you need to do is being as pointed as possible about what your core hypothesis is, and that hypothesis definition is the most important thing.
[08:49] **Tara Seshan**: What is actually, to use the Shishir Mehrotra phrase, like the eigenquestion, what is that specific most important thing to test?
[08:58] **Tara Seshan**: And everything else, like any other grand strategy you concoct is not relevant.
[09:03] **Lenny Rachitsky**: I'd love to hear more about that because that's really interesting as almost like here's the thing of the PM role that is not changing.
[09:09] **Lenny Rachitsky**: So much is changing, the world is changing, but there's still this piece that is even more important.
[09:14] **Lenny Rachitsky**: Speak more to that of what specifically that you think people need to focus more on.
[09:19] **Tara Seshan**: Yeah, there's so many trappings around the PM role of running execution on time and writing all these specific docs and presentations, et cetera.
[09:29] **Tara Seshan**: But the core of it has always been about, what is the most essential question you need to ask about your product?
[09:34] **Tara Seshan**: What is the thing that will determine whether your product works or doesn't work?
[09:39] **Tara Seshan**: How do you test that?
[09:40] **Tara Seshan**: How do you look at the results and how do you feed that back into a loop of refining your hypothesis and running it again?
[09:47] **Tara Seshan**: That truly has always been the PM job, and that involves, of course, trying to understand users, trying to understand the market, trying to understand the actual technology you're building, pulling those three things together to make the most sharp hypothesis you can, and then making the test as fast and effective as possible.
[10:06] **Tara Seshan**: And I think that is not only not changed, but it's become the most important thing at the company to be able to do.
[10:15] **Tara Seshan**: EMs are thinking this way, engineers are thinking this way, data scientists are thinking this way, designers are thinking this way.
[10:21] **Tara Seshan**: Everyone has moved to focus their efforts on this really, really important problem definition and testing loop.
[10:30] **Tara Seshan**: Like what are we actually doing and how do we know if it's working thing.
[10:33] **Tara Seshan**: And from a PM standpoint, it's great because PMs have always been really focused on trying to get that stuff right.
[10:40] **Tara Seshan**: That has always been the core of the job.
[10:42] **Tara Seshan**: And actually many of the other just trappings of the job have fallen away and that remains the key thing to get right every time.
[10:50] **Lenny Rachitsky**: You mentioned this idea of a loop.
[10:53] **Lenny Rachitsky**: And there's a lot of talk these days, loops were so hot, I don't know, a few weeks ago on Twitter.
[10:57] **Lenny Rachitsky**: And it feels like it continues to be a topic of discussion for knowledge work broadly.
[11:04] **Lenny Rachitsky**: And the way I understand a loop, essentially AI, here's what success looks like, go off and build and figure it out until you achieve success.
[11:13] **Lenny Rachitsky**: How do you think about just this idea of loops expanding from just software engineering to product management to all knowledge work?
[11:20] **Lenny Rachitsky**: Do you think that's going to be a thing?
[11:23] **Tara Seshan**: I do think that increasingly the future of work will look more like steering than rowing in the sense that there will be agents that you'll be able to work with that do a lot of the rowing and your role increasingly becomes steering the ship in the right direction and pointing it in the right direction.
[11:40] **Tara Seshan**: And to that point, I think that, that steering might grow higher and higher and higher level.
[11:46] **Tara Seshan**: The steering used to be at the level of, I wrote this line of code, press tab, to, oh wait, now I'm directing something a little bit more comprehensive to maybe the goal level, maybe to an even higher level.
[11:57] **Tara Seshan**: I think the steering will continue to maybe go up layers of abstraction.
[12:02] **Tara Seshan**: But ultimately I think it's still on a person to be able to find which direction are we pointing this in and given feedback and additional data, where do I want to take this thing next?
[12:12] **Tara Seshan**: Some of steering I think is about certainly what the data tells you, but a lot of it is about making opinionated call.
[12:21] **Tara Seshan**: I think sometimes that we underrate that power of intuition or even positive determinism of what we want the future to be.
[12:32] **Tara Seshan**: Like picturing, hey, I would like the product to look this way, not because the converse is not an equally viable strategy, but because I would like the world to look like the direction that I'm pushing it in.
[12:43] **Tara Seshan**: And that, I think, will always remain a opinion at least right now that is required from a person.
[12:50] **Tara Seshan**: And so I think that loops are awesome.
[12:54] **Tara Seshan**: Running agents in increasingly, increasingly larger loops where they're doing more and more of that rowing for you is great, but right now you really still need to steer.
[13:04] **Tara Seshan**: And I think work will also look like steering with other people over a group of agents that you guys work with together.
[13:13] **Tara Seshan**: Bringing in other teammates into that interaction between you and the agent where it's rowing and you're steering feels also incredibly valuable.
[13:20] **Lenny Rachitsky**: That's such an interesting way of describing it.
[13:23] **Lenny Rachitsky**: There's two thought here that come up.
[13:25] **Lenny Rachitsky**: One is if everybody has access to the same tools, the thing that will separate you is human, the person basically.
[13:33] **Lenny Rachitsky**: Otherwise, we're all just going to be building the same thing.
[13:36] **Lenny Rachitsky**: Everyone could be asking, how do we win?
[13:38] **Lenny Rachitsky**: What do we do?
[13:39] **Lenny Rachitsky**: And then the unfair advantage almost is the human brain.
[13:42] **Tara Seshan**: Yeah, I think it reminds me a lot of fashion actually in some ways.
[13:46] **Tara Seshan**: There are certainly functional clothes that everybody can wear and gets the job done.
[13:52] **Tara Seshan**: But so much about what you wear at least, or how I think about what I wear, is about what statement I want to make about my individuality or how I want to reflect to the rest of the world.
[14:01] **Tara Seshan**: And a lot of what makes that compelling is how it contrasts with other people's expression.
[14:06] **Tara Seshan**: The shirt I make makes a statement only because it is maybe different than what everybody else is doing or different than some cohort of people are doing or makes a statement about my group membership or something of that kind.
[14:17] **Tara Seshan**: And I think a lot of the products that we build feel similarly opinionated and artistic.
[14:23] **Tara Seshan**: Patrick Collison has this really nice statement, or maybe it's John Collison, has this really nice statement about software, which is that software is not like real estate.
[14:30] **Tara Seshan**: You don't put money in and get value out.
[14:33] **Tara Seshan**: It is a little bit more like filmmaking where you can put a lot of money into a film, but that doesn't guarantee that the film is successful or good.
[14:40] **Tara Seshan**: There is some auteur statement or is some opinionation and artistry that goes along with it.
[14:46] **Tara Seshan**: And I think that relies on you having something interesting to say or your team having something interesting to say about your product.
[14:54] **Lenny Rachitsky**: There's something Marty Cagan is big on, which is this idea that when you have an idea for a product or a future, rarely is that idea the thing that ends up being.
[15:04] **Lenny Rachitsky**: There's this whole process you go through to figure out what the hell actually it should be.
[15:09] **Lenny Rachitsky**: And it feels like that's kind of what you're saying here is you need to go through that process as a human to understand what it really is and what people actually want.
[15:15] **Lenny Rachitsky**: It's never going to be like, okay, got it.
[15:17] **Lenny Rachitsky**: Go build this thing.
[15:18] **Lenny Rachitsky**: I got it from the beginning.
[15:19] **Tara Seshan**: Yeah, for sure.
[15:20] **Tara Seshan**: For sure.
[15:21] **Tara Seshan**: And those loops are moving faster and faster and faster.
[15:24] **Tara Seshan**: And so your ability to form those intuitions, get the information you need to form those intuitions, and then use that with people and agents to put that into action is the key.
[15:36] **Lenny Rachitsky**: I'm curious what you think the next shift will be in how we work just broadly as knowledge workers.
[15:41] **Lenny Rachitsky**: It feels like not only do you have access to the most advanced tools that other people don't get, also you work around the most AI forward people in the world.
[15:52] **Lenny Rachitsky**: How are people working internally that you think will become a more normal way we all work using these AI tools in the next, I don't know, three to six months?
[16:02] **Tara Seshan**: Yeah, I think there's two aspects to this.
[16:04] **Tara Seshan**: One is continuing to work with agents at higher and higher levels of abstraction.
[16:12] **Tara Seshan**: So letting the agent do more and more for you independently, coming in, providing that steering, and then letting the agent continue to cook.
[16:20] **Tara Seshan**: Let the agent cook and provide details at higher of orders of abstraction feels like the way.
[16:26] **Tara Seshan**: People are increasingly thinking about agents that are persistent, that feel like teammates, that feel like coworkers, where you can work with them.
[16:33] **Tara Seshan**: The way I might work with someone on my team, which is they do a whole bunch of work, I provide input, and then they do work again.
[16:39] **Tara Seshan**: And we sync up at different cadences, look at each other's in progress work and provide more and more feedback.
[16:45] **Tara Seshan**: It feels like that coworker model is the way that things are certainly going.
[16:51] **Tara Seshan**: It feels like a much more natural interface for us to be able to work with agents, and we already see a lot of that internally as well.
[16:58] **Tara Seshan**: The second is that a lot of my work with agents thus far has been one-on-one.
[17:05] **Tara Seshan**: I work with my agent, maybe it's spawned some subagents to get some tasks done, but it's me and my agent together, and that is potentially divorced from what my colleagues are doing with their agents.
[17:16] **Tara Seshan**: And so there was a time where everyone internally was just sending their Codex threads, screenshots of their Codex threads to each other on Slack.
[17:25] **Tara Seshan**: And we're like, "Okay, well, I wanted to share with you how I got to this number.
[17:28] **Tara Seshan**: Here's how I got to this number.
[17:29] **Tara Seshan**: Here's a screenshot of what I did."
[17:31] **Tara Seshan**: But that's also not quite the most natural way for someone to collaborate together.
[17:37] **Tara Seshan**: And so as more and more work gets done with our agents, shouldn't we be able to get work done with our agents together?
[17:45] **Tara Seshan**: And what is the most natural interface to make that happen?
[17:48] **Tara Seshan**: And those are some of the things that we're thinking about.
[17:50] **Lenny Rachitsky**: Chat is what I'm picturing.
[17:52] **Lenny Rachitsky**: That makes so much sense.
[17:53] **Lenny Rachitsky**: It's like, okay, here's Tara's agent, here's my agent.
[17:56] **Lenny Rachitsky**: She did some work on some analysis.
[17:57] **Lenny Rachitsky**: I'd be, "Hey, my agent, Lenny's agent, go check, make sure this is legit and connects to the way I think about the world."
[18:04] **Tara Seshan**: Ideally, work feels like a multiplayer game where all of us together are getting stuff done, steering our agents as our agents continue to take care of more and more of those rowing tactical tasks.
[18:15] **Lenny Rachitsky**: It's interesting how it's just been this slow progression of trust and just awareness that this can be how we work.
[18:22] **Lenny Rachitsky**: Just this, "Okay, go work for longer, you can take on more."
[18:27] **Lenny Rachitsky**: There's been this talk of the slow takeoff, the fast takeoff scenarios, and everyone's afraid of this fast AI takeoff where it's way too smart and now we're in big trouble.
[18:35] **Lenny Rachitsky**: It feels very much like we're on the slow takeoff scenario, which is good, where it's just slowly iterating.
[18:40] **Lenny Rachitsky**: It doesn't feel that slow, but in a sense, we're not to some 300 IQ AI.
[18:47] **Tara Seshan**: I mean, the models are incredibly smart.
[18:49] **Tara Seshan**: But I think a lot of the things that have enabled us to then work with our agents together or have the agents take care of higher and higher order abstraction things certainly are about the intelligence, their ability to perform long-running tasks, and how long they can stay on task.
[19:03] **Tara Seshan**: But also actually, there are very meat and potatoes, tactical things that make this possible.
[19:09] **Tara Seshan**: Agents working locally are really convenient because they have access to all the data that's on your machine.
[19:14] **Tara Seshan**: To make an agent successful in the cloud, there is a ton of cloud infrastructure that you have to build to make that possible, and just access to your systems.
[19:21] **Tara Seshan**: How can agents talk to all these third-party systems that have all of your data?
[19:25] **Tara Seshan**: Just like a colleague who you hire, who you lock into a room, never give them access to Google Docs and Slack, and I don't know, the company database would not be that useful to you.
[19:34] **Tara Seshan**: Similarly, a cloud agent that is similarly isolated will not be that effective.
[19:39] **Tara Seshan**: And so a huge part of making these agents useful and achieving some of these futures are on the intelligence side, certainly, but a lot of it is also just really tactical data access, cloud infrastructure and reliability pieces that feel much more prosaic than some of the broader intelligence questions but matter in some ways just as much for the end effectiveness.
[20:05] **Lenny Rachitsky**: This touches on something else that has been coming up a bunch on this podcast, this word ambition.
[20:11] **Lenny Rachitsky**: I know you think a lot about this too.
[20:13] **Lenny Rachitsky**: It feels like not only are we able to be more ambitious because of these AI tools, we almost need to be more ambitious, which is not natural for a lot of people, because everybody can now do all these easy things really easily.
[20:27] **Lenny Rachitsky**: The easy stuff is super easy.
[20:28] **Lenny Rachitsky**: The hard stuff is easy.
[20:30] **Lenny Rachitsky**: And the thing that separates people now and companies now is just how ambitious they can be.
[20:36] **Lenny Rachitsky**: Talk about what comes up when I talk about the need and the emergence of this need for ambition.
[20:42] **Tara Seshan**: Yeah, I think the people that we see who are most effective at using AI tools don't simply use it to automate rote tasks, but use it to expand the set of things that they are capable of doing.
[20:52] **Tara Seshan**: Back in the day, before all this AI stuff, the unicorn person was someone who was a really thoughtful product sense person who also happened to be an engineer who may also have been a designer.
[21:06] **Tara Seshan**: That person was always the unicorn hire because they were able to really flatten the layers of translation needed between all of these functions and were able to build something or ideate something really quickly and easily themselves and get it up and running, and then were able to work with a team and collaborate with a team on it.
[21:26] **Tara Seshan**: And I think the most compelling thing I've found that certainly I try to be able to do with these tools and I've seen some of my most successful colleagues be able to do with these tools is really expand the set of things that are "within their range of possibilities" so that they can start realizing more and more of what's in their head into the reality, the way that someone who was previously jack of all trades was able to do.
[21:52] **Tara Seshan**: We kind of all have that superpower now that I can spin up a set of designs on something and I can go build an initial prototype of it and I can figure out the right pricing model for it and model out all the scenarios.
[22:03] **Tara Seshan**: Really, the set of possibilities have widened dramatically.
[22:07] **Tara Seshan**: And actually what that means in so many ways is that I have the ability to be, to that point earlier about film, be more of an auteur as I try to get something done and realize my vision maybe to higher fidelity.
[22:20] **Tara Seshan**: And that to me is part of what can elevate your ambitions while pursuing new ideas and new products, that because all of these things are now within reach, because this new set of capabilities is now within your reach to be able to try and access, you're not really limited.
[22:37] **Tara Seshan**: Your ambitions are no longer limited by what you're capable of executing yourself, what you're capable of communicating.
[22:44] **Tara Seshan**: It can be so much, so much wider.
[22:46] **Tara Seshan**: I think the hardest part about doing this is simply just expanding your thinking.
[22:50] **Tara Seshan**: Actually, the capabilities have expanded so dramatically.
[22:53] **Tara Seshan**: It is really expanding your thinking of what's possible in an unreasonably short timeframe.
[22:58] **Tara Seshan**: And to me, the best way of trying to do that is Patrick Collison has on his website, patrickcallison.com/fast, I think, which is all of these projects that were unreasonably ambitious that were executed in a really, really short time period.
[23:11] **Tara Seshan**: And what, for me, is now remarkable about that list of projects is that they all existed before these tools made it possible for you to learn how to build something almost instantly, or ask it with one question, "Hey, can you summarize this very complicated text or this very complicated book for me immediately?"
[23:27] **Tara Seshan**: Or can I try to do all of these things that were previously impossible to me, but now I'm able to do?
[23:32] **Tara Seshan**: "Can you make for me a CAD model of this idea that I might have?"
[23:37] **Tara Seshan**: Really, capabilities that were truly beyond my reach are now in my reach.
[23:41] **Tara Seshan**: And so if those fast projects were possible before with the capabilities we used to have, shouldn't we just see an exponential increase of the number of those types of unreasonably quickly and effectively executed things with what AI has given us?
[23:57] **Lenny Rachitsky**: To your point, the hardest part is just remembering to even to try just to be like, "Oh yeah, well let me see if Codex can do this for me."
[24:04] **Lenny Rachitsky**: It's just a new habit, a new thing we have to build in our brain.
[24:08] **Tara Seshan**: Tyler Cowen has this statement on his site, which is that most people underrate the impact of going to someone else and saying, "Hey, what is the more ambitious version of what you're doing??
[24:19] **Tara Seshan**: Or, "Couldn't you try this faster?"
[24:21] **Tara Seshan**: Or, "Couldn't you try this at a 10X bigger scale?"
[24:24] **Tara Seshan**: And in some ways, again, when I think of, what do PMs do that is incredibly effective now or what can they do that is incredibly effective now?
[24:30] **Tara Seshan**: I think elevating others' ambitions or reminding them of what's possible here is a huge part of the product management role.
[24:37] **Tara Seshan**: When folks say, "Hey, I think we can get this done in this way," or, "We can get this done by this timeline," or, "Maybe this is the first version of it," part of your job now is to elevate everyone's ambitions and say, "Actually, isn't the possibility ceiling meaningfully higher?
[24:51] **Tara Seshan**: Shouldn't we be more ambitious about what we're attempting here?
[24:54] **Tara Seshan**: Or couldn't we try this faster?"
[24:56] **Tara Seshan**: And I think it's a great place to be.
[25:00] **Tara Seshan**: It's a great place to be in terms of what you can build, what's possible, and in terms of how exciting the job becomes.
[25:08] **Lenny Rachitsky**: That is so interesting.
[25:10] **Lenny Rachitsky**: I remember Nick Turley was on the podcast who maybe had the role before you.
[25:15] **Lenny Rachitsky**: I think he's working at Enterprise Stuff now.
[25:16] **Lenny Rachitsky**: He had this meme internally.
[25:18] **Lenny Rachitsky**: "Is this maximally accelerated?"
[25:20] **Tara Seshan**: Yes.
[25:21] **Lenny Rachitsky**: There's like an emoji, I think, inside the Slack, "Is this maximally accelerated?"
[25:24] **Tara Seshan**: "Is this maximally accelerated," is totally a OpenAI meme.
[25:28] **Tara Seshan**: The other OpenAI meme that Andrew Ambrosino and I love to ask the team is, "Are you mainlining it yet?"
[25:35] **Tara Seshan**: Which is, are you using this product all day every day to get your thing done?
[25:39] **Tara Seshan**: And I think that in combination with, are we being as ambitious as possible, which is about the scope and the scale of what you're trying to do, is this maximally accelerated?
[25:51] **Tara Seshan**: Are we moving as fast as possible on it?
[25:53] **Tara Seshan**: And then are you mainlining it yet?
[25:55] **Tara Seshan**: Are you using it?
[25:56] **Tara Seshan**: And are you bringing all your taste to bear on whether this thing works and is something that people really want and tightening that feedback loop as much as possible?
[26:02] **Tara Seshan**: Those to me are the three memes of product development that we just have to spread as much as possible now.
[26:08] **Lenny Rachitsky**: I love that.
[26:09] **Lenny Rachitsky**: It's like the new dogfooding instead of dogfooding, you got to mainline it.
[26:14] **Tara Seshan**: Yeah, exactly.
[26:15] **Lenny Rachitsky**: And that shows so deeply in the tweets.
[26:19] **Lenny Rachitsky**: This is mostly how I see your team communicate of just how obsessed they are with the product and are just constantly asking, "What can we do better?"
[26:27] **Lenny Rachitsky**: "What's bugging you now?"
[26:28] **Lenny Rachitsky**: "Here's the thing we're building."
[26:30] **Lenny Rachitsky**: It's very clear how, to your point earlier, that everyone is just the founder of their product and it's very clear how they act as an external observer.
[26:40] **Lenny Rachitsky**: Are there any other memes internally?
[26:41] **Lenny Rachitsky**: Those are so interesting.
[26:42] **Lenny Rachitsky**: Any other, I don't know, cultural-
[26:44] **Tara Seshan**: Yeah, I'm trying to think if there's other good cultural memes.
[26:48] **Tara Seshan**: Certainly a really important one is feeling the AGI or just being conscious of AGI coming.
[26:56] **Tara Seshan**: There are so many outcomes for what it could look like or how one thinks about it, but a huge part of what puts most people at this company is believing in that mission of AGI being beneficial and trying to do whatever it takes to make that possible, both realization of AGI and ensuring that it is beneficial for humanity.
[27:18] **Tara Seshan**: And in building products, another just constant refrain I have to keep in the back of my mind is, are we building for where the models are going to be in two to three months?
[27:27] **Tara Seshan**: You fail if you build for where the models are now, you fail if you build for where you think the models will be in a year.
[27:33] **Tara Seshan**: Both outcomes are equally wrong, and I'm sure many people have talked about this, but both outcomes are really equally wrong.
[27:39] **Tara Seshan**: If you're too early, you're wrong.
[27:41] **Tara Seshan**: If you build something that was overly focused on a past model's capabilities, you're entirely wrong.
[27:47] **Tara Seshan**: The only way to build is two to three months.
[27:50] **Tara Seshan**: And having this meme of models are going to get way better.
[27:54] **Tara Seshan**: I need to think about the model capability as the center of this product.
[27:57] **Tara Seshan**: I need to get out of the way of the model in terms of the product constructs that I create.
[28:02] **Tara Seshan**: How do I ensure that this is right for the model in two to three months' time?
[28:05] **Lenny Rachitsky**: How do you know what two or three months is like?
[28:07] **Lenny Rachitsky**: It's a challenging understanding, especially while we're on this exponential.
[28:13] **Lenny Rachitsky**: Is it just a gut feeling?
[28:14] **Lenny Rachitsky**: Is there anything the researchers give you a sense?
[28:16] **Lenny Rachitsky**: How does that work?
[28:17] **Tara Seshan**: Yeah, certainly communicating really tightly with research on where they think things are going is incredibly important.
[28:25] **Tara Seshan**: These things aren't entirely a black box in that you know, "Hey, we're focused on these particular things.
[28:32] **Tara Seshan**: We would like models to be better at coding in these specific ways," or, "better at writing in these specific ways."
[28:38] **Tara Seshan**: So we certainly have focused efforts on making the model better at specific capabilities.
[28:43] **Tara Seshan**: And so knowing where that is and ensuring that product development is as tied as possible to what research has as its agenda and its roadmap is really important.
[28:54] **Lenny Rachitsky**: A quote that I'll never forget is when Kevin Weil was on the podcast, he was chief product officer at that time.
[29:01] **Lenny Rachitsky**: He said that this is the worst the models will ever be.
[29:04] **Lenny Rachitsky**: And it sounds so simple, but it's hard to just wrap your head around that, that this is the worst there will ever be.
[29:12] **Lenny Rachitsky**: It's such a cliche almost now to say that, but it's true.
[29:15] **Lenny Rachitsky**: It's absurd.
[29:15] **Lenny Rachitsky**: This is-
[29:16] **Tara Seshan**: Yeah, it's absurd.
[29:18] **Tara Seshan**: It's truly absurd.
[29:21] **Lenny Rachitsky**: Oh man.
[29:22] **Lenny Rachitsky**: Okay.
[29:22] **Lenny Rachitsky**: I want to talk about ChatGPT, the app, briefly.
[29:26] **Lenny Rachitsky**: Okay, so I have it open right now.
[29:28] **Tara Seshan**: Yes.
[29:30] **Lenny Rachitsky**: Okay.
[29:30] **Lenny Rachitsky**: So here's what I see in it.
[29:31] **Lenny Rachitsky**: ChatGPT, and then there's a dropdown and there's ChatGPT and Codex, and then there's this toggle, Chat and Work.
[29:39] **Lenny Rachitsky**: Tara, what is going on?
[29:40] **Lenny Rachitsky**: What are all these things?
[29:41] **Lenny Rachitsky**: Help us understand what each of these things are for.
[29:44] **Lenny Rachitsky**: And where do you think this goes?
[29:46] **Lenny Rachitsky**: Is it going to stay like this?
[29:47] **Lenny Rachitsky**: Is there a next step that you're imagining already?
[29:50] **Tara Seshan**: Our north star here is that users do not need to make decisions between picking between all these different options. Ideally, there is no toggle here. That you go to the box, you type in your task, like, I would like to build a really awesome app that, I don't know, helps my podcast guests do research before episodes or something like that.
[29:50] **Lenny Rachitsky**: Yes.
[29:50] **Lenny Rachitsky**: Do that.
[30:11] **Tara Seshan**: And it will just pick the right harness, it'll pick the right model for you to be able to get that thing done.
[30:18] **Tara Seshan**: Ideally, the choice here is not on our users to have to pick between all these different concepts and understand not only what are they trying to do, but understand the limitations and capabilities of our products.
[30:29] **Tara Seshan**: So that is certainly where we want to go.
[30:32] **Tara Seshan**: In the near term, picking between ChatGPT and Codex is really a choice for, do you want to stay in more development oriented UI or do you want to have the same power and capabilities in the ChatGPT mode?
[30:49] **Tara Seshan**: And so if you're a Codex user, keep using Codex, you're not missing out on anything, continue using it as much as possible.
[30:54] **Tara Seshan**: But if you're a ChatGPT user who is like, what are these new agentic capabilities?
[30:59] **Tara Seshan**: You should probably be in ChatGPT mode.
[31:01] **Tara Seshan**: And then when you're in ChatGPT, if you want to have conversations, if you want to search, that's where chat mode is the right thing.
[31:07] **Tara Seshan**: It's the same chat mode you know and love with better and better models and newer and newer capabilities every time.
[31:14] **Tara Seshan**: But in Work mode, that's where under the covers, this is Codex.
[31:18] **Tara Seshan**: We've removed some of the coding UI.
[31:21] **Tara Seshan**: You're not going to see a work tree pop up all of a sudden in Work mode, but it is the same power to get things done, to, for example, generate a really complex financial model.
[31:33] **Tara Seshan**: That's all possible in Work mode.
[31:36] **Tara Seshan**: And we see people, especially I mentioned our corporate finance team, use Work mode to do incredible, incredible things that were previously either manual or required deep expertise from one person on the team, become things that the whole team can be able to execute or just elevate the ambitions of everyone on the team in terms of timeline or capabilities or frontier of what they can get done.
[31:58] **Lenny Rachitsky**: Okay, that's really helpful.
[31:59] **Lenny Rachitsky**: So there's these three modes currently.
[32:01] **Lenny Rachitsky**: There's the engineering mode, the chat mode, and then the do knowledge Work mode.
[32:06] **Lenny Rachitsky**: And the knowledge Work mode, it's actually Codex doing all that work, but people may not know what Codex is, may be afraid of it.
[32:14] **Lenny Rachitsky**: Is there anything in that Work mode that's not just Codex?
[32:16] **Lenny Rachitsky**: Because that's actually really interesting.
[32:17] **Lenny Rachitsky**: Is there additional harness tweaks to make it feel a little different or is it just the same thing with a little different UI?
[32:23] **Tara Seshan**: It's really at the UI level.
[32:26] **Tara Seshan**: So Work mode and Codex mode, if you go to Codex and ask it to generate an amazing financial model to price your product or something like that or predict my revenue for the next six months or something like that, Codex will do as good a job as Work mode.
[32:40] **Tara Seshan**: It's really about whilst it's doing so, what kind of UI do you want to see in the chain of thought?
[32:44] **Tara Seshan**: What kind of technical detail do you want exposed to you?
[32:48] **Tara Seshan**: It's incredible.
[32:48] **Tara Seshan**: It's similarly powerful.
[32:50] **Tara Seshan**: And so Codex users aren't missing out on anything by not switching modes.
[32:53] **Tara Seshan**: In fact, we do not want them to.
[32:55] **Tara Seshan**: Stay in Codex and do all the stuff you want to do in Codex, and we will show you the appropriate UI based on the things you asked for.
[33:01] **Tara Seshan**: Truly our north star is to merge all these things so that users don't have to make any of these decisions.
[33:07] **Tara Seshan**: The separation is really more about how can we meet people where they are as much as possible in terms of the products that they use, in terms of their familiarity with concepts and make sure that we are enabling everyone to take advantage of working with agents, which has transformed entirely the way every single developer works.
[33:27] **Tara Seshan**: We should do the same thing with knowledge work.
[33:29] **Lenny Rachitsky**: It makes sense.
[33:32] **Lenny Rachitsky**: Because things move so fast, I imagine somebody's like, "Let's try Codex.
[33:36] **Lenny Rachitsky**: This is going to be awesome."
[33:38] **Lenny Rachitsky**: And then it takes off and there's 10 million monthly active users, and then they're like, "Wait, what are we doing here?
[33:42] **Lenny Rachitsky**: We got ChatGPT, we got Codex.
[33:44] **Lenny Rachitsky**: How do we..." So it makes sense why these things.
[33:46] **Lenny Rachitsky**: It's not going to feel obvious and perfect for a while because you have to adjust as things work and things don't work.
[33:53] **Lenny Rachitsky**: And there's these transition periods of like, okay, cool.
[33:55] **Lenny Rachitsky**: Now let's get people moving towards this vision of the super app, let's say.
[34:01] **Lenny Rachitsky**: Okay.
[34:03] **Lenny Rachitsky**: I imagine one of the hardest parts of your job is balancing this hundred billion MAU product, ChatGPT, maybe the most successful consumer product in history, with Codex, which is this new thing and other new things that you guys want to try.
[34:20] **Lenny Rachitsky**: How do you think about that, I don't know, just balancing these very innovative, fast-moving teams and products with this like, okay, there's a billion people using this, we can't change this dramatically?
[34:30] **Tara Seshan**: Yeah, I think one of the most interesting things here is that one of the goals of launching Work in ChatGPT web and launching it in the desktop app and bringing these things together was to look at those billion people who are using ChatGPT and bring them more and more of the agent's power.
[34:51] **Tara Seshan**: If you think about the first era of AI products as chat, the second era of these products is clearly working with agents and primarily has been coding agents.
[35:04] **Tara Seshan**: We'd like to bring it to more domains certainly, like knowledge work.
[35:09] **Tara Seshan**: And that is part of the goal of giving all these billion chat users the power of Work.
[35:13] **Tara Seshan**: Certainly the product challenge that's on us is, how do we not only bring it to them, but make it natural and easy to adopt, make it not a decision they have to explicitly make?
[35:24] **Tara Seshan**: We can just help them do the right thing.
[35:25] **Tara Seshan**: How do we decomplexify it so they don't need to think about things like harnesses, which feel like crazy concepts for a billion consumers to understand?
[35:34] **Tara Seshan**: So that is primarily the challenge.
[35:37] **Tara Seshan**: And then of course, that third era that might come soon is how do you work with a persistent coworker who is able to get things done with you, maybe collaboratively with other people?
[35:50] **Tara Seshan**: And so part of this challenge in the near term is we are introducing agents to a billion people who may not have experienced them yet.
[35:59] **Tara Seshan**: How do we do so in the easiest, most natural, and most usable way possible?
[36:04] **Tara Seshan**: Certainly there's a lot more for us to do to make that happen.
[36:07] **Tara Seshan**: But part of this is also a lesson I've had maybe contrasting pre-AI era or past product experience with this one, which is at previous companies, like polish was king, getting every UI interaction or getting every little thing completely right was way more important than shipping something early because time didn't make as much of a difference in terms of the outcome.
[36:34] **Tara Seshan**: And so as such, if every corner wasn't perfectly polished and everything wasn't exactly correct, you might as well not ship it.
[36:43] **Tara Seshan**: But I think what's been really compelling and interesting about this era and this product experience has been getting the product in the hands of users when you have so much conviction that, hey, it's transformative, is way better than perfect.
[36:57] **Tara Seshan**: And that urgency and that introduction of that product is so important.
[37:03] **Tara Seshan**: So we have a lot to do to make it more usable and easier for chat users, certainly especially for folks who are not maybe even using it for productivity, but using it for consumer tasks.
[37:15] **Tara Seshan**: But yeah, done is better than perfect, and we have so much more to do.
[37:20] **Lenny Rachitsky**: Yeah, I remember when this app first launched, there was a lot of comments about the confusion and seeing how quickly the team iterated and respond to the feedback is exactly what I'm hearing here is get it out, figure out what's not working, how people are using it, iterate quickly.
[37:34] **Lenny Rachitsky**: Feels like that's the model now.
[37:36] **Tara Seshan**: And of course there are things that you can continue to iterate and get that feedback prior to launching.
[37:40] **Tara Seshan**: And there's a lot that we can and should always do better.
[37:44] **Tara Seshan**: But iterating as quickly as possible and listening to the right signals is regardless of whether that's pre-launch, post-launch, ideally pre-launch, is the key thing.
[37:55] **Lenny Rachitsky**: This episode is brought to you by Mercury, radically different banking now with spend.
[38:00] **Lenny Rachitsky**: I've been a Mercury customer for so many years now.
[38:03] **Lenny Rachitsky**: I switched all my business banking to Mercury.
[38:05] **Lenny Rachitsky**: And honestly, I could not be happier.
[38:07] **Lenny Rachitsky**: It's what online banking feels like when it's built by product people, not by bankers.
[38:13] **Lenny Rachitsky**: And now, with Spend, you can give your team individual cards, set spending limits per person or per team and have expense receipts automatically pulled in from Gmail or over text.
[38:24] **Lenny Rachitsky**: You can even give your AI agents their own cards with their own limits and policies.
[38:28] **Lenny Rachitsky**: Most founders start out the same way, one card used by everybody at the company.
[38:32] **Lenny Rachitsky**: It works until it stops working.
[38:34] **Lenny Rachitsky**: Someone goes over, a receipt disappears.
[38:37] **Lenny Rachitsky**: You spend two days trying to figure out who spent what and why.
[38:40] **Lenny Rachitsky**: Spend is expense management built directly into Mercury.
[38:44] **Lenny Rachitsky**: All your team's cards, budgets and reimbursements all live in the same place as your business banking.
[38:49] **Lenny Rachitsky**: No chasing, no manual reviews, no end of month scramble.
[38:53] **Lenny Rachitsky**: The result is a team that can move fast and a founder who is no longer the bottleneck.
[38:57] **Lenny Rachitsky**: Learn more and get signed up at mercury.com.
[39:01] **Lenny Rachitsky**: Mercury is a FinTech company, not an FDIC insured bank.
[39:04] **Lenny Rachitsky**: Banking services provided to Choice Financial Group in Column N.A.
[39:06] **Lenny Rachitsky**: Members FDIC.
[39:08] **Lenny Rachitsky**: The IO card is issued by Patriot Bank and a Member FDIC pursuant to a license for MasterCard International Incorporated.
[39:14] **Lenny Rachitsky**: Something I've noticed on Twitter is there's definitely been this vibe shift from Claude Code to Codex in the past few months.
[39:23] **Lenny Rachitsky**: It used to be everyone was Claude Code this, Cloud Code that.
[39:26] **Lenny Rachitsky**: More recently, it just feels like people are leaning now towards Codex, at least on Twitter, which is a bubble, but that's where a lot of tech people are.
[39:34] **Lenny Rachitsky**: I'm curious what's shifted internally in the past, I don't know, three to six months other than Tara joining and shaping up the ship.
[39:42] **Lenny Rachitsky**: Is there anything that you can share that's just like, okay, we figured this thing out, we shifted this, we cut this thing.
[39:47] **Lenny Rachitsky**: What helped shift the vibes and help Codex become as successful as it's becoming?
[39:54] **Tara Seshan**: I think there's this phrase which is, "Before enlightenment carry water, chop wood.
[40:01] **Tara Seshan**: Post enlightenment, carry water, chop wood," sort of thing.
[40:05] **Tara Seshan**: And actually with the Codex app, the team who initially got it up and running and were working on it were super, again, user-focused, tight iteration loop, really dogfooded the thing, mainlined the app as much as possible to get everything right.
[40:22] **Tara Seshan**: Folks started to realize that was happening externally and on Twitter and users started to really notice.
[40:28] **Tara Seshan**: But the team was always really focused on users, really focused on that iteration.
[40:35] **Tara Seshan**: And it was merely, to some extent, the market catching up, that was the change.
[40:41] **Tara Seshan**: And that process has not changed internally.
[40:44] **Tara Seshan**: Everyone still constantly uses the app.
[40:47] **Tara Seshan**: Everyone who's building it obviously is a developer using it for development and is constantly fixing not only their own problems, but trying to listen to other people in the company's problems and user problems.
[40:59] **Tara Seshan**: Actually, what's sort of remarkable is that the mode of operating hasn't changed.
[41:03] **Tara Seshan**: It's always been the same thing I had mentioned earlier.
[41:06] **Tara Seshan**: Are we elevating our mission sufficiently?
[41:09] **Tara Seshan**: Are we maximally accelerating progress and are we mainlining it as much as possible?
[41:14] **Tara Seshan**: And I think it's great that users and folks on Twitter have noticed, but that operation, that full credit to the team, that hasn't changed.
[41:24] **Lenny Rachitsky**: What's really interesting about this answer is the very human part of it.
[41:29] **Lenny Rachitsky**: It's you, it's Andrew, it's Tibo, it's the team just being obsessed with the customer, the product.
[41:36] **Lenny Rachitsky**: And it's not like AI was the answer, it's the humans that made the difference.
[41:39] **Tara Seshan**: Yeah.
[41:40] **Tara Seshan**: The team deserves full credit here.
[41:43] **Tara Seshan**: Everyone on the team is incredibly thoughtful and independent and to the point of there are many founders at OpenAI, almost everyone on that team, the desktop team especially, acts like founders and cares about every piece and every detail.
[42:00] **Tara Seshan**: And when they notice an area that should be better, they go build it very independently and get the thing up and running.
[42:07] **Tara Seshan**: And if it doesn't test well internally, people aren't using it, if people don't find it useful, they'll iterate on it and then finally ship it externally.
[42:14] **Tara Seshan**: But that loop is full credit to people on the team and individuals for making that happen.
[42:20] **Lenny Rachitsky**: Something you touched on is this idea of roles overlapping, this idea of engineers are doing PME work, you're doing probably shipping prototypes and building, maybe shipping to production.
[42:30] **Lenny Rachitsky**: I don't know.
[42:32] **Lenny Rachitsky**: It feels like that also creates a lot of challenges.
[42:34] **Lenny Rachitsky**: I hear from a lot of people, "What is my job now as a designer?
[42:37] **Lenny Rachitsky**: What am I responsible for?
[42:38] **Lenny Rachitsky**: What am I not responsible for?
[42:40] **Lenny Rachitsky**: As a marketer, what am I doing?"
[42:42] **Lenny Rachitsky**: Is that something you notice?
[42:43] **Lenny Rachitsky**: Is that something that you're dealing with?
[42:46] **Lenny Rachitsky**: Just any thoughts along those lines.
[42:48] **Tara Seshan**: I think the thing I've always liked the most about working at startups, and sometimes I've started at a startup that accidentally grew into a large company, but largely primarily working at startups, is that there are very few boundaries around your role, that everything and nothing is your responsibility.
[43:04] **Tara Seshan**: But ultimately, you're accountable for success.
[43:07] **Tara Seshan**: Actually, Stripe was very, very much this way where there are no boundaries around what a engineer could do versus a product manager could do versus a designer could do.
[43:15] **Tara Seshan**: Everyone could do anything.
[43:17] **Tara Seshan**: And so actually it feels like I've always really loved that mentality and now finally capability is catching up to that.
[43:25] **Tara Seshan**: But the thing I really care about is that someone needs to look after or have core accountability for, is this product being used by users?
[43:38] **Tara Seshan**: Is it something that people want?
[43:39] **Tara Seshan**: Is it high quality?
[43:41] **Tara Seshan**: Is it effective?
[43:43] **Tara Seshan**: And whether that person is an engineer or designer or a PM or whomever, someone is the DRI.
[43:48] **Tara Seshan**: And then whatever work needs to be done to make that possible, certainly people can pick it up based on their affinity, based on their capability.
[43:57] **Tara Seshan**: But I like a team that doesn't really mind what the boundaries are between individual roles, but everyone's just focused on making the outcome happen.
[44:06] **Tara Seshan**: The converse of this is I also really love, the craft aspects of being a PM.
[44:12] **Tara Seshan**: There are so many aspects to PM craft that I know folks like Shreyas or maybe Marty Cagan, or Shishir, all these people have really espoused that I think are wonderful.
[44:23] **Tara Seshan**: And sometimes maybe some of these questions come from, "Wait, I so love the craft of my domain.
[44:31] **Tara Seshan**: By taking this more fluid approach to teamwork and collaboration to get something done, do I lose out on getting better in polishing my craft?"
[44:40] **Tara Seshan**: And I truly don't have an answer for that question.
[44:42] **Tara Seshan**: I think it's something we're all experiencing together, which is some pieces of our craft are actually getting abstracted by models being able to do it really effectively, maybe better than individuals can.
[44:54] **Tara Seshan**: And your craft moves from being able to do that very specific task you did in the past to now applying it to some other part of the product or the discipline.
[45:04] **Tara Seshan**: But yeah, that is still a question I'm thinking about, which is how do I balance my desire to be part of a team and use these tools and feel so compelled by how effective one can be now with all these products, with my love of the... Yeah, it's really fun handwriting code for an engineer all the time and one doesn't really do that anymore.
[45:28] **Lenny Rachitsky**: Yes, that's where I was going to go.
[45:29] **Lenny Rachitsky**: It's just unbelievable how different the engineering role is now.
[45:35] **Lenny Rachitsky**: It's like you used to write code all day, that was your job and that is no longer your job, and that happened so quickly, like you do not write code.
[45:42] **Tara Seshan**: I see people mourn the flow state of writing code manually yourself versus now what one does.
[45:49] **Tara Seshan**: Yeah, it's a tough transition.
[45:54] **Lenny Rachitsky**: Yeah.
[45:56] **Lenny Rachitsky**: And some people love it, some people don't, and that's a whole other topic.
[46:00] **Lenny Rachitsky**: Along those lines, something I'd like to ask people at the frontier of AI is, where do you think human brains will continue to be valuable in the future?
[46:09] **Lenny Rachitsky**: It's impossible to predict long term, will we need humans?
[46:12] **Lenny Rachitsky**: Hopefully.
[46:13] **Lenny Rachitsky**: But I'd say in the, I don't know, the next couple years, just where do you think human brains will continue to be most valuable?
[46:19] **Tara Seshan**: I think humans will continue to be the most valuable certainly as an entity of accountability, so who ultimately owns the outcome here.
[46:29] **Tara Seshan**: In some ways you can think of your agent that you're working with as your report.
[46:35] **Tara Seshan**: Ultimately who owns, what was the end product?
[46:38] **Tara Seshan**: Was it high quality?
[46:39] **Tara Seshan**: Was it a thing that you wanted it to do and say?
[46:41] **Tara Seshan**: That will certainly remain a person, at least for now, and especially in industries and places that are highly regulated or require a direct human interface.
[46:54] **Tara Seshan**: That makes a ton of sense to me.
[46:56] **Tara Seshan**: I think the human brain is also really valuable for expression.
[47:00] **Tara Seshan**: I had mentioned earlier that analogy of software is not like real estate, it is more like a film where you could put money and a great film does not come out.
[47:10] **Tara Seshan**: The greatest films are not the ones with the biggest budgets.
[47:13] **Tara Seshan**: And given that there's a certain artistry and opinionation and expression in building software where you feel like there's some authorship by a person or a group of people, and that part remains, to me, so human.
[47:27] **Tara Seshan**: What you choose to build and how it feels, feels like such a human question.
[47:34] **Tara Seshan**: I also think the human brain continues to be valuable in how we care for each other and relate to one another.
[47:41] **Tara Seshan**: That piece of my work has remained so human and has actually become more important than ever.
[47:48] **Tara Seshan**: The part where you talk to other people on your team and collectively figure out how you can be enthusiastic about a area, how you learn and work together, how you elevate each other's ambitions, all of that feels and remains such a human thing to do.
[48:05] **Tara Seshan**: Yeah, I think the human brain will continue to be so valuable in that regard.
[48:10] **Tara Seshan**: That said, I can't predict what'll happen with the models.
[48:14] **Tara Seshan**: But those pieces feel to me to be incredibly, incredibly human.
[48:18] **Lenny Rachitsky**: I love that answer.
[48:20] **Lenny Rachitsky**: There's this idea that you talked about, this idea of this overhang of what AI is capable of and what we're actually doing with it.
[48:29] **Lenny Rachitsky**: It feels like one of the biggest gaps is like, okay, what should I do with it?
[48:32] **Lenny Rachitsky**: I'm curious, what are some ways that you use AI in your work that may inspire people like, "Oh wow, I didn't think about using it that..." There's two buckets here.
[48:42] **Lenny Rachitsky**: One is just how your PM job has changed most, thanks to AI, that you're just like, "Okay, now I use AI for this stuff."
[48:49] **Lenny Rachitsky**: And then is there any super interesting creative uses of AI recently that you're like, "Oh yeah, I should try this?"
[48:55] **Tara Seshan**: One of the most exciting ways that I use AI in work is I actually build sites all the time now.
[49:03] **Tara Seshan**: I don't know if you've tried building sites in Codex.
[49:05] **Lenny Rachitsky**: I haven't talk about Sites.
[49:06] **Tara Seshan**: Sites is a really fun, amazing product.
[49:10] **Tara Seshan**: You can basically build a site, certainly in Work as a presentational artifact, but I also build sites for literally anything.
[49:17] **Tara Seshan**: I built a site for the team as a game where we all played a game together using a site because Sites have a database.
[49:25] **Tara Seshan**: I actually built a site because I went on a backpacking trip recently.
[49:28] **Tara Seshan**: I built a site of the route that tracked the elevation of everywhere we were going.
[49:33] **Tara Seshan**: Everyone on our trip inputted all their food.
[49:36] **Tara Seshan**: It was superfast and effective.
[49:38] **Tara Seshan**: Sites realized the dream of malleable personal software that Alan Kay flagged in the '60s of the true personal computer is one that has personal software.
[49:48] **Tara Seshan**: In some ways, Sites are the tangible way to make that possible.
[49:52] **Tara Seshan**: We had all once dreamed of making personal software, and certainly people with tools like Notion, et cetera, try with all these blocks to configure what that could be.
[50:01] **Tara Seshan**: But with the Site, it is literally a prompt.
[50:03] **Tara Seshan**: I literally with a prompt say, "Build me this exact tool that I need to get this thing done," and it just does it.
[50:11] **Tara Seshan**: They're shareable.
[50:12] **Tara Seshan**: They can auto update.
[50:15] **Tara Seshan**: You can use internal data to build a dashboard, for example, with lots of metrics.
[50:20] **Tara Seshan**: And rather than painstakingly laboring over some sort of slide deck, a site is just a way more dynamic surface for presentation.
[50:33] **Lenny Rachitsky**: How do you use a site? Do you have to do anything special or you tell it, create a site?
[50:33] **Tara Seshan**: In Codex be like, "Create a site that-
[50:35] **Lenny Rachitsky**: Create a site.
[50:36] **Tara Seshan**: ... is a, I don't know, is a mafia game for my team," and it will just do it.
[50:40] **Lenny Rachitsky**: And I'm thinking capital S site, but it doesn't matter, I imagine.
[50:44] **Tara Seshan**: Yeah.
[50:44] **Lenny Rachitsky**: It just knows what sites are?
[50:45] **Tara Seshan**: Mm-hmm.
[50:46] **Lenny Rachitsky**: Yeah, because it used to be, "Here's some source code, go figure out where to deploy it."
[50:50] **Tara Seshan**: Yeah.
[50:51] **Lenny Rachitsky**: And you're saying here is it just hosted for you and immediately you can use it.
[50:53] **Tara Seshan**: Host it for you.
[50:54] **Tara Seshan**: You choose whether it's public.
[50:55] **Tara Seshan**: You can choose whether it's with your team-
[50:57] **Lenny Rachitsky**: Awesome.
[50:57] **Tara Seshan**: ... or choose whether it's private to you.
[50:59] **Tara Seshan**: They're great.
[51:00] **Tara Seshan**: The easy reach of building a site all the time has changed what my day-to-day looks like, which often in previous worlds used to look like creating lots of artifacts like docs and sheets and whatever it might be.
[51:14] **Tara Seshan**: Now I just make sites all the time.
[51:16] **Lenny Rachitsky**: And you could do that through, I imagine, Work or... Can you do it through all the surfaces, Codex, Work, ChatGPT Chat?
[51:23] **Tara Seshan**: You can do it through Work. You can do it-
[51:23] **Lenny Rachitsky**: Okay, cool.
[51:25] **Tara Seshan**: ... through Codex.
[51:25] **Tara Seshan**: You can do it in the web.
[51:25] **Tara Seshan**: You can do it on mobile.
[51:26] **Tara Seshan**: You can do it anywhere.
[51:27] **Lenny Rachitsky**: Okay.
[51:27] **Lenny Rachitsky**: I just kicked off create a site about Tara Seshan.
[51:30] **Tara Seshan**: Great.
[51:31] **Lenny Rachitsky**: Is that how you pronounce your last name, by the way?
[51:32] **Lenny Rachitsky**: I haven't asked you.
[51:35] **Tara Seshan**: Tara Seshan, like station.
[51:37] **Lenny Rachitsky**: Seshan. Okay, cool. Okay, cool. Sites. Okay. Any other quick tips, while we're on this-
[51:37] **Tara Seshan**: I think that-
[51:44] **Lenny Rachitsky**: ... topic, for people?
[51:44] **Lenny Rachitsky**: Because that was a great tip, because I don't think a lot of people know about Sites, so it's very useful.
[51:47] **Tara Seshan**: Yeah, Sites are awesome.
[51:48] **Tara Seshan**: The other thing I really love is using Visualize in Codex.
[51:52] **Tara Seshan**: Have you used /visualize?
[51:53] **Lenny Rachitsky**: No.
[51:54] **Tara Seshan**: Oh, /visualize is incredibly exciting.
[51:57] **Tara Seshan**: You can just do /visualize, visualize my ChatGPT usage until now, or something like that, and it will pull in all the things that you've done and create an amazing visualization for it.
[52:07] **Tara Seshan**: The number of times that I've been thinking about, how do I not only pull in a bunch of charts and data, but present them in a way that is understandable and useful for the story I'm trying to tell has been infinite.
[52:19] **Tara Seshan**: And Visualize makes that incredibly simple.
[52:22] **Tara Seshan**: It is surprisingly delightful to use Visualize.
[52:26] **Lenny Rachitsky**: These are such good examples of there's so much power here we don't even know about or understand, and that's the challenge you have here. Help us-
[52:26] **Tara Seshan**: For sure, for sure.
[52:34] **Lenny Rachitsky**: Help us know all these things.
[52:35] **Lenny Rachitsky**: That's why podcasts like this are also useful.
[52:37] **Lenny Rachitsky**: Can't put it all in the product.
[52:39] **Lenny Rachitsky**: I'm going to go in a totally different direction.
[52:41] **Lenny Rachitsky**: I'm going to talk about writing.
[52:43] **Lenny Rachitsky**: I asked Brie Wolfson, who knows you well, what to ask you.
[52:47] **Lenny Rachitsky**: Funny enough, she suggested questions for the previous podcast conversation I did with Adam Ward from Cursor.
[52:53] **Lenny Rachitsky**: So she said, "Okay, you should ask her about writing/thinking.
[52:57] **Lenny Rachitsky**: A Tara brief is iconic."
[53:00] **Lenny Rachitsky**: Help us understand just what makes your writing your briefs iconic and any tips that might be helpful for people that are maybe trying to get better at writing and writing documents.
[53:13] **Tara Seshan**: I really strongly believe that I do two types of writing at work.
[53:16] **Tara Seshan**: One is writing as thinking, and the other is writing as reporting.
[53:20] **Tara Seshan**: Writing as thinking is me writing a brief about why we should build a certain product or why we should take a certain strategy or why maybe a spicy take.
[53:30] **Tara Seshan**: But writing as reporting is things like, oh, I'm summarizing the status of what our team has been up to this week and I'm sending over a report about it, or this is our plan for this particular launch or announcement or something like that.
[53:42] **Tara Seshan**: Writing as reporting, I happily automate or I use the models all the time to make that as simple as it can be.
[53:50] **Tara Seshan**: But writing as thinking is something I never will automate.
[53:54] **Tara Seshan**: I really strongly believe that, at least for me, the act of going through and outlining something, turning it into some level of pros, cutting it and editing it, continuing to iterate on it is one of the most important steps for me to get my ideas in line.
[54:13] **Tara Seshan**: I think most people actually will paint with a really broad brush, like, "I will never use the models for writing," or, "I always use the models for writing."
[54:22] **Tara Seshan**: And actually to me, both those broad brushes are wrong.
[54:25] **Tara Seshan**: I think you should use the models as much as possible for writing as reporting.
[54:29] **Tara Seshan**: And in as much as you think with writing, as I really do and I think a lot of people do, you should not use it.
[54:36] **Tara Seshan**: You shouldn't replace your thinking with it.
[54:38] **Tara Seshan**: But my briefs in the past, because I write so much as a way of thinking, is that I will go into a hole, write a brief for a new idea or a product, spend a ton of time refining that particular idea, shop it around with people and have them attack the ideas in it as much as possible and poke holes, make it stronger, and then take it to the next person and do the same thing.
[55:04] **Tara Seshan**: And so at Stripe, this is something I did many, many, many, many times over, whether that was to kick off a new product area or to suggest a big change in direction or to analyze a problem and suggest a path forward.
[55:20] **Tara Seshan**: And Stripe is incredibly oriented as a writing culture.
[55:24] **Tara Seshan**: And there are many people, like Jeff Weinstein, who are also very into writing and sharing briefs at Stripe.
[55:31] **Tara Seshan**: Stripe is one of the few places where a brief will go viral inside the company.
[55:35] **Tara Seshan**: And so writing as thinking there is really prized, and that's where I did the majority of that writing work.
[55:44] **Tara Seshan**: At OpenAI, I think I still write as thinking all the time.
[55:51] **Tara Seshan**: But the shareable artifact here is not really a long doc or a proof of work in that way, partially because times have changed and a long doc is not a signal that you thought through something.
[56:07] **Tara Seshan**: Because you could easily produce a long doc that indicates that you haven't.
[56:13] **Tara Seshan**: Maybe one of the biggest changes I've experienced personally in my day-to-day, which has been a big, maybe jarring change, is I used to think in a document and then do some translation of that into a presentational artifact, and that would be my indication that I thought through a problem and this is what we're going to do and the team moves in that direction.
[56:32] **Tara Seshan**: And now I am way more on mocks not docs, or prototypes not docs.
[56:37] **Tara Seshan**: And if I have something that people can try and interact with, or even better, I have results where we tried this, we ran an AB, here's the results, this is why I think we should go in this direction, that is a way better communication tool than the doc itself.
[56:52] **Tara Seshan**: And so I still write hundreds of docs all the time, but I do it for me and I no longer do it for other people really.
[57:01] **Tara Seshan**: That no longer is the best way to talk and communicate.
[57:04] **Tara Seshan**: That is probably the biggest change I've experienced personally in this era versus the previous era.
[57:12] **Lenny Rachitsky**: It is so interesting.
[57:12] **Lenny Rachitsky**: I really liked your tip of getting tons of feedback on a doc.
[57:16] **Lenny Rachitsky**: It sounds obvious, but you can get to an iconic doc/brief by just cheating almost and getting lots of feedback on it as you're iterating it to make it stronger and stronger stronger versus, cool, here it is first time and it's rarely going to be amazing.
[57:29] **Tara Seshan**: I previously had a manager who told me that the right thing to always do is write a doc to 70% completion and then take it to the people that you need buy-in from and get it from 70% to 100%.
[57:40] **Tara Seshan**: And that still is a thing that I do all the time.
[57:45] **Tara Seshan**: Because very few great people want to interact with a perfectly polished finished idea.
[57:50] **Tara Seshan**: A perfectly polished idea, their new ideas just bounce off of it versus something that has more crags and more rough edges that they too can polish with you together.
[58:00] **Tara Seshan**: And I think that bringing people into the process that way where a doc is an underlying artifact for that is one of the best ways to collaborate that I found.
[58:08] **Lenny Rachitsky**: How do you think about AI brain rot and starting to over rely on AI that's just a challenge everybody's going to have?
[58:16] **Lenny Rachitsky**: Why not use this magic to help look at something and then we start to lose our ability to write, read long documents?
[58:24] **Lenny Rachitsky**: Is there anything you do that you are trying to avoid that?
[58:28] **Tara Seshan**: Yeah, I think this writing as thinking discipline is one of the main pieces that I employ in my day-to-day to make sure I'm not overly atrophying my thinking abilities.
[58:39] **Tara Seshan**: I think I will, again, outsource all writing as reporting as much as possible to the model.
[58:44] **Tara Seshan**: But writing as thinking I have to do myself.
[58:47] **Tara Seshan**: I have this personal belief that, if I'm going to make someone read my document, I have to at least write it first that number of times.
[58:58] **Tara Seshan**: Or I think about this in meetings too, that if I'm going to call a meeting with a set of people, I need to have prepped the collective amount of time that people are going to spend in that meeting before the meeting.
[59:08] **Tara Seshan**: And so when it comes to keeping my thinking sharp, I do that writing for the document myself first and make sure I've invested the collective amount of time I expect people to read it at least in writing it and producing it.
[59:21] **Tara Seshan**: And I don't really rely on the model either for polishing my prose, which I don't think it really does, or especially not in generating the first version.
[59:32] **Tara Seshan**: But I do, of course, have the model help me a lot when it's summarization or translation of content from one format to the other all the time.
[59:42] **Lenny Rachitsky**: So what I'm hearing is write the idea, the brief, the plan yourself as a human, write it yourself, don't start with AI, and even don't use it to improve on the writing, just keep that all human.
[59:56] **Tara Seshan**: Yeah.
[59:57] **Tara Seshan**: At least for me, I start myself and I end myself.
[01:00:01] **Tara Seshan**: I might use AI in the middle to research specific elements or drop in some data or go pull some data or help me with-
[01:00:08] **Lenny Rachitsky**: Or push back on some ideas.
[01:00:09] **Tara Seshan**: Yeah, push back on some ideas. But start yourself and yourself with a piece of-
[01:00:09] **Lenny Rachitsky**: Awesome.
[01:00:13] **Tara Seshan**: ... writing and that doesn't deteriorate your thinking.
[01:00:16] **Lenny Rachitsky**: Okay.
[01:00:16] **Lenny Rachitsky**: One last question.
[01:00:18] **Lenny Rachitsky**: I want to ask about Sutter Hill.
[01:00:19] **Lenny Rachitsky**: You had this very unusual career step.
[01:00:21] **Lenny Rachitsky**: Your PMPM, founder person, and then just like, okay, EIR at Sutter Hill Ventures, which is a iconic VC.
[01:00:30] **Lenny Rachitsky**: People can look it up.
[01:00:31] **Lenny Rachitsky**: A lot of amazing companies came out of Sutter Hill.
[01:00:33] **Lenny Rachitsky**: It has a very unique way of approaching founding where basically they incubate companies, Snowflake as an example.
[01:00:41] **Lenny Rachitsky**: What was that about?
[01:00:43] **Lenny Rachitsky**: What'd you learn from that experience?
[01:00:45] **Tara Seshan**: Sutter Hill is an iconic firm and is intentionally a very illegible firm.
[01:00:50] **Tara Seshan**: If you go to the Sutter Hill website, you will see nothing on the website.
[01:00:53] **Tara Seshan**: It is a firm that doesn't operate loudly.
[01:00:56] **Tara Seshan**: It tries to operate as under the radar as possible, as modestly as possible, yet is somehow responsible for some of the most iconic successes that Silicon Valley has seen.
[01:01:07] **Tara Seshan**: And they have this very unusual incubation model, which Mike Speiser, who is one of the amazing partners there, started and has rolled out success after success.
[01:01:20] **Tara Seshan**: I think the thing that was most iconic to me about Sutter Hill is that people look at finding product market fit as a dark art or building a tens of billion dollar company as a dark art, like, "Oh, it's luck.
[01:01:31] **Tara Seshan**: Oh, it's chance.
[01:01:32] **Tara Seshan**: Oh, it's all these things that must come together."
[01:01:35] **Tara Seshan**: Yet Mike Speiser has done it multiple times.
[01:01:39] **Tara Seshan**: And so there's clearly a way to do it.
[01:01:42] **Tara Seshan**: There's clearly a roadmap for making that possible.
[01:01:44] **Tara Seshan**: There is a set of things one can do to get this repeatably.
[01:01:47] **Tara Seshan**: It's not just luck.
[01:01:49] **Tara Seshan**: It's not just a dark art.
[01:01:51] **Tara Seshan**: There is a playbook, as it were, and that playbook lives inside of the firm Sutter Hill.
[01:01:57] **Tara Seshan**: And they have figured out how to be right a lot in terms of calling shots and making bets.
[01:02:03] **Tara Seshan**: And they've learned how to be right a lot in terms of the daily compounding things that one does to create a successful company, whether that's how you set up your enterprise sales team, how you position your product, how you build the initial founding team.
[01:02:19] **Tara Seshan**: The recruiting at Sutter Hill is an unparalleled, excellent thing.
[01:02:23] **Tara Seshan**: They have a secret tool called Redical where they have a map of everyone that they've interacted with and the 10 best people that those people have interacted with that helps them be so, so effective at this.
[01:02:36] **Tara Seshan**: So I went to Sutter Hill because in some way my career has been about how do I try to find product market fit as many times as possible, whether that was as a founder or in starting new products at Stripe or in joining a startup like Watershed.
[01:02:50] **Tara Seshan**: And so Sutter Hill is the place where they've figured out how to find product market fit on B2B products, and I wanted to learn what I could from them.
[01:02:57] **Lenny Rachitsky**: What'd you learn?
[01:02:57] **Lenny Rachitsky**: What's one thing you took away from that experience other than they know how to do it?
[01:03:01] **Tara Seshan**: They definitely know how to do it.
[01:03:02] **Tara Seshan**: I think one thing that was very surprising to me that I learned there is that product market fit is, sure, important, but actually I really underrated product marketing fit.
[01:03:12] **Tara Seshan**: The idea that the way you talk about the product and the way you market it can proceed actually even building the product.
[01:03:19] **Tara Seshan**: It should probably come from some sort of bringing together of understanding the technology deeply and then understanding the enterprise sales process.
[01:03:28] **Tara Seshan**: And then that product marketing fit, that narrative, that positioning, is actually even before you build a product experience the right thing to test.
[01:03:35] **Tara Seshan**: So you should go pitch a hundred people, figure out how to refine that pitch as much as possible, get the marketing narrative of why this thing is transformative right.
[01:03:44] **Tara Seshan**: And then and only then go commit the, okay, this is exactly the product shape.
[01:03:49] **Tara Seshan**: And Mike Speiser is unbeatable at this art.
[01:03:53] **Tara Seshan**: Previously, I'd always underrated PMM work.
[01:03:56] **Tara Seshan**: I was like, "It's whatever.
[01:03:57] **Tara Seshan**: It's the glue between these functions.
[01:03:59] **Tara Seshan**: It's fine."
[01:04:00] **Tara Seshan**: And then I realized how transformative that work done excellently is to a company's outcome, and in fact can be the element that makes a company successful.
[01:04:12] **Lenny Rachitsky**: Amazing.
[01:04:12] **Lenny Rachitsky**: I so agree with that.
[01:04:13] **Lenny Rachitsky**: Positioning, we talk a lot about that on this podcast.
[01:04:16] **Lenny Rachitsky**: Okay.
[01:04:17] **Lenny Rachitsky**: I'm going to show you what sites got created real quick.
[01:04:20] **Lenny Rachitsky**: It was running while we were talking.
[01:04:21] **Lenny Rachitsky**: Check this out.
[01:04:21] **Lenny Rachitsky**: Look at this.
[01:04:22] **Tara Seshan**: Oh man.
[01:04:24] **Lenny Rachitsky**: I was like, "Make it more awesome," and it made it more awesome.
[01:04:26] **Tara Seshan**: That's-
[01:04:27] **Lenny Rachitsky**: Multi-product.
[01:04:29] **Lenny Rachitsky**: Beautiful.
[01:04:30] **Lenny Rachitsky**: Look at this.
[01:04:30] **Lenny Rachitsky**: This is like a legit design.
[01:04:32] **Tara Seshan**: Wow.
[01:04:32] **Lenny Rachitsky**: Look at it.
[01:04:33] **Lenny Rachitsky**: You got quotes, big conviction, small teams.
[01:04:35] **Tara Seshan**: It's true.
[01:04:36] **Lenny Rachitsky**: [inaudible 01:04:36] the buyer.
[01:04:37] **Lenny Rachitsky**: How do you feel about this being your website, your new website?
[01:04:40] **Tara Seshan**: I do think that the picture of me at maybe 19 years old at the top is really funny.
[01:04:45] **Tara Seshan**: But yeah, otherwise I love the site.
[01:04:48] **Lenny Rachitsky**: Okay, good job.
[01:04:49] **Tara Seshan**: It's looking good.
[01:04:51] **Lenny Rachitsky**: Good job Sites.
[01:04:52] **Tara Seshan**: I think that was my badge photo from Stripe.
[01:04:54] **Lenny Rachitsky**: Oh wow.
[01:04:54] **Lenny Rachitsky**: Amazing.
[01:04:55] **Lenny Rachitsky**: I already unshared it, but I love that it built the whole little thing around your head.
[01:05:00] **Lenny Rachitsky**: So cute.
[01:05:02] **Lenny Rachitsky**: Tara, is there anything else that you wanted to share?
[01:05:04] **Lenny Rachitsky**: Anything else you want to touch on before we get to our very exciting lightning round?
[01:05:08] **Tara Seshan**: Yeah.
[01:05:09] **Tara Seshan**: One thing that we've been thinking about a lot in product building, especially with ChatGPT Work in this new era, is how knowledge work and coding are actually fundamentally different.
[01:05:17] **Tara Seshan**: And one of the surprising things we learned as a part of that is that coding is so output oriented that when you ask it to do a coding task, you can verify whether it did the task correctly or well via tests.
[01:05:31] **Tara Seshan**: You can try it out and see if it works.
[01:05:33] **Tara Seshan**: There is a way to validate it based on the output.
[01:05:37] **Tara Seshan**: But knowledge work is different in that I can't simply look at the deck in the end and see the numbers, like, oh, it's like 90% success or whatever in the deck and actually believe that.
[01:05:47] **Tara Seshan**: I really need to think about the process and the inputs and the reasoning and how it went along the way.
[01:05:53] **Tara Seshan**: And so in terms of how that looks in the product, a lot of work that we have done and have to continue to do is continue to adapt the product to knowledge work, which means way more focus on making ChatGPT your collaborator, allowing you to see all the in-progress work, see its citations and inputs, help you go on the journey with the model to get to that end output, such that you know in the end that, oh wait, this thing is right, this thing is good, this thing is useful.
[01:06:23] **Tara Seshan**: And that shows up certainly in the UX of the product quite a bit, but also should show up in things like the reasoning in the chain of thought.
[01:06:30] **Tara Seshan**: Should you see more citations along the way, for example, of how it got to that end state in that data?
[01:06:36] **Tara Seshan**: Is the surface of a thread which is so suited to coding the right place for you to see all of that for knowledge work as well?
[01:06:43] **Tara Seshan**: There's so many big important product questions.
[01:06:46] **Tara Seshan**: And so as we think of maybe bringing in human collaborators into your work, we also need to think about how we can make the model more of a collaborator with you as you get things done together.
[01:06:58] **Lenny Rachitsky**: That is such a good point.
[01:06:59] **Lenny Rachitsky**: I'm imagining an exec meeting where you're trying to pitch the exec on, here's what the plan is, here's what I think we should be doing.
[01:07:08] **Lenny Rachitsky**: So much of that is helping them see here's the work I did to get there, here's all the steps.
[01:07:15] **Lenny Rachitsky**: And so it makes sense that you need the AI to show you that same sort of work.
[01:07:21] **Lenny Rachitsky**: That it did the proof of work essentially versus engineering where like, "Okay, I don't need to know all of the little architectural decisions you made, just what does it look like?
[01:07:28] **Lenny Rachitsky**: Is it passing all the tests that we have?"
[01:07:30] **Lenny Rachitsky**: So that is a really good point, just how different those two models are.
[01:07:34] **Lenny Rachitsky**: And also there's the context.
[01:07:36] **Lenny Rachitsky**: Does it have the context it needs to do the thing that you want it to do?
[01:07:39] **Lenny Rachitsky**: Does it know?
[01:07:40] **Lenny Rachitsky**: Can it see your email?
[01:07:41] **Lenny Rachitsky**: Can it see all your notion docs?
[01:07:43] **Lenny Rachitsky**: Such a good point.
[01:07:44] **Lenny Rachitsky**: So I see the challenge in your job to make all this work is one product.
[01:07:48] **Lenny Rachitsky**: Tricky, tricky.
[01:07:51] **Lenny Rachitsky**: Amazing.
[01:07:51] **Lenny Rachitsky**: Anything else before we get to our very exciting lightning round?
[01:07:54] **Tara Seshan**: Yeah, let's jump into it.
[01:07:56] **Lenny Rachitsky**: With that, we've reached our very exciting lightning round.
[01:07:58] **Lenny Rachitsky**: I've got five questions for you.
[01:07:59] **Lenny Rachitsky**: Are you ready?
[01:08:00] **Tara Seshan**: Yes.
[01:08:02] **Lenny Rachitsky**: What are two or three books that you find yourself recommending most to other people?
[01:08:06] **Tara Seshan**: One book I really recommend to people is Barbarian Days by William Finnegan.
[01:08:10] **Tara Seshan**: I don't know if you've read it.
[01:08:11] **Tara Seshan**: It's about a life of a man who is a New Yorker reporter, but how he fell in love with surfing as his passion.
[01:08:18] **Tara Seshan**: The thing I took away from the book is that one can be deeply passionate and dedicated and have something be your life purpose without you being good at it.
[01:08:26] **Tara Seshan**: And it is about the art of falling in love with surfing and his striving for excellence and perfection whilst knowing that he will never reach it.
[01:08:35] **Tara Seshan**: It is such a compelling and transformative story for how I think one should continue to live our lives.
[01:08:44] **Tara Seshan**: I really, really love that book.
[01:08:49] **Tara Seshan**: Another book that I might recommend as a book that people should read, I really love Anna Karenina.
[01:08:58] **Tara Seshan**: I've been rereading the classics lately, and I love Anna Karenina because it's a book of layers.
[01:09:04] **Tara Seshan**: And I think that a huge part of what we're going to have to do in this new era is transform ourselves or take ourselves on a journey to do different things than what we were used to.
[01:09:14] **Tara Seshan**: And when I think about that book, I think about when I was 13 and I read it, I understood basically the plot.
[01:09:22] **Tara Seshan**: When I read it at 17, I understood the European history dynamics and the class warfare.
[01:09:27] **Tara Seshan**: And then when I read it at 30, I was like, oh, this is a story about a woman and humans.
[01:09:32] **Tara Seshan**: And it just reminds me of growth and that it is possible to look at the same thing through multiple different lenses as you continue to grow, which I think is the challenge that's ahead for all of us as we consider our careers as well.
[01:09:47] **Lenny Rachitsky**: It's interesting on both these, I could connect to AI in the time we're living in now too.
[01:09:52] **Lenny Rachitsky**: I also recently read Anna Karenina.
[01:09:54] **Tara Seshan**: What did you think?
[01:09:55] **Lenny Rachitsky**: Earlier this year.
[01:09:56] **Lenny Rachitsky**: Amazing.
[01:09:56] **Lenny Rachitsky**: I've never read it before.
[01:09:57] **Lenny Rachitsky**: I saw it on a book list of here's what the smartest people in the world have read and it's a whole list of books and that was one that I hadn't read.
[01:10:03] **Lenny Rachitsky**: So I'm like, "I got to read that."
[01:10:05] **Lenny Rachitsky**: Yeah, it was amazing.
[01:10:07] **Lenny Rachitsky**: Someone gave away the ending, which made it less surprising.
[01:10:10] **Lenny Rachitsky**: I don't want to give anything away.
[01:10:11] **Lenny Rachitsky**: No spoilers.
[01:10:13] **Lenny Rachitsky**: And I also felt like it was very long.
[01:10:15] **Lenny Rachitsky**: But now I'm reading The Power Broker, which has set the new precedent for a long... Been reading it for half my life at this point.
[01:10:23] **Tara Seshan**: I love The Power Broker.
[01:10:24] **Tara Seshan**: Another  thing  that  I  highly  recommend  to  people  is  if  anyone  follows  the  Substack,  like  Simon  Hazel's Substack  where  he  does  a  slow  read  of  important  books.
[01:10:33] **Tara Seshan**: So he did One of War and Peace and he's doing one of Wolf Hall, I think, or he did one of Wolf Hall, which is the Hilary Mantel book, take it chapter by chapter.
[01:10:41] **Tara Seshan**: That's the only way to read something like The Power Broker or War and Peace or even Anna Karenina.
[01:10:46] **Tara Seshan**: It's chapter by chapter.
[01:10:47] **Lenny Rachitsky**: Speaking of that, there's someone, I forget who, told me this, there's a 99% Invisible book club breakdown of The Power Broker where it's 13 episodes an hour or two each, and they go through a couple chapters of the book one at a time and talk about it.
[01:11:03] **Lenny Rachitsky**: And they have special guests like Pete Buttigieg and AOC and folks that lived in that area and they talk about the story, and it's so fun to read and listen to their analysis of it.
[01:11:13] **Lenny Rachitsky**: And then they have Robert Caro come on a couple times, I guess.
[01:11:16] **Tara Seshan**: Whoa, that's amazing.
[01:11:18] **Lenny Rachitsky**: Yeah.
[01:11:18] **Lenny Rachitsky**: Yeah.
[01:11:19] **Lenny Rachitsky**: Hot tip.
[01:11:19] **Lenny Rachitsky**: Okay, we'll keep going with our very lightning round.
[01:11:22] **Lenny Rachitsky**: Favorite recent movie or TV show you've really enjoyed, if you've had time to watch anything.
[01:11:27] **Tara Seshan**: Of course I watched The Odyssey.
[01:11:28] **Tara Seshan**: I found it to be an incredible, incredible film.
[01:11:32] **Tara Seshan**: It is about AI, or my hot take is that it's about AI or Christopher Nolan's view on how AI transforms society, which I loved and I highly recommend watching The Odyssey.
[01:11:43] **Tara Seshan**: He's just an incredible director and has bridged artistry and commercial success in a way that I think no other modern director has done.
[01:11:54] **Tara Seshan**: I also recently watched the film Rashomon, which is the Akira Kurosawa film that for the first time did that technique of telling a story through multiple people's perspectives where you never know what was true in the end.
[01:12:08] **Tara Seshan**: That technique in film was pioneered by Kurosawa.
[01:12:11] **Tara Seshan**: And it reminds me what one can do under constraints.
[01:12:15] **Tara Seshan**: That film was made in the 50s.
[01:12:17] **Tara Seshan**: It was black and white.
[01:12:19] **Tara Seshan**: You know there's a guy holding the camera and yet it is so perfect and it is such a tasteful, innovative, amazing example of creativity.
[01:12:31] **Tara Seshan**: And what I'm reminded of watching that film is I have a hundred times the power and tools that he had making that film in my iPhone.
[01:12:39] **Tara Seshan**: And what's my excuse for not elevating my ambitions and making better stuff?
[01:12:42] **Lenny Rachitsky**: All comes back ambition.
[01:12:45] **Lenny Rachitsky**: On the Odyssey, I'm still trying to get tickets.
[01:12:47] **Lenny Rachitsky**: It's so hard.
[01:12:48] **Lenny Rachitsky**: I slept on it and now it's impossible for a month, there's no seats anywhere.
[01:12:53] **Tara Seshan**: Kevin Klock got us tickets at 10:00 PM at the Metreon earlier this week.
[01:12:57] **Tara Seshan**: It was so good.
[01:12:58] **Lenny Rachitsky**: Next time call me.
[01:12:59] **Lenny Rachitsky**: I'm in whenever you see it.
[01:13:02] **Tara Seshan**: For sure.
[01:13:02] **Lenny Rachitsky**: Oh, man, I have bots running on it.
[01:13:03] **Lenny Rachitsky**: I have a person working on it.
[01:13:05] **Lenny Rachitsky**: I have a friend.
[01:13:06] **Lenny Rachitsky**: We're all trying to find a seat.
[01:13:07] **Tara Seshan**: It's amazing.
[01:13:08] **Tara Seshan**: You're going to love it and I can't wait to hear what you think after you see it.
[01:13:10] **Tara Seshan**: If you agree with me that it is about AI and the collapse of morality.
[01:13:15] **Lenny Rachitsky**: Okay.
[01:13:15] **Lenny Rachitsky**: No spoilers.
[01:13:16] **Lenny Rachitsky**: Hopefully by the time this comes out, I have seen it, but if not, if anyone has hookups, please tell me.
[01:13:21] **Lenny Rachitsky**: And I'm trying to do the IMAX full power Metreon sort of thing.
[01:13:24] **Lenny Rachitsky**: Yeah.
[01:13:25] **Lenny Rachitsky**: Okay, next question.
[01:13:27] **Lenny Rachitsky**: Favorite or interesting AI product that you've recently discovered?
[01:13:31] **Lenny Rachitsky**: Ideally not OpenAI product, but you can also go there if you want.
[01:13:37] **Tara Seshan**: Ooh, I mean, of course my favorite AI product is ChatGPT and using cool Sites and Visualize stuff in Codex, which is amazing.
[01:13:45] **Tara Seshan**: But outside of OpenAI products, my favorite AI products are products that my friends make for me.
[01:13:52] **Tara Seshan**: Because now, actually people can do that.
[01:13:53] **Tara Seshan**: I think that's so cool.
[01:13:54] **Tara Seshan**: I'm such a huge fan of the cozy software movement where you make software tools for five of your friends and you guys use it together.
[01:14:01] **Tara Seshan**: And so I have a friend named Sebastian who made a really cool AI app that turns anything into a podcast and puts it in a little podcast app for you.
[01:14:13] **Tara Seshan**: And he also made a really great private social network for our friends, and it's called GATS.
[01:14:19] **Tara Seshan**: It is exactly what I think the future should be, which is people should make software that exactly meets their and their friends' needs.
[01:14:26] **Lenny Rachitsky**: What does GATS stand for?
[01:14:27] **Lenny Rachitsky**: Is that some inside joke?
[01:14:28] **Tara Seshan**: It is not, or at least if it is an inside joke, I don't know it.
[01:14:34] **Tara Seshan**: It's like private Twitter maybe for a small group of friends, and I learned the most interesting things on that product.
[01:14:42] **Lenny Rachitsky**: It's like a WhatsApp in that, like it's [inaudible 01:14:43].
[01:14:43] **Tara Seshan**: Yes, exactly, exactly.
[01:14:46] **Lenny Rachitsky**: The podcast app is interesting, but I feel like the version that I would love is it's actually podcasts in your feed of podcasts and then just new episodes get added of things you want to read or whatever-
[01:14:56] **Tara Seshan**: Yeah, that's what it does.
[01:14:56] **Lenny Rachitsky**: ... versus a separate app.
[01:14:57] **Lenny Rachitsky**: Oh, okay.
[01:14:58] **Tara Seshan**: It drops it in your Apple Podcast feeder or wherever you watch.
[01:14:58] **Lenny Rachitsky**: Oh, amazing. I want this.
[01:14:58] **Tara Seshan**: It's great.
[01:15:04] **Lenny Rachitsky**: Really, help me subscribe to this app.
[01:15:05] **Tara Seshan**: For sure.
[01:15:07] **Lenny Rachitsky**: Okay, amazing.
[01:15:07] **Lenny Rachitsky**: Okay, two more questions.
[01:15:08] **Lenny Rachitsky**: Do you have a favorite life motto that you find yourself coming back to often in work or in life?
[01:15:13] **Tara Seshan**: Ooh, my life motto that I come back to all the time in work is actually Toni Morrison's three takes on work.
[01:15:18] **Tara Seshan**: Let me pull it up really quickly.
[01:15:20] **Lenny Rachitsky**: Amazing.
[01:15:22] **Tara Seshan**: Okay.
[01:15:22] **Tara Seshan**: It's four things.
[01:15:23] **Tara Seshan**: It's from her essay, The Work You Do, The Person You Are.
[01:15:27] **Tara Seshan**: The first one is whatever the work is, do it well, not for the boss, but for yourself.
[01:15:33] **Tara Seshan**: The second is you make the job, it doesn't make you.
[01:15:37] **Tara Seshan**: The third is your real life is with your family.
[01:15:40] **Tara Seshan**: And the fourth is, you are not the work you do, you are the person that you are.
[01:15:45] **Lenny Rachitsky**: I got tingles. Wow. So good. And I think that's what you have pinned to your Twitter profile because I remember seeing that. So cool. Okay. Maybe we'll show that on screen as you're talking about that. I love that. That's a great way to remember something. Just stick it to the top of your Twitter, because every time I go to Twitter. "Oh, there it is again." Okay, final question. You were a Thiel Fellow back in the day. Thiel Fellow? Thiel or Thiel?
[01:15:45] **Tara Seshan**: Thiel.
[01:16:11] **Lenny Rachitsky**: Thiel.
[01:16:11] **Lenny Rachitsky**: Thiel, yeah.
[01:16:12] **Lenny Rachitsky**: What an alumni group.
[01:16:13] **Lenny Rachitsky**: Holy moly.
[01:16:14] **Lenny Rachitsky**: It's such a great idea and program.
[01:16:18] **Lenny Rachitsky**: Any story from that time that might be fun to share?
[01:16:21] **Lenny Rachitsky**: Something that's like, "Oh wow, that was crazy."
[01:16:23] **Lenny Rachitsky**: I don't know.
[01:16:24] **Lenny Rachitsky**: Any other Thiel Fellow that you're proud of?
[01:16:26] **Lenny Rachitsky**: What was the interview like?
[01:16:28] **Lenny Rachitsky**: I don't know, anything along those lines.
[01:16:30] **Tara Seshan**: Yeah, the Thiel Fellowship was an inflection point in my life.
[01:16:35] **Tara Seshan**: I wouldn't be where I am without it.
[01:16:37] **Tara Seshan**: Maybe to the point of there are key moments where you can tell people to elevate their ambitions and they do, and that changes them.
[01:16:43] **Tara Seshan**: That was a moment where someone came to me and elevated my ambitions and said, "No, you can do this.
[01:16:47] **Tara Seshan**: You don't have to take the path that you were on."
[01:16:49] **Tara Seshan**: And truly, I'm eternally grateful for them being able to do that.
[01:16:54] **Tara Seshan**: One of the Thiel Fellows that I get to work with all the time now is Ari Weinstein, who founded a company called Sky that was acquired by OpenAI.
[01:17:03] **Tara Seshan**: And prior to this, he founded and worked at Apple for a while because they acquired his previous company.
[01:17:10] **Tara Seshan**: Ari is just one of the most creative thinkers I've ever seen and is truly the expert on, what are all the cool things you can do on a Mac?
[01:17:21] **Tara Seshan**: And so Ari leads a lot of our computer use stuff at OpenAI, and he's shipped a whole bunch of great things for computer use.
[01:17:29] **Tara Seshan**: But yeah, his creativity and his joy in what he does and his love of his craft really inspires me.
[01:17:35] **Tara Seshan**: And Ari's a cool guy.
[01:17:37] **Tara Seshan**: But I'm trying to think what is a good story from that time that feels [inaudible 01:17:45].
[01:17:44] **Lenny Rachitsky**: As you think about it, I'll explain the Thiel Fellowship for people that don't know this, and correct me if I'm wrong.
[01:17:49] **Lenny Rachitsky**: Basically, Peter Thiel's like, "Hey, people shouldn't go to college.
[01:17:53] **Lenny Rachitsky**: Instead, they should just try building something that they want."
[01:17:57] **Lenny Rachitsky**: And you get $100,000 to not do college and instead just go follow your ambition.
[01:18:03] **Lenny Rachitsky**: Is that roughly correct?
[01:18:04] **Tara Seshan**: Yeah, that is exactly right.
[01:18:05] **Lenny Rachitsky**: Cool.
[01:18:06] **Tara Seshan**: And you're with 19 other people at the time.
[01:18:08] **Tara Seshan**: It's like 20 people every year because it's 20 under 20.
[01:18:12] **Lenny Rachitsky**: How many years did it go on for? Is it still going?
[01:18:13] **Tara Seshan**: I think it's still going, but I think it was constrained at the 20 number for the first four or five years or something like that.
[01:18:22] **Tara Seshan**: Yeah, I think a really crazy thing that happened my year is that I was the second every year of the fellowship.
[01:18:27] **Tara Seshan**: They decided to make it all a documentary on CNBC, and so my pitch for the fellowship, getting up on stage and presenting the idea I was going to do, all of that is unfortunately live on YouTube.
[01:18:40] **Tara Seshan**: So if you really want to see me as a 19-year-old doing something embarrassing, it's there.
[01:18:46] **Tara Seshan**: Of course, one of the most amazing and successful people who came out of that batch of the fellowship is Dylan Field, who is not only a incredible talent, but also a very kind person.
[01:18:58] **Tara Seshan**: And yeah, feel very lucky to be able to work with those folks.
[01:19:03] **Lenny Rachitsky**: Amazing.
[01:19:03] **Lenny Rachitsky**: Yeah.
[01:19:03] **Lenny Rachitsky**: It's interesting that Dylan's the guy.
[01:19:05] **Lenny Rachitsky**: I think everyone thinks of when they think of Thiel Fellows.
[01:19:09] **Tara Seshan**: Yeah.
[01:19:09] **Tara Seshan**: Yeah.
[01:19:10] **Lenny Rachitsky**: What a brand.
[01:19:10] **Lenny Rachitsky**: Okay, Tara, this was incredible.
[01:19:13] **Lenny Rachitsky**: Is there anything you want to plug, anything you want to point people to, and how can listeners be useful to you?
[01:19:18] **Tara Seshan**: Anything I want to plug and point people to, maybe they should use the ChatGPT desktop app.
[01:19:22] **Tara Seshan**: They should use ChatGPT in the web and try Work.
[01:19:25] **Tara Seshan**: It's unfortunately a little toggle.
[01:19:27] **Tara Seshan**: They can toggle over to it and try out Work.
[01:19:30] **Tara Seshan**: Ask it to do some cool thing.
[01:19:32] **Tara Seshan**: Ask it to build a site about you maybe to start, or ask it to make a little visualize a block of your ChatGPT usage.
[01:19:39] **Tara Seshan**: It's a really cool way to start experiencing the power of this stuff very intimately, and the list of use cases they can do from that are infinite, and I'm happy with it.
[01:19:53] **Lenny Rachitsky**: Here's a better idea.
[01:19:53] **Lenny Rachitsky**: Here's a better idea.
[01:19:54] **Tara Seshan**: Yes.
[01:19:55] **Lenny Rachitsky**: Ask it to build a site to tell you what you could do with Work.
[01:19:58] **Tara Seshan**: Great.
[01:20:00] **Tara Seshan**: That will work.
[01:20:02] **Lenny Rachitsky**: Solve all the problems.
[01:20:03] **Lenny Rachitsky**: Okay.
[01:20:04] **Lenny Rachitsky**: I interrupted you.
[01:20:05] **Lenny Rachitsky**: I apologize.
[01:20:06] **Lenny Rachitsky**: What else were you going to add or say?
[01:20:08] **Tara Seshan**: Yeah, my main plug is, yeah, go download the ChatGPT app, go use it on web.
[01:20:12] **Tara Seshan**: Even more transformatively, go try it on mobile, then take a long subway ride or something like that, or a Muni ride.
[01:20:19] **Tara Seshan**: And when you pop out after having no service, the thing is done for you.
[01:20:23] **Tara Seshan**: That's the part that feels super-duper magical.
[01:20:25] **Tara Seshan**: You're not wandering around with your laptop open the entire time.
[01:20:27] **Tara Seshan**: You've finally got these things running in the cloud doing real work.
[01:20:31] **Lenny Rachitsky**: Yeah, that last piece I was going to bring up, but I think a really underappreciated element of the product today on mobile.
[01:20:39] **Lenny Rachitsky**: And that's just a mobile only feature, the cloud piece, is it?
[01:20:43] **Tara Seshan**: No, it's everywhere.
[01:20:43] **Lenny Rachitsky**: It's everywhere.
[01:20:44] **Lenny Rachitsky**: Okay, so, amazing.
[01:20:46] **Lenny Rachitsky**: So on your mobile app, you can go to ChatGPT, toggle Work, ask it to do some work, and you don't need to actually have the...
[01:20:52] **Lenny Rachitsky**: It's not running locally, it's running in the cloud.
[01:20:54] **Lenny Rachitsky**: It'll keep doing work until it's done and then you could chat to it.
[01:20:57] **Lenny Rachitsky**: So it feels really simple, but that's a massively powerful thing.
[01:21:03] **Lenny Rachitsky**: Okay.
[01:21:05] **Lenny Rachitsky**: Anything else, Tara, before we let you go?
[01:21:07] **Tara Seshan**: No, that's it.
[01:21:08] **Lenny Rachitsky**: Okay.
[01:21:08] **Tara Seshan**: Thanks, Lenny.
[01:21:09] **Lenny Rachitsky**: Tara, this was awesome.
[01:21:09] **Lenny Rachitsky**: Thank you so much for doing this.
[01:21:11] **Tara Seshan**: Such a pleasure.
[01:21:12] **Lenny Rachitsky**: What a journey since the fellowship back in the day.
[01:21:14] **Lenny Rachitsky**: I'll talk about that more in the intro.
[01:21:16] **Tara Seshan**: Yeah.
[01:21:17] **Lenny Rachitsky**: All right.
[01:21:17] **Lenny Rachitsky**: Well, thanks for being here.
[01:21:18] **Tara Seshan**: Thank you.
[01:21:20] **Lenny Rachitsky**: Bye everyone.
[01:21:21] **Lenny Rachitsky**: Thank you so much for listening.
[01:21:23] **Lenny Rachitsky**: If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app.
[01:21:29] **Lenny Rachitsky**: Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast.
[01:21:35] **Lenny Rachitsky**: You can find all past episodes or learn more about the show at lennyspodcast.com.
[01:21:41] **Lenny Rachitsky**: See you in the next episode.

<!-- End of captured transcript -->
