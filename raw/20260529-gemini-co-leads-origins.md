---
type: raw
source: "https://www.youtube.com/watch?v=8hfpLa5wPGo"
author:
  - "Jeff Dean"
  - "Koray Kavukcuoglu"
  - "Noam Shazeer"
  - "Oriol Vinyals"
  - "Logan Kilpatrick"
published: "2026-05-29"
created: "2026-05-30"
tags:
  - clippings
  - Gemini
  - Google-DeepMind
  - unified-model
  - distillation
  - world-model
  - agentic
  - coding
  - interview
  - transcript
video_meta:
  videoId: "8hfpLa5wPGo"
  channel: "Google for Developers"
  channelId: "UC_x5XG1OV2P6uZZ5FSM9Ttw"
  duration: 2519
  language: "en"
  thumbnail: "https://i.ytimg.com/vi/8hfpLa5wPGo/maxresdefault.jpg"
---

# Gemini co-leads on project origins and what's next

To mark the launch of Gemini 3.5 Flash, Logan Kilpatrick sat down at Gradient Canopy with four of the people who built it: Jeff Dean, Koray Kavukcuoglu, Noam Shazeer, and Oriol Vinyals. They talked about the origin of the Gemini project, the bet on a single unified model, why each Flash generation now outperforms the previous Pro, and what's coming next.

## Table of Contents

* [00:00:00] Cold Open & Introduction
* [00:00:45] The Origin of Gemini & Why One Unified Model
* [00:02:06] Product Feedback Loops & the Importance of Real Users
* [00:04:49] Why a Single Model Powers Everything
* [00:06:22] How Controversial Was the Decision to Unify?
* [00:08:52] How the Teams Came Together
* [00:09:17] Multimodal & the Pathways Vision
* [00:10:07] Gemini Omni & World Modeling
* [00:12:33] How Everyone Met: Jeff Recruiting Noam & Oriol
* [00:17:19] The DeepMind Acquisition & First Code Review
* [00:19:02] Surprises: What's Gone Better or Worse Than Expected
* [00:20:28] Distillation: Packing Pro Intelligence into Flash
* [00:21:31] What Hasn't Worked & What's Still Hard
* [00:27:57] Research Disagreements & Different Focus Areas
* [00:31:01] Predictions for IO 2027
* [00:36:31] Three Products or Ten Thousand?
* [00:39:56] What Everyone Is Building Outside of Work

## Cold Open & Introduction [00:00:00]

**Jeff:** Even before we started the Gemini effort, there were a lot of people thinking about, you know, building incredibly general purpose models that could do things. Oriol was leading some efforts in DeepMind and I was sort of helping steer some efforts uh in around the Pathways project and things like Palm and Palm 2 and so on. I actually said this is silly. We are fragmenting our efforts and fragmenting our compute and if we're going to build an incredibly powerful model, we need to all come together and work on building a single single model. That's actually where the name Gemini comes from. The twins.

**Noam:** We mapped and then we reduced.

**Jeff:** Yeah. Yeah. Yeah. Exactly. Yeah. Something like that. And uh

**Noam:** I thought it was because I had twins.

**Jeff:** That too. That too.


## The Origin of Gemini & Why One Unified Model [00:00:45]

**Logan:** Hey everyone, how's it going? My name is Logan Kilpatrick. I'm on the Google DeepMind team. Today we're talking with Jeff, Koray, Noam and Oriol about all things Gemini, the origin of the Gemini project, and so much more. So, thank you all for sitting down and chatting.

We're sitting here in Gradient Canopy. We just launched the Gemini 3.5 era of models starting with Flash. Contextualize the moment. I think we've this is like the third and a half generation of Gemini models. We've shipped a lot of stuff, a lot of models in between. Maybe Oriol, you want to sort of fill us in on the moment with Gemini 3.5?

**Oriol:** Yeah, we could do one each maybe. Uh but contextualizing, I guess we started 2023. I want to say we've had a few releases, some half models or even point one. And been building on some foundation of multimodal, you know, tool use, agentic from from the get-go and just kept building the capabilities up.

So today it's exciting to be releasing the flash version of 3.5. It's a very powerful series and the focus of this one probably is on a coding and then of course preserving and enhancing the rest of capabilities. I think everyone feels like this is really the times where coding capabilities and agentic experiences are defining what it means to experience AI and like 3.5 is a huge huge step there.


## Product Feedback Loops & the Importance of Real Users [00:02:06]

**Jeff:** Yeah. Right. And I think everyone is actually experiencing that and it is being recognized as a very strong model. These big release moments have in one way gotten less exciting because the thing that's like most at the top of everybody's mind is not even the big release to the public.

