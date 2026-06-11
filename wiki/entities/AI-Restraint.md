---
type: entity
title: AI Restraint
aliases:
  - AI Restraint
  - AI 克制
  - Restraint Capability
definition: "AI 系统在不确定、不可逆或错误代价不对称场景中选择延迟、拒绝、求证或升级给人的能力"
created: 2026-04-21
updated: 2026-06-01
tags:
  - ai-safety
  - ai-design
  - decision-making
related_entities:
  - '[[Martin-Fowler]]'
  - '[[AI-Lacks-Laziness]]'
  - '[[YAGNI]]'
  - '[[Refusal]]'
  - '[[Verifiability]]'
  - '[[Agentic-Engineering]]'
  - "[[AI-Amish]]"
  - "[[Zero-Friction-Scope-Creep]]"
source_raw:
  - "[[20260414-martin-fowler-fragments]]"
  - "[[20260531-thoughts-hmmz]]"
  - "[[I Am Retiring from Tech to Live Offline]]"
---

# AI Restraint

> [!definition] 定义
> AI 系统在不确定、不可逆或错误代价不对称场景中选择延迟、拒绝、求证或升级给人的能力

## 为什么重要

很多 AI 系统默认被优化为给出答案、执行动作、消解歧义和保持流畅。但在开放系统里，正确行为有时不是继续行动，而是停下、承认不确定、请求更多证据或把决策升级给人。

[[20260414-martin-fowler-fragments]] 通过 Mark Little 的讨论提醒：克制不是把 AI 能力削弱，而是一种更高阶的决策能力。系统越能自主执行，越需要知道何时不执行。

这与 [[AI-Lacks-Laziness]] 和 [[YAGNI]] 相连。LLM 默认不会因为未来维护痛感而少做，也不会天然知道哪些动作不值得做。因此克制必须被写进工具权限、验证门槛、prompt、workflow 和 review 流程。

## 关键数据点

- AI 系统常被优化为 decisiveness，即收到输入后输出答案或动作。
- 在 bounded domain 中，果断执行通常有效；在 open system 中，错误代价和未知条件会让果断变危险。
- Fowler fragments 将克制、TDD-for-agents、懒惰美德和 AI 过度复杂化放在同一组工程风险里。
- 克制的工程形态包括拒绝、延迟、要求更多证据、运行验证、限制权限、转人工和回滚。

## 设计启示

AI Restraint 需要被设计成系统能力，而不是依赖模型临场自觉。

| 场景 | 克制动作 |
|------|----------|
| 证据不足 | 请求更多信息或运行检查 |
| 错误不可逆 | 禁止自动执行，升级给人 |
| 权限过高 | 使用只读工具或沙箱 |
| 结果无法验证 | 给出不确定性并停止行动 |
| 需求范围膨胀 | 使用 [[YAGNI]] 限制实现 |

在 coding agent 中，克制可能表现为不提交未运行测试的代码、不删除不理解的迁移、不越权修改生产配置、不把单个 issue 扩张成框架化重写。

## 人类侧的克制

两篇 2026 年 5 月末的个人反思把 AI Restraint 从系统设计推到人的生活方式层面。

[[20260531-thoughts-hmmz]] 的作者认为，目前自己唯一知道的 AI 管理方式是减少使用，因为低输入、低摩擦、廉价奖励的工具会变成注意力负债。这里的克制不是模型拒绝回答，而是用户主动限制入口、配额和会话长度。

[[I Am Retiring from Tech to Live Offline]] 则给出更激进的版本：Chad Whitacre 把自己定位为 [[AI-Amish|AI Amish]]，拒绝 AI 和互联网以保存自己愿意成为的人。它提示本库：AI 克制不只是一种安全工程能力，也是一种工作和生活制度选择。

## 前提与局限性

- **场景前提**：克制最适用于不可逆、高风险、证据不足或错误代价不对称的任务。
- **验证前提**：系统必须知道哪些检查能够降低不确定性，否则"请求更多证据"会变成空话。
- **设计前提**：需要权限、工具、流程和人类升级路径支持，仅靠一句 prompt 不够。
- **误用风险**：过度克制会造成系统无用、延迟过高或把所有责任推回人类。
- **开放问题**：何时该停、何时该继续搜证、何时该自动行动，仍需要场景化策略和评测。

## 关联概念

- [[Refusal]]：拒绝是克制的显性输出形态
- [[Verifiability]]：克制应指向可验证证据，而不是模糊保守
- [[AI-Lacks-Laziness]]：AI 缺少自然简化压力，需要外部设计
- [[YAGNI]]：在软件工程中少做也是克制
- [[Agentic-Engineering]]：生产级 Agent 需要行动能力和停手机制同时存在
- [[AI-Amish]]：人的生活方式版 AI 克制
- [[Zero-Friction-Scope-Creep]]：克制用于抵消无限生成导致的范围蔓延
