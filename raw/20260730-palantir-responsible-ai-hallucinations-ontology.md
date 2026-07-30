---
type: raw
source: "https://blog.palantir.com/reducing-hallucinations-with-the-ontology-in-palantir-aip-288552477383"
title: "Reducing Hallucinations with the Ontology in Palantir AIP (Engineering Responsible AI, #1)"
author:
  - "Palantir"
published: 2024-07-09
created: 2026-07-30
description: "Palantir 官方博客（2024-07-09，约 11 分钟阅读）。⚠️ Vendor 立场（中）：核心论点（next-token 预测 ≠ 真相检索；幻觉是结构性的而非 retrainable）来自 LLM 本质属性共识（实际引用的 [1] 是 anthropomorphization 警告 + 学术 hallucination 综述链接，未引用具体技术论文），不依赖 Palantir 产品；产品包装集中在 AIP Logic 的三种缓解机制。'Engineering Responsible AI' 系列 #1，专门处理 LLM 在企业决策场景中的 hallucination 风险。**核心论点——幻觉是结构性而非可训练消除**：LLM 的训练目标是预测'最可能的下一个 token'，而非返回 'truthful/accurate' 答案，'the job of an LLM is to just produce text that is statistically likely to look plausible'；某些幻觉是 next-token prediction 生成能力的内禀特性（'aspects of hallucinations are part and parcel of the generative capability'），靠改训练数据或架构并不总是可行——这一立场与 Anthropic/Amanda Askell 等关于 LLM 不应被信任为事实来源的判断一致。**架构答案——三层防御，用 Ontology 把 LLM 接入企业决策**：(1) **Grounding via Query Ontology**（'ontology 元数据 + data 工具'）：LLM 通过 search-query 间接访问 Ontology 数据，避免在 prompt 里塞全表；同文中给出明确术语 'Ontology-Augmented Generation (OAG)' 作为 RAG 的领域特化。(2) **Tool Handoff to Trusted Logic**（'deterministic/handoff'）：让 LLM 调用专用函数做不擅长的计算（Haversine 距离等）；同 #2 系列主张一脉相承，工具层暴露 inspectable execution。(3) **Human-in-the-loop Review**：AIP Logic 把 AI 提案 'queue up' 而不是直接落库，由 domain expert 显式 approve/reject，结合 ledger-style audit 形成 Human-AI Teaming 的具体模式。**Titan Industries 案例（虚构制造业演示）**：三个递进场景——(a) 询问美国分销中心城市 → LLM 凭空列出错误城市（数据不在训练集）；同任务接入 Ontology 查询工具后返回正确结果。(b) 卡车抛锚最近分销中心 → LLM 返回 Albany 而非正确的 Providence（用 next-token 模拟算术）；加入 Haversine function 后正确。(c) Inventory shortage 支持工单 → LLM 提取 → 检索文档 → 提议补货/调拨 → 入 queue 等待审核（不直接写入）。**与系列其他篇目互补**：本篇 (#1) 处理 *事实正确性*，#2 black-box 处理 *推理路径透明性*，#3 evals 处理 *开发期评测* —— 三篇共同构成 'Responsible AI = correctness + transparency + evals' 三脚架；本篇也连接 palantir-ontology-connecting-agents-to-decisions 的论断 'ontology 是 LLM 时代的 decision substrate'——本篇具体展示了这一 substrate 如何抵消 hallucination。**学术诚实补充**：注 [1] 单独指出'responding/replying/reasoning 是 anthropomorphization 风险'——这种主动去拟人化是负责任叙事的一种工程姿态。**编译指示**：相对于黑盒篇，本篇的工程主张更明确、更可操作（直接给 'OAG' 命名 + 三个具体机制），但相对其他企业 AI 部署材料仍然缺乏 benchmark/失效率数据，编译时应标注为 'vendor pattern extraction' 而非 'empirical validation'。"
tags:
  - clippings
  - palantir
  - responsible-ai
  - hallucination
  - ontology
  - oag
  - ontology-augmented-generation
  - tool-handoff
  - human-in-the-loop
  - aip-logic
  - agentic-engineering
  - fde
---

# Reducing Hallucinations with the Ontology in Palantir AIP (Engineering Responsible AI, #1)

*Palantir · Palantir Blog (Medium) · 2024-07-09 · 约 11 分钟阅读*

---

*Editor's Note: This is the first post in a series on responsible AI.*

