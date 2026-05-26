---
type: output
title: "Raw 全量重编译台账（2026-05-23）"
created: 2026-05-23
updated: 2026-05-23
tags:
  - output
  - audit
  - knowledge-compilation
---

# Raw 全量重编译台账（2026-05-23）

> [!summary] 核心判断
> 本次重编译的目标不是给 raw 追加更多摘要，而是逐篇确认 raw 是否进入了稳定 wiki 层：是否有 entity 承载概念、topic 承载机制、comparison 承载边界，并对承载过薄的主题页做回填加厚。

## 处理口径

- raw 仍作为证据源，不在本轮重写原文。
- 已有 `## 编译摘要` 只作为线索，不视为最终编译结果。
- 成功标准是未来回答问题时能优先读 wiki，而不是重新读 raw。
- 如来源本身只是岗位页、短帖或低密度材料，但能补强一手证据，则保留为证据，不强行抽象新 entity。

## 逐篇处理结果

| Raw | 重新编译后的核心贡献 | Wiki 承载页 | 本轮处理 |
|-----|----------------------|-------------|----------|
| [[(14) Jevons Paradox for Knowledge Work]] | 效率提升会扩大知识工作需求，瓶颈转向分配和管理 | [[AI-Era-Economy-Shift]], [[AI-Labor-Bottleneck-Shift]] | 已承载，保留为经济转型证据 |
| [[20260127-claude-coding-notes]] | Agentic Coding 的相变、tenacity、概念性错误和声明式调度 | [[AI-Era-Career-Skills]], [[Karpathy-AI-Thought]] | 本轮补强职业技能页 |
| [[20260409-ai-capability-gap-ai-psychosis]] | AI 能力鸿沟来自 coding agent 场景的局部跃迁 | [[Karpathy-AI-Thought]], [[AI-Capability-Gap]], [[AI-Psychosis]] | 已承载 |
| [[20260410-anti-patterns]] | Agent PR 的反模式：未经审查、无法运行、证据不足 | [[Agentic-Engineering-Patterns]], [[Agent-PR-Review]] | 本轮补强 Agentic Engineering 的证据负担 |
| [[20260410-better-code]] | AI 应用于持续改善代码质量，而非放大技术债 | [[Agentic-Engineering-Patterns]], [[Technical-Debt-Avoidance]] | 已承载 |
| [[20260410-code-is-cheap]] | 代码生成便宜，但好代码仍由验证、简洁和正确问题定义决定 | [[Agentic-Engineering-Patterns]], [[AI-Labor-Bottleneck-Shift]] | 已承载 |
| [[20260410-hoard-things-you-know]] | 可运行示例和个人知识资产成为 coding agent 的高杠杆输入 | [[Agentic-Engineering-Patterns]], [[Agent-Knowledge-Management]] | 已承载 |
| [[20260413-llm-wiki]] | Raw → Wiki → Schema 的知识编译范式 | [[Agent-Knowledge-Management]], [[RAG-vs-LLM-Wiki]], [[LLM-Wiki]] | 本轮补强知识管理页 |
| [[20260413-why-ai-first-strategy-wrong]] | AI-first 是围绕 Agent 重建流程和 harness，而非把 AI 接进旧流程 | [[Agentic-Engineering-Patterns]], [[Organization-as-Agent-Harness]] | 已承载 |
| [[20260414-cybersecurity-proof-of-work]] | 安全硬化变成 token 预算和验证流水线竞争 | [[Verifiable-Agent-Engineering]], [[Cybersecurity-Proof-of-Work]] | 已承载 |
| [[20260414-martin-fowler-fragments]] | AI 需要懒惰、YAGNI 和克制，不能把所有摩擦都转成生成 | [[Agentic-Engineering-Patterns]], [[AI-Restraint]] | 已承载 |
| [[20260420-build-first-business-ontology]] | 本体构建把业务规则变成 Agent 可读语义层 | [[Enterprise-Ontology-Application]], [[Code-as-Conceptual-Infrastructure]] | 本轮补强本体 topic |
| [[20260420-ontology-enterprise-ai-agent]] | 企业级 Agent 需要本体解决语义不一致、幻觉和不可解释 | [[Enterprise-Ontology-Application]] | 本轮补强本体 topic |
| [[20260420-ontology-meets-agent-case-study]] | 本体 + 推理机让业务规则分类可解释、可追溯 | [[Enterprise-Ontology-Application]] | 本轮补强本体 topic |
| [[20260502-most-companies-arent-ready-for-ai]] | AI-ready 的前提是组织能描述自身目标、流程和责任 | [[Organization-as-Agent-Harness]], [[Agent-First-Process-Redesign]] | 本轮补强流程重构页 |
| [[A Day in the Life of a Palantir Forward Deployed Software Engineer]] | Palantir FDSE 是“为一个客户启用很多能力”的现场平台化角色 | [[Forward-Deployed-AI-Enablement]], [[Forward-Deployed-Engineer]] | 已承载 |
| [[AI and the Future of Cybersecurity Why Openness Matters]] | 安全 Agent 需要开放脚手架、可审计日志和人类可见性 | [[Verifiable-Agent-Engineering]], [[Cybersecurity-Openness]] | 已承载 |
| [[Agent pull requests are everywhere. Here's how to review them.]] | Agent PR 审查重点是设计意图、测试、边界和可维护性 | [[Agentic-Engineering-Patterns]], [[Verifiable-Agent-Engineering]] | 本轮补强 Agentic Engineering |
| [[Andrej Karpathy: From Vibe Coding to Agentic Engineering]] | Software 3.0、Vibe Coding、Agentic Engineering 和可验证性主线 | [[Karpathy-AI-Thought]], [[Agentic-Engineering-Patterns]] | 已承载 |
| [[Anthropic's Boris Cherny: Why Coding Is Solved, and What Comes Next]] | 编程能力商品化后，产品 overhang、loops 和跨学科能力上升 | [[Claude-Code-Automation]], [[AI-Native-Product-Operating-System]] | 已承载 |
| [[Building a general-purpose accessibility agent—and what we learned in the process]] | 生产 Agent 必须识别高风险模式并知道何时拒绝 | [[Verifiable-Agent-Engineering]], [[Accessibility-Agent]] | 已承载 |
| [[Building an MCP Ecosystem at Pinterest]] | MCP registry 把工具调用从个人效率变成组织治理 | [[Organization-as-Agent-Harness]], [[Model-Context-Protocol-MCP]] | 已承载 |
| [[Demis Hassabis: Agents, AGI & The Next Big Scientific Breakthrough]] | 长期记忆、世界模型、工具架构和科学发现 AI 的边界 | [[Agent-Knowledge-Management]], [[Scientific-Discovery-AI]] | 本轮补强知识管理页 |
| [[Enabling agent-first process redesign]] | Agent-first 要求人类治理、Agent 执行、机器可读流程 | [[Agent-First-Process-Redesign]] | 本轮重写加厚 |
| [[Forward Deployed Engineer (FDE) - NYC]] | OpenAI 官方岗位页提供 FDE 职责、协作范围和成功标准证据 | [[Forward-Deployed-Engineer]], [[AI-Era-Career-Skills]] | 保留为一手岗位证据 |
| [[Forward Deployed Engineer：AI 时代的新宠岗位，到底干什么？]] | 中文语境中的 FDE 职业解释和行业转向信号 | [[Forward-Deployed-AI-Enablement]], [[Forward-Deployed-Engineer]] | 已承载 |
| [[Forward deployed engineering at OpenAI]] | OpenAI FDE 位于客户交付与平台开发交叉点 | [[Forward-Deployed-Engineer]], [[Forward-Deployed-AI-Enablement]] | 已承载 |
| [[Good Taste the Only Real Moat Left]] | AI 让合格输出廉价后，品味和判断力成为控制能力 | [[AI-Era-Taste-and-Judgment]], [[Taste]] | 本轮补强品味页 |
| [[How Anthropic’s product team moves faster than anyone else - Cat Wu (Head of Product, Claude Code)]] | Research Preview、evergreen launch room、PM 角色重构 | [[AI-Native-Product-Operating-System]], [[AI-Native-Shipping]] | 已承载 |
| [[How I run multiple USD10K MRR companies on a USD20month tech stack]] | 精益独立开发用低成本、约束驱动和时间护城河抵抗复杂化 | [[Lean-Indie-Engineering]] | 已承载 |
| [[Improving token efficiency in GitHub Agentic Workflows]] | token 成本可观测性是生产 Agent 工作流的一部分 | [[Verifiable-Agent-Engineering]], [[Agentic-Engineering-Patterns]] | 已承载 |
| [[Knowledge Work Is Dying—Here’s What Comes Next]] | 知识工作让位于智慧工作：情感清晰、判断、连接 | [[Wisdom-Work-Evolution]], [[Knowledge-Work-vs-Wisdom-Work]] | 已承载 |
| [[Learning on the Shop floor]] | 公开 Agent 工作现场重建渗透式学习和组织学徒制 | [[AI-Apprenticeship-and-Lehrwerkstatt]], [[Organization-as-Agent-Harness]] | 本轮重写加厚学徒制页 |
| [[MachinaCheck Building a Multi-Agent CNC Manufacturability System on AMD MI300X]] | 领域 Agent 应把确定性解析留给代码，把 LLM 用在制造推理与报告 | [[Verifiable-Agent-Engineering]], [[MachinaCheck]] | 已承载 |
| [[Maintainability sensors for coding agents]] | 质量传感器应覆盖会话内、CI 和周期性结构漂移 | [[Verifiable-Agent-Engineering]], [[Agent-Harness]] | 已承载 |
| [[Management as AI superpower]] | 每个人都要成为 model manager，管理能力从少数角色变成通用技能 | [[AI-Era-Economy-Shift]], [[Allocation-Economy]] | 已承载 |
| [[OncoAgent A Dual-Tier Multi-Agent Framework for Privacy-Preserving Oncology Clinical Decision Support]] | 医疗 Agent 的隐私、纠错 RAG、双层模型和本地硬件主权 | [[Verifiable-Agent-Engineering]], [[Dual-Tier-LLM-Architecture]] | 已承载 |
| [[OpenAI launches the OpenAI Deployment Company to help businesses build around intelligence]] | OpenAI deployment company 说明模型商业化转向现场落地 | [[Forward-Deployed-AI-Enablement]], [[The-OpenAI-Deployment-Company]] | 已承载 |
| [[OpenClaw + 6 个 Agent 运转半个月，从聊天到干活的完整工程实践]] | OpenClaw 的多 Agent、上下文工程和团队协作实践 | [[OpenClaw-Agent-System]] | 已承载 |
| [[OpenClaw + CodexClaudeCode Agent Swarm The One-Person Dev Team Full Setup]] | 一人多 Agent 开发团队的 worktree、handoff 和上下文配置 | [[OpenClaw-Agent-System]], [[Agent-Swarm]] | 已承载 |
| [[Taste for Makers]] | Paul Graham 的品味理论为 AI 时代判断力提供底层标准 | [[AI-Era-Taste-and-Judgment]], [[Taste-vs-Judgment]] | 本轮补强品味页 |
| [[The Always-On Economy AI and the Next 5-7 Years]] | AI 把服务时间从人类作息迁移到连续运行 | [[AI-Era-Economy-Shift]], [[AI-Labor-Bottleneck-Shift]] | 已承载 |
| [[The Anatomy of an Agent Harness]] | Agent Harness 的 12 组件、7 架构决策和脚手架隐喻 | [[Agent-Harness]], [[Building-Effective-Agents]] | 本轮补强 Building Effective Agents |
| [[The Conscious 1% Leading a new renaissance in the era of AI]] | 生产力过剩后，内在掌控、决策质量和共鸣变稀缺 | [[Conscious-Creation-in-AI-Era]], [[AI-Era-Taste-and-Judgment]] | 已承载 |
| [[The Knowledge Economy Is Over. Welcome to the Allocation Economy.]] | 价值从知识本身转向工作分配、质量评估和改进循环 | [[AI-Era-Economy-Shift]], [[Allocation-Economy]] | 已承载 |
| [[The PR you would have opened yourself]] | Agent 辅助贡献需要比普通 PR 更多证据，而不是更少 | [[Agentic-Engineering-Patterns]], [[Agent-Generated-PRs]] | 本轮补强 Agentic Engineering |
| [[The Return of the Deployment Company]] | 部署公司复兴揭示 eval、隐性知识锁定和分层 AI sourcing | [[Forward-Deployed-AI-Enablement]], [[Evaluation-Set]] | 已承载；raw 不追加旧式摘要 |
| [[The layoffs will continue till we learn to use AI]] | 代码便宜后，瓶颈转向 alignment tax、结果度量和组织分工 | [[AI-Labor-Bottleneck-Shift]], [[Organization-as-Agent-Harness]] | 本轮补强流程重构页 |
| [[The next biggest moat in AI]] | 组织形态、权力结构和人才配置比表面产品更难复制 | [[Organization-as-Agent-Harness]], [[Organizational-Shape-Moat]] | 已承载 |
| [[The-Founders-Playbook-05062026_v3]] | AI-native startup 需要从问题验证到 PMF 的纪律，而非只靠 Agent 构建 | [[AI-Native-Product-Operating-System]], [[AI-Native-Startup]] | 已承载 |
| [[Using Git with coding agents - Agentic Engineering Patterns]] | Coding agent 必须掌握 Git 历史、分支和回滚叙事 | [[Git-with-Coding-Agents]], [[Agentic-Engineering-Patterns]] | 已承载 |
| [[Validating agentic behavior when “correct” isn’t deterministic]] | Dominator analysis 从非确定性 trace 中提取必经状态 | [[Verifiable-Agent-Engineering]], [[Building-Effective-Agents]] | 本轮补强 Building Effective Agents |
| [[What Is Code?]] | 代码是概念模型和共享词汇，不只是机器指令 | [[Code-as-Conceptual-Infrastructure]], [[AI-Apprenticeship-and-Lehrwerkstatt]] | 本轮补强学徒制页 |
| [[What is agentic engineering? - Agentic Engineering Patterns]] | Agentic Engineering 的基础定义：工具循环、代码执行和 Vibe Coding 边界 | [[Agentic-Engineering-Patterns]], [[Vibe-Coding-vs-Software-2.0]] | 已承载 |
| [[Why I Don’t Vibe Code]] | 摩擦、本质复杂性和 ownership 是不能外包给 LLM 的工程判断 | [[Code-as-Conceptual-Infrastructure]], [[AI-Era-Taste-and-Judgment]] | 本轮补强品味页 |
| [[building-effective-agents-complete]] | Anthropic 的 workflow/agent 区分和 ACI 设计原则 | [[Building-Effective-Agents]] | 本轮重写加厚 |
| [[一篇文章卖了20万，开源CC+Obsidian打造的LLM Wiki 内容创作3.0系统]] | 从 runtime RAG 到 compile-time Wiki 的内容系统转型 | [[Agent-Knowledge-Management]], [[RAG-vs-LLM-Wiki]] | 本轮补强知识管理页 |
| [[工程师抗拒被"蒸馏"，企业的Skills从何而来？五大招破局]] | Skills 蒸馏的激励困境和对抗性蒸馏风险 | [[Organization-as-Agent-Harness]], [[AI-Apprenticeship-and-Lehrwerkstatt]], [[AI-Era-Career-Skills]] | 本轮补强学徒制与职业技能页 |
| [[当我们谈论 FDE 时，我们在谈论什么？]] | 真正 FDE 的四要素：平台、现场、产品发现、回流 | [[Forward-Deployed-AI-Enablement]], [[Forward-Deployed-Engineer]] | 已承载；raw 不追加旧式摘要 |
| [[深度解析LLM Wiki  Obsidian-Wiki  GBrain：Agent时代知识的“自组织”与“自进化”]] | LLM Wiki、Obsidian-Wiki、GBrain 和 progressive disclosure 的工程化比较 | [[Agent-Knowledge-Management]], [[RAG-vs-LLM-Wiki]] | 本轮补强知识管理页 |
| [[用Agent评测思路管理AI Coding —— 31万行代码AI重构的实践]] | 先人人对齐，再人机对齐；技术债可通过需求迭代渐进式消化 | [[Verifiable-Agent-Engineering]], [[AI-Era-Career-Skills]] | 已承载 |

## 本轮结构性发现

1. **覆盖率没问题，深度不均匀**：lint 基线显示 61 篇 raw 全部已被 wiki 引用，但部分 topic 只是列概念，没有解释生成机制。
2. **raw 摘要不是质量保证**：58 篇 raw 有旧式 `## 编译摘要`，3 篇没有；但本库新规范要求分析进入 wiki 层，所以没有必要为那 3 篇 raw 追加摘要。
3. **薄弱处主要在 topic 层**：entity 数量已经足够多，继续新增 entity 容易碎片化；更高价值动作是加厚 topic 的跨文章整合。
4. **FDE、Agent 工程、知识编译是当前三条主轴**：多数 raw 可以回到这三条主轴，说明知识库主题边界相对稳定。

## 本轮实际回填

- 加厚 [[Agent-First-Process-Redesign]]：从单篇流程自动化文章扩展为 AI-ready、alignment tax 与 FDE 的流程重构机制。
- 加厚 [[AI-Apprenticeship-and-Lehrwerkstatt]]：把公开协作、渗透学习、Skills 激励和通用语言合并为组织学习机制。
- 加厚 [[Agent-Knowledge-Management]]：补上 compile-time 知识层、四动作模型和质量门。
- 加厚 [[Building-Effective-Agents]]：把 Anthropic 模式与 Agent Harness、可验证工程连接。
- 加厚 [[AI-Era-Taste-and-Judgment]]：补上工程语境中的本质复杂性、摩擦和拒绝清单。
- 加厚 [[AI-Era-Career-Skills]]：补上 Skills 蒸馏、公开协作和职业技能外显化。
- 加厚 [[Enterprise-Ontology-Application]]：把本体明确放入企业级概念基础设施和 Agent 分工。
- 加厚 [[Agentic-Engineering-Patterns]]：补上 Agent PR 的证据负担。

## 本文使用的 Wiki 页面

- [[Agentic-Engineering-Patterns]]
- [[Verifiable-Agent-Engineering]]
- [[Forward-Deployed-AI-Enablement]]
- [[Organization-as-Agent-Harness]]
- [[Agent-Knowledge-Management]]
- [[Code-as-Conceptual-Infrastructure]]
- [[AI-Era-Taste-and-Judgment]]
- [[AI-Labor-Bottleneck-Shift]]
- [[AI-Native-Product-Operating-System]]
- [[AI-Apprenticeship-and-Lehrwerkstatt]]
- [[Agent-First-Process-Redesign]]
- [[Building-Effective-Agents]]

## 回填检查

| 新判断 | 支撑依据 | 处理 |
|--------|----------|------|
| “已编译”不等于“编译深入”，覆盖率和结构深度要分开看 | 本轮 raw→wiki 覆盖审计；Wiki: [[Agent-Knowledge-Management]] | 升级为本 output 的审计结论，不新增 entity |
| 全库当前更需要加厚 topic，而不是继续新增 entity | 本轮 182 个 entity、22 个 topic 的结构审计；Wiki: [[LLM-Wiki]] | 保留，作为后续维护策略 |
| 公开 Agent 协作是组织学徒制的必要条件 | Raw: [[Learning on the Shop floor]]；Wiki: [[AI-Apprenticeship-and-Lehrwerkstatt]] | 已升级到 topic |
| Agent PR 的生成成本下降必须伴随证据标准上升 | Raw: [[Agent pull requests are everywhere. Here's how to review them.]], [[The PR you would have opened yourself]] | 已回填到 [[Agentic-Engineering-Patterns]] |
| 本体是企业级概念基础设施 | Raw: [[20260420-build-first-business-ontology]], [[What Is Code?]]；Wiki: [[Code-as-Conceptual-Infrastructure]] | 已回填到 [[Enterprise-Ontology-Application]] |
