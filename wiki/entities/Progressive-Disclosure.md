---
type: entity
title: Progressive-Disclosure
aliases:
  - 渐进式披露
  - Skillify
definition: "根据任务语境分层加载知识的策略，让 Agent 先读高价值摘要，再按需展开证据和细节"
created: 2026-05-13
updated: 2026-11-28
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
  - "[[Skill-Chains]]"
source_raw:
  - '[[深度解析LLM Wiki  Obsidian-Wiki  GBrain：Agent时代知识的“自组织”与“自进化”]]'
  - "[[20260611-openai-harness-engineering]]"
  - "[[20260620-l8-principal-agentic-workflow]]"
  - "[[20261014-langchain-deep-agents-context-memory]]"
---

# Progressive-Disclosure（渐进式披露）

> [!definition] 定义
> 根据任务语境分层加载知识的策略，让 Agent 先读高价值摘要，再按需展开证据和细节

## 为什么重要

渐进式披露解决的是 Agent 的上下文预算问题：不是所有相关知识都应该一次性塞进 Context Window。更稳的做法是先给模型少量高价值结构，再根据任务继续展开。

在 [[LLM-Wiki]] 和 GBrain 语境中，这意味着知识页不只是存档，而要能被分层读取：标题、definition、摘要、关键数据、前提边界、关联概念、原始证据。Agent 先判断方向，再选择是否读整页、读 source summary 或回到 raw。

这与软件界面里的渐进式披露原则同构：先显示可决策的少量信息，避免让用户或模型一开始就被全部细节淹没。

## 关键数据点

- **与 Skill 的关系**：Skillify 是历史来源中的相关方法名（保留为搜索别名，不视为严格同义）；渐进式披露是按需展开策略，Skill 是带任务语义和执行约束的能力资产。普通 Markdown 片段可以按需读取，但不因此成为可执行 Skill。
- **GBrain 的三层检索流程**：先用低成本 chunk 判断相关性，再加载完整页面，最后按优先级呈现结论、结构和证据。
- **Token 效率**：分层呈现可能减少不相关载荷，也可能因为多次查询、摘要遗漏或回退增加总成本；应测量整任务而非首次 prompt。Kun Chen (2026) 的 Skills 实践印证了这一点——将 project memory 中条件性使用的信息（如 e2e testing 指令）提取为 skill，Agent 仅在需要时加载，避免每次请求都消耗 tokens。
- **认知路径**：先结论、后证据、再细节，能减少模型过早陷入局部材料。
- **Wiki 结构要求**：有意义的标题、元数据、摘要和证据链接有助于定位；具体字段按页面类型和现行 schema，不为形式添加空结构。

## 与 Code as Conceptual Infrastructure 的关系

如果代码和 Wiki 都是概念基础设施，那么渐进式披露就是这套基础设施的读取协议。

代码库里，Agent 不应每次读完整仓库，而应先读 AGENTS.md、CLAUDE.md、目录边界和测试，再按任务进入具体文件。Wiki 中按 search-first 找相关稳定页或来源；高风险、时效、冲突与新事实需回溯 raw/权威原文，不规定所有任务固定读取顺序。

这让 [[Context-Engineering]] 从"塞更多上下文"转向"控制知识展开顺序"。好的知识结构不是更多文本，而是让 Agent 知道下一步该读什么、不该读什么。

## Deep Agents：Skills 把渐进式披露做成 Harness 执行协议（2026-10）

LangChain Deep Agents（[[20261014-langchain-deep-agents-context-memory]]）给本页增加了直接的一手实现：Agent 启动时只扫描 skills 目录并读取每个 `SKILL.md` 的 header / description，把这些短描述作为“菜单”加入 system context；只有当模型判断某个 skill 与当前任务相关时，才通过 `read_file` 加载完整 instructions。

~~~text
skill catalog / short descriptions
          ↓ relevance decision
      selected skill
          ↓ read_file
full instructions + references
          ↓
       execution
~~~

这让 Progressive Disclosure 不只是知识库 UI 原则，而成为 **executable context protocol**。其收益有两部分：一是减少不相关 instructions 的 token 成本；二是减少多个规则同时竞争注意力造成的干扰。

**判断**：Agent Skills 的规模化上限很大程度取决于是否能把“可发现性”和“完整指令载荷”分离。Skill 数量增加时，应该增长的是可检索目录，而不是常驻 prompt。

- **证据**：[[20261014-langchain-deep-agents-context-memory]]；Skills section 明确描述先读 header、每次 model call 暴露 names/descriptions、按需读取完整 skill，并将其称为 progressive disclosure。
- **边界**：目录摘要若写得过弱，Agent 会漏召回；写得过宽又会让多个 Skill 同时竞争。文章没有给出 skill 数量 × task success 的独立扩展曲线，因此“十个 skills 只付十个 one-liner context”是上下文载荷描述，不等于成功率不受规模影响。

## 前提与局限性

- **结构前提**：知识页要有稳定 schema、标题、摘要、tags、source_raw 和关联链接。
- **质量前提**：高层摘要必须可信。如果摘要错，后续按需展开会沿着错误路径走。
- **延迟成本**：渐进式披露增加工具调用和文档读取步骤，响应速度可能慢于一次性 RAG。
- **召回风险**：metadata 和链接质量差时，Agent 可能漏掉关键页面。
- **生产边界**：根据真实任务比较关键词搜索、向量、缓存、直接读取与分层策略；混合架构不是实时性的必要条件。
- **过度分层风险**：层级太多会让 Agent 把时间花在找路上，而不是解决问题。

## 关联概念

- [[LLM-Wiki]] — 渐进式披露是 LLM Wiki 的核心知识组织机制
- [[GBrain]] — GBrain 的 Layered Feeding 是渐进式披露在检索环节的具体实现
- [[Obsidian-Wiki]] — Obsidian-Wiki 通过 20+ Skills 实现渐进式披露
- [[Thin-Harness-Fat-Skills]] — Skillify 理念的架构表达
- [[Knowledge-Compilation]] — 编译结构有助于分层读取；原始文档、工具和动态索引亦可按需展开
- [[Context-Engineering]] — 渐进式披露是 Context Engineering 在知识管理领域的应用
- [[Code-as-Conceptual-Infrastructure]] — 渐进式披露是概念基础设施的读取方式
