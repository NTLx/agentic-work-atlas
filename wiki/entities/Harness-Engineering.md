---
type: entity
title: Harness Engineering
aliases:
  - Harness Engineering
  - Agent Harness Engineering
definition: "工程团队的首要工作不再是编写代码，而是构建让 AI Agent 能有效工作的系统——设计 SOP、测试基础设施、集成系统、分诊系统，使 Agent 可检查、可验证、可修改。Addy Osmani (2026) 强调：**Agent = Model + Harness**，失效通常不是模型问题，而是配置（Harness）问题。"
created: 2026-04-16
updated: 2026-09-05
tags:
  - AI-Agent
  - Software-Engineering
  - Development-Paradigm
evidence_level: high
claim_type: mixed
related_entities:
  - '[[Agent-Harness]]'
  - '[[Agentic-Engineering]]'
  - '[[Vibe-Coding]]'
  - '[[Context-Engineering]]'
  - '[[Machine-Readable-Processes]]'
  - '[[Decision-Quality]]'
  - '[[Taste]]'
  - '[[Conceptual-Model]]'
  - '[[MCP-Registry]]'
  - '[[Deterministic-Retrieval]]'
  - '[[HaaS-Harness-as-a-Service]]'
  - '[[Agent-Legibility]]'
  - '[[AI-Capability-Management-Alignment]]'
  - '[[Mechanical-Sympathy-for-LLMs]]'
  - '[[Agent-Unit-of-Work]]'
  - '[[Self-Hosted-Models]]'
source_raw:
  - '[[20260713-microsoft-ships-ai-agents-enterprise-scale]]'
  - '[[20260713-martin-fowler-fragments-july-2026]]'
  - '[[20260413-why-ai-first-strategy-wrong]]'
  - '[[20260611-openai-harness-engineering]]'
  - '[[The Anatomy of an Agent Harness]]'
  - '[[What Is Code?]]'
  - '[[Building an MCP Ecosystem at Pinterest]]'
  - '[[20260419-agent-harness-engineering]]'
  - '[[20260608-paving-the-way-for-agents-in-biology]]'
  - '[[AI用得好不好，跟你会不会管人，我觉得越来越是同一件事。]]'
  - '[[20260702-anthropic-harnesses-long-running-agents]]'
  - '[[20260706-martin-fowler-fragments]]'
  - '[[20260727-github-harness-is-all-you-need]]'
  - '[[20260728-fowler-orchestrator-tax]]'
  - '[[20260613-NLAH-natural-language-agent-harnesses]]'
  - '[[20260623-ibm-cuga-agent-harness]]'
  - '[[20260702-qwen-agent-harness-practice]]'
  - '[[20260902-google-harness-engineering]]'
  - '[[20260902-google-ai-agents-challenge-patterns]]'
---

# Harness Engineering（驾驭工程）

> [!definition] 定义
> **Harness Engineering** 是工程团队的首要工作不再是编写代码，而是构建让 AI Agent 能有效工作的系统——设计 SOP、测试基础设施、集成系统、分诊系统，使 Agent 可检查、可验证、可修改。Addy Osmani (2026) 强调：**Agent = Model + Harness**，失效通常不是模型问题，而是配置（Harness）问题。

## 核心实践案例

### Pinterest：治理型驾驭（MCP Registry）
[[Pinterest-Engineering]] 通过构建 **[[MCP-Registry|MCP 注册表]]**，为 Agent 建立了一套准入和鉴权机制。这是一种典型的治理型驾驭：它规定了哪些工具是“受信任的”，并根据用户权限动态调整 Agent 的能力范围，从而在保证生产力的同时控制了 AI 的“爆炸半径（Blast Radius）”。

### Anthropic：科学驾驭（确定性检索层）
在生物学等高精度领域，Harness Engineering 的重点是构建 **[[Deterministic-Retrieval|确定性检索层]]**。例如 gget-virus 将混乱的 Web 界面操作封装为可靠的编程接口，使 Agent 的检索准确率从 16.9% 提升至 99.7%（Anthropic, 2026）。

