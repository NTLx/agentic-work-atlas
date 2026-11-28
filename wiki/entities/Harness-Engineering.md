---
type: entity
title: Harness Engineering
aliases:
  - Harness Engineering
  - Agent Harness Engineering
definition: "设计、维护和评估模型之外的执行环境、上下文、工具、状态、权限与反馈验证机制，使 Agent 在给定任务和风险约束下可靠工作；模型、环境、输入及验收器均可能是失败原因。Agent = Model + Harness 是系统构成的简写，不是因果归因公式。"
created: 2026-04-16
updated: 2026-11-28
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
> **Harness Engineering** 是设计、维护和评估模型之外的执行环境、上下文、工具、状态、权限与反馈验证机制，使 Agent 在给定任务和风险约束下可靠工作；模型、环境、输入及验收器均可能是失败原因。Agent = Model + Harness 是系统构成的简写，不是因果归因公式。

## 核心实践案例

### Pinterest：治理型驾驭（MCP Registry）
[[Pinterest-Engineering]] 通过构建 **[[MCP-Registry|MCP 注册表]]**，为 Agent 建立了一套准入和鉴权机制。这是一种典型的治理型驾驭：它规定了哪些工具是“受信任的”，并根据用户权限动态调整 Agent 的能力范围，从而在保证生产力的同时控制了 AI 的“爆炸半径（Blast Radius）”。

### Anthropic：科学驾驭（确定性检索层）
在生物学等高精度领域，Harness Engineering 的重点是构建 **[[Deterministic-Retrieval|确定性检索层]]**。例如 gget-virus 将混乱的 Web 界面操作封装为可靠的编程接口，在 Anthropic 的 VirBench 实验中，无专用工具的六个系统平均准确率范围为16.9%–91.3%，加入 gget virus 后均超过90%，GPT-5.5峰值为99.7%；端点不是同一模型的配对增益。

### Burke Holland：个体级驾驭（八步工作流）
GitHub 的 Burke Holland（2026-07）展示了 harness 工程的**个体从业者形态**——"the harness is all you need (mostly)"：生产力杠杆不来自安装新工具/skill/prompt，而来自理解 harness 本身。八步工作流全部使用 Copilot 内置功能：选工具（CLI 最接近 harness）→ YOLO 模式 + 沙箱隔离 → 原型先行（20 个 mock 并排比较；非视觉任务也做视觉原型暴露 nuance）→ plan mode 质询（边缘情况显式化；价值不在接受建议而在注入专业判断）→ Autopilot 实现（内置 loop + 自动编排：Explore 小模型读文件 / General Purpose 大模型做复杂动作）→ 人类评审迭代（taste 决定质量）→ rubber duck 跨模型评审（异构模型盲点互补，见 [[Agent-Verification]]）→ 提交（会话按主题隔离）。

与 Pinterest/CREAO 的组织级案例互补：前者为团队构建 harness 系统，后者提出"learn the harness once, use it everywhere"这一经验性建议——harness 体验正在跨工具收敛（CLI/app/IDE 共享同一核心工作流），个体只需精通工作流本身。

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
Addy Osmani 指出：Harness Engineering 是一种棘轮式的迭代过程。每当 Agent 犯错，工程师不应仅通过重试解决，而应在 Harness 中增加约束、工具或校验，针对已识别的失效模式建立可复跑检查并验证收益；不能保证错误永久消失。

棘轮不是“规则越多越好”。过度追加约束会使 `AGENTS.md` 膨胀、加剧 context rot，并让系统对新任务僵化。约束应有可观测失败支撑，并定期合并或删除失效规则。

### Harness 是可实验对象，不是胶水堆积

既有材料报告固定模型修改 Harness 后 benchmark 排名改善；本轮未复验榜单快照、运行预算及候选配置，不保留精确排名作为已核实数据。[[20260613-NLAH-natural-language-agent-harnesses]] 进一步把 Harness 表示成可执行自然语言并做消融：文件持久化状态稳定增益，多候选搜索和上下文压缩却可能降低表现。正确做法是用任务级评测选择机制，而不是不断累加脚手架。

实现形态也在分化：[[20260623-ibm-cuga-agent-harness]] 把治理策略内置进运行时；[[20260702-qwen-agent-harness-practice]] 则强调 Harness 的短期收益很高，但其中一部分会随基础模型进步而淘汰。Harness 因而必须同时具备可验证性和可替换性。

### 长程任务：把状态移出上下文

长任务中的 context reset、compaction 和 hand-off file 不是模型能力替代品，而是状态治理机制。优先把进度、feature 清单和验证结果写入可检查的外部 artifact；只有在外部状态不足时才增加 prompt 内上下文。

### HaaS (Harness-as-a-Service)
随着 Agent SDK（如 Claude Agent SDK, OpenAI Agents SDK）的成熟，Harness 开始以服务形式交付。开发者不再从零构建循环和工具分发，而是通过配置 HaaS 运行时来快速部署领域 Agent。

