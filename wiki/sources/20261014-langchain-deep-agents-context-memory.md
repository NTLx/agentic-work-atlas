---
type: source-summary
title: "Context Engineering: How Deep Agents Remember"
canonical_url: "https://www.langchain.com/blog/context-engineering-deep-agents-remember"
raw_state: index
original_raw_file: "20261014-langchain-deep-agents-context-memory.md"
original_body_sha256: "9929e63b6fc79d7c2ba898cdb051db7a7626f6bf9a5e947a8dcbb6a87bc6d879"
indexed_at: "2026-10-22T16:52:33+08:00"
created: 2026-10-22
updated: 2026-10-22
tags:
  - source-summary
  - context-engineering
  - memory
  - progressive-disclosure
  - agent-harness
evidence_level: medium
claim_type: mixed
source_locator:
  - "Raw L29-L67：context rot、两类 context management、Deep Agents 五种机制"
  - "Raw L87-L120：middleware 与 tool-result/user-message offloading；约 20K/50K token 实现阈值"
  - "Raw L122-L163：summarization、85% default threshold、recoverable conversation history"
  - "Raw L165-L199：skills progressive disclosure；只加载 SKILL.md header/menu 与按需全文"
  - "Raw L201-L245：subagent context isolation、long-term memory plain files、provider/model portability"
  - "Raw L247-L260：六条通用设计原则：offload not truncate、recoverable compaction、on-demand know-how、isolate noise、own memory、customizable defaults"
---

# Context Engineering: How Deep Agents Remember

> LangChain 于 2026-10-14 发布的 Deep Agents 概念指南，给出其 open-source agent harness 如何通过 middleware 管理长程上下文和跨会话记忆。文章提供明确实现细节与默认阈值，但主要是框架方对自身设计的解释，没有独立 benchmark 证明五种机制各自的因果收益，因此按 `medium / mixed` 处理。

## 编译摘要

### 1. 浓缩

#### 核心结论 1：Context Engineering 同时需要“入口控制”和“存量治理”

文章把 context rot 的处理分成两类：

- **prevent unnecessary information from entering**：offloading、skills、subagents 等，让噪声不要先进入主 context；
- **manage/filter what is already in context**：summarization 等，在长任务中持续压缩已积累历史。

这使 [[Context-Engineering]] 的运行时定义更完整：不是只有 retrieval（找什么进来），还包括 **context lifecycle management（进来之后如何卸载、压缩、隔离、恢复）**。

#### 核心结论 2：好的 compaction 不是删除，而是把 active context 变成可恢复索引

Deep Agents 的 offloading 与 summarization 都强调 recoverability：

- 大 tool result 写入 `/large_tool_results/{tool_call_id}`，主模型只看 preview + path；
- 超大 human message 写入 `/conversation_history/`；
- summarization 后旧消息虽然从 active window 移除，但原始内容保存在 `/conversation_history/{session_id}.md`，需要时可重新读取。

**判断**：这里真正稳定的原则不是 20K、50K、85% 这些当前实现阈值，而是 **active window ≠ source of truth**。窗口应只承载当前高价值 working set，原始细节留在可寻址的外部存储。

这与 LLM WiKi 自身 `entity/source-summary → raw evidence` 的渐进读取模式高度同构。

#### 核心结论 3：Skills 是 executable progressive disclosure

Deep Agents 只把每个 skill 的短 description/header 放进系统上下文；完整 `SKILL.md` 只有在模型判断任务相关时才通过 `read_file` 加载。LangChain 将其明确称为 **progressive disclosure**。

因此 [[Progressive-Disclosure]] 可以从“知识组织原则”进一步写成 Agent Harness 的执行机制：

```text
always-visible menu / metadata
  → relevance decision
  → on-demand full instructions
  → task execution
```

它的价值不仅是 token 节省，还在于避免不相关 instructions 同时竞争模型注意力。

#### 核心结论 4：Subagent 的重要价值之一是 context isolation，而不只是 parallelism

文章用 competitive analysis 举例：market researcher subagent 可以读取大量原始数据和搜索结果，但主 Agent 只收到三条结论。这样 noisy intermediate state 不会污染主工作线程。

**判断**：subagent topology 可以被理解为一种 **attention isolation primitive**。是否并行只是调度属性；更基础的价值是让高噪声探索发生在独立 context，主 Agent 接收经过 contract 压缩的结果。

#### 核心结论 5：Memory portability 来自“状态外置 + 用户拥有”，而非模型自身记住

Deep Agents 的 long-term memory 是用户控制存储中的普通 Markdown 文件：run 开始 load，每次 model call inject，学习到值得保留的信息后 update。因为记忆不绑定模型提供商，同一 backend 可以换模型而继续读取同一 memory。

这给长期 Agent 一个清晰的架构边界：**memory belongs to the system, not the model session**。模型可以替换，memory/provenance/store 应尽可能保持可检查、可迁移。

### 2. 实现细节与边界

- Tool result 大约 20,000 tokens、human message 50,000 tokens、summarization 85% context usage 都是 Deep Agents 当前默认或示例阈值，不是跨模型的理论常数。
- Summarization 会引入摘要误差；“可恢复”降低损失，但前提是 Agent 能意识到需要回读原文并找到正确文件。
- 文件式 long-term memory 容易审计和迁移，但持续 inject 整份 memory 本身仍可能重新制造 context growth，需要进一步分层/检索。
- Subagent 只返回压缩结果会降低主 Agent 的直接证据可见性；高风险场景仍应提供 provenance 或可回溯 artifact。

### 3. 跨来源综合

- 与 [[Context-Engineering]]：把已有的“最小高信号 token 集”进一步实现为 middleware 驱动的 context operating system。
- 与 [[Progressive-Disclosure]]：LangChain 提供了 Skill 层一手实现证据，证明“先目录、后全文”已经成为主流 harness pattern，而不是仅 Wiki 设计原则。
- 与 [[Compaction]]：补充 `recoverable compaction` 边界——摘要负责 active working set，原文必须保留外部恢复路径。
- 与 [[Agent-Harness]]：context management 是 harness responsibility，不应要求模型仅靠 prompt 自律地“记少一点”。
- 与 [[Retrieval-as-a-Subagent]]：subagent 不只承担 retrieval，还承担 noisy-context containment。

## 编译决策

不新增 `Deep Agents Memory` Entity。本文高价值部分已经由 [[Context-Engineering]]、[[Progressive-Disclosure]]、[[Compaction]] 等稳定节点覆盖，本轮应补强这些实体而不是增加产品级碎片。