---
title: "the solution might be cancelling my AI subscription"
source: "https://thoughts.hmmz.org/2026-05-31.html"
author:
  - "[[David]]"
published: 2026-05-31
created: 2026-06-01
description: "A personal reflection on AI tools, attention, friction, and the tendency to generate unmaintained software."
tags:
  - "clippings"
---
# the solution might be cancelling my AI subscription

I am trying to think of a list of all the wonderful things I've built with AI:

- a speech recognition system in rust
- an email archive rendering + quote collapsing tool
- a jellyfin desktop clone with gstreamer and qt quick
- an invidious clone in python + yt-dlp
- a faithful Windows 95 notepad.exe clone in fltk ported from the Wine sources
- a machine vision thing to count traffic flows from public street cameras in opencv
- a claude ui clone in python or rust i think, i don't even remember
- a regional news site i never meant to build that is actually getting traffic, python/flask
- a 3d car game built on the protocol for an existing multiplayer game in three.js
- an investment backtester in python
- a html clone of the lightroom ui, marvelled at the result then never made the backend
- a markdown viewer in qt or gtk or something else i can't even remember
- a replacement world clock widget for my laptop desktop environment in gtk and C
- a javascript network synchronised audio playback thing
- a rust client for a chinese IP camera reversed from its Android app
- a sizeable SaaS in rust
- maybe 50 other projects i've already deleted

Except for the SaaS, almost none of this is useful and I don't want to maintain any of it. I accidentally run a news outlet which is surely a liability. Sure, it has helped me "learn AI tooling" and I use many of these tools, but I didn't need them. I can't afford to maintain any of them, not in terms of time, commitment, belief, attention or willingness to spend on tokens.

I didn't mean to build most of these things. Usually the Claude session started with something like "write a quick script for X", and one hour later the result is not a *quick script for X*, nor in the usual case is my problem solved, whatever the original itch happened to be.

### attention is all you need

On that last point, this technology is **horrific** for attention. It's a thermonuclear ADHD amplifier and I have seen the same effect in every single one of my adult friends. Folk running 3 screens simultaneously working on totally unrelated "projects" they have little hope of maintaining, and such little commitment to the outcome that the time is obviously wasted.

In recent times, at least once per month someone sends a screenshot for an awesome tool they are working on. I'm like "whoa, that's really something" and the sender is obviously proud and enthusiastic. I try not to ask, but am always thinking "and where will you market it?", because when the question is asked of an engineer, the answer is unchanged since before LLMs existed.

I recently interviewed and when the topic of AI usage came up, the host answered something like "oh we're quite light on it, everyone has up to 5 rooms where they manage their agents" and I immediately felt a tightness in my stomach.

I had a vague sense of the effect a few months into using Claude. Later I reduced my subscription to Pro in the belief a quota restriction would mitigate excessive use. Then Claude went through a bad service period and I moved to Codex. Codex's CLI is much nicer than Claude's and noticeably faster. And usage started creeping back up.

The technology, when honed, is genuinely amazing. Ask it to zero shot a parser for an esoteric grammar implemented in an esoteric language with full tests and it's done. The tooling as it exists today promotes absolutely nothing like the focus required to apply it judiciously.

Almost every vendor and every tool intends to do exactly the opposite: more usage, more tokens, more output. Ask a simple yes/no question of ChatGPT and you can clearly see that it is hard-wired to include a relevant follow-up question to promote excessive interaction.

Slopping out a 10,000 LOC untested Python/JS mess in 5 minutes helps nobody. The thought of this happening in every commercial environment simultaneously is horrifying.

### friction = focus, focus = product

One of my early AI experiments, exploring *AI as a lens* in Marshall McLuhan-like thinking, was to connect speech recognition to a pipeline that generated blog posts on the other side, in the belief it would encourage me to capture my thoughts. All I needed was to press the voice note button in a Telegram channel, and out pops an Opus-formatted post.

The output was unbridled garbage. Because the effort was removed, so was the commitment, and with the commitment the focus, and with the focus any meaningful product at all. Quality writing is not conversational English simply cast through a lens: conversational English is low-bit rate noise, quality writing attempts to capture high bit rate information with better formed concepts, and this should have been obvious before I began.

I looked at repurposing the pipeline to capture private notes, but I have no need for private notes. It subverts the natural process of noise being forgotten. It is just more excess tool use.

Following from this, for as long as quality matters, I believe handwriting can never be obsolete.

---

It feels like we're heading towards crisis, and I doubt the answer is "better models" or "better tooling". [Cal Newport](https://www.youtube.com/watch?v=NDyuJcR2GH4) relates this to pseudo-productivity:

> The speaker argues that digital productivity tools, including AI and email, often create a "digital productivity paradox": they make individual tasks faster or easier, but they can leave knowledge workers busier, more distracted, and less productive overall. He cites research showing that AI users spent much more time in email, messaging, chat, and business-management tools, while spending less time in focused, uninterrupted work. His central claim is that tools designed to reduce friction often increase the volume of shallow tasks and context switching, which weakens deep work and high-value output.
>
> He explains that this happens because knowledge work often relies on "pseudo productivity," where visible busyness is treated as a proxy for real value. Digital tools reinforce this by making people look active: sending more messages, producing more drafts, attending more meetings, and generating more work artifacts. To avoid the trap, he recommends measuring real outcomes, identifying the true bottlenecks in one's work, and separating deep work from shallow work so that digital tools support meaningful progress instead of consuming attention.
>
> -- AI

These experiences have opened a new perception of all tool use, because beneath it all this is not about faster development = more apps or faster email = more communication being a desirable goal. Generically, it's about a unit time of life and how it is spent meaningfully.

I have no idea how to manage AI at present except by curtailing use, because a tool producing a cheap reward with minimal input and no friction can only be a liability, and achieving that realisation is probably the only real contribution of AI to date.

---

*David, Sun 31 May 14:31:04 2026*
