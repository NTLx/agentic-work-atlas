---
type: raw
source: "https://podcasts.apple.com/us/podcast/anthropics-first-technical-pm-on-token-maxing-the/id1627920305?i=1000778409270"
transcript_source: "https://pod.wave.co/podcast/lennys-podcast-product-career-growth-b65486a6-7cff-4966-bbea-2bc239e90aa4/anthropics-first-technical-pm-on-token-maxing-the-jagged-edge-and-living-in-the-future-dianne-penn"
title: "Anthropic's first technical PM on token maxing, the jagged edge, and living in the future"
author:
  - "Dianne Penn"
  - "Lenny Rachitsky"
publisher: "Lenny's Podcast: Product | Career | Growth"
published: 2026-07-26
created: 2026-07-30
description: "Lenny's Podcast 第 1627920305 集（2026-07-26，1h 34min）。Dianne Penn（Anthropic Head of Product for AI Research and Labs teams，前 Amazon Alexa AI、JP Morgan 高收益债交易员；2023 年作为 Anthropic 第一个 technical PM 加入时整个产品团队只有 5 个工程师）访谈。⚠️ Vendor 立场（中等）：Anthropic 是产品供应方也是被访谈对象；Penn 高度赞美 Claude 编码能力（“Opus 4.5 wouldn't have had that moment without a product like Claude Code”），机制层可独立验证、立场层需打折。核心方法论——Eval-driven development loop：Penn 团队核心实践是 'evals are the new PRDs'（与 Garry Tan 共识），evals 既是 model 评估也是 product 评估工具（替代传统 PRD 的需求描述功能）；building evals 是 PM/engineer 都被低估的能力——'you don't need hundreds, just 10 great evals'。Opus 3 → Opus 4.5 转折点：2023 没人说 'Anthropic+Claude+coding' 同句；Opus 3 是分水岭（开始 train 模型做 long-form code 而非 autocomplete）；Opus 4.5 + Claude Code 协同放大（'wouldn't have had that moment without each other'）。Anthropic Labs 孵化模型：内部独立团队加速/seeing around corners；五大 PM 团队并行——research PM team（Diane 领导，负责 model feedback → research + model launch shepherd）、Claude developer platform（APIs + managed agents）、Claude Code + Cowork、Enterprise（cost controls/RBAC/security）、Growth。PM 数量从 5 工程师时代的隐含 PM 到 30-40 PMs；TPM 角色定义——first principles thinking（非 pattern matching）+ 全栈工程师背景（'almost all PMs have either been engineers or ship code here on Claude Code'）+ 产品 taste（'very rare skill'）。'Right amount of AGI pilled'：看清 5 年后模型能力容易（'just a text box'）但要为当前模型规划产品路径（'how do you elicit the maximum capability'）；这是 PM 核心稀缺技能。Model introspection as debugging——问模型 'why did you do this' 揭示 system prompt 误导 / sub-agent 未 verify 等失败模式，反向修正 harness。Token maxing 概念：Dianne 视角 'product lens'——token 是 input，output 是用户结果（不像 VC 视角把 token spend 当 ROI 代理）；与 Fiona Fung 的 'token spin vs token spend' 讨论呼应；Garry Tan（YC）论点：愿年花 $100K 在 tokens 上 = 活在 2028 模式。Hire 偏好：engineers with great product taste（非更多 PMs）以减少 shipping overhead；designers 都有 frontend engineering 背景——team-level trust + speed multiplier。"
tags:
  - clippings
  - lennys-podcast
  - anthropic
  - claude-code
  - eval-driven-development
  - tpm-role
  - agentic-engineering
  - ai-research
---

# Anthropic's first technical PM on token maxing, the jagged edge, and living in the future

*Dianne Penn (Head of Product, Anthropic AI Research and Labs) · Lenny's Podcast · 2026-07-26 · 约 1h 34min · Transcript from pod.wave.co*

---[00:00]

Diane Penn

In 2023, when I started, nobody said anthropic and Claude and coding in the same sentence.

[00:06]

Lenny Rachitsky

I want to go back to the beginning of anthropic. I remember dealing, man, these guys have no chance. OpenAI is so far ahead.

[00:14]

Diane Penn

At the time I saw people were starting to use these models not just for code autocomplete, but actually writing long form code and set an opportunity for us to train Opus 3 to be better at that was the inflection.

[00:26]

Lenny Rachitsky

I always think about Opus 4.5 a year later, during winter break when everyone was home able to code.

[00:31]

Diane Penn

What was magic about Opus 4.5 is we also now not just had a model, but a vehicle, a great product experience like cloud code. Opus 4.5 wouldn't have had that moment without a product like cloud code. And cloud code wouldn't have had that type of adoption accelerated without Opus 4.5.

[00:50]

Lenny Rachitsky

I want to talk about how the product role is changing for my team.

[00:54]

Diane Penn

The way to drive user value is to figure out the right user feedback. The evals, we actually have a saying on the team of evals are the

[01:02]

Lenny Rachitsky

new PRDs, something Gary Tan's been talking about. If you're willing to spend $100,000 a year right now on tokens, you are living the way somebody in 2028 is gonna live.

[01:10]