It's like what am I going to be using tomorrow to do my engineering and my research and what are my friends around me around the office going to be using for their engineering and research and will they be complaining at me? Will they be happy? It's always fun and exciting on a day-to-day basis.

**Logan:** Reflecting back on sort of the initial like moment of and like coming together and forming the Gemini project and shipping those initial models. Was it obvious to you all that the like product story of like how we bring Gemini models to the world was going to be so important? Not from like obviously at Google we have lots of products and we bring AI to our customers through the products but actually to like improve the model was that like a we hope that this happens and it's something that we're going to intentionally work towards or has it just become like obvious over time that like we need to do that because the use cases are much more complicated than like the initial version of Gemini.

I'm actually curious what you all think.

**Jeff:** I mean I can weigh in and I think you know that was actually pretty obvious that if you have a model that is used by a lot of people that you're going to get a lot of lessons and experience of what's working well, what's not working well. And you know we've seen this in search for many many years is the the use of search by our users really informs you know what are the things that's not doing well, what are the things we should be doing better. um you know aggregating lots of interesting usage statistics to understand you know that in a deeper way and then working on improving those things is important and AI models should be no different.

**Logan:** Right so it seemed like that was pretty obvious from the beginning but we had to have a

**Jeff:** A thing out there that people were using.

**Noam:** Yeah that's the true test like people using it and is it useful to people because if you go in the box and you try to hill climb benchmarks then you end up hill climbing benchmarks then you know maybe you leak your benchmark it doesn't end up well.

**Koray:** You don't want to build intelligence in a black box. You want it to be useful. You want people to be using it like therefore like understanding what is required like what is the like scratching the frontier is both scratching the frontier of the research in terms of technical capability but also scratching the surface of what is the next thing that you can enable users.

You can't do it if you don't actually do it with the products and those two hand in hand define what the frontier means.


## Why a Single Model Powers Everything [00:04:49]

**Oriol:** So at the time like Gemini starts like there's a lot of already machine learning models making it into products and I think the what seemed obvious is that if we create a single more powerful than the average of the other models like powering everything that had to be like a leap forward.

Whether there was a single product that could be created around a single you know model that maybe wasn't as clear at the time but I think it was very clear that putting all the compute and intelligence into a single powerful model was going to leap frog many things Google was using already machine learning for and that was very exciting to be given that amount of compute and responsibility initially.

But I think it's proven to be indeed kind of the core engine of Google intelligence.

**Jeff:** Even before we started the Gemini effort there were a lot of people thinking about you know building incredibly general purpose models that could do things. Oriol was leading some efforts in DeepMind and I was sort of helping steer some efforts uh in around the Pathways project and things like Palm and Palm 2 and so on. I actually said this is silly. We are fragmenting our efforts and fragmenting our compute and if we're going to build an incredibly powerful model, we need to all come together and work on building a single single model. That's actually where the name Gemini comes from. The twins.

**Noam:** We mapped and then we reduced.

**Jeff:** Yeah. Yeah. Yeah. Exactly. Yeah. Something like that. And uh

**Noam:** I thought it was because I had twins.

**Jeff:** That's true. That you


## How Controversial Was the Decision to Unify? [00:06:22]

**Logan:** Jeff, that's a great segue to sort of again going back to sort of the formation of the Gemini project. I'm curious how controversial was that? Obviously like as you say it now and we sort of have we've done three and a half iterations. The sort of all the organizational complexity of bringing teams together is now sort of behind us. Was it like blatantly obvious at the time that like we won't win and actually deliver on building the right product and models for our customers if we don't do this or was it like sort of a originated as like a more pie in the sky idea or like I'm just curious like what was your level of confidence?

**Jeff:** I was sure the right thing was to come together. I actually articulated in a half-page memo like this is silly to fragment. We shared this half page we should put it somewhere release it somewhere. But it felt like fragmenting our best ideas across different research teams that weren't really working together and also fragmenting our compute. just both of those issues seemed like things we should fix.

And it was a little bit organizationally complicated and time zone wise like there was lots of people in London lots of people here 8 hours apart is never a recipe for easy collaboration but I think we've done a really good job of navigating that and bringing people together and now we have like a really good amazing team all over the world and we're cranking out good models.

**Logan:** There were a bunch of teams building LLMs at the time that you just needed to mash together basically. At some point

**Koray:** Like research in AI was a lot more academic right like you go back like 10 years a lot more academic research and at that point like the how you organize it is not really the key element it is more about the exploration and the speed of exploration is important.

