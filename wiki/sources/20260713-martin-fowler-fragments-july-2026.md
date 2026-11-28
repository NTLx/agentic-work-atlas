---
type: source-summary
title: "Martin Fowler Fragments: Harness Engineering, Self-Hosted Models, and Agent Unit of Work"
source_raw:
  - "[[20260713-martin-fowler-fragments-july-2026]]"
created: 2026-07-14
updated: 2026-11-28
tags:
  - source-summary
  - harness-engineering
evidence_level: medium
claim_type: mixed
---

# Martin Fowler Fragments: Harness Engineering, Self-Hosted Models, and Agent Unit of Work

## 编译摘要

### 1. 浓缩

- **核心结论1**: **该次 Thoughtworks retreat 中 Harness Engineering 成为专门讨论议题**——Thoughtworks retreat 首次有了完整的 Harness Engineering 专题讨论。Guide 侧聚焦 context 管理（agents.md 控制在 200 行以内），sensor 侧聚焦 computational sensors（property-based testing、形式化方法、向强类型语言迁移）。
  - 关键证据: "When we had our first retreat in Utah early this year, nobody had heard of Harness Engineering. This time we had a whole session on it." 与会者分享了具体实践——限制 context 大小、使用 Rust 替代 Python、形式化方法验证。
- **核心结论2**: **Agent 的"工作单元"是当前核心争议**——所有 session 都在回答同一个问题："How much do we let an agent decide, and how do we stay confident in what it does?" 不同团队在设置同一组控制参数：工作单元大小、交接准备、返回值检查、Agent 边界约束。
  - 关键证据: Kief Morris 的跨 session 综合发现——"people were making the same handful of choices over and over about a single thing: the unit of work they were prepared to hand to an agent."
- **核心结论3**: **Sam Ruby 提出用 Manage by Objective 理解非工程师委派 Agent**——当 manager 使用 LLM 时，不是"拿起工具"而是"做了一个 hire"。问题不是"非工程师是否被允许使用"，而是"是否知道如何管理目标而非方法"。这回到 Drucker 1959 年的管理学洞见。
  - 关键证据: Sam Ruby 的"Bring Me a Rock"session——"When a manager reaches for an LLM instead of routing the work to the team, they didn't pick up a tool — they made a hire." 这是管理视角的观点，不取消权限、专业资质或验收责任。

### 2. 质疑

- **关于"Harness Engineering 共识"的质疑**: 与会者是 tech-savvy 前沿实践者。harness engineering 的共识在 Thoughtworks retreat 中成立，但未必代表行业平均水平。"模型变好后 harness 是否还有必要"仍悬而未决。
- **关于"Unit of Work"的质疑**: 这个问题可能过于聚焦于静态任务分解。更深层的问题可能是：Agent 的工作单元应该如何随信任建立而**动态扩大**？不同团队的设置不同，但有没有一个成熟度模型？
- **关于"Manage by Objective"的质疑**: Drucker 的 MBO 框架在管理学中有争议——实际执行中常退化为 KPI 驱动的微管理。将 MBO 应用于 LLM 管理是否也会退化？"unstated objectives"被正确识别但没有系统化解决方案。
- **关于 Self-hosted models 的质疑**: GPU 人才稀缺是硬约束，但云服务提供商可能很快提供托管推理服务来降低门槛。self-hosting 的兴趣可能只是过渡期现象。

### 3. 对标

- **Agent Unit of Work 对标组织行为学 delegation theory**: delegation 不是全有全无，而是在范围、自主度、检查频率上的连续光谱。不同团队设置的"同一组控制参数"正是 delegation 的经典维度。
- **Self-hosted models 对标 private cloud 历史**: Fowler 自己提出这个类比——half-arsed private clouds 的教训是，简化交互协议才能避免重蹈覆辙。GPU 数据中心管理是新的稀缺技能。
- **Conformance tests (sensors) > specifications (guides) 对标 formal verification vs testing**: 在不确定系统中，Fowler 的判断是 runtime testing (sensor) 比 specification (guide) 更有价值——这是作者在未言明目标背景下的比较意见；规格和 conformance checks 互补，未证明传感器普遍优于规约。
- **Contributory vs Interactional expertise 对标 LLM distribution shift**: Dan Davies 和 Fowler 将二者类比为待讨论问题；不能从知识来源推出模型必然无法处理全新情境。这直接对应 distribution shift / out-of-distribution 问题。
- **Josh Comeau 自报当年课程销量约为原来的1/3（非明确收入下降比例）**: AI 对知识创造者经济模型冲击的早期量化信号。LLM 替代的不仅是学习者，也是内容创造者的商业模式。

### 关联概念

- [[Harness-Engineering]]
- [[Agent-Harness]]
- [[Agent-Verification]]
- [[Self-Hosted-Models]]
- [[Agent-Unit-of-Work]]
- [[AI-Era-Career-Skills]]
- [[Context-Engineering]]
- [[Martin-Fowler]]
