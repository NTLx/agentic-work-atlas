---
type: raw
title: "L8 Principal's Agentic Engineering Workflow"
source: "https://www.youtube.com/watch?v=iQyg-KypKAA"
author:
  - "Kun Chen"
published: "2026-06-20"
created: "2026-06-22"
language: en
duration: 2746
tags:
  - clippings
  - agentic-engineering
  - agent-harness
  - workflow
  - verification
  - multi-agent
---

# L8 Principal's Agentic Engineering Workflow

> Kun Chen — 前 Meta/Microsoft/Atlassian L8 Principal Engineer，近年在 Atlassian 构建前沿 coding agents，日常 ship 40-50 个 production commits。

Find everything from me here: https://linktr.ee/kunchenguid

## Chapters

| # | Title | Start |
|---|-------|-------|
| 1 | How to watch this video | 00:00 |
| 2 | Why I work in the terminal | 02:10 |
| 3 | WezTerm and my lua config | 03:49 |
| 4 | What is tmux | 05:09 |
| 5 | Neovim as editor | 07:18 |
| 6 | Agent harnesses | 09:21 |
| 7 | My global memory file | 11:24 |
| 8 | Project level memory file | 14:50 |
| 9 | Using skills | 16:12 |
| 10 | How skills may hurt your agent | 18:40 |
| 11 | Voice input | 20:27 |
| 12 | The importance of agent ergonomics | 22:12 |
| 13 | Planning with interactive artifacts | 24:25 |
| 14 | Validating code changes | 28:29 |
| 15 | Long running tasks | 33:12 |
| 16 | Parallel worktrees and agents | 36:20 |
| 17 | First Mate | 40:23 |
| 18 | The captain's mindset | 44:26 |

## Tools Mentioned

- WezTerm https://wezterm.org/index.html
- tmux https://github.com/tmux/tmux/wiki
- Neovim https://neovim.io/
- npx skills CLI https://github.com/vercel-labs/skills
- OpenSuperWhisper https://github.com/starmel/OpenSuperWhisper
- AXI https://axi.md/
- Lavish https://github.com/kunchenguid/lavish-axi
- No Mistakes https://github.com/kunchenguid/no-mistakes
- gnhf (Good Night Have Fun) https://github.com/kunchenguid/gnhf
- Treehouse https://github.com/kunchenguid/treehouse
- First Mate https://github.com/kunchenguid/firstmate

---

## Transcript

Hi everyone. Welcome to this video and this will be a full walkthrough of my agent engineering workflow. My name is Kun. I was previously an L8 principal engineer, worked at Meta, Microsoft, and Atlassian on many large scale systems like the Bing search engine, Windows, and Facebook games. In the recent couple of years, I have been building frontier coding agents at Atlassian and helped many engineering teams figure out how to use them effectively.

I have been building heavily with agents myself and shipping 40 to 50 almost every day, sometimes more. And these are all well tested and shipped to production, not those Minecraft demos you see people vibe code on social media. I have shaped my workflow to be both highly productive and enjoyable.

Many people recently asked me what it looks like. Be honest, I did debate a lot with myself whether I should make this video a paid course because it does have that level of value, but ultimately I decided to just share it here with everyone because I want to stay focused on building products as my main business. You can see this is a bit of a long video, because I'm going to walk through many fundamental concepts of agent engineering that not only show you how I do it, but also the why and how things really work under the hood. These are not gimmicks that look cool but can't actually be used for real work. These are all real workflows that professionals like myself use to get real work done. By the end of this video, I want you to feel like a captain that can sail a large ship with a crew of agents working for you, and do so in a stress free and satisfying way.

Largely speaking, we will be walking through these chapters. We'll start with assembling our ship, where I will introduce the core setup. We will then talk through how we recruit and ramp up our crewmates with the right usage of memory and skills. I will then demonstrate how we work with a single crewmate effectively. Then we'll upgrade to working with multiple crewmates all at the same time. And lastly, we will recruit a first mate that manages a lot of the overhead for us so we can focus on the big picture.

