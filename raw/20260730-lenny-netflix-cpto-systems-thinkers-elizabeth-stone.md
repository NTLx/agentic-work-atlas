---
type: raw
source: "https://podcasts.apple.com/us/podcast/why-netflix-is-betting-on-systems-thinkers-not-specialists/id1627920305?i=1000777423324"
transcript_source: "https://pod.wave.co/podcast/lennys-podcast-product-career-growth-b65486a6-7cff-4966-bbea-2bc239e90aa4/netflix-cpto-on-ai-and-the-future-of-product-and-tech-roles-elizabeth-stone"
title: "Why Netflix is betting on systems thinkers—not specialists—in the AI era"
author:
  - "Elizabeth Stone"
  - "Lenny Rachitsky"
publisher: "Lenny's Podcast: Product | Career | Growth"
published: 2026-07-19
created: 2026-07-30
description: "Lenny's Podcast 第 1627920305 集（2026-07-19，约 1h 6min）。Elizabeth Stone（Netflix CPTO，前 Lyft VP Science、Nuna COO、Analysis Group 经济学家、Merrill Lynch trader）访谈。Vendor 立场：低风险——Stone 是 Netflix 高管，访谈属“组织实践分享”非产品营销；Netflix 非 AI Lab，无产品叙事自利倾向。核心论点：AI 触发角色混乱（“PMs can ship code, designers can write PRDs, engineers can product”），但 Stone 用 Tuckman 团队发展模型（storming → forming）反驳“职能终结论”——craft excellence（great engineering / data science / creativity）仍稀缺。Hiring shift 三大趋势：(1) 从 local business expertise 转向 distributed systems / infrastructure / paved-path builders（AI agent 跨系统操作需要 source of truth data + 中央基础设施）；(2) designers 转向 design systems thinking（建立 templates 让非设计师也能产出统一体验，避免 'Frankenstein' 设计）；(3) generalists / adaptable people 取代 narrow specialists（“fewer specialists and more generalists or adaptable in multiple directions”——specialists 也需更广工具集）。Career ladder overlay 机制：Netflix 不重写每级 ladder，而是在所有 talent 之上叠加 'AI fluency' aspiration（形式因职能/职业阶段而异——experimentation mindset / 知道 AI 何时有用 / 实际用 AI 构建）；coding 面试现在允许用 AI 工具。三件套文化机制——Talent density（不可妥协）+ Accountability（input top people, give autonomy）+ Keeper test（“would I fight so hard to keep you?” 多数情况是 positive 反馈，少数诚实说不 pass）；excellence-as-OS 是这套机制的总框架。Junior talent 仍保留（intern + new grad 项目）——因 native AI fluency + consumer behavior instincts，但需更多 mentorship on 'what good looks like'。Engineering 5-10 年方向：distributed systems + infrastructure + systems thinking；craft 专才（encoding、playback systems）保留，但 mental model 转向“可快速跨域学习”。推荐书：Donella Meadows《Thinking in Systems》——与本文核心论点同构。"
tags:
  - clippings
  - lennys-podcast
  - netflix
  - ai-org-design
  - career-ladder
  - systems-thinking
  - talent-density
  - keeper-test
---

# Why Netflix is betting on systems thinkers—not specialists—in the AI era

*Elizabeth Stone (CPTO at Netflix) · Lenny's Podcast · 2026-07-19 · 约 1h 6min · Transcript from pod.wave.co*

---[00:00]

Lenny Rachitsky

Everyone can be everything now. PMs can ship code, designers can write PRDs, engineers can product. And there's this confusion and frustration of what is my job anymore.

[00:09]

Elizabeth Stone

Anytime a new technology comes along, you go through a storming phase before you go through the forming phase of things. We are in the middle of that right now. I don't think that means we should put AI back into the box and say let's not use it.

[00:23]

Lenny Rachitsky

If we all become builders, will we still need separate functions?

[00:26]

Elizabeth Stone

I still see a craft excellence that's really important that I don't think is going away anytime soon. I still find great engineering to be scarce, great data science to be scarce, great creativity to be scarce.

[00:38]

Lenny Rachitsky

If you look at the early culture deck of Netflix High agency autonomy, paying top of market. This is what I hear constantly now from how the top AI labs operate.

[00:48]

Elizabeth Stone

Netflix's culture has always been excellence as an operating system. It's a resistance to do the thing that a lot of bigger companies would do and to feel comfortable in that discomfort very often.

[00:59]

Lenny Rachitsky

What are the ingredients to make this happen?

[01:01]

Elizabeth Stone

Talent density is the non negotiable. Being very comfortable, comfortable with risk taking in cases where things are not going well, not assume that process is going to fix it.

[01:10]

Lenny Rachitsky

What have you added to the career ladders within this AI world?

[01:14]

Elizabeth Stone

We need more systems thinkers, people who can look across all the business domains and abstract that to. Here's the building blocks we're going to need.

[01:22]

Lenny Rachitsky

How do people learn this small trick?

[01:24]

Elizabeth Stone

Each problem you're trying to solve, step out. One click to the what am I assuming is true about the broader space