Over the past two decades, Palantir has promoted the responsible use of technology through our principles, public positions, and products. This is nowhere more important than in our current work partnering with organizations to leverage the power of AI through Palantir AIP. From ensuring safety to improving explainability to addressing fairness and bias, Palantir AIP provides our users with a suite of advanced capabilities for applying Responsible AI in practice. In this blog post series, we'll share how we instill our commitment to AI Ethics and Responsible AI directly in the product development of Palantir AIP.

In this post, we tackle one of the most common challenges in conversations about AI safety: hallucinations.

## Hallucinations

A "hallucination" occurs when a generative AI model responds with false or misleading information [1]. For example, you might ask a Large Language Model (LLM) about today's weather, and it responds that it's sunny and warm even though you're sitting in a torrential rainstorm. Or, you might ask for references to academic literature about a certain research area only to find the model returns a synthetic citation, made up of bits of real information — a legitimate journal, real authors, and a seemingly plausible article name — but taken together, a fake article that never actually existed. The term "hallucination" (though a source of some debate) refers to a tendency of LLMs to generate this kind of false information.

To better understand hallucinations and why they happen, let's review how LLMs work. LLMs are designed and trained to perform just one kind of task: predicting the next most likely "token" based on a given sequence of text. A token can be a word, a part of a word, or even a series of characters. LLMs are able to do this because they are "pre-trained" on long sequences of text and are further tuned to improve the relevance and quality of next token predictions so that these models can answer questions or respond to tasks. The capability of LLMs to predict the most likely next token is what enables these models to generate realistic text, complete tasks like answering questions, responding to dialogue, and drafting text that appears authentic. However, when it comes to answering questions, next token prediction does not require LLMs to return *truthful* or *accurate* answers to the questions posed. The job of an LLM is to just produce text that is statistically likely to *look* plausible, based on its training data.

There are a variety of reasons hallucinations can occur. For example, models are trained on a finite amount of data, and it is possible that the relevant data needed to answer your question was not included in the model's training data. Additionally, elements of randomness — or stochasticity — within the architecture of LLMs may lead the model to assign a higher probability to certain next word predictions than we might prefer.

And while some improvements in LLMs may help reduce the likelihood of hallucinations in the future, some aspects of hallucinations are part and parcel of the generative capability of these models. The very features that make LLMs helpful for generating text that seems fluent and creative also risk introducing hallucinations. So, how should we approach using LLMs to perform reliable and helpful tasks while mitigating the prevalence of hallucinations, especially when modifications to the training data or LLM architecture are not feasible?

A key insight is to focus on what LLMs are actually suited for: leveraging their capability to predict the next token and, by extension, generate synthetic text. Importantly, this should not limit us to applications like chatbots or email assistants. With the right tools to keep models on track and ground them in reality, we can harness the generative capabilities of LLMs for a wider variety of powerful and useful workflows, including search, orchestration, and automation. In this blog post, we highlight several techniques to reduce the risk of hallucinations in practice and demonstrate how you can integrate these methods into your workflows using Palantir AIP.

## Reducing Hallucinations in Palantir AIP

One of the core insights of Palantir's approach to building software platforms is that data is most valuable — and most useful for enterprise decision-making — when it accurately represents the concepts and processes within your organization. We refer to this software model of data and logic as the Ontology, and we've written extensively about why this model of software architecture is crucial for the effective use of AI. In the context of generative AI, the Ontology enables users to connect LLMs to the trusted data, logic, and actions that underpin organizational decision-making. This integration of LLMs with the Ontology can help reduce the likelihood and impact of hallucinations. Let's explore three practical examples that illustrate this.

### Querying the Ontology for Trusted Data

The Ontology serves as a trusted data source that grounds the LLM in the specific context of your organization. Let's first take a look at an example where an LLM hallucinates and returns misleading information. In the AIP Logic function below, we ask an LLM to answer a question about Titan Industries, our notional manufacturing company from our Build with Palantir AIP series. We want the model to return a list of cities where some of the US-based distribution centers are located.

*[图：AIP Logic 函数截图——调用 LLM 询问 Titan Industries 美国分销中心所在城市；prompt 仅为自然语言问题]*

When we run this AIP Logic function, the model generates a list of cities that it predicts as the most likely locations. However, this output is a hallucination. Although the information about Titan Industries is notional, our enterprise data indicates that Titan Industries primarily operates in smaller cities, concentrated in the US Northeast, Midwest, and California. None of the cities returned by the LLM are actual locations of distribution centers.

