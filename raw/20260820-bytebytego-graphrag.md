---
type: raw
title: "GraphRAG: How AI Answers Questions Hidden Across Many Documents"
source: "https://blog.bytebytego.com/p/graphrag-how-ai-answers-questions"
author:
  - "ByteByteGo"
published: "2026-08-19"
created: "2026-08-20"
description: "ByteByteGo 系统化介绍 GraphRAG：local vs global queries 的根本区别、Microsoft 6 阶段 indexing pipeline、hierarchical Leiden clustering 与 community reports、local/global/DRIFT 三种 query modes、LazyGraphRAG 把 indexing 成本降至 0.1%、Agentic RAG 按 query 类型路由策略、LinkedIn 客服场景 MRR +77.6%/resolution time -28.6% 的实证。"
tags:
  - "clippings"
  - "graphrag"
  - "knowledge-graph"
  - "retrieval"
  - "rag"
  - "agentic-rag"
---

# GraphRAG: How AI Answers Questions Hidden Across Many Documents

> Source: https://blog.bytebytego.com/p/graphrag-how-ai-answers-questions
> Author: ByteByteGo (Alex Xu 等)
> Published: 2026-08-19

Imagine an AI-based retrieval system pointed at five years of your team's engineering documents, including design docs, incident postmortems, and architecture decision records. Someone asks which service owns the payments retry logic, and a pretty accurate and well-cited answer is provided by the system. However, when someone asks which failure causes recur most often across all the postmortems, the quality of the answer goes down.

Depending on the setup, the response might list a handful of incidents that happen to use the word recurring, but we don't get any idea of the underlying pattern from the answer. In other words, the reason for asking the question is not fulfilled.

Both questions can look similar from the outside. Architecturally, however, they are opposites:
- The first has an answer that can be found in a specific document, which is precisely what similarity search was built for.
- The second has an answer that shows up only after the entire collection has been surveyed and understood. This requires a completely different retrieval mechanism.

GraphRAG was designed to handle the second kind of questions, and we are going to learn more about it in this article. Here's what we will cover:
- How standard RAG retrieval works, and where it reaches its limit
- Knowledge graphs, and how one gets built from ordinary documents
- The GraphRAG indexing pipeline
- Community detection and hierarchical summaries
- Local search and global search
- Cost, latency, and maintenance tradeoffs
- When standard RAG remains the better option
- Agentic RAG

*Disclaimer: This post is based on publicly shared details from various sources. References at the end. Please comment if you notice any inaccuracies.*

## Retrieval Basics

Standard RAG (Retrieval Augmented Generation) depends on a compact pipeline.

We take a collection of documents, slice each one into chunks of a few hundred to a few thousand tokens, and pass every chunk through an embedding model. The embedding model returns a vector, which is basically a long list of numbers standing in for the meaning of that text. Chunks with related meanings produce vectors that sit close together in the same numeric space. All of those vectors go into a vector index.

At query time, the same treatment applies to the question. The question also becomes a vector, the index returns the handful of chunk vectors closest to it, and the original text of those chunks gets placed into the prompt alongside the question. The language model then generates an answer from the supplied text.

The whole design rests on one simple assumption, which is that text answering a question would resemble that question. For a large share of queries, this assumption holds up well. For example, a question like "Which service owns the payments retry logic" contains the same vocabulary as the architecture decision record where that ownership was recorded. The vectors land near each other, retrieval returns the right document, and the citation points somewhere a reader can actually verify.

## Similarity Limits

This assumption about questions being similar to the answers holds for a specific class of questions, but it is by no means a universal thing.

Microsoft's GraphRAG documentation distinguishes local queries from global queries. A local query has an answer that resembles the query and lives inside a small number of text regions, which covers most who, what, when, and where questions. A global query requires reasoning across large portions of a dataset, or across all of it.

Our two example questions from earlier land on opposite sides of that line. The question "Which service owns the retry logic" is local. However, the question "Which failure causes recur most often across all postmortems" is global.

The reason the answer for the second one goes down in quality is that the phrase "recur most often" produces a vector, and the index returns whatever appears nearest to it. Across a corpus of incident reports, the nearest neighbours will be documents using words like recurring or frequent, which is a coincidence of vocabulary. However, the real answer to the question exists across two hundred documents as a distribution, which spans the corpus rather than occupying one retrievable location.

A reasonable objection at this point is that modern context windows are large enough to sidestep the problem entirely. Microsoft tested exactly that, comparing GraphRAG against vector retrieval pulling in 8,000 and then 64,000 tokens of context. However, on global questions, the larger window left the gap open on comprehensiveness, diversity, and quality of supporting source material.

This outcome is usually labelled as a hallucination problem. What actually happens is that retrieval returns material with little bearing on the question, and the model produces fluent text from it.

## Knowledge Graphs

Crossing this boundary in terms of the quality of answers requires recording how documents relate to one another, instead of treating each chunk as an independent unit of text. A knowledge graph is one way to record it.