[01:34]

Lenny Rachitsky

Today, my guest is Elizabeth Stone, Product and Technology Officer at Netflix. This is Elizabeth's second visit to the podcast. Her first visit when she was just the CTO was for the longest time one of the most popular episodes of this podcast. You'll soon see why this is such a killer conversation, because when we chatted two and a half years ago, AI was only starting to emerge. And as a longtime head of engineering and product and data science, Elizabeth has such a unique perspective on where things are heading and what's worth paying attention to. Prior to Netflix, Elizabeth was VP of Science at Lyft, Chief Operating Officer at nuna, an economist at the Analysis Group, and a trader at Merrill Lynch. Before we get into it, don't forget to check out Lenny's productpast.com for an entire year, free of the hottest and best crafted AI products in the world, available exclusively to Lenny's newsletter subscribers. With that, I bring you Elizabeth Stone Elizabeth, thank you so much for being here. Welcome back to the podcast.

[02:33]

Elizabeth Stone

Thank you. I'm honored to be here once and now twice.

[02:37]

Lenny Rachitsky

That's right. That's a rare. A rare treat for me. I don't know if you know this, but your first visit to the podcast, your episode ended up being my second most popular episode. You're right behind Brian Chesky for the longest time.

[02:50]

Elizabeth Stone

Wow. I. I'm pleasantly surprised and also mildly competitive of how do I get to the first spot? But I'll set that aside for now.

[03:01]

Lenny Rachitsky

This is our shot, Bri.

[03:02]

Elizabeth Stone

Brian's amazing, so I'll let that one go.

[03:04]

Lenny Rachitsky

Yeah, he is. And then there's just like all these fancy AI people that are just coming, you know, coming in hot. So it's been two and a half years at this point. A lot's changed, obviously. AI, something AI is allowing people to do is everyone can kind of be everything. Now. This idea of PM's can ship code, designers can write PRDs, and engineers can product, and everyone's everything. There's a bunch of elements of this conversation. One is that I've heard from people that there's also this kind of confusion and frustration of, like, what is my job anymore? Like, what am I responsible for as a pm, as a designer? Is that something you've experienced?

[03:44]

Elizabeth Stone

I hear it within Netflix, for sure. I think anytime a new technology comes along, especially one that's as transformative as gen AI, you go through a storming phase before you go through the forming phase of things. And I think we are in the middle of that right now. I don't think that means we should put AI back into the box and say, let's not use it, because this is complicating all of our preconceived notions about our roles. But I do think it means we have to be much more thoughtful about how do we get the benefits while reducing the costs. I think it's a great thing that people are experimenting with, how can I develop an idea faster, prototype an idea, put together an initial set of code that would allow us to test it? Do I believe that means anyone should be shipping code to production? That everyone should actually be doing everything? Probably not, but I think that it's good for people to be exploring what's possible. And then, like I mentioned earlier, the benefit of having product and tech teams together is that if the business problem is clear, I think it's okay. And it's healthy for there to be some fluidity in the roles that people play, because instead of having to wait for the engineering team to be ready to be able to prototype something. Product and design can move faster on it, but they should still work with their engineering partner to think about through how should we productize this, how do we scale it, what are the guardrails for it? So I don't think it makes the functional expertise obsolete. I think it means that teams have to be more comfortable with maybe this helps us move faster in a certain direction. From an organizational perspective, things I think about to make this more coherent or less frustrating are some of the things that have to be in place for us to get the benefits rather than the cost. So that includes clarity on source of truth data, guardrails on shipping code to production or testing before we make large changes, thinking about opportunities where we can trust the output of AI versus we should have a process or review that helps us check that we're getting high quality outcomes and the importance of reiterating that humans are still responsible for what happens. So it can be that an agent wrote the code or I helped to do an analysis when that's not really my background. But it doesn't make. It doesn't make people not have the responsibility that comes with what they've created. So I think investing in some of those core infrastructure and practices and reiterating the accountability and responsibility for the outcomes helps to balance some of like what's possible with what we should actually be doing.

[06:28]

Lenny Rachitsky

This episode is brought to you by our season's presenting sponsor, Work OS. What do OpenAI, Anthropic, Cursor, Vercel, Replit, Sierra, Clay and hundreds of other winning companies all have in common? They are all powered by workos. If you're building a product for the enterprise you've felt the pain of integrating single sign on SCIM, RBAC, audit logs and other features required by large companies. WorkOS turns those deal blockers into drop in APIs with a modern developer platform built specifically for B2B SaaS. Literally every startup that I'm an investor in that starts to expand upmarket ends up working with work os. And that's because they are the best. Whether you are a seed stage startup trying to land your first enterprise customer or a unicorn expanding globally, WorkOS is the fastest path to becoming enterprise ready and unblocking growth. It's essentially stripe for enterprise features. Visit workos.com to get started or just hit up their slack where they have actual engineers waiting to answer your questions. WorkOS allows you to build faster with delightful APIs, comprehensive docs, and a smooth developer experience. Go to workos.com to make your app enterprise ready today. What's really awesome about having you back on the podcast is we chatted like before, AI was a massive transformation in the world. So it's a really cool arc that we can explore here. The shift that we've all gone through. Coming back to the roles of the product and ENG teams, I'm curious how much these roles have changed in the last two and a half years. If you think about product engineering, design, data science, user research, which roles have changed most? Which roles have changed least? Like what's most different in the last two since two and a half years ago.

