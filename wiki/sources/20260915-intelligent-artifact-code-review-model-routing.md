---
type: source-summary
title: "Is a Low-Cost Model Good Enough for Code Review?"
source_raw:
  - "[[20260915-intelligent-artifact-code-review-model-routing]]"
canonical_url: "https://intelligentartifact.com/posts/gpt-5-6-luna-vs-gpt-6-astra-code-review/"
raw_state: full
created: 2026-09-18
updated: 2026-09-18
tags:
  - source-summary
  - code-review
  - verification
  - agentic-engineering
  - model-routing
evidence_level: low
claim_type: mixed
---

# Is a `$1.20` Model Good Enough for Code Review?

> 来源性质：Intelligent Artifact / Entelligence 的厂商实验。它同时销售模型路由和 AI code review 工具，因此适合提取实验设计与路由假设，不应当作独立基准结论。

## 编译摘要

### 1. 浓缩

- **核心结论 1：低成本模型可以覆盖一部分普通代码审查，但不能按平均命中率替代高能力模型。**
  - 关键证据：50 个公开 Pull Request 的植入缺陷实验中，GPT-5.6 Luna 找到 69 个经核验缺陷，GPT-6 Astra 找到 92 个；总花费分别为 `$0.20` 和 `$5.66`，Luna 约为 Astra 花费的 3.6%。
- **核心结论 2：安全和权限语义是便宜模型最明显的失效区。**
  - 关键证据：Keycloak 上 Luna 找到 6 个、Astra 找到 14 个核验缺陷；安全类缺陷 Luna 找到 9/24，Astra 找到 19/24。Luna 的 93 条发现中只有 74% 被保留，Astra 为 96%。
- **核心结论 3：合理的系统形态是按风险和上下文路由，而不是选择一个“全局最好”模型。**
  - 关键证据：两模型共同找到 44 个缺陷，Astra 独有 48 个，Luna 独有 25 个；并行使用两者可找到 117/143 个核验缺陷，成本约 `$5.86`。文章还指出，权限模型、调用链和历史事故上下文往往不在 diff 中。

### 2. 质疑

- **关于实验外推性的质疑**：样本只有 50 个公开 PR，缺陷是研究者植入的，且每个 PR 都来自模型训练截止时间之前的公开代码；这能控制记忆因素，却不能代表真实生产 PR 的缺陷分布。
- **关于“verified bug”的质疑**：核验标准依赖两个模型判断，Astra 既是参赛模型又是裁判之一；这降低了单模型自评偏差，但没有形成独立的人类或可执行真值。
- **关于稳定性的质疑**：十个 PR 的重复运行中，Astra 两次重复只重现约 67% 的核验缺陷，Luna 约 47%；单次运行的 92、69 等数字不能被读成稳定能力。
- **关于系统缺口的质疑**：文章和评论线程没有完整披露 harness、推理等级和上下文访问；因此“模型能力”与“模型 + 工具 + 仓库上下文”的贡献尚未分离。Hacker News 评论是旁证和方法线索，不是独立证据。
- **口径边界**：低成本模型的价格优势只有在误报、漏报、人工复核和二次调用成本一并计算时才有意义；不能只用每次调用价格做路由决策。

### 3. 对标

- **与 Agent PR 审查对标**：该实验把“便宜模型是否够用”改写成“哪类变更需要哪种审查深度”，可补充 [[Agent-PR-Review]] 的风险分层。
- **与 Harness 对标**：文章关于 diff-only 审查的局限，与 [[Agent-Harness]] 的核心命题一致：仓库结构、权限语义、历史经验和工具访问是审查质量的一部分。
- **跨域迁移**：模型路由应像分诊系统——低风险、可验证、低语义密度的任务优先使用专门化小模型；认证、授权、并发和不可逆操作进入高能力模型或人工升级路径。该迁移仍是综合判断，不是本文直接验证的结果。

## 前提与局限性

本文最适合作为“路由实验的设计样本”和“上下文缺失会扭曲模型比较”的证据，不足以证明某个模型在所有代码库中具有固定排名。厂商利益、植入缺陷、模型参与裁判、单次抽样和 harness 未披露共同决定了 `evidence_level: low`。

## 关联概念

- [[Agent-PR-Review]]
- [[Agent-Verification]]
- [[Agent-Harness]]
- [[Specialized-Small-Models]]
- [[Intelligence-Premium]]
