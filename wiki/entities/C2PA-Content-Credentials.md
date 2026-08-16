---
type: entity
title: C2PA Content Credentials
aliases:
  - C2PA
  - C2PA Content Credentials
  - Content Credentials
  - Coalition for Content Provenance and Authenticity
definition: "由 C2PA 联盟维护的开放行业标准，通过在文件 metadata 中嵌入 cryptographically signed note 来声明文件的来源与处理历史；与 [[Claude-Text-Watermark|文本水印]]机制独立但协同——Anthropic Claude 对 .png/.jpg/.svg 等文件使用 C2PA，对文本使用 SynthID-Text 变体"
created: 2026-08-16
updated: 2026-08-16
tags:
  - content-provenance
  - file-metadata
  - open-standard
  - ai-safety
evidence_level: high
claim_type: extracted
related_entities:
  - "[[Claude-Text-Watermark]]"
  - "[[SynthID-Text]]"
source_raw:
  - "[[20260816-anthropic-claude-text-watermark]]"
---

# C2PA Content Credentials

> [!definition] 定义
> **C2PA Content Credentials** 是 Coalition for Content Provenance and Authenticity 维护的开放行业标准，通过在文件 metadata 中嵌入 cryptographically signed note 来声明文件的来源与处理历史。Anthropic Claude 对 .png/.jpg/.svg 等文件使用 C2PA，对文本使用 [[SynthID-Text]] 变体——两类机制独立但协同。

## 关键数据点

### C2PA vs 文本水印的核心差异

| 维度 | C2PA Content Credentials | Claude Text Watermark |
|------|-------------------------|----------------------|
| 适用对象 | 文件（.png, .jpg, .svg 等）| 文本 |
| 信号嵌入位置 | 文件 metadata | token 选择随机性源 |
| 信号性质 | Cryptographically signed note | 统计模式（人类不可辨）|
| 检测要求 | 任何 C2PA-aware 工具 | 需 provider 的 key |
| 用户信息 | 不含 | 不含 |
| 标准化 | 开放行业标准（同 camera 厂商 + photo-editing 软件）| SynthID-Text 算法族（Aaronson 2022 → DeepMind 2024）|

### C2PA 联盟

- 创始成员包括 Adobe、Microsoft、BBC、Intel、Truepic 等
- 当前 spec 维护在 c2pa.org
- camera 厂商与 photo-editing 软件广泛支持

### Anthropic 集成（2026-08）

- Claude 生成的 .png / .jpg / .svg 文件自动附加 C2PA content credential
- 凭证包含声明"该文件由 Claude 制作或处理"
- **不含**用户身份信息
- "nothing in the file changes — it is not embedded or hidden"——区别于传统水印

## 关键命题

### 命题 1：C2PA 与 SynthID-Text 覆盖两个不同威胁面

- **C2PA**：文件型内容（图片、视频、文档）——基于 metadata 完整性
- **SynthID-Text**：文本内容——基于 token 统计模式

两者一起构成"AI 内容归属"完整基础设施。Anthropic 同时启用两者是工程上的一致选择

### 命题 2：C2PA 是密码学签名传统的延伸

数字文档签名 / 代码签名 / TLS 证书都是"事后可验证"信号；C2PA 把这个传统延伸到媒体文件。同 [[Claude-Text-Watermark|文本水印]] 是 LLM 实例，C2PA 是文件实例

## 前提与局限性

- **依赖 metadata 完整性**——剥离 metadata 即丢失凭证
- **camera 厂商与 photo-editing 软件支持度不均**——并非所有设备 / 工具原生支持
- **不防"完整重做"**——重做文件则 metadata 重写，C2PA 不再指向原文件
- **Anthropic 自家工具支持**——"we'll be providing our own where you can drop a file and check"
- **跨厂商兼容性**：不同 C2PA 实现可能不互通

## 关联概念

- [[Claude-Text-Watermark]] — 文本侧的并行机制
- [[SynthID-Text]] — 文本水印的具体算法
- Content Provenance — 内容归属通用问题