---
type: entity
title: Proof Indigestion
aliases:
  - Proof Indigestion
  - Proof Abundance
  - Proof Scarcity to Abundance
  - 证明消化不良
definition: "Tao 在 ICM 2026 提出的相变概念——AI 时代从 proof scarcity（生成是瓶颈）转向 proof abundance（消化是瓶颈）；5-stage pipeline（solve/verify/communicate/digest/canonicalize）各阶段速度失配导致结果无法被 community 内化"
created: 2026-08-20
updated: 2026-08-20
tags:
  - knowledge-management
  - ai-capability
  - proof-verification
  - mathematical-research
evidence_level: high
claim_type: extracted
related_entities:
  - "[[Terence-Tao]]"
  - "[[Mathematical-Canonicalization]]"
  - "[[Slopocalypse]]"
  - "[[Goodharts-Law]]"
  - "Theorem Economy Fall（forward reference，未建 entity）"
  - "Validation Pipeline（参考 wiki 中已有 [[Validation-Pipeline]]，fix link）"
  - "[[Knowledge-Compilation]]"
source_raw:
  - "[[20260820-arxiv-2608.16753-mathematics-ai.pdf]]"
---

# Proof Indigestion（证明消化不良）

> [!definition] 定义
> **Proof Indigestion** 是 Terence Tao 在 ICM 2026 演讲中提出的相变概念：**AI 时代从 proof scarcity 转向 proof abundance**——历史上生成是瓶颈（解决新问题稀缺），现在消化是瓶颈（理解、验证、表述、接纳、规范化全链路过载）。5-stage pipeline 各阶段速度失配导致结果无法被 community 内化。

## 5-Stage Pipeline 失配

| Stage | AI 加速 | Community 承载 | 失配模式 |
|-------|---------|----------------|----------|
| **Solve** | 极高（First Proof 7/10） | 低（理解问题） | 生成 > 评估 |
| **Verify** | 高（autoformalization） | 中（形式化检查） | 验证 > 沟通 |
| **Communicate** | 高（语法流畅） | 中（实质理解） | 表述 > 接纳 |
| **Digest & Accept** | 低（人类 referee） | 极高（专家时间） | 接纳 ≪ 生成 |
| **Canonicalize** | 极低（AI 难以融入理论） | 极高（共识建构） | 规范化 ≪ 所有上游 |

**Impedance mismatch**：前 3 阶段 AI 加速，后 2 阶段无法 AI 加速——产生"indigestion"。

## 从 Scarcity 到 Abundance

```
Scarcity Era（pre-AI）：
  Solve (稀缺) → Verify (困难) → Communicate (缓慢) → Accept (慢) → Canonicalize (慢)
  瓶颈：solve。所有上游慢导致下游也慢——pipeline 同步

Abundance Era（post-AI）：
  Solve (AI 加速) → Verify (AI 加速) → Communicate (AI 加速) → Accept (人类瓶颈) → Canonicalize (人类瓶颈)
  瓶颈：accept/canonicalize。前 3 阶段速率远超后 2 阶段——pipeline 异步失配
```

## 4 种 indigestion 模式

Tao 列出 pipeline 各阶段的失配症状：

1. **AI-generated proofs accumulate faster than can be verified**
2. **Verified proofs accumulate faster than can be given readable write-up**
3. **Well-written proofs overwhelm traditional peer review (volunteer labor)**
4. **Even published proofs are too numerous for community to canonicalize**

每种 indigestion 对应一个 stage 与一个 value——Tao 把"失配"重新框架为"哪个 value 被瓶颈"

## 为什么这是"indigestion"而非"abundance"

- **Abundance** 是中性：结果多
- **Indigestion** 是问题：结果多但 community无法内化
- **类比**：食物吃太多无法消化（胃胀），不是好事；结果太多无法消化（社区认知过载），也不是好事
- **解药**：不是减少 generation，而是**增强 digestion 能力**

## 与相关 concept 的关系

- **[[Slopocalypse]]**：Slopocalypse 是 noise flooding；Proof Indigestion 是 structure flooding——两者都是 AI 生成量超载的不同形态
- **[[Goodharts-Law]]**：Proof Indigestion 是 Goodhart 在知识生产域的具体表现——当 proof 数成为 metric，community 误把"数量"当"价值"
- **Theorem Economy Fall（forward reference，未建 entity）**：Bessis/Tao 主张 shift from proof generation to proof digestion——Proof Indigestion 是这一 shift 的实证依据
- **Validation Pipeline（参考 wiki 中已有 [[Validation-Pipeline]]，fix link）**：验证管线是 stage 1-2 的工程化，但 stage 3-5 缺乏等价工程化
- **[[Knowledge-Compilation]]**：canonicalization 是知识编译的最终阶段，Proof Indigestion 揭示这一阶段最稀缺

## 关键数据点

- First Proof 第二批 7/10 通过（2026-05-28 models）
- 每题 compute 成本 tens-hundreds USD
- Erdős problems database 已有 dozens of AI-generated proof submissions
- 多数 AI-generated submissions 无人 expert 验证

## 应对策略（Tao 建议）

1. **Decrease emphasis on proof generation**：减少"first to solve" 奖励
3. **Increase emphasis on proof digestion**：exposition / refereeing / publication / canonicalization
2. **AI tools as filters**：journals 用 AI triage submissions（controversial）
3. **Human referees cannot be removed**：自动过滤 ≠ 替代同行评审
4. **New workflows**：structured problem databases / video journals / negative results venues

## 前提与局限性

- **前提 1**：AI 生成的 proof 量大于 community 消化能力（conditional 在 Working Hypothesis）
- **前提 2**：消化阶段无法用 AI 加速（canonicalize 需 broad consensus）
- **边界**：pipeline 是 problem solving 单维度展开；theory building / teaching 是独立维度
- **未量化**：indigestion 各阶段的 backlog 大小未在 paper 中给出
- **未实证**：abundance 假设依赖 First Proof 7/10 等数据点外推

## 关联概念

- [[Terence-Tao]] — 概念提出者
- [[Mathematical-Canonicalization]] — pipeline 最瓶颈阶段
- [[Slopocalypse]] — noise flooding 的同构
- [[Goodharts-Law]] — AI 触发 proxy divergence
- Theorem Economy Fall（forward reference，未建 entity） — shift from generation to digestion
- Validation Pipeline（参考 wiki 中已有 [[Validation-Pipeline]]，fix link） — stage 1-2 工程化
- [[Knowledge-Compilation]] — canonicalization 的知识生产域对应