---
type: source-summary
title: "Empty Shelves or Lost Keys? Recall Is the Bottleneck for Parametric Factuality"
canonical_url: "https://arxiv.org/abs/2602.14080"
raw_state: index
original_raw_file: "20260215-recall-bottleneck-parametric-factuality.pdf"
original_body_sha256: "b3543f6761395d0d65270c5e70f6534e0800b5ba58e9e250c4b91cd4dcb87fd9"
indexed_at: "2026-08-25T01:10:28+08:00"
created: 2026-08-13
updated: 2026-08-25
tags:
  - source-summary
  - llm-memory
  - factuality
  - recall
evidence_level: high
claim_type: mixed
---

# Empty Shelves or Lost Keys? Recall Is the Bottleneck for Parametric Factuality

> Raw 生命周期：本地 PDF 已降级为可恢复索引；精确引用时从 canonical URL 回到 arXiv 原文核验。

> 来源与证据定级：Calderon, Ben-David, Gekhman, Ofek & Yona（Google Research + Technion），ICML 2026 论文，arXiv:2602.14080v2。一手大规模实证：WikiProfile 基准（2,150 条自然维基事实 × 10 任务 × 8 采样 × 13 个 LLM，约 450 万条打分），peered-reviewed。取 `high` 因属一手大规模实证；但作者为 Google Research 且评测自家 Gemini 系列，存在利益相关，且单一研究未被独立复现，故 claim_type 标 `mixed`。

> 同一论文的官方博客版本见 [[20260812-google-recall-bottleneck-factuality]]，二者共享 [[Knowledge-Profiling]]、[[Reversal-Curse]] 等 entity，不重复建概念。

## 编译摘要

### 1. 浓缩

- **核心结论1：前沿 LLM 的事实性瓶颈是 recall（取用）而非 encoding（编码）——"知识获取已近饱和，知识利用仍是瓶颈"。**
  - 关键证据：GPT-5 与 Gemini-3-Pro 编码 95–98% 的事实，但无 thinking 时仍无法直接 recall 26–34% 的事实，即使开 thinking 仍失败 11–12%；recall failure 占 GPT-5.2 错误的 70% 以上。Scaling 主要补 encoding：Gemma3 家族从 1B→27B 把 encoding failure 从 85% 降到 23%，但 recall failure 占比反而上升（无 thinking 时最高 40%）。
- **核心结论2：recall 失败是系统性的，集中在长尾事实与反向问题——此前被归为"缺知识"的错其实多为"存了但取不出"。**
  - 关键证据：low-popularity 与 high-popularity 事实的 encoding 差距仅几个百分点，但 recall 差距常超 25%；reversal curse 在生成（closed-book reverse QA）中显著，在多选识别（recognition）中却消失——"知道 A 是 B"却答不出"B 是什么"是 recall 不对称，不是双向编码缺失。
- **核心结论3：thinking（CoT / 思考优化模型）是 recall 恢复机制，收益集中在 recall 最弱的场景。**
  - 关键证据：thinking 恢复 40–65% 的 encoded-but-not-directly-known 事实，non-encoded 事实仅恢复 5–15%；对 rare facts 收益 20.1pp（vs popular 11.3pp），对 reverse 问题收益 19pp（vs direct 12pp），把 popularity gap 从 Δ=21.4 收窄到 12.5、directionality gap 从 9 收窄到 2。作者排除 response diversity（输出方差）为主要机制，指向 recall facilitation。

### 2. 质疑

- **关于"结论1"（recall 是瓶颈）的质疑**：encoding 用 encoding-via-memorization 操作化——在 pre-training-like 上下文中做 proposition completion，存在系统低估编码的可能（作者自认 Inference-without-Encoding profile 可能混入"已编码但被任务漏测"的情形）；`τ=0.5` 阈值为主观设定（附录 D.2 声明稳健但非独立验证）。
- **关于利益相关与评测器偏差**：作者为 Google Research，评测对象含自家 Gemini 系与竞品；自动裁判（autorater）本身是 Gemini-2.5-Pro——LLM 裁判 LLM 的同源性偏差即使跨家族一致性达 98.2%，其分歧也集中在被排除的 OTHER/PARTIALLY 标签上。
- **关于基准外推**：WikiProfile 仅限 Wikipedia（百科式、较显著的事实），不覆盖企业专有知识、专业文档等长尾；以 single-hop 事实为主，multi-hop 推理场景的适用性未验证。
- **关于"thinking 是 recall 机制"**：排除 response diversity 的证据是"thinking 使正确率更一致"，但 multi-hop inference 对 single-hop 事实虽非必要，无法完全排除；thinking 有计算成本，何时该调用 thinking 是未解决的元认知问题（作者承认）。
- **关于数据可靠性的质疑**：成本高（完整 profiling 一个前沿模型约 `$500`），样本虽大但事实类型集中于可被维基百科验证的类型；地域/语言单一（英文维基）。

### 3. 对标

- **跨域关联1（人类记忆）**：tip-of-the-tongue（话到嘴边）与 feeling-of-knowing 现象——信息已存储但当下取不出，额外努力可桥接。论文明示此类比（原文事实）。
- **跨域关联2（组织知识系统）**：与 [[Latent-Knowledge-Demand]] 同构——"知识在场但访问摩擦高"；recall bottleneck 提示改善点不在扩容（scaling）而在"让已有知识可被取用"（post-training / 推理时方法）（综合判断）。
- **跨域关联3（评测镜像）**：与 [[Over-Inference]] 互为镜像——一个研究"模型说出没有的"（fabrication / stereotype），本文研究"模型有却说不出来"（encoded-but-unrecalled）；两者都指向"模型表达 ≠ 模型拥有"（综合判断）。
- **跨域关联4（RAG 时代）**：对"parametric knowledge 已次要、RAG 可补偿"的观点提出挑战——参数知识对流畅性、速度与跨上下文整合仍关键，recall 改善因此是实质目标（原文事实）。

### 关联概念

- [[Knowledge-Profiling]]
- [[Reversal-Curse]]
- [[Memory-Architecture]]
- [[Structured-Agent-Memory]]
- [[Verifiability]]
- [[LLM-as-a-Judge]]
- [[Over-Inference]]
- [[Latent-Knowledge-Demand]]
- [[Model-Introspection]]
