---
type: raw
title: "Talking Postgres Ep 42 — How AI is changing software development with Simon Willison"
source: "https://share.transistor.fm/s/fe88354c/transcript"
author:
  - "Simon Willison"
  - "Claire Giordano (host)"
  - "Aaron Wislang (producer)"
published: "2026-08-20"
created: "2026-08-20"
description: "Simon Willison (Datasette/Django 共同创建者) 在 Talking Postgres Ep 42 阐述 AI 时代软件工程变化：'Could I explain this to somebody else?' 是判断 AI 生成代码可上线的金标准；red-green TDD 让 agent 跑每行代码；'Features are cheap, that doesn't mean you should build them all'；agent 时代工程管理技能比编码技能更重要；skill atrophy 是选择；系统设计未跟上 agent 产出量。"
tags:
  - "clippings"
  - "agentic-engineering"
  - "simon-willison"
  - "podcast"
  - "verification"
  - "evaluation"
---

# Talking Postgres Ep 42 — How AI is changing software development with Simon Willison

> Source: https://share.transistor.fm/s/fe88354c/transcript
> Guest: Simon Willison (creator of Datasette, co-creator of Django)
> Host: Claire Giordano (Head of open source community efforts for Postgres at Microsoft)
> Producer: Aaron Wislang
> Published: 2026-08-20

---

In this episode, we covered:
**

