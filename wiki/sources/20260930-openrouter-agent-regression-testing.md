---
type: source-summary
title: "AI Agent Regression Testing After a Prompt or Model Change"
canonical_url: "https://openrouter.ai/blog/tutorials/ai-agent-regression-testing-after-a-prompt-or-model-change/"
source_raw:
  - "[[20260930-openrouter-agent-regression-testing]]"
raw_state: index
created: 2026-10-12
updated: 2026-10-12
tags:
  - source-summary
  - agent-evaluation
  - regression-testing
  - agent-verification
evidence_level: medium
claim_type: mixed
source_locator:
  - "TL;DR and locked case set"
  - "Three kinds of change that need a regression run"
  - "Test across a model swap"
  - "Separate a regression from noise"
  - "Frequently asked questions"
  - "Conclusion"
---

# AI Agent Regression Testing After a Prompt or Model Change

> OpenRouter 面向 Agent 行为回归测试的工程教程。其稳定贡献不是某两个模型的价格/结果，而是把“Agent 变更”视为一个多变量实验：prompt、model、tool schema、retrieval/context、harness instruction 与 inference configuration 都可能改变行为，因此回归测试必须锁定 case set 与 execution envelope，并把结构性行为和 hard invariants 写成可运行契约。

## 1. 浓缩

### 1.1 Agent 的“代码版本”不足以定义被测系统

传统软件里，一个 commit 往往足以定位实现版本；Agent 系统不是这样。来源列出三类会触发行为变化的修改：

1. system prompt 的一行文字；
2. model swap / alias 背后的 checkpoint 更新；
3. tool schema、retrieval setting、conversation history 等上下文变化。

可以把 Agent behavior surface 抽象为：

```text
Behavior
= f(prompt,
    concrete model/provider,
    tool schema + tool results,
    retrieval/context,
    harness + implicit instructions,
    inference parameters)
```

**判断**：旧版本“测试通过”的对象不是单纯 prompt 或代码，而是整个 execution envelope。上述任一变量变化，旧 pass 都需要重新证明。

尤其 retrieval/context 的回归最隐蔽：输出仍可能非常流畅，但依赖的 policy 段落因为 chunking、history 或 tool response 变化而不再进入模型可见上下文。

### 1.2 Locked case set 是因果可比性的前提

来源明确要求锁定 case set：如果候选版本测试过程中顺便重写 case，就同时改变了 treatment 与 measurement，历史比较失去意义。

```text
baseline system ─┐
                 ├─ same locked cases → comparable evidence
candidate system ─┘
```

**判断**：评测 case 的编辑应被当作 schema migration / new experiment boundary，而不是无害的测试维护。单次 regression comparison 中，dataset 本身必须是 controlled variable。

这与 production-derived Golden Set 的长期演化并不冲突：

```text
between product epochs:
  refresh / version the eval set

within one regression experiment:
  freeze that exact eval-set version
```

### 1.3 行为回归不等于字符串 diff：contract 应区分 structure、outcome 与 invariant

两个正确的 Agent response 很少逐字一致。因此来源把 case contract 拆向结构行为：调用了哪个 tool、参数是什么、顺序/必需信息是否满足，以及 policy 是否被突破。

更稳定的三层结构是：

```text
behavioral contract
  ├─ outcome/rubric: 最终行为是否满足任务目标
  ├─ structural assertion: 只有路径本身属于需求时才检查 tool/action structure
  └─ hard invariant: 永远不能破的政策/安全边界
```

**判断**：structural assertion 不能无限扩张。若产品只关心最终结果，就不应把某一条 tool path 偶然固化成“正确答案”；只有当工具选择、审批顺序、升级动作本身属于 contract 时才适合做结构断言。这与既有 [[Evaluation-Set]] 中“除非路径本身是需求，否则评最终目的”的原则一致。

Hard invariant 则不同：退款上限、必须升级人工等边界不适合和 stylistic judge score 放在同一容错阈值里。candidate-only invariant break 应直接视为 release defect。

### 1.4 Baseline-before-candidate：共享失败首先审查测试系统