### Why I Work in the Terminal

As we get into my workflow, something that's going to be really hard to miss is that I do almost everything in my terminal. I know there are a lot of people who will tell you that the graphical user interface is better — it allows richer interactions and better visuals — but I think by the end of this video, I might just be able to convince you that terminal is not quite that yet.

I use the terminal mostly for two very real reasons. One is to allow my hands to almost never have to leave the keyboard. This is actually a much bigger deal than most people think, because when your hands stay on the keyboard, you stay in the flow. But if you have to move your hand to the mouse every couple of seconds, it breaks the flow and forces your brain to context switch. I know there are some GUI apps that also have great keybinds that allow you to do most things with the keyboard as well, but that's just not the primary interaction paradigm for GUI apps. And it's hard to build the discipline of hands on keyboard when every once in a while you still have to use the mouse. Terminal apps, on the other hand, are all designed for the keyboard, so there is no reason for your hands to move anywhere else.

The other very important factor that drives me to use the terminal is that I can keep the exact same workflow everywhere, even on my phone. But if you really don't like the terminal, that's okay too. I designed this video to be more about the fundamental concepts behind agent engineering rather than the mechanics. So most of the things that I talk about should be applicable to GUI based workflows as well.

### WezTerm and My Lua Config

This beautiful, clean and elegant terminal emulator you are looking at here is called WezTerm. WezTerm is a highly performant terminal emulator built by a guy named Wez. It's got 26k GitHub stars and has existed for many years. I like it mostly for two reasons.

One is that it's truly cross-platform. It's pretty much the only terminal emulator I can find that can work on Windows exactly the same way it works on Mac and Linux. Right now I mostly only work on Mac, but it was a big lifesaver when I was working for Microsoft and was forced to use Windows for work. The other reason is that it's highly customizable. You can write Lua scripts to configure pretty much everything.

Here let me show you my config in my dotfiles. It's all in this file called wezterm.lua. It's a Lua script, so it's not just static values. You can actually set conditions and write various kind of logic to make your config very dynamic and flexible. If I change some settings here, let's say I change the color scheme to chalk, you will see that it does a hot reload instantly, which is super handy.

### What is tmux

Inside of WezTerm, I run something called tmux. It's short for terminal multiplexer. If you haven't come across this yet, it's probably easiest to just show you what this does. So I'm typing this command here to start a session. Now I'm inside of tmux.

You can see not much is different except for that there is a bar at the top showing some information, and I still get a shell where I can type commands. But now I can split my terminal into multiple panes, as many of them as I like. This is super useful because I can spin up an agent in one pane and spin up an editor in another, and still have a pane to myself so I can just run commands. I can also spin up multiple tabs, and they are also called windows in tmux. This is very useful for running multiple agent sessions in parallel.

The other cool thing is that tmux sessions are persistent in the server. So if I use a keyboard shortcut here to detach from tmux, you can see I'm back in the normal shell without the status bar at the top. But if I type the same command to launch tmux again, I get back to the exact same state I was in, so I can continue my work here. What's even more useful is that I can connect to this same session from another device, like my laptop or my phone. That's a real game changer. That's very hard to replicate without this terminal centric workflow.

### Neovim as Editor

This text editor here is Neovim. It's basically the modern version of Vim. It's my favorite text editor. If you are not familiar with Vim yet, it's an editor whose main purpose is to keep your hands on the keyboard.

So if you watch my keystrokes here, I can move the cursor up and down, left and right with keys. I can also scroll up or scroll down. If I have to make edits, I can go into insert mode and start to type anything I like. There are a ton of keyboard shortcuts for doing everything you need. For example, let's say I want to delete the current line. I can just type dd and it's gone. I can undo it by typing u. And if you look at the left hand side I have relative line numbers.

I also have a bunch of plugins that help me get around in Neovim. And I have keybinds for all of them. Like space S allows me to search or grep for the codebase. I can type space F to find files by their names. Working with Neovim has a learning curve for sure, but once you get used to it, it just feels really, really good. Whenever I'm in Neovim, I'm just flying like a bird and it's awesome.

