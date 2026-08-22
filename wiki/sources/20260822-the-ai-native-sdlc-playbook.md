---
type: source-summary
title: "The AI-Native SDLC Playbook（Anthropic 官方）"
source_raw:
  - "[[20260822-the-ai-native-sdlc-playbook]]"
created: 2026-08-22
updated: 2026-08-22
tags:
  - source-summary
  - ai-native-sdlc
  - adlc
  - anthropic-official
evidence_level: high
claim_type: mixed
---

# The AI-Native SDLC Playbook（Anthropic 官方）

> 来源：claude.com/blog，Louis Claxton，2026-08-21。Anthropic 官方 AI-Native SDLC Playbook。**证据定级 high**：Anthropic 官方一手架构文档；**claim_type: mixed**——既有 SDLC 重构的方法论（extracted），也有与传统 SDLC 的对比框架（synthesized）。

## 编译摘要

### 1. 浓缩

- **核心结论1**：**当 code 不再是瓶颈，瓶颈左移到 build 阶段前后**（plan、review/test、deploy）。AI-native SDLC 的核心不是「让 AI 写更多代码」，而是**重新组织六阶段（Plan / Design / Build / Test / Deploy / Maintain）的契约产物与治理手段**
  - 关键证据：Anthropic 官方对比表（intent.md / spec.md / plan.md / CLAUDE.md / Skills / Hooks / Evals 替代传统 backlog / user story / QA gate / 人工 review / 监控）
- **核心结论2**：**Intent 是 AI-native SDLC 的第一公民**。Plan 阶段不再是「委员会收集需求」而是「发起人与 Claude 头脑风暴后写入 `intent.md`」——意图用发起人自己的语言一次性捕获，作为后续所有阶段的 source of truth
  - 关键证据：示例 intent.md（claims status self-service）展示结构——Problem / Proposed Outcome / Constraints 三段式；Design / Build 阶段分别生成 `spec.md`、`plan.md` 与 intent.md 配套
- **核心结论3**：**CLAUDE.md / Skills / Hooks / Evals 是 AI-native SDLC 的四大基础设施**。CLAUDE.md 是新人 context；Skills 是机构知识；Hooks 是 build-time 硬门禁；Evals 是 AI-native 的 stage-gate QA
  - 关键证据：每个基础设施都有具体用法——CLAUDE.md 子目录化、Skills 集中版本化、Hooks（block edits / run formatter / exclude credentials）、Evals（20-50 真实任务 + CI 周期跑 + 配置变更门禁）

### 2. 质疑

- **关于「六阶段非线性 loop」**：本文把 SDLC 重构为「loop」而非「pipeline」，但没说明 loop 的**触发条件**与**终止条件**。什么样的事件触发 Maintain → Plan 回到起点？事故、模型升级、用户反馈、还是季度 review？loop 的可操作性需要补充
- **关于「intent.md 作为 source of truth」**：发起人用自己语言写的 intent.md 必然有歧义、不完整、缺约束。Design 阶段由 Claude 生成的 spec.md 加入了组织 skills（brand / security / compliance / UX）——但**谁审 spec.md 是否覆盖了 intent.md 的所有约束**？Build 阶段的 plan mode 提供「质询 plan」机制，但 Design 阶段没有同等强度的 review gate
- **关于「Hooks 作为硬门禁」**：Hook 是 deterministic script，能执行 lint / test / path protection，但不能执行**语义级**约束（如「这段代码是否符合架构原则」）。本文把 Hook 描述为万能门禁，但实际 Hook 只能解决 syntactic concerns。语义级 review 仍需多层 agentic review + 人工 review
- **关于「Maintain 阶段的 1σ/2σ/3σ 响应分级」**：本文提到控制带破线时分级响应，但**控制带的定义、监控指标的选择、误报处理**未展开。这是 Monitoring (OpenTelemetry) 能力的实操考验，需要组织有成熟的 observability stack
- **关于「20-50 真实任务作为 evals」**：eval 任务的代表性（representativeness）、漂移检测（drift detection）、与 production incident 的因果关联（incident → eval 的反向追溯）均未深入。Cainex 等公司的高质量实践未必能直接复制到资源有限的 startup

### 3. 对标与旁逸

### 3a. 对标（跨域类比）

- **「intent.md → spec.md → plan.md」链路 ↔ [[Knowledge-Compilation|知识编译]] 的阶段化**（综合判断）：Plan 阶段产生 intent.md 是「用户意图编译」；Design 阶段产生 spec.md 是「意图 → 设计的精炼」；Build 阶段产生 plan.md 是「设计 → 实现的可执行规约」。三步产物与 LLM Wiki 的 raw → source → entity 编译链同构
- **「AI-native SDLC」 ↔ [[Agent-Development-Lifecycle|ADLC]]**（综合判断）：与既有 entity 完全同构——AI 时代取代 SDLC 的生命周期范式，Agent 覆盖全生命周期，Workflow 取代 CI/CD 作为编排原语。本期是 ADLC 的官方权威版本，提供了六阶段具体 plays
- **「CLAUDE.md」 ↔ [[AGENTS-md|AGENTS.md]]**（综合判断）：既有 entity 已定义 AGENTS.md 作为「Agent 棘轮规则手册」。本文具体化了子目录 CLAUDE.md 的用法——约定分层、命令索引、架构描述、常见错误。Skills-as-Products 提供 governance 视角（标准化目录 + CI + 责任到人）
- **「Hooks as build-time guardrails」 ↔ [[Secure-Paved-Path|安全铺装路径]]**（综合判断）：Palantir 提出的「绕过比遵守更难」原则的工程化实现——hooks 让 default path 强制通过安全检查，比让 developer 主动记得安全更可靠
- **「Maintain → 闭环回写 intent.md」 ↔ [[Lessons-MD-Self-Improvement|Lessons-MD 自我改进]]**（综合判断）：Claude Tag 实践是「事故 → lessons.md → 下次事故先读」的微观机制；本文的「Maintain → 写回 intent.md」是组织层的宏观闭环。两个机制同构——从产物反哺原始 spec
- **「Claude Tag 作为 Slack 频道成员」 ↔ [[Distinct-Principal-Identity|独立主体身份]]**（综合判断）：Maintain 阶段提到 Claude Tag「以自己的身份」参与工作沟通频道，与 Vercel Agent 的 Distinct Principal Identity 完全同构——AI 不再是工具调用，而是有持久身份的协作成员

