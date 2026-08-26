---
type: source-summary
title: "2026：FDE 成为 SaaS 的准入门槛"
canonical_url: "https://magneticgrowth.substack.com/p/2026-the-year-of-the-forward-deployed"
raw_state: index
original_raw_file: "20260825-forward-deployed-table-stakes-saas.md"
original_body_sha256: "993a429da92237c0c5c423e37e177f5470f8ac479dbcf8fcdd4f5d0eaa724489"
indexed_at: "2026-08-26T13:40:00+08:00"
created: 2026-08-25
updated: 2026-08-26
tags:
  - source-summary
  - forward-deployed-engineer
  - fde
  - ai-saas
  - agentic-ai
evidence_level: medium
claim_type: mixed
---
> Raw 生命周期：Substack 原文已降级为可恢复索引；精确引用时从 canonical URL 回到原文章节核验。


# 2026：The Year Forward Deployed Engineering Becomes Table Stakes for SaaS

> Alex Furmansky（Magnetic Growth, 2026-03-03）：AI SaaS 不再是"defined product"，而是"value opportunity"。兑现价值需要定制通用工具适配具体上下文，供应商只能在客户现场完成这件事——FDE 成为结构性必需品而非奢侈品。文章给出供应商为何不能沿用 SaaS playbook、客户为何不知买什么、系统思考为何难，以及 OpenAI/Anthropic 的产业布局数据。来源：行业实践者 Substack。证据等级：medium（实践者一手观察 + 产业数据，vendor/顾问立场需打折）。

## 编译摘要

### 1. 浓缩

- **核心结论1**: AI 打破了 SaaS 公式——"发现楔形产品→同款卖数万客户→80%+ 毛利"不再成立，因为任何单点 AI 功能有抛硬币概率在 6 个月内被通用 agent 超越；供应商被迫用"薄 agentic 平台 + 每客户重定制"回应
  - 关键证据: ChatGPT/Claude/Gemini 每 6 个月大幅移动推理/连接/UX 目标；BabyAGI/OpenClaw 等开源 agent 在 AI Twitter 快速病毒式扩散
  - 关键证据: AI 解决的是传统确定性软件做不到的概率性、判断密集、messy/contextual/"太人性化"的任务——"最大奖赏不是自动化既有工作流，而是发现以前不可能的工作流"
  - 关键证据: 客户期望随聊天 AI 改变——他们想要符合自身特定需求的定制软件，不愿为只用 20% 功能的完整 ERP 头疼
- **核心结论2**: 客户不知道买什么——C-suite 被"随处撒 AI"的压力驱动，但"系统思考"（识别哪些步骤需判断、哪些是机械、映射交接与边界案例）是真正难点，组织无法从内部完成
  - 关键证据: 传统客户发现像"iPhone 前问用户最喜欢的 App"——问题没有干净答案；最珍贵的用例只能*因为*技术而存在，必须在场才能发现
  - 关键证据: 组织的流程知识分散且过期——销售团队 5 人被问相同 lead 处理会给出 5 种不同答案；知识工作规则非确定性（"有时这样做，有时那样做，Jerry 又是另一种做法"）
  - 关键证据: 维持干净流程文档（BPMN/DMN）对多数组织近乎不可行——除非营收以小型国家 GDP 计（引自 SAP Signavio VP Lukas Egger）；FDE 是"必须有人做挖掘工作，因为组织永远不会自己做"
- **核心结论3**: 主要玩家已全面押注：OpenAI Frontier Alliance 与四大咨询结盟、FDE 团队 2025 年 2→52 人、企业占营收 ~40%；Anthropic 大规模扩张 Applied AI
  - 关键证据: OpenAI Frontier Alliance 配对 FDE + BCG/McKinsey/Accenture/Capgemini；FDE 团队 2025 年从 2 人增长到 52 人，嵌入 Morgan Stanley 等客户；企业占 OpenAI 营收约 40%，CFO 预期今年底接近 50%
  - 关键证据: Anthropic 激进扩张 Applied AI 团队——招 FDE、Technical Deployment Leads、Solutions Architects 嵌入战略企业客户，交付 MCP servers、sub-agents、agent skills；团队"据报增长 5x"
  - 关键证据: FDE 岗位发布在 2025 年 1-9 月暴增 800%+（Indeed / Financial Times）
