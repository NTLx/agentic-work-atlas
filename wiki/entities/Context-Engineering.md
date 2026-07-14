---
type: entity
title: Context Engineering
aliases:
  - Context Engineering
definition: "设计 Agent 每次推理时看到的信息结构，包括项目上下文、技能按需加载、记忆层级和上下文生命周期管理"
created: 2026-04-09
updated: 2026-07-09
evidence_level: high
claim_type: mixed
tags:
  - AI-Agent
  - OpenClaw
  - architecture
related_entities:
  - '[[Agent-Orchestration]]'
  - '[[Multi-Layer-Memory]]'
  - '[[Claude-Code-CLI]]'
  - '[[Conceptual-Model]]'
  - '[[Model-Context-Protocol-MCP]]'
  - '[[CLAUDE-md]]'
  - '[[Three-Layer-Agent-Memory]]'
  - '[[Capability-Map]]'
  - "[[Agentic-Analytics]]"
  - "[[Enterprise-AI-Learning-Gap]]"
  - "[[Agent-Legibility]]"
  - "[[Context-Minimalism]]"
  - "[[Company-Brain]]"
  - "[[Retrieval-as-a-Subagent]]"
source_raw:
  - '[[OpenClaw + 6 个 Agent 运转半个月，从聊天到干活的完整工程实践]]'
  - '[[What Is Code?]]'
  - '[[Building an MCP Ecosystem at Pinterest]]'
  - '[[The-Founders-Playbook-05062026_v3]]'
  - '[[20260526-obsidian-claude-code-brain]]'
  - '[[20260530-cursor-developer-habits-report]]'
  - "[[20260603-anthropic-self-service-data-analytics]]"
  - "[[20260608-become-ai-native-org]]"
  - "[[20260611-openai-harness-engineering]]"
  - "[[20260702-anthropic-context-engineering]]"
  - "[[20260713-microsoft-ships-ai-agents-enterprise-scale]]"
---

# Context Engineering

> [!definition] 定义
> Context Engineering（上下文工程）是设计 Agent 每次推理时看到的完整信息结构——系统级的信息架构设计。Unmesh-Joshi 指出，一个具有稳定词汇和清晰 [[Conceptual-Model|概念模型]] 的代码库本身就是最重要的上下文工程（Context Engineering）。

## 核心实践案例

### Anthropic：Context Engineering 的工程框架（2026-06）

Anthropic Applied AI 团队（2026-06）给出了 Context Engineering 的系统化定义：**在有限注意力预算下，找到最小的高信号 token 集合来最大化期望行为**。核心理由来自 Transformer 的 n² 注意力机制——context 越长，每个 token 捕获成对关系的能力越被稀释（[[Context-Rot]]）。

三个关键策略：

- **Compaction（压缩）**：接近 context window 限制时总结对话历史，保留架构决策/未解决 bug/实现细节，丢弃冗余工具输出。先最大化召回率，再迭代提升精确率
- **Structured Note-Taking（结构化笔记）**：Agent 主动写笔记持久化到 context 外部，跨 context reset 保持状态。Claude 玩 Pokemon 时用此技术维护精确计数、探索地图和策略笔记
- **Sub-Agent 架构**：专业化子 Agent 在清洁 context 中执行深度工作，返回 1,000-2,000 token 压缩摘要。在复杂研究任务上显著优于单 Agent 系统

**"Just in Time" 检索**：Agent 持有轻量标识符（文件路径、查询、链接），运行时动态加载数据，配合 [[Progressive-Disclosure]] 逐层发现。Claude Code 用此模式——写入定向查询，用 `head`/`tail` 分析大数据而不加载完整对象到 context。

**System Prompt 的 "Right Altitude"**：Goldilocks zone——不过度硬编码（脆性），也不过度模糊（无信号）。具体到能有效引导，灵活到能提供强启发式。

### Pinterest：按需注入工具（Domain-specific MCP）
[[Pinterest-Engineering]] 通过拆分多个领域特定的 **[[Model-Context-Protocol-MCP|MCP]]** 服务器，实现了上下文的“按需加载”。Agent 在处理 Presto 数据时只加载 Presto 相关的工具，而不是将所有（如 Spark, Airflow）工具全部堆在上下文窗口中。这有效地减少了噪声，提高了 Agent 决策的准确性。

### Anthropic：数据分析中的语义上下文