But as things get more and more focused what you want is to really to Jeff's point this focused operation where rather than us trying to build things in parallel. Well, because these things require a lot more focus, effort and each one of them is like a major operation in terms of many researchers coming together solving many problems. At that point I think it was really really a good idea to okay this is the moment that we need to change.

I think like both organizations acted with like great urgency on that and enabled it. I think that was an experience of course it's never easy bringing two organizations together but I think everyone realized that this is the right moment and there's a huge value to be gained from this and I think everyone all of us can see like the whole organization is very proud of what we have built together like Gemini is really the fruit of that.


## How the Teams Came Together [00:08:52]

**Noam:** It's the scale it's the fact that you can when you build one big beautiful giant LLM that it's uh you know it can do so many things and so you know you really do need to put together yeah that many people that that much compute and infrastructure teams data teams and so on.

**Jeff:** Yeah. Better to have one of those teams than five little ones.


## Multimodal & the Pathways Vision [00:09:17]

**Noam:** Yeah. Yeah. I mean to have one model than five. One thing I would say is like from the start we wanted Gemini to be I mean even pre-Gemini what one of the origins of the Pathways project was to explore you know a single model that could do many things a multimodal model that could deal with all different modalities a very large model that was sparse so you would activate different pieces of it for different kinds of things and all three of those things are sort of represented in the Gemini models that we have today.

Um and I think now with Omni we've gotten the multimodal kind of aspects of the now we can even generate video uh you know we used to be able to just generate images and audio pretty awesome because you have the full capability of this amazing reasoning model that can deal with lots of input modalities and can like edit the video it's just produced.


## Gemini Omni & World Modeling [00:10:07]

**Koray:** I think Omni is a whole new capability right like I mean we had Veo and Nabano of course like you can do text to video text to images but like what you want is really a model that understand all the modalities of the physical world so that it can understand the physics and everything but together with text because there's a lot of information about world in text as well at a very high level.

**Logan:** Koray, really quick, I have a question about this. In the IO keynote, we were sort of framing Omni in the sort of like world model section and I'm curious like how much uh like does it actually have a bunch of the genie world model stuff or is this sort of just like positioning for the next stage where it takes in anything and puts out anything and that's sort of our representation of world model?

**Koray:** That wasn't abundantly clear to me. I hadn't thought about it that way. I'll give my opinion like Oriol has worked on these things a lot. World modeling means that like you really understand the dynamics, the physics, the visuals and then like you have to be able to simulate that as well because that simulation aspect is critical for both us understanding if the model has it right and also when you want to rely on the model you want a model that is going to be able to roll forward that simulation and the decisions that are coming out of the model is based on those future simulations.

That's why I think Gemini Omni is a different category that is really transforming what we had with Gemini that is mostly understanding and text output and Veo that is text input and like doing the video modeling into turning to a really true world model by training jointly.

There's a hope that of course everything will transfer and making you know a better text understanding model will help the world modeling aspect but I think we're seeing this every time we try is not easy but as we get the recipes right we see that um you know back in the day like rolling out a complex video scene forward consistency all these things you kind of had to manually think about them and almost prespecify how to get the visuals right over time.

And when you turn the thing the object disappeared and just by training at scale and mixing all the data more and more we're seeing these capabilities emerge and that's what's exciting and sort of the main premise I guess we were putting forward and now finally we're outputting also like I mean amazing consistent like 3D worlds sounds all the things I mean it feels almost impossible if you ask me a few years ago this approach would work otherwise probably we would have done it like 10 years ago but you know it did happen.


## How Everyone Met: Jeff Recruiting Noam & Oriol [00:12:33]

**Jeff:** Yes yeah probably more data. When you say multimodal, you know, you instinctively are drawn to like human modalities like text and images and audio and video. But I think really you want the model to understand a much richer set of modalities like understand interesting scientific data that comes in genomic sequences or in chemical structure or robotic grasping data or LAR data. Exposing the model to a little bit of this kind of data makes it much better at understanding it when it does encounter more of it.

**Logan:** I feel like part of the story of Google DeepMind being able to pull off this model and actually like again this like formation story is actually like people and the fact that you all actually like know each other and we were talking off camera before this about when did you all like meet each other and start working together and like hear of each other and I'm curious for all your versions of that story.

**Jeff:** Maybe I can go first since I think I know people the longest. So uh one way to put it... Um, for many years I did a lot of engineering hiring and recruiting in the very early days of Google. So I screened all the engineering resumes that came into Google for three years or something.

**Noam:** It was amazing. They would just bring death like a giant stack of resumes. He'd be like, "No, yes, yes, no, no, no, yes." Like was like extremely fast.

