---
type: source-summary
title: "How Cresta turned CX expertise into an agent builder on the Claude Agent SDK"
canonical_url: "https://claude.com/resources/articles/how-cresta-turned-cx-expertise-into-an-agent-builder-on-the-claude-agent-sdk"
raw_state: index
original_raw_file: "20261005-claude-cresta-agent-builder.md"
original_body_sha256: "56f0eeef882abc414a549fda914f161ceac20f6036b0e08b4df70d4f0f38bf61"
indexed_at: "2026-10-21T12:36:09+08:00"
created: 2026-10-21
updated: 2026-10-21
tags:
  - source-summary
  - agent-harness
  - agent-evaluation
evidence_level: low
claim_type: mixed
---

# How Cresta turned CX expertise into an agent builder on the Claude Agent SDK

## 编译摘要

### 1. 浓缩
- **核心结论1：通用执行 Harness 与领域控制层可以分工。** Cresta 将 Claude Agent SDK 用作通用执行 Harness，负责收集上下文、调用工具、编写并运行代码；Conductor 则在其上承载 CX 专属的对话数据、领域知识、工作流、策略、可观测性、验证与反馈。其产品价值主张是把 Cresta 的 CX 经验接入通用 Agent 开发能力，而不是另建一套通用执行底座。
  - 关键证据：文中 “Building Conductor on the Claude Agent SDK” 明确描述 SDK 与 Conductor 的分层；Renjie Li 的引语说明把对话智能、CX 专长、评估和 runtime 接到 SDK harness 上。
- **核心结论2：Agent builder 的核心工作包含发现并固化灵活性与确定性边界，以及持续迭代。** Conductor 借助历史对话发现哪些环节应保留模型适应空间、哪些企业关键流程要用规则和受控工具行为加固；需求和边缘案例再转成 eval 测试，在政策、系统和对话模式变化后持续回归。
  - 关键证据： “Making the important decisions easier” 描述从历史对话识别人工介入与模型适应边界；“How Cresta evaluates Conductor” 及后续段落说明构建期捕获的需求和边缘案例会成为测试，并用于持续监测与更新。
- **核心结论3：评估应覆盖结果、执行过程和成本，并用固定任务集比较迭代。** Cresta 的任务包括构建新 Agent、编写测试、修改既有 Agent 和根因分析；评价结果可用性、工具/上下文使用路径、相对参考答案的质量及时间与模型用量。新 Claude 模型或框架更新时，以相同任务和评分回归。
  - 关键证据：原文 “How Cresta evaluates Conductor” 列出的四项维度及新模型/框架更新后的同任务回归描述。

### 2. 质疑
- **关于分层架构的质疑**：这是 Cresta 对自身 CX 产品的架构陈述，能说明一种落地方式，但没有与其他 Harness/控制层设计做对照，也没有量化各层独立贡献；不能据此认定所有垂直 Agent 都需要同样的分层。
- **关于灵活/确定性划分的质疑**：历史对话可暴露常见模式和边界候选，但来源没有交代如何处理低频、高损失事件、分布漂移或对话样本中的偏差。规则是否完整、工具权限是否正确仍需独立验收。
- **关于评估的质疑**：固定任务集和 curated reference 有利于回归，但可能覆盖不了线上新情境，也可能让系统针对已知任务优化。文中未给任务数、评分者一致性、指标方差或线上安全结果。
- **关于部署效果的质疑**：初始部署时间约减半是 Anthropic 对 Cresta 早期用例的转述，属于厂商案例中的 Cresta 自报；无基线定义、样本量、时间窗和独立验证，不能外推为普遍提效幅度。
- **关于资源与成本的质疑**：评估包含时间和模型用量，但文章没有报告实际数值，因而不能判断质量收益与成本变化的净效果。

### 3. 对标
- **跨域关联1：Harness 的通用执行能力与领域知识层分离**，可与 [[Agent-Harness]] 中 Harness 负责运行时、工具和状态边界的框架对读。本例补充的是产品化路径：复用通用执行 Harness，把耐久差异化投入领域数据、规则、eval 与反馈闭环。
- **跨域关联2：固定任务回归把 Agent builder 变成可持续验证的开发流程**，与软件工程中的回归测试相似；但 Agent 的验收还应观察路径和资源使用，不能只看最终产物是否通过。
- **跨域关联3：灵活性与确定性按风险分配**，可迁移到有硬性政策约束的工作流：从真实交互识别需固化的边界，将低风险表达和适应性留给模型；此迁移是分析推论，具体边界须由各域风险、规则和可验证性决定。

### 证据定位
- 原始网页标题与摘要、背景和“quick pitch”：文章开头至 “A meta-agent that helps build the next agent”。
- 灵活/确定性边界、历史对话用途： “Making the important decisions easier”。
- 任务集、四项评估维度、模型/框架回归： “How Cresta evaluates Conductor”。
- SDK 与 Conductor 分层、隐私/租户/密钥/控制/可观测性考量： “Building Conductor on the Claude Agent SDK”。
- 部署时间约减半：上述架构段落之前的 Cresta 早期用例陈述；来源未提供方法细节。

### 关联概念
- [[Agent-Harness]]
- [[Agent-Verification]]
- [[Harness-Engineering]]