[[Agentic-Analytics]] 把 Context Engineering 的边界讲得更硬：不是把 data warehouse、历史 SQL 和文档全塞给 Claude，而是构造 canonical datasets、semantic layer、domain skills、evals 和 provenance。

Anthropic 的关键数据点是，访问数千个历史 SQL 文件只带来不到 1 个百分点准确率提升；没有 skills 时准确率不超过 21%，有 skills 后整体超过 95%。这说明上下文工程的核心不是资料数量，而是资料是否处在正确抽象层、是否有 owner、是否能被评测和维护。

## 核心问题：Agent 系统的热力学第二定律

**不加约束，entropy 只增不减。** 持续运行的 Agent 系统会**确定性地**走向崩溃。

Agent 就像一个没有操作系统的进程：
- 谁来管理它的内存（上下文）？
- 谁来做垃圾回收（Session 清理）？
- 谁来防止 OOM（膨胀保护）？

不设计就没有人管。

## 三学科交叉本质（07-09 深度思考）

Context Engineering 不是单一学科的应用，而是三个学科的交叉地带：信息论（Shannon 信道编码——管理信息量）、非平衡态热力学（Prigogine 耗散结构——管理动态熵增）、结构设计（Alexander 模式语言——管理结构质量）。三者缺一都是盲人摸象。

Token 同时支付计算成本（Token FinOps 管理）和信息维持成本（Context Engineering 管理），两者耦合在同一个 Pareto 前沿——更好的 context 结构 → 更少的 token → 更好的结果（Anthropic skills 数据：21%→95%）。

终态不是"零 context"也不是"无限 context"——是动态稳态（信息如河流持续流动但总量稳定）。这个稳态永远需要人类参与——人类 Context Advantage 的结构维度（架构直觉、概念框架）不可编码为 token，与 [[Agent-Loops]] 的人类参与线是同一个不可压缩下界。来源：07-09 深度思考（roundtable+qa）

## 上下文层级结构

```
~/.claude/CLAUDE.md     ← 全局（所有项目通用）
~/project/CLAUDE.md     ← 项目级（当前项目专用）
~/project/src/CLAUDE.md ← 子目录级（进入该目录时加载）
```

所有层级是**叠加**的，不会覆盖。

[[CLAUDE-md]] 位于这个层级结构中的项目级和目录级位置：它把架构决策、范围边界和稳定规则放到 Agent 每次工作都能读取的位置，避免同一个代码库在不同会话里被反复重新解释。

## Agent 信息架构设计

| 层级 | 文件 | 内容 | 特点 |
|-----|------|------|------|
| **身份层** | SOUL.md | 身份定义、决策框架、绝对禁止项 | 放在 system prompt 最前面，精简核心 |
| **操作层** | AGENTS.md | 操作规范和协作协议 | 跟在 SOUL.md 后面 |
| **技能层** | Skills | 可复用知识包 | 通过 extraDirs 按需加载 |
| **冷存储** | Obsidian Vault | 归档产出 | 不参与推理 |

## LLM 上下文窗口的特性

**上下文窗口不是等价的**：
- system prompt 前面的信息权重远高于后面的
- session 膨胀到几万 tokens 后，早期消息的影响力被稀释

类比操作系统的内存管理：**热数据放缓存，冷数据放磁盘，关键数据常驻内存**。

## 按需加载策略

Trading 的 15 个 Skills（68000+ 行）：
- `stock_analysis`（技术面评分）在每日扫描时才需要
- `bilateral_analysis`（龙虎榜分析）只在异动时触发

全部常驻上下文的话，**噪声淹没了真正重要的规则**。通过 `extraDirs` 按需注入，每次推理只加载相关的 1-3 个 Skill。

## 规则措辞原则

**面向最弱的模型写规则**：

| 措辞 | GPT-5.4 | Qwen3.5+ | qwen3:8b |
|-----|---------|----------|----------|
| `"建议不要编造数据"` | 基本遵守 | 偶尔遵守 | 几乎无视 |
| `"MUST: 不编造数据"` | 高遵守 | 显著提升 | 较高遵守 |
| `"MUST + P0 + NON-NEGOTIABLE"` | 很高 | 高 | 高 |

多模型 fallback 时，所有关键规则都要按最弱模型的理解能力来写。**显式 > 隐式，硬规则 > 软建议**。

## Harness 框架自动管理

