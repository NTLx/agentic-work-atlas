---
type: raw
source: "https://martinfowler.com/articles/reliable-llm-bayer.html"
author:
  - "Sarang Sanjay Kulkarni"
  - "[[Martin-Fowler]]"
published: "2026-06-16"
created: "2026-06-17"
tags:
  - clippings
  - agentic-engineering
  - RAG
  - multi-agent
  - pharma
  - context-engineering
---

# Building Reliable Agentic AI Systems

A Case Study in building production-ready agentic AI systems

*This paper presents the Preclinical Information Center (PRINCE), a cloud-hosted platform developed by Bayer AG with Thoughtworks to address pharmaceutical industry challenges in drug development. PRINCE leverages Agentic Retrieval-Augmented Generation and Text-to-SQL to integrate decades of safety study reports. We describe PRINCE's evolution from keyword-based search to an intelligent research assistant capable of answering complex questions and drafting regulatory documents.*

## The Challenge: Navigating the Preclinical Data Maze

Preclinical drug discovery is inherently complex and data-intensive. Researchers face the significant challenge of efficiently accessing and analyzing vast volumes of information generated during this critical phase. Traditional keyword-based search methods, often reliant on rigid Boolean logic, frequently fall short when confronted with the nuanced and intricate nature of preclinical research questions.

The challenges at Bayer included:
- Data Silos: information was fragmented and scattered across numerous disparate systems and repositories
- Limited Search Capabilities: traditional keyword-based search engines struggled with the complexity and variability of preclinical terminology
- Time-Consuming Manual Analysis: extracting specific insights or compiling information across multiple documents required considerable manual effort

## The Solution: PRINCE - An Evolutionary Platform

PRINCE was conceived as a unified gateway to preclinical data, initially focusing on consolidating previously siloed structured study metadata. The emergence of Generative AI, particularly RAG, provided the key to unlocking this wealth of unstructured data.

This evolution reflects PRINCE's progression through three distinct phases:

1. **Search**: the initial phase focused on creating a unified gateway to thousands of nonclinical study reports
2. **Ask**: this phase introduced an AI-powered question-answering system utilizing Retrieval Augmented Generation (RAG)
3. **Do**: the current phase positions PRINCE as an active research assistant capable of executing complex tasks through multi-agent systems

## System Architecture: Engineering a Reliable Agentic RAG System

The system functions as an interactive conversational UI, powered by a robust backend infrastructure. Its architecture is orchestrated using LangGraph and served via a FastAPI application.

A design principle running through this architecture is **context discipline**. Larger context windows did not remove the need to be selective about what each agent sees. In early iterations, putting too much information into the context made the system harder to steer and harder to evaluate. PRINCE therefore avoids treating the prompt as one large container for all available information. Instead, different stages receive different context: planning context for Think & Plan, retrieval context for the Researcher Agent, evidence context for the Reflection Agent, and synthesis context for the Writer Agent.

## The Agentic RAG System

PRINCE incorporates an agentic RAG system to handle complex user requests that require multiple steps, reasoning, and interaction with different tools or data sources.

### Clarify User Intent

The Clarify User Intent step serves as the first line of defense against ambiguity. Rather than relying on expensive trial-and-error across all data sources, the system proactively asks clarifying questions to pinpoint the specific domain or data type. This ensures the system enhances the query with the necessary constraints to target the correct tools.

### Think & Plan: Process Reflection

The Think & Plan step is responsible for devising a strategy to fulfill the user's request. This critical component gives the system a dedicated space to reason about the next steps before taking action—a technique inspired by Anthropic's Think tool. Importantly, this step performs process reflection: evaluating whether the agent is making the right progress toward its end goal.

This "thinking space" has proven particularly valuable in scenarios involving multiple tool calls. As PRINCE integrated more data sources, the number of available tools grew significantly. With this explosion of tools came an inherent challenge: overlapping concerns and domain boundaries across different tools. By introducing a dedicated thinking step, the system can explicitly reason about which tool best matches the user's intent.