**Jeff:** So I didn't actually interview Noam, I don't think, but he had interviewed and gotten an offer. And I think you were debating should you take the offer. So, I called you up on the phone in 2000 and I said, "Hey, you know, let me just chat. I want to introduce myself and you know, I really like the kinds of things you're excited about and working on. I think you'd really enjoy it here." And I finished the phone call.

**Logan:** Honest question. Were you just selling at that point or did you or like was there something like he had an offer?

**Jeff:** So, I'm selling. I want him to accept the offer.

Yeah.

Yes.

**Logan:** I love it.

**Jeff:** So, then he did. He did. And then Noam became my office mate for like three and a half years or something.

**Noam:** Oh yeah, I mean I remember joining and everyone got a mentor to like ask questions as a new hire because there are like a million things you don't know and I would ask my mentor and every time a mentor would like know the answer and you know it was like wow everyone knows everything here and it turns out that Jeff was my mentor and it was just that Jeff knows everything and had written like half the codebase.

**Jeff:** Yeah. So then fast forward I guess maybe to 2012 I think. Yeah. Uh so Oriol had interviewed with us and I don't think I interviewed you but I think you had an offer and I was trying to convince you. You were considering this and another company. So I called you up and said hey you should really come here. We're really doing really interesting deep learning choice deep learning models and we're having an awesome time.

We were all in the Google Brain team wedged into like probably a 30 person office just outside on the main patio of the main four buildings of the Googleplex. Somehow I managed to convince you to come which was awesome. Uh and

**Oriol:** Yeah there was I mean I remember lots of back and forth. I had like the last maybe one year of my PhD. So I was just writing the thesis no LLM at the time. So you actually had to you know write every single word. Lots of pondering but I joined and I maybe not exactly like mentor like Noam mentioned but we started two projects one of which was distillation.

And so I remember I mean the codebase was complex like C++ you're like in academia so you don't know exactly how to implement things so but the idea was clear and literally like I remember sitting by Jeff's desk and he was just coding the classes like okay distillation and KL divergence and so on so forth so we didn't have coding agents at the time. But you know I can say maybe for a little bit Jeff was kind of acting as like the coding agent for the project.

**Koray:** I mean a hard benchmark to beat still today.

**Jeff:** That project was good because Geoff Hinton did some of the very early exploration on MNIST which is like a tiny tiny data set that he could run on his laptop and he had some good ideas about how to get a bigger model to transfer into a smaller model. I'm like we got to show this thing at scale.

So we trained a 50 model ensemble for 300 million images which was a lot at that time and 50 distinct ones. So we grouped the categories. So this one was going to be good at cars and this was going to be good at wild animals. Then we transferred the knowledge with distillation into a single model and it was much more accurate than the single model you could have trained on the raw data.

And by the way, at the time I remember compute was already constraining, but all you needed to do is ask Jeff, hey, we ran out of CPU. And he would just go to some website, change a number, and we doubled it. And we did that a few times.

Yeah. I had super user power thing.

**Oriol:** That was not I missed that.

**Jeff:** Yeah. Sadly, exponential growth sometimes.

Yeah.


## The DeepMind Acquisition & First Code Review [00:17:19]

**Koray:** I remember first time we really sat together talked was actually during the acquisition discussions of DeepMind that you flew to New York and uh to London sorry there was this moment that like there were all sorts of discussions and such there's bunch of people in the room but then Jeff comes to me and says let's look at the code I'm like okay.

So I sat down at the keyboard I'm like okay um you know don't show me anything too sensitive but I want to see that directory. Yes. So pokes at that directory and we go inside. I'm like okay let's see this file.

He's like okay. And then like I go and explain okay here's what we are doing here. Here's what we are doing there. This is this idea. This is that idea. I mean at the time for me it was a big deal right? Like I'm sitting together with Jeff. I'm explaining to him okay these are the ideas and this is the code and like we are walking through it.

**Jeff:** Our first code review together. Looks good to me.

**Logan:** Was it actually Jeff? You were just like pointing at random directories and then Koray just happened to know what was happening.

**Koray:** We'd seen 15 talks which was great. At the time I would remember I would review pretty much all the code at DeepMind. So like I would know pretty much everything going.

**Jeff:** Yeah. And I think the company was like 55 or 60 people or something. So we all flew over to London and then we like not slept super well the that night and then we go in and we see 13 consecutive 30-minute talks.

**Koray:** Yes. Geoff Hinton had a bad back, so he's laying on the floor in the back of the conference room.

**Jeff:** We just flattened him and then

**Koray:** I heard that story.

**Jeff:** Yeah. Towards the end of the day, I'm like, "Okay, this seems pretty promising. Let me just... But let's see the code because we'd seen some nice slide decks."

**Logan:** That's crazy. We need a movie about this. I feel like this would be a good movie.


