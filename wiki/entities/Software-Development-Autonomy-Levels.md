---
type: entity
title: Software Development Autonomy Levels
aliases:
  - Software Development Autonomy Levels
  - 软件开发自治分级
  - 三级自治框架
definition: "Berkeley RDI 等（2026-07）类比 SAE 自动驾驶分级提出的软件开发自治分类法：按 SDLC 哪些阶段的责任从人类转移到 AI，分为 Level I 代码自治 / Level II 流水线自治 / Level III 需求自治，使能力主张、部署选择与问责归属变得可读"
created: 2026-07-28
updated: 2026-07-28
evidence_level: medium
claim_type: mixed
tags:
  - agentic-engineering
  - verification
related_entities:
  - "[[AI-Autonomy]]"
  - "[[Agent-Verification]]"
  - "[[Reward-Hacking]]"
  - "[[Agentic-Engineering]]"
  - "[[Context-Engineering]]"
  - "[[Task-Horizon]]"
  - "[[Shared-Memory-Contamination]]"
source_raw:
  - "[[20260726-berkeley-auto-software-dev]]"
  - "[[20260708-towards-autonomous-software-dev.pdf]]"
---

# Software Development Autonomy Levels（软件开发自治分级）

> [!definition] 定义
> 类比 SAE 自动驾驶分级（L0-L5）的软件开发自治分类法：按软件开发生命周期（SDLC）中**哪些阶段的责任已从人类转移到 AI 完全控制**，划分为三级。分级的目的不是预测，而是让能力主张、部署选择和问责归属变得可读（legible）——"autonomous coding agent" 一词可以指建议几行代码的工具，也可以指决定建什么功能的系统，这些是失败模式完全不同的东西，需要不同的词汇。

## 三级定义

| 级别 | 名称 | AI 拥有 | 人类保留 |
|------|------|---------|---------|
| **Level I** | Code Autonomy（代码自治） | 系统设计 + 实现，产出完整 PR（含设计理由、代码、文档） | 决定建什么、PR 粒度审查、测试与安全审计监督、部署门控 |
| **Level II** | Pipeline Autonomy（流水线自治） | 设计 → 实现 → 测试 → 审计 → 部署全流程 | 陈述高层需求、评估结果行为（不写也不审代码） |
| **Level III** | Demand Autonomy（需求自治） | 从遥测/用户行为/安全通告/依赖变化中识别需求，决定建什么 | founding mission（系统创立时设定的使命） |

**Level II 是质变点**，依赖两个前提：① 人类意图可被充分完整的规格捕获；② 无人检查中间产物时自动验证可信。**两个前提当前在规模化下均不成立**。高保障领域可能长期停留在 Level I 或以下，内部工具与一次性应用可能更快接近 Level II——不同领域以不同节奏推进。

## 三个横切维度

级别只回答"AI 拥有哪些阶段"，同级别系统行为仍可完全不同，取决于三个正交维度：

- **规格粒度（Specification granularity）**: 带复现测试的详细 bug 报告约束 agent；"加上多租户"迫使它自行推断范围、架构、权衡与成功标准。弱规格会把名义低级别系统推向高级别的挑战
- **时间自治（Temporal autonomy）**: ticket 级 / sprint 级 / release 级 / 跨月跨年的连续运行。长时间跨度引入记忆、溯源、回归和架构连贯问题——一次性 benchmark 无法捕获
- **监督模式（Oversight mode）**: 从共同规格制定、动作级审批、PR 审查、策略护栏，到仅监视与自动回滚。合适模式取决于领域风险与可逆性

## 统一问题：保存人类意图

三级共享一个以不同形态出现的挑战——**直接人类控制退场时，保存并忠实执行人类意图**：Level I 意图可经审查恢复；Level II 意图须编码进无人端到端验证的规格；Level III 由 AI 自己合成并维护规格。四个看似分离的失败是同一问题的表达：

- **Specification drift**: 实现逐渐偏离人们想要的东西
- **[[Reward-Hacking|Reward hacking]]**: 满足可测代理指标，违反底层目标
- **Multi-agent disagreement**: 不同 agent 基于互不相容的解释行动，且不暴露冲突
- **自一致性陷阱（CORE RISK）**: 写实现的 agent 同时写测试时，**通过测试只证明一致性，不证明正确性**

> [!important] 保障对象的转移
> 验证软件产物不再足够，还必须审计产出产物的 agent：其规格、技能、记忆、决策溯源、通信协议与执行轨迹。信任生产过程与信任生产物同等重要。

## Level-Skipping：最现实的风险

最紧迫的风险不是奇异的全自治系统，而是**组织跳级**：名义运行 Level I（人类对审查和部署负全责），实践中却合入无人真正检查的 agent 变更——采用 Level II 实践而没有 Level II 的验证、治理与问责。对策是**显式 level gating**：系统只有在当前级别的挑战已被可证明地解决后才应升级；证明负担随自治度、时长和风险上升。

