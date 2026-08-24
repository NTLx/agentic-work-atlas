---
type: source-summary
title: "Engineers will do anything to avoid learning from history"
source_raw:
  - "[[20260815-engineers-history-reinvention]]"
created: "2026-08-19"
updated: "2026-08-19"
tags:
  - source-summary
  - software-history
  - program-management
  - agentic-orchestration
  - reinvention
evidence_level: medium
claim_type: mixed
---

# Engineers will do anything to avoid learning from history — Horn (2026-08)

## 编译摘要

### 1. 浓缩

- **核心结论 1**：**工程师有一种系统性的习惯——把已有领域重新发明，包装成新东西**；AI 时代的"agentic orchestration"就是 program management 的重新命名。
  - 关键证据：3 个历史先例——(1) 数据科学 = 统计学 + cooler name；(2) Crypto = finance 的 speedrun；(3) 甚至"重新发明公交站"。
  - 关键证据：AI 时代工程师突然发现需要为 AI 写明 spec（→ waterfall）、不能读 10k 行 PR（→ 中间过程）——他们在重新发明程序管理。
  - 关键证据：作者对 HN 上 Geoffrey Litt "Understanding is the new bottleneck" 和 Allen Bargi "Working with AI feels more like leadership" 两篇帖的反应——这是趋势。

- **核心结论 2**：**"重新发明"动机的二分**——有效原因（不信任传统机构、从第一原理建立更深理解）+ 无效原因（包装新东西能融资、"能有多难？"）。
  - 关键证据：作者明确二分两类动机。
  - 关键证据："Nobody raises a round to apply a well understood discipline correctly"——融资激励倒置。

- **核心结论 3**：**Agent management 实际上需要的是程序管理的核心实践**——明确需求文档、确定优先级、清晰工作流、过程保证、定期 check-in——agentic orchestration 已经在做这些但不愿用旧名字。
  - 关键证据：6 本推荐书覆盖程序管理经典：Making Things Happen、PMBOK、Mythical Man-Month、Royce 1970 原论文（12 页 PDF）、High Output Management、The Goal（约束理论）。
  - 关键证据：Mythical Man-Month 关于"communication overhead 随 headcount 二次方增长"——直接适用于 10 个 agent 的情况。

### 2. 质疑

- **关于"重新发明 = 不读 manual"的强论断**：
  - **依赖前提**：假设"已有领域"稳定。但 deep learning 不是统计学的简单重新命名——GPU/TPU 训练范式、Transformer 架构是新增的。
  - **反例**：CRDT 不是分布式系统理论的简单重新包装——实质解决了 CAP 下的可用性 tradeoff。
  - **反例**：Linux kernel development 不是传统 OS 教科书的简单重做——open source 协作模型是新增的。
  - **边界**：作者的核心论断（"工程师系统性地不读 manual"）仍成立，但"重新发明 = 完全相同"的强论断需谨慎。

- **关于"agentic orchestration = program management"的精确性**：
  - 这是核心命题，需警惕"鸭子测试"的过度简化——看起来像 duck 但不一定是 duck。
  - **反例**：agent 与人类员工的关键差异——deterministic execution + no context switching cost + no ego——program management 的人际方面可能完全不适用。
  - **反例**：Geoffrey Litt 那篇 "Understanding is the new bottleneck" 实际上邀请工程师重新理解 spec——这不是拒绝 PM，是接受 PM 的核心 spec writing。
  - **边界**：spec writing 和 requirements documentation 在 AI 时代有质变（自然语言 spec 可能比传统 spec 更灵活），不能简单回归到 1970 范式。

- **关于书单推荐**：
  - 这是作者主观判断——他承认 High Output Management 自己没读。
  - **反例**：很多程序管理书针对的是瀑布式/重型项目，不适用于 startup / AI 时代小团队。
  - **边界**：推荐 Royce 1970 原论文值得读，但 Royce 论文本身是描述而非规范——他实际展示的是"瀑布的失败案例"，不是程序管理的圣经。

