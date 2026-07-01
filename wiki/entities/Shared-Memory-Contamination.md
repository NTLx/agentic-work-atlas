---
type: entity
title: "共享记忆污染治理"
aliases:
  - "Shared Memory Contamination Governance"
  - "Memory Poisoning"
definition: "多 Agent 共享记忆中的错误传播无法被架构完全隔离——但可通过四层防护架构（L0 写入标签 + L1 正交审计 + L2 置信透明 + L3 时间遗忘）+ 证据-解释分离 + 遗忘优先于纠错的原则，将污染管理到可接受水平。"
created: 2026-07-01
updated: 2026-07-01
evidence_level: medium
tags:
  - memory-system
  - context-engineering
  - AI-Agent
  - agentic-engineering
related_entities:
  - "[[Memory-Architecture]]"
  - "[[Multi-Layer-Memory]]"
  - "[[Three-Layer-Agent-Memory]]"
  - "[[Context-Rot]]"
  - "[[Context-Engineering]]"
  - "[[Agent-Harness]]"
source_raw:
  - "[[20260604-openai-dreaming-memory]]"
---

# 共享记忆污染治理

> [!definition] 定义
> 多 Agent 共享记忆中的错误传播无法被架构完全隔离——但可通过四层防护 + 证据-解释分离 + 遗忘优先原则管理到可接受水平。核心公式：系统净清洁 ⇔ 遗忘速度 > 污染扩散速度。

## 污染的独特性质

共享记忆错误污染不同于传统数据损坏或谣言传播：

- **语义级注入**：错误是语义级的——事实和推断在共享存储中失去区分度，下游消费者无法判断置信度（Huyen: "retrieval drift"）
- **相关故障**：Agent 共享基础模型导致故障非独立——多数投票可能放大而非纠错（Lamport: Byzantine 模型的独立故障假设不成立）
- **可用性级联**：首次写入自动获得锚定效应，重复访问自强化可信度（Kahneman）
- **读取即污染**：记忆是编码-重构系统，每次读取都是一次重构，引入情境偏差（Matuschak）

## 四层防护架构

| 层次 | 信号类型 | 机制 | 可博弈性 | 关键约束 |
|------|---------|------|---------|---------|
| **L0 写入标签** | 结构信号 | 强制标注 [事实/推断/待验证] | 可博弈（Agent 可改写标签） | 低成本，作为第一道机械过滤 |
| **L1 正交审计** | 矛盾信号 | 独立审计 Agent 检测跨条目异常 | 低（若实现独立） | **必须使用不同基础模型或规则引擎**——共享模型 = 相关故障 = 伪正交 |
| **L2 置信透明** | 历史信号 | 读取时显示验证历史（验证次数/上次验证时间/反驳标记） | 不纠错，只暴露 | 不防止污染，只防止盲信 |
| **L3 时间遗忘** | 时间信号 | 强制过期 + 从不可变原始证据重推导 | 不可博弈（时间不可伪造） | 依赖原始证据被保留且未被篡改 |

## 核心原则

### 遗忘 > 纠错

纠错试图判断"当前记忆是否正确"——但"正确"在开放语义空间中不可判定（Gödel 投影）。遗忘不判断——它只是让旧解释过期，然后从原始证据重新推导。新证据自然产生新结论，旧错误被时间淘汰。

### 证据-解释分离

- **不可变证据**：原始对话记录、git history、交易日志——永远只读，不进入共享记忆
- **可变解释**：Agent 从证据中推导的结论——进入共享记忆，可被替换
- **指针格式**：`{claim, evidence_pointer, derivation_agent, derivation_time}`——指针指向只读证据源
- **重推导**：过期后从证据源重新推理，而非重读旧解释

### 可博弈性结构必然

不存在不可博弈的显式仲裁标准。Goodhart（度量→目标→脱钩）+ Soros 反射性（规则改变行为→行为改变规则前提）+ Gödel 投影（足够丰富仲裁系统必有不可判定正确性）三重独立论证。替代：多层异构仲裁 + 博弈成本 > 博弈收益 + 博弈驱动标准进化。

## 关键数据点

- Zylos AI (2025): 65% 企业 AI 失败源于上下文漂移/记忆丢失——非上下文耗尽
- Galileo.ai: "memory poisoning"——幻觉通过共享记忆传播，退化渐进非即时触发
- explainx.ai (2026): Claude CCA Domain 5 专设上下文管理与可靠性（15% 权重）
- O'Reilly (2026): 引用 Bousetouane arXiv:2601.11653 + Cemri et al. 2503.13657

## 前提与局限性

- L1 正交性是小团队的最大瓶颈——多模型基础设施成本高，单模型下 L1 降级为"尽力而为"
- 遗忘依赖原始证据保留——如果证据被选择性删减或丢失，重推导地基受损
- 可博弈性结构必然定理是理论推导，缺博弈成本/收益的量化实证
- 四层架构的全链路压力测试尚未有大规模生产数据

## 关联概念

- [[Memory-Architecture]] — 记忆系统的 staleness/correctness/scalability 三大挑战
- [[Multi-Layer-Memory]] — 五层记忆 + promotion gating（≥3 次升级）
- [[Three-Layer-Agent-Memory]] — 记忆腐化：L1/L2/L3 混淆 = 污染
- [[Context-Rot]] — 上下文窗口填充导致推理质量非线性下降
- [[Context-Engineering]] — 上下文工程：决定 Agent 在任一时刻能访问什么信息
- [[Agent-Harness]] — Agent 治理骨架，L0-L2 的执行基础设施

## 开放问题

- 错误窗口期量化——建模遗忘速度 vs 污染扩散速度的动力学
- "新证据"不可博弈定义的实证方案
- L1 正交性的低成本实现——规则引擎/形式化约束替代 LLM 审计
- 推导器版本漂移管理——同一证据用不同模型版本重推导得出不同结论