### Agent Harnesses

Our ship is ready to sail, but we have no crewmates yet. We can't do everything by ourselves. We need to bring in agents as our crewmates. I use four different agent harnesses regularly.

There is Claude Code, which is basically the only practical choice if you are using the subscription from Anthropic. Generally speaking though, it's a pretty good harness. I think it has the most sensible default experience out of the box. It's also got a pretty rich feature set. The downside is that sometimes it's a little bit buggy, and it's not as customizable as some of the other options.

The next one I use a lot is Codex CLI. It's written in Rust, and you can feel it's a little bit smoother than Claude Code when you use it. It's also open source, so if you run into some problems, you can often just have Codex inspect its own source code and figure out a workaround by itself. It's a bit lacking in terms of bells and whistles, and it's also not very customizable.

And then there is the Pie coding agent. Its whole philosophy is to be minimal and highly extensible. It's great if you don't want any bloat and you'd like to tinker around and kind of make it your own.

And lastly, there is Open Code. I like it a lot. It's got a beautiful smooth TUI, and it's got good integration with pretty much every model you can find. It's also got a more complete out of the box feature set than Pie. So if you want to use an agent harness that is model agnostic and one that you can just grab from the shelf and just go, Open Code is a pretty good choice.

For the rest of this video though, I'm going to use Claude Code because I know many people are already familiar with it. But I have been very strict about making my workflow agent agnostic because the landscape is changing very, very fast. Who knows which model or agent will be the best performing one next month? So everything I show here in the video is agent agnostic and should be applicable regardless of which model or harness you use.

### My Global Memory File

The problem with these crewmates is that they are fresh recruits, and they have no idea how we run our ship or how we like to work. We need a proper onboarding process to ramp them up. We will do this mostly through two ways: memory files and skills.

There are a few types of memory files: global memory files and project level memory files. The global memory file for Claude Code is at `~/.claude/CLAUDE.md`, and every other agent uses the other standard location `~/.agents/AGENTS.md`. So what I do is I use a symbolic link to make them both point to the same file.

Here's the content of my actual global memory file. You can see it's pretty minimal. There is only 27 lines. Because everything in this file gets loaded into the system prompt of every single agent session across all our projects. If we have too much content in this file, it will silently use a lot of our tokens.

I mostly write down my personal preferences here, like "never use em dash." Somehow AI models are trained to use em dash by default instead of a plain dash. So now whenever I see em dash, I just feel like it's robotic. And I don't like that when I need the agent to write something for me, like PR descriptions.

Oh, and this is a good one: "When making technical decisions, don't give too much weight to development cost." Here is something interesting that you may not know. If we ask a frontier model to estimate the development cost of a project, let's say I want to build a 3D first person shooting game that I can play locally with AI enemies. How long do you think that will take? Let's see what Claude will say.

Okay, here it is. See, the estimate is in days and weeks and months. But if we ask the agent to actually build it now, I can guarantee it will come back with a playable version in just a few minutes. Because I have done this so many times. This mismatch is happening because the models were trained from human data, and that is what a typical human developer would give as the estimate. AI doesn't seem to know it can code much faster than humans yet.

When AI is making technical decisions, it's implicitly assuming the development cost for some of the options are much higher than they actually are. This biases the model to choose cheap solutions that are often low quality, not scalable, or hard to maintain. So I have this rule here to correct that bias.

I also said "when doing bug fixes, always start with reproducing the bug in an end-to-end setting as closely aligned with how an end user would experience it as possible." AI models today by default like to write unit tests, which are often not sufficient and not really covering the product behaviors we want to guard. I found that leaning into end-to-end testing is a lot more reliable.

### Project Level Memory File

Besides the global memory file, each project can also have a project level memory file. Let me show you one example here by going into this project called HighBit. This is an AI Twitter app I have been working on.

The project level memory file is typically stored as `.claude/CLAUDE.md` or `.agents/AGENTS.md` depending on which agent you use. I do the same thing here with a symbolic link, so the same file is shared for both Claude and other agents.