Let's unpack why this might happen. Detailed information about our notional company Titan Industries, does not exist online or anywhere else. This information is only available in Titan Industries' enterprise data, which is integrated into its Ontology. This means the LLM never encountered any of the information needed to accurately answer this question during its training. Therefore, when asked about the cities where American distribution centers exist, the model predicted the most statistically likely tokens based on its training data. These cities are considered "hallucinated" because they are a factually incorrect answer to the question, even though they may appear convincing.

To address this kind of hallucination, users can "ground" the LLM with trusted, validated data. In practice, this means allowing the model to request data directly from the Ontology to add to the information in the original prompt. In AIP Logic, we can ground the LLM in the Ontology by providing the Logic function with a tool to query objects within the Ontology. This process augments the user-provided prompts with Ontology metadata (information about object types and their properties), guiding the LLM to generate a search query that can then be executed against the Ontology.

Let's see this in practice. By re-running this Logic function with the tool added, we see that the model now returns the correct answer.

*[图：AIP Logic 函数截图——加入 Query Ontology 工具（tool 列显示 'Query objects'）；输出为正确的城市列表（与 enterprise 数据一致）]*

It's important to note that hallucinations like the one described can still occur even when the relevant information was included in the LLM's training data. In such cases, the LLM might simply fail to predict the correct next word to produce a *factual* answer, underscoring the importance of grounding your LLM in the Ontology. To delve deeper into this approach, read our blog post on Ontology Augmented Generation (OAG).

### Handing Off to Trusted Logic Tools

Equipping our LLMs with the ability to query the Ontology for trusted data is a significant step forward in reducing the likelihood of hallucinations in model responses. But, this is not a silver bullet. Hallucinations can occur for many reasons, so let's examine another cause: hallucinations that occur from over-reliance on LLMs for computation tasks these models are not well-suited to perform. As mentioned earlier, LLMs are designed to predict the next best token. While this capability is helpful for generating realistic-looking text, it's not always the right tool for more complex tasks like solving equations, forecasting, or running simulations, which are better handled with purpose-built models or functions.

## Get Palantir's stories in your inbox

Join Medium for free to get updates from this writer.

Similar to providing the LLM with a tool to the query the Ontology, we can also have the LLM orchestrate handoffs to other types of models or rules. By leveraging more explainable, deterministic, or reliable forms of logic for tasks that LLMs are not well-suited to perform, we can further reduce the likelihood of a hallucination in the overall Logic function.

Let's continue with our example about Titan Industries. This time, one of our trucks has gotten stranded somewhere, and we want to interact with AIP to help us figure out which distribution center it might be closest to. As we learned from the first example, we've now provided the Logic function with a tool to query the Ontology, giving the model access to the locations of our distribution centers. Upon running the Logic function, the model returns Albany, NY, as the closest distribution center to the coordinates of the stranded truck. This, however, is a hallucination. The actual location of the truck is in Springfield, MA, which is closer to the Providence, RI, distribution center.

Let's consider why this might have happened. To start, an LLM has no in-built capability for computing distances between coordinates. Predicting the most likely token can only get the model so far in approximating simple arithmetic, let alone the more complicated calculation required for calculating travel distance. Next token prediction is the wrong type of computation for this task, and we only increase the likelihood of misleading outputs if we ask an LLM to perform a task that it's not well-suited to do.

*[图：AIP Logic 函数截图——Logic function 用 LLM 估算距离并选择最近分销中心，结果错误返回 Albany NY]*

To reduce the likelihood of this kind of logic-based hallucination, we can provide the LLM with a "tool" to delegate a computation to a model, function, or other piece of logic. In this case, we can provide the LLM with a custom Function in our Ontology that computes the travel distance between any coordinate point and a known Distribution Center using the Haversine formula. Just like with the Query Ontology tool, the LLM can then create a request for the tool, and AIP logic will invoke the tool with the given request and pass back the result to the LLM. This kind of handoff between the LLM and Tools augments the LLM's core capability for next token prediction, arming the model with the right kind of tools for whatever type of logic it might need to perform.

In this case, re-running the same Logic function with the custom Function, we see the Logic function correctly outputs Providence, RI as the closest distribution center. This is because it was able to rely on the custom Function to perform the distance calculation instead of hallucinating an incorrect answer.