Diane Penn

You have to sweat the tokens as much as you sweat the pixels. You have to be using the models to come up with good, then great, then better ideas. And there's no substitute for that.

[01:21]

Lenny Rachitsky

People need to be more ambitious with AI tools these days because they're just capable of so much.

[01:26]

Diane Penn

One thing I ask the team is, let's say Claude 8 comes around. What changes in users do? What does that mean for how you're building today?

[01:36]

Lenny Rachitsky

Today my guest is Diane Penn, Head of product for the AI Research and Labs team at Anthropic. She joined anthropic as the first technical product manager over three years ago, which is a lifetime in AI time. When the product team was just five engineers. She's helped ship every model at anthropic from Claude 2 through Fable. She's also helped incubate and launch Claude Code, MCP skills, Claude design and also core capabilities like computer use, tool use and reasoning. It is always such a treat and so mind expanding to get to talk to someone who's at the very center of AI and product management. It's hard to imagine someone who has seen more of where things are going than the head of product for Anthropic's research and labs. Teams. Before we get into it, don't forget to check out lennysproductpass.com for a year. Free of the hottest and most beautifully crafted AI products in the world, available exclusively to Lenny's newsletter subscribers. With that, I bring you Diane Penn. Diane, thank you so much for being here and welcome to the podcast.

[02:41]

Diane Penn

Thank you, Lenny. It's so nice to see you again.

[02:43]

Lenny Rachitsky

I want to go back to the beginning of Anthropic, the early days. I remember when Anthropic first launched. This was, I don't know, the first model when it launched years ago, three years ago, something like that. It works. Three years. I remember just like feeling that, man, these guys have no chance. OpenAI is so far ahead. Everyone, they're just like, what are they thinking? How is this possible? OpenAI has won. It's too late. Things are very different now. The latest number I saw was Anthropic was making like, I don't know, $50 billion billion dollars in ARR. That's like what companies used to go public at. Like very successful companies went public at 50 billion in valuation. Anthropic reportedly is making that every single year. You joined as one of the earliest PMs. There were something like five engineers when you joined. The model hasn't, hadn't even launched when you joined. What was it like in those early days, Eventhropic? What's something that might surprise people about what it was like at the beginning?

[03:45]

Diane Penn

I think a big part of what's made Anthropic today actually has been very much the core of even the early days. So I joined in 2023, like you said, we had five product engineers. There was one engineer for the entirety of our API business, if you believe. And I think a big portion of it was the culture was really strong. And I think this is something I emphasize for folks who are interested in the company really do walk the walk of the mission and the culture and the values and the energy was very much like a startup. And I think you're right. We were very much trying to find our identity in the early years. Like, I think there's one piece around the technology, but how does that technology bring value to users, bring value to society, and what can it possibly be? And I think the early years were us exploring that in different ways. Like, we did start with Claude AI, another chatbot chat assistant, and evolving into things like tool use. I think one of the moments where really we started to get into our groove was shipping things like Goldengate. Claude, I don't know if you remember that?

[05:02]

Lenny Rachitsky

No.

[05:03]

Diane Penn

So this, this was actually up for about 24 hours or so. We had just published one of our early interpretability research in early 2024, and one of the examples was essentially you could have what's called, like, features of the model within the layers which express certain types of thematics. So one of the themes that the researchers was able to identify was, let's say, bullet point writing. Another one was people and places. And one that really came up frequently that resonated was the Golden Gate Bridge. And so when you actually essentially dialed up that feature, CLAUDE would obsess about the Golden Gate Bridge. So meaning in every one of its responses, it would come back and talk about the Golden Gate Bridge. So if you said, like, give me a recipe for making spaghetti, it would say, here is a recipe. And the orange color is just like international red that the Golden Gate Bridge looked like. And so it was like, really quirky. And we very much wanted to, in that situation, just bring that user, bring it to the masses and bring it to people who are starting to use claude. And so the entire experience, actually we spun up on our Claude Cloud AI website within 24 hours. And that took engineering, product design, our research teams all working together, and we were really, really proud of it. I think it maybe reached only 2,000 people, to be honest, but it made us feel like, oh, we can actually bring new user experiences, showcase our research in a way that's different and authentic to us and in a very startupy like pace. That to me was like one of those maybe hidden inflection points of we were starting to find our identity, that we could build products, build experiences that were different from what our competitors had seen, what was already out there. And I think that obviously labs, cloud code, et cetera, we then started to identify ourselves as well, what do we actually think the world, how to think about AI, how to bring that closer to the public. But it was a very bottoms up culture. And so that entire experience was very bottoms up. I see engineers, I see designers donating time to work on. And so I like to always use that as example of what the early days were like. But the culture and the values have very much, I think, stayed the same since those early days.

[07:46]

Podcast Sponsor/Announcer

