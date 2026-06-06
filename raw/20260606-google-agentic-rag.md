---
type: raw
title: "Unlocking dependable responses with Gemini Enterprise Agent Platform's Agentic RAG"
source: "https://research.google/blog/unlocking-dependable-responses-with-gemini-enterprise-agent-platforms-agentic-rag/"
author:
  - "Cyrus Rashtchian"
  - "Da-Cheng Juan"
published: 2026-06-05
created: 2026-06-06
description: "Google Research 介绍 Gemini Enterprise Agent Platform 的 agentic RAG：通过 planner、query rewriter、search fanout 和 sufficient context agent 处理跨语料、多跳企业查询，并报告最高 34% 的 factuality 提升。"
tags:
  - "clippings"
  - "enterprise-ai"
  - "agentic-rag"
  - "retrieval"
  - "grounding"
---

# Unlocking dependable responses with Gemini Enterprise Agent Platform's Agentic RAG

## 剪藏价值判断

**高价值，建议后续编译。**

理由:

- 直接命中本库主线：不是泛泛谈 RAG，而是讨论企业工作流里跨系统、多跳、多源查询怎样从“检索”升级为“可依赖回答”。
- 机制清晰，可复用性强：给出了 planner、query rewriter、search fanout、sufficient context agent 的角色分工，比“加长上下文”更接近真实 harness 设计。
- 和本库已有问题强连接：它本质上在回答 [[Corrective-RAG]]、[[Agent-Harness]]、[[Verifiable-Agent-Engineering]] 在企业检索场景里应该怎样工程化。
- 提供了量化结果，不只是概念包装：文中给出最高 34% factuality 提升，以及 cross-corpus 场景 90.1% 的准确率。

## 关键事实摘录

- Google 把当前单步 RAG 的核心限制定义为：无法处理企业环境中的多源、多跳问题，信息散落在多个“数据孤岛”中。
- 他们提出的 agentic RAG 由多个角色组成：orchestrator、planner、query rewriter、search fanout 和最终整合答案的 LLM。
- 关键创新是 **Sufficient Context Agent**：不只是判断“有没有结果”，而是判断“是否已经具备足够上下文回答原问题”，并能指出缺了什么，再触发下一轮检索。
- 在 FramesQA 上，相比标准 RAG，文中报告 factuality 数据集最高提升 34%；在 4 个语料库的 cross-corpus 设置中，准确率达到 90.1%，且延迟和 single-corpus 版本几乎相同。

## 为什么适合本知识库

这篇文章的重要性不在于“Google 也做了 agentic RAG”，而在于它把企业检索问题重新表述成一个更接近工作系统的问题：当答案分散在不同数据库、文档库和业务系统中时，系统需要的不只是更强模型，而是能发现缺口、继续搜索并停止猜测的工作流结构。

后续编译时适合重点提取：

- sufficient context 与 corrective loop 的关系
- 检索系统从单轮命中转向多轮闭环的工程含义
- cross-corpus retrieval 对企业知识系统的意义
- “知道自己不知道什么”如何变成 agent harness 的一部分

## 原文摘录

Current single-step [retrieval-augmented generation](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) (RAG) systems weren't designed for the multi-source, multi-hop queries of modern business workflows. If, for example, the query is, "What are the specs of the server used in Project X?", the system might find documents about Project X, but those documents might only mention a server ID. It won't know to take that ID and perform a second search in another database to find the specs. The result is a partial answer or a "not found" response because the information is spread across different "islands" of data, requiring deeper exploration to find the facts.

Enter "agentic RAG", which plans, reasons, and iteratively interacts with data sources, enabling the handling of complex queries to increase dependability and accuracy.

Today, we're excited to introduce Google's [Gemini Enterprise Agent Platform](https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform?e=48754805)-hosted version of [Cross-Corpus Retrieval powered by Agentic RAG](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/rag-engine/cross-corpus-retrieval). Like [other multi-agent RAG](https://huggingface.co/learn/cookbook/multiagent_rag_system) frameworks, ours employs various agents that work together to reliably answer complex queries. Unlike other multi-agent frameworks, ours incorporates [sufficient context](https://research.google/blog/deeper-insights-into-retrieval-augmented-generation-the-role-of-sufficient-context/) to confirm if there is enough information for an accurate answer. Compared to standard RAG, our framework increases accuracy on factuality datasets by up to 34%. We also evaluated our system with proprietary, internal datasets and found that we achieve better grounding and improved reasoning accuracy on multiple domain-specific tasks.

## How multi-agent architectures work: Planning, rewriting, and routing

It helps to think of multi-agent RAG not as a single search engine but as an organized research department. In a multi-agent framework, the system breaks the job down into specialized roles:

1. _The Orchestrator_ evaluates your complex request and decides, "This isn't a one-step job", and delegates the work to agents.
2. _The Planner Agent_ maps out the information pathways.
3. _The Query Rewriter_ translates your request into multiple search queries.
4. _The Search Fanout Agent_ sends those refined queries to various retrieval sources.
5. Finally, an LLM aggregates all the context to deliver a final response.

## What makes our agentic RAG different from others

The key difference with our new agentic RAG framework is _persistence_. Compared to other RAG solutions, our framework is effective because it knows when it is missing information and continues searching until the context is complete.

Think of the Sufficient Context Agent as a quality-control inspector standing at the end of an assembly line. It examines three specific findings before allowing a response to be generated:

### 1. Retrieved snippets

The Sufficient Context Agent evaluates the actual text chunks pulled from the database by the RAG Agent.

### 2. Intermediate draft

The system also creates a "rough draft" response. The Sufficient Context Agent then reviews the prompt, draft, and retrieved snippets to evaluate whether the model has everything it needs to provide a comprehensive and grounded answer.

### 3. Missing pieces analysis

This is the most critical part. The Sufficient Context Agent identifies exactly what is not there. It doesn't just output that "this is insufficient"; it generates a specific "Reason" and "Feedback" log.

### Phase 4: Iteration

Because of the Sufficient Context Agent feedback, the Query Rewriter creates a new search. Then, the RAG Agent dives deeper into files it ignored the first time and finds the missing information.

## Experiments and results

We evaluated agentic RAG on [FramesQA](https://huggingface.co/datasets/google/frames-benchmark), which is based on the [FRAMES](https://arxiv.org/abs/2409.12941) paper.

We ran an experiment to test this ability at scale (FramesQA has 824 queries along with a corpus containing 2,676 PDF documents). In the cross-corpus setting, we also include three other distracting datasets, where the Planner Agent must determine where to retrieve from.

In the cross-corpus setting, our system nearly matches its single-corpus accuracy. Even when the Planner Agent must select the correct corpus out of 4 possibilities, we successfully route the search queries and answer 90.1% of questions correctly. Also, the latency of both single- and cross-corpus versions is about the same (within 3% on average).

## Conclusion

By combining advanced query planning, routing, and sufficient context, our agentic RAG system ensures that AI-generated responses are auditable, traceable, and grounded. This new feature is now available as [a public preview offering in Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/rag-engine/cross-corpus-retrieval).