A knowledge graph stores two kinds of things:
- Entities are the nouns a corpus talks about, such as people, services, teams, incidents, and decisions.
- Relationships are the typed connections between those entities.

Both carry a plain-text description.

Take one sentence from an incident postmortem: "The checkout service began returning timeouts after the payments team deployed the new retry handler on March 3." Extraction over that sentence produces entities for the checkout service, the payments team, and the retry handler, along with relationships recording that the team deployed the handler and that the deployment preceded the timeouts.

Once thousands of sentences have each contributed nodes and edges, paths appear that no single document contains. An engineer may be named in one design doc, a service is named in a second, an incident is described in a third, and the path from that engineer to that incident runs through both intermediate nodes.

LinkedIn's customer service team published results from this approach at SIGIR in 2024. Their support tickets had been stored as plain text, which discarded the internal structure of each ticket along with the connections between tickets. Rebuilding retrieval around a knowledge graph that preserved both improved mean reciprocal rank by 77.6 percent, and median per-issue resolution time dropped 28.6 percent in production. Similarly, Neo4j's documentation separates the lexical graph, which links documents to their chunks, from the entity graph, which links the things those documents describe.

Most GraphRAG systems build both and query across them.

## Graph Construction

Building that graph from raw documents is a pipeline, and most of its cost concentrates in a single stage.

For reference, Microsoft's documented indexing workflow runs through six phases:
1. Documents are sliced into text units, the same chunking step standard RAG performs.
2. A language model processes each text unit and extracts entities carrying a title, type, and description, along with relationships carrying a source, target, and description.
3. Entities sharing a title and type are merged across text units, and their descriptions collect into an array. A second language model pass compresses each array into one description. Relationships receive the same treatment.
4. Claim extraction runs optionally, producing time-bound factual statements about entities.
5. The assembled entity graph is clustered into a community hierarchy.
6. Community reports are generated, and text units, entity descriptions, and report contents are embedded into a vector store.

The merge step accounts for a lot of the expense. For example, a service mentioned across two hundred documents produces two hundred separate descriptions during extraction. Every one of those has to be reconciled into a single coherent description before the graph becomes usable.

Every extracted entity, relationship, and claim retains a pointer back to the text unit it came from. This pointer is what allows a generated answer to cite a specific paragraph in a specific document.

Also, two language model passes over an entire corpus add a substantial amount of inference. Microsoft's documentation estimates graph extraction at roughly 75 percent of total indexing cost. Lastly, extraction quality also depends on prompts tuned to the domain.

As a separate point, FastGraphRAG replaces the language model in extraction with traditional NLP, treating noun phrases as entities and co-occurrence within a chunk as a relationship. Indexing becomes far cheaper, and the resulting graph carries considerably more noise

## Community Detection

A graph of entities and relationships answers connection questions well. However, answering whole-collection questions requires one more layer on top of it.

GraphRAG runs hierarchical Leiden clustering across the entity graph. The algorithm recursively partitions the graph into clusters, called communities, and keeps subdividing until communities fall below a size threshold. The output is a hierarchy with several levels.

These levels behave like a resolution control over the same underlying graph. Level 0 contains a small number of broad communities, each covering a large region. Deeper levels contain many more communities, each covering a narrower region. A single payments community at level 0 might split into separate communities for retry behaviour, settlement, and fraud checks two levels further down.

For every community at every level, a language model generates a community report. Each report contains an overview of that community along with its key entities, relationships, and claims. Reports are then summarized again into shorthand versions for compact use at query time.

This is the step that makes whole-collection questions answerable. A summary of what a cluster of documents collectively says gets written during indexing, well before anyone asks about it. When a global question arrives, the material required to answer it already exists as text.

Which particular level supplies the reports is a decision with real consequences. Microsoft's documentation states that response quality is heavily influenced by that choice. Lower levels produce more thorough answers because their reports carry more detail, but they also cost more time and more tokens because there are many more reports to process.

## Query Modes

With a graph and a hierarchy of reports sitting on disk, retrieval can follow two structurally different paths. GraphRAG supports both.

Local search begins by matching the query against entity description embeddings, which produces a set of entry-point entities. From each entry point, expansion proceeds along five directions in parallel:
- Text units that mention the entity.
- Community reports that contain it.
- Neighbouring entities connected to it.
- The relationships forming those connections.
- Covariates, meaning any extracted claims attached to it.

Each of those candidate sets is ranked and filtered independently. The survivors are packed into a single context window of predefined size. The expansion is bounded, and the ranking is explicit, which makes local search closer to a structured gather-and-rank operation than to open-ended pathfinding across the graph.

Global search leaves the entity graph untouched. Community reports from a chosen hierarchy level are split into batches, and those batches are shuffled so that batch ordering stays randomized. A map stage runs each batch through a language model and produces an intermediate answer where every point carries a numerical importance rating. A reduce stage then collects the highest-rated points across all batches and generates the final answer from them.

