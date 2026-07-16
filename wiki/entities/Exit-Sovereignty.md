---
type: entity
title: Exit Sovereignty
aliases:
  - Exit Sovereignty
  - 退出主权
  - AI 时代的退出权
  - 切换主权
definition: "个人或组织从单一 AI 厂商/平台中退出的能力——可移植数据、可热切换模型、开源替代是退出保障；缺失退出权 = 协商变接受条款"
created: 2026-06-06
updated: 2026-06-16
evidence_level: medium
claim_type: mixed
tags:
  - AI-policy
  - vendor-lock-in
  - AI-relations
related_entities:
  - "[[Co-Existence]]"
  - "[[Prompt-Injection-Risk]]"
  - "[[Open-Source-Operational-AI-Framework]]"
  - "[[Agent-Harness]]"
  - "[[Exit-Ratchet-and-Layering]]"
  - "[[Credible-Threat-Structural-Binding]]"
  - "[[Collective-Exit-Right]]"
source_raw:
  - "[[20260604-mollick-coexistence]]"
---

# Exit Sovereignty（退出主权）

> [!definition] 定义
> **Exit Sovereignty** 是个人或组织从单一 AI 厂商/平台中退出的能力——可移植数据、可热切换模型、开源替代是退出保障。缺失退出权时，"与 AI 协商"实质上退化为"接受 AI 厂商条款"，Co-Existence 名存实亡。

## 形式化

```
协商空间 = 厂商能力 × 用户 prompt × 退出权
当下退出权 ≈ 0 → 协商空间被压扁 → "协商"实质 = "接受条款"
```

## 退出主权的组成

| 组件 | 状态 | 提供方 |
|------|------|--------|
| 可移植数据 | 部分支持（厂商标准不一） | 用户/开源 |
| 可热切换模型 | 早期（API 协议碎片化） | 用户/开源 |
| 开源替代 | 能力上限低于 frontier | 社区/开源实验室 |
| 本地部署 | 成本高、需要技术 | 用户 |
| 数据导出 | 厂商主导 | 厂商 |
| 标准化协议 | 早期 | 行业 |

## 与 Co-Existence 的关系

Co-Existence 范式假设人类与 AI 关系是"协商"。但：

| 条件 | 协商真发生 | 协商变接受 |
|------|-----------|----------|
| 退出权存在 | ✓ | — |
| 退出权缺失 | — | ✓ |
| 多厂商竞争 | ✓ | — |
| 厂商垄断 | — | ✓ |
| 数据可移植 | ✓ | — |
| 锁死 | — | ✓ |

当下大多数用户的实际状态：技术上有退出能力（可换模型），但退出等于接受更差能力，**不是真正的自由选择**。

## 历史对照

- 1990s 微软 Windows 锁定 → 开源 Linux 是退出保障
- 2010s iOS App Store 锁定 → Android + Web 是退出保障
- 2020s OpenAI/Anthropic/Google 锁定 → 开源模型（Llama, Mistral, DeepSeek）+ 本地部署是退出保障
- 三次锁定都有"开源 + 标准协议"作退出保障

## 前提与局限性
- **开源能力上限**：开源模型在 coding/math/agent 任务上仍低于 frontier；不是"等价替代"
- **本地部署成本**：本地部署需要硬件、技术、电力；不是所有人都能负担
- **标准化早期**：跨厂商 API 协议（OpenAI-compatible, MCP）正在形成，但未稳态

## 关联概念
| 本库主题 | Exit Sovereignty 的连接 |
|---------|------------------|
| [[Co-Existence]] | 协商的前提条件 |
| AI-Gatekeeper | 退出 = 绕过 gatekeeper |
| [[Open-Source-Operational-AI-Framework]] | 退出的基础设施 |
| [[Agent-Harness]] | 退出的工程实现 |
| AIO | 退出的反面是被 AIO 锁定 |

- [[Ethan-Mollick]] — 概念讨论

## 关键数据点

（关键事实、统计、时间线从原 raw 源沉淀，见 source_raw 字段）