This one we are looking at here is a little bit verbose. Let me show you on a high level what I put into this file. It has some context on what this project is, how the repo is laid out, some terminology, how some of the most important components work, how to do end-to-end testing, and some conventions at the bottom.

This file is a lot more verbose than the global memory file, because this is basically the collective learning of all the agent sessions in this project. The way I built this file is not by writing everything by hand, but rather that every time I saw the agent doing something wrong, I would correct it and ask it to remember to not make the same mistake again by storing the learning into this memory file. So over time, our crewmates working on this project get smarter and more experienced. You don't need any fancy memory system to do that. This markdown file is all it takes.

### Using Skills

Over time, the memory file does tend to get more and more bloated though. One way I reduce the size of this file is by moving some conditional information that is not always needed into a skill.

For example, the end-to-end testing instruction here is only needed if the agent is making code changes, right? So if I just ask the agent a question, this whole section is totally useless and would be wasting tokens. The way to improve efficiency here is by converting this kind of conditionally useful information from the memory file into skills.

I typically just ask the agent to do this. Cloud already knew how to do this — what skills mean and how to create them — but other agent harnesses may not understand how to do that out of the box. To teach your agent how to create skills, you can install a skill called Skill Creator which was written by Anthropic. You can do that by running `npx skills add`. This npx skills thing is a CLI from Vercel that is very handy. It's basically my main tool for installing and managing skills. It supports pretty much any agent.

Once this skill is installed, your agent will be able to follow the rules and create new skills for you moving forward. Let me show you what Claude created for us. It basically removed a large chunk of the content from our AGENTS.md file and moved that into a skill file.

This is a good thing about skills — it's designed for progressive disclosure, which means when your agent starts, it only loads this tiny description field from your skill into the system prompt to know what the skill does. And only when it actually decides that it needs to use a certain skill, it will then read the rest of this file. This allows you to store a lot of the knowledge about how to do various kinds of things without blowing up your system prompt and memory file with a ton of content that uses your tokens for every single request, whether the request actually needs those skills or not.

### How Skills May Hurt Your Agent

One thing I do want you to know about skills is that you should generally avoid installing random skills from the internet. Even the ones that have a lot of GitHub stars.

First of all, these skills can instruct your agents to run pretty much anything on your machine. This is a very risky thing to do, because the agent can leak your API keys or even credentials to your bank account to untrusted third parties without you knowing.

Even if we put aside the security problem, some of the skills actually degrade your agent's performance. Look at this repo here called Andrej Skills, which has 177k GitHub stars. That's massive. So it must be really good, right? I actually evaluated a skill in this repo with ProgramBench, which tests the agent's ability to build programs end to end. And the result shows that by using this skill, the agent will use 5% more tokens while making the results worse.

And if you look closely, this skill is not even written by Andrej Karpathy himself. I'm not here to criticize the author of this repo, though. I'm mainly saying that being popular is not the same as actually being good. A lot of the skills being widely shared today have not been rigorously evaluated, and are typically just some random guy who found something that worked for themselves and somehow got it to go viral. Their GitHub stars only tell you how popular they are and not whether they are actually helpful.

So as a general rule of thumb, I recommend that you do not install any skill from the internet that claims to magically make your agent perform better, but hasn't published anything rigorous that proves its claim.

### Voice Input

Now that we have memory files and skills to help ramp up crewmates, it's finally time to actually start working with the crewmates and set sail. The first thing about working with the crewmate is how you talk to them.

I have pretty much completely moved to voice input now. So instead of typing, I will just say "explain this repo in a concise way and give me a recap of what the recent PRs have been working on." This is just so easy.

There is an actual paper from Stanford that seriously compared the efficiency. And basically talking is three times faster than typing. So this is a very big boost in productivity. I also want to show you something interesting here. If we go to the references of this paper, look who's here. It's our guy Dario. What is the CEO of Anthropic doing here? Apparently if we follow this link, Dario was doing some speech recognition stuff back in 2016. Now we're using speech recognition technology to talk to Claude which is also created by Dario. What a small world.

