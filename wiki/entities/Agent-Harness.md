---
type: entity
title: Agent Harness
aliases:
  - Agent Harness
  - agent harness
definition: "包装 LLM 的完整软件基础设施——编排循环、工具、记忆、上下文管理、状态持久化、错误处理和护栏，将无状态 LLM 转变为有状态的 Agent"
created: 2026-05-11
updated: 2026-05-25
tags:
  - AI-Agent
  - architecture
  - infrastructure
related_entities:
  - "[[Harness-Engineering]]"
  - "[[Context-Engineering]]"
  - "[[Agent-Orchestration]]"
  - "[[Agent-Workflow-Patterns]]"
  - "[[Agent-Loops]]"
  - "[[Multi-Layer-Memory]]"
  - "[[ACI-Agent-Computer-Interface]]"
  - "[[Building-Effective-Agents]]"
  - "[[Agentic-Engineering]]"
  - "[[Multi-Agent-System-Pathology]]"
  - "[[Agent-Dissociation]]"
source_raw:
  - "[[The Anatomy of an Agent Harness]]"
  - "[[Maintainability sensors for coding agents]]"
  - "[[Multi-Agent 火了，但 AI 的组织病还没人治｜Hao好聊趋势]]"
---

# Agent Harness

> [!definition] 定义
> **Agent Harness** 是包装 LLM 的完整软件基础设施——编排循环、工具层、记忆系统、上下文管理、状态持久化、错误处理和安全护栏。它将无状态 LLM 转变为有状态、可执行工具、能自我纠正的 Agent。Anthropic 官方定义："the agent harness that powers Claude Code."

## 核心区分：Agent vs Harness

Agent 是**涌现行为**——用户交互的目标导向、工具使用、自我纠正实体。Harness 是**产生该行为的机器**。当有人说"我构建了一个 Agent"，实际意思是他们构建了一个 harness 并指向一个模型。

LangChain 的 Vivek Trivedy 公式：**"If you're not the model, you're the harness."**

## Von Neumann 类比

Beren Millidge (2023) 的精确类比：

| 计算机组件 | Agent 对应 |
|-----------|-----------|
| CPU | 原始 LLM |
| RAM（快速但有限） | 上下文窗口 |
| 磁盘（大但慢） | 外部数据库 |
| 设备驱动 | 工具集成 |
| 操作系统 | **Harness** |

> "We have reinvented the Von Neumann architecture" — Beren Millidge

## 三层工程

| 层级 | 范围 |
|------|------|
| **Prompt Engineering** | 设计模型接收的指令 |
| **Context Engineering** | 管理模型看到什么、何时看到 |
| **Harness Engineering** | 以上两者 + 完整应用基础设施 |

Harness 不是 prompt 的包装，而是使自主 Agent 行为成为可能的完整系统。

## 12 个生产级组件

### 1. 编排循环 (Orchestration Loop)

心跳。实现 Thought-Action-Observation (TAO) 循环，也称 ReAct 循环：组装 prompt → 调用 LLM → 解析输出 → 执行工具调用 → 反馈结果 → 重复。

Anthropic 称其运行时为"dumb loop"——所有智能在模型中，harness 只管理轮次。

### 2. 工具层 (Tools)

Agent 的手。定义为 schema（名称、描述、参数类型）注入 LLM 上下文。处理：注册、schema 验证、参数提取、沙箱执行、结果捕获、格式化为 LLM 可读的观察。

### 3. 记忆 (Memory)

多时间尺度运作：
- **短期记忆**：单次会话内的对话历史
- **长期记忆**：跨会话持久化（[[CLAUDE-md|CLAUDE.md]] / MEMORY.md、JSON Stores、Sessions）

Claude Code 三级层次：轻量索引（~150 字符/条目，始终加载）→ 详细主题文件（按需加载）→ 原始记录（仅通过搜索访问）。关键原则：**Agent 将自己的记忆视为"提示"，行动前验证实际状态。**

### 4. 上下文管理 (Context Management)

核心问题：**上下文腐烂**——关键内容落在上下文窗口中间位置时，模型性能下降 30%+（Chroma 研究 + Stanford "Lost in the Middle"）。

