---
type: source-summary
title: "A Scorecard for the AI Age"
source_raw:
  - "[[20260717-openai-scorecard-ai-age]]"
created: 2026-07-27
updated: 2026-07-27
tags:
  - source-summary
  - AI-economics
  - token-efficiency
  - enterprise
  - evaluation
evidence_level: medium
claim_type: mixed
---

# A Scorecard for the AI Age

> OpenAI CFO Sarah Friar 提出以"Useful Intelligence per Dollar"为核心的四问记分卡框架，用于衡量企业 AI 投资回报。来源：OpenAI 官方博客（2026-07-17）。证据等级 medium——框架由厂商 CFO 提出，具有商业推广动机，但所引数据（DeepSWE 基准、token 效率对比）可独立验证。

## 编译摘要

### 1. 浓缩

- **核心结论1：AI 价值度量应从 cost-per-token 转向 cost-per-successful-task**
  - 关键证据：四问记分卡的第二问明确定义"成功任务成本 = 完成工作的全部成本 / 达到质量标准的任务数"。最低 token 单价≠最低结果成本——前沿模型一次通过可能比便宜模型多次重试更经济。
  - 关键证据：GPT-5.6 Sol 在 Artificial Analysis Coding Agent Index 上使用 54% 更少的输出 token 同时创下新 SOTA，直接说明 token 消耗量与任务完成质量不成正比。

- **核心结论2：AI 部署的可靠性应分三档评估（ready-to-use / needs-correction / needs-escalation）**
  - 关键证据：ChatGPT Work 产品中实际落地的三档分类体系——直接可用、需要修正、需要人工介入。
  - 关键证据：第三问要求在 AI 从"起草"走向"执行"之前，组织应预先定义数据访问边界、系统权限和人工审查阈值。

- **核心结论3：AI 投资的复利效应——计算为中心的飞轮**
  - 关键证据：Friar 描述的飞轮：更好基础设施 → 更好研究 → 更强模型 → 更好产品 → 驱动采用 → 支持持续投资。这是 OpenAI 作为垂直整合厂商的战略叙事。

### 2. 质疑

- **关于"cost-per-successful-task"的质疑**：框架本身合理，但 Friar 作为 OpenAI CFO 提出此框架，利益相关性明显——当 OpenAI 的前沿模型在 cost-per-task 上有优势时，推广此度量等于推广自家产品优势。这不影响框架的逻辑正确性，但读者需区分"好的度量方法"和"对某一厂商有利的度量方法"。与 [[Input-Output-Outcome]] 框架异曲同工——两者都主张从结果而非输入计量 AI 价值，但 Friar 框架更具操作性（四问可直接做成检查表）。

- **关于 GPT-5.6 Sol 数据的质疑**：DeepSWE v1.1 得分 72.7%（vs Claude Fable 5 的 69.9%）和"36.2% 更低 API 成本"是厂商自报数据。"估计 API 成本"的计算方法未披露——是否包含重试、上下文预加载、工具调用等真实部署场景中的成本？54% fewer output tokens 在单一基准上的表现不一定泛化到实际工作流。

- **关于三档可靠性模型的质疑**：ready-to-use / needs-correction / needs-escalation 分类是实用的，但缺乏量化阈值——什么算"达到质量标准"由谁定义？如果由 AI 厂商的产品定义，存在 [[Goodharts-Law|Goodhart 效应]] 风险。

### 3. 对标

- **跨域关联1（Token 效率 → 架构质量投影）**：Friar 的"cost-per-successful-task"与 [[Agentic-Workflow-Token-Efficiency]] 中的"Token 效率是架构质量在成本轴上的投影"高度吻合。两者都主张不应用原始 token 消耗量衡量 AI 价值，但 Friar 框架更面向企业决策者（四问检查表），Token 效率实体更面向工程师（ET 公式、Forsgren 四维度互锁）。互为补充。

- **跨域关联2（Delegative UI 的验收结构）**：三档可靠性分类（ready-to-use / needs-correction / needs-escalation）与 [[Delegative-UI]] 中"AI 从起草走向执行"的叙事完全一致——Delegative UI 需要明确的验收标准和异常升级规则，Friar 的三档体系提供了一个可操作的验收分类。同时与 [[Escalation-Based-Human-Oversight]] 直接对应。

- **跨域关联3（Input-Output-Outcome 的厂商版）**：Friar 框架可视为 [[Input-Output-Outcome]] 的"厂商操作化版本"。Input-Output-Outcome 是批判性分析框架（质疑 AI 是否真的提升了 outcome），Friar 框架是建设性操作框架（提供四问帮助企业追踪 outcome）。前者适合治理审计，后者适合采购决策。

### 关联概念

- [[Agentic-Workflow-Token-Efficiency]]
- [[Input-Output-Outcome]]
- [[Delegative-UI]]
- [[Escalation-Based-Human-Oversight]]
- [[Token-Supply-Chain]]
- [[Goodharts-Law]]
- [[OpenAI]]