This episode is brought to you by our season's presenting sponsor, WorkOS. What do OpenAI, Anthropic, Cursor, Vercel, Replit, Sierra, Clay and hundreds of other winning companies all have in common? They are all powered by work os. If you're building a product for the enterprise, you've felt the pain of integrating single sign on scim, RBAC audit logs and other features required by large companies. WorkOS turns those deal blockers into drop in APIs with a modern developer platform built specifically for B2B SaaS. Literally every startup that I'm an investor in that starts to expand upmarket ends up working with work os and that's because they are the best. Whether you are a seed stage startup trying to land your first enterprise customer or a unicorn expanding globally, WorkOS is the fastest path to becoming enterprise ready and unblocking growth. It's essentially stripe for enterprise features. Visit workos.com to get started or just hit up their slash where they have actual engineers waiting to answer your questions. WorkOS allows you to build faster with delightful APIs, comprehensive docs and a smooth developer experience. Go to workos.com to make your app enterprise ready today.

[08:57]

Lenny Rachitsky

What are some of the other big inflection moments as you think about just anthropic going from just this lab that's trying to compete with this juggernaut of OpenAI at that point to what it is today? What are some moments that stick out of like wow, that really changed things

[09:11]

Diane Penn

definitely when we were training and testing Opus 3, I think that was the moment when the company, I think we were less than 200 people still at that point and it was very clear that we needed and wanted to create a frontier model and that was very important in terms of our ability to reach users, consumers and to showcase our research. We were looking for ways for also why should somebody choose Claude? And that was a core question and that was a core question we were getting asked in the early days. I think with Opus 3. It launched I think early March 2024, but there was many, many months of various teams across inference, across research, fine tuning, pre training that rallied at different points and towards a common goal. And I think everybody that was involved was really proud. I remember being the PM us the research leads myself, we were all in our this was around December so we were all at home in our various parents homes and seeing everybody's background of their childhood room and everybody is working really hard to figure out what are we training the model for, is it showing up the right way? So I think that was really powerful in terms of just building a lot of trust and a lot of our research leads have actually from that time are now leading reinforcement learning, leading our character work alignment work. So that foundational trust I think also helped us work well now with any of our production models across product and research because we were working just so much in the trenches together in the early days. And then I think there were things like identifying that coding was important. Right in 2023, when I started, nobody said anthropic and Claude and coding in the same sentence. I think competitor models like GPT4 at the time was used a bit for coding, but it was one of many use cases. And one thing that, for example, I saw was people are starting to use these models not just for code, not just like code autocomplete, but actually writing long form code. And is that an opportunity for us to train Opus 3 to be better at. It ended up being a relatively smaller change from a training perspective, but it ended up helping us differentiate in the early days competitively for users and actually bring a lot of the very early cloud enthusiasts and developers because we were providing a value that they didn't really think was possible at the time.

[12:10]

Lenny Rachitsky

It's so interesting, you talk about Opus 3 that's so long ago. And just like it's hard to think that was a big inflection. And so this is really interesting to hear that that was internally a big milestone. It almost feels like this confidence. You all built that, wow, we could really ship a Frontier model, which is now today, so not great if you compare it to what we've got today. What I always think about is Opus 4.5, which was, and interestingly, like a year later, also during winter break when everyone was home able to code. Was that another big Milestone?

[12:39]

Diane Penn

Yeah, Opus 4.5 was definitely another large moment. I think what was magical about Opus 4. 5 is we also now not just had a model, but a vehicle which is like a great product experience, like Claude code. One thing we say a lot on the team is you need Frontier products in order to have Frontier models and for people to feel the magic of Frontier models. And I think we felt the magic of Claude code for many months before that. But the fact that the model essentially got to a level of intelligence where at a very broad level, users can experience both frontier intelligence in new use cases, allow it to run things end to end in an agentic manner, I think that was the inflection. It was actually both. I think Opus 4. 5 wouldn't have had that moment without a product like cloud code and Claude code, I think wouldn't have had that type of adoption accelerated without opus 4.5.

[13:51]

Lenny Rachitsky

So kind of speaking on this thread, Dario, interestingly, if you look back at all his predictions, he's just like, okay, coding is going to be solved. It'll be 100% in like a year, something like that. He kept talking about how we're going to do like AI is going to do all our code. And I remember everyone being like, there's no way. This is way too complicated. How is AI ever going to get really good at this very complex thing that humans do? No, this is going to be humans for a long time. He was completely right. Something else that he talks a lot about is this exponential that we're now. Now that we're on. That's the way he describes it now we're like, we're on the exponential curve. I remember not long ago, new models were being released and everybody was like, okay, we're done. There's no more upside, it's plateauing, it's over. There's no more room to grow. And now it's like the opposite. Now we're inside. Like if you think about the curve of the exponential, we're like inside of the exponential now, which by definition means every improvement is a massive jump because we're like on that hockey stick part, what's it like just being on the inside of this crazy historic moment when AI is improving so fast, so much is being unlocked? What is it like and how should people prepare for the coming acceleration of more and more improvement throughout from AI?

[15:06]

Diane Penn