### Burke Holland：个体级驾驭（八步工作流）
GitHub 的 Burke Holland（2026-07）展示了 harness 工程的**个体从业者形态**——"the harness is all you need (mostly)"：生产力杠杆不来自安装新工具/skill/prompt，而来自理解 harness 本身。八步工作流全部使用 Copilot 内置功能：选工具（CLI 最接近 harness）→ YOLO 模式 + 沙箱隔离 → 原型先行（20 个 mock 并排比较；非视觉任务也做视觉原型暴露 nuance）→ plan mode 质询（边缘情况显式化；价值不在接受建议而在注入专业判断）→ Autopilot 实现（内置 loop + 自动编排：Explore 小模型读文件 / General Purpose 大模型做复杂动作）→ 人类评审迭代（taste 决定质量）→ rubber duck 跨模型评审（异构模型盲点互补，见 [[Agent-Verification]]）→ 提交（会话按主题隔离）。

与 Pinterest/CREAO 的组织级案例互补：前者为团队构建 harness 系统，后者证明"learn the harness once, use it everywhere"——harness 体验正在跨工具收敛（CLI/app/IDE 共享同一核心工作流），个体只需精通工作流本身。

## 2026-09 补充：把可靠性写进所有路径

Google 的实践型解释把 Harness Engineering 收束为三个最低限度动作：明确 sandbox 边界，把构建/测试错误形成 repair loop，以及用可发现的仓库结构替代巨型说明书。Google AI Agents Challenge 的优秀案例进一步显示，降级模型、廉价路由、并行分支和对外 MCP 都必须穿过同一质量门；否则只是产生了多条未统一验证的产品路径。

这补足了“棘轮”原则：真正值得固化的不是更多 prompt，而是可重复的边界、状态、反馈和验收条件。

## 核心原则

### 从代码产出到系统构建

| 传统工程 | Harness Engineering |
|---------|-------------------|
| 工程师编写代码 | 工程师构建让 Agent 写代码的系统 |
| "AI 如何帮助工程师？" | "如何重构一切，让 AI 负责构建？" |
| 人工审查每行代码 | 系统化审查门控 + 人工审查战略风险 |
| 问题 → "再努力一把" | 问题 → "缺少什么能力？如何让 Agent 理解并执行？" |

### 棘轮效应（The Ratchet）
Addy Osmani 指出：Harness Engineering 是一种棘轮式的迭代过程。每当 Agent 犯错，工程师不应仅通过重试解决，而应在 Harness 中增加约束、工具或校验，确保该错误永久性消失。

棘轮不是“规则越多越好”。过度追加约束会使 `AGENTS.md` 膨胀、加剧 context rot，并让系统对新任务僵化。约束应有可观测失败支撑，并定期合并或删除失效规则。

### Harness 是可实验对象，不是胶水堆积

同一模型只改变 Harness，Terminal Bench 2.0 排名可从前 30 提升到前 5，说明 Harness 会实质改变系统能力。[[20260613-NLAH-natural-language-agent-harnesses]] 进一步把 Harness 表示成可执行自然语言并做消融：文件持久化状态稳定增益，多候选搜索和上下文压缩却可能降低表现。正确做法是用任务级评测选择机制，而不是不断累加脚手架。

实现形态也在分化：[[20260623-ibm-cuga-agent-harness]] 把治理策略内置进运行时；[[20260702-qwen-agent-harness-practice]] 则强调 Harness 的短期收益很高，但其中一部分会随基础模型进步而淘汰。Harness 因而必须同时具备可验证性和可替换性。

### 长程任务：把状态移出上下文

长任务中的 context reset、compaction 和 hand-off file 不是模型能力替代品，而是状态治理机制。优先把进度、feature 清单和验证结果写入可检查的外部 artifact；只有在外部状态不足时才增加 prompt 内上下文。