The voice input we just did was actually transcribed locally using this app called OpenSuperWhisper. It's completely free and open source, which is what I think this type of software should be. It runs the Whisper model locally on your machine and does the transcription. And the quality is really, really good. So this is how I do most of my prompts.

The only case where I fall back to typing is when I need to give the agent a URL or a file path, or something like that. Trust me, you don't want to speak a URL out loud, whether it's by yourself or with other humans around.

### The Importance of Agent Ergonomics

If we come back to this prompt and let the agent run, you will see that because we asked the agent to look at recent PRs, it will need to call GitHub to fetch the data. This is an important thing to pay attention to, because agents rely on external tools like GitHub to do their tasks. The design of these external tools can greatly affect your agent's performance.

Take GitHub as an example. Many people use the GitHub MCP server for accessing GitHub. However, I ran this benchmark here that measured various kinds of ways to access GitHub. For the exact same task, using GitHub MCP server will cost you 3x more on token cost, and more than double the latency compared to using the CLI. If you are using the GitHub MCP, you are pretty much wasting both time and money for no clear benefits.

Now you can see there's this thing called AXI, which has the lowest cost but highest success rate. So what is it? Let me show you.

AXI is a set of design standards I authored after discovering the huge upside we can have by designing our tools to treat agents as a first class citizen and optimize for agent ergonomics. I created ten principles for how to make a tool highly efficient for agents. For example, using token efficient output format can save about 40% tokens compared to using JSON.

And then I built a few AXIs. Besides the GitHub AXI I showed earlier, I also built Chrome DevTools AXI and benchmarked it against other various browser tools. And here you can see the agents taking less turns and using less tokens to get the same tasks done with the AXI.

The main point here is: when you give tools to your agents, do some research on their efficiency because they can greatly affect how much mileage you get out of your agents. If you want to use the AXIs I mentioned earlier, you can just go to axi.md and find them in the catalog.

### Planning with Interactive Artifacts (Lavish)

Speaking of this catalog, there is something called Lavish AXI here. This is a very important tool in my setup. I pretty much rely on this tool for planning any kind of complex work. Let's do a real feature live and I'll show you how it works.

Let me first launch HighBit to show you what I'm trying to work on here. HighBit is an AI Twitter I'm building for kids. I'll just create a test profile here. You can see here at the top I have these two buttons — "What I Can Do" and "My Progress." They are showing very similar content right now, which is a problem. And also the UI is not very exciting or fun. So let me go back and talk to Claude.

I'll still use voice input here. I'll just say "I'd like to consolidate the 'What I Can Do' and 'My Progress' buttons, because their functionality is very similar and I'd like to revamp the experience there to be something more fun and exciting, like an achievement system. Come up with some options and let's discuss. Don't use Lavish."

The reason I said "don't use Lavish" is that I wanted to show you what the default workflow today looks like for many people. And then I'm going to show you the difference Lavish makes. Because I already have the Lavish skill installed, my Claude will automatically use Lavish for this type of question, which is why I had to tell it not to do that right now.

Claude has come back with a response. Sometimes it will use its plan mode, or sometimes it will ask you to write down the plan in a markdown file. But it's more or less the same — it's a wall of text I now have to read through. It's not very easy to understand what each option is actually going to look like. And if I'm not happy with some parts of it, I can't very easily tell Claude which parts I'm talking about. I can select a piece of text in the plan and say "this is wrong."

Now let's try the exact same prompt with Lavish. Claude would roughly do the same things to figure out the options, except at the end it would not print out that wall of text. It will launch the browser and show me this page. Now look at this — this is the Lavish editor. The reason I named it Lavish is that it's richer than a rich editor.

Lavish editor basically instructed the agent to create an HTML artifact to visualize what we need to discuss. It always uses the same design system as the current project being worked on, so this is consistent with how the app actually looks. This makes it very easy to review concepts and prototypes. See the options are laid out here. This is so much easier to understand than the huge wall of text we were looking at in the terminal, right?

