---
type: source-summary
title: "Agent Memory Architecture：The 5-Layer Playbook"
source_raw:
  - "[[Agent Memory _ The 5-Layer Playbook.pdf]]"
raw_state: full
created: 2026-09-16
updated: 2026-09-16
tags:
  - source-summary
  - agent-memory
  - memory-architecture
  - context-engineering
evidence_level: low
claim_type: mixed
---

# Agent Memory Architecture：The 5-Layer Playbook

> 来源性质：用户上传的 13 页独立编译工程笔记，封面标注“Production Agent Engineering Practice 2026”，并明确声明与 Anthropic 无隶属或背书关系。原文件没有可确认的 canonical URL，因此保留 `raw_state: full`。

> 编译判断：材料与知识库主线直接相关，收录为 Agent Memory 的一条二手架构综合；其中的外部指标、产品实现和“90%”等效果数字只能视为该 PDF 的报告，不能仅凭本文件升级为高强度证据。

## 编译摘要

### 1. 浓缩

- **核心结论1：Agent 记忆应按职能分层，而不是把所有历史塞进一个上下文或向量库。**
  - 关键证据：PDF 第 1、6、8 页把工作记忆（当前上下文）、情景记忆（发生过什么）、语义记忆（什么为真）、程序性记忆（如何做）和遗忘机制（删除/替代/冲突处理）连成一条数据流；第 2–4 页分别规定了各层的内容、检索方式和寿命。
- **核心结论2：记忆的生产闭环是“任务前检索 → 执行 → 任务后写入 → 重复成功晋升技能 → 定期清理”。**
  - 关键证据：第 6–8 页的七日构建路径、Memory-Aware Agent Loop 和系统提示词模板；第 4 页建议只有在方法重复且至少成功三次后才晋升为程序性技能。
- **核心结论3：记忆系统的收益来自选择性、结构化和生命周期治理，而不是单纯增加存储量。**
  - 关键证据：第 3 页用 ontology 限制实体/关系/校验，第 4–6 页要求冲突解决、技能版本化和过期策略，第 9 页要求按项目或 Agent 隔离共享范围，第 10–11 页进一步区分 hot/warm/cold 存储。

### 2. 质疑

- **关于“五层”的地位**：CoALA 为语言 Agent 提供的是模块化记忆、行动空间和决策过程的概念框架，并不自动证明“工作/情景/语义/程序/遗忘”是唯一或普适的生产分层。该 PDF 的五层更像工程分类法；其中“遗忘”按实现是横切所有长期记忆的生命周期控制器，而不是与其他层同类的存储桶。
- **关于定量效果**：PDF 没有复现实验、样本、置信区间或完整 benchmark 协议；Mem0、Snowflake 的数字来自不同产品/内部实验版本，不能直接拼成普遍的 ROI 定律。尤其“memory pays for itself on day one”和“memory—not the model—is the bottleneck”是推广性判断，不是本文件证明的结论。
- **关于固定阈值**：30/90 天 TTL、至少三次成功、成功率高于 0.8 等参数是启发式默认值。医疗、研究、客户支持和安全关键系统的保留周期、人工复核和删除权可能完全不同。
- **关于自动遗忘与冲突**：简单的 keep-newer 或自动过期可能删除一次性的关键决定；“同一实体单写者”能降低并发覆盖，却把写入权限、事实归属、审计和人工仲裁问题留给系统设计者。
- **关于实现完整性**：示例代码是教学骨架，未覆盖权限、隐私删除、并发事务、事实 provenance、检索误召回、技能回滚验证和多租户隔离；JSON/SQLite/YAML 只是起步存储，不等于生产方案。
- **关于外推范围**：PDF 将编码架构、企业数据 ontology、个人助理记忆和多 Agent 协同放在同一 playbook 中，但这些场景对新鲜度、责任、权限和可审计性的约束不同，不能只靠一套 TTL 和检索器解决。

### 3. 对标与旁逸

#### 3a. 对标

