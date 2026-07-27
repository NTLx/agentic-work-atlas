---
type: source-summary
title: "If AI is so great, why isn't it working?"
source_raw:
  - "[[20260719-if-ai-is-so-great-why-isnt-it-working]]"
created: 2026-07-27
updated: 2026-07-27
tags:
  - source-summary
  - ai-deployment
  - ai-failure
  - agentic-engineering
  - organizational-change
evidence_level: medium
claim_type: mixed
---

# If AI is so great, why isn't it working?

> Varick Agents 创始人 Daniel Kornum 基于与 100+ 美国大企业 C-Suite 的对话，论证 AI 企业部署失败（95%）的瓶颈不在模型而在流程：工程工作因 bounded/checkable/structured/verifiable 四属性独享 AI 红利，其他职能需先做流程审计与确定性分解。来源：公司博客（2026-07-19）。证据等级：medium（一手客户访谈但样本自述、无方法论披露；多机构失败率数据互证较强）。

## 编译摘要

### 1. 浓缩

- **核心结论1**: 模型已不是瓶颈——多机构失败率数据在每一代模型改进中保持恒定（MIT NANDA 5%、BCG 4%、Deloitte 6%、RAND 80%+ 失败），证明失败率与模型能力脱钩
  - 关键证据: BCG/Deloitte/RAND/IBM/Gartner/McKinsey 六家机构方法论各异但收敛于同一数字；同期模型能力大幅提升（GPT-o3 → Opus 4.7/GPT 5.5，价格暴跌，上下文窗口扩大，tool calling 精度提高）
- **核心结论2**: 软件工程独享 AI 红利是因为工程工作具备四个其他企业职能不具备的属性——Bounded（输入输出明确）、Checkable（编译器/测试秒级反馈）、Structured（版本控制与确定性构建）、Verifiable（PR 是离散可评审产物）
  - 关键证据: GitHub 2024: Copilot 用户快 55%；Anthropic 2025-08: 开发者任务时间缩短约 80%；Pichai 2026 初: Google 75% 新代码由 AI 生成并经工程师批准。对比财务结账（AP/AR/跨系统对账）四项属性全无
- **核心结论3**: 成功的 5% 遵循五步模式：审计先行（4+ 周数字孪生映射实际工作流）→ 分解到大部分确定性（85% 代码 + 15% LLM）→ 单一编排层（杀死 agent sprawl）→ 模型无关路由 → 持续演化的基础设施专职团队
  - 关键证据: conformance gap（SOP 与实际工作流的差距）通常 30%+，异常驱动流程超 70%；为文档流程构建 = 自动化 70% 流量 + 在 30% 上崩溃，30% 产生的工作量超过自动化前

### 2. 质疑

- **关于"模型不是瓶颈"的质疑**: 失败率恒定也可能反映"组织消化能力"的恒定而非模型的无关性——每一代模型提升被组织同步扩大的部署野心抵消（Jevons 悖论式动态）。RAND 的"80%+ 失败率是普通 IT 项目两倍"恰说明 AI 项目的额外失败来自 AI 特有的不确定性，而非纯流程问题
- **关于"四属性"框架的质疑**: 框架解释力强但有循环论证风险——"AI 在可验证领域成功"近乎同义反复（AI 需要反馈信号才能学习/对齐，可验证性本身就是反馈信号的存在）。更有生产力的问题不是"哪些工作可验证"，而是"哪些工作的验证成本可以被工程化降低"
- **关于 85/15 比例的质疑**: "生产系统 85% 代码 + 15% LLM"是经验断言，无来源。这个比例随领域和模型能力变化——18 个月前可能是 95/5，下一代模型可能是 70/30。把特定时间点的快照当作架构原则有风险
- **关于作者立场的质疑**: Varick Agents 自身销售 AI 部署服务，文章的结论（"你需要专职团队 + 6 个月部署路径"）恰好是其服务目录。"审计先行"的建议正确但激励结构值得注意——与 [[20260718-ai-mania-eviscerating-decision-making]] 中 Ludicity 的立场问题同构（咨询公司批评 AI 项目同时推销自己的方案）

### 3. 对标

- **跨域关联1: 四属性 ≈ 生成-验证不对称**: 工程工作的四属性本质上是"验证比生成便宜"——编译器/测试让验证成本趋近零。这与 [[Grindability-vs-Verifiability]] 的核心命题一致：AI 杠杆率 = f(验证成本/生成成本)。财务结账之所以不 work，是因为其验证需要跨 NetSuite/Concur/三个银行/两个 ERP 的人工对账——验证成本高于生成成本
- **跨域关联2: Conformance gap ≈ 地图与领土的偏差**: SOP 与实际工作流 30-70% 的差距，是组织知识中"未被写下的部分"（[[20260718-ai-mania-eviscerating-decision-making]] 中内部聊天机器人失败的同一根因：LLM 无法获取未被写下的知识）。两篇来源独立指向同一机制：组织的形式化描述系统性偏离实际实践
- **跨域关联3: 模型无关路由 ≈ 供应链所有权**: "路由层吸收模型变更"与 [[20260727-langchain-own-your-intelligence]] 的 model optionality 主张完全一致——两篇来源（一篇咨询公司、一篇框架厂商）独立收敛于"拥有模型之上的层"

### 关联概念

- [[AI-Deployment-Valley-of-Death]] — 六机构失败率数据是该实体最密集的外部证据集
- [[Grindability-vs-Verifiability]] — bounded/checkable/structured/verifiable 四属性是该概念的操作化版本
- [[Verifiability]] — 四属性中 checkable/verifiable 直接对应
- [[Agent-Orchestration]] — "单一编排层杀死 agent sprawl"
- [[AI-Ready-Organization]] — "process is the bottleneck" 指向组织就绪度
- [[Machine-Readable-Processes]] — 审计与数字孪生即流程的形式化
- [[Building-Effective-Agents]] — 文章直接引用 Anthropic 该文献的"最简方案"结论