[08:13]

Elizabeth Stone

So you've mentioned some of the things, so I'll reiterate them and then maybe build. So I have found that PMs, designers, data scientists are able to get farther in the product development life cycle before engineering really needs to be front of the line in unlocking things than was true a couple years ago. I say that with some caution because like we were talking about, I don't think it's great to all of a sudden have thousands of prototypes if they're not aimed at this is an important problem to solve for the business, and the engineering partners are aware that we're solving that problem and that designers and product managers are going to take the lead in starting to shape the idea. But it's not working in a vacuum and it's not throwing a bunch of spaghetti at the wall to see what sticks. But when it's the right problem, approach in a thoughtful way with some alignment on that. I've seen product design data science move faster in the direction of let's get to something that's testable on this hypothesis. So that's prototyping, that's writing code. The other thing I've seen as being very valuable is we have a lot of information running around in the virtual walls of Netflix. We have experiments we've run over decades, we have insights from consumers, we have input from stakeholders across the business. And that was a problem that really presented a challenge of how do we get the most out of that long history of knowledge and learnings to say let's apply that to the problem we've got now to move faster in this is a promising path, or this is something that we've learned something about and we could leverage here. And AI is very powerful at distilling information, looking across a broad set of things, doing an analysis around it, getting to the core of here's some insights to start with. I would hesitate to rely on that Exclusively. But I think it's a head start. And I find even in my own work, day to day, instead of sending an email that disrupts someone of, like, remind me, what research did we do in what year and what was the question and what was the test we ran? I can find that almost instantly. Then I can form my own. Here's what I find interesting about this. And I have now skipped a couple steps towards is there something actionable here? So that's data analysis, it's modeling, it's distillation of information. And I'm seeing more people do that to your original question. So instead of that needing to be only the experts who were here for 20 years and saw every experiment or know where to find it, we're now able to do that faster within product and tech, across all functions. And a big unlock for us is our business stakeholders sitting in finance and content and advertising can do that as well and then bring back an initial hypothesis where they want to work more deeply with the data scientist and engineer and so on. So there's something there about the, the hypothesis generation, prototyping, thinking deeply about problems, that feels like it's accelerating and that functions are able to do that in a more fluid way. But I still see comparative strengths. So data scientists are still going to be experts at, can we trust this data? Are we interpreting it the right way? What's the data versus judgment that we should be applying here? A product manager is still going to be exceptional at saying, have we really framed the what of this? Like the problem worth solving is in the right way? An engineer still has a craft around the how. How does this scale? What does high quality look like? What problems is this going to create for us based on how we build and deploy something? So I still see the nuggets of that comparative advantage. It's just that we're able to move more fluidly in a lot of steps that normally we would have blockers on.

[11:56]

Lenny Rachitsky

There's so much interesting stuff here. One is this last point you made something I've been thinking about. If we all become builders, well, we still need separate functions. There's this like, member of technical staff trend that is happening across AI where it's like, all right, we don't have a title. You could be anything. You don't have to be in a bucket. What you're saying here is you believe we will continue to have specialties, product person, engineer, data science designer, while they do more of other functions. There's still a lot of value. And tell me if I'm hearing you correct in having this specific discipline and

[12:26]

Elizabeth Stone

skill and background, I still see a craft excellence that's really important in the disciplines that I don't think is going away anytime soon. Even if there's fluidity or blurring of the work across the functional lines. It goes back to what I mentioned earlier of you still have humans who have to make sure that what we're doing makes sense, we're solving the right problems in a way that is best for Netflix members or business stakeholders. And that if I talk to an engineer, a data scientist, a designer, yes, they speak more languages now than they used to because they have the benefit of these AI tools. But there's still something that is not replaceable when I think about the craft and how they think about what good looks like. And that feels true across all levels. And I still find great engineering to be scarce, great data science to be scarce, great creativity to be scarce. So I yes, some things are easier, but that hasn't dissolved in my mind.

[13:28]

Lenny Rachitsky

Are there functions that you are finding you are hiring more of, like the pie chart, pie expanding, say for engineering or PM or design or something, and then functions you need less of? With AI tooling and LLMs rising, I'm

[13:44]

Elizabeth Stone

