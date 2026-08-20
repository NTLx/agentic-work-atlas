---
type: raw
title: "Engineers will do anything to avoid learning from history"
source: "https://horn.gg/blog/engineers-will-do-anything-to-avoid-learning-from-history/"
author:
  - "Horn"
published: "2026-08-15"
created: "2026-08-19"
description: "工程师有一种系统性的习惯：把已有领域（统计、金融、程序管理）重新发明一遍，包装成新东西。AI 时代的 'agentic orchestration' 就是 program management 的重新命名——但工程师不愿承认，因为这等于承认传统管理者是对的；推荐 6 本程序管理/瀑布/约束理论的书，建议工程师学习历史而非重新发明"
tags:
  - clippings
  - software-history
  - program-management
  - agentic-orchestration
  - reinvention
---

## 来源元信息

- **作者**: Horn（域名 horn.gg，HN top commenter；具体姓名待 validated_source）
- **发布日期**: 约 2026-08（晚于 Geoffrey Litt 2026-07-02《Understanding is the new bottleneck》和 Allen Bargi《Working with AI feels more like leadership》）
- **平台**: 个人博客（horn.gg）
- **延伸引用**:
  - Geoffrey Litt: Understanding is the new bottleneck (2026-07-02)
  - Allen Bargi: Working with AI feels more like leadership
  - xkcd 1838 (Machine Learning) + xkcd 793 (Physicists)
  - Matt Levine: Crypto basically speedran the history of finance
  - 《50 Years of Data Science》— Donoho
  - Nate Silver: "data scientist is a sexed-up term for a statistician"

---

## 正文

I recently became [the top comment](https://news.ycombinator.com/item?id=49293184) on an HN post about how ["Understanding is the new bottleneck"](https://www.geoffreylitt.com/2026/07/02/understanding-is-the-new-bottleneck). It came off a little more snarky than I intended when basically doing the "always has been" meme, but today I just saw a new HN post make the frontpage titled ["Working with AI feels more like leadership than coding"](https://allen.bargi.org/notes/working-with-ai-feels-like-leadership/), and it's worrying me that this is becoming a trend. Engineers are developing this (mostly correct) intuition that managing multiple agents is a lot like managing engineering teams. Now I feel compelled to complain about what I believe is the nastiest habit of engineers: no one reads the fucking manual.

The first time I noticed it was data science. Engineers spent years establishing a baseline of techniques and diagnostic approaches. It was an exciting time in a new field.

Except it wasn't a new field. It was statistics with a cooler name. Sure, the people actually pushing the field forward knew that. I believe their thought at the time was that probability went to certainty as you collected enough observations, which is where the Big Data meme came from. Statisticians didn't typically know how to work with Big Table or write map reduce. However, I'm not convinced most knew the math part was old when I watched them.

It seems to be a recurring theme. [50 Years of Data Science](https://courses.csail.mit.edu/18.337/2015/docs/50YearsDataScience.pdf) noticed it in academia and Nate Silver once said "I think data scientist is a sexed-up term for a statistician," which triggered a lot of upset blog posts by people in data science. Then came crypto. Matt Levine noticed crypto basically [speedran the history of finance](https://www.bloomberg.com/features/2022-the-crypto-story/) with sometimes interesting but often hilarious and disastrous results. We even [reinvented bus stops](https://stanforddaily.com/2018/04/09/when-silicon-valley-accidentally-reinvents-the-city-bus/).

There's a lot of valid reasons why software engineers might do this.

- Distrust of institutional fields that predate modern software, thus feeling arcane.
- Learning by operating from first principles means you can sometimes develop a deeper understanding of the discipline and discover new efficiencies.

And a few less valid reasons:

- You can make lots of money by making something appear novel and undiscovered, and consequently make yourself sound smart and cutting edge. Nobody raises a round to apply a well understood discipline correctly.
- "How hard could it be?"

It's the less valid reasons that motivate me to write about this, because when I read think pieces about how to manage your agents I feel like I can see where this is all going. Engineers who never took a TDD or PRD seriously are discovering they need to define every behavior ahead of time lest the AI presume incorrectly and build the wrong thing. Engineers who bemoaned that their nontechnical EM never really knew how things worked are realizing they can't be bothered to read the 10k line PR their AI produced. Suddenly, waterfall is is the thing to do.

But it seems like engineers probably won't call it waterfall or program management. It will be called something sexier with a lot of reinvented knowledge. Maybe calling it by the old name would admit the managers were right. Or maybe they just don't even know what waterfall is anymore since it's been so long since it was referred to favorably. I doubt most people know who Winston Royce is or read any of his papers. Even the process engineers rejected, they rejected without truly understanding it. Then again, how to guides for program management don't tend to make the HN front page.

But program management is all agentic orchestration is! Making sure requirements are well documented. Making sure those requirements are actually the most important thing to work on to begin with lest you waste precious tokens and time. Creating clear lanes of work. Process to ensure the artifacts produced meet all criteria. And the longer agents run, the more necessary it will be to see them produce regular check-ins along the way. There's a word for that ritual, and engineers have spent fifteen years debating about its length, who should be in it, or if it's even worth their time at all.

So this is a plea to engineers who are thinking about this stuff to save themselves and the industry some time and learn a little from history. A few books on the topic that I have read that I think likely apply to AI management:

- **Making Things Happen** and **The PMBOK Guide** are arguably the literal program management manuals whose covers look like something you'd only find in the college book store.
- **The Mythical Man-Month** is the one on this list most people have probably heard of. It's about how communication overhead scales quadratically with headcount and, if you read between the lines, the challenges you'll have spinning up ten agents
- **Managing the Development of Large Software Systems** describes the waterfall that most AI coders are probably doing, why it's bad, and what to do instead. It's a 12 page PDF that's annoyingly hard to find on the internet, but worth it.
- **High Output Management** is one I must admit that I have not personally read yet but is on my list. It has enough endorsements that I feel compelled to mention it because it may be the least directly applicable book with the highest opportunity for interpretation.
- **The Goal** is about what happens when you optimize non-bottlenecks. This is one of the original "understanding is the new bottleneck" books. It's where the theory of constraints comes from, if you've ever heard of it.