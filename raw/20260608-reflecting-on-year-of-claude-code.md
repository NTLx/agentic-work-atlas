---
type: raw
source: "https://www.youtube.com/watch?v=Hth_tLaC2j8"
author:
  - "Boris Cherny"
  - "Cat Wu"
published: "2026-06-08"
created: "2026-06-12"
description: "Claude Code 一周年回顾：Boris Cherny 和 Cat Wu 回顾 Claude Code 从内部项目到全球开发者工具的历程，涵盖 verification 最佳实践、auto mode 安全机制、routine/loop 工作流、context minimalism，以及工程组织如何围绕 AI 重构。"
tags:
  - clippings
  - claude-code
  - agentic-engineering
  - verification
  - auto-mode
  - context-engineering
---

# Reflecting on a year of Claude Code

One year ago, we made Claude Code generally available. What started as an internal project—an agentic coding tool that runs in your terminal—is now used by developers and organizations worldwide.

Boris Cherny (Head of Claude Code) and Cat Wu (Head of Product, Claude Code) look back on the Claude Code's first year, from a Slack demo that got two reactions to engineering teams deploying it across entire codebases. They cover best practices for verification, the thinking behind auto mode, their favorite routines and loops, Claude Code's adoption beyond engineering, the rise of context minimalism, and how to build for the AI exponential.

## Table of Contents

* The origins and evolution of Claude Code
* How to make Claude good at verification
* Roles merging: Claude Code beyond engineers
* Using routines for CI, code review, and more
* Boris' go-to feature: auto mode
* Securing auto mode: red teaming and evals
* Why loop is the next leap
* How engineering orgs and responsibilities are changing
* Is the future product or engineering?
* Working with hundreds of agents: using agent view, voice mode, and Remote Control
* From context engineering to context minimalism
* What's next for Claude Code

---

## The origins and evolution of Claude Code

**Boris:** When we first released Claude Code, it was like a little video and I remember posting it to Slack and there was like two people that gave the reaction—people were like excited. I thought it was really cool, especially for my very easy engineering tasks. It was quite good at it.

**Cat:** That's like a really nice way to say that it wasn't really good.

**Boris:** I can't believe it's only been a year since we first launched Claude Code. It's hard to remember what that was like. It's so different than what we're doing today. Now I just have like armies of agents that are doing stuff—I'm prompting one agent or I have an agent that's prompting agents that's prompting agents and it's like a tree of like thousands of agents. But I think the most important idea when working on this stuff is every single time Claude makes a mistake, I don't tell Claude to do it differently. I tell it to write it to the CLAUDE.md or to make a skill or something to do it differently. And if you can do this, then Claude can just run forever.

And I think the other thing that we kind of realized is that verification is really important.

## How to make Claude good at verification

**Cat:** We didn't realize that. I hear this come up a lot with developers and enterprises that we meet with. What are your tips for making Claude Code really good at verification?

**Boris:** I sort of feel like this is this thing that just everyone misunderstands because whenever we talk about verification, people are thinking like unit test or they're thinking like lint or like type check. These are the things that are obviously really easy to automate and these are the things that were already automated. But actually when we talk about verification for agents, it's something slightly different. It's like can the agent run the thing? It takes a little bit of mental work to figure out how exactly do you do this because it's often not straightforward. And I think that's one of the challenges.

I remember with Opus 4, Claude tested itself and we just hooked it up to Opus 4 and I was like, "Claude, build a feature and then test yourself in bash." And it opened a little Claude CLI and tested its own feature and I was just like whoa, it's crazy. Now we're so used to it. Now we have these loops going for the iOS simulator and the Android simulator and like computers for desktop. It's not surprising, but back then that was crazy.

**Cat:** How are you doing it? I've been mainly hacking on the desktop app these days and one of the engineers on the team actually added this desktop development skill that teaches Claude how to run the local desktop app and I've been having it use it and it still runs into issues or like bugs with the staging environment sometimes. And so what I have it do is in those cases I have it read Slack and understand hey is staging down right now or has someone else already hit this? And then when it debugs the whole issue I tell it to update the desktop development skill. What the skill does is Claude actually spins up a local desktop app and it uses computer use to click around it. And so when I add a new UX it clicks around to invoke the new UX. It also tests edge cases and when there's an issue it fixes it, saves it and rechecks.

**Boris:** This is like honestly one of my favorite things about this team is everyone codes.