## 关键数据点

- 能力两端并存的证据：16 个并行 Claude agent 以低于 `$20K` 造出可用 C 编译器；但测试持续演化（非孤立任务）的 benchmark 上前沿 agent 急剧退化——能加功能，无法跨连续变更保持正确性与架构连贯
- 六大结构性转变（position paper 预测）：软件生成化（规格成主产物 / 抽象边界可渗透 / 软件动态化）→ 工程 agent 中心化（保障从产物到 agent / 多 agent 协调超越人类组织形态）→ 生态重构（团队缩小 + 治理密集化 / 独立审计认证机构成新基础设施）
- 最具体研究呼吁：建设仓库级规格合成 benchmark 与"规格-实现漂移"的长时程评估——没有它们，Level II/III 就绪声明无法被证实
- 终局判断："Software becomes abundant; trust becomes scarce."

## 完整版论文增补（07-28）

完整 position paper（[[20260708-towards-autonomous-software-dev.pdf]]，38 页，131 篇参考文献）在四处增量上论证了本框架：

**适用边界**：三级框架针对长生命周期、持续维护的软件（主系统、服务、SaaS）。当今 AI 所写代码的很大部分是单次使用（抛弃脚本、一次性分析），该领域与框架中心关切"基本正交"（长时程规格/维护/问责不适用），但并非无风险——意图错位、幻觉、意外副作用同样致害。

**验证者失败机制**（CORE RISK 深化）：把检查委派给独立 verifier agent 也未必有效，有两个具体机制——**talk past**（verifier 与 generator 互不理解、无法收敛）或 **co-adapt**（共同适应，直到测试仅仅背书实现的 bug）。这解释了为何"跨模型家族盲点互补"只是数据级独立而非目标级独立（详见 [[Agent-Verification]]）。

**实证锚点**：

- **EvoClaw benchmark**：前沿 agent 孤立任务 >80% → 连续演化设定坍缩至至多 38%（能加功能、不能防回归）——[[Task-Horizon]] 作为独立能力维度的硬证据
- **验证能力悬殊**：相同算法任务端到端通过率 Dafny >80% vs Lean 27%；自然语言描述带来的验证提升出奇地小 → 瓶颈在形式推理能力，不在检索/上下文
- **MAST**：战术性修复（更好的 prompt）仅适度改进，失败率仍高于生产阈值——结构性协议重设计才是绑定约束
- **命名新失败模式**：**slopsquatting**（AI 生成内容仿冒）、**toxic-skill propagation**（[[Shared-Memory-Contamination]] 的 skill 层同构）

**制度脚手架已开始成形**：OWASP Top 10 for Agentic Applications、Microsoft Agent Governance Toolkit（开源）、AWS Agentic AI Security Scoping Matrix；监管期限：EU AI Act 高风险义务 2026-08、Colorado AI Act 2026-06。责任归属立场：agent 构建的应用泄露数据，责任归部署组织而非模型提供商——这本身是保留人类监督的强激励。

## 前提与局限性

- **框架性质**: position paper 的分类法与研究议程，不是实证结论；十个预测自称"前瞻而非必然"
- **SAE 类比的边界**: SAE 是物理安全单维分级，软件自治是规格/时间/监督三维叠加；把三维压成级别会隐藏同级差异（文章自承）
- **审计者回归问题**: "审计 agent"需要可信审计者，审计者本身也可能是 agent——独立验证要求目标级独立，跨模型家族只是训练数据级独立，这是开放研究问题
- **话语效应**: 分级框架把领域议程导向"如何逐级放行自治"，这一设定本身有利于 agent 厂商（作者机构含 Cursor 与 Microsoft）；但框架的谨慎声明（Level II 前提不成立、level gating）实质提升了可信度

## 关联概念

- [[AI-Autonomy]] — 框架互补：Anthropic 的任务类型自主度量（1-5 量表）测"什么任务被自主完成"，本框架分"SDLC 哪些阶段的责任已转移"
- [[Agent-Verification]] — CORE RISK 与保障对象转移（产物 → agent）的理论来源
- [[Reward-Hacking]] — 意图保存统一问题的四种表达之一
- [[Agentic-Engineering]] — 自治分级是 agentic engineering 成熟度的话语框架
- [[Context-Engineering]] — 预测8：project context 成为比多代代码更长寿的持久资产，需可移植、厂商中立格式

## 来源

- [[20260726-berkeley-auto-software-dev]]（博客摘要版）
- [[20260708-towards-autonomous-software-dev.pdf]]（完整 position paper: Towards Autonomous Software Development）
