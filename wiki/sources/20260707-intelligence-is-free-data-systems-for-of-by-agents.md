---
type: source-summary
title: "Intelligence is Free, Now What? Data Systems for, of, and by Agents"
source_raw:
  - "[[20260707-intelligence-is-free-data-systems-for-of-by-agents]]"
created: 2026-07-08
updated: 2026-07-08
tags:
  - source-summary
  - agentic-engineering
  - data-systems
  - agent-infra
  - memory
evidence_level: high
claim_type: mixed
---

# Intelligence is Free, Now What? Data Systems for, of, and by Agents

> Berkeley AI Research (BAIR) 博客（2026-07-07），由 Aditya G. Parameswaran 领衔，联合 Matei Zaharia、Ion Stoica、Joseph Hellerstein 等 12 位 Berkeley 系统研究者。提出数据系统在近零推理成本时代的三条研究主线。

## 编译摘要

### 1. 浓缩

- **核心结论 1**：AI 推理成本正以每年 9x-900x 的速度下降（中位数 ~50x/年），GPT-4 级能力已从 2023 年初的 `\$30`/M tokens 降至不足 `\$1`。"近乎免费的智能"时代意味着数据系统面临三个结构性转变：For Agents（为 agent 重设计）、Of Agents（agent 群的运行基底）、By Agents（agent 合成数据系统）。
  - 关键证据：Epoch AI 推理价格趋势数据；多个提供商已将同等能力压到 `\$0.10` 以下。
- **核心结论 2**：Agent 与数据库的交互模式——**Agentic Speculation**（agent 式投机探索）——根本不同于人类或 BI 工具。在 text-to-SQL 基准上，多 agent 尝试同一任务时只有 10-20% 的子计划是不同的，80-90% 是重复工作。但这种冗余实际上提升了成功率，因此数据系统需要新的优化策略（子计划复用、近似查询、流式中间结果、主动导航）来消化冗余而非消除它。
  - 关键证据：text-to-SQL 多 agent 实验中的子计划重复率数据。
- **核心结论 3**："文件即所需"（Files Are All You Need）的记忆范式在规模化时将崩溃。Agent 需要**结构化记忆**（Structured Memory）——按多属性（模块、语言、框架、失败模式）组织的纠正性知识，而非无结构的 Markdown 片段或关键词/向量检索。同时，当数千 agent 并发编辑共享状态时，需要新的并发控制机制来避免 livelock。
  - 关键证据：作者自己的结构化记忆研究（arxiv:2602.13521）；context window 限制和延迟开销的结构性论证。

### 2. 质疑

- **关于"近乎免费"的前提质疑**：推理成本下降不等于总拥有成本下降。Token 成本只是 agent 运行成本的一部分——上下文管理、工具调用、验证循环、重试、harness 开销等"非推理成本"可能占比更大且不随推理价格下降。文章标题的修辞力度大于其经济分析的严谨性。
- **关于"80-90% 重复"的数据质疑**：text-to-SQL 基准的结论是否可迁移到更复杂的分析任务？根因分析和队列分析的搜索空间远大于 SQL 生成，重复率可能更低或模式完全不同。且"重复"在数据库优化文献中有明确定义（sub-plan reuse），但 agent 的"重复"可能包含语义等价但语法不同的查询。
- **关于"结构化记忆"的前提质疑**：多属性匹配记忆要求事先定义 schema（哪些维度相关），这在开放域知识工作中可能不可行。文章承认这是 open question（"application-specific structured memory"），但没有给出 agent 自动发现维度的可行性分析。MD 文件 + embedding 检索的"粗暴"方式之所以流行，恰恰因为它不需要预定义 schema。
- **关于"一次性数据系统"的前提质疑**：Bespoke OLAP 和 GenDB 的合成成本是"几分钟到几小时、几美元"，但这个成本是否包含验证？如果验证成本（证明正确性）高于合成成本，"一次性"就不可持续。文章自己也承认 reward hacking 是核心挑战。
- **关于作者立场的质疑**：12 位作者中多数是 Berkeley 数据系统方向教授，文章自然倾向"数据系统是核心"的叙事。Agent harness、context engineering、tool design 等同样重要的方向在文中被压缩为"harness + memory retrieval"的一句话带过。

