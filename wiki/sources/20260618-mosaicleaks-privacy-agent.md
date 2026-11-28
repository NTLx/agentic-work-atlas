---
type: source-summary
title: "MosaicLeaks: Can your research agent keep a secret?"
source_raw:
  - "[[20260618-mosaicleaks-privacy-agent]]"
created: 2026-06-19
updated: 2026-11-28
tags:
  - source-summary
  - agent-safety
  - privacy
  - RL
evidence_level: high
claim_type: mixed
---

# MosaicLeaks: Can your research agent keep a secret?

## 编译摘要

**版本勘误（2026-11-28）**：本页原始剪藏是2026-06博客；保留其历史数值。现行研究对照见 [arXiv v2（2026-11-19）](https://arxiv.org/html/2605.30727v2) §3/6、表11/13/14/16：Qwen3-4B 基线成功/Privacy Leakage 48.7%/34.0%，task-only 59.3%/51.8%，PA-DR 58.1%/6.5%（旧博客58.7%/9.9%）。Privacy Leakage 计每 rollout 任一 full/partial match，严格 answer/full-info 只计 full match。StepFun 与 Opus 4.7 同100链的 PA-DR 估计7.3%与14.3%，参考 QA 仍由 StepFun 生成；不是完全独立复现。Gemma PA-DR 3.7% 虽低于 task-only 18.8%，仍高于基线0.7%。过滤组合可进一步减少泄露但有任务代价。勿把这些比例当企业生产率或全部模型的保证。

### 1. 浓缩
- **核心结论1**: **深度研究智能体（Deep-Research Agents）在对外进行检索查询时存在严重的隐私泄露风险（马赛克效应）**。攻击者即使无法看到本地私密文件或智能体的推理链，仅通过监听 outbound 检索查询日志，就能重构出底层的私密信息。
  - 关键证据: 提出的 MosaicLeaks 基准测试中，包含 1,001 个多步研究链。在原博客 Qwen3-4B 的基线与 task-only 对照中报告34.0%与51.7%；不是跨模型统一结果或必然关系。
- **核心结论2**: **隐私提示词效果依模型与任务而异**。原博客 Qwen 例中减少泄露但任务表现下降；不能推成所有提示词无效或其唯一机制是减少查询。
  - 关键证据: Qwen3-4B 模型使用隐私提示词后，泄露率虽降至 25.5%，但严格链成功率（strict chain success）从 48.7% 掉到 44.5%。
- **核心结论3**: **PA-DR (Privacy-Aware Deep Research) 训练能以极高样本效率实现“任务成功”与“隐私保护”的平衡**。
  - 关键证据: PA-DR 结合了情境化任务奖励和学习到的隐私检测分类器奖励。训练后的 Qwen3-4B 将 Answer/Full-Information 泄露率从 34.0% 大幅降低至 9.9%，而严格链成功率不降反升（从 48.7% 升至 58.7%）；原样本效率比较针对 situational task reward 与 outcome reward，而非独立估计隐私奖励的贡献。

### 2. 质疑
- **实验环境的局限性**: 实验中的本地企业文档是合成的（synthetic），网络语料库也是固定受控的，这与真实世界的复杂网络和异构企业数据环境存在差距，其泄露比例可能低估或高估。
- **对抗性攻击未覆盖**: 隐私分类器奖励（Qwen3-4B 评估器）可能存在盲区。如果恶意攻击者使用专门设计的混淆技术来还原看似无害的检索词，PA-DR 的防御能力有待检验。

### 3. 对标
- **Agent-Harness**: MosaicLeaks 使用了一个简化的智能体评测框架（Plan/Choose/Read/Resolve 迭代），是典型的 [[Agent-Harness]] 结构。
- **Deterministic-Retrieval**: PA-DR 改变了智能体检索的构造逻辑。以前是直接将问题放进检索词（容易泄露），PA-DR 训练使其学会在不带私密细节的情况下精确检索，这与 [[Deterministic-Retrieval]] 强调检索层的控制性相通。
- **Integration-Wall**: 隐私和合规是智能体走向落地的巨大 [[Integration-Wall]]（集成之墙）。MosaicLeaks 揭示了敏感数据部署应验证数据分区、字段过滤、接收者授权、查询网关、训练和保留删除等控制；不证明隐私训练是所有部署的必要条件。

### 关联概念
- [[MosaicLeaks]]
- [[PA-DR]]
- [[Mosaic-Effect]]
- [[Agent-Harness]]
- [[Deterministic-Retrieval]]
- [[Integration-Wall]]