*[图：AIP Logic 函数截图——加入 Haversine 计算 Function 后，正确返回 Providence RI]*

To learn more about building a workflow with LLMs and logic tools, read our blog post: Building with Palantir AIP: Logic Tools for RAG/OAG.

### Reviewing AI-Generated Actions

The Ontology is a decision-centric model of your enterprise, bringing together data, logic, and action. So far, we've discussed how data tools and logic tools can be used to reduce the likelihood and impact of hallucinations. But, no matter how well we design our use of LLMs, hallucinations are a potential side-effect of using generative AI, so we need to account for the possibility that a model still returns a hallucinated response despite these measures. Let's now take look at how we can leverage the Ontology to better oversee and monitor potential hallucinations in LLM-suggested actions.

Continuing with our example of Titan Industries, we can write an AIP Logic function to use an LLM to help us find solutions for incoming support tickets about inventory shortages, as depicted below. We'll extract details from the support ticket, map it to components in the Ontology, bring in documentation to help find relevant information, and ultimately propose a solution to reallocate or substitute inventory across distribution centers if applicable.

*[图：AIP Logic 函数截图——Inventory shortage support ticket 处理 flow：(1) LLM 解析工单 → (2) map 到 Ontology 组件 → (3) 检索文档 → (4) 提议 reallocation/substitution]*

Importantly, we're incorporating the approaches described above to both ground this workflow in the data of our Ontology and also hand-off to specialized models for tasks LLMs are not specifically designed to solve. For example, take a look at the kinds of tools in the second block in our Logic function:

*[图：第二个 block 的工具细节截图——展示调用的工具组合（查询 + 推理 + 计算 + 业务规则）]*

We can then wire up this AIP Logic function into our Inventory Management application. Every time a new Support Ticket is created in the Ontology, our Logic function is invoked automatically to find a solution. Despite providing our LLM with tools to query data and hand-off to trusted logic, the model could hallucinate a response. For example, the explanation in the support ticket might be vague and not match any information in the documentation in our Ontology, leading to an unhelpful suggestion. Or the LLM might not invoke the reallocation model with the correct arguments. In any of these cases, it's critical to incorporate human review and oversight into our workflows to provide another check against hallucinations.

Instead of directly taking the suggested reallocation or substitution action and writing that back to an external system, AIP Logic can instead *queue up* a suggested reallocation proposal for approval. At this point, a domain expert can review the suggested reallocation, confirm it makes sense in the context of the support ticket, and explicitly approve or reject the action — and even investigate how the particular AI-generated solution was reached. Incorporating this form of human review can provide another layer of defense to reduce the impact of hallucinations in operational decisions.

*[图：UI 截图——Inventory Management 应用中的 'Suggested Reallocation' 队列卡片，包含 approve / reject 按钮与 AI 解释]*

This approach of "Human-AI teaming," allowing users to seamlessly interact with, oversee, and revise AI-generated actions is crucial for applying principles of Responsible AI in practice. And, this extends beyond just reducing the impact of hallucinations: this design pattern can improve accountability, clarify AI-generated outcomes, and ensure that the use of AI remains human-centric. We'll cover these kinds of topics in future posts in this blog series.

## Conclusion

Reducing the risk of hallucinations is critical for using generative AI effectively and responsibly. Palantir AIP enables you to ground LLMs in data from the Ontology, letting you seamlessly provide trusted data to the model and help it produce more relevant results. AIP Logic also lets you extend your LLMs with Tools, allowing LLMs to delegate certain logical tasks that could be better addressed with another form of computation. And importantly, the Palantir Ontology lets you leverage generative AI while still ensuring that you have the appropriate oversight and control over AI-suggested decisions. These three approaches — building on the data, logic, and actions of your Ontology — can reduce the likelihood and impact of hallucinations and enable organizations to apply LLMs to their most challenging problems in Palantir AIP.

*[1] When we use expressions such as "asking a model to respond to a query," we're drawing upon everyday language that might be familiar to the context of inter-personal exchanges. In the discourse about language models, words like "responding" and "replying" have become a convenient way of describing interactions with the model. While we use these terms in the blog post, it's important to caveat the risk of anthropomorphizing models. These models cannot respond, reply, or reason in the true sense of the words; rather, we provide some text as input to the model, and the model returns some statistically likely text as its output.*