### HaaS (Harness-as-a-Service)
随着 Agent SDK（如 Claude Agent SDK, OpenAI Agents SDK）的成熟，Harness 开始以服务形式交付。开发者不再从零构建循环和工具分发，而是通过配置 HaaS 运行时来快速部署领域 Agent。

### 与 Vibe Coding 的根本区别

Vibe Coding（打开 Cursor，提示直到跑通，提交）只能产出原型。生产系统需要稳定、可靠、安全——你需要一套能在 AI 写代码时保证这些属性的系统。**你构建的是系统，提示词只是消耗品。**

### 两个关键区分

1. **AI-Assisted（AI 辅助）**：把 AI 嫁接到现有流程上，效率提升 10-20%，结构不变
2. **AI-First（AI 优先）**：围绕"AI 是主要构建者"重新设计流程、架构和组织，差距是量级上的

## 实践框架（CREAO 案例）

### 架构决策：Monorepo 统一

碎片化代码库对 Agent 不可见——Agent 看不到全貌，无法推理跨服务影响，无法运行集成测试。统一代码库使 Agent 可检查、可验证、可修改。

> 碎片化的代码库对 Agent 来说是不可见的，统一的代码库才是可读的。

### 自愈反馈循环

```
检测（CloudWatch/Sentry）→ 分诊（AI 聚类+评分）→ 工单（Linear 自动创建）
    → 修复（工程师验证+推送）→ 审查（3轮 Claude AI 审查）
    → CI/CD（6 阶段流水线）→ 验证（分诊引擎重检）→ 自动关闭工单
```

每个工具处理一个阶段，没有工具试图包揽一切。

### 工程组织：两种角色

| 角色 | 人数 | 职责 | 核心能力 |
|------|------|------|---------|
| **架构师** | 1-2 人 | 设计 SOP、构建测试/集成/分诊系统、定义"优秀"标准 | 批判性思维：批评 AI 而非跟随它 |
| **执行者** | 其他人 | Bug 调查、UI 优化、PR 审查、验证确认 | 技能和专注力，不需要架构推理 |

### 关键洞察：谁适应最快

初级工程师比高级工程师适应更快——工具放大了他们的影响力，且没有十年积累的习惯需要抛弃。适应能力比积累的技能更重要。

## 超越工程：全职能 AI 原生

如果工程以 Agent 速度运行，但其他职能以人类速度运行，那个人类速度的职能就会制约整体。AI-First 必须推进到每个职能：产品发布说明、功能视频、社交内容、健康报告——全部 AI 生成。

## 管理能力层级视角

[[Digital-Life-Kazke|数字生命卡兹克]]（2026）从管理学角度提出：Harness Engineering 对应**策略层目标**的管理范式——给 AI 目标和约束，而非逐步指令。这一范式位于 Prompt Engineering（执行层）和自主 Agent（愿景层）之间，适用于"高级员工"级别的模型。管理方式与模型能力的错配是 AI 使用效果差的核心原因（详见 [[AI-Capability-Management-Alignment]]）。

## 术语演化速度（2026-07 补充）

Martin Fowler 在 FOSE 退修会系列中观察到：2026 年 2 月 Utah 场次上 **Harness Engineering 还不是一个术语**，到 2026 年 7 月 Engelberg（欧洲场）已成为热议话题。5 个月从"不存在"到"主流讨论"——这个演化速度本身就是信号，说明该概念命名了一个已经广泛存在但尚未被命名的实践。

同时观察到一个翻转：Utah 场次上人们还在想方设法激励大家使用 AI，Engelberg 场次上已在担忧 token 成本。

### 从"是什么"到"怎么做"（2026-07 Thoughtworks Retreat）