not sure that it matches exactly to functions, but I can tell you what we're having. We're seeing more of, we need more of. We need more systems thinkers in a world with AI that looks a little bit different across functions, but I could play out a couple examples. So in our core infrastructure team at Netflix in central engineering, a lot of what made Netflix successful over time was that local teams with specific business problems could move fast to deliver. They very often were not feeling like they needed to be on a central paved path. They built the stack that they needed to solve the problem and have the impact. In a world of AI with agents operating across multiple systems wanting source of truth data, the importance of having preferred paved paths that get the most of the benefits and produce some guardrails so we can make sure we're doing good work. Common infrastructure, common paved paths. Solving problems once with a core set of capabilities becomes more important. So we are hiring more people who can look across all the business domains and abstract that to here's the building blocks we're going to need in a world with AI. So that's one of the lenses, but also just with a lens of what got Netflix here doesn't get Netflix there and we're going to have to have a stronger set of infrastructure to move quickly in this future so that Means that engineering profiles are more distributed systems, more infrastructure, more of that system thinking mindset than a local business expertise. Though of course we still have people who are deep in personalization and advertising and content delivery. So it's more something additive for us to have that core, core infrastructure and systems thinking. If I take another example, like design, it's extremely important that our experience design team is developing templates and again systems thinking for what does great user design look like at Netflix so that they can enable lots of people, including those who are not designers by training, to develop products that are coherent, that fit into the end to end member experience. I get really nervous about having different design languages or different types of user interactions and shipping. Frankenstein's basically. So designers need to then be the people we're hiring again for design systems thinking how do we think about templates and expression of the brand and what a good user experience looks like and what is Netflix and like the Netflix differentiated special sauce. So there's more people on our design team that have to think that way now than could I help to design a specific feature for a specific product. So there's this stepping back to look at the big picture that I think is happening in every single function and that requires some reorientation of skills among the existing team and also hiring people who've got that type of expertise. And across all of it, it's a mindset shift. So we are not hiring people who are not excited to explore, try new things, understand lots is changing and feel comfortable with that ambiguity, be comfortable that there's a blurring of how we work and how we partner. That's true for people who are already at Netflix and people who we are adding to the team that that curiosity innovation mindset has not. It's not been more important, at least in the time that I've been working

[17:21]

Lenny Rachitsky

in this field on the system's thinking piece is the reason this is becoming more important that people are moving so fast that you need to invest in platforms and frameworks and design language and basically teach people to fish so they can not be blocked. Or are there other reasons?

[17:38]

Elizabeth Stone

I think it's probably velocity. So platforms do have a benefit of leverage. So in general that's an opportunity with or without AI for a platform to get most teams 80% of the way there and then they don't have to reinvent those building blocks. We have more bets that we're making across the business, more things we're trying to build. So platform mindsets are good and it's something that is Relatively more recent for Netflix to think about that being a real critical enabler. There is also the sense of a scaffolding in a world of AI. So not just the higher velocity, but you have more people doing more types of work that are different or new like we were talking about. And there's risk that comes with how do you think about access and identity in that situation? How do you think about security in that situation? How do you think about shipping high quality code and design and user experiences? And so I don't think it scales well to have each person who's building something have to go figure out, could you remind me what good looks like here and what are the bumpers or guardrails I should keep in mind, I think we need to encode that in our paved paths and our ways of working. And for a data science or analytical field to encode. Here's the source of truth data, here's how to interpret it, here's how to access it, here's what to do with it or not to do with it. And to be careful with certain types of data. An organization that has thousands of people can no longer rely on tribal knowledge or I'm going to find the one person who knows this. So this was a challenge that was there before AI. It's probably a more urgent challenge with AI and, and I like the idea of using AI or any new tech to motivate. Like we knew this is work we needed to do. No time like the present to invest in that more heavily across the team.

[19:27]

Lenny Rachitsky

I wonder if another reason for this becoming more valuable is because agents are now doing a lot of work and giving them the context, giving them the scaffolding, giving them the design language, just speeds all that up.

[19:38]

Elizabeth Stone

Yeah. And one of the visions we have at Netflix is we will have so many agents that are contributing to doing work that you need to be able to reason and rationalize throughout that, you know, the humans are the ones guiding what's the problem we need to solve. Do I feel like what we're producing is impactful and high quality output, but the work will be done by both humans and agents and that creates velocity and benefits and it creates risks. And I think that's important from, especially from an engineering perspective that we figure out how to manage that in a way that lets people move quickly but doesn't create undue downside or risks for the company.

[20:21]

Lenny Rachitsky

This connects so directly with Ginny Wen was on the podcast. She was head of design for Cloud Code and cowork and had this whole design Process is dead kind of thesis. And the pitch there is just there's no time for design, the design process. And instead as a designer, you're just kind of steering people and pointing in the direction and adjusting and also thinking big pictures when you have the time. And it feels like that's kind of what you're describing here is like create the platform for people to move fast and then there's no time for like design process of a specific new feature.

[20:51]

Elizabeth Stone

I have mixed feelings about that because I We do want to enable with infrastructure and systems thinking more people to do great work with strong design as part of it. Why not take that opportunity that the new tech provides? But for our most important priorities, design is critical to solve things in the right way. So we do still make time for important design work. It can move faster. The designers themselves have more tools in their toolkit so they can do incredible work at a faster velocity, show more options, learn iterate, test more quickly. But I think it would be a mistake to say design and deep design expertise and thinking gets squeezed out just because we can write code faster, we can do data analysis faster. That feels like, at least for a large scale consumer product like Netflix. I feel like we would lose one of the things that makes Netflix great, which is the product. Technology and design makes a lot of complexity invisible and makes for a seamless customer experience. That that's a design mindset that has to be core to it. So the work itself might look different, but I don't think we lose the mindset.

