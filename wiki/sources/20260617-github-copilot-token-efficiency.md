---
type: source-summary
title: "Getting more from each token: How Copilot improves context handling and model routing"
source_raw:
  - "[[20260617-github-copilot-token-efficiency]]"
created: 2026-06-17
updated: 2026-06-17
tags:
  - source-summary
  - context-engineering
  - model-routing
  - token-efficiency
  - agentic-engineering
evidence_level: high
claim_type: mixed
---

# Getting more from each token: How Copilot improves context handling and model routing

## 编译摘要

### 1. 浓缩
- **核心结论1**: HyDRA 模型路由可根据任务复杂度动态选择模型，实现 72.5% 成本节约（聚合模式）或超越 Sonnet 质量（峰值模式，12.9% 节约）
  - 关键证据: HyDRA (Cons.) 在 SWEBench 上与 OpenRouter Auto 分辨率持平（70.8%），但成本节约 3.3x；HyDRA (Agg.) 超越 Azure Foundry 两种运行模式
- **核心结论2**: Prompt caching + tool search 降低 token 消耗——缓存复用重复前缀，tool search 按需加载工具定义而非每轮全量发送
  - 关键证据: 长会话中工具定义固定成本随工具数线性增长；tool search 允许保持宽工具集同时减少每轮上下文
- **核心结论3**: Cache-aware routing 在自然缓存边界切换模型，避免缓存失效抵消路由收益
  - 关键证据: 首轮无缓存可失时切换、compaction 后前缀重置时切换；中间轮保持模型不变以维持缓存

### 2. 质疑
- **关于"72.5% 成本节约"的质疑**: 聚合模式牺牲了部分质量换取成本；对于需要深度推理的任务（复杂调试、架构设计），便宜模型可能不足；文章未公开质量下降的具体幅度
- **关于"跨语言路由"的质疑**: 16 语族训练数据的覆盖深度未说明；CJK 与欧洲语言的表现差距仅说"4 个百分点内"，具体数字未公开
- **关于 HyDRA 论文的可复现性**: 路由模型本身是闭源的，外部团队无法独立验证其在不同任务分布上的表现

### 3. 对标
- **Context-Engineering**: 本文的 prompt caching + tool search + cache-aware routing 是 [[Context-Engineering]] 在产品级 agent harness 中的工程实践
- **Model-Introspection**: HyDRA 的"学习模型何时需要升级"机制与 [[Model-Introspection]] 中模型自省概念有相似之处，但 HyDRA 更侧重路由而非行为调整
- **Agentic-Workflow-Token-Efficiency**: 本文的 token 效率策略直接对应 [[Agentic-Workflow-Token-Efficiency]] 中的 harness 优化方向
- **Agent-Harness**: Copilot 的 harness 改进（缓存、工具搜索、模型路由）是 [[Agent-Harness]] 概念在商业产品中的具体实现

### 关联概念
- [[Context-Engineering]]
- [[Agentic-Workflow-Token-Efficiency]]
- [[Agent-Harness]]
- [[Model-Introspection]]