Engelberg 场次的 Harness Engineering session 焦点已从概念定义转向具体实践：
- **Guide 侧**（context 管理）：将 `agents.md` 限制在 200 行以内，管理模型注意力焦点而非堆砌上下文
- **Sensor 侧**（computational sensors）：向强类型语言（如 Rust）迁移、使用 property-based testing 和形式化方法。与会者的务实态度："I'm not smart enough to write specifications in a formal specification language, but I'm smart enough to read it and check it makes sense for my domain."

Fowler 的判断：对 harness 的关注是否会被模型改进淘汰？"attention to harnesses pays off. We find it reduces token usage, and also allows weaker models to be useful."

## 关键数据点

- OpenAI 于 2026 年 2 月提出 Harness Engineering 概念
- CREAO：25 人公司，10 名工程师，99% 生产代码由 AI 编写
- 14 天内平均每天 3-8 次生产部署（旧模式两周可能零发布）
- 功能从构想到上线可在当天完成，A/B 测试实时验证
- 用户参与度上升、付费转化率上升（非以质量换速度）
- 每个自动化工单包含：样本日志、受影响用户、受影响端点、调查路径
- Anthropic 研究显示：引入确定性检索层 gget-virus 后，Agent 在生物数据检索上的准确率从 16.9% 提升至 99.7%
- CTO 管理时间从 60% 降到 10% 以下

## 前提与局限性

- **前提**：Agent 具备 Code Execution 能力（无此能力则 Harness 无意义）
- **前提**：模型能力是驱动一切的时钟——Opus 4.5 做不到 Opus 4.6 能做的事
- **局限**：单人案例（CREAO 25 人），未经验证在大型组织中的可扩展性
- **局限**：转型代价真实——员工不确定感、CTO 每天 18 小时、高级工程师质疑自身价值
- **局限**：文章作者利益相关——CREAO 是 Agent 平台，用自家 Agent 重建自家平台
- **风险**：6 阶段部署流水线的确定性依赖 CI 覆盖率——未覆盖的边界仍是盲区
- **风险**：Harness 优化可能只适配特定模型或 benchmark；模型跃升后，旧脚手架可能成为技术债

## 关联概念

- [[Agent-Harness]] - Harness 的技术架构层：12 个组件 + 7 个架构决策的完整框架
- [[Agentic-Engineering]] - Harness Engineering 是 Agentic Engineering 的进一步发展：从"使用 Agent 辅助开发"到"围绕 Agent 重建整个工程系统"
- [[Vibe-Coding]] - Harness Engineering 的反面：未经审查的原型 vs 系统化保障的生产代码
- [[Context-Engineering]] - Harness 的信息架构层：设计 Agent 每次推理看到的完整信息结构
- [[Machine-Readable-Processes]] - Harness Engineering 的流程层：让流程可被 Agent 理解和执行
- [[Decision-Quality]] - 架构师角色的核心能力：从代码产出转向决策质量
- [[Taste]] - 架构师需要的产品感知：在用户开口前知道 UI 不对
- [[Deterministic-Retrieval]] - 针对特定领域（如科学、医疗）的 Harness 关键感知层
- [[HaaS-Harness-as-a-Service]] - Harness 工程的交付范式转向
- [[Mechanical-Sympathy-for-LLMs]] - 对 LLM 工作机制的经验性理解，是构建精准 Harness 的认知前提
- [[Orchestrators-Tax]] - 第四种 harness：编排过程本身（前馈规则 + 反馈自评 + 人类掌舵更新 = 棘轮效应的微观实例）

## 来源

- [[20260413-why-ai-first-strategy-wrong]] - Peter Pang (CREAO CTO), 2026-04-13
- [[20260419-agent-harness-engineering]] - Addy Osmani, 2026-04-19
- [[20260608-paving-the-way-for-agents-in-biology]] - Anthropic, 2026-06-08
- [[AI用得好不好，跟你会不会管人，我觉得越来越是同一件事。]] - 数字生命卡兹克, 2026-06-22
- [[20260727-github-harness-is-all-you-need]] - Burke Holland (GitHub), 2026-07-27