生产策略：
- **压缩 (Compaction)**：接近限制时总结对话历史
- **观察掩码 (Observation Masking)**：隐藏旧工具输出，保留工具调用可见
- **即时检索 (JIT Retrieval)**：维护轻量标识符，动态加载数据
- **子 Agent 委派**：每个子 Agent 广泛探索但仅返回 1,000-2,000 token 摘要

目标：找到**最小的高信号 token 集合**，最大化期望结果的可能性。

### 5. Prompt 构建 (Prompt Construction)

分层组装：系统 prompt → 工具定义 → 记忆文件 → 对话历史 → 当前用户消息。

OpenAI Codex 优先级栈：服务端系统消息（最高）→ 工具定义 → 开发者指令 → 用户指令（级联 AGENTS.md，32 KiB 限制）→ 对话历史。

### 6. 输出解析 (Output Parsing)

现代 harness 依赖原生 tool calling，模型返回结构化 tool_calls 对象。检查：有工具调用？执行并循环。无工具调用？那就是最终答案。

### 7. 状态管理 (State Management)

LangGraph：类型化字典流过图节点，super-step 边界检查点。Claude Code：**git commits 作为检查点，进度文件作为结构化草稿本。**

### 8. 错误处理 (Error Handling)

10 步流程，每步 99% 成功率 → 端到端仅 ~90.4%。错误快速复合。

四种错误类型：瞬态（退避重试）、LLM 可恢复（返回错误作为 ToolMessage）、用户可修复（中断等待人工）、意外（上报调试）。Stripe 生产 harness 限制重试不超过两次。

### 9. 护栏与安全 (Guardrails & Safety)

三级：输入护栏、输出护栏、工具护栏。"绊线"机制触发时立即停止 Agent。

Anthropic 架构分离：模型决定尝试什么，工具系统决定允许什么。Claude Code 独立门控 ~40 个离散工具能力。

### 10. 验证循环 (Verification Loops)

区分玩具 demo 与生产 Agent 的关键。三种方式：基于规则的反馈（测试/linter/类型检查器）、视觉反馈（Playwright 截图）、LLM-as-Judge（单独子 Agent 评估输出）。

Boris Cherny：**给模型验证自身工作的方式，质量提升 2-3x。**

Birgitta Böckeler 对这层做了更细的落地：同一套 sensor 不只存在于 CI 末端，而是分布在编码会话、集成后复验和周期性审查三个时间尺度。type checker、ESLint、Semgrep、dependency-cruiser、测试覆盖、增量 mutation testing 与 GitLeaks 负责给 Agent 持续反馈；自定义 lint message 则把这些反馈进一步转成可执行的自我纠正指令。

### 11. 子 Agent 编排 (Subagent Orchestration)

Claude Code 三种执行模型：Fork（父上下文字节级复制）、Teammate（独立终端窗格 + 文件邮箱通信）、Worktree（独立 git worktree + 隔离分支）。

### 12. 安全执行环境 (Sandboxed Execution)

工具在沙箱环境中执行，读取操作可并发，变更操作串行。

## 7 个架构决策

### 1. 单 Agent vs 多 Agent

Anthropic 和 OpenAI 都说：先最大化单 Agent。多 Agent 增加开销（额外 LLM 调用、上下文丢失）。仅在工具过载超过 ~10 个重叠工具或明确分离的任务域时才拆分。

Hao 好聊趋势的 multi-agent 组织病文章补充了第二个理由：多 Agent 不只是增加工程开销，也会引入 [[Multi-Agent-System-Pathology|组织病理]]。harness 可以治理动作、权限和上下文，但如果 Agent 需要彼此讨论、形成共识或接受不可见编排，还会出现从众、责任稀释和 [[Agent-Dissociation|内态解离]] 这类更深问题。

### 2. ReAct vs Plan-and-Execute

ReAct 每步交织推理和行动（灵活但每步成本高）。Plan-and-Execute 分离规划与执行。LLMCompiler 报告比顺序 ReAct **快 3.6x。**

### 3. 上下文窗口管理策略

五种生产方案：基于时间的清除、对话总结、观察掩码、结构化笔记、子 Agent 委派。ACON 研究通过优先推理痕迹而非原始工具输出，实现 **26-54% token 减少同时保持 95%+ 准确率。**

### 4. 验证循环设计

计算验证（测试/linter）提供确定性 ground truth。推理验证（LLM-as-Judge）捕获语义问题但增加延迟。Martin Fowler 框架：**guides（前馈，行动前引导）vs sensors（反馈，行动后观察）。**

