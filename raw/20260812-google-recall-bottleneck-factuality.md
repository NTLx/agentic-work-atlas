---
type: raw
source: "https://research.google/blog/empty-shelves-or-lost-keys-recall-is-the-bottleneck-for-parametric-factuality/"
author:
  - "Nitay Calderon"
  - "Gal Yona"
published: "2026-08-12"
created: "2026-08-13"
tags:
  - clippings
  - google-research
  - factuality
  - llm-memory
  - recall
---

# Empty shelves or lost keys? Recall is the bottleneck for parametric factuality

> Source: [research.google/blog](https://research.google/blog/empty-shelves-or-lost-keys-recall-is-the-bottleneck-for-parametric-factuality/)
> Author: Nitay Calderon, Gal Yona（Google Research）
> Date: 2026-08-12

## 正文

Factuality is essential for making Large Language Models (LLMs) reliable. When a model answers a factual question incorrectly, is it because the fact was never encoded, or because the fact is encoded but not accessible? Standard accuracy metrics collapse these cases together, even though they suggest very different limitations and very different interventions. Encoding failures call for scaling model size or expanding data coverage, while recall failures might also point to post-training and inference-time methods that help LLMs better utilize what they already encode.

In “[Empty Shelves or Lost Keys? Recall Is the Bottleneck for Parametric Factuality](https://arxiv.org/abs/2602.14080)”, we introduce *knowledge profiling*, a behavioral framework that measures both *encoding* and *recall*, and use it to examine the underlying bottlenecks of factuality in frontier LLMs (such as [Gemini3](https://blog.google/products-and-platforms/products/gemini/gemini-3/) and [GPT-5](https://openai.com/index/introducing-gpt-5/)). We then show that many factual errors in frontier LLMs are better understood as *lost keys (recall failures)*, not *empty shelves (encoding failures)*.

By analogy, we use [encoding](https://en.wikipedia.org/wiki/Encoding_(memory)) to denote parametric representation of facts, [recall](https://en.wikipedia.org/wiki/Recall_(memory)) to denote retrieving encoded facts without external cues, and [recognition](https://en.wikipedia.org/wiki/Recognition_memory) to denote identifying the correct fact when it is presented among alternatives. To support this analysis, we introduce [WikiProfile](https://huggingface.co/datasets/google/WikiProfile), a benchmark of 2,150 Wikipedia-derived facts, each paired with ten questions that probe encoding, recall, and recognition.

## The core idea: Knowledge profiling

Knowledge profiling shifts the unit of analysis from individual questions to facts. Instead of asking whether a model answered a specific question correctly, we ask a broader question: what is the state of the fact? We classify each fact into one of five knowledge profiles: (1) encoding failure, (2) recall failure, (3) direct recall, (4) recall with thinking, and (5) inference without encoding. These profiles provide a more informative diagnosis than question-level accuracy alone.

The classification is based on whether the fact is encoded and how accessible it is: Cannot be recalled, can be directly recalled, or can be recalled only with *thinking* (eliciting intermediate computations before the final answer, including [chain-of-thought](https://research.google/blog/language-models-perform-reasoning-via-chain-of-thought/) prompting and [thinking-optimized LLMs](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-model-thinking-updates-march-2025/#gemini-2-5-thinking)).

![Diagram illustrating five knowledge retrieval states in language models, ranging from encoding failure to direct recall.](https://storage.googleapis.com/gweb-research2023-media/images/KnowledgeProfiling1_Overview.width-1250.png)

*Five knowledge profiles that characterize facts.*

We operationalize this with three behavioral notions:

* *Encoding:* A model *encodes* a fact if it can correctly reproduce it in a pre-training-like context. In our setup, we measure this using proposition completion and contextual questioning, which place the model in contexts similar to those in which the fact would naturally appear during pre-training (without revealing the answer), thereby [priming](https://en.wikipedia.org/wiki/Priming_(psychology)) the model to expose whether the fact is encoded.
* *Knowledge:* A model *knows* a fact if it can correctly answer semantically equivalent questions about it across different phrasings, including both direct and [reverse](https://arxiv.org/abs/2309.12288) questions (e.g., if \*A is B\*, a direct question asks "What is B?", while a reverse question asks "What is A?").
* *Recall:* A model recalls a fact if it *knows* an encoded fact. If it recalls the fact without thinking, we refer to this as direct recall. If it knows a fact that is not encoded, we refer to this as inference without encoding. This occurs only when thinking is enabled and the model relies on other encoded facts and performs multi-hop reasoning or educated guesses.

![Diagram operationalizing factual knowledge in LLMs. It defines encoding as reproducing a fact in a pre-training context and knowing as correctly answering direct or reverse questions about it.](https://storage.googleapis.com/gweb-research2023-media/images/KnowledgeProfiling2_Operationalize.width-1250.png)

***Top****: We extract facts from Wikipedia, a predominant source of pre-training data.* ***Left****: We measure encoding by prompting the LLM to reproduce facts within their original context.* ***Right****: We measure knowledge by asking questions across varied phrasings and relational directions, with and without thinking.*

## Introducing WikiProfile

To operationalize knowledge profiling, we constructed [*WikiProfile*](https://huggingface.co/datasets/google/WikiProfile), a benchmark designed to measure factuality on naturally occurring facts. WikiProfile is constructed using a fully automated pipeline powered by a prompted LLM, Gemini-2.5-Pro with thinking. Prompts were developed through manual optimization on a small held-out subset. We extract candidate facts from Wikipedia pages by identifying facts: a proposition involving an ordered pair of entities (subject and object), where the subject appears first in the document. Each fact is paired with 10 tasks: two for encoding, four for knowledge evaluation, and four multiple-choice variants for recognition.

We generate direct and reverse questions through a three-step process of generation, refinement, and filtering, ensuring that each question is unambiguous, specific, minimal, and has a unique answer. All questions undergo filtering grounded in a search engine. We discard cases where multiple answers are returned or clarification is needed. After this automated filtering and a final manual validation step, the benchmark contains 2,150 facts.

![Flowchart detailing the WikiProfile pipeline for converting Wikipedia documents into validated multiple-choice questions.](https://storage.googleapis.com/gweb-research2023-media/images/KnowledgeProfiling3_WikiProfile.width-1250.png)

*A fully automated pipeline based on prompted LLMs.* ***Left*** *(purple): Fact extraction and construction of the proposition completion task.* ***Center*** *(red and blue): Construction of direct and reverse questions via generation, refinement, and filtering.* ***Right*** *(green): Creation of remaining questions (natural phrasing, contextual, and multiple-choice versions) based on the direct/reverse pairs.*

### How we evaluate LLMs

We evaluate 13 LLMs. Each model is evaluated both with and without thinking. For each model, fact, and task, we sample eight responses. Responses are graded automatically by prompted LLM autoraters (more details in [the paper](https://arxiv.org/abs/2602.14080)), producing approximately 4.5 million responses.

## Main result: Recall, not encoding, is the bottleneck

Across the frontier LLMs (Gemini-2.5-Pro, Gemini-3-Pro and Flash, GPT-5), factual encoding is close to saturation, but recall is not. For Gemini-3-Pro and GPT-5, 95–98% of facts are encoded, yet these models still fail to directly recall 26–34% of facts. Even with thinking, they still fail on 11–12% of facts***.*** This means that in frontier models, factual errors increasingly come not from absent knowledge, but from knowledge that is stored and not reliably accessible. In other words, the bottleneck is shifting from knowledge acquisition to knowledge utilization.

Scaling reinforces this picture. In the Gemma 3 family, larger models show far fewer encoding failures, but recall failures remain substantial and become a larger share of the remaining errors. Scaling improves what the model stores more than it improves what the model can access.

![Stacked bar chart showing the distribution of five knowledge retrieval states across various language models](https://storage.googleapis.com/gweb-research2023-media/images/KnowledgeProfiling4_Results1.width-1250.png)

*Distribution of the five profiles across 13 LLMs (percentages). The black line marks potential knowledge. As shown, encoding failures decrease sharply with scale, while recall failures persist even in frontier models.*

## Why does recall fail?

Our results suggest that recall is tightly coupled to the conditions under which a fact was learned. When the query diverges from the training-time context, phrasing, or ordering in which the fact was encountered, recall becomes harder. We highlight two cases where this happens systematically.

### Rare facts are encoded, but hard to recall

[Prior work](https://arxiv.org/abs/2211.08411) has shown that LLMs struggle with long-tail (rare) facts, often framing this as a problem of model capacity. Our results suggest a complementary picture. When we compare low-popularity and high-popularity facts, we find that rare facts are encoded at rates close to popular facts. The gap in encoding is relatively modest; however, the gap in recall is larger. This reframes the long-tail problem: Many rare facts are not absent from the model's parameters. They are present, but difficult to access. The bottleneck has shifted from knowledge acquisition to utilization.

![Bar charts showing that language models encode and recall high popularity facts better than low popularity facts.](https://storage.googleapis.com/gweb-research2023-media/images/KnowledgeProfiling5_Results2.width-1250.png)

*We compare two popularity tiers (bottom 20% vs. top 20%) in terms of encoding rates and direct recall rates. The Δ indicates the gap between tiers. As shown, it is narrow for encoding but wide for recall. See our paper for the results of all LLMs.*

### Reverse questions are verifiable, but hard to recall

We also revisit the *reversal curse*: when LLMs know "A is B" but can't answer "What is B?". At first glance, this could suggest that LLMs lack bidirectional knowledge. But our results suggest a refinement of this view. In open-ended generation (i.e., recall), reverse questions are consistently harder than direct questions. In multiple-choice verification (i.e., recognition), however, reverse questions are no harder than direct ones, and are often easier. This dissociation matters. If a model can recognize the correct answer when it is presented among distractors, but cannot generate it in a reverse query, then the issue is not simply that the bidirectional knowledge is missing. Rather, the fact appears to be encoded, and even recognizable, but difficult to recall when the query direction departs from how the fact was encountered during training. The reversal curse is a recall problem.

![Bar charts comparing language model performance on direct versus reverse fact retrieval in verify and generate tasks.](https://storage.googleapis.com/gweb-research2023-media/images/KnowledgeProfiling6_Results3.width-1250.png)

*We compare direct and reverse questions across two tasks: verification (multiple-choice) and generation (closed-book). The Δ denotes the gap between the direct and reverse settings. LLMs handle reverse questions effectively in verification but struggle in generation.*

## Thinking as a recovery mechanism

We now turn to the question of what enables the recovery of otherwise inaccessible knowledge. To this end, we examine the potential of thinking to fill this role. Thinking improves recall most strongly exactly where direct recall is weakest. The gains are especially pronounced for rare facts and reverse questions, narrowing both the popularity gap and the directionality gap.

![Bar charts showing how a thinking step improves recall across fact popularities and question directions for various models.](https://storage.googleapis.com/gweb-research2023-media/images/KnowledgeProfiling7_Results4.width-1250.png)

*We examine the impact of thinking on recall (knowing encoded facts).* ***Left****: we compare two fact popularity tiers (bottom 20% vs. top 20%).* ***Right****: we compare direct and reverse questions.The popularity or directional gaps are denoted by Δ (no thinking) and* ***ΔT*** *(with thinking).*

*As shown, thinking narrows the gaps (****ΔT****< Δ).*

More specifically, in thinking-optimized models, thinking recovers roughly 40–65% of encoded-but-not-directly-known facts. By contrast, it helps much less on facts that are not encoded. This pattern suggests that thinking primarily acts as a recall-facilitation mechanism: it helps the model access facts it already encoded, rather than mainly deriving answers through complex multi-step reasoning. That said, thinking is not free. It carries a computational cost, and it remains unclear how to determine exactly when a model should invoke it.

![Line chart indicating facts are significantly more likely to be retrieved with thinking if already encoded in the model.](https://storage.googleapis.com/gweb-research2023-media/images/KnowledgeProfiling8_Results5.width-1250.png)

*We report the percentage of not-known facts that become known with thinking, conditioned on whether the fact is encoded (red) or not (yellow). Thinking recovers 40–65% of encoded facts in thinking-optimized LLMs, but only 5–15% of non-encoded facts.*

## Takeaway

Knowledge profiling enables us to precisely diagnose factual behavior in LLMs. Applying this methodology to Wikipedia facts, our results suggest a shift in the way we should think about factual errors in frontier LLMs. If encoding is already near saturation, then further gains in factuality may come less from scaling (of model size or data). By showing that thinking can recover a substantial fraction of encoded-but-not-directly-known facts, the next improvements in factuality may come not only from better knowledge acquisition, but from
 the model.