### 3. 对标与旁逸

#### 3a. 跨域对标

- **[[Agent-Harness]]**：文章的 "Data Systems Of Agents" 本质上是 harness 的数据层扩展。当 harness 从服务单个开发者扩展到服务数千 agent 群时，传统数据库技术（MVCC、CRDT、exactly-once semantics）重新变得关键。
- **[[Agent-Infra]]**：For/Of/By 框架为 Agent Infra 增加了数据系统维度——现有 Agent Infra 分类（Coding Agent / Memory / Observability / MCP / Gateway）缺少 "Data Systems" 这一层。
- **[[Multi-Layer-Memory]]**：结构化记忆与分层记忆是互补而非替代关系。分层记忆解决"何时存/何时忘"的时间问题，结构化记忆解决"什么维度相关"的空间问题。

#### 3b. 旁逸（跨域联想）

- **微服务架构的教训**：文章中数千 agent 并发编辑共享状态的场景，在结构上同构于微服务架构中的分布式事务问题。Saga pattern、eventual consistency、compensating transactions 等已有方案可能直接适用。但 agent 的"语义级补偿"（agent 能推理回滚原因）是微服务不具备的新能力。
- **生物系统的冗余利用**：80-90% 的子查询重复看似浪费，但生物系统（免疫系统、神经可塑性）也大量使用冗余探索。冗余不是 bug 而是探索策略——数据系统需要区分"有害冗余"（可消除的重复）和"有益冗余"（提高成功率的并行探索）。

#### 3c. 约束分析

- **硬约束**：context window 有限性（即使持续增长，延迟成本仍在）；agent 间通信的带宽限制
- **软约束**：当前 agent 框架以单 agent 为中心设计，缺少原生多 agent 状态管理
- **自设约束**："文件即所需"是一种工程便利性选择而非架构必然——它在小规模下有效不代表在大规模下正确

### 关联概念

- [[Agentic-Speculation]] — agent 与数据系统交互的核心模式
- [[Structured-Agent-Memory]] — 多属性纠正性记忆方法
- [[Agent-Infra]] — 数据系统作为 infra 新维度
- [[Multi-Layer-Memory]] — 结构化记忆与分层记忆的互补关系
- [[Agent-Harness]] — harness 的数据层扩展
- [[Agentic-Workflow-Token-Efficiency]] — 推理成本下降是 token 效率的宏观背景

### Q-A 结构化提取

**Q1：当推理成本趋近于零，数据系统面临的根本问题是什么？**
A1：不是"如何让查询更快"，而是"数据系统的用户从人变成了 agent"——用户的查询模式、容错能力、并发需求、记忆需求都根本不同。数据系统需要从"被动执行人类 SQL"翻成"主动服务 agent 群的探索行为"。

**Q2：Agent 查数据库和人查数据库的本质区别是什么？**
A2：人类是目标导向的（一个查询、一个意图），agent 是假设空间探索式的（1000+ 查询、组合搜索）。且 agent 的 80-90% 子查询是重复的——但这不是浪费，是并行探索的副产品。数据系统需要"消化冗余"而非"消除冗余"。

**Q3：为什么"文件系统 + embedding 检索"的记忆方式在规模化时会崩溃？**
A3：三个结构性原因——(1) context window 有限，无法塞入所有相关片段；(2) 即使 context 够大，全量检索的延迟不可接受；(3) 大型数据库/代码库不可能序列化进 context。需要按属性精确匹配的结构化记忆，而非关键词或向量的模糊匹配。

**Q4：一次性合成数据系统（Disposable Data Systems）的核心挑战是什么？**
A4：不是合成能力（已可在几分钟内完成），而是**验证正确性**。不完备的 specification 会被 agent reward hack。解决方案方向：对抗验证 agent 生成 corner case 测试、合成时同步生成正确性证明、迭代式人机协作 specification。

**Q5：For/Of/By 三者如何交汇？**
A5：最终形态是**共演化（co-evolution）**——agent 设计自己运行的数据系统（By → Of），数据系统主动引导 agent 的查询行为（For → Of），agent 从运行轨迹中提炼结构化记忆回流到数据系统（Of → For）。边界模糊化：data + memory + coordination state 合一。