## Roles merging: Claude Code beyond engineers

**Boris:** I have never been on a team where my PM would code and it's like crazy and your code is like really good.

**Cat:** Here's your noise. But I also just feel like it's also just becoming easier because it's essentially like Claude writes the code. And so what matters a little more is what's the idea that you have. And I feel like if you're a person that has the product context and the business context and you're thinking about the design and the user, you're just going to come up with better ideas. It's kind of like all the roles are merging.

**Boris:** I remember seeing Megan, our designer's PRs and I was just horrified at the beginning. I was like, "Oh my god, why is Megan putting up PRs?" And then she was like, "Yeah, yeah, I'm just fixing the button." And I was like, "Okay, all right. Well, the code looks good, so maybe it's fine." And I feel like now it's just totally normal.

**Cat:** Yeah. We see this across all the enterprises we talk with. The engineers adopt Claude Code first and then the adjacent roles look over their shoulder and they're like, "Wow, this thing is very powerful. Let me try it out." And we found—it's crazy—we found that our designers are more productive making prototypes and making changes directly in the app instead of paying an engineer. PMs are making changes in the app. Our finance team runs Claude Code. They do their projections there. Data science—if you talk with our data scientists, it's so cool. It's just everyone just has Claude Code up on their screens.

**Boris:** I feel like it's remarkably versatile for different roles.

## Using routines for CI, code review, and more

**Cat:** What do you feel like nowadays are the use cases that are pushing the limit?

**Boris:** One that I'm super excited about is routines. There's one engineer on our team who launched voice mode across all of our products and he has this routine set up that just listens for every ticket that comes—every GitHub issue, every bug report about voice mode—and his Claude just picks it up proactively, puts up a fix, and then pings the PR to him. And when he got that working for voice mode, he thought, "Okay, we're getting a lot of other feedback that isn't being responded to." So he also set up a routine to listen for that.

So I shipped this small feature and there was like an edge case in it that I didn't see. And so someone filed a bug for it and I was going to get to the bug that night. And as my Claude was working, it said, "Wait a second, another Claude has already fixed this." And I was like, "How's this possible?" I've never talked to him about this feature before. And so I pinged him and I was like, "How did you fix this so quickly?" And he said he has another routine that just looks for bug reports that haven't been responded to in 5 hours and puts up a fix and he merges the ones that are easy to verify.

**Cat:** Claude tells me this like all the time now—that someone else has already fixed it. There's always like another person's Claude that's working on it.

**Boris:** Yeah, that's been one of the changes. I feel like we're—a while ago we were trying to figure out how to use routines. And I feel like the agent SDK was this first idea that we could use Claude Code programmatically, but at the beginning it just wasn't obvious how do we use it? What do we use it for? And I think routines are the first really obvious application. It just does all the code review. It babysits every PR. Remember back in the day you used to actually have to respond to code review comments. You used to have to fix CI. You used to have to rebase.

**Cat:** Yeah.

**Boris:** I haven't done that in a long time.

## Boris' go-to feature: auto mode

**Cat:** When you're in the CLI and you're synchronously working with Claude, what are your go-to features?

**Boris:** Okay. What they used to be is plan mode. I don't use that anymore. I use auto mode.

**Cat:** Auto mode instead of plan mode?

**Boris:** Yeah. Because the newer models—they don't actually need a planning step anymore. I think this was really important for like Opus 4 through maybe 4.5, then I think starting with 4.6 and definitely with 4.7 it just doesn't need that planning step. I think some people still use it. They like to have that artifact. I don't use it and I just do auto mode for everything because then I start my Claude, it starts to work and then I just move on to the next Claude and I don't have to sit there and watch it.

But from the very early stage we had this permission prompt model for Claude Code, right? It runs a tool and then it asks you like hey are you okay running this tool and you had to say yes or no. And at the time that was kind of the best we had a year and a half ago because we didn't have classifiers, the model was not as well aligned as it is today. So auto mode was just such a big step up because actually you don't want to read most of these requests—just routing it to a different model and having it check for security works so much better.

**Cat:** Yeah. And if a thing is a little sus or you know this isn't a command that you think you want to run or it's not safe, the model will just deny it and then you can go back and you can allow it later. I think this has been one of those step changes. We just—there's no way we could have done this a year and a half ago.

**Boris:** It's just human nature when you accept 99% of requests that your eyes just glaze over when you read it.

