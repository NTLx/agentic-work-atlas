---
type: raw
title: "Thousand Token Wood: shipping a multi-agent economy on a 3B model"
source: "https://huggingface.co/blog/build-small-hackathon/thousand-token-wood-sim"
author:
  - "Lester Leong"
published: 2026-06-05
created: 2026-06-06
description: "Build Small Hackathon 的项目复盘：用 Qwen2.5-3B 驱动 5 个 woodland agents，靠设计 scarcity、prompt constraint 和价格漂移机制，在小模型上跑出一个可交互的多智能体经济系统。"
tags:
  - "clippings"
  - "small-models"
  - "multi-agent"
  - "simulation"
  - "emergence"
---

# Thousand Token Wood: shipping a multi-agent economy on a 3B model

## 剪藏价值判断

**高价值，建议后续编译。**

理由:

- 它不是抽象谈“小模型也能做事”，而是给了一个具体的多智能体实验：5 个 agent、5 种商品、scarcity 机制、价格漂移、legend shocks、结构化输出修复。
- 很适合补本库“多智能体并不自动等于更强智能”这条主线：这里的进展几乎都来自环境设计、约束设计和 prompt 设计，而不是单纯换更大模型。
- 和 [[Specialized-Small-Models]]、[[Multi-Agent-System-Pathology]]、[[Emergence-World]]、[[Local-Bounded-Reasoning]] 有明显连接。
- 来源虽然是 hackathon 复盘，不是正式论文，但细节足够工程化，且公开了 traces dataset，具备后续深挖价值。

## 关键事实摘录

- 系统由 5 个 woodland creature agents 组成，底层模型是 Qwen2.5-3B，服务栈是 vLLM on Modal，前端是 Gradio。
- 作者发现“自然状态下不会交易”，于是通过 diet variety、spoilage 和 winter fuel crisis 三个机制主动制造 scarcity。
- 在约束和例子补齐后，3B 模型实现了 100% valid JSON（75/75 调用），但真正改善决策质量的手段是 prompt sharpening，而不是更大模型。
- 一个 15-turn 的代表性 run 中：trade per turn 持续 3 到 9，honey 价格从 10 跌到 3，firewood 从 4 涨到 7，Gini 从 0.14 扩大到 0.38。

## 为什么适合本知识库

这篇文章的价值，在于它把“小模型、多 agent、涌现行为”这几个经常被泛化的词，压回到了非常具体的工程现实：**要先设计环境的约束、稀缺性和可见反馈，agent 才有东西可学、可博弈、可表现。**

后续编译时适合重点提取：

- scarcity design 为什么是 emergent multi-agent demo 的前提
- “valid JSON 不等于好判断”这一点怎样映射到真实工作流 agent
- 小模型的优势更像是可并发、低成本、结构稳定，而不是更强 reasoning

## 原文摘录

A Build Small Hackathon field report on what a 3-billion-parameter council of traders can and cannot do.

