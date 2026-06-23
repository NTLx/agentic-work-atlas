---
type: entity
title: Progressive-Disclosure
aliases:
  - 渐进式披露
  - Skillify
definition: "根据任务语境分层加载知识的策略，让 Agent 先读高价值摘要，再按需展开证据和细节"
created: 2026-05-13
updated: 2026-06-22
tags:
  - knowledge-management
  - AI
  - agent
evidence_level: medium
claim_type: mixed
related_entities:
  - "[[LLM-Wiki]]"
  - "[[GBrain]]"
  - "[[Obsidian-Wiki]]"
  - "[[Thin-Harness-Fat-Skills]]"
  - "[[Context-Engineering]]"
  - "[[Knowledge-Compilation]]"
  - "[[Code-as-Conceptual-Infrastructure]]"
source_raw:
  - '[[深度解析LLM Wiki  Obsidian-Wiki  GBrain：Agent时代知识的“自组织”与“自进化”]]'
  - "[[20260611-openai-harness-engineering]]"
  - "[[20260620-l8-principal-agentic-workflow]]"
---

# Progressive-Disclosure（渐进式披露）

> [!definition] 定义
> 根据任务语境分层加载知识的策略，让 Agent 先读高价值摘要，再按需展开证据和细节

## 为什么重要

渐进式披露解决的是 Agent 的上下文预算问题：不是所有相关知识都应该一次性塞进 Context Window。更稳的做法是先给模型少量高价值结构，再根据任务继续展开。

在 [[LLM-Wiki]] 和 GBrain 语境中，这意味着知识页不只是存档，而要能被分层读取：标题、definition、摘要、关键数据、前提边界、关联概念、原始证据。Agent 先判断方向，再选择是否读整页、读 source summary 或回到 raw。

这与软件界面里的渐进式披露原则同构：先显示可决策的少量信息，避免让用户或模型一开始就被全部细节淹没。

## 关键数据点

- **与传统 Skill 的区别**：传统 Skill 固化为特定 `SKILL.md` 文件或指令集；Skillify 将 Skill 泛化为知识组织形态，任何 Markdown 文件、文档片段或笔记都可以被按需加载。
- **GBrain 的三层检索流程**：先用低成本 chunk 判断相关性，再加载完整页面，最后按优先级呈现结论、结构和证据。
- **Token 效率**：分层呈现避免把无关搜索结果全部塞进上下文，减少 token 消耗和注意力噪音。Kun Chen (2026) 的 Skills 实践印证了这一点——将 project memory 中条件性使用的信息（如 e2e testing 指令）提取为 skill，Agent 仅在需要时加载，避免每次请求都消耗 tokens。
- **认知路径**：先结论、后证据、再细节，能减少模型过早陷入局部材料。
- **Wiki 结构要求**：页面必须有清晰 metadata、definition、summary、关联链接和 source_raw，否则 Agent 很难判断是否继续展开。

## 与 Code as Conceptual Infrastructure 的关系

如果代码和 Wiki 都是概念基础设施，那么渐进式披露就是这套基础设施的读取协议。

代码库里，Agent 不应每次读完整仓库，而应先读 AGENTS.md、CLAUDE.md、目录边界和测试，再按任务进入具体文件。Wiki 中，Agent 不应每次回到 raw，而应先读 entity、topic、comparison 和 source summary。

这让 [[Context-Engineering]] 从"塞更多上下文"转向"控制知识展开顺序"。好的知识结构不是更多文本，而是让 Agent 知道下一步该读什么、不该读什么。

## 前提与局限性

- **结构前提**：知识页要有稳定 schema、标题、摘要、tags、source_raw 和关联链接。
- **质量前提**：高层摘要必须可信。如果摘要错，后续按需展开会沿着错误路径走。
- **延迟成本**：渐进式披露增加工具调用和文档读取步骤，响应速度可能慢于一次性 RAG。
- **召回风险**：metadata 和链接质量差时，Agent 可能漏掉关键页面。
- **生产边界**：高实时场景需要混合架构，例如向量初筛、缓存热点知识、再由模型精读。
- **过度分层风险**：层级太多会让 Agent 把时间花在找路上，而不是解决问题。

## 关联概念

- [[LLM-Wiki]] — 渐进式披露是 LLM Wiki 的核心知识组织机制
- [[GBrain]] — GBrain 的 Layered Feeding 是渐进式披露在检索环节的具体实现
- [[Obsidian-Wiki]] — Obsidian-Wiki 通过 20+ Skills 实现渐进式披露
- [[Thin-Harness-Fat-Skills]] — Skillify 理念的架构表达
- [[Knowledge-Compilation]] — 编译后的结构化知识是渐进式披露的前提
- [[Context-Engineering]] — 渐进式披露是 Context Engineering 在知识管理领域的应用
- [[Code-as-Conceptual-Infrastructure]] — 渐进式披露是概念基础设施的读取方式