I can also annotate and make comments on specific parts of the artifacts to give feedback to the agent. This is something that's really hard to do with the wall of text or a markdown file. And at the bottom, there are things for me to decide on, and I can just click on these options to make the decisions. I just sent this feedback back to the agent inside of Lavish without even having to go back to the terminal. Honestly, I can never go back to reading text in the terminal anymore. This is just way too much more efficient.

Now the agent has made updates to the plan and I feel happy about this, so I'll just tell the agent to start building. We can then go back to the terminal now and see the agent will start to work on the implementation. Because we already clarified all the requirements in the planning phase, I typically don't need to interfere at all during this implementation phase. I only come back when the agent has done.

### Validating Code Changes (No Mistakes)

When the agent says it's done, that's actually when things get really tricky. This is where a lot of people will spin up their editor and start reviewing the diff. The problem is, AI writes code so fast, and if every piece of code requires your review, then you are creating a big bottleneck on yourself because you can only review so many diffs every day. Your velocity will be hard capped by it.

And even more importantly, reviewing diff is just not fun. No one says "I became an engineer because I love reviewing diffs all day." My advice here is that in order to really scale ourselves with AI, we have to think of ourselves more as an engineering manager or engineering director. Your directors most likely don't review any PRs yet. They can influence the quality of their team's software by creating good culture and processes, and rely on the team to carry them out. That's what we should do with AI.

What I do here, when the agent says the work is done, is not to start reviewing the diff or start manually testing the changes. That's too much overhead on myself. I send the change into a pipeline I built called No Mistakes. No Mistakes is also free and open source.

It orchestrates your agent to execute a series of steps that takes this first pass code all the way through to a clean PR. It would:

1. **Create a branch** if one doesn't exist yet, and create a commit
2. **Isolated worktree** — takes it through a pipeline in an isolated worktree, so nothing during the validation would affect your current repo
3. **Understand intent** — analyzes your agent session to understand the real intent behind the change
4. **Rebase** — rebases the change on top of the latest main branch on remote origin and resolves merge conflicts up front
5. **Adversarial review** — starts an adversarial review in its own fresh context window. This is where most problems get caught. Obvious problems will get self-corrected, but ambiguous ones that have product implications will be escalated to us humans for a decision
6. **End-to-end testing** — tries to test the change end-to-end against the original intent. This step will actually record evidence that proves the change is working
7. **Documentation pass** — updates all relevant documentation to reflect the latest change
8. **Linting** — makes sure there are no linting problems
9. **Push and PR** — pushes the branch to remote and raises a PR
10. **PR babysitting** — keeps babysitting the PR until it's merged, handling merge conflicts and CI pipeline failures

Another way to trigger No Mistakes is as a skill. I can just type "no mistakes" in the agent and it will do the same pipeline.

This may seem very slow, but in practice I never stare at this screen. I would go spin up other tasks. I come back only when No Mistakes says all checks passed. That's when I go to the PR and apply my judgment.

Here's the PR from the change we just did. We can see here it summarized the original intent, what's changed, how it's tested, and what happened during the No Mistakes pipeline. We can click to see the evidence from its testing to know whether it really has done what we asked for. Depending on what the change is, the evidence could be a screenshot, a video demo, a log file, or something else. It's designed to give you the most direct way to see the change working as you intended.

We can also see that the pipeline discovered some problems and fixed them before raising the PR. This is a good time to audit whether these changes are actually what we need. If anything doesn't look right, we can go back to the agent and ask for more changes before merging this PR.

The risk assessment here is also very useful. I basically look at this to decide how much time I should spend on reviewing this change in more detail. For low risk changes, I don't really look at the diff at all, because I have validated time and time again — for low risk changes, any problem I could catch is very likely already caught by the pipeline. Only more risky changes are worth my time.

This is how I scale up the volume of code changes I do every day through a large crew of agents, without losing control on quality.

One thing we are starting to see now is that the place where I spend time is towards the beginning and the end of the task. At the beginning I would spend time in Lavish to plan the requirements more clearly. At the end I would come in and hold the bar on quality. All these parts in the middle is done by AI, which frees me up to spin up other tasks.