One thing I like to say on the team is most of us weren't actively working yet when the Internet transitioned from this novelty to something that everyone can use. And it feels like that's just taking humans. I think analogies are helpful. And so the analogy of that is. I think a couple of things. Number one is adaptability becomes very important. I think we have evals, we have on the safety side, safety testing, red teaming on the capabilities and product side, new prototypes, products like cloud Code, Tag and others. But it's very hard to predict the exact moment or the exact model. And so the adaptability of when you're faced with new information, how do you then make better decisions versus keeping the same plan? That agility is really important. I think another piece is with that, how do you actually be thinking very first principles and reason through what's next? What's the. So what, how do we invest in new products? How do we invest in explaining the differences to users? So a lot of the, A lot of the experiences I think of being in that exponential is that pace, understanding how you operate and make better decisions and then applying that first principles, thinking to then do something that maybe we pull up a plan that we would were expecting a few months from now, but now the model can actually do and work on and actually bring that to users. So this is things like cowork skills, tag, you know, it's a very positive self reinforcing loop. And I think a big part of it also is just having the like trust in each other, like making sure we have like we're thinking through the right decision making, we're bringing folks along. Some teams might see the exponential, feel it faster than others. So how do we kind of have the grace to bring the organization, the growing organization and company along on that?

[17:23]

Lenny Rachitsky

So what I'm hearing here is you almost don't know what will be possible with every model release. And so the important things to focus on is being adaptable. As things emerge. To your point, the product itself has to stay up to, has to catch up to what is possible. To your point again, just like it can do so much, but people may not understand how to do it and may not be able to do it. So the product making it easy and even just like telling you here's something you could do feels like an important part. Is that roughly what you're doing describing?

[17:52]

Diane Penn

I think so. I think there's some really interesting graphs in the original scaling law papers. And I think folks are very familiar with the scaling laws in the lens of as you add in more compute and data, what's called loss, AKA the loss from next token prediction goes down. And so it's a very smooth linear curve of like the models get more intelligent as you scale them up. What's actually also interesting in that paper is there are these very different emerging capability graphs. And so for example, as you add in more data and you train the models with more compute, you essentially see these actually discontinuous emergent capabilities jump. So the models go from one plus one being a thing that it can't calculate to a thing that it can reliably calculate. And so these emerging capabilities, this like some nature of like predictability is, is, is not necessarily everyone knows exact moment, like you need the evals to be able to assess. That has actually always been a part of how this technology works. And also what makes like things like safety harder because unless you have the evals, unless you have the systems to test these jumps might actually happen. And you don't know.

[19:16]

Lenny Rachitsky

That's so interesting that you may have developed this AI brain that can do something you're not even aware of. And so part of the job is just uncovering, wow, it just got really good at this thing. What can we do with that?

[19:27]

Diane Penn

I think there's product overhang and user overhang to maybe put it in our PM language, even on today's models. And I think there's a lot that we could be exploring on our current opuses and definitely with Fable, for example. And that discovery is actually another part of what's been in the early days of anthropics, DNA and I think is also continuing to be a big part of how we operate in product, in labs and. And across research.

[20:03]

Lenny Rachitsky

This makes me think about something Gary Tan's been talking about, President of yc. I don't know what his title is. He's. He had this interesting point that if you're willing to spend $100,000 a year right now in tokens, you are living the way somebody in 2028 is going to live. Because by then it'll be really cheap. Everyone can work this way, but if there's this alpha opportunity right now to just live in the future, go crazy on token spend. And so there's a big opportunity for people to learn what the future is like and also just build much faster thoughts on this idea and the value of token maxing, let's call it.

[20:37]

Diane Penn

Yeah, I think I take more of like a almost product lens. It's almost like token spin is more the input and really the output is what you described of experimentation. And I think if we were orienting goals around experimentation, I feel like that that might be the better framing of the outcomes and therefore there might be different ways of achieving that outcome. I will say internally, some of the most creative thinkers, the best prototypers, do spend a lot of time with Claude. With every new version of a research model that we have, there is something around. You have to be using the models to then come up with good, then great, then better ideas, and there's no substitutes for that. It's very hard to come up with a perfect strategy without touching the technology when it's moving this quickly. At the same time, I think there's other things that we could be doing. So one thing that we do a lot is actually working in public internally within anthropic. And so in the early days when we had less product surfaces, there was a slack channel where everyone, almost the entire company was testing early versions of Claude and trying different use cases. Like people were not calling them use cases, but you might be asking it to edit an essay or to come up with the right way to send this email. They were all different use cases, but we all worked in public. And then what you would see magically is different users or different folks on the team coming up with an idea and then other people trying different variations of that idea. Then within maybe 10 or so requests, there was something magical or potentially a new use case that emerges. I think there's a lot in not just individuals, but figuring out by themselves how to use this technology. I think we could be doing more to actually bring that communal discovery when we do experimentation. Experimentation is not always necessarily a individual sport.

[22:55]

Lenny Rachitsky

It's so interesting. Yeah. This idea that we're not sure what this is capable of or what we could do with it. And it takes all this poking around and people trying things, hearing what other people are trying to figure out what's possible. Such an interesting, I don't know, technology or just like, okay, here's what. Oh, well, I figured out I could do this thing. What are you going to do with that?

[23:13]

Diane Penn

I think in a broad theme we know, right. We know that the models can write great essays or can write long form writing, but individual pain points of what can you actually solve with that and bring it to a user level that people can use? I think is something that is more exploration or experimentation based.

[23:34]

Lenny Rachitsky