[22:06]

Lenny Rachitsky

That's an awesome counterpoint. So what I'm hearing is kind of trending up. Skills, attributes. You look for systems thinking and this kind of mindset of being comfortable and excited about change and what's coming and not being stuck in your own ways. What are you finding is trending down? What are you less looking for that you used to value more highly?

[22:28]

Elizabeth Stone

The days of very narrow, deep specialization feel more limited to me. I can come up with examples where we still need it because there's an industry or technology expertise where there's only a few people in the world who really know how things work. We have examples of that on the team for encoding or how our playback systems work and things that have been incredibly innovative and novel for Netflix. I still believe we need specialized practitioners in those spaces. But as a general rule, compared to five or ten years ago, I would believe we have fewer specialists and more people who are generalists or adaptable in multiple directions. And that could be adaptable across functional expertise. It could be Adaptable across flavors of engineering. So can I navigate both back end and front end systems? Can I hook into infrastructure with a lot of expertise? I think the mindset now needs to be I can learn that quickly. And that goes back to the systems thinking. So I think specialists can learn to have a broader array of tools more easily than was true in the past. So we need fewer of them perhaps because talent's able to grow in that direction. And there's something about sticking to a narrow specialty that maybe triggers for me a concern about what? About the mindset of growing in different directions and exploring. And I don't want to be too narrow even in my own assessment of that. But I it's important that people who are specialists still have that sense of I want to try a new way of solving these problems versus the way we have in the past.

[24:13]

Lenny Rachitsky

And when you say specialists, are you thinking like front end? I'm a front end engineer versus a back end? Or is there other?

[24:18]

Elizabeth Stone

Or it could be a domain set of knowledge of payments expert. I'm a payments expert. I'm an ads marketplace design expert. I am an expert in this very specific tooling that studio productions use. So their specialist and subject matter expertise is an advantage provided that person is willing to grow and extend into Is this really still the right tool or the right way to think about the problem? So I think it's the layers of the stack from an engineering perspective that there's less specialty and then tools that are unlikely to be static or to have a lot of inertia around them. I would think we would want people who are able to innovate and imagine what's the future version of this. And so we want more talent like that.

[25:10]

Lenny Rachitsky

Awesome. So coming back to the systems thinking piece, people hearing this are like, okay, I got to work on my systems thinking skill set. How do people develop the skill? Other is it just do it for a long time? Work at a lot of complex projects. Like I think of this book that everyone always references with a slinky on the front. Thinking in systems. Yeah. How do people learn this small trick?

[25:34]

Elizabeth Stone

Each problem you're trying to solve, step out one click to the like. What am I assuming is true about the broader space in solving this problem? So I was given a task to build some new feature for the Netflix member experience. Let me take one beat and think about what is the bigger consumer problem we're trying to solve here? What's the type of content that this feature is going to be able to support? Do I think that the way I was planning to build this is going to make sense in a way that scales across multiple content types, or it could be something that's a capability that then is contributed to a platform set of offerings from multiple areas. Is the consumer problem that I'm solving with this feature going to be one of the most important consumer problems that Netflix is going to need to solve as we have an expanding world of entertainment and we want to make it more personalized and immersive? Those are all questions that like, you don't have to boil the whole ocean, you don't have to solve for Netflix's overall strategy and who are we relative to competition. But you take the thing you're responsible for and you just do one. Zoom out of the problem you're solving and question that. I wouldn't spend too long in the questioning state because then you're stuck, then you're not making forward progress. But I think that helps people to think in terms of systems and question that are we solving the right problem in the right way that matters for the end consumer?

[27:07]

Lenny Rachitsky

Another way, as you describe it, another way I'm thinking about it is like think if you were your manager, how would they. What's their broader perspective across not just your one team and problem and KPI, but the larger picture?

[27:19]

Elizabeth Stone

I've got advice over years that is similar to that, which is are there ways that I can do my job that helps my manager do their job? And so if I thought about all the things I'm directly responsible for, but I thought about it from the perspective of my manager, so not just product and tech, but finance and content and other parts of the business, I would naturally zoom out and think about how all these component pieces need to come together and how the whole could be greater than the sum of the parts. I think that's useful thinking and for engineers to think about how do I leave a better version of these systems? How do I think about the thing that's going to be high quality and scale for others? There's both a how do I help my manager? And there's how do I help my colleagues, which is a core part of some of our engineering principles of do the thing that is right for the broader organization instead of just what's right for you locally. That's systems thinking as well. So it's not just seniority, but it's breadth of the way I solve this problem and I build this. Is it going to be useful to my colleagues and am I going to leave a stronger version of things for the future set of innovations that we want to make.

[28:25]

Lenny Rachitsky

That is awesome tactical advice. Making your manager's life easier is always a good a good tactic career wise.

[28:31]

Elizabeth Stone

