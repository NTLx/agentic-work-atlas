---
type: source-summary
title: "Solving a 31-year-old grand challenge in mathematics – the KLS conjecture"
canonical_url: "https://www.microsoft.com/en-us/research/blog/solving-a-31-year-old-grand-challenge-in-mathematics-the-kls-conjecture/"
raw_state: index
original_raw_file: "20261021-microsoft-kls-human-ai-math.md"
original_body_sha256: "5c8f9e96063bb1bfc3f1a0a8b3810c3922e5e2f1195545bf06c2f3fb7b10440d"
indexed_at: "2026-10-22T09:55:17+08:00"
created: 2026-10-22
updated: 2026-10-22
tags:
  - source-summary
  - mathematics
  - human-ai-collaboration
  - verification
evidence_level: high
claim_type: mixed
source_locator: "正文：At a glance；Technical details；Independent confirmation；Human-AI guidance；Conclusion。"
---

# Solving a 31-year-old grand challenge in mathematics – the KLS conjecture

## 编译摘要

### 1. 浓缩

- **核心结论 1**：Xinzhi Zhang 与合作者给出了 Kannan–Lovász–Simonovits（KLS）猜想的常数界证明，解决了一个 1995 年提出的高维几何/概率核心问题。关键数学推进是先得到新的 criterion，再利用 recursive refinement 将维度依赖从缓慢增长最终压到 universal constant。
- **核心结论 2**：AI 的作用不是一次 end-to-end 自动求解。研究者把一个候选方向扩展成多条并行 trajectory，让 Agent 做高阶 tensor 计算、推导和候选探索；研究者反复查看中间结果、剪掉无望分支，并把最有希望的结果传入下一轮。整体探索超过 100 个候选方法。
- **核心结论 3**：来源提供了一个非常有价值的对照：团队还用多个领先模型做了反复 unguided solve attempts，并给了与主流程大致相同的总 token budget，但没有成功。最终突破依赖“模型搜索能力 × 人类数学 judgment × iterative pruning”，而不是单纯更多 token。
- **核心结论 4**：验证链超出了作者自身 proof checking：完整证明发布同日出现另一组专家的独立完整证明，第三个证明也使用 closely related idea；随后又出现 Lean 4 formalization。也就是说 correctness evidence 同时包含独立人类推导与 machine-checked formalization。

### 2. 质疑

- Microsoft Research Blog 是研究机构对自家成果的官方叙述，AI 使用细节和 token-budget 对照不是独立实验报告；“roughly same total token budget”也不足以排除 prompt、search policy、researcher intervention timing 等变量。
- “100+ trajectories”说明 search breadth，不代表这些 trajectory 统计独立，也不能推出固定的人机 pruning recipe 对其他数学问题同样有效。
- 独立证明和 Lean formalization显著增强 correctness confidence，但不能回答“AI 对最终关键思想贡献多少”这一归因问题；来源明确把 recursive method、反复应用和 error accumulation proof 归为研究者的原创贡献。

### 3. 对标与约束

- **与 [[AI-in-Mathematics]] 的连接**：这篇把 Meta Muse Spark 的“专家主导开放研究协作”进一步推进为带有明确 counterfactual 的案例：相近 token budget 的 unguided AI 失败，而 human-directed branching/pruning 成功。
- **与 [[Human-Curation]] 的连接**：人类价值不只是最终 proof review，而是在搜索过程中持续做 branch selection、识别有希望的局部结构、把 partial insight 连接到已有方法。
- **与 [[Agent-Verification]] 的连接**：独立 proof 与 Lean formalization 是两种不同 oracle；它们不是让原始生成器自证正确，而是引入不同推理链和形式化检查器，降低共源错误风险。
- **硬边界**：数学可验证性很强，但“知道哪个中间 criterion 值得递归推进”仍是 search policy / taste 问题，当前不能被 proof checker 直接替代。

## 关联概念

- [[AI-in-Mathematics]]
- [[Human-Curation]]
- [[Agent-Verification]]
- [[Mathematical-Canonicalization]]