Try it first: the [Space](https://huggingface.co/spaces/build-small-hackathon/thousand-token-wood-sim), and the open [agent traces](https://huggingface.co/datasets/build-small-hackathon/thousand-token-wood-traces).

I built Thousand Token Wood for the Build Small Hackathon. It is a tiny economy: five woodland creatures, each its own agent on Qwen2.5-3B, trade five goods for pebbles, gossip, hoard, and panic. You poke the wood and watch bubbles, crashes, and a widening wealth gap appear on their own. The model is served with vLLM on Modal; a Gradio app is the window onto the wood.

This is a field report on the engineering, written for people who build with small models. The short version: a 3B model is a reliable format generator and an unreliable reasoner, emergent systems need designed scarcity, and the best demos sit where a technical constraint meets something you already understand deeply.

## Why small is the design, not the limit

A living economy needs many agents thinking many times per run. That is exactly where a frontier model is the wrong tool: too slow and too costly to run a council of traders every tick. A small model is what makes a real-time multi-agent simulation feasible. Every creature decides in a single batched GPU call per turn.

## The first economy was dead on arrival

The naive version did nothing. Production outran consumption, so every creature was self-sufficient and never had a reason to trade. The market cleared once and went silent. The fix was to engineer scarcity:

- Diet variety: a creature can eat only one unit of any single food per meal, so surviving means buying foods it does not grow.
- Spoilage: perishable food rots if hoarded, forcing surplus to be sold while it still has value.
- A winter fuel crisis: every creature must burn firewood each turn, the need rises over time, and only one creature makes firewood.

That last mechanic drives the drama. One supplier cannot meet rising demand, so the woodcutter gets rich and everyone else competes for warmth.

## Valid JSON, weak judgment

With scarcity in place, the honest small-model lesson surfaced. The 3B emitted valid JSON on 100% of calls, but its economic judgment was poor: a creature that produced acorns would post an order to buy acorns, the one thing it had in surplus.

The fix was not a bigger model, it was a sharper prompt. I told each agent what it produced and must never buy, computed the exact list of goods it was short on, and gave it one worked example. Decision quality jumped and the creatures began trading to their roles. The whole loop is wrapped in a tolerant JSON parse-and-repair layer, so a malformed response degrades to a no-op instead of crashing the simulation.

A second lesson came from wellbeing. I first modeled it as an accumulator, and any chronic shortfall ground every creature to zero over a run, a death spiral that was no fun to watch and that punished the agents' imperfect optimization. I reframed it as a mean-reverting mood that recovers when a creature is fed and warm and never hits zero. Stakes belong in pebbles, prices, and status, not starvation.

## Then it started telling stories

The feature I am most pleased with ties the project to market history. The player can draw a Wood Legend: a famous episode reskinned as woodland folklore. Tulip Mania becomes the Great Acorn Mania. The South Sea Bubble becomes the Hollow Log Trading Company. The 1929 bank runs become the Run on Oona's Hoard.

These are not flavor text. Each legend fires real shocks, and the agents react. In one run I drew the Run on Oona's Hoard, the rumor that the owl's vault was empty. Oona began liquidating her honey to raise pebbles, and the flood of supply crashed the honey price from 10 to 3 over the next turns. A reskinned bank run made an agent dump assets and moved a market price. None of it was scripted.

For that to be visible, prices had to move. They were frozen because the agents quoted back the reference price I showed them. The fix was to let the market reference drift with residual supply and demand after each round: heavy unfilled buying pushes a price up, a glut pushes it down. Prices now trend during scarcity and stay calm in balanced trade.

## What actually happened

A representative fifteen-turn run, with a drought and a winter rumor injected partway:

| Metric | Result |
| --- | --- |
| Valid JSON actions | 100% (75 of 75 calls) |
| Trades per turn | sustained 3 to 9, never silent |
| Honey price | crashed 10 to 3 during the bank-run legend |
| Firewood price | rose 4 to 7 as winter scarcity bit |
| Wealth gap (Gini) | widened 0.14 to 0.38 |
| Outcome | the woodcutter ended richest, the hoarder broke |

The reasoning behind every one of those moves is in the open [traces dataset](https://huggingface.co/datasets/build-small-hackathon/thousand-token-wood-traces): each row is a creature's full prompt, raw response, parsed actions, and private thought.

## Takeaways for building with small models

Most of the engineering is closing the gap between a small model's reliable formatting and its unreliable reasoning, with structure and prompting rather than scale. Emergent systems need designed scarcity; abundance is boring. And the most compelling small-model demos do not need invented drama. Three centuries of market history had it ready, and a council of 3B agents was enough to play it out.

Small models, big adventures. Try the [Space](https://huggingface.co/spaces/build-small-hackathon/thousand-token-wood-sim).

Originally published on Medium: https://medium.com/@LesterLeong/thousand-token-wood-emergent-market-drama-from-3-billion-parameter-agents-22545d5982bf
