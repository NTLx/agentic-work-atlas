---
title: "Jeff Dean: The 1% Rule for Building in AI"
source: "https://www.ycrootaccess.com/p/jeff-dean-the-1-rule-for-building"
author:
  - "Root Access"
published: 2026-07-30
created: 2026-08-31
description: "Google's Chief Scientist on specialized hardware, context engineering, and where two or three people in a room can still beat a frontier lab."
tags:
  - "clippings"
  - "agentic-engineering"
  - "context-engineering"
  - "AI-Agent"
  - "startup"
---

*Google's Chief Scientist on specialized hardware, context engineering, and where two or three people in a room can still beat a frontier lab.*

In 2001, Jeff Dean and Sanjay Ghemawat did the math and realized Google’s entire search index would fit in RAM — then shipped it in a few days, and search got fast. In 2013, another napkin calculation showed that three minutes of daily speech recognition per user would require doubling Google’s server fleet; that one became the TPU. At Startup School 2026, Google’s Chief Scientist talks with YC’s Diana Hu through the thought experiments behind both, why inference hardware is the next specialization, and where two or three people in a room can still win.

[Watch on YouTube](https://youtu.be/CxXgV54KzpQ)

### **Timestamps**

00:07 — Are AI Models Already Junior Engineers?
01:44 — AI Systems That Improve Themselves
02:40 — The Google Search Breakthrough That Changed Everything
04:38 — AI Agents Will Run for Weeks
05:58 — The Napkin Math That Led to TPUs
09:20 — How to Find Breakthrough Ideas
10:25 — The AI Engineer’s New Mental Model
12:33 — Why AI Is Really an Energy Problem
16:11 — Context Engineering Is the Next Frontier
19:46 — The Skill That Made AI Better at Optimization
22:13 — Why Long-Running Agents Fail
25:21 — Where Startups Can Still Beat Google
31:19 — How to Become an AI-Native Founder
36:36 — Question Your Biggest Assumptions
42:08 — AI That Builds Better AI
50:02 — Build Something That Truly Matters

### **Transcript**

**Diana Hu:** All right. Should we get started, Jeff?

**Jeff Dean:** Sure. Sounds great.

**Diana:** All right, Jeff, welcome. And again, thank you so much for being here, especially you just got a cold and thank you for being here.

**Jeff:** Yeah, I’m afraid I’ve lost my voice. I don’t normally sound quite like this, but we’ll do what we can.

**Diana:** So you built MapReduce, BigTable, TensorFlow, the TPU, Gemini. We could spend a whole hour on all the things you’ve done, but what I love is that you’re still making bold predictions in public. Last year, yes last year, in May 2025 at AI Ascent, you said that AI is at the level of a junior engineer. That was about a year ago. How close are we to that prediction?

**Jeff:** Yeah, I feel like the models have been getting a lot better at agent-based, longer-running coding tasks, and it seems pretty clear that they are now actually pretty capable. And depending on exactly your definition of junior engineer, it seems pretty spot on, I would say.

**Diana:** What did you underestimate from that prediction?

**Jeff:** I think the ability to do more and more complex tasks has been growing faster than I thought. And I also think outside of coding, these agent-based systems are really starting to shine in other domains. And I think that’s going to be an important trend in the future.

**Diana:** So give us another bold prediction. What do you think is going to be the 2027 edition?

**Jeff:** I think you will see a lot more automation of ML systems themselves, basically getting ML systems to improve their capabilities by running lots of experiments, breaking things down into sub-problems, running those sub-problems in a tight automatic experimentation loop, putting the results together, and being able to then get some improved system out from that fully automated problem decomposition and automated experimentation. I think that’s going to be really exciting. I think that also applies not just to ML, but also to other fields of science and engineering. Basically anything where you can have a measurable objective. I think you can actually make a lot of progress these days.

**Diana:** Now let’s go back a little bit in history. Way back in 2001, Google search used to run on hard drives. And you and Sanjay did the math and realized that at some point the whole search index would finally fit in all of the RAM of all the computers you had running. And you made that radical realization, and you basically, in a few days with Sanjay, shipped in production a whole new search version that worked in RAM rather than hard drive. And that was the thing that got Google to be so fast: Google searches. So history tends to remix. What is the ‘it fits the memory’ moment right now in 2026 that everyone in this room should be thinking about and designing?

**Jeff:** Yeah. It’s a little different, but I think you’re going to see more and more high-performance and low-energy inference hardware systems. Because I think everyone is now realizing that inference is the key to making these agent-based systems be available to more and more people. And that latency is really important, and that specialization of the hardware is a really key way you can make things that are more energy efficient and lower latency than more general-purpose computational devices like, say, GPUs or TPUs.

**Diana:** Because I think everyone here is used to waiting for responses on models.

**Jeff:** Waiting’s no fun.

**Diana:** Master of speed. So you’re saying, what if we don’t have to wait anymore?

**Jeff:** Yeah. Imagine what you could do with something where the latency is 50X better.

**Diana:** Interesting thought. Now, what’s one assumption that perhaps 6,000 people in this room hold as already false about AI?

**Jeff:** Yeah, that’s a good question. Probably one thing is people don’t quite realize how possible it is to have agent-based systems that can run not just for an hour or two hours on a problem you care about, but for some problem domains and with highly capable models underlying them, you can get them to run for days or weeks and do really, really complicated tasks. Some people are starting to see inklings of this, but I don’t think everyone has really internalized it. And that’s going to be a pretty big deal.

**Diana:** What’s a particular task that you have run that has run for weeks? What did you tell the agents to solve?

**Jeff:** You can tell agents to go off and implement completely new versions of software in different programming languages that might have better safety properties or better performance properties. And then they can go off and actually do that in a pretty serious way.

**Diana:** That’s pretty cool. Now, one thing that you’ve been very well known for is you’re really good at napkin math. Sounds funny. So one of the stories about you is that back in 2013, when speech recognition started to work at Google, you did the napkin math where if every Google user used their phone and talked to it and used the speech recognition system for just three minutes a day, you found that the system requires a Google server, you would have to double the fleet, which would be really, really expensive just to do speech translation.

**Jeff:** Yeah.

**Diana:** And instead you basically built a custom chip, and that was the origin story of the TPU.

**Jeff:** Yeah. We were starting to see really good quality results on the deep learning-based speech systems, speech models we were training, but they were computationally expensive compared to the old speech system, but they halved the error rate. So that was the equivalent of 20 years of advances in speech recognition in just a few months of fiddling with the model and scaling it up a bit and getting better data. We started to get worried that if speech worked a lot better, people would use it more. That back-of-the-envelope calculation was really about that. What if people start to use speech recognition more to dictate emails or to talk to their phone or whatever? It turned out that we realized we needed some better solution than running on CPUs at the time.

And so we came up with TPUs, which are very specialized for essentially low-precision dense linear algebra, which is at the heart of nearly all of the modern machine learning algorithms we use today. If you build a specialized chip for low-precision, dense linear algebra and can’t do anything else, that turns out to be really useful for machine learning inference, even though it can’t run Chrome or Word or whatever. That system produced a chip a couple years later that was 30 to 80 times more energy-efficient than CPUs and GPUs of the day. And also much, much lower latency, like 20 to 30X lower latency.

**Diana:** Which is incredible, what the foundation that TPU has become today. No way you would’ve predicted that TPU would be so foundational now with transformer architecture, which was invented way later, before you actually invented the TPU.

**Jeff:** Yeah. That’s why we built a general-purpose linear algebra system, which is what a TPU is, really. We knew ML algorithms were still evolving, and you didn’t want to overspecialize, but you wanted to specialize enough that you got the dramatic performance benefits of very big multiplier units, high-speed memory, and high-speed interconnect for later TPUs that brought many chips to bear on the same problem efficiently. We’ve continued to scale those up and improve their performance over many generations now.

**Diana:** Incredible napkin math. Napkins are good. So actually, what’s a good napkin math that everyone here who wants to be a future founder should run tonight to potentially build something as consequential as the TPU?

**Jeff:** Yeah. It’s always hard to say. Think about what problems you see in whatever it is you’re thinking about, what bottlenecks you see. Are there very different ways of thinking of the solutions to some of those problems that would get you an order of magnitude or two orders of magnitude better performance or capability or whatever it is? Sometimes if you just squint at a problem and think about not necessarily being anchored on exactly how that problem is solved today, but how you would solve it from first principles, you can come up with really good ideas that are maybe not what other people are thinking about.

**Diana:** That’s a good tip. Now for everyone here who doesn’t know, years ago, Jeff wrote a very famous list called The Latency Numbers Every Engineer Should Know. These are numbers around, for example, how long a cache miss takes, disk seek, a network packet traveling, let’s say from California to Netherlands. Lots of numbers like this about distributed systems and systems engineering. It’s been taped up and become the Bible for a lot of distributed systems engineers.

**Jeff:** Okay. Yeah.

**Diana:** Now, fast forward, that list is up for an update. Give us the AI edition for now, 2026.

**Jeff:** Yeah. If you looked at what is important in AI systems these days, you would want to know things like the bandwidth between your main memory system on your accelerator, to the on-chip memory, to the multiplier unit. You want to know how much energy it takes to do a single multiplier operation. What is the interconnect bandwidth between chips? How many chips can you connect with that bandwidth? If you go beyond that domain, what is the falloff in network bandwidth when you need to talk to 10,000 chips instead of 500? I think these are all really important numbers to learn and really affect how you think about solving particular kinds of problems.

**Diana:** And one interesting thing that I’ve heard you talk about is that nowadays, the unit that you measure everything is energy.

**Jeff:** Yeah.

**Diana:** You pointed out that doing a calculation of math costs about one picojoule, but moving the data and doing data IO costs a thousand times that.

**Jeff:** Yeah. Just bringing it in from HBM on an accelerator into the processor so it can actually compute on it. Yep.

**Diana:** That gap quietly decides what products are possible and how these algorithms and AI are built. So what are the kinds of problems that founders keep calling model problems, but are in fact actually energy or data IO problems?

**Jeff:** Yeah. I think the example you raised of a thousand X difference in moving data versus actually computing on it in terms of energy is a pretty significant one. It shapes a lot of aspects of what we do in machine learning. Because if you didn’t have that thousand X difference, then you wouldn’t have to do batching. But you have to do batching of many examples or maybe many tokens at once in order to amortize that data movement so that you can avoid paying a thousand X slowdown, but instead pay a thousand X divided by batch size energy cost. And for really low latency, batching is not very good. So I think these kinds of things and the energy behind various decisions in the computer hardware we use really affect a lot of decisions we make in building higher-level systems.

**Diana:** A very concrete example is just how training models is done. There’s this whole concept of batching the data sets and running epochs. That’s basically—people perhaps may confuse that as a model problem, but it’s really a systems data IO problem, right?

**Jeff:** Yeah. You have to assemble batches to get better efficiency in your hardware. Ideally you might do batch size one training, but it’s not as good in terms of efficiency. So people use pretty large batches these days.

**Diana:** Do you think it’s possible for—I know you’re well known for taking off on a long week or a weekend and coming up with this brilliant solution. Is there such a thing as Jeff Dean going and working on it for a couple of weeks and getting batch size equals one training done?

**Jeff:** Yeah, I’ve been thinking more about inference actually. I think inference is a pretty interesting problem because you do want very low latency. Training, you don’t necessarily need incredibly low latency. And I think there’s a lot of room for specializing hardware more for inference than we are today.

**Diana:** What are some of those interesting things that are on inference that you’re really thinking a lot about?

**Jeff:** Just trying to minimize data movement, trying to think about incredibly low precision operations and maybe not supporting lots and lots of different kinds of precisions. If you feel like you have a good answer for what kinds of precision you need, maybe just build that into the hardware and not much else.

**Diana:** Which I think brings down to a core analogy I heard from famous computer scientists that really the whole process of AI is a big compression problem. Because in order to have the data to be fully lossy and compress it and then restore it, you basically need to understand it.

**Jeff:** Yeah. If you truly understand the data, you should be able to compress it really well.

**Diana:** And now transformer architecture is basically one of the ways that has turned out to work really well.

**Jeff:** Yeah. Yeah, I would say.

**Diana:** Working pretty well so far.

**Jeff:** Good work by my colleagues.

**Diana:** Yes. Now let’s zoom out a bit. AI progress used to mean just better models. You had more data trained, bigger models with bigger parameters. But increasingly in the last year or so, it’s everything around the model, not just the model size and number of parameters or more data. It’s everything around things like retrieval, tools, memory, agent tools. And it might get consolidated into what people call context engineering, right?

**Jeff:** Yeah. I think the model is really only one piece of what you’re trying to do, which is build an overall system that can solve really interesting problems. And that involves a model that knows how to use various tools. It maybe knows how to retrieve relevant information, maybe has a history of other information that it has retrieved for past problems. And it can put information into the context of the model. The nice thing about that is that information is really clear to the model. Unlike the training data the model was trained on, where it’s all trillions of tokens stirred together into a soup of hundreds of billions or trillions of parameters, but it’s all less clear than the actual context that the model sees directly for this particular problem or use case. And then I think being able to understand what tools are available, which ones are going to help the model solve this next phase of the problem, how to decompose a problem into a sequence of tool calls, maybe trying multiple approaches to solve the problem and seeing which ones work and being able to evaluate that.

This is the whole orchestration of complex agent and multi-agent systems that I think is going to be more and more important and super exciting times, I would say.

**Diana:** And I think the fun thing about this particular problem domain set is actually something that everyone in this room can do because before, to train a model, you needed an incredible amount of resources, an incredible amount of access to GPUs and data. But for context engineering, everyone here could do it. You need the API to something like Gemini and then work on your own setup for your own retrieval, your own tool calls, et cetera. So what are some tips for everyone here? How does everyone get better at and become exceptional at context engineering?

**Jeff:** Yeah. I think a really good way to do it is to use these models, harnesses, and tools to try to solve problems. Sometimes you can actually see where the models are failing. Often, you can make the model work better and succeed at that kind of problem not just by adjusting the model parameters, which is hard to do from the outside, but by creating better guidelines for the model—writing skills for the model to know how to use different tools that would be incredibly useful for solving this particular class of problem. As you do that, you end up with this kind of improving, self-improving setup that you’re trying to use to solve things. That’s a really good way to get better at understanding what additional information the model would want in order to become more capable.

**Diana:** Can you give an example of some context engineering you personally have done? Skills you wrote, tools that really made a huge difference in your workflow?

**Jeff:** Yeah. I mean, I guess Sanjay and I were working a few weeks ago, and we often do some amount of performance improvement for very low-level libraries. We have a microbenchmark library we’ve written at Google where you can write microbenchmarks of how long different kinds of operations take or how long it takes to populate a data structure or whatever. Sometimes those data structures are used on millions of processes across Google, so it’s actually pretty important to make sure they’re high performance. You can write microbenchmarks, but then without an agent-based system, what you usually do is measure what the current performance is on some benchmarks you care about, make some modifications to improve the performance you hope for, then rerun the benchmarks to see where things improved. You run maybe a broader set of benchmarks, measure the cache footprint of things.

So we wrote a skill that basically taught the model how to do most of those things in various sequences so that it could actually do self-improving benchmark measurement, benchmark code changes, measure the performance improvement, and then iterate on that. That seemed to work pretty well for some kinds of problems. It really just is us giving the approach we would use as people to the model in a form that it could use.

**Diana:** That seems very impressive. So you’re saying you have this skill that if someone got access to it, it could perform optimizations like Jeff Dean. Seems like the world would love this and is worth an infinite amount of money. Does someone have access to this?

**Jeff:** Oh, we actually published a document maybe a few months ago called Performance Hints that Sanjay and I wrote. It’s a 30-page document about various kinds of performance tricks. Some people have taken that and given it in summarized form to various models and seen that the model can now get better at reasoning about performance issues and code.

**Diana:** So you heard it all here. You could actually optimize your own code like Jeff Dean if you take this paper that you published and perform the hints. It’s all freely available. So you should all try it. Very cool.

**Jeff:** Yeah.

**Diana:** We’re talking about agents. Everyone here is probably building one or has built one at some point. I’m sure everyone has seen their agent go off the rails at perhaps step 30 or 40. Agents are great up to step 10 or so, and then it gets shaky at step 50. What do you think is the constraint today? Is it context, evaluators, or just errors that compound because it’s basically an open-loop system?

**Jeff:** Yeah. Obviously we want agents to be able to run for very long periods of time because that’s how they’re going to solve more and more complicated problems. But as you observe, today they sometimes stop working after 10 interactions with the tools and so on. Sometimes that’s because the model is trying to do something it doesn’t have a lot of experience doing. It’s been trained on a whole set of things, and as soon as you get a little bit off the distribution of things it knows how to do, then, like most machine learning models, its performance will suddenly start to degrade. The farther you get off the comfort zone of what it knows how to do, the more likely it is to not work as well. There’s a bunch of things you can do. One is give the model skills and hints that tend to keep it in the more brightly lit path of things it does know how to do.

I think having multi-agent systems where you have multiple agents trying different approaches, and maybe another model or agent that’s evaluating which ones of those seem promising, is another way to, in some sense, search the space of possible solutions and stick to the ones that seem most promising and discard the ones that didn’t seem to work or maybe that went off the rails. That’s a very useful general technique: inference time compute to perform search over plausible ways of solving the problem that can get much higher performance or much more reliability in long-running agent flows.

**Diana:** How are some ways you implemented this particular workflow for your agents internally?

**Jeff:** Yeah. We have harnesses, and then we have a whole set of skills, particularly in the internal Google development environment. We have skills so that the agents can know how to use lots of our internal tooling for coding, code reviews, measuring performance, or fetching log files. Those are just skills that you can add to make the base model more capable. Even though it hasn’t necessarily been trained on exactly the way that Google internal engineers would fetch log files from our proprietary system, with the right kind of skill definition, you can actually get it to work. That improves the usefulness of the agents.

**Diana:** Now let’s talk about where startups can win. This section is one that I personally care a lot about because everyone here in this room needs to decide what to build in the future if you’re a future founder. The thing about Google is you co-design everything on the system, from the processors to the products. Which are the layers that someone like Google would keep building and compounding, being better, and where does a two- or three-person team still win?

**Jeff:** Yeah. I mean, I think obviously Google and our Gemini models and our hardware infrastructure are really trying to build very general models that can do almost anything. But in a lot of cases, that means we don’t have a lot of attention on particular domains where perhaps a really well-designed surface and maybe a model and set of skills, or maybe a specialized model that isn’t in the general mix of things that our models do well, can actually have a significant advantage. Because you can build something delightful and really high accuracy here, really high quality for a domain that you are really passionate about. And I think that’s where the two or three people in a room building that, that they’re really excited about, can have an advantage. But I would also caution that the general models are definitely getting better at a broader and broader range of things.

So you have to figure out, is that thing you’re working on going to be a durable thing, or do you think the models at the forefront are going to get better at that in the next six months or 12 months? Or is it something they’re not going to be able to do for a couple of years or three years? And you want to weigh that as you’re deciding what to work on.

**Diana:** Let’s dive deeper into this. So the general models, of course, you’re going to keep working on and keep making them all better. And how should the audience reason about what are those areas that it doesn’t? How should a founder think about things to pick on and work on?

**Jeff:** Yeah. The most important thing is to pick something you’re super excited about and want to build and you think would be useful in the world. If you do that, you’re already way ahead than if you wake up and you’re like, “Oh, I don’t really want to do this,” or you’re going to build something that is actually not that useful to the world or to many people. So I think that’s the number one selection criteria I try to apply for what problem should I work on next. Second, I think you want to look at what the current more general models can do in that problem domain. You can test them with, are they able to do this thing very well? And if they’re completely failing, that’s probably a good sign. If they’re kind of able to do some of it but not very well, that’s maybe not a great sign because that’s probably a sign that the capability is starting to be present in those models.

And with more training data or larger-scale models or whatever, it’s likely to get better. So look for something where the model succeeds 0% or 1% of the time, not 20%.

**Diana:** How do you find those? Are those things effectively out of distribution from the training set? And what exactly is the problem shape that fits that?

**Jeff:** Yeah. I think sometimes it’s a product that you build that might have access to particular kinds of data that the underlying model might not, a general model. So it might be you’re building something to help users organize all their own personal information and the model won’t necessarily have access to that. There you can have a big advantage because all of a sudden your model or your product has visibility into important data. It could be some incredibly hard problem where if you get the right training data and you can train a more specific model than a general-purpose one, you can actually do that in a very affordable way. Maybe it doesn’t take that much compute to train a niche model for this particular problem, but you can get something that’s highly accurate. That can sometimes be a really good building block for solving an important problem that is maybe not handled very well by the general model.

**Diana:** I think that’s interesting. I think there are basically two paths. The first path is a little bit funny, is you guys are organizing the world’s information. That’s probably kind of well covered. But organizing your personal information that’s open, which is funny. And then the second path, you talked about more specialized models in certain domains. Can you tell us more about what are some of these domains?

**Jeff:** Yeah. I mean, I think if you look at my colleagues’ work on, say, AlphaFold, that was a very specific model for protein folding. And it was highly successful and was able to really handle that domain quite well so that all of a sudden you now have this amazing tool and model that can give you answers to questions about proteins and their structure really effectively. But it’s not a general model. It’s a very specific one. And there are other, I think, domains where that kind of approach can work really well, maybe in material science or chip design or things like that, that will enable you to leverage the capabilities of a very accurate but niche model to do things that are hard today.

**Diana:** That’s a good example. So if some of you find a problem that’s similar in shape, like AlphaFold, it could be a good problem to work on. Now let’s assume you found a problem to work on. We’re going to talk a bit about how you become an AI native founder. How do you really become good at it? You in the past said that managing a fleet of agents, say 50 or 100 agents, is all about writing really good, crisp design docs or specs. And how do people get good at that? What do those look like?

**Jeff:** Yeah. I think you’ll have a lot more success when working with your virtual agents if you can clearly specify what it is you want. The clearer you are on what you want, the more the agent will have guidelines and rules—an outline of what it is trying to accomplish. Whereas if you don’t specify very much, the agent has to infer what you meant. In many cases, it might infer things that are different from what you imagined. We’ve always told computer scientists from the very beginning that it’s really important to specify what the software you’re writing is trying to accomplish before going and writing it. Now we actually have agent-based systems that can do the writing, but the importance of specifying what you want has actually gone up, because before you’d be handing it off to a very intelligent human who maybe has context or can ask you follow-up questions.

Agents can sometimes do that, but I think clear specifications are a really good idea. To give you an example of a use of a coding agent that works extremely well: you can ask today’s models to translate software from one computer language to another very effectively. In that case, you actually have an incredibly detailed specification. You have the whole software that says what the system is supposed to do. So if you have a Python implementation of something and you want a Go implementation of it, that is something that the models seem incredibly capable of doing these days. They can take all the tests that are in Python, make sure they pass in the Go version, translate the tests to Go, compare behavioral differences between the implementations until there aren’t any, and be highly effective because that spec is so clear.

**Diana:** Now let’s assume every founder gets good at running hundreds of agents at the same time and all the code is written for them by the agents. What becomes the scarce skill?

**Jeff:** Yeah. I think it’s really having incredibly good taste in what you ask your agents to work on. That is the crux of, from my background, a research problem. A researcher can have all the tools and all the techniques, but often most of the battle is what problem are you going to spend your time on? If you pick the problem well and succeed in solving it, that’s way better than if you delightfully execute a research investigation into a rather boring problem. That high-level wisdom of what to work on is incredibly important. I think models are not necessarily going to be that good at it. So you’re going to have people steering a lot of AI-assisted computation in order to accomplish great things more quickly. But that essence of what it is you want your models to do is the key thing you should focus on.

**Diana:** So let’s talk a bit more about taste because it gets talked about a lot right now in this current era with agentic coding. How do you exactly build taste and do that? That sounds so esoteric. How do you make it concrete?

**Jeff:** Yeah. It is a difficult thing. It’s not like there’s a measurable objective of taste in a lot of cases. I think some of it is from experience. Working on a lot of different problems in the past teaches you about what kinds of problems might be interesting in the future or what kinds of things might be just barely possible by cobbling together these previous approaches, and then some open problems you might have to work on in order to get to something magical or highly useful. Another way you can get more experience for yourself is to just write down a bunch of things you think might be important in the next 12 months. Maybe you pick one of them to work on, but go back and evaluate in 12 months which of these other things actually seemed important, or which ones did other people in the world go out and create, and which ones did not seem to happen yet.

That can give you a lot more samples for your own taste creation capability. And that’s an important skill to have.

**Diana:** I think a third way we were talking earlier was doing very crazy thought experiments.

**Jeff:** Oh yeah. That’s another good way. Sometimes it’s good to not take as a given things that most people seem to take as a given. I was doing a crazy thought experiment with some colleagues the other day: for 60 years, the whole silicon chip design and fabrication industry has done tremendous work to make smaller and smaller scale transistors that are very low error rate. The assumption is that every chip we manufacture of the same design should be identical to every other chip.

**Diana:** You don’t want any bits to flip.

**Jeff:** No bits should flip.

**Diana:** Deterministic.

**Jeff:** There are all kinds of error margins built in—memories have ECC memory these days. At the macro scale, we don’t make that assumption when we’re building large-scale distributed systems. We build reliable, large-scale distributed file systems out of unreliable parts. Individual disks can fail, but your data should be safe. So we have mechanisms at a higher level to enable us to have three copies of the data on three different machines and three different racks, so that if any rack switch or individual machine or disk fails, you still have your data. We have Reed-Solomon encoding techniques, but we don’t seem to do this at a really extreme level at the transistor scale of the technology we’re working on. So basically, an interesting thought experiment is: what would happen if you tried to build a system out of transistors that might have 20 errors per day.

**Diana:** Oh my God.

**Jeff:** Rather than one every million years. That would be a very different design point and might enable you to do really interesting things in the fabrication side of things. You have very different design methodologies because if you want to get a signal from here to there and you have these super unreliable transistors, you might have very different ways of signaling. You might send it along multiple redundant paths in order to make sure that it gets along one of them. And I think that would be a pretty interesting set of thought experiments. I’m not saying we should go do this, but that’s the kind of thing where you do want to occasionally question assumptions. Now, oftentimes these thought experiments don’t work out because there are very good reasons that for the last 50 years we’ve done this thing this way and not that way. But it’s good to revisit those every so often.

**Diana:** That is so wild. It’s starting to rhyme a lot with neuromorphic computing or the human brain and how nature works.

**Jeff:** Yeah. Exactly. Signals in our brain are not especially reliable from getting one place to another. And so I think in brains, when there are really important things you need to get from one place to another, there are multiple pathways that enable you to do that.

**Diana:** You have such an impressive career. What is one of these crazy assumptions that you threw out of the window that actually built a consequential system in the past?

**Jeff:** Yeah. I guess—

**Diana:** That worked out, actually.

**Jeff:** Yeah. I think, well, TPUs is a good example. Being able to specialize hardware for a very niche problem domain before that problem domain seemed as important as it is today is one thought experiment. I think the origin of MapReduce is another good example. So we had worked, Sanjay and myself and a number of other colleagues had worked on various iterations of the crawling and indexing system at Google. And we’d written lots of hand-parallelized code with lots of checkpointing to make sure it would be robust and reliable if it was running on a hundred computers or a thousand computers and some of those died.

But that code tended to be intermixed with the actually relatively simple thing you often were trying to do. I just want to look at all the contents of all the webpages and then compute on the side mapping from URL to what language is this page in? It’s the text of this page. And it would get obscured by all this other code for parallelization and reliability. And so we remembered our training in functional languages and realized we could squint at those problems and develop this MapReduce abstraction that you could have above this implementation. And then below the implementation, you could put all the checkpointing and reliability mechanisms into that lower-level library that everything could then build on. And so that became a hugely successful way of dealing with very large-scale computations at Google in a robust and reliable way from that thought experiment of, well, if we squint at it, could we find lots of problems that fit into this abstraction?

**Diana:** That’s impressive. So this thought experiment led you to create MapReduce.

**Jeff:** Yeah.

**Diana:** Awesome. Now let’s go back to- you talked a bit about your interest right now in working on a lot of customized hardware. So right now AlphaChip lays out chips. Now you also got AlphaEvolve that proposes solutions, evaluates them and keeps all the ones that work. Seems like you’re starting to build all these systems that can compound and build AI that builds AI.

**Jeff:** Yeah. I think more generally there’s the foundation of the scientific method where you propose an experiment, you implement what you need to run the experiment, and you evaluate the experiment, and then you get results from that. I think there are more and more problems that are now possible to implement where that whole loop of running not just a few experiments, but running many, many experiments because you’re able to automate that loop and make the latency of that loop extremely low is going to be really, really important. It’s going to enable us to tackle lots of different problem domains in science and engineering and machine learning model design itself and also in engineering tasks like designing chips. If you can actually do those things in an automated way and have some orchestration framework that can take very high-level objectives and break them down into sub-problems, and each of those sub-problems can be one of these automated loops that is exploring the best way to solve that sub-problem.

And then an orchestration framework that can put together sub-problem solutions into the overall solution for the higher-level problem. That’s going to be really impactful, and it’s really, really important. I think it’ll enable us to accelerate machine learning progress. It’ll enable us to accelerate science and enable us to accelerate engineering. I think that’s going to be amazing.

**Diana:** That sounds awesome. It sounds like a lot of fields basically where you can have very good evaluators and maybe adjacent to things that can be formally verified. Those are ripe for AI systems that can self-improve.

**Jeff:** Yeah. I think in a lot of cases, sometimes your evaluators need to be made much faster. As an example, my colleagues did some work maybe a decade ago on some problems in quantum chemistry where you’re trying to understand the properties of a particular molecule, and you can generate some molecule configuration, and then you want to understand what properties it has. You can run a very computationally intensive density functional theory simulator, which is something that might take a night of computation to tell you the answer for one thing.

But what my colleagues did was take a bunch of output from those simulation runs, the input molecule configurations and the outputs of the expensive simulator, and then use it to train a neural approximation to the simulator. So this is now a validation device, but instead of it taking a night, they made something that was 300,000 times faster and nearly as accurate as running the full-scale simulator. So now that completely changes how you would do science, right? Because now you have 10 million things to screen. You could do that while you go to lunch rather than it being a six-month endeavor where you try to scrape together enough compute to run all these simulations. And I think there’s a lot of room in a lot of domains for much faster validation models, possibly learned validation models that can get you an approximation to the true answer much more rapidly.

And that changes how those experimental loops can be thought of and how quickly you can go around those loops.

**Diana:** What are some of the spaces and problems that you’re super excited that this super sped up scientific method is going to solve or achieve? What particular problems or spaces?

**Jeff:** Yeah. I mean, I think, well, clearly machine learning itself is one. So can we have a model that is able to recursively self-improve itself by running lots of experiments? And if you think about how models are improved today in large research teams, what usually happens is people think of some ideas, they run a bunch of small-scale experiments, they see if those small-scale experiments worked out well. If so, they take the most promising ones of those, they try them at larger scale and that gets then evaluated. And then the results get integrated together into a new recipe for your model. But I think there’s no real impediment to making that be a much more automated loop where the model itself decides it’s going to explore or maybe with a nudge from some people at the various highest level like, oh, why don’t you try some new ideas around model architectures that incorporate this?

And then they will go run lots of experiments, see which ones work, and then those will get incorporated at a much more rapid rate. And effectively you want to optimize your discoveries per unit of compute input.

**Diana:** Very cool.

**Jeff:** Yeah.

**Diana:** Now going back to the room, as all of you will become at some point founders or start your careers, you will probably collect lots of rejections. That will happen. It has happened to you too, Jeff. There’s a story that in 2014, you, Geoff Hinton, and Oriol Vinyals wrote a paper on distillation, which has to do with taking a big teacher model to train a much smaller and more efficient model that’s a lot cheaper to compute, with fewer model parameters. And it has become a trick that everyone is using right now in industry.

**Jeff:** Yeah.

**Diana:** And the thing is, this paper got rejected at NeurIPS.

**Jeff:** Yeah. I mean, I think I don’t fault the program committee because a lot of times a paper gets three reviews and someone will look at, one of the reviewers will look at it. And in this case they said, oh, it’s unlikely to have significant impact.

But I think when we wrote the paper, we actually saw this was a super important problem because we knew making cheaper, highly capable models from larger-scale models was something we desperately wanted to do because we wanted to serve models to more and more people in many different domains like speech or vision. But sometimes the reviewer maybe didn’t have that experience because maybe they’re not thinking about large-scale AI services and are thinking about, is this a fundamental advance? So it gets rejected every so often; that’s fine. We put it on arXiv, people read it, people use it. It’s all good. And we do use it in making our flash models, for example, from our larger-scale pro model. That’s partly why our flash models, for example, in Gemini, are so capable relative to their size and speed.

**Diana:** They’re some of the best in the benchmark for their model size class, which is impressive. And I think part of the lesson is that even if you get rejected, keep going.

**Jeff:** Yeah, that’s the lesson I would distill from that.

**Diana:** Now, I think the fun thing is that when you joined Google as a 20-person startup back in 1999, now if you were to take the young Jeff Dean from way back then to transport him to now, today, in this era with your skills.

**Jeff:** I’m feeling so vigorous and young now.

**Diana:** What would you do? Do you join a frontier lab, start a company? I don’t know. What would you do with Jeff Dean today, 25-year-old Jeff Dean?

**Jeff:** Yeah. It’s always hard to say, and it’s a very personal choice of what it is you want to spend your time on. To me, some of the most important questions are, are you going to work on something you really care about? While you’re working on that, and if you’re able to make progress on it with a bunch of colleagues you like working with, if you’re able to collectively solve it or make progress on it, will that make a difference in the world in some positive way? Will you suddenly be able to do something and offer that service to, you know, maybe it’s a very niche thing, but it will tremendously help biochemists or something. Or maybe it’s a broader thing. It’ll help programmers, or it will help all consumers on the internet or other things.

What you should strive to do is to have impact in the world that is positive and to work with people you enjoy working with and to work hard and do your best. So in terms of, say, the particular trade-off you offered—joining a frontier lab versus starting a company with just one or two or three of you and your close friends—I think those are different experiences. In a large established organization, you have some structure, you have lots and lots of amazing colleagues who know lots of things you don’t. You have lots of interesting problems that you can work on. And you already have a platform for impact by your work influencing lots and lots of people in the world already. And then as a very small startup, you have to have something you’re passionate about. And there’s a lot of risk in working on that particular problem in a way that you’re going to succeed and you’re going to grow and endeavor in order to do that.

But that can also be incredibly rewarding, I would imagine. So I think it’s really up to personal taste, but at the very least, regardless of what path you take, ask yourself, “If I work on this problem and the best possible outcome happens, will the world be a lot better in some way? Or will the world go, eh, that’s kind of cool, but whatever.” That’s not the kind of thing you should spend your time on.

**Diana:** Now let’s talk a bit more about that second path of working with people that you really like in a small team. You’ve been able to be an incredible mentor and manager to many, many engineers, and you’ve been able to build huge systems. What are some of the lessons for everyone here on how to get the most and how to work with smart people or find smart people?

**Jeff:** Yeah. You always want to find people who have really good skills in some area that’s needed in a team you’re trying to form, whether that’s inside a company or starting a company. But you also want to find people that are people you delight being around because you’re going to spend a lot of time around people working on really hard problems. And you want people who are low ego, that are team players, that have complementary skills to your own, perhaps. I always find working in a small team where people know things that I don’t know and where maybe I have some skills that other people don’t have as much of is super fun because you’re collectively building something or working on something that none of you could maybe do individually. But in the process of working on that, you actually gain a lot of new knowledge and new skills for yourself, and so do they.

And you want to view your engineering or research career as having an amazing tool belt of techniques. You always want to be adding new tools to that tool belt because you never know when you might come across a problem where you need these four specialized tools rather than these three. Adding more tools makes it more likely that the problems you encounter in the future will be solvable by you.

**Diana:** Now, one last thing, I’m pretty sure someone in this room or multiple people will eventually build something as consequential as you’ve done with MapReduce, TPU, distillation, et cetera, et cetera. What problem do you hope they would be working on?

**Jeff:** Oh, yeah. I think there’s a lot of interesting problems in the world. I’ll just rattle off a few. This is not exhaustive because the world is a very big place and full of problems. I’m particularly excited about new approaches to hardware. That thought experiment there was kind of an indication of that, or much more efficient inference hardware. I think there are radically different kinds of algorithms for machine learning that might be much more data efficient than the approaches we’re using today. If you think about our large-scale models today, they probably see a thousand times as much data as a human does by the age of 18. Yet the human by the age of 18 is better in a lot of things and on par with those frontier models that have seen way more data. So could you come up with much more data-efficient systems that can learn continuously, learn from their own actions?

Continual learning is a really interesting thing. I think multi-agent interactions are interesting. Creating ways of having better discourse among people in the world could be interesting. Are there ways to have much more civil conversations and help people meet others all over the world that they should know based on their interests? These are interesting things, I think. There are lots of cool things in the world, and we should all strive to make even cooler things occur.

**Diana:** That sounds wonderful. Thank you so much, Jeff Dean. That’s all we have today.

**Jeff:** Appreciate it. Thank you all.