- **与 [[Multi-Layer-Memory]] 的关系**：现有页面按存储位置、时间尺度和所有权划分五层；本 PDF 按认知职能和持久性语义划分五层。两套分类可以组合，但没有一一映射：例如程序性记忆可能落在长期经验层或技能层，语义记忆可能由知识图谱、数据库或文件共同承载。
- **与 [[Memory-Synthesis]] / [[Staleness-Problem]] 的关系**：PDF 把“从情景记录提取 durable facts、处理 supersession、定期清理”写成可运行的后台管线；这与记忆合成的提取—合成—更新闭环同构，但 PDF 更强调任务经验和技能晋升。
- **与 [[Structured-Agent-Memory]] / [[Ontology]] 的关系**：ontology 在此不是增加知识，而是规定什么实体、关系和约束可以进入记忆，从而降低无结构存储的检索歧义；这与结构化记忆的“空间组织”维度互补于分层记忆的“时间/生命周期”维度。

#### 3b. 旁逸

- **“遗忘”是负向知识编译**：写入不是唯一的学习动作；过期、替代和冲突标记决定旧判断何时失去行为权重。对 Agent 来说，删除策略与提取策略同样属于 harness 的认知基础设施。
- **技能晋升是受门控的经验编译**：一次成功只产生 episode；重复成功、明确步骤、可用工具和成功标准共同满足后，才把 episode 编译成 procedure。这与本库已有的“重复模式再晋升”机制相连，但仍需环境变化后的重新验证。
- **共享记忆同时是协作面和安全边界**：多 Agent 共享 semantic/procedural memory 能减少重复探索，也会扩大污染、越权读取和旧事实传播的半径；因此 memory scope 应与工具权限和项目边界一起设计。

#### 3c. 约束

- **硬约束**：上下文窗口有限；长期事实会变化；并发写入可能覆盖；多租户记忆不能默认互通。
- **软约束**：TTL、top-k、技能晋升次数、成功率阈值和 hot/warm/cold 分层，必须按任务分布、风险和成本调参。
- **自设约束**：七日上线顺序、JSONL/SQLite/YAML 选型和“至少三次”是可替换的工程起点，不是架构定律。

## 外部核验与证据边界

- **CoALA**：官方论文 [Cognitive Architectures for Language Agents](https://arxiv.org/abs/2309.02427) 支持“模块化记忆”的概念来源，但没有证明本 PDF 的五层组合或其性能数字。
- **Mem0**：官方[功能文档](https://docs.mem0.ai/features/contextual-add)曾报告 90% token savings 与 91% latency reduction，但较新的[官方 benchmark 说明](https://mem0.ai/blog/context-window-is-ram-not-storage-why-most-agent-failures-happen-how-to-fix-them-in-2026)使用约 26,000 tokens 对比低于 7,000 tokens 等不同口径；PDF 中“1,800 tokens / 26,000 tokens”的精确组合应视为特定版本或实验条件下的报告，不能脱离 benchmark 外推。
- **Snowflake**：官方 [Agent planning](https://www.snowflake.com/en/artificial-intelligence/agents/agent-planning/) 页面报告其内部实验约 20% accuracy 提升和约 39% tool calls 减少；这支持“ontology 可能降低工具调用”的方向，但内部实验的外推边界仍需保留。
- **Anthropic**：官方 [Claude Tag](https://www.anthropic.com/news/introducing-claude-tag) 说明记忆可按频道/工作范围隔离，支持“scope 是记忆边界”的工程方向；它不等于 PDF 所称的完整 Claude memory architecture 证据。

## 关键证据索引

| 主题 | PDF 定位 | 编译用途 |
|------|----------|----------|
| 五层总图与核心主张 | 第 1 页，Fig. 1、Abstract | 识别五层的职能关系 |
| 工作/情景/语义记忆 | 第 2–4 页 | 内容、检索、TTL、ontology、冲突处理 |
| 程序性记忆与遗忘 | 第 4–6 页 | 技能 schema、晋升门槛、supersession、review |
| 生产管线与决策框架 | 第 6–8 页 | 七日 build path、agent loop、何时不加记忆 |
| 多 Agent、分层存储与领域配置 | 第 9–11 页 | scope、并发、hot/warm/cold 和领域差异 |
| 测试与局限 | 第 11–13 页 | amnesia、contradiction、staleness、skill promotion、load test |

## 关联概念

- [[Multi-Layer-Memory]]
- [[Memory-Architecture]]
- [[Memory-Synthesis]]
- [[Staleness-Problem]]
- [[Structured-Agent-Memory]]
- [[Ontology]]
- [[Context-Engineering]]
- [[Agent-Harness]]
- [[Shared-Memory-Contamination]]
- [[Agentic-Memory-Dosage]]
- [[Skill-Internalization]]