## Securing auto mode: red teaming and evals

**Cat:** And so actually we feel that auto mode is more safe than reading every single permission prompt because it means that you're only paying attention to the most important thing and not being spammed a bunch of things that are just 99% yes. I think security is one of these things like you can talk about it and then it's a totally different thing to actually do it correctly because it just doesn't always look the way that you think it's going to look and it's just all about always red teaming, always pentesting, always having a threat model and then using that to figure out how is this thing going to get attacked, how are people going to get prompt injected.

**Boris:** Exactly. And I just feel like the team is just obsessed with this and it's so important because as a result I just trust the agent to run and I can move on and I can just have a second agent. And if I didn't trust it, then I just wouldn't have been able to do that.

**Cat:** And internally, to actually get auto mode out to our users, we needed to really trust it first. And so what we did was we collected thousands of transcripts of an entire agent trajectory and a permission prompt and had auto mode classify whether or not it was safe. And it was extremely good at this. So then we got red teamers and we asked them to try to prompt inject and try to hack the codebase and we used this to create evals and made sure that all of these were denied and then we had our own internal teams try to prompt inject and hack Claude Code's auto mode and then we improved auto mode to make sure that we caught all of these. So it's not only just protecting you against the vulnerabilities that are out there in the wild today, but the most intelligent attacks that we can construct.

**Boris:** Yeah. I mean, it's honestly like a weird approach. I feel like there's all these features the last year where the first time someone pitched it, I was like, "Ah, no, no way. That's not going to work." And I feel like over time I just learned like I'm actually wrong so often now because building on the model is so weird. It's just all this engineering stuff that I've learned over the years—so much of it I just have to throw out. And this is just part of what the job is now. Like we're building on a new thing and we just have to relearn it. And auto mode was definitely one of these. The first time I heard it, I was like route the prompt to a model? No way. That's not going to work. And then it actually turns out empirically it works really really well.

## Why loop is the next leap

**Cat:** I heard you also love Loop.

**Boris:** Yeah, I love Loop.

**Cat:** How do you use it?

**Boris:** I think for Loop there's this transition that we went through like a year and a half ago where we were like all right there's source code but actually the thing an engineer should interact with—maybe it's not the source code, maybe it's the agent. And so we made this leap of like I don't write the source code, I talk to an agent and the agent writes the source code for me. And I think right now what's happening is we're making the next leap—I don't talk to an agent anymore, I talk to a Loop or I talk to a routine and it prompts Claude for me. And it's just crazy. I mean, it's been a year and a half and this is two big leaps.

## How engineering orgs and responsibilities are changing

**Cat:** If you take a step back, how are you seeing entire engineering orgs change?

**Boris:** I'm going to put on my business cat hat. I have this favorite case study. This is a Harvard Business Review from the '90s and they were talking about computers are here. Why are we not seeing the productivity benefits? And it's just this amazing snapshot into what it actually felt like at the time because people used to use mainframes, at some point companies switched to personal computers. It was sort of a new thing and companies were trying to figure out how to use it the same way they're trying to figure out how to use AI right now. And it turned out that to get the productivity benefits from computers, what you had to do isn't like you have your paper filing cabinet and your paper and pen business process and then there's a computer on the side that does something. Actually, what you have to do is you throw out the filing cabinet. You have to throw out all your paper and all your pens and then you put a computer in the center and everything has to run through the computer. It has to be at the center of every business process.

And I feel like at Anthropic we do this thing where when you onboard, you don't ask people questions. No one asked me questions when they onboard. You probably have the same thing. They ask Claude. And this is kind of weird. This is the first company I've been at like that. And I feel like for us, Claude is just at the center of everything. Whenever I have a question, I ask Claude. Whenever I write code, I use Claude. Whenever I need a code review, Claude does it. Whenever I need a security review, Claude does it. Whenever I need to fill out a form or something, Co-Work does it. So it's just Claude is at the center of everything.

And I feel like the companies that are really figuring it out, and there's a bunch of them now, they're just putting Claude at the center of it.

**Cat:** But I think for computers, the transition took 10 to 15 years. But actually for AI because so much of our work is already digitized and Claude can use a computer and it can write code and run code, this transition is happening a lot faster.

