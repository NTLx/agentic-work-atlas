---
type: source-summary
title: "Context Engineering Inside the Harness: 4 Mechanisms That Beat Context Overflow and Goal Loss on Long-Horizon Tasks"
source_raw:
  - "[[20260912-context-engineering-inside-the-harness]]"
canonical_url: "https://www.marktechpost.com/2026/09/12/context-engineering-inside-the-harness-4-mechanisms-that-beat-context-overflow-and-goal-loss-on-long-horizon-tasks/"
raw_state: full
created: 2026-09-17
updated: 2026-09-17
tags:
  - source-summary
  - context-engineering
  - agent-harness
  - compaction
  - memory
evidence_level: low
claim_type: mixed
---

# Context Engineering Inside the Harness：长程任务的四种上下文机制

> 来源：MarkTechPost，Asif Razzaq，2026-09-12。文章是二手综合，串联 AWS、Anthropic、LangChain、Manus、OpenAI 和 Amazon Bedrock 的公开材料；文中阈值和效果数字应视为“文章转述”，不能仅凭本文当作跨产品通用基准。

## 收录判定

这篇材料直接命中“Agent 如何重写工作系统”：它把长程 Agent 的失败从单纯的模型能力问题，展开为 Harness 对上下文、状态和记忆生命周期的管理问题。文章还有可迁移的机制拆分、产品实现阈值和评测建议，信息密度足以全文剪藏；但来源本身不是原始研究或产品规范，因此证据等级设为 `low`。

## 编译摘要

### 1. 浓缩

- **核心结论 1：长程 Agent 的首要瓶颈是上下文与状态管理，而不是简单扩大 Context Window。**
  - 关键证据：文章以 context overflow、goal loss 和长期状态缺失作为浅层 Agent 的三种失败；并引用 Chroma 对 18 个 LLM 的 Context Rot 观察，以及 Manus 关于约 50 次工具调用、接近 100:1 输入/输出 token 比的报告（raw 第 23–31 行）。这是文章的框架性判断，不是本文自己的受控实验。
- **核心结论 2：有效的 Harness 把上下文预算分成四个相互衔接的机制：先卸载，再压缩；用 todo 状态保持近期目标；用跨会话记忆保存可复用状态。**
  - 关键证据：文章转述 Deep Agents 在工具响应超过 20,000 tokens 时写入文件、上下文达到 85% 时把旧编辑内容替换为指针；转述 Claude Code 的延迟加载和重读上限；并比较 Claude Code、Deep Agents、OpenAI Responses API 与 Claude Developer Platform 的 compaction 设计（raw 第 35–49 行）。
- **核心结论 3：上下文管理必须以“目标是否仍能完成、细节是否可恢复”为评测对象。**
  - 关键证据：文章建议在中途强制触发摘要，测试 goal drift、错误宣告完成和 needle-in-a-haystack 恢复，并提到 LangChain 的目标延续评测与 AgentCore 的 goal success rate evaluator（raw 第 69–73 行）。交互式 200K window 模拟器只提供直观解释，作者明确称其 token 数为 illustrative（raw 第 65–67 行）。

### 2. 质疑

- **关于“不是模型而是 Harness”的质疑**：这是有用的工程归因，但表达过强。模型的长上下文能力、指令遵循、工具调用质量和 Harness 的预算/状态策略是交互变量；文章没有把模型能力与 Harness 机制分离的对照实验。
- **关于阈值可迁移性的质疑**：20,000 tokens、85%、200 行、25KB、5,000 tokens、10–20% 或 25% 等数字来自不同产品和实验设置。它们是实现默认值或评测触发点，不是所有模型、任务和风险等级的最优值。
- **关于 compaction 的质疑**：摘要能降低上下文负担，也会丢失约束；文件重读和原始 transcript 落盘只是提供恢复路径，不能保证 Agent 一定会找到或正确解释被压缩的事实。文章没有给出摘要遗漏率、恢复成功率或 compaction 的总成本。
- **关于 todo-state 的质疑**：文章同时承认证据不单向：Deep Agents v0.7 的三类任务评测在关闭 todos 时得到略高 reward 和更低成本，但仍建议长任务、弱模型和进度 UI 使用它（raw 第 51–57 行）。因此 todo 是条件性机制，不是无条件增益。
- **关于持久记忆成本的质疑**：20%–23% 的成本增幅来自文章转述的 ETH Zurich 结果，本文没有给出论文、任务和成本定义；“每次重载记忆都要付注意力税”方向合理，但增幅不能外推到所有记忆架构。
- **关于来源和样本的质疑**：MarkTechPost 将多家厂商的文档、博客、实验和营销材料混合叙述，没有统一的任务定义、测量口径或复现实验；核心数字需要回到原始来源核查。

### 3. 对标与旁逸

#### 3a. 跨域对标

