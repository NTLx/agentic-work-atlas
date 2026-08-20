---
type: source-summary
title: "Citizens Build, Agents Execute, Experts Govern"
source_raw:
  - "[[20260820-rachel-laycock-citizens-agents-experts.md]]"
created: 2026-08-20
updated: 2026-08-20
tags:
  - source-summary
  - engineering-judgment
  - ai-era
  - thoughtworks
  - organization
evidence_level: medium
claim_type: mixed
---

# Citizens Build, Agents Execute, Experts Govern

## 编译摘要

### 1. 浓缩

- **核心结论1**: AI 时代的稀缺资源发生相变——过去几十年我们优化"编码能力"（稀缺），但**真正的稀缺是 engineering judgment**——知道"什么算好"、"风险是否理解"、"works today 是否能 trust in production"；experienced engineers 不被取代，反而被**极度 leverage**
  - 关键证据: FOSE 讨论中"spent surprisingly little time talking about coding"——design/architecture/governance/learning 主导；experts 从"自己写每个 feature"翻转为"design guardrails/platforms/practices 让 thousands features 安全被构建"
- **核心结论2**: "Citizens Build, Agents Execute, Experts Govern" 三分法——不是角色分类而是**价值流动**：Citizens（任何能 turn ideas into working software 的人）+ Agents（执行：write code/refactor/test/fix/iterate）+ Experts（治理：架构/安全/韧性/operability/compliance/cost）
  - 关键证据: Rachel 自陈"I think I was talking about where value is moving, not roles"；FOSE 团队"specification design → agents work → review next morning" 模式
- **核心结论3**: demo 阶段与 production 阶段的鸿沟不在 capability——在 judgment。同一段代码在 demo phase works，但 "is customer data protected? What happens when a dependency fails? Can someone else understand this system in two years? Will it survive an audit? Can it cope with 1000×more users?" 这些问题不出现
  - 关键证据: Rachel 自陈 "I certainly wasn't asking them when I was building my first apps. I only cared about features!"
- **核心结论4**: **"Organisations don't run on code. They run on trust."**——当 agents 可生成大量 code 时，good design matters more, not less；judgment 的杠杆是因为 decisions 的下游影响放大（千 features 共用 platforms/guardrails）
  - 关键证据: Rachel 引用 FOSE 讨论共识

### 2. 质疑

- **关于"engineering judgment 真的稀缺"的归因**：Rachel 自己也说"I'm not convinced that was ever the real scarcity"——可能从来都稀缺，只是被 coding scarcity 掩盖。AI 时代 judgment 显形而非新稀缺
- **关于"three buckets 三分"的边界**：Citizens / Agents / Experts 的边界在 AI 时代模糊——citizens 也用 agents，agents 内部有 judgment，experts 也 write code。框架是 value-flow 描述而非可操作的 role boundary
- **关于"experts 不被取代"的可能反向**：experts 数量未必增加，但 productivity 可能下降（治理开销 vs coding 产出）；不同 org 会用不同模型——startup 可能 lean agents + minimal experts；enterprise 必然要 experts
- **关于"experts 杠杆增加"的边界**：杠杆增加意味着每 expert 负责更大 scope 的 citizens × agents——但 experts 仍是 bottleneck（人员有限）；crowd-source judgment 是否可行未论证
- **关于"production concerns 是 expert 的活"的归因**：vs developers with AI literacy 也可承担 production concerns——AI 时代的 "engineer" 可能更接近 "full-stack producer + operator" 而非 pure expert
- **关于 FOSE 共识**：是 Thoughtworks 内部观察 + industry event anecdotal；缺乏跨组织系统性数据
- **关于"Citizens build safe software"**：citizens 用 AI 建的软件进入 production 时的 risk 与 expert-built 不同；可能需要更严格的自动 verification + sandbox
- **关于"trust 不是 code"**：是修辞——trust 在 production 系统由 technical controls（access control + audit + monitoring + SLO）保证，不是由 expert 的话保证

### 3. 对标与旁逸

- **跨域关联1**: "Citizens/Agents/Experts" 三分与 [[AI-Era-Career-Skills]] 同构——后者展开 AI 时代的 engineer skill 转型，本文浓缩为 value-flow 框架
- **跨域关联2**: "experts 设计 guardrails/platforms 让 thousands features 安全被构建" 与 [[AI-Native-Engineering-Org]] / [[Agent-First-Enterprise]] 同源——组织形态调整
- **跨域关联3**: "engineering judgment 是真正稀缺" 与 Engineering Judgment（forward reference，未建 entity）（forward reference） / [[Taste-vs-Judgment]] 同源——judgment 在 AI 时代的稀缺性
- **跨域关联4**: "Captain-Mindset" 概念与本文 experts 角色高度同构——Captain = Experts who design vessel/platform 让 crew 自由航行
- **跨域关联5**: "Organisations run on trust" 与 [[AI-Identity-Bifurcation]] / [[Distinct-Principal-Identity]] / [[Operational-Responsibility]] 同源——agent 时代 trust 的建立机制
- **跨域关联6**: "experts 杠杆放大" 与 [[Jevons-Paradox-for-Knowledge-Work]] 同构——AI 让 feature 便宜，但 expert governance 变得更关键
- **跨域关联7**: "weekend app vs enterprise software" 鸿沟与 [[Knowledge-Debt]] / [[Operational-Responsibility]] 同源——deployment 后才知道的 concerns
- **跨域关联8**: "AI 让 anyone build software" 与 [[Agent-Adoption-Curve]] / [[Agentic-Speculation]] 同构——AI 时代软件生产普及
- **跨域关联9**: "good design matters more not less" 与 [[Just-Do-Less]] / [[Capability-Overhang]] 同源——廉价时代 design 的相对价值升高

## 关联概念

- [[Citizens-Agents-Experts-Framework]]（新建）— 三分法本身
- [[Rachel-Laycock]]（新建）— Thoughtworks CTO
- [[AI-Era-Career-Skills]]（已有）— engineer skill 转型
- [[Captain-Mindset]]（已有）— experts 角色对应
- [[AI-Native-Engineering-Org]]（已有）— 组织形态调整
- [[Taste-vs-Judgment]]（已有）— judgment 的稀缺
- [[Operational-Responsibility]]（已有）— production ownership
- [[Jevons-Paradox-for-Knowledge-Work]]（已有）— knowledge work 悖论
- [[Agent-Adoption-Curve]]（已有）— AI 普及
- [[Knowledge-Debt]]（已有）— deployment 后才发现的 concerns