来源的实践有一个很重要的 verifier discipline：先确认 baseline 在当前 harness 中仍通过，再评价 candidate。如果 baseline 与 candidate 同时在同一个 case 失败，优先调查 harness、case、judge 或 environment。

```text
baseline fail + candidate fail
        ↓
first suspect evaluator / harness / environment
        ≠
automatically candidate regression
```

教程最后甚至指出，其测试过程没有发现候选模型的问题，却发现了自身 harness 的两个问题。

**判断**：回归测试不是一个永远正确的裁判。它本身也需要 health check，而 baseline replay 是最便宜的 evaluator self-test 之一。

### 1.5 Model alias 会让实验在没有 commit 的情况下漂移

来源特别指出 `latest` / family alias 对生产使用方便，却与严格可复现回归存在张力：同一个配置字符串可能在不同时间指向不同 concrete model。

因此 provenance 至少要记录：

- requested model identifier；
- actual concrete served model/version；
- provider（需要时）；
- supported/used inference parameters。

**判断**：如果一个外部依赖可以在 Git 不变时改变 Agent 行为，就必须把它纳入 regression trigger 或定时重跑。否则仓库 history 无法解释 production behavior 的变化。

### 1.6 Hermetic run 的对象还包括“隐式上下文”

Agent coding/runtime 环境中，`AGENTS.md`、`CLAUDE.md`、skills、workspace instructions 等文件会成为模型行为的一部分，但常常不在测试作者显式列出的变量里。

**判断**：Agent regression 的 hermeticity 不只意味着固定 API 参数，还意味着**披露/隔离所有会进入上下文的隐式 instruction sources**。否则一次看似模型回归的变化，可能只是运行目录里多了一份 instruction file。

### 1.7 Soft score 与 hard invariant 需要不同 release policy

来源承认 LLM judge 会漂移、有偏好，单个 borderline failure 不应机械成为 release blocker；应使用 rerun、threshold 与噪声政策。

但 hard invariant 不是统计平均项：

```text
soft quality drift
  → threshold / rerun / investigate

hard invariant violation
  → zero-tolerance candidate defect
```

**判断**：把所有 eval 都压成一个 aggregate pass rate 会掩盖 contract 的风险层级。回归报告至少应把 hard policy defects 与 noisy quality scores 分开。

## 2. 对现有知识的增量

### 对 [[Agent-Verification]]

本文把“验证 Agent 输出”推进到“控制一个 Agent behavior experiment”。测试证据只有在 execution envelope 被固定/记录时才有因果意义：

```text
locked cases
+ pinned prompt
+ concrete model/provider
+ fixed tools/schema/results
+ fixed retrieval/context
+ fixed judge
+ explicit inference params
+ disclosed implicit instructions
→ baseline vs candidate
```

### 对 [[Evaluation-Set]]

Golden Set 需要随 production drift 长期演化；Regression Set 在一次 comparison 内必须冻结。两者描述的是同一资产在不同时间尺度上的治理：**版本间可以更新，版本内不可漂移。**

这使“评测集版本”本身成为实验边界。修改 case 后不应继续把新结果与旧 baseline 当成同一测试条件。

## 3. 证据边界

- 这是 OpenRouter/Ori Eval 导向的厂商教程，不是跨框架对照研究。
- 教程中的具体模型、价格、provider 数量和一次 model-swap 结果是时间敏感示例，不进入稳定知识结论。
- Structural assertions 容易 overfit harness 实现；只有路径本身属于业务契约时才应强制。
- LLM judge 的阈值和 rerun 策略需要按任务风险与方差校准，来源没有提供普遍适用的统计门槛。
- “baseline 通过”也不证明 harness 正确；它只是一种强有用的 sanity check。若 baseline 与 harness 同时共源错误，仍需独立 oracle/人工审计。
- pin concrete model 可以提高可复现性，但 provider runtime、依赖服务和未显式记录的后端变化仍可能造成漂移。

## 4. 关联概念

- [[Agent-Verification]]
- [[Evaluation-Set]]
- [[Rubric-Based-Evaluation]]
- [[Evaluator-Miscalibration]]
- [[Agent-Harness]]
