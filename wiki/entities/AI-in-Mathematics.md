---
type: entity
title: AI in Mathematics
aliases:
  - AI数学
  - 数学AI
definition: "AI在数学领域的应用与进展，包括自动定理证明、问题求解、概念发现等，被认为是AI能力的前沿指标"
created: 2026-07-01
updated: 2026-10-20
evidence_level: medium
claim_type: mixed
tags:
  - AI-capabilities
  - mathematics
related_entities:
  - '[[Conceptual-Breakthroughs]]'
  - '[[Grindability-vs-Verifiability]]'
  - '[[Autoregressive-Generation]]'
  - '[[Scientific-Discovery-AI]]'
  - '[[Human-Curation]]'
source_raw:
  - '[[20260701-grant-sanderson-ai-math-future]]'
  - '[[20260801-lean-kernel-soundness-bug-postmortem]]'
  - '[[20261002-meta-solving-open-research-problems-together]]'
---

# AI in Mathematics

> [!definition] 定义
> **AI in Mathematics** 指AI在数学领域的应用与进展，包括自动定理证明、问题求解、概念发现、证明验证等。数学被认为是AI能力的前沿指标，因为其高度可验证性和结构化特性。

## 核心要点

### AI在数学中的进展速度

数学是AI进展最快的领域之一。Grant Sanderson指出，AI在数学中的进展是其他领域的预演——数学中的成功模式将预示AI在其他领域的发展。

### AI擅长的数学领域

- **几何**：AI可以在19秒内解决IMO几何问题（AlphaGeometry）
- **数论**：AI可以找到Erdős问题的反例
- **代数**：AI可以处理多项式求解问题

### AI在数学中的局限

- **组合数学**：需要更多创造性思维，AI仍面临挑战
- **概念突破**：AI难以产生需要跨领域连接的"闪电般的想法"
- **可磨性依赖**：AI在数学中的成功依赖于问题的可磨性（可并行化、可容器化）

### 数学作为AI能力的试金石

Grant Sanderson认为，数学是观察超级智能的第一个领域。AI在数学中的进展模式将揭示：
1. AI如何处理需要创造性思维的任务
2. AI如何连接不同领域的知识
3. AI如何产生新的概念和理论

## 关键数据点

- AlphaGeometry在2024年IMO中解决几何问题仅需19秒
- AI在2024年IMO中差点获得金牌（因组合数学问题失分）
- OpenAI模型找到了单位距离问题猜想的反例
- Montgomery-Dyson在IAS的午餐对话揭示了随机矩阵理论与Riemann假设的联系
- **AI 双重角色：exploit 生产者 × 验证器审计者**（2026-08 Lean kernel 事后分析）：AI 辅助产出的 Collatz "反证"精准利用了 Lean kernel 与 nanoda 检查器各自的实现缺陷（两个不相关 bug 对齐），同时骗过两端——AI 生成的验证级产物开始压力测试*验证基础设施本身*；同一事件中 OpenAI 的 cybersecurity 专用 AI 又反向找出 Lean kernel 的更多编程错误。数学前沿的攻防两端同时加速（[[20260801-lean-kernel-soundness-bug-postmortem]]，验证独立性分析见 [[Agent-Verification]] 形式验证镜像节）。

## 从竞赛 benchmark 到开放研究协作（Meta Muse Spark，2026-10）

[[20261002-meta-solving-open-research-problems-together]] 把 AI 数学能力从“已有标准答案的高难竞赛题”推进到一个不同的评价对象：**没有 answer key、允许失败回退、需要处理 prior art 与研究信用的开放问题**。Meta 报告数学家使用 Muse Spark 1.1/1.2 Thinking Mode，通过普通 meta.ai chat、无 custom research scaffold 合作形成六篇论文，并称其中五篇回答此前开放的研究问题。

这组案例的重要增量不是“模型独立做数学”，而是 AI 在 research workflow 中承担了多种不同功能：

- proof calculation / argument revision；
- 生成 GAP 搜索程序并寻找 counterexample；
- probabilistic reframing 与 proof strategy exploration；
- 跨 number theory / p-adic string theory 的 connection proposal；
- candidate proof 与 technical-section drafting。

与此同时，人类仍承担 problem selection、关键 proof idea、错误修订、结果验证、prior-art / concurrent-work 处理和最终论文责任。Meta 还要求第二组数学家复核，并在论文中标注哪些段落主要由研究者或 AI 起草。

**判断**：当 AI 进入开放数学研究后，合理的能力单位从 `model → answer` 转向 **`human-AI research system → auditable research artifact`**。最终 theorem/counterexample 仍然重要，但 provenance trace——谁选问题、谁提出关键 idea、谁写搜索程序、谁验证、谁修正、是否独立 concurrent discovery——开始成为评价不可缺失的一部分。

- **证据**：[[20261002-meta-solving-open-research-problems-together]]；来源逐项描述六个合作案例及统一 collaboration principles。
- **边界**：这是 Meta 对自身合作项目的官方总结，没有公开失败项目 denominator、human-only baseline、interaction/compute cost，也不是六篇论文的独立 correctness audit。它支持“AI 已在专家主导的开放数学研究中产生论文级贡献”，不足以证明自主数学研究已解决。

这也与 [[20260918-terence-tao-if-math-more-than-proof]] 的边界一致：**生成 proof artifact 与产生可被共同体理解、检查和继续构建的数学知识不是同一件事。** Meta 明确把目标写成帮助研究者发展他人可以理解和 build on 的 insight，并保留复核、起草 attribution 和 prior-work provenance；这些治理动作本身就是从 demo 进入 science 的组成部分。

## 前提与局限性

- **前提**：数学的可验证性使其成为AI进展的理想测试场
- **前提**：AI在数学中的成功依赖于问题的可磨性（可并行化）
- **局限**：概念突破的验证循环可能长达一个世纪（如Galois理论）
- **局限**：自回归生成方式难以产生跨领域的"闪电般连接"

## 关联概念

- [[Conceptual-Breakthroughs]] — AI在数学中的核心挑战是产生概念突破
- [[Grindability-vs-Verifiability]] — AI在数学中的成功依赖于可磨性而非可验证性
- [[Autoregressive-Generation]] — 自回归方式的局限性影响AI的数学能力
- [[Scientific-Discovery-AI]] — 数学中的AI进展预示科学发现领域的AI应用

## 来源

- [[20260701-grant-sanderson-ai-math-future]] — Grant Sanderson与Dwarkesh Patel的播客访谈