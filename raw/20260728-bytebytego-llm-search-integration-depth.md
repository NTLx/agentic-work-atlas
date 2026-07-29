---
source: "https://blog.bytebytego.com/p/why-doordash-instacart-and-uber-eats"
title: "Why DoorDash, Instacart, and Uber Eats Integrated LLMs Into Search Three Different Ways"
author:
  - "ByteByteGo"
published: 2026-07-28
created: 2026-07-29
description: "三家外卖巨头围绕 LLM 重建搜索的案例对比：同一问题、同一研究基础、三种迥异架构。核心命题：把 LLM 加入既有技术栈归结为一个问题——LLM 应该多深地触达运行时？答案由既有基础设施决定，而非模型选择。DoorDash（离线图谱增强+受限输出解析）/ Instacart（查询理解层，头部 RAG 缓存+尾部微调 Llama-3-8B）/ Uber Eats（微调 Qwen 作双塔检索 embedding 骨干）。二手综合（基于各家公开披露）。"
tags:
  - clippings
  - enterprise-ai
---

# Why DoorDash, Instacart, and Uber Eats Integrated LLMs Into Search Three Different Ways

*ByteByteGo Newsletter · 2026-07-28*

Over the last few years, three of the biggest food delivery companies rebuilt their search systems around LLMs. DoorDash, Instacart, and Uber Eats were solving the same problem of trying to understand a user's intent when they type something in search. They were also accessing more or less the same research base. And yet, the architectures they shipped look quite different from each other.

That divergence is one of the most interesting aspects of modern development using LLMs. Once we understand why each company landed where it did, we will have a mental model for thinking about how AI can be integrated into any production system.

Adding an LLM to an existing stack comes down to one question: how deeply should the LLM reach into the runtime?

Ultimately, DoorDash, Instacart, and Uber Eats each answered that question differently, and the specific LLM each chose was secondary. The specific model each company picked was secondary. The infrastructure they already had in place is what determined the answer.

In this article, we will walk through their differing solutions and try to make sense of their choices and understand the pattern behind them.

*Disclaimer: This post is based on publicly shared details from various sources. References are present at the end. Please comment if you notice any inaccuracies.*

## The Problem

Type "something healthy for a rainy evening" into a food delivery app and watch what comes back. The result we get today is somewhere between useful and impressive. The same query five years ago might have returned a random jumble of items, because keyword search treats the words as a bag of tokens rather than as an intent, and the query offers little for keyword matching.

This pattern repeats across several common failure modes in food search. For example:

* **Synonyms:** "Soda" and "soft drink" describe the same product, but a keyword engine treats them as different tokens.
* **Typos:** "Mozzarela" should retrieve mozzarella results, but the spelling mismatch breaks the lookup.
* **Shorthand:** "Gf pizza" meaning gluten-free pizza requires the system to recognize an abbreviation as a synonym for the full phrase.
* **Language mix:** The Spanish word "pan" means bread, while the English word "pan" means a cooking vessel, so a bilingual search bar has to disambiguate.
* **Word-sense ambiguity:** "Apple" the fruit and "Apple" the company share the same spelling but mean different things, and the right answer depends on context.

Each one is a potential moment where the user's intent and the catalog's words fail to line up.

Two harder problems lie beneath this:

* **The long tail:** Grocery and restaurant platforms see an enormous number of unique queries. Any specialized model trained on conversion data struggles with queries that appear only a handful of times, because rare queries are rare by definition.
* **The constraint problem:** A query like "vegan chicken sandwich" has a hard constraint inside it, and similarity-based retrieval might return a chicken sandwich that violates the constraint, because the similarity score still looks close. Dietary restrictions, allergens, and quantity filters all sit in this bucket.

Food search is the right domain to watch this play out, because all of these failure modes show up at the same time. In the subsequent sections, we look at how different companies handled these situations differently.

## DoorDash

DoorDash already had a knowledge graph for items and restaurants when LLMs became viable for production. The graph held structured attributes for every item, including dish type, dietary preference, cuisine, brand, and flavor.

Their approach was to use LLMs to enrich this graph offline by extracting attributes from SKU data, and to use LLMs at runtime only for parsing queries into chunks that could link back to the graph. Retrieval itself stayed keyword and graph-driven.

Consider the query "small no-milk vanilla ice cream." The LLM segments it into three chunks.

* "small" is a quantity attribute.
* "no-milk" is a dietary preference attribute that maps to the canonical label "dairy-free."
* "vanilla ice cream" splits further into a dish type ("ice cream") and a flavor ("vanilla").

