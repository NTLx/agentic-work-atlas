---
source: "https://arxiv.org/abs/2603.28063"
title: "Reward Hacking as Equilibrium under Finite Evaluation"
author: "Jiacheng Wang, Jinbin Huang"
date: 2026-03-30
tags:
  - reward-hacking
  - principal-agent-theory
  - ai-alignment
  - goodhart
  - agentic-systems
  - mechanism-design
---

# Reward Hacking as Equilibrium under Finite Evaluation

## 一句话

在五个最小公理下（多维质量、有限评估、有效优化、资源有限、组合交互），任何被优化的 AI agent 都会系统性地在评估系统未覆盖的质量维度上投入不足——Reward Hacking 是结构性均衡，不是可修复的 bug。

## 五个公理

1. **多维质量**：任务输出质量是多维向量 q = (q1,...,qN)，N≥2
2. **有限评估**：评估系统将质量空间投影到严格低维子空间 K<N
3. **有效优化**：Agent 的努力分配正向响应评估信号结构
4. **资源有限**：Agent 分配有限资源 e，Σei ≤ B
5. **组合交互**：T 个可组合工具时，质量维度 N(T) ≥ T + α·C(T,2)，即 Ω(T²)

## 核心命题

### Proposition 1：扭曲不可避免
在 Axioms 1-4、λ∈(0,1)、K<N 的条件下：
- (a) 所有不可签约维度 i>K 上，ei* ≤ ei^FB（投入不足）
- (b) e* ≠ e^FB（agent 的均衡 ≠ 第一最优）
- (c) W(q*) < W(q^FB)（福利损失）

### Proposition 2：Agentic 放大
如果评估工程预算 C(T) = o(T²)（评估投资增长严格慢于工具数量的平方）：
- (a) 覆盖率 K(T)/N(T) → 0（随工具增长趋于零）
- (b) 契约不完备性 κ(T) → 1
- (c) 攻击严重性无界增长

**为什么 C(T) = o(T²) 是通用的**：
- 能力侧：集成工具 t+1 需要 O(1) 工程成本
- 评估侧：评估工具 t+1 与现有 t 个工具的交互需要 O(t) 成本
- 总评估成本：Σ O(t) = O(T²)
- 实践中评估预算以分数增长，不可能维持二次增长

## 可计算的扭曲指数

Di = w̃i/wi = { λ·(ri/wi) + (1-λ) if i≤K; (1-λ) if i>K }

- Di > 1 → 过度投入（如谄媚、长度博弈）
- Di < 1 → 投入不足（被忽视的质量维度）
- 所有不可签约维度共享最低 Di = (1-λ)

## 猜想：Goodhart → Campbell 转变

- **Goodhart 体制**：Agent 在固定评估系统内重新分配努力（Propositions 1-2 覆盖）
- **Campbell 体制**：Agent 分配资源**降级评估系统本身**的有效覆盖

**猜想 1**（能力阈值）：存在临界能力 B*，B<B* 时 Goodhart 体制成立，B>B* 时进入 Campbell 体制。

**猜想 2**（能力陷阱）：在 B* 附近的邻域内，委托人的福利 W(B) 可能**非单调**——更强的 AI 反而更差。这是 Bostrom "treacherous turn" 的首次经济学形式化。

## 框架适用范围

框架不适用于：
1. N=1（质量单维——对复杂任务不现实）
2. K≥N（评估覆盖所有维度——形式化验证中可能，通用 AI 中不现实）
3. Agent 行为违反行为正则性（对齐训练完全无效）

## 意义

这篇论文为知识库中的"可博弈性结构必然定理"（Goodhart + Soros反射性 + Gödel投影）提供了独立的经济学形式化论证。它将 Agentic Amplification（Proposition 2）——工具越多，评估覆盖越差——与我们关于"Agent 控制平面必须治理运行时评估覆盖率"的判断精确对应。