- **核心结论4**: FDE 的核心价值是"旋转跨 engagement 获得的模式识别"——面向市场的动手研究 + 采纳加速同时发生；组织需要自身无法内部生成的市场情报与产品发现
  - 关键证据: FDE 在多个客户间轮转获得的模式识别，是内部团队永远得不到的（企业规模效应在跨组织侧）
  - 关键证据: 个人最佳特质——销售+技术+享受解决不同问题，能 hold C-suite 的焦虑与 skeptical 工程团队之间的空间，有咨询/投行/战略 pedigree，且"能 hold 什么是现在技术上可能的歧义，同时保持对 90 天后可能性的开放"

### 2. 质疑

- **关于立场与激励的质疑**: 作者是 AI 实施服务商（讽刺地复用"forward deployed"标题并末尾招聘）——"SaaS 与 services 界限模糊"恰是其生意所在；稿件是实践者一手观察，不是中立市场分析。FDE 岗位数据（800%、2→52、5x）来自引用，未经独立审计
- **关于"供应商不能 follow SaaS playbook"的边界**: 论点预设 AI 平台能力每 6 个月一变的持续速度快于产品打磨——若模型能力增速放缓、或培育出稳定的平台层（如 MCP/A2A 协议成熟），纯产品 SaaS 可能重新赢回"薄平台+轻定制"；文章未评估这种均衡
- **关于"组织无法从内部完成系统思考"的泛化**: 该结论高度依赖组织现状（小团队、无流程文档、营收未达"小国 GDP"）；对已经投资流程治理的大企业（合规/精算/飞机制造），内部 process 团队可能比 FDE 更懂自己的约束——FDE 必要性不是普遍真理
- **与库内 FDE 框架的校准**: 本文描述的 FDE 是"咨询式技术骨干"（实施+培训），偏轻"产物回流"——它讲清了"为什么现在必须 FDE"，但几乎不谈"如何把一次性部署沉淀为平台能力"；与库内 [[Forward-Deployed-AI-Enablement]] 的四要素（有平台/嵌入现场/产品发现/产物回流）相比，本文偏向前三步，回流层缺位

### 3. 对标

- **与 [[Forward-Deployed-AI-Enablement]] topic 的直接对接**: 本文提供了该 topic 缺失的**产业规模数据**——为什么 2026 是 FDE 临界点（FDE 岗位 +800%、OpenAI Frontier Alliance、Anthropic 5x），是"为什么横向所有主要玩家收敛同一模式"的市场证据
- **与 [[Forward-Deployed-Engineer]] entity 的对接**: 本文给出岗位画像（销售+技术+hold ambiguity+咨询 pedigree），可并入职位定义；它与 Palantir 机制群（[[Decision-Centric-Architecture]] 等）互补——本文讲"为什么需要 FDE"，Palantir 讲"FDE 靠什么机制沉淀能力"
- **与 [[Agent-First-Process-Redesign]] 的关系**: "系统思考"（判断 vs 机械、交接与边界、保持人在环路）正是 Agent-First 流程重构的现场版——FDE 做的"挖流程"工作与 [[20260825-enterprise-ai-workflow-redesign|Workflow Redesign]] 的"映射决策单元"同构
- **跨域类比：FDE ≈ 外科手术中的"现场会诊"**: 不是远程开处方，而是进入手术室看真实组织——医疗里复杂病例需要主刀现场会诊而非远程咨询，与"最珍贵的 AI 用例只能在场发现"同构（跨域联想）
- **模式识别 ≈ 咨询行业的"采样"学习**: FDE 跨客户获得的模式识别，与顶级咨询顾问跨行业积累的"这问题我见过 30 遍"直觉同构；但咨询业最终被质疑"给通用模板"，FDE 是否也会随 AI 实施成熟而从定制滑向模板化——这是该模式的可测试反例（综合判断，见研究 agenda）

### 前提与局限性

- 实践者的单点观察，非系统性研究；市场判断（vendor 无法 follow playbook）含因果推断
- 主要数据（800%、2→52、5x、~40%）来自引用而非一手测量，准确时点 2026 年 3 月，Market 环境快速变化
- "AI SaaS = value opportunity"的界定暗示 vendor 立场；读者需区分"现象描述"（可信）与"行业方向论证"（正被其业务印证）

### 关联概念

- [[Forward-Deployed-AI-Enablement]] — 本文是其产业背景数据，且暴露其"回流层"的实践缺失
- [[Forward-Deployed-Engineer]] — 岗位画像与扩张数据的来源
- [[Agent-First-Process-Redesign]] — "系统思考"是流程重构的现场执行
- [[AI-Deployment-Valley-of-Death]] — 客户"不知买什么"的部署死亡谷侧面
- [[Integration-Wall]] — FDE 存在的理由：穿越集成之墙