Following this thread, you oversee product for the Labs team, which is extremely cool. We've had Ben Mann on the podcast, Mike Grieger, who both work on labs now talk about labs. What is labs? What's come out of Labs? Many people have heard of these things and how do they work that enables them to create such innovative ideas outside of even the core anthropic product team?

[23:58]

Diane Penn

The thesis of Labs in many ways is identifying and pulling the thread on the thread of discontinuous large bets that might not be in the core roadmap and figuring out is there a there there? And also what is the 10x100x1000x of the there there. And so, for example, things like cloud code, I think I've heard of it. Things like cloud code, things like skills, and most recently cloud design. Mcp. The thing that we really try to emphasize within the teams is especially right now, there are so many things that could be built. What does it mean then to have a discontinuous bet? And I think one approach that we're taking this year is you can be very strongly held opinion about the theme or the area and then more weakly held about the exact prototype. There is a culture of experimentation. There's a lot of the bottoms up engineers on the team are very self enabled, self driven to test out different ideas and sometimes we have a thesis and it might not work yet. And so we then might revisit it in one to two model generations. And so this idea of like these prototypes that actually end up just helping us learn, like that's also valuable even if it doesn't lead to something immediately shipping. And so I think that allows the incubation and like the charter of labs to really accelerate and see around corners more broadly for Anthropic.

[25:45]

Lenny Rachitsky

It's so funny to think about a labs within an anthropic which is already so innovative and creative and just shipping like crazy that there's value to still creating a labs team within Anthropic. What enables labs to work as well as it has? Because you listed all these products and it's like, what else has Anthropic shipped? It feels like all the biggest wins almost. I'm sure there are many that I'm not thinking about right now. What's kind of core to creating a successful labs org within, within a larger company?

[26:13]

Diane Penn

I think the team culture, like, similar to broadly at Anthropic, I think the team culture is very valuable. I think Ben sets an incredible vision and pushes people to think about the 10x100x of the idea. And the pods within labs is small. Sometimes these ideas start with one engineer. Right. And I think sometimes when there's almost really large teams pursuing very ambiguous large ideas, you end up actually being slowed down because of that. So I think it's culture. I think we actually also select for folks who actually want to do that zero to one experimentation. And it's not easy. There's a lot of bets that we end up turning down or turning off and maybe, you know, we revisit them in the future. But that's hard. That's hard. When you pour your heart and soul, you're acting as a founder for BET and it's not working yet. So I think it's like that type selecting for that type of personality, folks who are really passionate and deep about the 0 to 1.

[27:30]

Lenny Rachitsky

So you lead product for the research team, you work with the researchers at Anthropic, a lot of people kind of get a sense of what is research, what are research, what researchers do. I think a lot of people don't totally understand these very valuable people at all the AI labs. The way I think about it, and I want to help people understand, help me understand just what are the researchers doing all day. What I imagine is they have a hypothesis for how to improve the model. They find data, they tweak some algorithms, they check, adjust how it's trained and they Test it, see how it did, keep iterating and keep trying to find ways to improve the model. Is that roughly right slash help us understand what researchers are doing all day.

[28:08]

Diane Penn

That's really, I think that's a lot of. Maybe the more day to day. I think one piece around researchers and research organizations like Anthropic is there's also a vision of the future more broadly. So for example, things like, I think even at the founding of the company, researchers were talking about how do we get Claude to use a computer, how do we get AI to navigate a screen? So there's a lot of actually very founder like energy is how I describe it within. Researchers are really bold and ambitious researchers and we have a ton of those at Anthropic. So there's one layer of vision of what this technology can go and then I think on this other side of the loop, there's also now that this technology or clot is in people's hands, how do we make it better today? So it's a medium and long term and a lot of energy thinking about that lens of the future. And also in the immediate and short term, what are the improvement areas we can make. And so I think you're describing a really good sense of how do we make iterative improvements on different versions of Claude. The way that my team works with researchers is kind of being very integrated and embedded in those loops, particularly areas where there's a lot of impact on users. So this is things like vision, computer use, coding, agentic coding tool use, test time, compute things where there's a direct user impact and then figuring out what are the ways to bring the user feedback and ground it in a level that is understandable for researchers and also actionable for researchers. And I think that's the second piece that's actually a big part of the job and sometimes a hard part of the job. So for example, we might get feedback on Claude AI Claude hallucinated. It's very vague. If you bring that to a researcher and you say, please fix Claude from being Hallucinated, it's not very actionable. And so part of the time of the team is understanding, okay, what's the trajectory of why that user gave that feedback? And it's like consented. And so we look at, okay, should CLAUDE have called tools in that moment or from its current knowledge or it called the right, looked at the right document, but it looked at the wrong facts. In the first case that would have been a failure on tool use. On the second case it would have been a Failure on let's say search or knowledge insertion, search synthesis or it could be something around alignment. And so bring that level of detail to researchers. Coming up with like is this a big enough problem figuring out things like evals to then describe what we've improved it like those are the levels of actionability and it's the day to day language of the researchers. And so we try to stay very close to how to bring that in an actionable manner, not between users to the core model training and the research development loop.

[31:36]

Lenny Rachitsky