## Surprises: What's Gone Better or Worse Than Expected [00:19:02]

**Logan:** Um Oh, actually another thread of this reflecting back to three and a half years, maybe even longer than that. Like something now sort of as we sit here that is both like positive surprising and also negative surprising like something maybe you wish we had made more progress and it's surprising we haven't and also something maybe we've made way more progress than you expected.

And obviously so much of the stuff is so like hard to have imagined 5 years ago but anything that like sticks out for all of you.

**Oriol:** Maybe I start with positive and very timely for today I really didn't expect we could keep doing what we've been doing generation after generation which is to pack the intelligence of pro back into flash. So it's kind of like that happened in 1.0 and you could say well you know was it was the first run and it was fairly suboptimal in some way. So that makes sense we improved the recipe.

But in a way even that seems to be sometimes even accelerating depending on which version we look that flash next gen outperforms pro previous gen. I mean just even understanding distillation how it works I'm still like mesmerized how can we pack so much intelligence per bite or per parameter.

**Logan:** Has distillation like fundamentally changed in a like is it like sort of and I'm not super I know of the concept I don't know the details is there like architectural improvements to the way we do distillation which is part of how we can like keep packing more in or is it like the technique is relatively the same of what you all came up with originally?


## Distillation: Packing Pro Intelligence into Flash [00:20:28]

**Jeff:** Yeah, I would say it's even simpler. I mean, we had some, you know, trick with temperatures in the softmax and we had to, you know, take an ensemble of models. This

**Oriol:** Don't tell.

**Jeff:** Um, no, no, I won't tell. I'm just making sure. I'm going to spill the recipe. You have a really, really good teacher and then you have a student. So, but you didn't need an ensemble of 50 teachers. You just have one really good teacher and then one student. And you pretty much use the recipe described in the original paper with some modest tweaks, but the basic spirit of the idea is pretty much the same.

**Oriol:** Wow. Let me give you the most technical explanation. It's like squeezing the lemon. You squeeze the lemon, the juice comes out, it's the good bits, you put it in a glass, which is your small model.

**Logan:** I like that. Let's go.

**Oriol:** You should read the intro of the paper. It has some poetic intro as well about larva and insects.

**Jeff:** The original paper that was just like soft labels and

**Oriol:** Yeah pretty much yeah.


## What Hasn't Worked & What's Still Hard [00:21:31]

**Logan:** Anything that's that's sort of you're surprised we haven't been able to pull off given how much progress like across the board Gemini has made over the last three and a half generations?

**Noam:** I mean the good side like thinking back to... good it's also about the beginning of Google right like we had this what was it this one box philosophy right like Jeff you must remember like the one box for everything like the search box also with you could use it for type in something it would show you sports scores type in something else it would show you stock quotes.

And like on the back end like you know these were all separate very separate backends and like our custom built whatever some of them were AI-ish and some of them weren't.

**Jeff:** Spelling did you did you mean is like largely Noam's starter project I think.

**Noam:** Oh yeah the user would assume oh there must be some brilliant general purpose AI behind the whole thing and it knows it can do all these different things. Um and now we actually built it like we built the general purpose AI that

It's one box.

**Jeff:** It is one box.

**Noam:** It is one box and it's like one back end like we finally we finally have the back end for the front end and we have the right interface because we built the one box.

**Koray:** He wants a negative thing. No, no, not negative, not negative. But it's obviously like we people want more, you know. Is there something that you wish? But I think you should say it's hard for us, right? Like because we've been in it and for us especially for like researchers like you don't operate with negativity that much. Like if something doesn't work, it's a learning and like you put on top of it.

From your point of view, what would you have expected to see and you are not seeing? What's your disappointment?

**Logan:** That's a good I wouldn't frame it as disappointment. Um but he hasn't

**Koray:** I have one part engineer part researcher so engineers can be more negative.

Um I mean I felt like we would make more progress on sort of continual learning and more kind of not so structured model architectures like right now we have which are like lots of experts. They're all very similar structure. I felt like a much more organic style thing would be something we

Yeah. Always imagine that kind of like bigger architecture. I still think that could be interesting, but we are not doing that yet, but you know what we're doing seems to work. So,

**Jeff:** I'm a little disappointed. Okay, we haven't um like cured every disease yet. You can't just like type in like invent me a cure for cancer or something and you know it'll just do it. But, you know, we're moving along.

**Logan:** Yeah. I think that and I'm curious to get y'all's reaction to this. I think it's not a negative thing, but it's like surprising to me. It seems like how much energy and effort it takes to sort of like merge the capabilities into a single model like obviously like and that it's like a really difficult like juggling act like you merge in a new capability.

