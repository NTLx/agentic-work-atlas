---
type: entity
title: Agent Harness
aliases:
  - Agent Harness
  - agent harness
definition: "包装 LLM 的完整软件基础设施——编排循环、工具、记忆、上下文管理、状态持久化、错误处理和护栏，将无状态 LLM 转变为有状态的 Agent。Addy Osmani (2026) 总结公式：**coding agent = AI model(s) + harness**。"
created: 2026-05-11
updated: 2026-06-13
evidence_level: high
claim_type: mixed
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
  - "[[Agent-Containment]]"
  - "[[Agent-Logic]]"
  - "[[Local-Bounded-Reasoning]]"
  - "[[Policy-as-Code-for-Agent-Governance]]"
  - "[[Graph-Guided-Agent-Investigation]]"
  - "[[Context-Rot]]"
  - "[[Ralph-Loops]]"
  - "[[HaaS-Harness-as-a-Service]]"
  - "[[AGENTS-md]]"
  - "[[Deterministic-Retrieval]]"
  - "[[NLAH]]"
source_raw:
  - "[[The Anatomy of an Agent Harness]]"
  - "[[Maintainability sensors for coding agents]]"
  - "[[Multi-Agent 火了，但 AI 的组织病还没人治｜Hao好聊趋势]]"
  - "[[Harness, Scaffold, and the AI Agent Terms Worth Getting Right]]"
  - "[[20260528-agentic-ai-2026-landscape]]"
  - "[[20260530-cursor-developer-habits-report]]"
  - "[[20260602-ibm-agent-logic-scalable-ai-adoption]]"
  - "[[20260419-agent-harness-engineering]]"
  - "[[20260608-paving-the-way-for-agents-in-biology]]"
  - "[[20260613-NLAH-natural-language-agent-harnesses]]"
  - "[[20260617-langchain-art-of-loop-engineering]]"
  - "[[20260617-langchain-agent-engineering-new-discipline]]"
  - "[[20260617-bayer-prince-agentic-rag]]"
  - "[[20260617-huggingface-agentic-resource-discovery]]"
  - "[[20260613-coding-agent-organizational-engineering]]"
  - "[[20260613-qoder-human-bottleneck]]"
  - "[[20260613-aliyun-agent-infra-constraint-infrastructure]]"
---

# Agent Harness

> [!definition] 定义
> **Agent Harness** 是包装 LLM 的完整软件基础设施——编排循环、工具、记忆、上下文管理、状态持久化、错误处理和护栏，将无状态 LLM 转变为有状态的 Agent。Addy Osmani (2026) 总结公式：**coding agent = AI model(s) + harness**。

## 核心区分：Agent vs Harness

Agent 是**涌现行为**——用户交互的目标导向、工具使用、自我纠正实体。Harness 是**产生该行为的机器**。当有人说"我构建了一个 Agent"，实际意思是他们构建了一个 harness 并指向一个模型。

LangChain 的 Vivek Trivedy 公式：**"If you're not the model, you're the harness."**

## Scaffold vs Harness：细粒度区分

HuggingFace（2026）对术语做了更细的拆分，以解决 ICLR 2026 后社区对 harness/scaffold 含义不收敛的困惑：

| 组件 | 定义 | 类比 |
|------|------|------|
| **Scaffold**（脚手架） | 行为定义层：系统提示、工具描述、输出解析、上下文管理——模型"看到"和"依据"的一切 | 剧本：演员按此表演 |
| **Harness**（harness，细粒度） | 执行层：调用模型、处理工具调用、决定何时停止——让 Agent "跑起来"的循环 | 导演：控制何时开拍、何时喊停 |

**两种用法并存**:
- **广义**: Harness = 模型之外的一切（Claude Code 官方文档："Claude Code serves as the agentic harness around Claude"）
- **细粒度**: Scaffold（行为定义）+ Harness（执行循环）分离，在训练管线中尤为重要——训练时 scaffold 定义 agent 如何行为，harness 管理 rollout 和梯度更新

**实践意义**: 当只关注推理侧时，广义用法足够。当需要独立推理行为（scaffold）和执行（harness）时——例如训练管线中 scaffold 不变但 harness 管理并行 rollout——区分才有价值。

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

Harness 是 prompt 的包装，而是使自主 Agent 行为成为可能的完整系统。

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

核心问题：**[[Context-Rot|上下文腐烂（Context Rot）]]**——随着上下文窗口填充，模型推理和任务完成能力下降，关键内容落在窗口中间位置时性能下降 30%+。

生产策略：
- **压缩 (Compaction)**：接近限制时总结对话历史
- **观察掩码 (Observation Masking)**：隐藏旧工具输出，保留工具调用可见
- **即时检索 (JIT Retrieval)**：维护轻量标识符，动态加载数据
- **上下文重置 (Context Reset)**：对于超长任务，销毁当前会话并根据紧凑的“移交文件（Hand-off file）”重建新鲜上下文（Anthropic 模式）。
- **子 Agent 委派**：每个子 Agent 广泛探索但仅返回 1,000-2,000 token 摘要

目标：找到**最小的高信号 token 集合**，最大化期望结果的可能性。

### 5. Prompt 构建 (Prompt Construction)

分层组装：系统 prompt → 工具定义 → 记忆文件 → 对话历史 → 当前用户消息。

OpenAI Codex 优先级栈：服务端系统消息（最高）→ 工具定义 → 开发者指令 → 用户指令（级联 [[AGENTS-md|AGENTS.md]]，32 KiB 限制）→ 对话历史。

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

