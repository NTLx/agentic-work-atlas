---
type: entity
title: SynthID-Text
aliases:
  - SynthID-Text
  - SynthID Text
definition: "Google DeepMind 于 2024 年发表于 Nature 的 LLM 文本水印算法——通过在 token 选择阶段用\"key + 前文\"替换通用 PRNG 的随机性源，使第三方可用 key 事后检测文本是否由带水印的 LLM 生成；Anthropic Claude 等当前主流 LLM 文本水印的算法祖先"
created: 2026-08-16
updated: 2026-08-16
tags:
  - content-provenance
  - watermark
  - google-deepmind
  - ai-safety
evidence_level: high
claim_type: extracted
related_entities:
  - "[[Claude-Text-Watermark]]"
  - "[[C2PA-Content-Credentials]]"
  - "[[Anthropic]]"
source_raw:
  - "[[20260816-anthropic-claude-text-watermark]]"
---

# SynthID-Text

> [!definition] 定义
> **SynthID-Text** 是 Google DeepMind 于 2024 年发表于 *Nature* 的 LLM 文本水印算法——通过在 token 选择阶段把随机性源从通用 PRNG 替换为"key + 前文"，使第三方可用 key 事后验证文本是否由带水印的 LLM 生成。是当前主流 LLM 文本水印（包括 Anthropic Claude Watermark）的算法祖先；思想源头可追溯至 Scott Aaronson 2022 年提案。

## 关键数据点

### 算法要素

| 要素 | 实现 |
|------|------|
| 随机性源 | "key + 前文"（替代通用 PRNG）|
| 检测方式 | 第三方持有 key 时事后验证序列是否与带水印生成路径一致 |
| 读者体验 | 不可区分（人类读者无法辨别）|
| Provider 隔离 | 不同 provider 使用不同 key，互不识别 |
| 算法源头 | Aaronson 2022 提案（思想）→ DeepMind 2024 *Nature*（实现 + 评估）|

### DeepMind 验证数据（2024 Nature）

- 在 Gemini 部分流量上做 A/B 对照：水印模型 vs 无水印模型
- thumbs up/down 评分无统计显著差异
- 验证水印不影响输出质量（创造性、可读性、内容）

### 边界条件（同 [[Claude-Text-Watermark]]）

- factual passages / code / proofreading 处 token 选择余地小，水印稀疏
- 短文本检测置信度低（水印需要足够多的低熵 token 选择）
- 轻编辑可能移除部分水印

## 关键命题

### 命题 1：SynthID-Text 是 LLM 责任基础设施的标准化集中点

Anthropic、DeepMind、其他 EU Code of Practice 签署方使用同一算法族。这是**AI 责任基础设施的标准化集中点**——一个 Nature 论文成为行业事实标准

### 命题 2：水印 vs 检测软件 = 密码学 vs 启发式

- **水印**（SynthID-Text 类）：密码学基础，准确性高，需 key
- **AI 检测**（Pangram 类）：启发式基础（"this isn't [X], it's [Y]"、"quietly" 频率），无 key，估计性

两者是互补关系，不是"watermark vs no watermark"二元对立

## 前提与局限性

- **依赖 key 保密**——key 泄露则水印失效
- **factual / code / proofreading 处水印稀疏**——见 [[Claude-Text-Watermark]]
- **跨语言 / 跨 tokenizer 通用性需各自评估**
- **2014 年 Aaronson 提案以来未根本性更新**——意味着检测方与生成方博弈尚浅，攻击方研究空间大

## 时间线

- **2022** — Scott Aaronson 提案（思想基础）
- **2024** — Google DeepMind *Nature* 论文（SynthID-Text 实现 + Gemini 流量对照验证）
- **2026-07** — EU Code of Practice on Transparency of AI-Generated Content 签署
- **2026-08** — Anthropic Claude 全球启用 SynthID-Text 变体

## 关联概念

- [[Claude-Text-Watermark]] — Anthropic Claude 的 SynthID-Text 变体实例
- [[C2PA-Content-Credentials]] — 与 SynthID-Text 协同的文件元数据标准
- [[Anthropic]] — SynthID-Text 变体的实施方
- Content Provenance — 内容归属通用问题