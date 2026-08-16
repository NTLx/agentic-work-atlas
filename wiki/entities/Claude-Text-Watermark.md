---
type: entity
title: Claude Text Watermark
aliases:
  - Claude Text Watermark
  - Claude Watermark
  - Text Watermark
definition: "Anthropic 为 Claude 输出嵌入的 SynthID-Text 变体文本水印——通过将 token 选择的随机性源从通用 PRNG 替换为\"key + 前文\"，使第三方可在事后用 key 验证文本是否由带水印的 Claude 生成；2026-08 由 EU AI Act 合规驱动全球启用"
created: 2026-08-16
updated: 2026-08-16
tags:
  - content-provenance
  - ai-policy
  - watermark
  - ai-safety
evidence_level: high
claim_type: extracted
related_entities:
  - "[[SynthID-Text]]"
  - "[[C2PA-Content-Credentials]]"
  - "[[Anthropic]]"
  - "[[AI-Policy-Framework]]"
source_raw:
  - "[[20260816-anthropic-claude-text-watermark]]"
---

# Claude Text Watermark

> [!definition] 定义
> **Claude Text Watermark** 是 Anthropic 为 Claude 模型输出嵌入的 SynthID-Text 变体文本水印——通过在 token 选择阶段把随机性源从通用 PRNG 替换为"key + 前文"实现，使第三方可在事后用 key 验证文本是否由带水印的 Claude 生成。该机制在 2026-08 由 EU AI Act 合规驱动全球启用。

## 关键数据点

### 机制原理（Anthropic 描述）

- **基础观察**：LLM 在生成每个 token 时本就有随机性（如 "cold and..." 之后选 overcast 还是 grey 都不影响语义）
- **水印修改**：仅替换这个随机性的来源——从通用 PRNG 换成"key + 前文"
- **可检测性**：检测方有 key 时可事后验证序列是否与带水印生成路径一致；无 key 不可检测
- **pi digits 类比**：用 pi 的小数位序列代替骰子随机数——结果对玩家随机，但看到完整序列后可推断是否用了 pi

### 边界条件（水印稀疏场景）

| 场景 | 水印密度 | 原因 |
|------|---------|------|
| 一般自然语言 | 高 | 大量低熵 token 选择（连词、副词、同义词）|
| Factual passages（如 "Isaac Newton's ... Principia"）| 极低 | 唯一正确答案，无随机性 |
| Code（"2 + 2 ="）| 极低 | 唯一正确 token；仅在注释等可有选择处有水印 |
| Proofreading / 轻编辑 | 极低 | Claude 仅改少量词，watermark 几乎无落脚点 |
| 翻译 | 高 | 每个词都由 Claude 选择 |

### 政策驱动

- **EU AI Act + EU Code of Practice on Transparency of AI-Generated Content（2026-07 签署）**
- 签署方：~190 个（包含 Anthropic + 多个主要 AI provider）
- **全球 rollout**（Anthropic 自承"无法 durable 地按地域 scope"）
- 旧模型（2026-08-02 之前发布）有过渡期

### 不可追溯用户

watermark key 不含用户/组织信息；只证明"Claude 参与过"而非"哪个用户生成"——这与 [[Distinct-Principal-Identity]] 区分：watermark 追溯 provider，identity 追溯 user/agent

### 三类信号对比

| 信号 | 适用对象 | 机制 | 检测 |
|------|---------|------|------|
| Claude Text Watermark | 文本 | SynthID-Text 变体，统计模式 | 需 key，事后验证 |
| C2PA Content Credentials | 文件（.png/.jpg/.svg）| Cryptographically signed metadata | 任何 C2PA-aware 工具 |
| Pangram 类 AI 检测 | 文本 | Heuristic 语言模式（"this isn't [X], it's [Y]"，"quietly" 等）| 无 key，启发式概率 |

## 关键命题

### 命题 1：水印是 AI 责任的基础设施

当 AI 改变工作系统时，谁来标记 AI 输出？这是组织与部署主线"AI 责任"侧的具体落地——区别于 [[Distinct-Principal-Identity]]（追溯 agent 身份），水印追溯 provider 的存在参与

### 命题 2：水印的强项 = 不在生成时影响质量

作者声明在 SynthID-Text Gemini 流量对照中 thumbs up/down 无统计显著差异——水印不改变读者体验。这与 [[Agent-Environment-Misalignment]] 思路同构：让模型输出与人类消费解耦，把"AI 标记"作为额外层

### 命题 3：水印的弱点 = 不在"内容归属"决策点

watermark 只能事后验证 Claude 参与；不能区分"Claude 写了"与"Claude 重度编辑了"；factual / code / proofreading 处水印稀疏；轻编辑可能移除部分水印。这削弱了"用 watermark 验证学生论文 / 新闻原创性"等强主张——watermark 是**概率信号**而非**认证机制**

### 命题 4：水印与 LLM 责任 = 同构于密码学签名传统

物理钞票水印 / 数字文档签名 / 音频指纹 / 图像感知哈希都是"事后可验证"信号；LLM 文本水印是同一家族的 LLM 实例。区别：传统水印是离散符号（人可辨），LLM 水印是统计模式（人类不可辨，需 key 才能检测）

## 前提与局限性

- **factual / code / proofreading 处水印稀疏**——高价值 AI 内容（事实性写作、代码）反而最难检测
- **轻编辑可能移除部分水印**——完全重写则 100% 移除
- **无法区分 "Claude 写了" 与 "Claude 重度编辑了"**——watermark 是参与证明，不是 ownership
- **watermark 检测 API 尚未推出**——实现细节 in process
- **Anthropic "无影响输出质量"声明缺乏独立第三方评估**——仅自家对照 + SynthID-Text Nature 论文对照
- **全球 rollout 与 "最小干预"原则的张力**——非 EU 用户也被强制水印（Anthropic 自承"无法 durable scope by region"）
- **"watermark 不改变用户权利"是政策姿态而非技术事实**——EU AI Act 要求告知用户 AI 生成，水印是技术手段不是告知机制

## 关联概念

- [[SynthID-Text]] — Claude 水印的算法祖先（DeepMind 2024 Nature）
- [[C2PA-Content-Credentials]] — 文件型内容凭证（与文本水印机制独立但协同）
- [[Anthropic]] — Claude 水印的实施方
- EU AI Act — 合规驱动
- Content Provenance — 内容归属通用问题
- [[AI-Policy-Framework]] — 政策框架
- [[Distinct-Principal-Identity]] — 追溯 provider（watermark）vs 追溯 user/agent（identity）
- [[Reverse-Information-Paradox]] — "AI 与人协作的产物归谁"的延伸问题