### 3b. 旁逸（跨域洞察）

- **「code 不再是瓶颈 → 瓶颈左移」 ↔ [[Jevons-Paradox]] 的工程层版本**（综合判断）：code 边际成本骤降（生成成本几乎为 0）后，组织瓶颈自动迁移到稀缺资源（人类判断力、领域知识、合规审查、observability 容量）。这是 [[Jevons-Paradox]] 在软件工程层面的具体应用
- **「Plan → Design 坍缩为单 session」 ↔ [[Cognitive-Debt|知识债务]] 与 [[Incidental-Learning|附带学习]]**（综合判断）：传统 SDLC 的多阶段 sign-off 不仅是治理，也是 incidental learning 的载体——产品经理在 workshop 中学习工程师的实现约束。坍缩为单 session 会让这种学习短路，需要补充 [[Cognitive-Debt]] 风险
- **「evals as stage-gate QA」 ↔ [[Evals-as-PRD|评测即需求文档]]**（综合判断）：两者都把 evals 提到比传统测试更高的地位——既是质量门禁，也是需求/契约的承载体。本文给 evals 加了 incident → eval 的反向追溯，与 Lenny/PRD 框架互补
- **「Maintain 阶段 1σ/2σ/3σ 分级响应」 ↔ [[Alert-Closed-Loop|告警闭环]]**（综合判断）：分级响应是 [[Alert-Closed-Loop]] 的具体实现——1σ 只 log（通知）；2σ 诊断（评估 + 干预）；3σ 行动（复盘 → 改进）。把告警生命周期完整落到 agent 可执行配置中

### 3c. 约束（边界分析）

- **「intent.md 作为 source of truth」的硬约束是「发起人对问题的语言表达能力」**（综合判断）：intent.md 的质量直接决定下游所有阶段。如果发起人不能用 AI 清晰表达问题，intent.md 会成为系统性噪声的源头。这是 AI-native SDLC 的隐藏门槛——组织需要投资「prompt literacy」（与 4D AI Fluency 同构）
- **「Hooks 作为硬门禁」的软约束是「Hook 维护成本与开发者摩擦的平衡」**（综合判断）：Hook 越多越安全，但开发者摩擦越大。Anthropic 的「绕过比遵守更难」是默认正向设计，但具体每个组织的 hook threshold 需要根据 feature velocity vs safety tradeoff 调整
- **「Continuous evals in CI」的软约束是「真实任务的样本代表性」**（综合判断）：20-50 真实任务的采样方法、时间窗口、多样性保证——如果不严谨，evals 会成为 Goodhart target。本文未给采样方法论，需要结合 [[Sample-Efficiency]] 等评估方法学
- **「非线性 loop」的硬约束是「loop 内各阶段的契约清晰度」**（综合判断）：loop 比 pipeline 高效的前提是阶段间契约（intent.md / spec.md / plan.md）足够清晰。如果契约模糊，loop 反而会比 pipeline 更混乱——因为它失去了 stage-gate 的强制 review 机制

## 关联概念

### 直接引用 / 强关联
- [[Agent-Development-Lifecycle|ADLC]] — 本期是 ADLC 的官方权威版本
- [[Knowledge-Compilation]] — intent.md / spec.md / plan.md 三步编译链
- [[AGENTS-md|AGENTS.md / CLAUDE.md]] — 四大基础设施之一
- [[Skills-as-Products]] — Skills 的 governance 视角
- [[Secure-Paved-Path|安全铺装路径]] — Hooks 的安全哲学
- [[Lessons-MD-Self-Improvement|Lessons-MD 自我改进]] — Maintain 闭环反哺
- [[Distinct-Principal-Identity|独立主体身份]] — Claude Tag 在 Slack 频道的身份
- [[Alert-Closed-Loop|告警闭环]] — 1σ/2σ/3σ 分级响应
- [[Claude-Tag]] — Maintain 阶段的代表 agent
- [[Claude-Code-CLI]] — Build 阶段的核心工具

### 旁逸关联
- [[Jevons-Paradox]] — 「code 不再是瓶颈」的经济学解释
- [[Cognitive-Debt]] / [[Incidental-Learning]] — 多阶段坍缩的学习短路风险
- [[Evals-as-PRD|评测即需求文档]] — evals 的更高地位
- [[Sample-Efficiency]] — evals 采样方法论
- [[Generation-Verification-Asymmetry]] — Hooks 只能解决 syntactic concerns 的边界

### 待补 entity 候选
- **AI-Native-SDLC** — 本文核心概念，已有 [[Agent-Development-Lifecycle|ADLC]] 接近但未具体化为六阶段 + 契约产物。建议建独立 entity 或在 ADLC 内部补充
- **Intent.md / Intent Spec** — AI-native SDLC 的第一公民产物，值得建独立 entity
- **Hooks-as-Guardrails** — 已被多个 entity 提及（[[Secure-Paved-Path]]、[[Skills-as-Products]]），但未建独立 entity；本文提供了 build/deploy 两阶段的具体用法
