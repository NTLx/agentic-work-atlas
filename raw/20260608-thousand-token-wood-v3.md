---
type: raw
title: "The crash that vanished: control and emergence in a five-model economy"
source: "https://huggingface.co/blog/build-small-hackathon/thousand-token-wood-sim-v3"
author:
  - "Lester Leong"
published: 2026-06-08
created: 2026-06-12
description: "Build Small Hackathon 第三篇：从单模型到五模型 council 后，原来 emergent 的 honey crash 消失了。复盘三种失败尝试，得出关键区分——emergent for texture, authored control for moments that must happen."
tags:
  - "clippings"
  - "small-models"
  - "multi-agent"
  - "simulation"
  - "emergence"
  - "market-design"
---

# The crash that vanished: control and emergence in a five-model economy

> Field notes from the Build Small Hackathon, June 2026. Third installment.

In the first of these notes I told a story I was proud of. I drew a Wood Legend called the Run on Oona's Hoard, a 1929 bank run reskinned as woodland folklore, and watched the owl who keeps the honey read the panic and start liquidating. The flood of supply crashed the honey price from 10 down to 3 over the next turns. Nobody scripted it. A reskinned bank run made an agent dump an asset, and the dump moved a price. That was the whole thesis: give a small model a role and a budget, and emergent market behavior falls out for free.

Then I rebuilt the wood, and the crash stopped happening. This installment is about why, because the failure taught me more about building on agents than the original success did.

## Five labs, five minds

The rebuild swapped one model running five creatures for a council of five different labs' small models, each driving its own creature: an OpenAI model, an NVIDIA model, an OpenBMB model, and a half-billion-parameter model I fine-tuned myself running two of them. The point was honesty. If the claim is that small models can run a living economy, the strongest version of that claim is five distinct architectures making distinct choices in the same market, not one model wearing five hats.

That heterogeneity is exactly what broke the story I had already written up.

## The price is whatever the agents decide to trade at

I rebuilt the operator side too. The player is now a financier who works from the shadows: short a good, whisper a true tip to set up its fall, spring the legend, and collect when the price craters. I made that loop legible on the screen, with an objective, a scoreboard, and a one-click first trade. Making a promise visible is the fastest way to discover the promise is false.

Because when I shorted honey and sprang the Run on Oona's Hoard, honey did not crash. It rose. The council models, reading a rumor that the vault was empty and a tip that the crop was doomed, did not dump honey the way the original single model had. They hoarded it. Scarcity, not a fire sale. The short lost money, and the headline the narrator wrote, with no irony, was that the honey gamble had soured.

This is the lesson, and it is not specific to a game. In an agent economy the reference price is not a dial you turn. It is the residue of what the agents actually choose to trade. The original crash was real, but it was contingent on one model's disposition, not a robust property of the system. Change the population, and the emergent behavior you documented can simply evaporate.

## Three ways to fail

I spent three live runs trying to make the crash come back by pushing on the economy from the outside, the way you would shock a textbook supply and demand model.

First I left the legend as a pure rumor and trusted the agents to react. They did not sell. Second I dumped a windfall of honey into every creature's stores, reasoning that a glut would collapse demand and pull the price down. That worked beautifully against my test policy, a rule-based stand-in I use for fast offline runs, because the test policy follows a mechanical wants-threshold: flood its inventory and it stops buying. The live models ignored the windfall and traded on their own read of the room. The gambit lost again. Third I sized the short up, which only made the loss larger.

Three recordings, three losses: minus fifteen, minus twenty-six, minus twenty-seven pebbles, when the entire premise was that this was how you made money. The pattern was the warning. Every lever I pulled was an input to the agents' decision, and the agents were free to decline. You cannot steer a heterogeneous population of models with a mechanical shock, because the shock only biases a choice they still get to make.

The trap inside the trap is worth naming on its own. The fix that worked against my fast test policy gave me false confidence and cost me a live run to disprove. When the cheap stand-in and the real agents disagree, the stand-in is the one lying, and any result that only reproduces under the stand-in is not a result.

## Author the seam, do not push the inputs

The resolution was to stop trying to convince the agents and to make the panic true by construction. A bank run is, definitionally, a crash. So the legend now crashes its good at settlement, after the market has finished clearing for the turn, by overwriting the reference price directly. The agents trade all they like; then the run lands as a fact, the price halves, and the short that front-ran it settles into profit. The crash is no longer a behavior I hope for. It is an authored consequence I impose at the one seam where nothing downstream can argue with it.

That sounds like giving up on emergence, and it is the opposite. The emergent layer, five models trading, gossiping, hoarding, forming grudges, is still doing all the work that makes the wood feel alive. What I learned is that you do not get reliable outcomes by pushing harder on emergent inputs. You get them by choosing the precise seam at which to author a deterministic override, and leaving everything upstream free. Emergence for texture, authored control for the moments that have to happen. The craft is knowing which is which, and where the seam sits.

| Attempt | Mechanism | Honey at settlement | Gambit P&L |
| --- | --- | --- | --- |
| Original, one model | that model chose to dump | 10 to 3 | the showcase win |
| Council, rumor only | five models chose to hold | rose on scarcity | minus 15 |
| Council, inventory glut | demand collapse, test policy only | barely moved | minus 26 to 27 |
| Council, settlement override | price crashed post-clearing, by fiat | halved reliably | plus 40 |

Table 1. The same gambit across four worlds. The crash was emergent and fragile under one model, absent under a heterogeneous council, and reliable only once it was authored at the settlement seam.

## What I took away

Three things, and all three outlive the game.

First, emergence is contingent, not durable. Behavior you observe and write up from one population of agents can vanish when you change the population, even if nothing else changes. Treat a single impressive run as an anecdote, not a property, until it survives a different cast.

Second, you do not control a market of agents by shocking its inputs. Supply and demand levers only bias choices the agents are still free to make, and a heterogeneous council will frequently decline. Reliable outcomes come from authoring at a settlement seam, downstream of every decision, not from pushing harder upstream.

Third, the cheap simulator that lets you iterate fast is also the one most likely to flatter a wrong fix. When the stand-in and the real agents disagree, believe the agents.

I build agent-based market models for a living, and I have made every one of these mistakes at larger scale and higher stakes than a wood full of woodland creatures. It was useful to make them again somewhere the only thing at risk was a pile of pebbles and a story I had told too confidently the first time.

Small models, big adventures, and a crash you have to author yourself.

---

Try it: the [Space](https://huggingface.co/spaces/build-small-hackathon/thousand-token-wood-sim). Open agent traces: the [dataset](https://huggingface.co/datasets/build-small-hackathon/thousand-token-wood-traces).
