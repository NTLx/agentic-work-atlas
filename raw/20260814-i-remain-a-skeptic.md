---
type: raw
title: "I remain a skeptic"
source: "https://blog.jsbarretto.com/post/i-remain-a-skeptic"
author:
  - "Joshua Barretto"
published: "2026-08-14"
created: "2026-08-19"
description: "Joshua Barretto 作为开源项目维护者，从 7 个维度系统论证自己为何仍是 LLM 怀疑论者——即使 AI 革命 4 年后仍不用 LLM 处理任何自己在意的工作；论据包括行业产出匮乏、个人未落后、$1.5T 投资无独立研究证明生产力、LLM 生成 PR 质量低、前沿模型遗漏明显问题、Peter Naur 的代码哲学、大科技推动劳动力同质化"
tags:
  - clippings
  - ai-skepticism
  - labor-politics
  - software-philosophy
  - evidence-gap
---

## 来源元信息

- **作者**: Joshua Barretto（开源项目维护者，库被 FAANG 公司依赖）
- **发布日期**: 2026-08-14
- **平台**: 个人博客
- **链接延伸**: 文章末尾链接至 "Enter the tarpit 🤖"，延续 AI 炒作批评

---

## 正文

I still do not use LLMs for anything I actually care about. There are a lot of reasons I could give: environmental, social, political. I could talk about ecosystem lock-in, learned dependence, self-sovereignty, philosophical concerns, the intentional dismantling of labour bargaining power, and more. But before all of that, the simple question of efficacy - whether they actually work for the purpose of building non-trivial software - is still very far from settled.

Here are a few reasons for my skepticism:

- **We are 4 years into this 'revolution' and the industry has almost nothing to show for it.** Software has not improved in quality, got faster, become cheaper to produce (when you exclude the mountain of poor-quality demoware that no reputable organisation would touch with a barge pole), or become more capable. It's certainly not become more *secure*. A technological revolution is usually marked by old empires falling and being replaced with new players and ideas. It is not clear to me that the industry has produced *any* new ideas in the last few years that haven't been in the navel-gazing arena of AI boosterism. Everybody is yelling at the top of their lungs but nobody is actually shipping anything useful.

- **I do not feel like I'm falling behind by not using them, despite expecting to.** Nobody has turned up to steal the reputational lunch money of my open-source projects, for all the noise. You might be able to replicate the function of my code, but so can a simple `memcpy`: an open-source project that people feel they can trust enough to build their system on is about so much more than a feature list.

- **The evidence is tenuous and thin.** $1.5 trillion later and we still have almost no independent studies that can attest to top-level productivity improvements associated with AI. Given that half of our economy currently rests on this central claim being true, we should expect more than a few one-off studies and anecdotes. Every study I'm aware of either zooms in too close and tracks a metric that has nothing to do with top-level productivity ('lines written', 'PRs merged', 'features added', etc.) or is too small to draw useful conclusions from. Even then, those studies that do exist and suggest some amount of academic rigour point to only marginal or even negative productivity gains.

- **The LLM-generated PRs I get are still rubbish.** The code has become less obviously repetitive and less stylistically consistent, but no more fit for purpose. The proportion of them that are worth actually merging is still much lower than those written by humans. A fair criticism is that it's becoming increasingly difficult to tell the two apart due to AI outputs becoming slightly less formulaic, but even the most careful humans will still leave the odd typo in their description so I'm unconvinced that the bots are yet walking among us to that degree.

- **They still miss obvious shit.** Several of my open-source libraries are in the dependency trees of FAANG companies and I've had several reports passed to me as a result of scans with frontier models. Some of it's good, most of it's bad; I can recall several situations in which a frontier model missed something obvious and important that was found by a hobbyist using their brain soon afterward.

- **The philosophy exuded by AI boosters still defies the last half-century of theory about what software development *even is*.** We should all know by now that code is an input to the software development process and not an output: yet even the most forward-looking organisations still tacitly treat lines of code as a productivity metric. That is the path to unmaintainable slop, whether the slop comes out of a machine or is simply the byproduct of humans conforming to poorly designed incentive structures. [Peter Naur remains undefeated](https://pablo.rauzy.name/dev/naur1985programming.pdf).

- **When everybody is super, nobody is.** The not-so-quiet goal of the LLM push by big tech was to homogenise intellectual labour such that it can be made fungible. When labour is fungible you can swap it out whenever you like for an alternative, decreasing the bargaining power of workers. Software development was one of the last 'guild fields' and now we are seeing its industrialisation occur. By not leaning into LLMs I've given myself the room to specialise in a smaller set of skills. So far that conscious decision is working out well, and I remain confident about my job security.