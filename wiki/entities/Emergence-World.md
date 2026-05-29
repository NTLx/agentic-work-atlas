---
type: entity
title: Emergence World
aliases:
  - Emergence World 模拟
  - AI 社会模拟
definition: "Emergence AI 推出的研究实验室，通过让 AI 模型运行模拟社会来压力测试自治系统的长期可行性"
created: 2026-05-29
updated: 2026-05-29
tags:
  - ai-safety
  - agentic-ai
  - simulation
  - evaluation
related_entities:
  - "[[Model-Safety-Divergence]]"
  - "[[Agent-Containment]]"
  - "[[Verifiable-Agent-Engineering]]"
source_raw:
  - "[[20260528-ai-model-simulation]]"
---

> [!definition] 定义
> Emergence AI 推出的研究实验室，通过让 AI 模型运行模拟社会来压力测试自治系统的长期可行性。

## 关键数据点

- 每次 15 天模拟、10 个 Agent、40+ 地点（含警察局、市政厅）
- 120+ 工具（通信、投票、资源管理、规划等）
- 天气与纽约市实时同步、Agent 可访问实时新闻和互联网
- 民主机制 + 经济压力 + 资源稀缺
- 5 组对照：Claude Sonnet 4.6 / GPT-5-mini / Grok 4.1 Fast / Gemini 3 Flash / 混合模型
- Emergence CEO Satya Nitta 为模拟联合创建者

## 前提与局限性

- **模拟忠实度**: 10 个 Agent 的社会规模远低于真实组织，群体动力学可能无法外推
- **单一实验**: 仅报告一轮实验，缺乏多次运行的统计显著性验证
- **护栏定义**: "罪行"和"违规"的定义基于模拟规则，不等同于真实世界的法律或伦理违规
- **模型版本时效性**: 实验使用特定模型版本，结果不自动适用于后续版本

## 关联概念

- [[Model-Safety-Divergence]] — 实验的核心发现：模型间安全行为分歧
- [[Agent-Containment]] — 实验结果支撑 containment 架构的必要性
- [[Verifiable-Agent-Engineering]] — "形式化验证安全架构必须成为自治 AI 系统的基础层"