I was talking to someone the other day about how it feels like research, AI research is the place to be now if you want to be very successful in life. What does it take to become a really successful researcher from which you can tell not everyone can get in, not everyone's brain is going to work this way. But just say people are like hey, I want to explore this career path. From what you've seen, what does it take to, to make it there?

[31:59]

Diane Penn

Researchers generally or research and product managers working with research or both.

[32:04]

Lenny Rachitsky

Let's do both. But the researchers like you know, PM's working researchers also going to be very successful. But it feels like everyone's trying to, you know, poach all the top researchers across every company. So just and I know you're not an AI researcher, but just from what you've seen, just like what does it take to make it in that, in that career path?

[32:21]

Diane Penn

Yeah, I think a lot of the most successful researchers and research leadership at Anthropic are folks who are really strong first principles thinkers about problems. They reason through problems really well, who are just passionate about their research area and have a bold description of what that could look like and then who are actually close to the details. And so our leadership, our chief scientists, our heads of fine tuning and RL folks are actually really close to the training runs and actually look at things like how the training run is going evals looking at the underlying data. So actually staying really close and be excited to be in the details I think have been a sign of really strong researchers and developing taste. And I think another piece is just their ability to think big over time and be very ambitious. The Dario we can transform software engineering and I think going in that direction you learn so much. You had to shoot for the stars in many ways across your ideas eye. I think in order to be a successful researcher.

[33:49]

Lenny Rachitsky

I love just this meme of just be more ambitious comes up so often now which is so hard. It's easy to say that it's hard to actually just like how big can you think and how that so much of what AI now unlocks just be more ambitious.

[34:03]

Diane Penn

I think it's thinking through it once or twice, end to end and then being I think stubborn about the area and maybe more loose around the exact approach. It is a question we challenge ourselves with. But the technology is moving so quickly and so how do you make sure what you're building is actually forward compatible? And so it's also actually part of like I think the core product development loop to think bigger. Right. One thing I ask the team frequently or how I think about when we're building a product is let's say Claude 8 comes around, what changes in what users do and then what does that mean for how you're building today? Is it going to be forward compatible to that experience? Right. So like just grounding it's. I think being ambitious is very broad and so trying to like ground it in, in some ways of describing, describing that.

[35:13]

Lenny Rachitsky

And also yeah, everything heading in a direction that all is cohesive and makes sense versus just ambitious in a completely different direction. Speaking of ambition and Claudia Fable slash Mythos recently feels like hit this very new kind of tipping point with models where it used to be. You have an awesome model, release it. Hey everyone, welcome. Opus 4.5 is out, everyone can use it. Mythos went in a very different direction. It got blocked. There was a lot of scrutiny, a lot of concern about what it was capable of. All the companies had to go make sure it wasn't going to hack into all their systems. And it feels like now every model, because they continue to get better, will now have a lot more scrutiny and there will be more restrictions on who can use them, which feels like a big deal. How do you think about that? How does that change the way you operate?

[36:02]

Diane Penn

I'm going to maybe leave the policy and the export control side to focus on that and work on that. I think the product question and how we interact with these internally is, I think as you mentioned, as frontier models become more capable, the safeguards and the ways of red teaming and testing and the pre release process also needs to evolve and adapt quickly to address that. And so one example is before Fable models we didn't have as strong of, let's say fallback UXS and systems because our goal is to make sure that there is asymmetrical benefit for this technology and to minimize the like the downside or a severe risk of it. And so we ended up building fallback systems so that users will still get a great response from Opus 4a immediately. And so I think there's a piece around as we evolve and improve safety systems, how do we continue to develop and deliver great user experiences? I think there's more that we can do on both sides and so you'll see us innovating, improving on what we call out the model safeguards package more and more in the coming, coming weeks and months.

[37:29]

Lenny Rachitsky

What's really interesting and just like unexpected here is creates this really interesting advantage for anthropic where you have access to the latest stuff and this is going to happen at every lab, everyone's going to keep improving and it's, it creates this unfair advantage within the labs to have access to the best stuff that other people can't. Yet outside of your control, you'd prefer everyone use it. So it's really interesting, this new feedback loop that's going to start where models that are so advanced are only accessible to certain companies and that's going to be a whole new unexpected. It's like a second order effect of all these restrictions.

[37:59]

Diane Penn

Our goal is to be to develop these systems in the models to be as inclusive as possible. I think our goal is to not have that happen for the general purpose, general use like technologies and to make it more accessible. I think, you know, this is like one of our top priorities right now, to kind of reduce what we're seeing there.

[38:21]

Lenny Rachitsky

Yeah, that makes sense. I would imagine you'd want as many customers and people using this thing as possible. This episode is brought to you by Mercury. Radically different banking.

[38:29]

Podcast Sponsor/Announcer

Loved by over 300,000 entrepreneurs and now with command. I've been a customer of Mercury's for over six years. I have never once thought about leaving.

[38:39]

Lenny Rachitsky