### Long Running Tasks (Good Night Have Fun)

This is a core aspect of how I work, and you can see the more time I can free up in the middle, the more work I can go do in parallel. So an interesting question now is: how do we get the agents to work for longer and longer in the middle? That depends on us giving them more and more complex tasks that take longer to complete. But more complex tasks are often not as easy for our agents to complete autonomously.

An extreme version of this is when I go to bed. I sleep for 7 to 8 hours every night. How do I keep the agents busy for 8 hours? This is where I say "good night, have fun." It's another free and open source tool I built specifically for long running tasks. It's becoming quite popular.

It's that simple to use. Just give it an objective and it will keep going until it meets some stop condition you defined. Let me show you a real example that I often do. This is again in the HighBit repo. I will run `gnhf` (Good Night Have Fun) and give it a prompt:

> "Pretend you are a seven year old kid and use the HighBit app end to end. Don't mind the profile creation step which is designed for parents. In the rest of the app, try to do different things and find the first usability problem that would confuse you as a kid, or stop you from knowing how to proceed. If you find a problem, stop and fix it, then rinse and repeat."

Good Night Have Fun is now running in a loop to execute on what I just asked for. I can monitor token usage here or how many iterations have been done. The iterations will be showing up as the moons in this row, and I can see how many commits have been made as well. Or I can just go to bed knowing the agent won't stop until there is no more problem to be found.

When I wake up, I can review a list of commits made on this new branch and decide which ones I want. I typically use Good Night Have Fun for improving on some verifiable objectives or objectives where I trust the agent to have reasonable judgment over. Verifiable objectives are more like reducing page load time, improving end-to-end test coverage, or like "try different hypotheses to improve on the metric." These are all well suited for a long running loop.

The recently introduced `/goal` command in Codex and Claude Code can also do something similar. Good Night Have Fun still gives me a better experience because I can set a token cap or iteration cap or stop condition more precisely, whereas in Claude Code and Codex, if I set a goal before I go to bed, I might wake up realizing my weekly quota is all gone.

### Parallel Worktrees and Agents (Treehouse)

Good Night Have Fun solved a very important problem, which is to keep the agents running for a long time. So when the agents are running, I'm freed up to do more things. This is when we level up and start working with multiple crewmates in parallel.

So let's spin up another tab in tmux and get more work started. Now here's the problem. In this directory I already have Good Night Have Fun running. So if I spin up another agent working in the same directory, they will step on each other's toes and cause conflicts.

The default solution here is git worktree. For those of you who aren't familiar with it, a git worktree is basically creating a clone of your repo directory. I can create one by typing `git worktree add` and give a path here. Now we have a worktree and we can navigate to it. This is a separate directory on the file system, so we can have an agent doing anything here and it won't conflict with Good Night Have Fun, which is running in the original repo directory.

The problem with worktrees is that we now have something to maintain in our head. I need to remember "oh, I have highbit-2 here." Next time I come into this highbit-2 directory I would wonder what was I doing in this worktree last time? Is there still an agent running or is it done? All of that has to exist in my head, and there is no way I'm going to remember all that. So this worktree basically becomes a debt. To get rid of it, I need to run the remove command. This is just a lot of overhead.

My solution to that is another tool I built called Treehouse. It's very simple. I just come into this repo and I run `treehouse`. It would drop me into a fresh worktree where I can start doing whatever I want. I can keep spinning up more and more of these worktrees by running Treehouse again. And if I want, I can see a list of all the worktrees by typing `treehouse status`. So I can see which ones are being used versus not. When I'm done, I can just close this tab and Treehouse knows that I'm done, so it will free up that worktree for future use. Next time I ask for a worktree, it will try to reuse one of the idle worktrees instead of creating a brand new one.

So let's start some real work. I have a bunch of user feedback from my son's last round of playtesting, so let me use this first worktree we created and launch Claude, and I will say: "I remember it's hard for the kid to realize they can press and hold the voice input button to talk. By default they just click it and then they will see a popover. Maybe in the popover, we add a label that tells them they can also press and hold."

