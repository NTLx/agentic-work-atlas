---
type: source-summary
title: "1Password's AI patching benchmark is misleading"
source_raw:
  - "[[20260915-trail-of-bits-1password-ai-patching-benchmark]]"
canonical_url: "https://blog.trailofbits.com/2026/09/15/1passwords-ai-patching-benchmark-is-misleading/"
raw_state: full
created: 2026-09-18
updated: 2026-09-18
tags:
  - source-summary
  - agent-verification
  - agent-security
  - benchmarks
  - code-review
evidence_level: medium
claim_type: mixed
---

# 1Password's AI patching benchmark is misleading

> 来源性质：Trail of Bits 对 1Password FLAWED 报告的技术批评，同时给出自己的咨询记录和 Patch the Planet 数据。它是冲突中的一方，不能被当作无偏裁判，但提供了可复核的口径拆解和替代测量原则。

## 编译摘要

### 1. 浓缩

- **核心结论 1：补丁基准的总成功率高度依赖样本、提示、工具权限和评分规则。**
  - 关键证据：Trail of Bits 指出 1Password 的 26% clean-fix headline 混合了六个特意挑选的困难漏洞、占数据 22% 的“应用错误修复”提示、占 36% 的禁止构建/测试运行，以及不同模型的 reasoning settings。
- **核心结论 2：能阻断 supplied exploit 不等于完成安全修复，反过来，不能运行测试也不应被当成失败证据。**
  - 关键证据：在允许测试且没有错误提示的子集里，2,634/3,067 个模型生成补丁（86%）阻断了 supplied exploit；作者明确说这仍不能证明完整修复。其 post-patch-validation skill 要求复现原始 bug、测试另一条根因路径、检查回归/新漏洞，并把 broken test run 记为 inconclusive。
- **核心结论 3：人类和 Agent 都会漏掉“修复之后才出现”的路径，比较双方必须使用同一任务和工作条件。**
  - 关键证据：Trail of Bits 对 2024–2026 年 2,265 个漏洞的首个开发者修复中发现 283 个未完全解决，失败率 12.5%；在 freenginx 案例中，Agent 指导的补丁和维护者的独立补丁都漏掉了超时清理路径并引入同一崩溃。

### 2. 质疑

- **关于反批评的质疑**：Trail of Bits 的 86%、12.5% 和 Patch the Planet 接受率来自其自身项目，样本、任务分配、工程师参与和维护者标准可能与普通团队不同。
- **关于接受率的质疑**：186 个已关闭或合并的 Patch the Planet PR 中，126 个被合并（67.7%），其中 91 个保留了原始安全修复；合并不等于正确，作者也明确提醒不能把 maintainer acceptance 当作 correctness。
- **关于人机可比性的质疑**：开发者数据是“有详细漏洞报告且知道会被复核”的有利条件，Agent 数据则是工程师指导的公开项目补丁；两者仍不是严格的 matched experiment。
- **关于评分器的质疑**：文章指出模型裁判与人类在五类总结果上的一致率只有 65.9%，同一补丁由两个模型得到不同结论的比例为 36.8%；评分器本身必须成为被验证对象。
- **关于口径冲突的质疑**：1Password 的 26% 是在特定实验混合条件下的 clean-fix，Trail of Bits 的 86% 是子集里的 exploit blocking；二者不是同一分母或同一正确性定义，不能直接互相“证伪”。

### 3. 对标

- **与 Agent Verification 对标**：[[Agent-Verification]] 的核心原则“通过测试不等于正确”在安全补丁中被具体化为多路径复现、回归测试、sanitizer/fuzzing 和不确定结果保留。
- **与 Agent PR Review 对标**：[[Agent-PR-Review]] 的“关键路径、边界条件、测试是否真的失败过”检查点，正好对应 post-patch-validation 的四步。
- **与评测集对标**：[[Evaluation-Set]] 和 [[Minimal-Pair-Evaluation]] 提示，基准需要把研究问题、工作条件、验证器、重复次数和逐漏洞方差分开记录。
- **跨域迁移**：高风险 Agent 评测应从“模型一次生成是否通过”改为“人/机在相同条件下，修复—验证—复核—后续回归的总成本与残余风险是多少”。

## 冲突与口径

| 来源 | 表面结论 | 不可直接比较的前提 |
|------|---------|-------------------|
| 1Password FLAWED 报告（Trail of Bits 转述） | 混合条件下 clean fix 仅 26% | 困难样本、错误修复提示、禁用测试、不同 reasoning settings |
| Trail of Bits 子集重分析 | 2,634/3,067（86%）阻断 supplied exploit | 允许测试、排除错误修复提示，且 exploit blocking 不是 complete fix |
| Trail of Bits 开发者记录 | 首个修复 12.5% 未完全解决 | 有详细报告、知道会被审查、项目与任务不随机 |

> [!warning] 这些数字回答不同问题。应先固定研究问题和工作条件，再决定指标与分母。

## 前提与局限性

本文适合作为“如何审查 Agent benchmark”的一手批评和验证方法清单；其自有成效数据仍是单一机构的项目记录，不能独立证明 Agent 已经或没有超过人类。

## 关联概念

- [[Agent-Verification]]
- [[Agent-PR-Review]]
- [[Evaluation-Set]]
- [[Minimal-Pair-Evaluation]]