Mercury is basically what happens when banking is built by product people, not by bankers. They make it so easy, dare I say fun, to send invoices, move money around, set up virtual cards for folks on my team. Does your bank have an API, a terminal, native CLI or an AI ready MCP server? I don't think so. And just recently they launched Command, a conversational interface built directly into Mercury, which acts as your financial operator. I've been using Command to transfer money around to figure out what categories I've been spending the most money in, analyze my cash flows and just today I used it to find out how much I've made from a specific sponsor over the past year. I just ask how much have I made from X over the past year? 10 seconds later I have an answer. It is so freaking cool.

[39:26]

Podcast Sponsor/Announcer

Visit mercury.com to learn more and apply

[39:29]

Lenny Rachitsky

online Online in minutes.

[39:30]

Podcast Sponsor/Announcer

Mercury is a fintech company, not an fdic. Insured bank. Banking services provided through Choice Financial Group and column NA members fdic.

[39:38]

Lenny Rachitsky

I want to talk a little bit about how the product role is changing and who, who is doing well in this new world now that AI is such a core part of, of our life. When you're hiring PM's product people, when you're looking at people that do well in today's world, what are some things that you noticed? What are you looking for more? Most. What are you looking for more? What's kind of like trending up and what you find is important and what's kind of trending down?

[40:04]

Diane Penn

We actually on my team have not changed our hiring loop for three years now. So what we actually look for and the traits and how we evaluate generalists like pns, generalists like research product managers have actually been the same. So I think some of those traits, number one is first principles thinking. And this is really rather than pattern matching what you used to do in let's say consumer product or B2B SaaS, but actually figuring out in this moment for this user group with this technology, what, what is the user value?

[40:50]

Lenny Rachitsky

Is there an example that a lot of people hear first principles thinking? They're like, yes, I got it, I'm good at this. What's an example of someone having really demonstrated really good first principles thinking?

[41:00]

Diane Penn

I think one example is I think you think of a product manager as I own product strategy and delivering user value, but I demonstrate day to day by writing a PRD or writing a product vision document. And for my team as research product managers, the way to drive user value is to figure out the right user feedback, the evals that then can be a personification of that user need. We do write some product documents and PRDs, but we actually have a saying on the team of evals are the new PRDs because in order to deliver that user value, it's not that exact artifact that people used to write in the last one to two decades. It's a new way of working. And so the first principle thinking would be let me figure out what is the thing I should do to achieve my goals rather than here is a set of activities that I've done and therefore I will continue to do so.

[42:10]

Lenny Rachitsky

The idea here is used to be have kind of an idea, create a prd, talk to people about it, align on the plan, design it, build it, ship it, see how it goes, iterate. What I'm hearing here is it's like, okay, here's some feedback about something that's wrong or an opportunity. Step one is the eval is now how you define what the work is versus a prd.

[42:32]

Diane Penn

Maybe, maybe step one would be understanding the user pain point. And so the way to even access a user pain point is different. Right. In the past we might do a user interview. I think if you go deep enough, you might have the user walk you through their user flow. The pixels here you have to sweat the tokens as much as you sweat the pixels. And so one activity we have on the team is reading the transcripts and understanding what was the trajectories that failed very deeply to then say, was this like a hallucination? Was this Claude being overconfident? So like the theme of the failure actually has a lot of nuance and then that allows you to build a description, a like sustained description of that pain point. So that could be essentially in a new eval. And is the eval on distribution? Right? Is it capturing both the positive situations where this is failing and also areas when it should actually not fail and then bring that back to, let's say, research so then we can make the improvements and actually measure the quality of. Okay, when we have Opus 5.5, is this area improving or not? Is Claude now able to identify the right places in the document and pull the right synthesis out? So it's just the actionability and shorten the distance to actionability for our stakeholders and partner teams, like researchers to take action on.

[44:17]

Lenny Rachitsky

Is there an example of something like this where you found an issue or opportunity and then wrote the eval and what is the eval looking like? In most cases, when people want to picture an eval, what is that? What do they picture?

[44:29]

Diane Penn

We actually pioneered this concept within Anthropic. So one of the early examples is the early cloud models were not very good at following specific schemas. So things like outputs and JSON. And now that is fundamental to Claude being able to be a good agent.

[44:51]

Lenny Rachitsky

Right.

[44:51]

Diane Penn

If you can output a certain format, you don't know how to access APIs, you can't call tools, et cetera. And so the initial end to end was I was hearing feedback around Claude two days. Claude was not very good at following instructions. So then digging in with users, what do you mean by Claude is not good at following instructions? Give me what situations this was happening. What's the exact paragraph? What did you ask? What was Claude's response? Going to that level of detail and what I saw was something like 80% of what people meant in the early days for this failure was CLAUDE would not write the right JSON. And so then, okay, let's generate maybe to start just 30 to 40 examples of when CLAUDE was not doing this thing correctly. Then that actually is your eval set and you could have essentially a prompt and a response. If that is not working in the right golden answer that you might have, then that means that the eval essentially it's beneficial because identifying a pain point consistently. And so then we added that to our repositories for evals and when we have versions of claude, we actually run that eval and just check. I think at this point it's always 100% or like 99.9 and so it's no longer a pain point. But in the early days it was taking the user feedback, figuring out actually what they mean by can we reproduce it, is it consistent, is it a big issue? And then figuring out how to standardize it in a way that can be consumable for researchers.

[46:42]

Lenny Rachitsky