Each chunk is then linked to a specific field in the knowledge graph. The dietary preference becomes a hard filter, so only dairy-free items get retrieved. The flavor becomes a soft preference for ranking. The dish type narrows the candidate pool.

What distinguishes DoorDash's approach is how they constrain the LLM's outputs.

They use retrieval-augmented generation as a guardrail rather than as a generator. For each query segment, an approximate nearest neighbor lookup retrieves the top 100 closest taxonomy concepts from the existing graph. The LLM is then prompted to pick from that list rather than invent labels. This is a clever inversion of the usual RAG pattern, where RAG typically injects context into a generator. Here, RAG defines the entire output space, so the system only ever produces concepts that the rest of the design already knows how to handle.

The measured impact is a roughly 30% lift in the trigger rate for popular dish carousels, all delivered through an architecture whose runtime stays mostly classical.

The takeaway is that DoorDash's LLM lives mostly offline, mostly in batch, working on the periphery of the runtime.

## Instacart

When Instacart's engineers first investigated an off-the-shelf LLM to categorize the search query "protein," the model returned chicken, tofu, beef, and other high-protein foods.

The answer is reasonable by any reading of the English language. The problem is that Instacart's actual users, when they type "protein," are looking for protein bars and protein powders. The model's general world knowledge and the company's specific user behavior were pulling in different directions, and this small failure points at the central problem Instacart had to solve.

The system they were replacing was complex.

Query category classification ran on a FastText model, query rewrites came from a separate engine that mined session behavior, and spell correction, query tagging, and aisle classification each ran as a separate model with its own data pipeline and serving infrastructure. The maintenance burden was substantial, and tail queries still suffered because each model needed its own labeled data, and labels for rare queries are scarce by definition.

Instacart's strategy is layered across three approaches:

* **Context engineering:** Retrieval-augmented generation pulls Instacart-specific context (top-converted categories, historical conversion data, catalog details) into the prompt before the LLM sees a query.
* **Post-processing guardrails:** Semantic similarity filters drop LLM outputs that drift away from the original query.
* **Fine-tuning:** For the most advanced tasks, the team fine-tunes Llama-3-8B on Instacart's proprietary data, so domain knowledge gets baked directly into the model weights.

The serving architecture splits along the head-versus-tail distribution.

Head queries hit an offline RAG-and-cache pipeline that is latency-tolerant and deeply context-engineered, while tail queries hit a real-time fine-tuned Llama-3-8B model that keeps latency under 300ms through adapter merging, H100 GPUs, and autoscaling.

The cache serves queries the company has seen before, while the real-time fine-tuned model serves everything else, which is where the cold-start tail lives. This split is exactly the kind of decision the head-versus-tail traffic distribution encourages, since pre-computing only pays off for queries that repeat.

After this solution, query rewrite coverage jumped from 50% to over 95%, with 90%+ precision across substitutes, broader rewrites, and synonyms. The real-time fine-tuned model improved search quality for the bottom 2% of queries (the cold-start tail), cutting scroll depth by 6% and complaints about poor tail-query results by half.

The takeaway is that Instacart's LLMs live at the query understanding layer, with some offline-cached and some online and fine-tuned, while retrieval and ranking downstream are still done by traditional machine learning and information retrieval systems. The LLM brain is doing the upstream interpretation, while the classical approach is doing the downstream serving.

## Uber Eats

Uber Eats faced the same problem the others did, plus a complication. They run across multiple verticals, including restaurants, grocery, and retail, across multiple markets, and across a long list of languages.

Their previous setup was fragmented, with separate BERT-based embedding models per vertical, lexical search in places, and the operational overhead of maintaining all of these in parallel. The goal was a single retrieval system that handled every vertical, every market, and every language with one consistent embedding space.

The architecture they decided on is a classic two-tower setup, where a query encoder and a document encoder each produce vectors in a shared space, and matching is done by similarity in that space.

The twist is in what sits inside each tower, because both towers use a fine-tuned Qwen LLM as their backbone embedding layer. The query tower runs online, embedding each incoming query in real time, while the document tower runs offline and pre-embeds billions of documents into an HNSW vector index (a graph-based structure built for fast similarity search at scale). This split is what makes the system economically possible, since running a heavyweight LLM on every document at query time would be prohibitive, while pre-computing once and looking up at retrieval time is tractable.

The fine-tuning matters as much as the architecture choice.

Out of the box, Qwen brings world knowledge and cross-lingual capability, which is what handles the Spanish "pan" problem mentioned earlier. Fine-tuning on Uber's proprietary query-document interactions teaches the embedding space what Uber Eats users actually care about, and this is what gives the system its domain alignment. The base model contributes general semantics, and the fine-tuning adds the specific rules of Uber Eats.

