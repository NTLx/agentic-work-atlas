---
type: source-summary
title: "Auditing in the age of (good enough) AI"
canonical_url: "https://blog.trailofbits.com/2026/09/18/auditing-in-the-age-of-good-enough-ai/"
raw_state: index
original_raw_file: "20260918-trailofbits-auditing-good-enough-ai.md"
original_body_sha256: "d404a8d7010ae5ab760b7e5de56763632771aec557a2352d5aeccfce5c455781"
indexed_at: "2026-09-22"
created: 2026-09-22
updated: 2026-09-22
tags:
  - source-summary
  - agentic-engineering
  - security-audit
  - formal-verification
evidence_level: medium
claim_type: mixed
source_locator:
  - "开篇与 Auditing the Miden zkVM：审计背景与工具缺口"
  - "Building all the tools!：LSP、decompiler、静态分析与回归验证"
  - "Finding all the bugs!：400+ validation locations 与高严重度问题"
  - "But what if there are no bugs?：Lean 模型与 95 个 machine-checked proofs"
  - "Why we couldn’t have done this two years ago：Agent 改变探索性工具经济学"
---

# Auditing in the age of (good enough) AI

## 编译摘要

### 1. 浓缩

- **核心结论 1：Agent 对安全审计的最大增量不只是“自动看代码”，而是把原本不值得投入的专用工具和形式模型变成可负担的前置基础设施。**
  - 关键证据：Trail of Bits 在 Miden zkVM 审计前约六个月，用 Agent 从零构建 MASM LSP、decompiler、静态分析引擎和 Lean VM executor；这些工具后来直接进入人工与 Agent 审计流程。
- **核心结论 2：可信收益来自 Agent 生成与确定性/形式化验证的组合，而不是依赖 Agent 自己判断正确。**
  - 关键证据：decompiler 只覆盖可正确反编译的子集，并用随机 procedure 回归；抽象解释器承担确定性数据流检查；Lean kernel 验证 Agent 生成证明，人工重点审 theorem statement 是否证明了正确性质。
- **核心结论 3：Agent 降低的是探索失败成本，因此扩大了“值得尝试”的工程空间。**
  - 关键证据：作者明确说这类副项目一两年前难以向客户出售，因为 payoff 不确定；现在失败副项目主要消耗 tokens。最终工具发现 400+ 个 type-validation 位置、1 个高严重度问题，Lean 产生 95 个 correctness proofs，并额外发现两个单测遗漏的 bug。

### 2. 质疑

- **关于工具收益的质疑**：这是单个高保证 cryptographic VM 项目的成功复盘，团队本身具备强安全与形式化能力，不能直接推出普通团队复制同样工具链也会获得同等收益。
- **关于“good enough AI”的质疑**：Agent 能生成大量工具代码，不意味着这些工具天然可信；案例中恰恰依赖限制 decompiler 支持范围、回归测试、抽象解释和 Lean kernel 才把“够用”转成可审计结果。
- **关于经济性的质疑**：文章没有披露 token/算力成本、人工监督时长、工具维护成本或与“直接增加人工审计时间”的对照，因此只能支持“探索边际成本下降”，不能量化 ROI。
- **关于因果归因的质疑**：高严重度发现来自 Agent 构建的分析基础设施与专业审计方法共同作用；不能归因为单一模型能力。

### 3. 对标与约束

- **与 [[Agent-Verification]] 对标**：该案例把“验证 Agent 输出”推进到“用 Agent 建 verifier，再让 verifier 约束后续 Agent/人工工作”。验证器依旧必须依靠 deterministic semantics、regression oracle 或 proof kernel，而不是让生成者自证。
- **与 [[Verifiable-Agent-Engineering]] 对标**：可规模化的部分不是无限自主，而是把 MASM 的隐式栈语义转成 IR、抽象解释和可检查 theorem，扩大了可验证边界。
- **硬约束**：cryptographic correctness、type invariants、proof kernel semantics 不因 AI 变便宜而放松。
- **软约束**：是否值得提前构建工具取决于项目期限、复用机会和团队专业能力；Agent 主要改变这一投资决策的成本曲线。
- **综合判断**：Agentic Engineering 的一个高价值模式是“先自动化认知基础设施，再自动化任务本身”；当领域缺少工具时，最优投入可能不是直接让 Agent 审代码，而是先让 Agent 把问题变得更可观察、更可分析、更可证明。

## 证据边界

- 这是 Trail of Bits 自身项目复盘，核心数字与效果主要由项目方报告，证据强度定为 medium。
- 400+ validation locations 不等于 400+ security vulnerabilities；文章明确区分其中绝大多数为 validation 改进点，另有一个高严重度问题。
- “failed side project only costs tokens”是作者对经济性的概括，不应解释为人工监督、维护和机会成本为零。

## 关联概念

- [[Agent-Verification]]
- [[Verifiable-Agent-Engineering]]
- [[Agentic-Engineering]]
- [[Cybersecurity-Proof-of-Work]]