| 机制 | 触发条件 | 动作 |
|-----|---------|------|
| compaction memoryFlush | Session > 40K tokens | 提取精华到 memory/YYYY-MM-DD.md |
| contextPruning | 上下文 > 6 小时 | cache-ttl 裁剪，保留最近 3 条 |
| session reset | 每天 5:00 或空闲 30min | 自动重置 |
| session maintenance | 文件 > 7 天 | 自动清理，磁盘上限 100MB |

## 真实事故案例

### P0 — 全团队瘫痪 8 小时

ainews 的 session 因连续处理新闻累积到 **235K tokens**。Gateway 启动时对所有 session 做 compaction，这个 session 永远超时 → crash → macOS 守护进程每秒重启 → 无限循环。所有 Agent 全部离线。

修复要四层：手动清理膨胀 session → ThrottleInterval 1→10 → idleMinutes 180→30 → exec.security full→allowlist。

### P2 — 信息过载后关键规则失效

当 SOUL.md 堆满各种操作规范、session 膨胀到几万 tokens，Agent 开始"选择性遵守"规则。管家蜘蛛越界做投资分析，交易蜘蛛忽略数据验证规则。**关键信息被噪声淹没了**。

## Token 经济学实证：上下文已成主要成本

Cursor 2026 春季报告用大规模产品数据印证了上下文工程的经济重要性：

### Input Token 主导非缓存 Token 量

- Input tokens 占 input/output 非缓存 token 的 **90%+**
- 上下文（context）已成为非缓存模型使用的主导部分

### Input Token 成为主要成本驱动

- Input tokens 的价格等效成本占比从年初约 50% 升至近 **70%**
- 虽然 input token 单价低于 output token，但体量的压倒性优势使其成为主要成本

### Cache-Read Token 主导总 Token 活动

- 当包含缓存后，**cache-read tokens 主导总 token 活动**
- Agent 工作越来越依赖**复用先前的上下文**而非每次从头读取
- Cursor 持续改进 agent harness 以优化跨模型和提供商的 token 缓存

> [!important] 核心洞察
> **Agent 工作的主要成本不再是"生成回答"（output），而是"理解上下文"（input + cache）。** 这意味着上下文工程的优化方向不只是让模型看到更好的信息，而是让模型用更少的成本看到必要的信息。

## 关键数据点

- P0 事故：ainews session 累积到 235K tokens，导致 Gateway compaction 超时 → crash → 无限重启 → 全团队瘫痪 8 小时
- Input tokens 占非缓存 token 的 90%+，价格等效成本占比从年初约 50% 升至近 70%（Cursor, 2026 春季）
- Cache-read tokens 主导总 token 活动，Agent 工作越来越依赖上下文复用（Cursor, 2026 春季）
- Anthropic analytics：无 skills 时准确率不超过 21%，有 skills 后整体超过 95%；原始 SQL corpus 访问只带来不到 1 个百分点提升
- Analytics skills 若不维护，一个月内准确率可从约 95% 掉到约 65%；约 90% 数据模型 PR 包含 skill 变更
- P1 事故：3500 字报告被框架 content compaction"优化"到 800 字，数据表格被"智能压缩"掉
- P2 事故：SOUL.md 信息过载 + session 膨胀后，Agent 开始"选择性遵守"规则
- Harness 四个机制：compaction memoryFlush（>40K tokens）、contextPruning（>6h）、session reset（每天 5:00 或空闲 30min）、session maintenance（>7d，磁盘上限 100MB）
- Trading 有 15 个 Skills 共 68000+ 行，通过 extraDirs 按需加载，每次推理只加载 1-3 个
- 规则措辞面向最弱模型：`"建议不要编造数据"`→qwen3:8b 几乎无视，`"MUST + P0 + NON-NEGOTIABLE"`→各模型都高遵守

## 前提与局限性

- Context Engineering 必须与 Harness 协同——只有前者，session 膨胀后一样崩溃；只有后者，关键规则被噪声淹没
- SOUL.md 必须精简，因为 system prompt 前面的信息权重远高于后面
- 规则措辞必须按最弱模型的理解能力来写（多模型 fallback 环境下不知道哪次推理会用弱模型）
- Context 层级是叠加而非覆盖，需注意各层级内容不冲突

## 关联概念

- [[Multi-Layer-Memory]] — 上下文工程与分层记忆协同
- [[Agent-Orchestration]] — 编排层持有业务上下文
- [[Agent-Swarm]] — Swarm 需要专业的上下文配置
- [[Agent-First-Enterprise]] — 上下文工程是 Agent-First 的技术基础设施

## 来源
