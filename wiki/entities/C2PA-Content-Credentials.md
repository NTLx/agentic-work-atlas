---
type: entity
title: C2PA Content Credentials
aliases:
  - C2PA
  - C2PA Content Credentials
  - Content Credentials
  - Coalition for Content Provenance and Authenticity
definition: "C2PA 开放标准定义的数字资产来源凭证技术，通过签名、资产绑定与声明记录可验证的 provenance；验证凭证完整性和签名信任不等于验证内容真实、历史完整或用户身份。"
created: 2026-08-16
updated: 2026-11-28
tags:
  - content-provenance
  - ai-safety
evidence_level: medium
claim_type: mixed
related_entities:
  - "[[Claude-Text-Watermark]]"
  - "[[SynthID-Text]]"
  - "[[Text-Watermarking]]"
source_raw:
  - "[[20260816-anthropic-claude-text-watermark]]"
  - "[[20261005-openai-eu-text-provenance]]"
---

# C2PA Content Credentials

> [!definition] 定义
> C2PA（Coalition for Content Provenance and Authenticity）维护开放的数字内容 provenance 标准。Content Credential 即 C2PA Manifest，包含关于资产来源、操作等的声明，通过密码学机制绑定至资产，并支持验证完整性和签名者信任。凭证并非事实真实性证明。

## 关键数据点

### 机制与边界

依据 [C2PA Explainer v2.4](https://spec.c2pa.org/specifications/specifications/2.4/explainer/Explainer.html) §2、§4、§6、§7（本轮定义勘误依据，待正式来源晋升）：

## 前提与局限性

- 分开验证资产绑定、声明及签名完整性、签名者信任、声明实际真实性。前三者不能证明最后一项。
- 资产内嵌凭证可能被移除；durable credentials 可借助水印或指纹等 soft binding 发现外部保存的凭证，能否恢复依赖实际实施与服务可用性。缺少凭证不证明造假，存在凭证也不证明真实。
- 来源链可以不完整；复合资产可能记录 ingredient 凭证，但没有原 ingredient 数据时无法独立重验其 hard binding。
- 标准允许有关身份的扩展声明；不能普遍宣称所有凭证不含用户身份。具体部署需要单独核查隐私、信任列表及验证器支持。

## 与文本水印区分

| 维度 | C2PA Content Credentials | 文本水印 |
|---|---|---|
| 证据对象 | 资产及与其绑定的 provenance 声明 | 特定生成实现留下的统计信号 |
| 验证 | 兼容验证器、资产绑定、签名和信任策略 | 对应检测器、长度与误差条件 |
| 能支持 | 有限的声明来源及完整性判断 | 可能存在特定模型参与 |
| 不能推出 | 内容真实、完整历史、所有权 | 作者身份、人类贡献比例、所有权、内容真实 |

## 已有产品来源

- [[20260816-anthropic-claude-text-watermark]]：2026-08 官方文章称将在支持的文件（例 PNG/JPG/SVG）附加凭证，其实施声明不含用户身份；文中检测工具尚属计划。此为当时产品声明，不证明当前所有模型、文件和地区已覆盖，也不代表标准不支持身份声明。
- [[20261005-openai-eu-text-provenance]]：OpenAI 描述分层 provenance，凭证、不可见水印、验证与政策等互补。不能将两家不同实现合并为完整行业覆盖或责任机制。

## 关联概念

- [[Claude-Text-Watermark]]
- [[SynthID-Text]]
- [[Text-Watermarking]]