### The Researcher Agent

As PRINCE expands across multiple preclinical domains, the Researcher capability is evolving into a hierarchy of domain-specific sub-agents. Each domain agent owns its own toolset along with tailored prompt instructions.

The Researcher Agent employs a hybrid retriever approach focused on two distinct patterns:
- Retrieval-Augmented Generation (RAG): for processing unstructured data, primarily PDF reports
- Text-to-SQL: for querying structured data housed in Amazon Athena

#### RAG Pipeline

The RAG pipeline comprises a comprehensive ingestion process and a sophisticated query-time architecture:

**Ingestion**: Preclinical study reports are centralized into an S3 data lake, passed through an extraction pipeline, normalized into structured JSON, chunked, enriched with metadata, and embedded in Amazon OpenSearch Service.

**Query-Time**: The multi-stage retrieval process includes:
1. Keyword Extraction: LLM extracts keywords relevant for keyword search
2. Metadata Filter Generation: LLM generates metadata filters to narrow search space
3. Query Expansion: Smaller model generates n=5 semantically similar queries
4. Hybrid Retriever: Combines metadata filtering, semantic vector similarity search (kNN), and keyword-based retrieval with weighted scoring (0.7 semantic, 0.3 keyword)
5. Reranking: Cross-encoder model selects top k=7 most relevant chunks
6. Response Generation with Citation

#### Text-to-SQL Pipeline

The Text-to-SQL tool converts natural language questions into executable SQL queries:
1. Query Analysis and Intent Recognition
2. Schema Understanding and Relevant Schema Selection
3. Dynamic Few-Shot Prompting for SQL Generation
4. SQL Query Generation and Validation (only SELECT queries permitted)
5. Query Execution and Result Limiting (max 50 records)
6. Error Handling and Iteration (up to 3 retries)

### The Reflection Agent: Data Validation and Sufficiency

While Think & Plan provides process reflection, the Reflection Agent performs data reflection: evaluating whether the data retrieved from various tools is sufficient and relevant to answer the user's question. If insufficient, it generates specific follow-up questions for further retrieval.

### The Writer Agent: Answer Synthesis and Formatting

The Writer Agent turns raw material into the final answer. It must ground every claim in the supplied context and attach accurate citations back to the underlying chunks and study IDs.

This gives PRINCE three complementary reflection loops:
1. **Process reflection**: checks whether the workflow is on the right path
2. **Data reflection**: checks whether the gathered evidence is sufficient
3. **Draft reflection**: checks whether the generated output is complete

## Building Trust in a Production LLM System

### Transparency and Explainability
- Intermediate steps displayed to users
- Links to source materials presented
- Factuality verification through citation mechanism
- Users can hover over any sentence to see corresponding citation

### Evaluation
- **Dataset Evaluations**: conducted on significant changes, using curated datasets with pre-defined reference answers. Metrics: Faithfulness, Answer Relevancy, Context Relevancy, Answer Accuracy, Semantic Similarity
- **Live Traffic Evaluations**: daily batch job on real user queries without pre-defined reference answers

### Monitoring
- Continuous monitoring using Langfuse for observability, performance and quality analysis

## Engineering for Resilience

Key error handling and recovery mechanisms:
- **State Persistence**: workflow state stored in Postgres via LangGraph checkpointer, application state in DynamoDB
- **Built-in Retries**: automatic retries at various workflow steps
- **User-Initiated Retries**: manual retry leveraging persisted state to continue from failure point
- **LLM Fallbacks**: automatic fallback to alternative LLM provider on failure
- **Domain-Specific Sub-Agents**: each domain agent owns its own toolset to reduce cross-domain leakage

## Enhancing Data Quality

Named Entity Recognition and Annotation:
- Automated NER pipeline identifies and tags key entities (compounds, study IDs, species, endpoints)
- Human-in-the-loop validation ensures annotation quality
- Annotations enable precise metadata filtering in RAG layer
- Continuous feedback loop improves NER accuracy over time