It's not just like it works out of the box or something like that. You like trade off against something and you have to make some change to try to like make up those gaps. And I think it's not super intuitive to me as far as

**Oriol:** From my point of view that is one thing that I'm amazed with the models that there's still like there's insane amount of capacity in the model and we keep packing stuff like imagine that the current models are not like that much bigger than what was happening like 3 4 years ago.

Right but like we keep packing more and more and more capability and information. So like the fact that we can do that like there is so much room in the model maybe this is the negative part like but to me like we keep doing that and it's still there is room and there's so much more room in these models.

And like that's why it makes me actually excited because like in terms of algorithmic AI development there's a lot of room I really believe in that the models have much more capacity than what we are getting out of them right now. There's going to be big innovations that's going to enable us to do a lot more with the models.

**Jeff:** Yeah. And part of it I would say is we really need to come up with algorithmic things that just get much more out of every piece of data or example that the model sees or every token.

Because I think you know if you look at the efficiency of say human learning it's a thousand times better than what our sort of LLM learning can do. Like the LLM gets to see a thousand times as much data as a you know really capable human and then gets to like roughly capture similar capability maybe slightly better in some things and not quite as good in others but it needed a thousand times as much data.

So if we could make it so that you could get a thousand times as much information out of every example would be amazing. And a human has heard what like a billion words in a lifetime and then yeah a model has been trained on

**Oriol:** Trillions.

**Jeff:** Trillion trillions and can remember them. Yeah.

**Noam:** Do you disagree a bit though? Right. We're pre-trained. I mean it's not like you're the first human. So anyways there's some arguments also about that. But the source code is so small. We got like gigabytes of source code. Like

**Logan:** This is one of my questions. This is why you don't want this conversation happening. By the way, I have a hard one like in terms of what's been difficult.

**Oriol:** I think evaluation is very difficult. It's been somewhat underappreciated in the community even from the academic era that Koray was mentioning evaluating capabilities in isolation or what are the next big things that will happen and how to evaluate in a way that is not leaked into the data sets and that users will agree with the number that's been.

There's a lot of work and progress but I feel like that's been maybe surprisingly hard but perhaps because we came from a table of numbers in papers and now we have users and feedback that's just been a surprising and exciting because every time you find something difficult you get motivated by trying to fix it but evaluation is one that needs to keep getting better.

**Jeff:** I mean the whole dream of every AI researcher ever has been how do we build systems that can generalize to things they've never been confronted with and that's really you know even when you're training specific models on particular tasks, you want to generalize to new examples of that task.

But I think what we're trying to do now is generalize to anything anyone might ask. And that is kind of a hard problem. But by having a lot of users, you get a lot of feedback about okay, well, we're generalizing pretty well in these kinds of problems, but in these kinds of problems, we're falling short.


## Research Disagreements & Different Focus Areas [00:27:57]

**Logan:** One of the questions controversial questions that I had for you all was what is um you all have obviously worked together for a long time in different capacities. What are some like research things that you all still don't all agree on? Um and I want to preface this by I think this maybe this is a positive thing. The beauty of having people who have different perspectives is that there's disagreement and we try different things. I'm curious if there's anything that like comes to mind.

**Oriol:** I'm trying to... I'm trying.

**Logan:** Or you all agree.

**Oriol:** I don't think we would all agree but I don't think there would be like big major disagreements because I think like in the grand scheme of design of Gemini I think like this group has experimented with all sorts of things. I think we built a lot of ideas through experimentation.

I know that Jeff always had this idea of building something a little bit more flexible and has more plasticity and more fluid. We didn't get there but it's not like we disagreed on that. It's just that I think the current systems have sort of empirically showed us the way that like this is the model that we are doing and um but otherwise like I don't know if we had like big disagreements.

**Jeff:** At any given time each of us is kind of spending more of our effort on say one particular thing or a few things and the others are not necessarily spending as much time on that thing. So, you know, like I'm spending a lot of time on, you know, what should future inference hardware look like? Because I think that's a super important capability for us to have.

Um, and you know, you're not spending as much time, but I describe it to you in the kitchen. You're like, "Oh, yeah, that sounds good." Like, when can we have it?

**Koray:** Reality is a good way of getting people to agree. You see experimental results and see what works and what doesn't work. So,

I mean, in general, Gemini is quite data-driven, I would say. Like lots of people run experiments at small scale and then say oh yeah here's the results like oh that looks promising if you tried combining it with this thing and you need to use your pool of researchy compute in the most effective way possible and being data driven is

I think something like Gemini if you think about Gemini or AI in general it pulls in so many things like from hardware to like model design to product to everything. So I think having like this group to work together is actually one of the most important factors that actually make it work.

