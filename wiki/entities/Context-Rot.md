---
type: entity
title: Context Rot
aliases:
  - 上下文腐烂
  - context rot
definition: "随着上下文窗口逐渐填充，LLM 的推理、指令遵循和任务完成能力逐渐下降的现象，特别是关键信号落在窗口中间位置时表现最差。"
created: 2026-06-10
updated: 2026-07-10
evidence_level: medium  # 理论框架完整，C*量化值待校准
claim_type: mixed
tags:
  - LLM
  - context-engineering
related_entities:
  - "[[Agent-Harness]]"
  - "[[Context-Engineering]]"
  - "[[Token-Efficiency]]"
source_raw:
  - "[[20260419-agent-harness-engineering]]"
  - "[[The Anatomy of an Agent Harness]]"
  - "[[20260702-anthropic-context-engineering]]"
  - "[[20260708-bun-in-rust]]"
  - "[[20260708-agent-loop-bytebytego]]"
  - "[[20260708-vercel-agent]]"
---

# Context Rot（上下文腐烂）

> [!definition] 定义
> **Context Rot** 指的是随着上下文窗口（Context Window）的填充，模型对信息的处理质量非线性下降的现象。这种现象不仅受 Token 总量影响，还受信息分布位置的影响（如 "Lost in the Middle" 效应）。

## 关键数据点
- 关键内容落在窗口中间位置时，模型性能可能下降 30% 以上（Stanford 研究）。

## 本质：不变的设计约束

Context Rot 不是限制（可绕过）也不是问题（可解决），而是**不变的设计约束**——像摩擦力之于机械系统，永远存在、可管理、不可消除。

从自由能原理看，Rot = KL散度(P_actual, P_model)——模型信念分布与真实世界状态分布之间的偏离，关于上下文长度 C 单调递增（dRot/dC > 0）。每个有限上下文窗口的系统在处理超过其容量的信息时必然退化（香农信道容量上限）。

**残余误差下界**：通过冗余（von Neumann 并联冗余）和隔离可将 rot 影响压缩到任意小水平，但存在**不可消除的残余误差下界**，由模型间共享偏差的深度决定（相关性系数 ρ > 0）。同模型多实例共享基础偏差 → ρ > 0；多模型少实例可降低 ρ 但破坏一致性。最优策略 = 关键接口统一(ρ高) + 实现细节多样(ρ低)。来源：07-10 深度思考（roundtable+think+qa）

## 五模式 Anti-Rot 架构

| 模式 | 机制 | 案例 |
|------|------|------|
| 隔离容器 | 将 rot 局限在可丢弃的上下文中 | Bun 的 64 worktree 隔离 |
| 新鲜审查者 | 审查者用全新上下文，不继承执行者历史 | Bun 的 2 reviewer per implementer；L3 对抗审查 |
| 客观信号锚 | 用 rot-proof 工具（编译器/测试）检测 rot | Bun 的 16,000 编译错误作为 rot 信号 |
| 分层熵减 | 每层验证在不同时间尺度捕获 rot 逃逸 | L1(秒)→L2(分钟)→L3(小时)→L4(天) |
| Rot-proof 人类接口 | 人类看结构化摘要，不暴露原始上下文 | Vercel Agent "checkout 500错误，建议回滚" |

违反任何一条 → rot 逃逸概率指数级增长。来源：07-10 深度思考（roundtable+think+qa）

## 双重 Rot 共振（共模故障）

Agent rot 和 human rot 是两种不同的退化：
- **Agent rot** = 信息论退化（上下文填满 → 注意力稀释 → 能力下降）
- **Human rot** = 认知疲劳（AI 依赖 → System 2 关闭 → 意愿下降）

两者同时发生时形成**共模故障**（common-mode failure）：agent 做不好 + 人类不想检查 = 最危险的失败模式。解法 = 多样性冗余：人类不应阅读 agent 的原始上下文（会加速自己的 rot），而应看 rot-proof 的结构化摘要。来源：07-10 深度思考（roundtable+think+qa）

## 与风险分工的关系

双重 rot 共振提出了一个悖论：如果人类也 rot，那"人类不可替代 = 有穷性 = 风险认领"是否被动摇？

**解决**：风险分工的根基不是认知能力（可被 rot 侵蚀），而是**可改变性**（不可被 rot 侵蚀）。有穷性的时间尺度（年~数十年）远长于 rot 周期（分钟~小时）。Rot 让人"不理解"因果链，但不能让人"不被因果链改变"。人类不可替代 = 可被因果链永久改变 = 不可重启。来源：07-10 深度思考（think 六层追本）

## 前提与局限性
- 随着模型架构改进（如线性注意力、更强的长文本模型），rot 的增速可能变慢，但作为设计约束永远存在
- 五模式架构假设任务可被分解为独立子任务；本质不可分解的任务（如长篇小说连贯性）与隔离容器原则存在张力
- 增强陷阱（长期 AI 依赖 → 永久判断力退化）可能使 human rot 从短期波动变为长期结构变化，此时 rot 时间尺度逼近有穷性时间尺度，风险分工质量持续下降

## 长周期 Agent 设计的五条约束（07-17 推导）

从五模式 Anti-Rot 架构和双重 Rot 共振定理推导长周期 agent 的具体设计约束：

1. **最大有效运行时间 ≤ f(隔离容器刷新率)**：agent 不能在同一个上下文中无限运行。将长周期任务分解为独立子任务——每个子任务拥有新鲜上下文。最大连续运行时间 = 上下文被 rot 填满到超过质量阈值的时间。超过则必须强制上下文刷新。
2. **审查者新鲜度 > 执行者新鲜度**："新鲜审查者"模式要求审查者用全新上下文。长周期 agent 必须包含周期性审查者轮换——不能在同一个上下文中既执行又审查。
3. **客观信号锚优先**：编译器/测试框架的输出不随上下文长度退化（rot-proof）。长周期 agent 的**所有**反馈回路必须锚定在客观信号上，不能在 LLM 内部判断上——因为内部判断随上下文退化而 rot。
4. **双重 rot 共振防护**：agent rot + human rot 的共模故障是长周期 agent 的最危险失效模式。不能假设"人类会发现 agent 的 rot 问题"——因为人类也在疲劳退化。必须设计 agent **自主的** rot 检测（客观信号偏离 > 阈值 → 触发降级）和降级策略（暂停/上下文刷新/人工升级）。
5. **最优任务分解粒度**：子任务太小 → 协调成本过高（跨子任务上下文传递的 token 成本）。子任务太大 → rot 在单任务内累积过多。最优分解粒度 = argmin(rot累积损失 + 协调成本)。取决于 rot 累积速率（模型相关）和任务的结构耦合度。

## 关联概念
- [[Agent-Harness]] - Harness 是 anti-rot 架构的载体
- [[Context-Engineering]] - 上下文工程的核心挑战之一是管理 rot
- [[Agentic-Workflow-Token-Efficiency]] - Token 效率与 rot 管理互为约束
- [[Ralph-Loops]] - 长周期 loop 必须内建 anti-rot 机制
- [[Agent-Loops]] - 分层验证(L3 fresh reviewer)是 anti-rot 的关键层
- [[Human-Governor-Agent-Operator]] - Governor 也 rot → 需要 rot-proof 接口