- **关于"工程师不愿承认管理者是对的"**：
  - 这是社会学观察，可能有 selection bias。
  - **反例**：很多工程师确实在转向 servant leadership / coaching 风格——不是拒绝管理角色，是重新定义管理。
  - **边界**：作者的"snarky 抱怨"语气本身是文化信号——HN 社区的反管理传统使得"用程序管理解决 AI 问题"听起来不性感，但这是 social dynamics 不是 logic。

### 3. 对标与旁逸

#### 3a. 跨域类比

- **"重新发明 = 不读 manual" ↔ [[Harness-Engineering]]**：Harness 是工程化"manual"，Agent = Model + Harness。这与 horn 的核心命题同构——harness engineering 是 manual-reading 的工程化。
- **"agentic orchestration = program management" ↔ 软工程项目管理经典**：与 [[Mythical-Man-Month]] 概念直接相关——Brook 1975 关于 communication overhead 二次方的论断被作者重新映射到 agent 管理。
- **"Mythical Man-Month 通信开销 ↔ Multi-Agent 系统复杂度"**：与库中 multi-agent 主题同构——多个 agent 之间的协调成本确实是 scaling 的核心问题。
- **"Royce 1970 瀑布论文 ↔ spec-driven development"**：Royce 论文实际是论证瀑布的失败（多数读者忽略）——这与 [[Software-2.0]] / spec-driven 的现代 AI 时代讨论同构。
- **"约束理论（The Goal） ↔ AI 时代瓶颈"**：Geoffrey Litt "Understanding is the new bottleneck" 是 The Goal 的 AI 时代回响——作者对此 snarky 反应揭示了"工程师不愿承认前人已说过"模式。

#### 3b. 旁逸

- **"Winston Royce is probably unknown to most engineers"**——作者隐含的"工程师集体失忆"论断：1970 的瀑布论文描述是 failure case，但工程师既没读过论文，也没真正理解 waterfall 的局限性，所以 AI 时代又重新踩进同一个坑。这是历史认知的代际丢失信号。
- **"How to guides for program management don't tend to make the HN front page"**——这是 [[Vibe-Coding]] 文化的反面：HN 社区偏爱"性感新东西"（vibe coding、agent orchestration），但程序管理不被看见。这是一个 cultural filter effect——不是知识不存在，而是被 social dynamics 过滤掉。

#### 3c. 约束分析

- **结论 1 成立的硬约束**：软件工程史上有大量"重新发明"——这是历史模式；但也有真正新增范式（open source、cloud-native、Linux、deep learning）——需区分"重新包装"vs"重新发现"。
- **结论 2 成立的硬约束**：工程师心理动机难观察——"营销驱动 vs 理性驱动"二分可能过于清晰。融资激励确实存在但非唯一驱动。
- **结论 3 成立的软约束**：program management 经典书籍（1970-2000）针对瀑布项目——AI 时代的 adaptation 需重新做，不能简单回归。

### 关联概念

- [[Horn]]（Author，待 validated_source）
- [[Mythical-Man-Month]]（forward reference，跨源经典）
- [[Peter-Naur]]（forward reference，与 jsbarretto 共享引用）
- [[Harness-Engineering]]
- Waterfall（forward reference，单源待建 entity）
- [[Software-2.0]]（forward reference，库中 raw 已存但 entity 待复核）
- Geoffrey-Litt（forward reference，被引用的 upstream）
- Understanding-is-the-New-Bottleneck（forward reference，Litt 论文）
- [[20260814-i-remain-a-skeptic]]（同向反方对照）
- [[20260816-openai-head-of-design-best-time]]（OpenAI 视角对照）

### 待解问题

1. "重新发明 = 不读 manual" 是普遍模式还是 selection bias？需更多历史样本验证。
2. agentic orchestration 与 program management 的精确映射——哪些维度同构？哪些维度有质变？
3. 工程师 collective 失忆现象（Royce 1970 已被忘记）的代际机制是什么？
4. Mythical Man-Month 的 communication overhead 二次方定律在 multi-agent 系统是否仍成立？
5. AI 时代 program management 的 revival 是"重新命名"还是"实质性重新发明"？