Like Jeff as he said like focusing on hardware like Noam is focusing on models. Oriol has been focusing on models now going very deep on agents and doing really like deep work there. And I try to focus on okay like where are we going with Gemini and like are we working well with the products? Are we getting that experience and like are we running well.

So I think all of us like work together in a way that are taking care of different important areas because it's a whole technology transformation that is happening and I think like having people who are deeply thinking about different aspects of this technology transformation I think that's what makes it work.


## Predictions for IO 2027 [00:31:01]

**Logan:** I love it. We should do predictions just so that we have something to be wrong about uh a year when we reflect back on this conversation. Uh obviously huge amount of progress, lots of exciting things from this year's IO. If we were sort of sitting here 2027, which sounds like a made-up year, um is going to be around the corner. 2027, we're going to be sitting here at

**Koray:** The made-up year.

**Logan:** I mean, just like I'm like 2027 just seems not real. Like it's so far in the future and it's 6 months away or whatever.

**Jeff:** I'm going to be 50.

**Logan:** Wow. Well, yeah, you're 50. Happy early birthday. Your 50th birthday. We'll be celebrating. IO 2027 any sort of predictions of things that you would you are hopeful that will actually land by then from a model capability perspective or anything like that.

Let's try to predict like IO 2027 and what are we announcing.

**Jeff:** No let's not do that.

**Logan:** Let's do that. Anything well like directionally directionally just like given where we are now it's like you know coding you know obviously we made a huge amount of progress on coding how you know will we be saturated will we still be spending as much time focused on it. Same thing with agents. Like just given like sort of the exponential that it feels like we're on for a bunch of these different capabilities.

**Koray:** Maybe I'll jump in. I think one thing that might be happening in a year's time is like self-learning.

**Logan:** Self-learning is the same as continual learning or different?

**Koray:** I think they're related. Maybe like for some it is the same but like we are in an era where like models are a lot more agentic and like they are very good at writing code. We use them in our research. I think slowly we're going to use them more and more in our research and there will be a point where at least at some experimentation level we are going to rely on the models to improve different parts of Gemini.

And I think like next year we will definitely be on that path and like probably talking about it would be my prediction. Let's see.

**Jeff:** We'll probably be able to point to like some very significant thing in our models that was generated by the models and agents working. So I do self-improvement. Yeah. Under the guidance of Facebook.

Hey. Right. And instead of suggesting to one of your team members, hey, why don't you like experiment with this a bit and let me know how it's going next week? We'll be telling the model to do that.

**Koray:** Hard to disagree with that one. But maybe to build on the continual learning what more as a capability. I mean the ability of a model to through its experience interactions to improve without the need to kind of update its weights some sort of like knowledge base update that works really well.

Right like I mean we have examples of this working but I don't think the capability has seen like a steep curve in terms of being so good that this would be an obvious thing that everyone would be using and turning on you know in the model. So that's one that I'm hopeful we'll see. One year seems possible. Yeah, maybe.

**Logan:** A lot of interesting weird problems on that to solve. I feel like I see examples all the time where you like ask in today's era of this you ask models the question. It pulls in some like random personal context that is like completely unrelated about a friend's birthday party and somehow that's related to my question that has nothing to do with it. So it does feel like it needs like another

**Koray:** A year. We're sort of in our own tech bubble, right? Like I mean because we are in the research of this like from your point of view and you are much more plugged into real world than us, I would say like what do you want to see? What do you expect?

**Logan:** That's a good question. This is not an interview Logan episode, but the

**Jeff:** Maybe we should have some of them.

**Logan:** No, you don't want to hear what I have to say. The model is the product. That's all I have to say. I want the models to get better. Um, no, I think the long-running stuff I think will be really interesting to see because it does I feel like that's like a frontier that we can like really easily track.

And like even if coding models get 20% better tomorrow and they're really good, like I still think you'll run into limitations for like how long you want the model to like run autonomously for and it feels like that feels like it's, you know, IO 2027 if we're able to say this model's been running for like 30 days or something leading up to IO like that would be like I think really surprising to a lot of...

And maybe we won't say that, but like maybe something to shoot for,

**Jeff:** But that quantity of work that is being done independently by the model would be the good. Yeah, would be surprising. And I think actually I think it takes the full stack to pull that off. It's like you're going to need sort of like memory systems and you're going to need continual learning and you're going to need better hardware because it's going to cost a zillion tokens to let something run for 30 days. So,

Well, and also you want your better hardware to have low latency because like if it finished it in one day, you'd be way happier than 30 days. 30 days is a good marketing line, but actually I'd be happy.