Several reasons.

[28:32]

Lenny Rachitsky

Yeah, following the thread a little bit, I know you all added career ladders and levels recently. It was like a new thing. You used to not have these things. So kind of on that thread, what have you added to the career ladders within this AI world, if anything that you find you want people to lean into more, you're looking to more or not. Like, did you not change your career ladders and performance criteria?

[28:59]

Elizabeth Stone

So the way we've approached this so far is instead of trying to articulate at each level exactly how AI changes those expectations, to instead put an overlay across all of the talent at Netflix, people on the team and those who are hiring to talk about an aspiration for AI fluency and what that looks like is going to vary by function. It's going to vary based on where you are in your career. That could be what level you're in or what type of role or Persona work you're doing. But the aspiration for AI fluency, which is a tough thing to define. So does it mean that I have an experimentation mindset? Does it mean that I know where AI is useful and not useful? Does it mean that I've actually built things using AI? I feel like the way that has shown up in career ladders and how we talk about it evolves almost by the quarter, if not month or day because the tech itself is advancing so much. So the most useful thing is not to make it level specific or role specific, but to encourage everyone towards the expectation on AI fluency. Which doesn't mean use it as a tech for the sake of tech. It's tech where it's useful to have good judgment about that and to have the mindset to be open minded to a explore and try new things. That's the non negotiable for all roles. And that's true at the senior most levels of Netflix where we talk about we too need to have deep fluency in AI even if we're not writing code as part of our day jobs. So that's changed and then that's showing up in our hiring practices as well. Getting comfortable within interviews exploring how are people thinking about AI or technology, what are they using in their day to day or their current job, how comfortable are they with change and exploration and even for things like coding interviews, allowing candidates of course to use AI tools because that's going to be part of what the work requires now. So those have been shifts that we've made, but I doubt it's a shift that's done versus we're right in the middle of it.

[30:59]

Lenny Rachitsky

I'm just going to keep following this thread. Obviously AI is transformative for coding. It's a big unlock for prototyping. Are there other use cases of AI at Netflix that have been really impactful that people may not think about or not realize?

[31:16]

Elizabeth Stone

So there's two that come to mind. So the first is data analysis, distillation of information modeling, which is, you know, using the tools to get our arms around all the insights we have. Similar to what I mentioned before. What experiments have we run? What are the metrics that I should be looking at for a certain problem? What's the consumer research that we've done? And that is much higher velocity and much higher quality contingent on you Check that the results are valid. You work with your local data scientist on am I using the source of truth data on this? But that's been a great one and that's one personally that I would say I most use some of these tools for. So that goes beyond prototyping and coding to general analytical thinking and translating data to action and insight. The other one is on the content production creation part of the business, which has lots of applications. This was true before Genai. So ML and AI were deeply used in a lot of the production tools. We've used them to think about how to create promotional assets at scale, how to localize in subtitles and dubs. So Genai is a big step function in where the impact can be in creative ideation. We call those things like pre visualization or basically bringing a creator's vision to life before you even get into the you bring people to a set and start to actually go through the production itself. There's lots of use cases in post production. So we recently acquired a company, Interpositive, that was started by Ben Affleck that built a set of models and capabilities that allow you, after you've shot something to relight, reframe, reshoot, change, dialogue in ways that are very impactful to get higher quality content are still led by the filmmaker creator saying, you know what, I would like to try something else to bring this vision to life. But that impact is extremely promising and we're seeing lots of productions leverage different tools, some of them built in house, some of them that we enable through other vendors for those content creation use cases. And then as we think about how content comes to the product, I mentioned localization, subtitles and dubs, but also how we create high quality trailers, images, artwork at scale that then we can use to help make sure that titles find their audiences around the world. Those all are huge levers when we think about the AI impact. So that that again goes well beyond prototyping or coding to some of the creative use cases. And you can imagine that just like they work for studio productions, for film and tv, they work for advertising, they work for marketing, off service campaigns. And so those are all areas that we're exploring.

[34:01]

Lenny Rachitsky

This episode is brought to you by Mercury. Radically different banking loved by over 300,000 entrepreneurs and now with Command. I've been a customer of Mercury's for over six years. I have never once thought about leaving. Mercury is basically what happens when banking is built by product people, not by bankers. They make it so easy, dare I say fun, to send invoices, move money around, set up virtual cards for folks on my team. Does your bank have an API, a terminal, native CLI or an AI ready MCP server? I don't think so. And just recently they launched Command, a conversational interface built directly into Mercury, which acts as your financial operator. I've been using Command to transfer money around to figure out what categories I've been spending the most money in, analyze my cash flows. And just today I used it to find out how much I've made from a specific sponsor over the past year. I just ask how much have I made from X over the past year? 10 seconds later I have an answer. It is so freaking cool. Visit mercury.com to learn more and apply online in minutes. Mercury is a fintech company, not an fdic. Insured bank. Banking services provided through Choice Financial Group and Column NA members fdic. You mentioned how Netflix has been very early to AI and ML for a long time. Younger people may not remember this, but y' all had this contest to optimize. Yeah, the Netflix prize. Like, like just show an example of how early you were to AI and ML people. There was, I think it was a million dollar prize to optimize the Netflix ranking algorithm a little bit like whoever could optimize it the most. And I think the winner optimized it by a few percentage points. Something like that. And it was like a huge deal. All these super smart people got around, around the world. And it happened a few times. Right?