The mapping back to our payments questions can be made clearer now. The question: "Which service owns the retry logic" names an entity, so local search locates it and expands around it. Also, the question "Which failure causes recur most often" names no entity in particular, so global search aggregates across pre-written reports covering the whole corpus.

A third mode, DRIFT search, blends the two. It starts by comparing the query against the most relevant community reports to produce a broad initial answer along with follow-up questions, runs local search against those follow-ups, and returns a hierarchy of questions and answers ranked by relevance.

GraphRAG also ships a basic search mode, which is plain top-k vector retrieval, for queries where that remains the appropriate tool. When an answer comes back broad and shallow, or narrow and precise, the query mode usually explains it.

## Cost Tradeoffs

What we have looked at so far are the various capabilities associated with GraphRAG. However, cost determines whether a specific capability is worth acquiring for a given system.

Standard RAG has a modest cost at both ends, with one embedding pass at index time and one nearest-neighbour lookup per query. In contrast, GraphRAG redistributes the spending considerably. Index time absorbs two language model passes over the corpus plus report generation for every community at every level. Query time then splits, with local search running cheaply against a prepared context window, and global search running a language model across many report batches for a single question.

The index is also a derived artifact. New documents arriving means extraction, clustering, and summarization run again over the affected material, and the community hierarchy itself can shift as the graph grows. For a corpus that changes daily, this becomes an ongoing operational commitment.

Microsoft's own follow-up work addressed the cost directly. For example, LazyGraphRAG builds its index using NLP rather than a language model, skips summarization entirely, and defers all language model work to query time. In this case, indexing cost matches vector RAG and lands at 0.1 percent of full GraphRAG. Global-query quality stays comparable to global search while query cost drops by more than a factor of 700.

Microsoft still argues against making every deployment LazyGraphRAG. Their stated reasoning is that the pre-built entity, relationship, and community summaries carry value beyond question answering, because people read and share those reports directly.

Two findings from Microsoft's own evaluations are as follows:
- Vector RAG remains the stronger option for local queries, where the answer resembles the question and sits in a specific region of text.
- GraphRAG's measured advantage lies in comprehensiveness, diversity, and supporting source material. On faithfulness, it scored at a similar level to baseline RAG.

The second point matters whenever someone asks whether GraphRAG reduces hallucination. The evidence supports better coverage and better sourcing, but it stops short of claiming better factual accuracy per individual claim.

## Agentic Retrieval

Since different question types favour different retrieval strategies, committing to one strategy when a system is built gives up the others.

Agentic RAG helps formulate a response to that constraint.

A language model classifies the incoming query, selects a retrieval strategy, executes it, and synthesizes the result. Available strategies might include vector search for local questions, global search for corpus-wide questions, a SQL query for structured data, and web search for anything current.

LlamaIndex documents a two-layer version of this:
- A composite retriever selects which index to query, guided by a description supplied for each index.
- Within the selected index, an auto-routed mode then selects which retrieval method applies to that specific query.

In other words, routing decisions happen at both layers.

The approach carries its own costs. It adds a language model call ahead of retrieval, which increases both latency and per-query spend. Routing errors also produce a debugging problem, because a poor answer can come from a perfectly good retrieval running under the wrong strategy.

The overall progression from basic RAG through advanced RAG to GraphRAG and then agentic RAG describes a sequence of decisions about when a system commits to a retrieval strategy. It works well as a ladder where each step outperforms the one below it.

## Conclusion

In this article, we've gone deep into GraphRAG and understood it in detail. Here are the key learning points to remember:
- Local queries have answers that resemble the question and sit in a small number of text regions, while global queries require reasoning across large portions of a collection.
- Similarity search returns whichever chunks sit nearest the query vector, so global questions tend to retrieve vocabulary matches instead of the underlying pattern.
- Larger context windows leave that gap open. Vector retrieval with 64,000 tokens still trailed on global questions in Microsoft's testing.
- A knowledge graph stores entities and typed relationships with descriptions, preserving connections that plain chunking discards.
- GraphRAG indexing runs two language model passes over the corpus, one to extract entities and relationships and one to merge their descriptions.
- Graph extraction accounts for roughly 75 percent of indexing cost, making it the first stage to examine when reducing spend.
- Hierarchical Leiden clustering produces communities at several levels of resolution over the same entity graph.
- A community report is generated for every community at every level, so summaries of what the corpus collectively says exist before any question arrives.
- Local search expands from matched entities and ranks the results into one context window, while global search runs map-reduce across community reports.
- The index is derived and perishable. LazyGraphRAG responds by moving language model work to query time, cutting indexing cost to 0.1 percent of full GraphRAG.
- Vector RAG remains stronger for local queries, and agentic retrieval selects a strategy per query rather than committing to one when the system is built.