It's basically test driven development for PMs is the world we're living now or you write the test first. So is this just a core part of the product management job now at Anthropic writing emails?

[46:53]

Diane Penn

I think so. I also think it's something I've Talked to other PMs at other companies about and I think it's also more and more of the skillset more broadly because a lot of the products that we're building is at the intersection of models with harnesses, with a set of contacts for a set of users. And so having things like evals actually is a way not just for folks working on models, but generally within product to get to better user experiences because you can't improve what you can't measure. And a lot of this is very still tactile based, it's still very judgment based. And so you have to stay close

[47:37]

Lenny Rachitsky

to the details and also very non deterministic, which is a big part of this. Just like it's not going to give you the same answer every time. So you got to describe it kind of more broadly. It's not going to be an exact match. So this is a really interesting change in the way product happens and will happen is evals. Writing evals versus BRDs is a big part of this. Do you guys still do BRDs? Is there still like a one pager describing a problem or is it replace. Okay, you're shaking your head.

[48:01]

Diane Penn

Yes, we are, we do. I think when there's a very defined problem, I think things like evals Might be almost a shorthand. I think there's other cases where PRDs are really valuable. PRDs are great vehicles for getting a very large group of people aligned on a set of sources of truth about experience and set of goals. So when we do have a model, we actually, for every model we do have a prd. Less necessarily for our researchers, but more for our growing product surfaces, for our engineering teams, for our stakeholders like legal and safety and others as just a source of truth, of putting together what we're aiming to achieve so that a big group of people can row in the same direction. The other place where I do think PRDs are valuable are on the more ambiguous problems and opportunities.

[49:01]

Lenny Rachitsky

Right.

[49:01]

Diane Penn

So if we haven't shipped a thing like computer use, we don't necessarily have a set of user specific pain points always. And I think there's value in the product vision portions of a PRD to explore what could, even if a technology is not yet ready to work for everyone, how do you get it to work well for some group so you can explore the value. You can actually bring something that is coherent to a user group. So we do have PRDs. I think the application's a little different now.

[49:39]

Lenny Rachitsky

Okay, this is great. I just had a Andrew, he's the head of the codex app at OpenAI and he's. You guys are aligned. Peerd is not dead. Still very useful for specific projects and ideas. Great. Okay, we've closed, closed the book on purity is still kicking. Okay, so we've been talking a bit about just what kind of skills are kind of emerging for product people. Is there anything else that you find is shifted in what patterns are common across people that are doing well in this new AI world? In terms of product managers and focus on the product teams, is there anything else that you're like, okay, there's something you got to shift or something you look for more people.

[50:19]

Diane Penn

I think maybe specifically for folks who might be mid career or folks who have been more in a managerial like product like leadership seat. One thing that I think I feel pretty strongly about is in order to be good managers of teams and PMs working with this technology, you have to be really hands on yourself and have spent not just time tinkering, but actually shipping with this technology and again being in the details and sweating the tokens along with your PMs and your engineers and your teams. And so even for folks that I hire who have more tenured PM experience, the onboarding plans are exactly the same as somebody who is like more early career and it's around understanding users, reading like consented user feedback, talking to customers, talking about. I think there's something around being able to understand what to do with this, what good looks like, and having developed that in a very hands on manner, that's important. It's not necessarily easy for someone to agree or be able to see what a good or great AI product or AI feature could look like if they haven't kind of experience building themselves. So I think there is a. I do feel pretty strongly that like, you know, if you're a manager, you have to be hands on, you have to spend a portion of your time actually shipping, you have to kind of walk in the shoes of your teams and that's. I always try to carve out a portion of time to actually like own one to two work streams when we have models. In order to keep my theory of mind, keep my sense of how the models are moving, how quickly it's improving, so I can help the team make decisions and make better decisions.

[52:36]

Lenny Rachitsky

So what I'm hearing here is if you're not, no matter where you are in the ladder of hierarchy at a company, if you're not building yourself, if you're not actually talking to Claude, talking to Codex, building stuff, you're not going

[52:46]

Diane Penn

to make it and you should have fun working with his technology. I think that's the other piece. I think the folks that will be most successful regardless of their level are people who love working with AI and are exploring and experimenting and carving out the time not just for the experimentation, but actually hands on shipping end to end. Getting the user feedback, I think has to be fundamental for everyone.

[53:12]

Lenny Rachitsky

I 100% know what you mean. There just like me sitting on my newsletter in this podcast, just talking about stuff and like, yeah, yeah, that sounds great. Like every time I actually build something and I tinker with all kinds of little projects, you just like, okay, I see what's happening here. And you just get so much more. It's like hard to exactly describe what you're, what you, what you experience actually working with the models and building stuff. But it's like a whole different world of like, okay, I see. Here's what the, here's what they're talking about, computer use. Here's what they're talking about with this limitation of this UX situation. Yeah, yeah. So it's just like, and you made this really interesting point that you have to have fun with it, which is not easy for a lot of people because they're pushed to use AI or they just don't know exactly what to do with it. For people that are just like, I don't know, it's just so annoying. I just have to do this. I don't know, like, I hate this frigging thing. Why do I have to work with this? Things are changing