[35:49]

Elizabeth Stone

I mean you said it on my behalf. Often when there's questions about how is Netflix thinking about AI? It's great to remind people of exactly that point, that this is not new to us, that Especially for personalization, it's been central to delivering a great experience to members. It's impossible to take the breadth of content that we have. There's ever more content. That's one of the challenges we face. And make discovery easier and easier and easier, which is one of the challenges that Netflix has. And using AI and ML has been a way to do that. You want to personalize right title for the right person at the right moment. That problem gets harder. The more exciting our catalog gets, the greater breadth of content we have. Not just film and tv, but games and live and podcasts. Personalization becomes even more important and what that experience is. So we can take a lot of that history and say, okay, well, now how do we solve this problem? Because the tech is even more powerful. But it gives us a running head start in being clear about the problem to solve how important it is that Netflix solve that for our members. And then the same is true. As I was mentioning, on the creative side of the house, AI and ML have been in things like visual effects or in localizing language for a long time. Now we say, what's the next era of that when the tech is more powerful? And in both cases, it ends up taking a strength that Netflix has, which is marrying entertainment and technology and making sure we stay ahead of the game to deliver things that are even better. So I love that it's part of our history. It still continues to be a strength, and it's going to have to be a strength given the size of the challenges we're facing around the breadth of entertainment while keeping a great experience.

[37:33]

Lenny Rachitsky

Yeah. And I love that back then it was called machine learning, and AI was like, no, no, this is not. It's not AI. AI is never, never, never, never going to happen. It's just machine learning.

[37:41]

Elizabeth Stone

Well, then all of a sudden we call everything AI and some of it's machine learning.

[37:46]

Lenny Rachitsky

That's right.

[37:46]

Elizabeth Stone

So I tried, you know, it depends, like the thing that is of the moment to describe. So I think we bucket all of it as AI now.

[37:55]

Lenny Rachitsky

Yeah.

[37:55]

Elizabeth Stone

And there's a lot of AI use cases that are not generative use cases. So we could go down a deep, dark hole of all the specific things. But in general, I don't think it would surprise anyone that Netflix is using a broad array and with so much excitement about what's possible. The fun thing at Netflix for the people who work here, is that if you're really passionate about the applications of tech, for creative outlets, for consumer products, for infrastructure, we have all of those problems and AI is at the center of them and it's good not to forget that that that's true. Even if Netflix isn't branded as an AI company, AI is a tool that we're very comfortable using to get these great entertainment and technology outcomes.

[38:38]

Lenny Rachitsky

The other really interesting thing, just to kind of keep complimenting Netflix here. If you look at the early culture deck of Netflix and also our conversation last time, things that emerge from that are things like high agency. This was like something core to Netflix in the beginning. High agency autonomy, high talent density, very bottom buzz up thinking, super quick experiments and launching paying top of market. This is all stuff that every AI like. This is what I hear constantly now from how the top AI labs operate. So we're all ending here and this is where Netflix has been forever.

[39:13]

Elizabeth Stone

Yeah, it's a little prescient in understanding what makes talent incredible. I've thought about all those aspects of the culture at Netflix as this is going to sound a little bit nerdy, but excellence as an operating system, the goal of all those cultural elements wasn't the end goal in themselves. It wasn't, let's just make sure people have as much responsibility as possible. Or we don't like process, so let's make sure that we don't have any of that. It was instead a very strongly held opinion that the you get to excellence by giving people a lot of agency and accountability, by pushing decisions as deep in the organization as possible, hiring great people who can be trusted to have good judgment and make good decisions. And that ends up driving incredible outcomes, plus a lot more motivation and sense of responsibility. It means every person on the team can feel like I'm being given a lot of keys and a lot of accountability for what happens here. And I myself feel like when you know you're carrying that level of trust and accountability, you want to do your best work. And so there's something that feels very intuitive about Netflix's culture has always been aiming at excellence. And when you have great talent and you give them the ability to do their best work without micromanaging it or drowning it in process, you actually get much better outcomes. And so I do think that the newer era companies are picking up on something that is feeling very familiar to us and it's not something that comes easily. So having culture is not a static thing. Culture needs to grow and evolve. As the company gets bigger, the types of problems you're solving change. But the notion that we're going for excellence and trusting that exceptional talent needs to be able to do their best Work that's unchanged and something that I think continues to be a special sauce for us.

[41:11]

Lenny Rachitsky

I love this concept, excellence as an operating system. It's very systems thinking, you might say, for how to set up a company.

[41:18]

Elizabeth Stone

Exactly, Lenny.

[41:21]

Lenny Rachitsky

