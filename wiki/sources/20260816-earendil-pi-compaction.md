---
type: source-summary
title: "How Compaction Works in Pi"
source_raw:
  - "[[20260816-earendil-pi-compaction]]"
created: 2026-08-16
updated: 2026-08-16
tags:
  - source-summary
  - context-engineering
  - compaction
  - coding-agent
evidence_level: high
claim_type: extracted
authors:
  - "Earendil Engineering"
venue: "Earendil Engineering Blog, 2026-08"
---

# How Compaction Works in Pi

> 来源：Earendil Engineering Blog（2026-08）。**证据定级 high**：Pi coding agent 母公司对其 compaction 机制的工程详解，含 GitHub 源码链接（具体到 utils.ts:152-L158、compaction.ts:463-L498）+ 具体 token budget 数值 + 与 prompt cache 张力的图示。**claim_type extracted**：主体为工程机制说明（事实），跨域对标为综合判断。

## 判题（主题宪法）

- **主问题命中**：Coding agent 上下文管理是工作系统结构层（命中 `Agent-Harness`、`Context-Engineering` 主线）
- **结构性强**：触发时机 + 摘要结构 + prompt 设计 + 与 prompt cache 张力，沉淀为 `Compaction` 实体
- **机制优先**：auto-trigger 策略 / 独立 LLM 调用 / token budget 配置 / 跨模型延续
- **一手**：Pi 工程团队（提供代码链接）

→ 收录，标准路径（三步编译法），触发 1 个新 entity（Compaction）。

## 编译摘要

### 1. 浓缩

- **核心结论 1**：**Compaction 是 LLM 上下文压缩的工业实现**——当上下文逼近窗口上限时，agent 把"较老轮次"序列化成摘要（用一次独立的 LLM 调用），保留最近 N 个消息不变，结果作为新 turn 的前缀插入
  - 关键证据：触发时机 = turn 结束检查 + 手动 `/compact` 命令 + mid-turn context overflow error 触发
  - 关键证据：触发后结构 = `[system + tools][older turns 摘要][recent retained messages]`
  - 关键证据：retained token budget 默认 20k tokens ≈ 5-20 turns（可配置）
- **核心结论 2**：**Compaction 用独立的 LLM 调用 + 不同 prompt 完成摘要**——与常规对话 prompt 分离
  - 关键证据：system prompt = "you are a context summarization assistant"（而非 "expert coding assistant"）
  - 关键证据：user message = "structured summary of this conversation branch for context when returning later"
  - 关键证据：摘要结构 = goal / progress / key decisions 三段式
  - 关键证据：standalone request 不复用 conversation history → 可用不同 LLM 模型（成本/质量权衡）
- **核心结论 3**：**Compaction 与 prompt cache 存在结构性张力**——compaction 改变 prompt 前缀（[older history] → [summary]），cached prefix 必须作废
  - 关键证据：cached before compaction 状态有完整 cached prefix；first request after compaction 只能复用 `[system][tools]` 段，所有 retained turns 都需重新计算
  - 关键证据：compaction 之后请求重新建立 cache 链——这是**重新进入 warm cache 状态的成本**
- **核心结论 4（候选第三条）**：**Compaction summary 存为纯文本，支持跨模型延续**——把摘要持久化为 plain text（非结构化嵌入），便于切换 LLM 模型而不丢失上下文
  - 关键证据：session portability（不同模型读同一 summary 继续工作）

### 2. 质疑

- **关于"triggered when nearing context limit"**：trigger 阈值未披露——是 95%？99%？这影响"留给 user 的反馈时间"。threshold 太低则频繁 compaction 浪费 token；太高则 context overflow mid-turn error 风险高。Pi 工程团队没给出 best practice 数字
- **关于"retained 20k tokens ≈ 5-20 turns"**：20k tokens 是合理上限还是过早压缩？早期 compaction 浪费 LLM 调用；晚期 compaction 风险 overflow。**最优点取决于任务特征**——Pi 默认值适用于一般 coding 任务，但对深度调试类任务可能不够
- **关于"独立 LLM 调用"**：compaction 用独立 LLM 是好选择，但用何种模型？deepSeek / Claude / GPT？小型模型做摘要可能遗漏关键决策点；大型模型做摘要增加 cost。**未披露 Pi 的默认 compaction 模型**
- **关于"compaction 破坏 prompt cache"**：作者描述了 cache miss 现象但未量化成本——compaction 一次约浪费多少 tokens × cost？是否应该延迟 compaction 直至 cache 充分利用？
- **关于"structured summary with goal/progress/key decisions"**：摘要结构是 Pi 的工程选择，**未必适用于所有任务**——数据探索任务可能需要"已执行的查询"段；写作任务可能需要"已写章节"段。Pi 未提供任务感知的摘要模板
- **关于"summary 存为 plain text 支持跨模型"**：plain text 的优势是 portability，但 **loss of structured information**——无法程序化查询"已完成的 step 数"。这是 tradeoff 而非纯优点
- **数据可靠性**：GitHub 源码链接 + 具体行号引用 → 高可信；触发阈值 / 默认 compaction 模型 / 实际成本数字未披露 → 完整画像不足