What makes the system viable at scale is a stack of optimizations:

* Matryoshka Representation Learning trains a single model whose embedding can be truncated to different lengths, and Uber serves at 256 dimensions in production with under 0.3% recall loss compared to the full 1,536.
* Scalar quantization (int7 instead of float32) cuts latency in half again.
* Pre-filters on hexagon, city, and fulfillment type shrink the candidate set before the ANN search even runs.

The numbers tell the cost story. Tuning the ANN parameter k dropped latency by 34% and CPU by 17% with negligible recall impact, quantization halved latency at recall above 0.95, and MRL cut storage by nearly 50%. Together, these are the engineering choices that let a fine-tuned LLM serve as the retrieval substrate of a production search system at Uber Eats' scale.

The takeaway is that Uber Eats' LLM is the embedding model itself, since every query and every document gets an LLM-derived vector, and retrieval at every level depends on LLM-produced representations.

## Integration Depth

If we line up the three companies on a single axis labeled "how deeply does the LLM sit in the runtime," the pattern provides some insight.

* DoorDash sits on the left, with the LLM enriching the catalog offline and parsing queries with constrained outputs while the runtime stays mostly classical.
* Instacart sits in the middle, with LLMs handling query understanding through offline RAG for the head queries and a fine-tuned Llama-3-8B for the tail, while retrieval downstream is still traditional.
* Uber Eats sits on the right, with a fine-tuned Qwen as the embedding backbone running for every query and pre-baked into every document vector.

Each company's position on the spectrum was largely determined by the infrastructure it already had.

* DoorDash already had a knowledge graph that classical retrieval could exploit, so the cheapest gain came from making the graph richer and teaching queries how to talk to it.
* Instacart had specialized query-understanding models that were hard to maintain, so the biggest win came from consolidation under a unified LLM strategy.
* Uber Eats already had two-tower embedding infrastructure running per vertical, so the natural next step was swapping in a fine-tuned LLM as the shared backbone, allowing one model to handle every vertical and every language.

The lesson would be that before asking which LLM to use for some task, the better question is where in an existing stack an LLM would actually help.

## Conclusion

Three of the largest food delivery companies rebuilt search around LLMs in the same window of time, with overlapping research literature and similar production constraints, and they arrived at three completely distinct architectures.

The reason food search was a good place to investigate this is that it breaks classical keyword retrieval in many ways simultaneously. Subjective queries (something healthy for a rainy evening), long-tail traffic, multilingual catalogs, and compound constraints all sit in the same search bar.

The three approaches each represent a different setting:

* DoorDash uses LLMs offline to enrich a knowledge graph, while classical retrieval still drives the runtime.
* Instacart uses LLMs at the query understanding layer, with fine-tuned smaller models handling tail queries in the hot path.
* Uber Eats fine-tuned a Qwen LLM into the embedding backbone of two-tower retrieval, so every query and every document gets an LLM-derived vector.

Each company's position on this spectrum traces back to the infrastructure it already had, which is why the depth-of-integration question matters more than the model choice.

Three universal tradeoffs survived every architecture.

* Hybrid systems are the default everywhere. Classical retrieval, knowledge graphs, and ANN indexes still do most of the work.
* World knowledge from a pre-trained model is just a head start. Domain context still has to be injected somewhere, through RAG, fine-tuning, or both.
* Guardrails are an important part of every production LLM system. Constrained vocabularies, similarity filters, and taxonomy enforcement quietly determine whether outputs stay aligned with the catalog.

**References:**

* [Evolution and Scale of Uber's Delivery Search Platform](https://www.uber.com/blog/evolution-and-scale-of-ubers-delivery-search-platform/)
* [Scaling Multilingual Semantic Search in Uber Eats Delivery](https://arxiv.org/abs/2603.06586)
* [How DoorDash leverages LLMs for better search retrieval](https://careersatdoordash.com/blog/how-doordash-leverages-llms-for-better-search-retrieval/)
* [Building DoorDash's product knowledge graph with large language models](https://careersatdoordash.com/blog/building-doordashs-product-knowledge-graph-with-large-language-models/)
* [Building The Intent Engine: How Instacart is Revamping Query Understanding with LLMs](https://www.instacart.com/company/tech-innovation/building-the-intent-engine-how-instacart-is-revamping-query-understanding-with-llms)
* [Supercharging Discovery in Search with LLMs](https://tech.instacart.com/supercharging-discovery-in-search-with-llms-556c585d4720)