- **操作系统的内存层级**：Context Window 像有限的 RAM；大工具结果写入文件像落盘；路径和预览像指针/缓存索引；compaction 像垃圾回收与 checkpoint；跨会话 memory 像持久存储。这个类比解释了为什么“窗口更大”不能替代分层管理：不同存储层的容量、延迟和可恢复性不同。
- **分布式系统的 checkpoint 与 handoff**：结构化 compaction summary、`todo.md` 和 progress 文件都把易失消息转成可恢复状态。它们类似 checkpoint / write-ahead log：不保存所有历史，而保存继续执行所需的意图、已完成工作、未决问题和下一步。
- **软件测试与故障注入**：强制中途 compaction、摘要后找回被隐藏的事实、检查是否误报完成，类似对状态恢复路径做 fault injection；goal success rate 和 needle-in-a-haystack 是比“窗口没有溢出”更接近真实可靠性的验收指标。
- **工作系统的持久状态**：文章隐含的组织级迁移是：目标不能只存在于一次对话里，而要存在于可审查、可更新、可恢复的外部 artifact 中。这与 [[Plan-as-Agent-Checkpoint|计划即 Agent 检查点]] 和 [[Agent-Harness|Agent Harness]] 的状态外置原则同构。

#### 3b. 旁逸：四种机制其实是一条“状态外化阶梯”

综合判断：这四种机制不是四个孤立技巧，而是在不同时间尺度上搬运 Agent 状态。

```text
进入上下文前：预算 / 卸载        → 控制什么能进来
上下文将满时：Compaction         → 有损压缩连续历史
每轮执行之间：Todo recitation     → 把目标重新放到近期注意力
会话结束之后：持久记忆            → 保存可跨任务复用的状态
```

它们分别优化 **新鲜度、可恢复性、注意力成本和跨会话连续性**。因此“记忆越多越好”与“摘要越短越好”都不是正确目标；正确目标是让任务所需状态在合适的时间尺度上可见、可恢复且可验证。这个判断是本次编译综合，不是原文直接提出的定理。

#### 3c. 约束

- **硬约束（世界）**：上下文容量、注意力稀释、延迟和推理成本有限；摘要天然有损；外部文件只有在 Agent 能检索、读取和解释时才等于可用状态。
- **软约束（实现）**：触发阈值、保留多少最近文件、todo 重写频率、记忆抽取策略和 compaction prompt 都应随模型、任务长度和风险等级调节。
- **自设约束（产品选择）**：是否默认启用 todo、是否把全文 transcript 落盘、是否把 memory 放进每次启动上下文，都是具体 Harness 的策略，不是 Agent 的普遍定律。

## 冲突标记

| 来源 | 观点 | 前提条件 |
|------|------|---------|
| [[20260912-context-engineering-inside-the-harness]]（转述 Manus / Anthropic） | 反复重写 todo 或外部笔记能把目标拉回近期注意力，降低长程漂移 | 任务足够长，且 todo 的维护成本小于它带来的目标保持收益 |
| [[20260912-context-engineering-inside-the-harness]]（转述 LangChain Deep Agents v0.7） | 三类任务评测中关闭 todos 略高 reward、成本更低，因此 `TodoListMiddleware` 改为 opt-in | 评测任务、模型和 todo 工具成本属于特定设置；不能直接否定长任务中的条件性收益 |

> [!warning] 两个观点并不必然矛盾：一个讨论机制在长程任务中的作用，一个讨论特定评测集上的平均收益；应按任务长度、模型能力和 UI 需求选择，而不是把 todo 设为绝对规则。

## 与既有知识的关系

- **[[Context-Engineering|上下文工程]]**：本文提供一组面向长程 Agent 的机制化切片，补充“最小高信号 token 集合”之外的状态生命周期视角。
- **[[Agent-Harness|Agent Harness]]**：四种机制说明 Harness 不只是工具调用循环，还负责证据进入、状态持久化、上下文刷新和恢复。
- **[[Context-Rot|Context Rot]]**：Context Rot 是需要管理的退化约束；预算、卸载、压缩和新鲜上下文是工程缓解手段，不是消除该约束。
- **[[Compaction]]**：本文将 Pi/编码 Agent 的 compaction 放入 Claude Code、Deep Agents、OpenAI 与 Claude API 的横向实现中，增加 goal preservation 与恢复路径维度。
- **[[Progressive-Disclosure|渐进式披露]]**：工具 schema 延迟加载、文件路径指针和子 Agent 摘要都是“先给地图、按需取细节”的运行时实现。
- **[[Memory-Architecture|记忆架构]]**：跨会话 memory 必须同时考虑抽取策略、召回路径和每次重载的注意力成本。
- **[[Agentic-Memory-Dosage|Agentic Memory Dosage]]**：本文关于记忆成本的警告与“记忆剂量需按模型调节”相互印证，但本文没有提供独立剂量实验。

## 证据边界

- 本页可直接支撑：这篇 MarkTechPost 文章提出了什么、如何组织四种机制、它引用了哪些产品实现和评测建议。
- 本页不能单独支撑：20,000/85% 等阈值对所有产品的普遍适用性、各厂商实现的当前行为、ETH Zurich 成本数字的完整实验结论。
- 需要继续核查的原始来源包括：AWS Agent Harness 设计指南、Anthropic Context Engineering / Claude Code 文档、LangChain Deep Agents v0.7 与 context management 博文、Manus context engineering 文章、OpenAI Responses compaction 文档和 AgentCore Memory / Evaluations 文档。

### 关联概念

- [[Context-Engineering]]
- [[Agent-Harness]]
- [[Context-Rot]]
- [[Compaction]]
- [[Progressive-Disclosure]]
- [[Plan-as-Agent-Checkpoint]]
- [[Memory-Architecture]]
- [[Agentic-Memory-Dosage]]