### 3. 对标（跨域）

- **与 [[Context-Engineering]] 的关系**：现有 Context-Engineering 实体涵盖"Agent 看到什么、何时看到"，但未深入"压缩"机制。**Compaction 是 Context-Engineering 的子机制**——具体解决"如何让 agent 在长会话中保留关键决策"
- **与 [[Context-Rot]] 的反向证据**：Context-Rot 主张"上下文填充越多，模型推理下降"。本文 Compaction 提供**对抗 Context-Rot 的工程手段**——通过定期压缩保持 high-signal token 比例
- **与 [[Ralph-Loops]] 的相似性**：Ralph-Loops 通过重注入 prompt 实现长程任务；Compaction 通过摘要压缩实现长程会话。两者都对抗 context 衰减但路径不同——Ralph-Loops 是"同一上下文无限循环"，Compaction 是"上下文定期重置"
- **与 [[Memory-Summary-Page]] 的同构**：Memory-Summary-Page 是 Obsidian vault 的轻量索引模式（~150 字符/条目）；Compaction 是 coding agent 的轻量上下文索引。两者都是"摘要 + 按需加载"的不同实现
- **跨域对标 1（数据库 view materialization）**：Compaction = 数据库的 materialized view——定期把"原始数据"重新物化成"摘要"，新查询基于摘要而非原始数据。trigger 时机 + 摘要结构 + 与 cache 张力 与数据库 view maintenance 是同构问题
- **跨域对标 2（新闻业 story summary）**：长新闻 / 长报告 → 摘要 → 编辑回顾。Compaction prompt 强调 "like a handoff briefing from one shift to the next" 正是借用新闻业"shift handoff"隐喻
- **跨域对标 3（认知科学 chunking）**：人脑通过 chunking 处理大量信息（Miller 1956 magic number 7±2）；Compaction 把 LLM 上下文"chunking"成可保留的"记忆块"。两者机制同构
- **约束分析（ljg-constraint 应用）**：
  - **硬约束（世界规律）**：transformer 上下文窗口有限（物理上限）；prompt cache 要求 exact prefix match（缓存协议）
  - **软约束（工程选择）**：retained token budget 20k（Pi 默认值）；auto-trigger 阈值；独立 LLM 调用而非嵌入摘要；plain text 存储（vs structured embedding）
  - **自设约束（解释性）**："context-aware compaction prompt 不可行"——Pi 没披露为什么不能用常规对话 prompt 做摘要，必须用独立 prompt；这可能是工程简化而非理论必要

## 关联概念

- [[Compaction]]（本文触发的新 entity）
- [[Context-Engineering]] — 父概念；本文是子机制
- [[Context-Rot]] — 反向证据：compaction 对抗 context-rot
- [[Ralph-Loops]] — 同样对抗 context 衰减的替代方案（无限循环 vs 周期压缩）
- [[Memory-Summary-Page]] — 同构的"摘要 + 按需加载"模式
- Prompt Cache — 与 compaction 存在结构性张力
- [[Agent-Harness]] — Compaction 是 harness 的子组件
- [[Coding-Agents]] — Claude Code / Codex / Pi 等 coding agent 普遍采用
- [[AGENTS-md]] — Coding agent 的初始配置；与 compaction summary 是两类不同 artifact

## 数据卡片

| 维度 | 数值 |
|------|------|
| Pi retained token budget 默认 | 20k tokens |
| Pi retained turns | 5-20 turns（取决于 turn 平均长度）|
| 触发时机 | auto（turn 结束）+ manual（/compact 命令）+ emergency（mid-turn overflow error）|
| 摘要 prompt system | "you are a context summarization assistant" |
| 摘要 user message | "structured summary of this conversation branch for context when returning later" |
| 摘要结构 | goal / progress / key decisions |
| 摘要 LLM 调用 | 独立（不嵌入常规对话）|
| 摘要存储 | plain text（session 内）|
| Prompt cache 影响 | compaction 后 cached prefix 失效，需重新建立 cache |
| 源码引用 | utils.ts:152-L158（system prompt）+ compaction.ts:463-L498（user prompt）|