生产级 harness 的问题不只是“有没有 sensor”，而是 sensor 是否分布在正确时间尺度、是否会给 Agent 太多噪声，以及反馈文本本身是否足够可执行。

### 5. 权限与安全架构

宽松（快速但有风险）vs 严格（安全但慢）。取决于部署上下文。

### 6. 工具作用域策略

更多工具往往意味着更差的性能。Vercel 从 v0 中**移除 80% 工具**后效果更好。Claude Code 通过懒加载实现 **95% 上下文缩减。** 原则：暴露当前步骤所需的最小工具集。

### 7. Harness 厚度

多少逻辑放在 harness 中 vs 模型中。Anthropic 押注薄 harness + 模型改进。图框架押注显式控制。Anthropic 定期从 Claude Code 的 harness 中删除规划步骤，因为新模型版本内化了该能力。

## 脚手架隐喻

建筑脚手架是临时基础设施，使工人能够到达无法触及的楼层。它不做建筑工作，但没有它工人到不了高层。**关键洞察：建筑完成时脚手架被拆除。** 随着模型改进，harness 复杂度应降低。

Manus 在六个月内重建了五次，每次重写都移除了复杂性。复杂工具定义变成通用 shell 执行。"管理 Agent"变成简单的结构化交接。

**共进化原则**：模型现在在训练时将特定 harness 纳入循环。Claude Code 的模型学会了使用它被训练的特定 harness。更改工具实现可能因这种紧密耦合而降低性能。

**面向未来的测试**：如果性能随更强大的模型提升而无需增加 harness 复杂度，设计就是正确的。

## 关键数据点

- LangChain 仅改变 harness（同一模型、同一权重）就从 Top 30 外跃升至 TerminalBench 2.0 第 5 名
- 独立研究项目通过让 LLM 自身优化 harness 实现 76.4% 通过率，超越手工设计系统
- 上下文窗口中间位置内容使模型性能下降 30%+
- Vercel 移除 80% 工具后效果更好
- Claude Code 通过懒加载实现 95% 上下文缩减
- LLMCompiler 比顺序 ReAct 快 3.6x
- ACON 实现 26-54% token 减少，保持 95%+ 准确率
- 10 步流程每步 99% 成功率 → 端到端仅 ~90.4%
- 验证循环使质量提升 2-3x（Boris Cherny）
- Claude Code 独立门控 ~40 个离散工具能力
- Manus 六个月内重建五次

## 前提与局限性

- Harness 有效性高度依赖具体模型——更换 harness 可能只是针对特定 benchmark 优化，而非通用能力提升
- "薄 harness"假设模型能持续内化当前 harness 功能，但新能力可能只是增加新的复杂性维度
- 共进化原则暗示模型和 harness 的锁定效应——更换 harness 需要重新训练模型
- 12 组件框架是对多个框架的综合抽象，实际实现中组件边界可能模糊
- 大部分数据来自框架自述（Anthropic、OpenAI、LangChain），独立验证有限

## 关联概念

- [[Harness-Engineering|Harness Engineering]] — Agent Harness 的工程实践视角，强调团队如何构建和维护 harness
- [[Context-Engineering|Context Engineering]] — Harness 的第 4 和第 5 组件，管理模型看到什么
- [[Agent-Orchestration|Agent Orchestration]] — Harness 的第 1 和第 11 组件，管理多 Agent 协作
- [[Agent-Loops|Agent Loops]] — Harness 心跳，TAO/ReAct 循环的调度范式
- [[Multi-Layer-Memory|Multi-Layer Memory]] — Harness 第 3 组件，多时间尺度记忆系统
- [[Agent-Workflow-Patterns|Agent Workflow Patterns]] — Harness 架构模式集合
- [[ACI-Agent-Computer-Interface|ACI]] — 工具层的接口设计原则
- [[Building-Effective-Agents|Building Effective Agents]] — Anthropic 的 harness 构建指南
- [[Agentic-Engineering|Agentic Engineering]] — 在 harness 之上实现的工程范式
- [[Agentic-Workflow-Token-Efficiency|Agentic Workflow Token Efficiency]] — 上下文管理策略的 token 优化
- [[Multi-Agent-System-Pathology]] — 多 Agent harness 成功后暴露的群体认知和组织治理风险