[00:00](https://share.transistor.fm/s/fe88354c/transcript#t=0m0s)Intro & music

[04:00](https://share.transistor.fm/s/fe88354c/transcript#t=4m0s)A week of work before breakfast

[09:12](https://share.transistor.fm/s/fe88354c/transcript#t=9m12s)Red-green TDD makes agents exercise every line

[14:42](https://share.transistor.fm/s/fe88354c/transcript#t=14m42s)A million lines mean nothing if you don’t understand it

[18:28](https://share.transistor.fm/s/fe88354c/transcript#t=18m28s)Finding low-hanging fruit among open PRs & issues

[22:07](https://share.transistor.fm/s/fe88354c/transcript#t=22m7s)Getting work done while walking the dog

[23:01](https://share.transistor.fm/s/fe88354c/transcript#t=23m1s)Gold standard: “Could I explain this to somebody else?”

[28:27](https://share.transistor.fm/s/fe88354c/transcript#t=28m27s)Slop proxies add no value at all

[30:49](https://share.transistor.fm/s/fe88354c/transcript#t=30m49s)Aggressive nitpicking reviews

[35:01](https://share.transistor.fm/s/fe88354c/transcript#t=35m1s)Everything in software engineering is about trade-offs

[41:16](https://share.transistor.fm/s/fe88354c/transcript#t=41m16s)Racoon heist game is only fun for 1 minute 15 seconds

[43:46](https://share.transistor.fm/s/fe88354c/transcript#t=43m46s)New Year’s resolution to be more ambitious

[48:11](https://share.transistor.fm/s/fe88354c/transcript#t=48m11s)You have to learn to throw things away

[51:57](https://share.transistor.fm/s/fe88354c/transcript#t=51m57s)Features are cheap. That doesn’t mean you should build them all

[1:00:45](https://share.transistor.fm/s/fe88354c/transcript#t=1h0m45s)Engineering management skills are so useful

[1:04:44](https://share.transistor.fm/s/fe88354c/transcript#t=1h4m44s)QA specialists should be having a great time

[1:07:53](https://share.transistor.fm/s/fe88354c/transcript#t=1h7m53s)Writing is thinking, don’t outsource it

[1:08:23](https://share.transistor.fm/s/fe88354c/transcript#t=1h8m23s)Skill atrophy is a choice you make

[1:10:07](https://share.transistor.fm/s/fe88354c/transcript#t=1h10m7s)I believe in people who are motivated

[1:11:55](https://share.transistor.fm/s/fe88354c/transcript#t=1h11m55s)Systems are not set up to deal with this volume

[1:18:48](https://share.transistor.fm/s/fe88354c/transcript#t=1h18m48s)Research agents stopped being absolute garbage

[1:21:49](https://share.transistor.fm/s/fe88354c/transcript#t=1h21m49s)The whole point of the “human in the loop”

[1:26:10](https://share.transistor.fm/s/fe88354c/transcript#t=1h26m10s)Dream: I want there to be more small businesses

#### Creators and Guests

Host

Claire Giordano

Head of open source community efforts for Postgres at Microsoft. Ex-Citus Data, Amazon, Sun Microsystems, and Brown University CS. Serves on PGCA board. Prolific Postgres conference speaker. Co-creator of POSETTE: An Event for Postgres. Loves sailing in Greece.

[](https://x.com/clairegiordano)[](https://www.linkedin.com/in/claireg/)[](https://hachyderm.io/@clairegiordano)[](https://bsky.app/profile/clairegiordano.bsky.social)[](https://github.com/clairegiordano/)

Producer

Aaron Wislang

Open Source Engineering + Developer Relations at Microsoft + Azure ☁️ | Go (golang), Cloud Native, Linux 🐧 🐍 🦀 ☕ 🍷📷 🎹 | Toronto 🇨🇦🌎 | 💨😷💉 | https://aaronw.dev/hello/

[](https://x.com/as_w)[](https://www.linkedin.com/in/aaron-wislang/)[](https://mastodon.social/@asw)[](https://www.threads.net/@aaronw.dev)[](https://bsky.app/profile/aaronw.dev)[](https://github.com/asw101)[](https://aaronw.dev/hello/)

Guest

Simon Willison

Independent AI researcher, creator of datasette.io and llm.datasette.io, building open source tools for data journalism, writing about a lot of stuff at https://simonwillison.net/

[](https://x.com/simonw)[](https://www.linkedin.com/in/simonwillison/)[](https://hachyderm.io/@simon@simonwillison.net)[](https://bsky.app/profile/simonwillison.net)[](https://github.com/simonw)[](https://simonwillison.net/)

#### What is Talking Postgres with Claire Giordano?

Talking Postgres is a podcast for developers who love Postgres. Guests join Claire Giordano each month to discuss the human side of PostgreSQL, databases, and open source. With amazing guests such as Boriss Mejías, Melanie Plageman, Tom Lane, Simon Willison, Robert Haas, and Andres Freund, Talking Postgres is guaranteed to get you thinking. Recorded live on Discord by the Postgres team at Microsoft, you can subscribe to our calendar to join us live on the parallel text chat (which is quite fun!):[https://aka.ms/TalkingPostgres-cal](https://aka.ms/TalkingPostgres-cal)

CLAIRE:[00:00:05](https://share.transistor.fm/s/fe88354c/transcript#t=0h0m5s)
Welcome to Talking Postgres. It's a monthly podcast for developers who love this database. I'm your host, Claire Giordano, and in today's podcast and all the episodes, we explore the human side of Postgres databases and open source, which means why do people who work with Postgres do what they do and how did they get there? I want to say thank you to the team at Microsoft for sponsoring today's community conversation. And today's guest is Simon Willison. This is Simon's third time back on the podcast, which makes me feel really, really good that he's willing to come back. He's experienced it before and he's willing to do it again.

SIMON:[00:00:44](https://share.transistor.fm/s/fe88354c/transcript#t=0h0m44s)
It's always a great time.

CLAIRE:[00:00:46](https://share.transistor.fm/s/fe88354c/transcript#t=0h0m46s)
Thank you. Simon is an independent open source developer, and his first claim to fame, which most people have heard of, is that he was co-creator of the Django web framework. Since 2002, which is a while ago now, he's been a prolific blogger, sharing what he's learned on a daily basis, as far as I can tell, multiple posts a day in many cases. And you can find his blog at SimonWillison.net. Officially, Simon works full-time building open source tools for data journalism, creating software that is going to help somebody win a Pulitzer Prize someday, including tools like Datasette, which he created. And he also spends a lot of time these last couple of years. Exploring the cutting edge of the latest LLMs and AI tools, sharing his observations and what he's learned, which of course the rest of us are really happy about. So, welcome, Simon.

SIMON:[00:01:44](https://share.transistor.fm/s/fe88354c/transcript#t=0h1m44s)
Hey, I'm really glad to be back.

CLAIRE:[00:01:47](https://share.transistor.fm/s/fe88354c/transcript#t=0h1m47s)
So today's topic, officially, I pushed out a social media post earlier today, was titled How AI is changing software development. But I considered a couple other titles: How AI is changing how I build software, where I is you, Simon, or How AI is affecting open source projects, because I do want to talk a little bit about open source projects later in the show. So what I really want to jump into are specific stories and examples of how you are using AI to build software now, how it's changed what your day-to-day life looks like. And then also, I'm hoping you share some stories about things you've heard from friends and other people as well, because I want people listening to be able to visualize, to be able to imagine what's possible, because maybe, maybe they're not there yet in terms of their day-to-day use.

SIMON:[00:02:47](https://share.transistor.fm/s/fe88354c/transcript#t=0h2m47s)
You know what? I have the perfect story to kick us off. [Oh, good.] So one of, I've got.

CLAIRE:[00:02:52](https://share.transistor.fm/s/fe88354c/transcript#t=0h2m52s)
Does it involve a seal named No?

SIMON:[00:02:55](https://share.transistor.fm/s/fe88354c/transcript#t=0h2m55s)
Named Chonkers? It doesn't, but Chonkers is always on my mind. There was a wonderful giant Steller sea lion in San Francisco a couple of months ago called Chonkers, who is three times the size of the other sea lions and made, made quite an impression on people. Okay, so this morning, I was— one of my open source projects is a little tool called sqlite-utils. I do most of my work with SQLite. sqlite-utils is a command line tool for dumping data into a SQLite database, and a Python library as well. So a lot of my projects end up as both Python libraries and command line tools. And the neatest feature of sqlite-utils is that you can take a bunch of JSON and say, stick this in my database, and it will create the correct schema for you. It'll go, Oh, okay, this JSON has a title, which is a string, and it has an age, which is an integer in it, creates the table and inserts the data, and that all just works. And it's a one-liner in your terminal to do that. And this morning, I was thinking, you know what, I've always wanted— To have a version of that that works with Postgres and with other databases as well, like DuckDB and such like.

SIMON:[00:04:00](https://share.transistor.fm/s/fe88354c/transcript#t=0h4m0s)
So literally, while I was in the shower this morning, on my phone, I fired up a coding agent session on my laptop, because you can remote control. I'm using Codex, and you can remote control that from your phone. And I fired it up and I said, go and look at sqlite-utils and build me a new version of this library which works against PostgreSQL and DuckDB as well, and do it with test-driven development and build everything. And that was it, and it's done it. And so now I'm looking on my computer right now at a new version of my software that works against PostgreSQL and DuckDB in addition to SQLite. And this is It's one of these weird, it's a research spike, right? It's a little proof of concept to see if that would work.

SIMON:[00:04:40](https://share.transistor.fm/s/fe88354c/transcript#t=0h4m40s)
Except that the software's got over 100 tests now, and it runs the full test suite against all three of those database engines. And my involvement was pretty much typing on my phone in the shower to try and kick the thing off, and then a couple of follow-up prompts to get it to add new features. This is wildly—this is, when we talk about what's changed in software engineering, this is sort of the ultimate extreme end of all of this. This is where you can have an idea for quite a sophisticated piece of software, and this is something which I'd been idly thinking about for a couple of years now. I like using this tool. Wouldn't it be great if I could use this tool with other database engines? The latest frontier models are now capable of taking as loose as, take the ideas from this project and rebuild them against these other things, and churning out working software. And that, I feel like this is new as of.

SIMON:[00:05:34](https://share.transistor.fm/s/fe88354c/transcript#t=0h5m34s)
Really, November was when we got the first models that, like Opus 4.5, that were capable of taking these larger projects and actually delivering them without making too many stupid mistakes along the way. Is that what, it's what, that was what, 8 months ago, 9 months ago?

CLAIRE:[00:05:48](https://share.transistor.fm/s/fe88354c/transcript#t=0h5m48s)
November, November 2025. Okay, and that's what you call the inflection point, I think.

SIMON:[00:05:53](https://share.transistor.fm/s/fe88354c/transcript#t=0h5m53s)
I think that was the inflection point, because prior to that, Claude Code itself was born in February of last year. So that was really the first coding agent of the kind that we think of today. Really isn't that old as a piece of software. It came out in February, but it was—and for the first sort of six months of that year, it was fun to poke around with, but you wouldn't trust it to build you useful software. As of November, the models caught up to the point where now you can trust it to write software. Now, what is it? It's August now, and yeah, I'm increasingly outsourcing extremely ambitious projects to these tools and getting back software that I trust myself, but I won't release to other people until I've done a little bit of extra work because I don't want to stake my reputation on something that I'm not 100% confident in. But it's astonishing. What an incredible rate of advancement we've had in the past sort of nine months.

CLAIRE:[00:06:47](https://share.transistor.fm/s/fe88354c/transcript#t=0h6m47s)
Okay, so I want to get really nitty gritty and dig into the request that you made when you were in the shower. You didn't use voice apparently because you said you were typing it on your phone. Is that right?

SIMON:[00:07:00](https://share.transistor.fm/s/fe88354c/transcript#t=0h7m0s)
I've not hooked up voice via my phone to control my laptop yet. I believe it is possible. I use voice a lot, but for this particular one, I haven't quite got that working yet.

CLAIRE:[00:07:09](https://share.transistor.fm/s/fe88354c/transcript#t=0h7m9s)
So how long of a request was it that you typed in? How long were you sitting there typing and pecking into your phone?

SIMON:[00:07:15](https://share.transistor.fm/s/fe88354c/transcript#t=0h7m15s)
I'm looking at it now. It is two paragraphs of text. I can read the whole thing. It says, do a research spike to see what it would take to build a library with the same core API as sqlite-utils, in particular the insert and upsert and create and update methods and the table introspection stuff, but backed by SQLAlchemy so it works for multiple database engines. Test against Postgres and SQLite and DuckDB. Use `~/dev/sqlite-utils` for reference. Create a Git repo for this. Commit early and often. Use `uv init` to set up the project. Use red-green TDD and pytest. So a bunch of jargon in there about how I wanted this to work, but that was it.

SIMON:[00:07:50](https://share.transistor.fm/s/fe88354c/transcript#t=0h7m50s)
This is, and it's one of those things as well where a lot of people are concerned about the impact this has on software careers, because now I can knock out a couple of paragraphs on my phone in the shower and it does a substantial piece of work. But you have to have so much expertise yourself in the sort of domain in order to drive these things. I was pointing it at SQLAlchemy and telling it how to use red-green TDD and all of these different bits and pieces. And because I've spent so much time tinkering with these models, I was pretty confident that it was going to work. I can now sort of imagine a prompt that will more likely than not get me to the desired state. And that was it. And off it went, and it worked for 43 minutes. And delivered something that mostly worked, and then I told it to refactor the code so the engine-specific portability stuff lives in a file for each specific engine, because the code was full of if-then statements that I didn't like.

SIMON:[00:08:43](https://share.transistor.fm/s/fe88354c/transcript#t=0h8m43s)
And it said, okay, I did that, and off it went. And yeah, this is... Honestly, this is, this is like a week of work for me in the before times, and it got it done in an hour this morning while I was having a shower and then making breakfast.

CLAIRE:[00:08:57](https://share.transistor.fm/s/fe88354c/transcript#t=0h8m57s)
So wait, you said the software has over a hundred tests now. How does it have a hundred tests? Where did that spec come from? Are you satisfied with those tests, or are they superficial and incomplete, or?

SIMON:[00:09:09](https://share.transistor.fm/s/fe88354c/transcript#t=0h9m9s)
Well, so I've hardly even looked at them. The reason it has tests is I told it to use red-green TDD and pytest. And red-green TDD, that's the thing where you have to write a test and watch it fail, and then you write the implementation and get the test to pass. I've found that this has This has been giving me really good results with agents, because the one thing you don't want is you don't want an agent to write a bunch of code that hasn't really been exercised at all. And then you're basically just rolling the dice as to if the thing works or not. I want every line of code they write to have been exercised, and the easiest way to get them to exercise them is to tell them to write tests, because they're very good at writing tests generally. The one test file I did browse, I poked into a couple of them, and it was doing exactly the right thing in that it was It was exercising the sort of user-facing library feature.

SIMON:[00:09:59](https://share.transistor.fm/s/fe88354c/transcript#t=0h9m59s)
And then it was using pytest fixtures to run the exact same test against the three different backends. And that's exactly how I want this to work. I want every test to run against Postgres and then SQLite and then DuckDB, and only pass if all three engines pass. And that worked. And partly as well, this is because I'm using pytest, the Python testing framework, which is very well established, extremely mature software. All of the agents have seen it running in so many different configurations. And pytest has baked-in features called fixtures for running the same test against three different backends. All of that kind of stuff is at well-understood patterns. So once you know that, you can Point to the agent, you can basically say to the agent, use pytest, and you know that the agent is going to pick up those techniques from that because you've got that deep understanding of that software and you've seen the agent use it well in the past. So all of this stuff comes down to enormous quantities of sort of built-up experience across both the technologies that you're using and across the agents. You have to know what kinds of things they're capable of. If I'd tried this with an agent six months ago, I very much doubt I'd have got good results out of it. But this one, I'm using GPT-5.6 Sol Ultra, which is the mode of GPT-5.6 where it fires up multiple sub-agents and does research and has something else looking at the documentation, all of those kinds of things.

SIMON:[00:11:26](https://share.transistor.fm/s/fe88354c/transcript#t=0h11m26s)
And it's cost me, well, it's been, it hasn't cost me anything at all because I've got a subscription, but apparently I've burnt through $66 worth of tokens already. Just today. $61, because you, and this is off my $100 a month subscription to OpenAI. Because the subscriptions give you just a massive discount on the actual price of the tokens. If I was paying API prices, if I was an enterprise, I would have spent $61 on this project so far.

CLAIRE:[00:11:57](https://share.transistor.fm/s/fe88354c/transcript#t=0h11m57s)
Okay, but instead it's included as part of your subscription, no matter how little you use or how much you use, or is there some threshold after which you're going to be capped?

SIMON:[00:12:02](https://share.transistor.fm/s/fe88354c/transcript#t=0h12m2s)
Exactly.

SIMON:[00:12:09](https://share.transistor.fm/s/fe88354c/transcript#t=0h12m9s)
Well, there's a threshold. I'm now 71% of the way through my— no, I'm 29% of the way through my five-day threshold. But OpenAI resets the usage limits all the time as a marketing exercise. So there's almost this thing. I actually see people; somebody from OpenAI announced that they were going to reset everyone's usage limits in four hours, and a bunch of people were saying, brilliant, fire up Ultra, let's, let's burn through those four hours because we know we're getting a reset, which is unhealthy, quite frankly, you know, back when Claude Fable was on limited release, people were losing sleep because they didn't want to waste a second of the day that they could have been spent prompting these models. So that whole side of things is kind of gross. But yeah, the results that we're getting are. Really quite astonishing at this point.

CLAIRE:[00:13:00](https://share.transistor.fm/s/fe88354c/transcript#t=0h13m0s)
So one of the things you said on, I don't know how many podcasts you're on. I feel special because this is your third time on Talking Postgres, but I do know. Was it, let's see, it's August. So five months ago, you were on Lenny's podcast and you talked about the state of the AI union or something like that. And in that podcast, you said something like, by 11 o'clock in the morning, you are exhausted because you and your agents have done so much at that point in time. And I guess you were trying to describe your day-to-day. And I want to understand what your morning looks like from when you wake up till 11 a.m. That leads you to being exhausted at that point. Did I capture that right?

SIMON:[00:13:45](https://share.transistor.fm/s/fe88354c/transcript#t=0h13m45s)
Well, so the good news is I've found a bit more balance than I had five months ago. So five months ago, this was like peak, God, Claude Opus 4.6, I think. But it was that period where, in January and February of this year, that's when People really started paying attention to these tools because they got good in November, and then we had December and we had the sort of holiday break. And during the holidays, individuals were tinkering with them a bit. But January and February was when companies started figuring out, oh, actually, this stuff works now. And you had the token-maxxing and all of these absurd sort of absurd scenarios while people are trying to understand what we can do with this stuff. And yeah, that was a very exhausting period of time because you did feel this pressure to— you almost felt like if one of your agents isn't writing code, you're wasting time, which is a very unhealthy mentality. So I've definitely got over that now. I do not feel like I'm missing out if I don't have something churning away.

SIMON:[00:14:42](https://share.transistor.fm/s/fe88354c/transcript#t=0h14m42s)
But there is a real challenge here in finding this new balance, because we can work so much faster and, you know, an agent can churn out 10,000 lines of code in an hour. That's not. That doesn't mean that it's code that you can ship, because even if the code is good, even if the code is good and passes tests, my, I feel like our professional responsibility is we have to understand it. Delivering code to the rest of the world that you don't understand yourself is a very dangerous thing to do. It's a, that's where you get the sort of cognitive overload where firstly you're sort of getting exhausted by what's going on. You don't really understand what you've been delivering. And also for projects that you intend to keep on working on, there's this interesting thing where if you don't understand the state of your project in enough detail, you can't make decisions about it. You can't sit down and think, okay, what should I do next? Because the amount that you don't understand about your own piece of software just keeps on Growing. So that's, I think that's one of the most interesting sort of friction points at the moment, is figuring out, okay, what is the fastest we can work while we're still confident that the software is good, and we're confident that we understand it well enough to be able to make good decisions about what to do next.

SIMON:[00:15:56](https://share.transistor.fm/s/fe88354c/transcript#t=0h15m56s)
And when you start thinking about it like that, firstly, it means that you can slow down a little bit because there's no point in churning out a million lines of code in a week if you don't know what you built. And you start building much, much, much more sort of sensible habits in terms of spotting—there are tasks that are tiny and inconsequential, and you can completely outsource them to an agent. The other day, a website that I work on had that bug where when you log in, you visit a page and you're logged out, and you log in, and it doesn't send you to where you were before. You know, the classic: when you log in, it really needs to send you back. And I knew I'd implemented that in the past and it worked, and now it didn't work. And again, on my phone, I fired up an agent and I said, Figure out why redirects don't work, and it found the bug, and it was a two-line change, and it wrote a test, and we shipped the change, and it was done. And it was great because that's the kind of thing where If I'd carved out time for it myself.

SIMON:[00:16:52](https://share.transistor.fm/s/fe88354c/transcript#t=0h16m52s)
It would have been a minimum of 20 minutes of me sort of researching, trying to figure out, and it was open-ended task. Maybe it would take me four hours to fix, and maybe it would take me half an hour to fix. But it was very difficult for me to justify investing that time on something which was an irritation, but it wasn't the most important thing I could work on. You outsource that to the agent. Either the agent solves it, in which case it's solved, or it doesn't, in which case, okay, it was harder than I thought. Maybe I'll look at it later. That kind of work, that sort of parallel work where you can be working on something else while these sort of smaller, more irritating, but not necessarily Worth spending large amounts of time on tasks are just being investigated over there. But yeah, so I feel I've diverted from your original question. These days, yeah, the mornings, I'm not exhausted by 11 a.m. Anymore because I'm pacing myself properly. I don't have that, I don't feel that tension to have as many things going as possible.

CLAIRE:[00:17:45](https://share.transistor.fm/s/fe88354c/transcript#t=0h17m45s)
And I'm glad you've course corrected my question because I'm, I hate to say it, but I'm not actually interested in what your mornings were like five months ago. [Ooh, okay.] I'm kind of interested in today because I know the AI world has changed so much in the last five months. So, yeah, talk me through a typical morning in the last week or two, assuming you haven't been on vacation or something like that. Because I want, I want people to, to be able to visualize how they could be using these tools. Now, I know a lot of people are on the bandwagon and they're there, but not everybody is, so. Or not as far as they want to be.

SIMON:[00:18:28](https://share.transistor.fm/s/fe88354c/transcript#t=0h18m28s)
Okay, so something I've been doing recently, which I spent a day on just a couple of days ago, I've got way too many open issues and pull requests against some of my projects. And I've got to that point of that sort of that guilt where you're like, if I don't look at them, maybe I won't feel bad about all of the ones that I haven't got to yet. And it turns out they're all available by the GitHub API, and the agents know how to use the GitHub API. So you can basically, so I actually said to, I said to Codex, Do a review of every open issue and pull request from the last six months on this repository and figure out what are the low-hanging fruit, which are the ones where the fix is actually quite straightforward and it won't take much time, or there's a pull request that's ready to land with a few changes, and then prioritize them by easiest to hardest. And it gave me a list of ten, and I went through and I knocked off the first four, and I felt so good about it. This was— Actual, meaningful. It was, it was, it was probably.

SIMON:[00:19:24](https://share.transistor.fm/s/fe88354c/transcript#t=0h19m24s)
I invested about an hour of my time closing down four issues that had been open for quite a while, landed good code that I fully understood. I felt good about it. I didn't write the code. In two of those cases, it was pull requests from someone else, and I reviewed their code. Codex reviewed their code, made a couple of tiny formatting tweaks and landed it, and that was fine. And the other two were open issues where The fix was, it was tiny. You know, these are fixes that are four or five lines of code, but the problem is always figuring out where the four or five lines of code go. And so it was very quick to review. Reviewing four or five lines of code that an agent has checked out is no major— The problem with review comes when you've got a thousand lines. That's when things sort of freeze up. But if you can arrange things into these much smaller commits, and that was great. You know, that was, and that sort of— It unstuck me on that, that aspect of that particular project. And so that, but part of the problem is that I'm very, yeah.

CLAIRE:[00:20:23](https://share.transistor.fm/s/fe88354c/transcript#t=0h20m23s)
But does the unsticking continue? Okay, so in other words, you had the low-hanging fruit and you integrated, you said four of them, right? [Yes.] So now what? What about all the rest of them?

SIMON:[00:20:36](https://share.transistor.fm/s/fe88354c/transcript#t=0h20m36s)
So I got inspired, and I'm like, you know what, there's this one much bigger task on this project that I've been putting off. Let's spend some time on that, and that turned into a— Two-and-a-half-hour session of paying close attention to what was going on. This was solving a particularly gnarly sort of database migration-related problem. But because I'd got that momentum going from fixing some small things, I could move, I could start taking on the much, much larger project. And that was the kind of thing where You have to pay. That's more of a collaboration with the agent, where you're not just setting off on a side quest and then wandering off. You're actually paying attention to what it's doing. You're directing it. You're modifying little bits and pieces yourself.

SIMON:[00:21:21](https://share.transistor.fm/s/fe88354c/transcript#t=0h21m21s)
But that was good, you know, and that, that, so that sort of the low-hanging fruit turned into shipping actually quite a significant feature, which I'd been putting off again for months. All of this keeps on coming back to procrastination and guilt, which is kind of interesting. Something I have noticed, though, that's very weird is that sometimes, in traditional software engineering, you have hard problems where you really do need to carve out four hours of uninterrupted time. You have to focus everything. There's that famous idea that if you interrupt a programmer to ask them a question, you might have just cost them half an hour because the whole stack of cards in their head comes tumbling down, and then they have to get back into the zone, and that, that's, that's, that's a major problem. That's not a problem for me anymore. Only because.

SIMON:[00:22:07](https://share.transistor.fm/s/fe88354c/transcript#t=0h22m7s)
If you're working with an agent, the agent holds a lot of that context itself. See, and you can ask it questions and say, Oh, where did we get to? and get back up and running really quickly. But the really weird thing is that the harder a task is, the more you can be distracted from it, because you might have a task where an agent has to crunch away for 15 minutes working on it, and that's suddenly 15 minutes that you have free for something else. I do get substantial amounts of work done. When I'm walking the dog, which is a bizarre state of—it's absolutely bizarre that that's true these days, but I can fire up a really difficult task, go on a walk with the dog, check in on my phone occasionally to see if it's going in the right direction and maybe prod it somewhere else.

SIMON:[00:22:51](https://share.transistor.fm/s/fe88354c/transcript#t=0h22m51s)
And by the end of the walk, I've got 90% of a very difficult problem solved for me. And then the challenge is, it's that discipline. It's making absolutely sure that you fully understand everything in there. My gold standard is, could I explain this to somebody else? Can I take this change, which is going to have my name on it, you know, I have to be able to take accountability for the work. Could I sit down with somebody else and talk them through exactly how it works? And if I can, I feel confident shipping that as production software, even though I wrote hardly any of the lines of code that make up the change.

CLAIRE:[00:23:22](https://share.transistor.fm/s/fe88354c/transcript#t=0h23m22s)
So I feel like that gold standard is something that a lot of people are. Either struggling with or not getting right yet. It's, it's, it takes discipline to do that. And in fact, you wrote a blog post the other day that I loved that was a blog post about a blog post, which you do sometimes. You see another blog, you really like it, and you want to give it a shout-out and quote from it and kind of shine a light on it. And it was a Sophie Alpert blog post titled, There Are No Lossless Transformations of Natural Language Text, which I'd love you to expound on why you thought that was so important, but—

SIMON:[00:23:42](https://share.transistor.fm/s/fe88354c/transcript#t=0h23m42s)
Mhm. Yes. It's such a great post, yeah. So this was the internal policy on acceptable use of AI writing by engineers that Sophie wrote for her employer, Clay. And it's very short. You should read the whole thing. It's like, what, five paragraphs of text. [Yeah, yeah, yeah.] But it's such an important topic right now because these things are really, really good at—they're really good at writing code, and they're very good at writing technical documentation. AI writing, if you're trying to be convincing or creative, I think it's garbage. You know, you can—you just read these things and your teeth get set on edge. I use it for documentation all the time because the whole point of documentation is it just has to describe in the most boring way possible exactly what the thing does. And so if you manage to tell your AI not to add any jokes or try and fluff things up, you can get very, very useful results out of it.

SIMON:[00:24:51](https://share.transistor.fm/s/fe88354c/transcript#t=0h24m51s)
And you know, it's great at writing things like pull request descriptions because a pull request description just has to describe exactly what it is. And yet, when I see an AI-written pull request description, I don't want to read it. You know, it's like eight paragraphs, and it's all technically accurate, but it's not telling me that sort of higher-level thing where a human being is communicating to me, these are the things that matter. That, it turns out that I care about that more than accuracy in a lot of cases. I want to know, what did you, with your unique human judgment, think is the most valuable thing about this? And so, Sophie, one of the things Sophie said is, you must stand behind every idea and every sentence in your documentation. It has to be representative of your own thoughts before you share it. If a reviewer asks, What did you mean by this line? It's not acceptable to reply with, Oh, sorry, AI wrote that. Just ignore it. I love that. That, to me, because the other thing, I think it's very important not to tell people they shouldn't use AI for Writing, because a lot of people have English as a second language. I've got nearly 25 years of blogging experience. I'm a very experienced writer. It is not fair for me to say to other people, You should not use technical assistance for your writing, just because I find it easy because I've been doing it for 25 years. But at the same time, there's a very important thing about respect. You have to show respect to your readers, to your coworkers. You have to have put the effort in to make sure that the thing that you're communicating to them is good and it reflects the exact truth in your mind of what matters. And that, I think, Sophie caught that beautifully with this piece. Then her closing, that line about lossless transformations, she says, There are no lossless transformations of natural language text. Every rewrite and rephrase...

SIMON:[00:26:33](https://share.transistor.fm/s/fe88354c/transcript#t=0h26m33s)
Changes the meaning of your writing, and if this is done by an entity that doesn't have the most detailed mental representation of what you personally are trying to communicate, information will be lost. And that, that nails it for me. You know, I don't care if the AI wrote it, as long as you will stand by every single detail on it and you're confident that it's the best expression of what you're trying to communicate, and it's not going to waste my time to read through it.

CLAIRE:[00:26:57](https://share.transistor.fm/s/fe88354c/transcript#t=0h26m57s)
Yeah, so I feel like. I just feel like that's, that's a— A struggle for some people, because it's just so easy to skip that step, be like, okay, it did it, I'm going to move on. I want to get— Sometimes people just want to get things done, and they glance at it, they give it a superficial review. Anyway, I've seen— AI slop, and I don't like it. So...

SIMON:[00:27:21](https://share.transistor.fm/s/fe88354c/transcript#t=0h27m21s)
It's, it's a plague right now. It's an absolute plague. I've got this problem on Twitter in particular because I show up on lists of prominent AI voices to follow. Anything I post on Twitter gets at least a dozen automated AI bot replies with all of the, the, the— and it's just soul-destroying. It's— I've seen a few of them start to show up on Bluesky as well, and it's just horrifying. It's like this, this, this is absolute junk, and it instantly— Which if it destroys the credibility of the people using the bots, which is, is, is something people just aren't understanding yet.

CLAIRE:[00:27:58](https://share.transistor.fm/s/fe88354c/transcript#t=0h27m58s)
I mean, it's no different, I suppose, that as a project lead or a maintainer, just because a PR was written by another engineer on the project, if you're the maintainer and you commit it and you accept it, you have to stand by it. So in many ways, these agents are like the people submitting the code or the employee or the intern, if you will. You still are responsible and accountable for it.

SIMON:[00:28:25](https://share.transistor.fm/s/fe88354c/transcript#t=0h28m25s)
Absolutely, yeah, it's the, the accountability and the credibility are the two most important things. If you want to stay credible with your co-workers, with the world at large, you can't be seen as just—there was a great term for this—there's slop cannons, there's the, the word slop shows up in all sorts of different ways around it. A slop proxy, I think was it. It's just. [Oh.] Copying and pasting in through exactly what the AI said, and that adds no value at all. And my optimistic hope here is I think this is a passing phase. [I hope so.]

SIMON:[00:28:59](https://share.transistor.fm/s/fe88354c/transcript#t=0h28m59s)
Because it's all so new. [Yeah.] The fact that an AI can write you a decent pull request has been—that's, again, six months ago that started being the case. And the friction is already starting to show up, and people are beginning—it's becoming socially unacceptable to do that in certain circles. And I'm hoping that spreads because what I've actually, something I've started doing recently is, so GitHub Issues supports the summary details HTML element. So you can say less than summary, no, less than details greater than less than summary greater than bit of text, and then splat in the rest of the stuff. And it gives you a little collapsed, a little piece of collapsed text. So there's a little arrow and a single line, and when you click the single line, it expands.

SIMON:[00:29:44](https://share.transistor.fm/s/fe88354c/transcript#t=0h29m44s)
And shows you everything else. I've started using this for the AI pull requests. So if my agent wrote a very detailed pull request, I will make it available on the pull request, but I will collapse it. So I will have a paragraph of text that I wrote saying, I fixed this and this and this, and then I'll have a little thing that says Claude 5 PR description. And if you click that, you'll get 20 paragraphs of detail from Claude, which is useful if you want to see it, but it just feels less pollute-y and less sloppy to hide that stuff by default unless people opt into seeing it.

CLAIRE:[00:30:17](https://share.transistor.fm/s/fe88354c/transcript#t=0h30m17s)
Oh, that's a literal example of having to double click into something. You know, that horrible, horrible phrase that people use, but yeah, I like it. The 20 paragraphs, though, I do sometimes find that AI-generated text can be too long. [Yep.] It can be too much. It can be overwhelming. And it goes back to what you said, you need that human to figure out what matters, or we need to use our LLM tools to get to the crux of what matters more.

SIMON:[00:30:49](https://share.transistor.fm/s/fe88354c/transcript#t=0h30m49s)
Honestly, like I said, I do let the AI write a lot of my technical library documentation, but I read every single line it wrote and I try to edit it not by editing it myself, by saying to the agent, make that shorter. Don't mention that detail. Drop that bit off. Split that into two bullet points. And that's something I found as useful as a technique for code review as well. So occasionally you do need to review a thousand lines of AI-generated code. It's built some kind of complex subsystem. You need to take responsibility, so you have to review it. Reviewing a thousand lines of code is miserable. It's very, very easy for your eyes to glaze over and you skip over the details. Something I found quite helpful is, I think of it as a sort of aggressive nitpicking.

SIMON:[00:31:34](https://share.transistor.fm/s/fe88354c/transcript#t=0h31m34s)
Review, the kind of thing you would never do to your coworker because it's really rude to go after your coworker and nitpick every single tiny detail of the code that they've written. It's not rude to do that to an agent at all. So you can set yourself a goal to basically force it to rewrite almost every single line. And it's the tiniest, tiniest little things, like absolute nitpicking. But the goal isn't actually to improve the code so much as to make sure that you've had to think about and transform every bit of that code just so that you've paid attention to it. And I've done that for a few of these larger changes, and I think it works pretty well. I come out of it at the end, I definitely understand the code. I feel like I've got—I'm ready to stake my credibility on that. I'm ready to say, no, this is, I have reviewed this, even though it was a thousand lines. Made a bunch of little tiny changes to it. I feel good about it.

CLAIRE:[00:32:23](https://share.transistor.fm/s/fe88354c/transcript#t=0h32m23s)
So you said a few minutes ago that your gold standard with a thousand lines of code or whatever is, could you explain it to someone else? [Yes.] But it sounds like the way you're getting to that ability to explain it to someone else is perhaps this aggressive nitpicking review that causes the rewrite. Are there other ways?

SIMON:[00:32:43](https://share.transistor.fm/s/fe88354c/transcript#t=0h32m43s)
I mean, you can just sit down and read it really, really, really carefully. I just, I'm skeptical. I don't think I have the ability to read a thousand lines of code and really come out at the end fully confident that I understood the whole thing. I feel like I have to be manipulating that code in some way. And sometimes I'll fire up, I use Python, so I can fire up a Python interactive interpreter and try a few things interactively there. That can help. But honestly, for those larger code blocks, I think it really, the, the nitpicking review so far is the thing I found that feels the most credible. It feels like I've really forced myself to engage with the code because I'm actively trying to find reasons to change it.

CLAIRE:[00:33:28](https://share.transistor.fm/s/fe88354c/transcript#t=0h33m28s)
All right, so. You can see I've done a tiny bit of research here. I want to go back to, or go over to another podcast that you were on recently, which was with Bryan Cantrill and Adam Leventhal, Oxide and Friends, who, you know, I used to work with them at Sun. We were all in the kernel group together. Bryan was across the hall, Adam was down the hall and around the corner, and so I've known them for decades, and they're awesome. But there was an example you used on that podcast where you described something that had happened that day. You said, I...

SIMON:[00:33:40](https://share.transistor.fm/s/fe88354c/transcript#t=0h33m40s)
Oh, that was fun, yeah.

CLAIRE:[00:34:02](https://share.transistor.fm/s/fe88354c/transcript#t=0h34m2s)
I think you, I don't know which LLM you were working with, but you said, I gave it my main open source project and I prompted it and said, do some experiments and try to make it faster. And I'm assuming that's Datasette that you're talking about. Okay. And you just checked in to see the results and it had sped it up by 36%.

SIMON:[00:34:14](https://share.transistor.fm/s/fe88354c/transcript#t=0h34m14s)
Yeah, yeah, it.

SIMON:[00:34:21](https://share.transistor.fm/s/fe88354c/transcript#t=0h34m21s)
And you know what? I've not even reviewed or landed that code. That is somewhere on my computer. I have a branch of Datasette that is 39% faster, and I just haven't got round to reviewing what it did yet.

CLAIRE:[00:34:31](https://share.transistor.fm/s/fe88354c/transcript#t=0h34m31s)
That's exactly what I wanted to ask. I wanted to know, and so maybe we can talk about this theoretically then, since you haven't gotten to it yet. But what are you going to do next? What do you have to do before you can accept that 36% improvement change? To verify it, to QA, to review it, to make sure there's no regressions, to document it.

SIMON:[00:34:50](https://share.transistor.fm/s/fe88354c/transcript#t=0h34m50s)
That is such a good question. [I know.] I think the reason I've not done it is everything in software engineering is about trade-offs, and the number one trade-off is your time, right? This is what's so disruptive about coding agents is a lot of people will tell you that it makes no sense at all to measure productivity in terms of lines of code written. That's, that's, that's— and I'd actually disagree with those people because there is this sort of hard limit in the before times. A software engineer could produce a few hundred lines of working code per day. And when I say working code, I mean a few hundred lines of production-ready, and that's actually an incredibly good day if you produce 200 lines of working, debugged, production-level code.

SIMON:[00:35:40](https://share.transistor.fm/s/fe88354c/transcript#t=0h35m40s)
You can feel very, very good about yourself. Most days you'd produce 50 or 60 lines of production-ready debugged code. If agents let you produce a thousand lines of debugged code, that really is a very meaningful improvement, as long as that code is of the same quality, right? It has to be high quality, it has to be maintainable, it has to be tested, all of that kind of stuff. You can get to that point with agents, but it takes a huge amount of skill and knowledge and experience and all of the, this is what senior engineers are made of, is this ability. So on the basis of those trade-offs, the problem is I've now got a branch of Datasette with a 39% performance improvement. I know that getting that from where it is right now to Feeling confident, properly tested, QA'd, in the project such that I can explain to other people is. Several hours to several days of work, and I've not. Chosen to put that at the top of my stack yet.

SIMON:[00:36:36](https://share.transistor.fm/s/fe88354c/transcript#t=0h36m36s)
And at some point, I hopefully will. But it's a huge problem because that's not the only one. I've got dozens of branches of my major open source projects now with changes of that nature, oh, it's sped it up by 39% and so forth. And they all just sit there sort of going stale because just because you can do this, 

...(content truncated)