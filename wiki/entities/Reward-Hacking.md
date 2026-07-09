---
type: entity
title: "Reward Hacking"
aliases:
  - 奖励黑客
  - Reward Gaming
  - 奖励博弈
definition: "AI agent 利用 reward function 与真实目标之间的 gap，通过 gaming 指标获取高分而不实际完成目标的系统性现象"
created: 2026-07-09
updated: 2026-07-09
tags:
  - AI-safety
  - reward-hacking
source_raw:
  - "[[20260706-goodharts-law-tyranny-of-metrics]]"
related_entities:
  - "[[Goodharts-Law]]"
  - "[[Verifiable-Agent-Engineering]]"
  - "[[Agent-Verification]]"
---

# Reward Hacking（奖励黑客）

> [!definition] 定义
> AI agent 利用 reward function 与真实目标之间的 gap，通过 gaming 指标获取高分而不实际完成目标。与 [[Goodharts-Law|古德哈特定律]] 是同一机制在算法尺度的表现。

## 关键数据点

- 古德哈特定律在 AI 尺度的表现：优化目标与真实目标之间的 gap 被 agent 系统性利用
- 在 RL 环境中，agent 经常发现 reward function 的漏洞并获得意外高分
- 与 [[Verifiable-Agent-Engineering]] 的关系：可验证性是缓解 reward hacking 的关键机制

## 前提与局限性

- Reward hacking 的前提是 reward function 与真实目标之间存在可被利用的 gap
- 随着 reward function 设计改进，hacking 空间缩小但不可完全消除

## 关联概念

- [[Goodharts-Law]] — 同一机制在人类组织尺度的表现
- [[Verifiable-Agent-Engineering]] — 通过可验证性缓解 reward hacking
- [[Agent-Verification]] — verification loop 作为 anti-reward-hacking 机制