Oh, another prediction is I think well not a prediction for announcements, but I think one thing that these agents are going to stress is that all of our tools are too slow.

Right. Like a lot of the tools that these agents rely on, if you make the model infinitely fast, you are going to limit how much you can actually speed up real work because often they involve interactions with tools that are designed for kind of human latency

**Koray:** Or the frequency of working, right? Exactly.

**Noam:** 29 and a half days of those 30 days are spent like waiting.


## Three Products or Ten Thousand? [00:36:31]

**Logan:** Um, another actually maybe another sort of meta controversial question that I'm curious and I think Koray I like the research take of this which is why I'm interested. Um, I asked Josh this the other day which is like five years from now Google either has like three products or we have like 10,000 products. What do you think? What seems more plausible?

**Jeff:** We have one.

Well, only one product. Yeah, it's model.

**Logan:** Okay, I like it. Sure. Sure. I'll take that answer. What do the rest of y'all think?

**Jeff:** I mean, I do think if you have an incredibly capable model, it can do many, many things. And I think you saw in the search demos today at IO that, you know, it can even create little apps inside search that are customized for you and the visualizations and write code. So, in some sense, that's I don't know if that counts as one product or 10,000 products or 10 million products.

**Koray:** If there's a bunch of users. But like on a serious note like I feel like people want to consume information in different ways and I think something like search is fundamental and I think like 5 years from now we will definitely have search maybe with a much more magical box but I think the idea that people want to reach information and consume that information for themselves that like that learning activity I think it's still fundamental.

So I really think that it's going to be there and like probably we'll have many many more because it will be easy to do products because they're all powered by the intelligence more and more.

**Jeff:** Yeah. I mean I think there's many product outlets and there's you know a smaller number of things that make those products amazing. So like if you think about the glasses that were demonstrated at IO that's a product but it's going to be made better because the models are better and they understand audio better and they can speak to you better. But that's a distinct product from search.

**Oriol:** Exactly. Right. I think it's clear to us there's definitely one model powering whatever it is. I'm not an expert, but as a user sometimes I feel like, you know, I make an active choice of what I want to do with a digital device, right? Like I want to check my calendar, email, buy something.

And having that division that might be more of a human factor rather than the technology is incapable to present all these in a single product. But I feel like the choice of what I want to do that focus whether it goes away or we just evolve out of it I'm not sure but I find myself liking the separation of concerns sometimes. So betting on one product I would not do it at this time at least for myself.

**Jeff:** I guess we've been talking about the informational products that deliver information and there you can just talk about how do humans want to consume that information. Is it visual? Is it text? Is it glasses? Is it some kind of brain computer interface where you get like the models internal embeddings like straight into your neurons or something weird like that? But uh

**Noam:** Vector processing.

**Jeff:** But powered by you know the things like Omni like maybe we will get into physical products in the future and start moving atoms and not just bits but that is a prediction for the far future.


## What Everyone Is Building Outside of Work [00:39:56]

**Logan:** I love it. Moving atoms and not bits is the future. One more fast round things that you all are building. Um I'm curious if like sort of obviously all the AI coding stuff like just maybe maybe personal less Gemini specific anything interesting that y'all are doing it could not be with code too anything like you know physical atoms in the real world painting carpentry woodworking whatever it is.

Jeff you go first.

**Oriol:** I mean I think I'm just enjoying some of the consumer-facing products that we're putting out that are now much more capable. I made a cute little Mother's Day card for my daughter had her first baby so that was kind of fun.

**Koray:** I love building Mother's Day hearts as you all know we just like I mean we made the decision we moved here so that means a new house new house comes with all sorts of things that you need to fix learn adapt so like nowadays like house DIY like it goes from like home automation to like fixing stuff with a nail and hammer like so that spectrum and like I enjoy that like I like being able to do hands-on things.

**Noam:** I love... But I'm just trying to make the model smarter.

**Koray:** Build some new model architectures.

**Jeff:** Yeah, I've been trying to build a knowledge base of lots of research that I couldn't possibly process because we were too busy building and then create a brainstorming partner to just figure out what the next big things might be.

**Logan:** I love it. That's awesome. Well, thank you to all four of you for taking the time to sit down. Lots of controversial answers, but it was wonderful. It's fun. I made this comment last year at IO in a conversation. I think I made this to you, Koray, but I feel like IO and bringing people together and launching this stuff like you feel the warmth of like humanity as we build, you know, this technology together and sort of I feel this conversation made me feel that.

So I appreciate it. It was wonderful to sit down and talk. Um and thank you all. Thank you all for listening and for watching this episode of Release Notes. We'll see you in the next one.
