---
type: entity
title: Text Watermarking
aliases:
  - Text Watermarking
  - 文本水印
definition: "在生成文本的 token 或选词过程中嵌入统计或密钥相关信号，供相应 detector 事后检测的技术类；具体算法与密钥体系按 provider 实现区分。"
created: 2026-10-21
updated: 2026-10-21
tags:
  - content-provenance
  - watermark
  - ai-safety
evidence_level: high
claim_type: mixed
related_entities:
  - "[[SynthID-Text]]"
  - "[[Claude-Text-Watermark]]"
source_raw:
  - "[[20260816-anthropic-claude-text-watermark]]"
  - "[[20261005-openai-eu-text-provenance]]"
---

# Text Watermarking

> [!definition] 定义
> **文本水印**是在生成文本的 token 或选词过程中嵌入统计或密钥相关信号，供相应 detector 事后检测的技术类。它通过生成路径留下可检测信号，不等于从语言风格推测机器生成的 heuristic AI detector，也不等于嵌入文件 metadata 的 [[C2PA-Content-Credentials]]。

## 关键数据点

### 实现类型

- **[[SynthID-Text]] / Claude variant**：Anthropic 来源将 Claude 的实现描述为 SynthID-Text 变体。
- **OpenAI textGrain**：OpenAI 独立的文本水印实现，在选词中加入统计信号；OpenAI 将 SynthID for text 列为比较对象。textGrain 不属于 SynthID。
- **Heuristic AI detectors**：从文本的表面语言模式估计来源，没有生成时嵌入的 provider 水印信号，机制与证据含义不同。

### 跨来源共同边界

- **篇幅与选词自由度**：短文本或低熵、受约束文本可供嵌入/检测的信号更少，检测能力会下降。
- **编辑与改写**：同义词替换等变更会削弱水印；未检出不等于文本未经 AI 生成。
- **检测结果的解释范围**：水印可支持文本经过特定带水印生成路径这一有限判断，不能测量人类贡献，也不能确立所有权、责任、用户身份或内容真实性。
- **实现依赖**：具体 detector 识别的是对应实现的信号；不同 provider 的算法、实验结果和覆盖范围须分别验证。

### Rollout 是政策选择

- Anthropic 来源记载其 Claude 水印全球启用，并说明其地域范围策略。
- OpenAI 公布的策略是：API 全球对部分模型 opt-in；符合条件的 ChatGPT/Codex 在 EU 逐步启用；文本 detector 初期面向获批研究者和专家组织。
- 这些差异是 provider-specific deployment choices，不能从一种实现推断另一家的 rollout。

## 前提与局限性

- **检测不是归属裁决**：命中不表示文本由模型独立写成；更不识别具体用户、权利人或责任主体。
- **未检出不是人工证明**：篇幅、受约束内容、编辑/改写、翻译、模型覆盖范围与启用时间都会影响检测。
- **厂商自评需保留边界**：来源中的性能或质量评估应注明实施方、评测语料、检测阈值及任务范围；单方结果不能自动外推为跨厂商或真实环境表现。
- **与文件 provenance 互补而非等同**：Content Credentials 可记录文件来源与历史；文本水印关注 token/选词中的统计信号。分层 provenance 可组合水印、文件凭证、验证工具及政策/执法机制。

## 关联概念

- [[SynthID-Text]] — Google DeepMind 的文本水印算法；Claude 来源记载其为 Claude variant 的技术基础
- [[Claude-Text-Watermark]] — Anthropic 在 Claude 输出中的实现
- [[C2PA-Content-Credentials]] — 文件 metadata 凭证，与文本水印机制不同
- [[20260816-anthropic-claude-text-watermark]] — Anthropic 一手来源摘要
- [[20261005-openai-eu-text-provenance]] — OpenAI textGrain、评估边界与部署策略