Then I'll spin up a new tab: `treehouse claude`. And this time I will say: "The image attachment dropdown menu should have an action that takes a screenshot of the current app and use that as the attachment."

All right, one more tab: `treehouse claude`. "Our agent status bar right above the chat input is not always showing bot activity. Look into what happened there and make sure when any bots are in progress, it always displays something that reflects the latest activity."

Boom! We now have three sessions running in parallel. Now I can keep going because none of these sessions will need my attention anytime soon, especially if I tell them to run No Mistakes after implementation. I know whether they need me by looking at the top status bar, and I can switch between the tabs using keyboard shortcuts. That's very important for managing a lot of parallel sessions efficiently.

### First Mate

That said, after doing this for a while, you will discover that juggling between all these sessions is quite exhausting. The constant context switch and having to remind yourself what each session was even doing just doesn't feel like an ideal end game experience.

So I kept pushing the boundary on this and I discovered that I needed a first mate — someone I can talk to as a captain that will carry out all my directions and manage all the crewmates for me, so I can focus on the big picture like where should we go next, not playing whack-a-mole with this increasingly high number of crewmates. This is how I level up and truly become a captain.

My First Mate is another free and open source project and it's very new. The way to use it is by just cloning it. And then I can run an agent in this repository. Now I just talk to it and ask it to work on any projects I like.

Let's say I'd like to work on Lavish AXI, GitHub AXI, and Chrome DevTools AXI. They are all GitHub projects I own. First Mate is starting up and the first time we run it, it will do some setup and ask for some preferences. First Mate is asking how strict I want to be with the code changes in these repos, and I want to select "full gates to PR." This is basically going to be using No Mistakes as the pipeline to validate its changes.

A real thing I want to do is for all three projects, I'd like to add an update command on the CLI that will update their version to the latest on npm. And let's see what First Mate does. It realizes that this is not one task, but three parallel tasks, and it's now spinning up these tabs in tmux just like we did manually. It would also call Treehouse to create worktrees, and then run an agent in that worktree to get the work done, and then it will run No Mistakes to validate the change and get the PR ready for us to review.

Now you can see it's First Mate that's doing the juggling. I don't need to worry about any of this now. I can just keep giving it more work. "Hey First Mate, let's also look at the most recent three open issues in Lavish AXI and let's discuss which ones are actionable."

Boom! First Mate is now pulling the open issues from the repo while waiting for the three background agents working in parallel. First Mate said number 87 is cleanest. It's very actionable. Let me just see what this is — "Don't toggle in annotation mode." Okay, that's a clear bug. All right, First Mate, let's address number 87.

Look, now First Mate is juggling a lot of tasks for me that I otherwise would have to manage by myself. Watching it context switch is actually an oddly satisfying experience, because I know that's what I would have to do otherwise. First Mate is basically all my tools coming together as one cohesive workflow, and I have been really happy with it. It's been a pretty significant improvement to my overall experience working with agents. I highly recommend trying it out if you are still directly talking to every single agent session one by one — it will be a pretty massive upgrade.

### The Captain's Mindset

Something you start to notice after having a First Mate is that because First Mate took care of so many things for you, you start to run out of ideas for what to ask it to do. This is a good thing because it indicates the bottleneck is shifting. But it also means you, as the captain, need to keep up.

This requires a mindset shift of focusing more of your energy on understanding what matters by talking to your users, understanding the competitive landscape, and crafting a good treasure map that can lead your crew in a good direction. Once you started doing that, congratulations! You have successfully transitioned from a sailor into a great captain.

All right, we have gone from not having a ship to being a captain that has a First Mate and a big crew that sails together. This is a pretty good time to wrap up this video. All my tools can be found on my GitHub and will be linked in the description below. They are all free and open source. I built them because I just want to see more people learning how to do agentic engineering effectively and doing it in an enjoyable way, and that's what I hope you can get out of this video.
