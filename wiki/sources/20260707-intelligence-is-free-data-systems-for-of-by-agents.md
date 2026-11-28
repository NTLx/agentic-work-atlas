---
type: source-summary
title: "Intelligence is Free, Now What? Data Systems for, of, and by Agents"
source_raw:
  - "[[20260707-intelligence-is-free-data-systems-for-of-by-agents]]"
created: 2026-07-08
updated: 2026-11-28
tags:
  - source-summary
  - agentic-engineering
  - data-systems
  - agent-infra
  - memory
evidence_level: medium
claim_type: mixed
---

# Intelligence is Free, Now What? Data Systems for, of, and by Agents

> Berkeley AI Research (BAIR) 博客（2026-07-07），由Aditya G. Parameswaran等12位研究者撰写。canonical现有Disclosure明确文章为领域综述与观点，部分方向来自作者团队正在进行的研究；For/Of/By为研究议程，不是预测已兑现的事实。

## 编译摘要

### 1. 浓缩

- **核心结论 1**：作者以历史API价格下降提出近零推理成本假说。Epoch AI 2025-03-12报告六类benchmark中固定性能门槛下最低API token价格的历史拟合降幅为每年9–900倍、中位50倍，并非全部模型/任务或当前价格的统一趋势。GPT-4级能力价格是BAIR概括，不以通用等价能力或当前报价引用。"近乎免费的智能"时代意味着数据系统面临三个结构性转变：For Agents（为 agent 重设计）、Of Agents（agent 群的运行基底）、By Agents（agent 合成数据系统）。
  - 关键证据：[Epoch AI原始分析](https://epoch.ai/data-insights/llm-inference-price-trends) Analysis/Assumptions：对固定性能门槛最便宜模型的价格与发布日期做log-linear拟合，每项至少4点；最快趋势始于2024年后，作者明确不保证持续。六项评估成本趋势与token价格趋势可能不同；未重核BAIR另引供应商价格，不宣称同等能力。
- **核心结论 2**：Agent 与数据库的交互模式——**Agentic Speculation**（agent 式投机探索）——可能不同于常见人类或 BI 查询模式。在 text-to-SQL 基准上，多 agent 尝试同一任务时只有 10-20% 的子计划是不同的，80-90% 是重复工作。作者报告增加尝试时成功率改善，未隔离重复计算本身的因果贡献；提出候选优化策略（子计划复用、近似查询、流式中间结果、主动导航）来消化冗余而非消除它。
  - 关键证据：text-to-SQL 多 agent 实验中的子计划重复率数据。
- **核心结论 3**：作者预测大规模无结构文件检索将面临上下文和延迟约束；并未证明文件式存储必然崩溃，结构化索引和文件载体可组合。作者提出**结构化记忆**（Structured Memory）作为候选——按多属性（SQL关键词、表、列、数据类型、适用条件及纠正陈述；见Tk-Boost论文）组织的纠正性知识，可与文件、关键词、向量或图结构检索组合。同时，当数千 agent 并发编辑共享状态时，需要新的并发控制机制来避免 livelock。
  - 关键证据：[Tk-Boost v2](https://arxiv.org/html/2602.13521v2) §3–6：NL2SQL属性匹配后还由LLM过滤，再局部修订，非纯确定性检索。GPT-4.1 Spider2 SQLite特定配置执行准确率27.7→44.6%，调用12→15.9、延迟29.6→37秒（Table3/5）；详见[[Structured-Agent-Memory]]第53轮复核。

### 2. 质疑

- **关于"近乎免费"的前提质疑**：推理成本下降不等于总拥有成本下降。Token 成本只是 agent 运行成本的一部分——上下文管理、工具调用、验证循环、重试、harness 开销等"非推理成本"可能占比更大且不随推理价格下降。文章标题的修辞力度大于其经济分析的严谨性。
- **关于"80-90% 重复"的数据质疑**：text-to-SQL 基准的结论是否可迁移到更复杂的分析任务？根因分析和队列分析的搜索空间远大于 SQL 生成，重复率可能更低或模式完全不同。且"重复"在数据库优化文献中有明确定义（sub-plan reuse），但 agent 的"重复"可能包含语义等价但语法不同的查询。
- **关于"结构化记忆"的前提质疑**：多属性匹配记忆要求事先定义 schema（哪些维度相关），这在开放域知识工作中可能不可行。文章承认这是 open question（"application-specific structured memory"），但没有给出 agent 自动发现维度的可行性分析。MD 文件 + embedding 检索的"粗暴"方式之所以流行，恰恰因为它不需要预定义 schema。
- **关于"一次性数据系统"的前提质疑**：Bespoke OLAP 和 GenDB 的合成成本是"几分钟到几小时、几美元"，但这个成本是否包含验证？如果验证成本（证明正确性）高于合成成本，"一次性"就不可持续。文章自己也承认 reward hacking 是核心挑战。
- **关于作者立场的质疑**：12 位作者中多数是 Berkeley 数据系统方向教授，文章自然倾向"数据系统是核心"的叙事。Agent harness、context engineering、tool design 等同样重要的方向在文中被压缩为"harness + memory retrieval"的一句话带过。

### 3. 对标与旁逸

#### 3a. 跨域对标

- **[[Agent-Harness]]**：文章的 "Data Systems Of Agents" 本质上是 harness 的数据层扩展。当 harness 从服务单个开发者扩展到服务数千 agent 群时，传统并发、版本、幂等和事务机制是候选工具；CRDT/MVCC本身不提供所有副作用的exactly-once或正确性。
- **[[Agent-Infra]]**：For/Of/By 框架为 Agent Infra 增加了数据系统维度——现有 Agent Infra 分类（Coding Agent / Memory / Observability / MCP / Gateway）缺少 "Data Systems" 这一层。
- **[[Multi-Layer-Memory]]**：结构化记忆与分层记忆是互补而非替代关系。分层记忆解决"何时存/何时忘"的时间问题，结构化记忆解决"什么维度相关"的空间问题。

#### 3b. 旁逸（跨域联想）

- **微服务架构的教训**：文章中数千 agent 并发编辑共享状态的场景，在结构上同构于微服务架构中的分布式事务问题。Saga pattern、eventual consistency、compensating transactions 等已有方案可能直接适用。语义级补偿可辅助确定修复范围，但仍需授权、业务不变量、真实终态和可恢复性；非微服务不能实现的独有能力。
- **生物系统的冗余利用**：80-90% 的子查询重复看似浪费，但生物系统（免疫系统、神经可塑性）也大量使用冗余探索。这是探索与计算复用的设计类比，数据系统可尝试区分"有害冗余"（可消除的重复）和"有益冗余"（提高成功率的并行探索）。

#### 3c. 约束分析

- **硬约束**：context window 有限性（即使持续增长，延迟成本仍在）；agent 间通信的带宽限制
- **软约束**：当前 agent 框架以单 agent 为中心设计，缺少原生多 agent 状态管理
- **自设约束**："文件即所需"是一种工程便利性选择而非架构必然——它在小规模下有效不代表在大规模下正确

## 证据边界（2026-11-28）

直接回核本地Raw全部103行、[BAIR canonical](https://bair.berkeley.edu/blog/2026/07/07/intelligence-is-free-now-what/)及Epoch AI原分析；结构化记忆沿用已核Tk-Boost v2关键结果。80–90%重复来自博文所述text-to-SQL子计划实验，未在本轮取得其详细运行协议，不推断可消除的成本比例。原文Bespoke OLAP/GenDB时间和费用是特定早期报告，本轮未逐项回核论文、验证成本或实际部署；不把自定义系统视为普遍低成本。For/Of/By是研究分类，不能由价格拟合推导未来零成本、Agent主导负载或必然平台演化。**本库综合**：按真实工作负载区分探索增益与冗余计算，复用需要版本、权限、查询语义和数据快照一致；近似结果不得冒充最终权威状态。未复跑实验或改造任何系统。

### 关联概念

- [[Agentic-Speculation]] — agent 与数据系统交互的核心模式
- [[Structured-Agent-Memory]] — 多属性纠正性记忆方法
- [[Agent-Infra]] — 数据系统作为 infra 新维度
- [[Multi-Layer-Memory]] — 结构化记忆与分层记忆的互补关系
- [[Agent-Harness]] — harness 的数据层扩展
- [[Agentic-Workflow-Token-Efficiency]] — 推理成本下降是 token 效率的宏观背景

### Q-A 结构化提取

**Q1：当推理成本趋近于零，数据系统面临的根本问题是什么？**
A1：作者提出Agent工作负载可能成为重要场景；原有数据库仍可服务人和Agent，具体查询、容错、并发与状态需求应基于工作负载测量。

**Q2：Agent 查数据库和人查数据库的本质区别是什么？**
A2：原文举例多 Agent 探索可产生数千查询，并报告特定 text-to-SQL 实验80–90%子计划重复；未给出详细协议或普遍分布。应分别测探索增益与重复计算成本，不把两者视为因果等价。

**Q3：文件式记忆在何种规模与查询条件下遇到瓶颈？**
A3：三个结构性原因——(1) context window 有限，无法塞入所有相关片段；(2) 即使 context 够大，全量检索的延迟不可接受；(3) 大型数据库/代码库不可能序列化进 context。按属性匹配是候选策略，可与关键词、向量及文件存储组合；需按查询与成本验证。

**Q4：一次性合成数据系统（Disposable Data Systems）的核心挑战是什么？**
A4：作者引用特定合成系统的早期成果；生成成本、验证正确性、迁移、维护与总成本均需测量。不完备的 specification 会被 agent reward hack。解决方案方向：对抗验证 agent 生成 corner case 测试、合成时同步生成正确性证明、迭代式人机协作 specification。

**Q5：For/Of/By 三者如何交汇？**
A5：候选未来方向是**共演化（co-evolution）**——agent 设计自己运行的数据系统（By → Of），数据系统主动引导 agent 的查询行为（For → Of），agent 从运行轨迹中提炼结构化记忆回流到数据系统（Of → For）。原文设想综合状态基础设施，不要求所有数据、记忆与协作状态物理合库。