### 与 Vibe Coding 的根本区别

仅凭直觉提示和未经验证的提交不足以保证生产质量；是否能交付取决于具体实现和验收证据。生产系统需要稳定、可靠、安全——需要能约束、检测并处理相关失效的工程系统；测试通过不等于保证全部属性。**你构建的是系统，提示词只是消耗品。**

### 两个关键区分

1. **AI-Assisted（AI 辅助）**：在既有流程内使用 AI；收益须按实际任务测量
2. **AI-First（AI 优先）**：围绕"AI 是主要构建者"重新设计流程、架构和组织，收益及迁移成本因组织与任务而异

## 实践框架（CREAO 案例）

### 架构决策：Monorepo 统一

CREAO 将代码库集中以改善该团队的跨服务发现和测试体验。多仓库同样可经受控检索、版本契约、集成测试和服务拓扑实现可见性；monorepo 不是必要或充分条件。

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
| **执行者** | 其他人 | Bug 调查、UI 优化、PR 审查、验证确认 | 实现、诊断、验证与必要的架构判断 |

### 关键洞察：谁适应最快

CREAO 作者报告其团队中部分初级工程师适应较快；未进行匹配任务或长期绩效对照。经验、领域判断、学习能力均可能影响效果。

## 超越工程：全职能 AI 原生

若某职能的有效处理能力低于需求，它可能成为瓶颈。是否采用 AI 应按实际等待、质量、风险与成本决定，不要求每个职能全部 AI 生成。

## 管理能力层级视角

[[Digital-Life-Kazke|数字生命卡兹克]]（2026）用人类管理粒度类比AI交互。2026-11-28回读Raw纠正：Fable 5半天是反事实设想，非同任务对照。Prompt、Harness和自主执行可组合，不按固定拟人职级排列；根据任务、权限、风险和结果实测选择，详见 [[AI-Capability-Management-Alignment]]。

## 术语演化速度（2026-07 补充）

Martin Fowler 在 FOSE 退修会系列中观察到：2026 年 2 月 Utah 场次上参与者尚未普遍使用 Harness Engineering 这一术语，到 2026 年 7 月 Engelberg（欧洲场）已成为热议话题。该观察反映特定退修会参与者的关注变化，不证明术语首次出现或全行业普及。

同时观察到一个翻转：Utah 场次上人们还在想方设法激励大家使用 AI，Engelberg 场次上已在担忧 token 成本。

### 从"是什么"到"怎么做"（2026-07 Thoughtworks Retreat）

Engelberg 场次的 Harness Engineering session 焦点已从概念定义转向具体实践：
- **Guide 侧**（context 管理）：一位与会者将 `agents.md` 限制在200行以内（个人配置，非通用规范），管理模型注意力焦点而非堆砌上下文
- **Sensor 侧**（computational sensors）：向强类型语言（如 Rust）迁移、使用 property-based testing 和形式化方法。与会者的务实态度："I'm not smart enough to write specifications in a formal specification language, but I'm smart enough to read it and check it makes sense for my domain."

Fowler 的判断：对 harness 的关注是否会被模型改进淘汰？"attention to harnesses pays off. We find it reduces token usage, and also allows weaker models to be useful."

## 关键数据点

- OpenAI 于2026年2月发布相关工程实践；不据此主张术语首创
- CREAO：25 人公司，10 名工程师，99% 生产代码由 AI 编写
- 14 天内平均每天 3-8 次生产部署（旧模式两周可能零发布）
- 功能从构想到上线可在当天完成，A/B 测试实时验证
- 用户参与度上升、付费转化率上升（非以质量换速度）
- 每个自动化工单包含：样本日志、受影响用户、受影响端点、调查路径
- Anthropic 官网 VirBench（120个查询，40种病原体，人工核实计数）：无专用工具16.9%–91.3%，加入后各系统>90%，GPT-5.5最高99.7%。[原文](https://www.anthropic.com/research/agents-in-biology)（2026-11-28核对正文）；不等同任意生物检索准确率。
- CTO 管理时间从 60% 降到 10% 以下

## 前提与局限性

- **前提**：明确任务、外部接口和可观察的执行/验收边界；代码执行只是可选能力。
- **前提**：模型与环境应共同测量；新模型可能改善或削弱既有配置效果。
- **局限**：CREAO 为单组织自报案例，其组织数字及效果未在本轮重新回溯原文，不作为一般性结论。
- **局限**：转型代价真实——员工不确定感、CTO 每天 18 小时、高级工程师质疑自身价值
- **局限**：文章作者利益相关——CREAO 是 Agent 平台，用自家 Agent 重建自家平台
- **风险**：6 阶段部署流水线的确定性依赖 CI 覆盖率——未覆盖的边界仍是盲区
- **风险**：Harness 优化可能只适配特定模型或 benchmark；模型跃升后，旧脚手架可能成为技术债

## 关联概念

- [[Agent-Harness]] - Harness 的技术架构层：12个组件与7个设计轴的综合分类，并非完整性要求
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
