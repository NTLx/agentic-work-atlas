---
type: entity
title: Token Maxing
aliases:
  - Token Maxing
  - token 最大化
definition: "企业无差别消耗 AI token 的现象，导致推理成本失控，迫使公司从全面实验转向配给制"
created: 2026-05-31
updated: 2026-08-21
evidence_level: medium
claim_type: mixed
tags:
  - ai-cost
  - token-economics
  - enterprise-ai
related_entities:
  - "[[Enterprise-AI-Rationing]]"
  - "[[Agentic-Workflow-Token-Efficiency]]"
  - "[[Token-Supply-Chain]]"
  - "[[AI-First]]"
  - "[[Token-Maxing-vs-Token-Efficient]]"
source_raw:
  - "[[20260528-corporate-america-ai-rationing]]"
  - "[[20260730-lenny-anthropic-first-technical-pm-dianne-penn]]"
  - "[[20260819-valley101-e249-token-economic-pivot]]"
---

# Token Maxing（Token 最大化）

> [!definition] 定义
> **Token Maxing** 是企业员工无差别消耗 AI 推理 token 的现象，导致成本在视野外失控。Goldman Sachs 预测 Agentic AI 普及将驱动 token 消耗到 2030 年增长 24 倍，达到每月 120 quadrillion tokens。

## 核心机制

Token Maxing 不是单点浪费，而是结构性问题：

1. **全面实验阶段**：企业鼓励员工广泛使用 AI 工具，不设上限
2. **消耗不可见**：token 消耗分散在各部门、各工具中，缺乏统一可观测性
3. **Agentic 放大效应**：Agent 从"回答一句话"变为"连续多轮工具调用"，单次任务 token 消耗量级上升
4. **账单冲击**：月末/季末账单远超预期时才发现失控

## 关键数据点

- Uber 4 个月烧完 2026 财年全部 AI 编码工具预算，COO 质疑支出合理性
- Microsoft 撤销开发者对 Anthropic Cloud Code 的访问权，强制迁移到内部 Copilot CLI（2026 年 6 月 30 日前完成）
- 某企业客户单月 AI license 支出达 `$500 million`，因未能限制员工使用量
- Goldman Sachs 预测 2030 年 token 消耗增长 24 倍至每月 120 quadrillion
- 四大超大规模云厂商 2026 年合计资本支出 `$725 billion`
- 47% 的企业基于 AI 幻觉做关键决策，年经济损失 `$67.4 billion`

## 正面 Framing：token 作为实验投入（2026-07 冲突标记）

> [!warning] 冲突标记
> 同一术语存在两个相反的叙事框架，应并列使用而非调和：
> - **成本框架**（本条目原定义）：token maxing = 无差别消耗 → 账单失控 → 被迫配给。证据：Uber 预算燃尽、Microsoft 强制迁移。
> - **投入框架**（Dianne Penn / Garry Tan，2026-07）：token 是 **input**，output 是 experimentation；围绕 experimentation 设目标比围绕 token spend 设目标更准确。Garry Tan 主张"愿意年花 \$100K tokens = 活在 2028 年的工作方式"；Penn 的修正是"token spin 是输入，真正的产出是实验，也许该围绕实验来设目标"。Anthropic 内部观察：最具创造力的 prototyper 确实花大量时间与模型共处——"you have to sweat the tokens as much as you sweat the pixels"。

两个框架的适用边界：**个人/产品探索层**投入框架成立（token 便宜、学习价值高）；**组织成本层**成本框架成立（无差别消耗不可观测、不可归因）。混淆两层会产生错误推论——用投入框架为组织级失控辩护，或用成本框架压制个人级实验。

## 阶段二：Token Efficient（2026 下半年起，详见 [[Token-Maxing-vs-Token-Efficient]]）

> [!info] 阶段演化（2026-08-21 补充）
> 硅谷101 E249（2026-08-19）明确：2026 年下半年开始，工程纪律追上来了——三个事件（GPT-5.5 / DeepSeek V4 / Fable 5）击碎了 Token Maxing 的「合理性假设」。Token Maxing 不是被取代，而是被纳入更大的「Token Maxing → Token Efficient」时序递进；详见 [[Token-Maxing-vs-Token-Efficient]] 对比页。

## 前提与局限性

- Token Maxing 可能是学习曲线的一部分——早期广泛实验后自然收敛到高价值场景
- `$500 million` 单月数据来自匿名咨询师转述，缺乏可验证来源
- Goldman Sachs 预测基于 Agentic AI 全面普及假设，实际采纳速度可能更慢
- "AI 只适用于编码"（Ali Ansari 观点）可能低估了法律、客服、内容等场景的价值

## 关联概念

- [[Enterprise-AI-Rationing]] — Token Maxing 的直接后果：企业被迫实施配给制
- [[Agentic-Workflow-Token-Efficiency]] — 技术层面的应对策略
- [[Token-Supply-Chain]] — 基础设施层面的 token 治理框架
- [[AI-First]] — Token Maxing 是 AI-First 战略的成本侧反面
- [[Token-Maxing-vs-Token-Efficient]] — 阶段递进对比页：Token Maxing 是 Token Efficient 的过渡阶段