So for people that like everyone listening to this will want excellence as an operating system, like, who would not want this? It'd be helpful for people to hear what are kind of the ingredients to make this happen. One is obviously high talent density, just hiring only the best. Two is accountability. Kind of there's like the input and the output essentially. Input amazing people, top the top people, make them accountable, give them autonomy. What would you say? Kind of like the pillars of creating this excellence as an operating system. If people, if founders are listening to this, like I want them to do that.

[41:51]

Elizabeth Stone

Well, the talent density is the non negotiable. You have to start with that. If you don't have that, you can't get to a place where you have confidence in decision making at all levels of the organization. Allowing people to take risks and innovate quickly. That's a big part of excellence in the Netflix culture, which is being very comfortable with risk taking. We don't try to avoid failures, we try to recover quickly when we have them. I think there's been great examples of that. Our foray into live was a wonderful example of being comfortable, taking a ton of risk, knowing it would be imperfect, knowing we would learn fast and we would be better for it. I've never been prouder of the team, seeing how we worked through that. So you have to be talent density, comfortable that people are going to take the context that you give them strong judgment and risk taking and fight for the things that are the best outcomes for the business. You have to be very clear that what you're doing is driving outcomes for consumers and Netflix. So it's Netflix matters. Netflix members matter. It's not about my own personal success or what I prefer. So there's a selflessness that is part of this excellence operating system. And then the other thing I would say is some of the things that are. They're really unnatural for humans to do. So I could give a couple examples of things to get comfortable with, which is there are certainly days where I see decisions happening and I think I would make a different decision, like, is that really going to be the best thing? But my job, especially in the Netflix culture, is not to step in in every one of those cases and overrule or veto or question someone, especially if it's not material, it's not going to burn the place down, let people make that decision and learn from it and ask for those reflections afterwards of like, how did it go? Maybe I was wrong, maybe the decision was a great one, but that it's related to the risk taking and the like. Help people learn how to feel comfortable making their own decisions, especially when they're not all going to be the right decisions and they're going to learn something tough from it. I felt that myself, from my boss and my peers saying, this is your decision. You know, I can provide input, I can help you brainstorm. It's yours in the end. And it just doesn't come naturally when the stakes are high. When I feel responsible for what the org's doing. To let people lean into risk can be uncomfortable. And I think that also means in cases where things are not going well, as another example, to not assume that process is going to fix it. So if something I've learned over the past few years that when planning is difficult, I've never heard someone say, like, oh, we figured out the perfect way to plan or the perfect way to go through feedback and leveling and compensation. But every time we saw that and we added more process, we spent more time without getting better outcomes. And so it's another unnatural thing that I think everyone's inclination when things are hard and complicated is you think you're simplifying the problem by putting a lot of constraints around it, but it actually goes against the like, is there a more creative way to plan or to make people decisions or to make prioritization decisions that actually get us to better outcomes? And so it's a resistance to do the thing that a lot of bigger companies would do and to feel comfortable in that discomfort very often. So that's something I feel in my role and I would believe a lot of people at Netflix feel it because you try not to do the thing that is standard.

[45:39]

Lenny Rachitsky

It's easy to say that and hear that, but I so know what you mean where somebody screws up and you're like, okay, what was the thing that went wrong? Let's put a process in place to avoid this from happening. And what you're saying is like, you need to resist that because that slows things down. And the best people don't want to be working in a place with all these checklist and processing gates and things like that.

[45:59]

Elizabeth Stone

No, I think the best people want to know there's going to be a blameless retro and they're going to feel so individually responsible that they're going to say, how Do I make sure this doesn't happen again? Not with process, but with, like, how could I share these learnings? How could I do work differently to make sure that I get to a better outcome next time? When you are trusting people to take those reflections and learn and grow, I think you get much better outcomes over time and you get a much stronger team, which I think is part of our role as leaders of like, you're trying to grow a team that is resilient and durable and knows how to have great impact. You're not trying to control everything, which

[46:42]

Lenny Rachitsky

is a key to building a team with high talent density. There's kind of. There's two sides to this that I want to chat about briefly. One is the hiring and the other is keeping the people. So you're famous for the Keeper's test. We talked about this last time. Another unnatural thing for people, people that want to understand what this is, they can listen to the first conversation. But has that. How has that evolved over the last couple of years? That's still a core part of the culture, this idea of the Keepers test.

[47:06]

Elizabeth Stone

It's often cited in a way where you think of Keepers test as that moment where you decide to let someone go, that they're not the right fit for the role and the conversation about that. But it's equally commonly used to have a conversation about how extraordinary someone is, how well they're doing in a role. Because the entry point is for me to say to one of my direct reports, or for them to say to me, how am I doing on your Keeper test? And the lion's share of the time, my response is, I would fight so hard to keep you. Let me go through a set of things that I think you're doing such a great job at, what your strengths are, where you're having a lot of impact. Here's how you could be even better. So it's an entry into a conversation that is very positive and uplifting for people. But the framing is, do I pass the Keeper test? And then of course, there's the harder situations where I'm evaluating, does someone pass the Keeper test? Or they're asking me and it's. This is the toughest thing to say, to be honest. You're not passing that right now. I think you