**Boris:** I think it's just really exciting. Like I feel like now I don't have to bug people anymore. And when I interact with people it's because it's fun and I get to collaborate with them on stuff and we get to create something together. It's not that I need something from them because Claude can actually do a lot of that stuff now. And I also feel like as an engineer, I've just never had this much fun doing engineering because the tedious part I don't have to do. Like I'm just coming up with ideas. I'm talking to customers and every idea—like I don't have a to-do list anymore. Claude just builds everything. And so my job is to come up with these ideas and it's just so fun.

## Is the future product or engineering?

**Cat:** Okay, so here's a question. Is the future product or engineering? Like is everyone going to be a PM or is everyone going to be an engineer?

**Boris:** Everyone's going to be both. I feel pretty strongly that these roles are merging. Like when we look at our team, our product team all writes code, our devro team all writes code, our design team all writes code. And then we look at our engineers and a lot of them ship products end to end. They have an idea for what to build. They build it. They work with legal and marketing to figure out how we communicate this to the world and make sure it's safe and with security too. And a lot of times they just see through this whole process end to end.

So I think right now AI really benefits people who have a lot of curiosity, have a lot of product taste, who love to have this end-to-end ownership. And now a lot of people are running hundreds of agents.

## Working with hundreds of agents: using agent view, voice mode, and Remote Control

**Cat:** What are the products that you think people should be adopting as they transition from single to multiple to hundreds?

**Boris:** Until recently, the way that I wrote code was I had like six terminal tabs with six git checkouts of the same repo and then I would just tab between them. Now it's pretty different. I have one tab. I use the new agent view that we just shipped. It's so good. And I'm so glad that we took a while to iterate on it to make that really good. And I also use the desktop app because I don't have to fiddle with checkouts that way. It just does the work tree cloning—it creates the work trees for me. And the thing that I would not have expected 6 months ago is probably half my engineering now I do on my phone. So I just have so many agents running that I just start from my phone. I use remote control which is amazing now. And I'll start something on my computer and then I'll just remote control in from my phone and I'll just walk around. I'll get coffee and then I'll check in on my agents and maybe I'll start another agent.

And sometimes I'm talking to someone and we come up with a new idea. I'll just start an agent on the spot. I'll talk to it with voice mode and just have it build something and I don't even have to go back to my computer anymore.

**Cat:** I remember when you started doing this because you would actually leave work, have your computer on your desk open, plugged in, screen locked, and I just thought you would come back to the office at some point to get your computer, but then we were pretty late. And I was like, hm, maybe you just left it here by accident. And then it happened again the next day. And the next day. And I was like, "Wait, this is so weird because you're landing PRs so your computer is right next to me." And I remember you responding and you're like, "Yeah, I'm coding from my couch."

**Boris:** Yeah, that was the week that remote control got really good.

## From context engineering to context minimalism

**Cat:** So, another thing that users are asking about all the time is how do you do context engineering, especially in a large enterprise?

**Boris:** This is a thing—people used to talk about prompt engineering, they used to talk about context engineering. This is sort of matching where the model was at the time. Back in the days of Sonnet 3.5, you had to prompt engineer. Back in the days of Opus 4, you had to context engineer. But with the models of today, you don't do any of this. You give it the minimal possible system prompt, the minimal possible tools, and then you let the model figure it out. Like you just have to give the model some way to pull in the context. I think that's the most important thing.

**Cat:** How do you think about it?

**Boris:** I see things very similarly. I'm a context minimalist. So my general philosophy is tell the model only what it needs to know and let it figure out the rest of it. I think when you give the model too much context, it's kind of like you're micromanaging it. And sometimes the model knows a better way to get to the same outcome. And I personally prefer to give the model that freedom to do that. And then in general, we're also making our harness more lean so that you have more room for your own prompts. And so that follows your promise better.

**Cat:** There's all these different ways to use Claude now.

## What's next for Claude Code

**Boris:** But I feel like in a year it's going to be a totally new set of things and it's going to be so surprising if it's still these same things because I think we're seeing these giant trends happening right now. Agents are running for longer. They're more autonomous. Very rarely am I running one agent at a time. It's usually like a few agents or dozens or hundreds or thousands. And so the form factor for that, it's going to be really different than what came before. And I don't know what it's going to be. And I think in a large part it's going to be up to the team to figure it out. And this is why I'm so happy we run the team the way that we do where everyone just comes up with ideas and everyone is able to think about the product. Everyone talks to users all the time because I don't think these ideas are going to come from us. It's going to come from the team.

**Cat:** Totally. And from everyone in our community building with us.