Boris Cherny：**给模型验证自身工作的方式，质量提升 2-3x。** 在生物学等高精度领域，这层演化为**[[Deterministic-Retrieval|确定性检索层]]**（如 gget-virus），将混乱的界面操作转化为机器可验证的可靠步骤（Anthropic, 2026）。

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

IBM Research 的 [[Agent-Logic|agent logic]] 给这个问题增加了企业侧边界：在强结构工作流中，harness 不应只做模型调用和工具循环，还应承载知识图谱、程序分析、策略执行、图遍历和验证逻辑。判断标准不是”harness 越厚越好”，而是稳定、可验证、低熵的企业约束应留在模型外，开放、语义、跨上下文的部分才交给 LLM。

[[NLAH|Natural-Language Agent Harnesses (NLAH)]] 提出了另一种可能：把驾驭策略从代码中外置为可执行的自然语言文档。消融实验首次用数据回答了”harness 该保留哪些模块”——文件持久化状态是最稳正贡献，多候选搜索和上下文压缩反而有害。

## 脚手架隐喻

建筑脚手架是临时基础设施，使工人能够到达无法触及的楼层。它不做建筑工作，但没有它工人到不了高层。**关键洞察：建筑完成时脚手架被拆除。** 随着模型改进，harness 复杂度应降低。

Manus 在六个月内重建了五次，每次重写都移除了复杂性。复杂工具定义变成通用 shell 执行。"管理 Agent"变成简单的结构化交接。

**共进化原则**：模型现在在训练时将特定 harness 纳入循环。Claude Code 的模型学会了使用它被训练的特定 harness。更改工具实现可能因这种紧密耦合而降低性能。

**面向未来的测试**：如果性能随更强大的模型提升而无需增加 harness 复杂度，设计就是正确的。

## Harness 即平台：Cursor Automations 与 SDK

Cursor 2026 春季报告揭示了 harness 演化的下一个阶段：**从开发者工具变成可编程平台**。

- **Cursor Automations**: 自动化工作流（安全审查为首个强用例），采用增长迅速
- **SDK runs**: 将 Cursor 的 agent 基础设施作为可编程平台，按公司自定义方式构建和维护软件
- **平台化信号**: harness 不再只是单个开发者的编码助手，而是整个团队的软件构建系统
- **HaaS (Harness-as-a-Service)**: 从构建底层 API 转向构建 Harness 运行时 API。开发者不再从零构建循环，而是基于成熟的 Harness SDK 进行场景化配置。

> [!tip] 演化路径
> 单 Agent harness → 多 Agent harness → 自动化 harness → harness 即平台（SDK + Automations） → HaaS (Harness-as-a-Service)

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
- Cursor Automations 采用增长迅速，安全审查为首个强自动化用例；SDK runs 展示 harness 向可编程平台的演化（Cursor, 2026 春季）
- Cursor 持续改进 agent harness 以优化跨模型和提供商的 token 缓存（Cursor, 2026 春季）
- Anthropic 研究显示：科学 Agent 在无专用工具时检索准确率低至 16.9%，引入确定性检索层 gget-virus 后升至 99.7%（2026）。
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
- [[Agent-Infra]] — Agent Harness 概念在生态层面的扩展，从单个 harness 到整个 Agent 基础设施层
- [[Agent-Logic]] — 企业级 harness 中运行在模型外的工作流专用逻辑层
- [[Context-Rot]] — Harness 必须应对的上下文衰减现象
- [[Ralph-Loops]] — 实现长程任务的一种 Harness 循环技术
- [[HaaS-Harness-as-a-Service]] — Harness 的交付与平台化范式
- [[AGENTS-md]] — Harness 的核心配置与约束文件规范
- [[Deterministic-Retrieval]] — 在特定领域 Harness 中至关重要的确定性感知层
- [[NLAH]] — 将驾驭策略从代码中外置为自然语言文档的新范式
- [[Sleep-Token]] — Harness 基础设施使能的离线 Token 产出模式
- [[Constraint-Infrastructure]] — Harness 方法论的基础设施化落地，将约束原则映射为可编程的平台能力

## 四层循环堆叠模型（2026-06 更新）

LangChain（Vivek Trivedy）提出的四层模型是 Agent Harness 的分析框架，不是最优结构：

### 四层结构

| 层级 | 功能 | 必要性 |
|------|------|--------|
| **Agent loop** | 基础循环：感知-思考-行动 | 必须 |
| **Verification** | 验证层：检查输出是否正确 | 必须 |
| **Event-driven** | 事件驱动：处理外部事件和中断 | 可选 |
| **Hill climbing** | 自我改进：从错误中学习并优化 | 可选 |

### 关键洞察

1. **Verification 是必须的，其他层是可选的**：没有验证的 Agent 是危险的——它可能自信地输出错误结果
2. **验证深度取决于风险等级**：风险等级 = 失败成本 × 检测难度 × 影响范围
3. **四层模型是工具箱，不是最优结构**：每层可选，根据场景决定
4. **企业需要标准化验证策略**：预定义风险等级 + 标准化流程 + 异常处理

### 验证深度框架

| 风险等级 | 失败成本 | 检测难度 | 影响范围 | 验证深度 |
|---------|---------|---------|---------|---------|
| 低风险 | 可逆 | 显性 | 局部 | 基本验证（编译/测试） |
| 中风险 | 部分可逆 | 中等 | 多个系统 | 标准验证 + 人工审查 |
| 高风险 | 不可逆 | 隐性 | 全局 | 深度验证 + 多层检查 + 事后审计 |

### Harness-Bench 测试结果

- 配置级差异导致 23.8 分的性能差距
- 可观测性是关键因素
- 简单循环 + 良好提示可能就够了（Simon Willison 视角）
