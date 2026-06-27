---
type: source-summary
title: "Paving the way for agents in biology"
source_raw:
  - "[[20260608-paving-the-way-for-agents-in-biology.md]]"
created: 2026-06-10
updated: 2026-06-10
tags:
  - source-summary
  - deterministic-retrieval
---

# Paving the way for agents in biology

## 编译摘要

### 1. 浓缩
- **核心结论1**: **生物数据基础设施目前是“步行者城市”，不适配 Agent（汽车）**。现有的生物数据库充满了为人类浏览器操作设计的“点击税（Click tax）”，导致 Agent 在检索准确性上表现不佳。
  - 关键证据: 在没有专用工具的情况下，最强模型（如 GPT-5.5, Claude 4）在 VirBench 检索任务中的准确率仅在 16.9% 到 91.3% 之间，无法满足科学研究 100% 准确率的要求。
- **核心结论2**: **确定性检索层（Deterministic Retrieval Layers）是连接 Agent 意图与混乱数据库的必需桥梁**。通过将复杂的浏览器过滤逻辑转化为机器可读的接口，可以极大提升 Agent 的可靠性。
  - 关键证据: 引入 `gget virus` 工具后，所有 Agent 的准确率均升至 90% 以上，GPT-5.5 达到 99.7%，且消除了会话间的随机波动。
- **核心结论3**: **科学发现中的“细节决定成败”**。检索阶段的微小错误（如基因组版本混淆）会通过下游工作流放大，最终导致完全错误的生物学结论。
  - 关键证据: Sonnet 4 检索到的不完整序列集导致埃博拉爆发的时间追溯（TMRCA）偏差了数月甚至数十年（从 2014 年推至 1922 年）。

### 2. 质疑
- **关于“确定性工具”寿命的质疑**: 作者承认未来 Agent 可能强大到能自主克服基础设施的混乱。那么现在投入大量精力开发如 `gget virus` 这样的中间层工具，是否会被下一代更强的模型迅速淘汰？
- **关于“可信度 vs 创造力”的质疑**: 作者强调底层检索必须“无聊地可靠”，但过度依赖确定性工具是否会限制 Agent 在发现非预期关联（Serendipity）方面的潜力？
- **关于基础设施改造的质疑**: 与其为每个数据库建隧道，是否直接推动 NCBI 等机构建立 Agent-native 的原生 API 才是更根本的解法？

### 3. 对标
- **跨域关联1**: 类似于**软件工程中的“上下文工程”**。在 CLI 中，`ls` 和 `grep` 是 Agent 的确定性感知器；在生物学中，`gget` 扮演了类似的角色。
- **跨域关联2**: 类似于**城市规划中的“城市枢纽工程”**。为了让物流（Agent 任务）高效，需要将步行街（浏览器界面）改造成带匝道和标识的高速路（Agent-friendly API）。

### 关联概念
- [[Deterministic-Retrieval]]
- [[Scientific-Discovery-AI]]
- gget-virus
- Biological-Data-Infrastructure
- Laura-Luebbert
- VirBench
- [[Context-Engineering]]
- [[Integration-Wall]]
