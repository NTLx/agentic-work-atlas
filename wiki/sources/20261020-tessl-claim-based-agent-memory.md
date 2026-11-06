---
type: source-summary
title: "Your AI isn't stupid. It's blind."
canonical_url: "https://tessl.io/blog/your-ai-isnt-stupid-its-blind"
raw_state: index
original_raw_file: "20261020-tessl-claim-based-agent-memory.md"
original_body_sha256: "46b2bd03cac56002ab13d2f77944129a20f05205bfc1cbf606a4e9e6e7feeb9a"
indexed_at: "2026-11-06T00:57:55.293Z"
created: 2026-11-06
updated: 2026-11-06
tags:
  - source-summary
  - knowledge-management
evidence_level: low
claim_type: mixed
source_locator:
  - "Original article section: Why agent memory matters now"
  - "Original article section: 1. Store claims, not chunks"
  - "Original article section: 2. Make time and absence explicit"
  - "Original article section: 3. Decide permissions before the model runs"
  - "Original article section: Where memory fits in a software factory"
  - "Original article section: TL;DR"
---

# Your AI isn't stupid. It's blind.

> 证据来源：https://tessl.io/blog/your-ai-isnt-stupid-its-blind（2026-10-20，Ran Aroussi）。2026-11-06 读取官方网站公开正文并逐节核对。原文以 canonical URL 为权威；本 Wiki 保存自撰释义、章节定位和推理边界，不存储网页逐字全文；original_body_sha256 仅记录临时来源索引记录的哈希，**不是**网页全文校验值。**本文数据若未注明独立验证，均为该来源的报道/作者陈述。**

## 编译摘要

### 1. 浓缩

- **核心结论 1：组织 Agent 记忆的单位应尽量是有来源、时间区间与可见性的 Claim，而非未治理的相似文本块。**
  - **原文证据**：作者称其 VarOps 系统为每个 Claim 保留说话人、事实、有效时间与原文 span；LongMemEval 500 问中正确证据出现在前十检索结果比例 99.8%；另称在约 3500 万 token 摄入中只用两 CPU、无 GPU 的本地嵌入模型。

- **核心结论 2：记忆应区分事实变化与知识空白，避免把缺失内容自动补全成想象。**
  - **原文证据**：作者保留新旧事实及 supersedes 关系，让系统区分 answered、searched but absent、out of scope；在一项消融中，禁止拒答令 30 次本应诚实拒答的情况被错误编造，尽管总体得分变化不大。

- **核心结论 3：访问控制应在检索前按用户身份执行，而不是让模型负责事后隐去敏感信息。**
  - **原文证据**：作者描述写入时计算披露等级、查询前按授权选择数据，示例里不同角色看到精确营收或区间；报告了 45 次跨隔离存储攻击的本地测例及 frontier/local 模型的结果对比。

### 2. 质疑与证据边界

- 文章由系统作者撰写，关键 benchmark 数字未在本轮独立复现；LongMemEval 的检索命中率不能等同端到端答案正确率。
- Claim 蒸馏有信息损失；多人权限、来源组合派生信息和时间冲突需要明确定义。
- 所谓 45/45 防御只是所述攻击集内结果，不能证明普遍抗越权。

### 3. 对标与应用约束

- **跨域迁移（综合判断，非原文证实）**：对 [[Agent-Knowledge-Management]]：与现有 provenance、Evidence/Reasoning 区分以及 Schema 的 source locator 有直接结构同构；但不应据此把全文 Source 自动丢弃，须由恢复性与活跃 Claim 依赖决定。
- **使用前提**：任何架构类比只能用于提出评测与工程变更候选；生产推广需真实权限、失败恢复、成本与回归实测。

## 重要判断（Claim / Evidence / Boundary）

- **判断**：组织 Agent 记忆的单位应尽量是有来源、时间区间与可见性的 Claim，而非未治理的相似文本块。
  - **证据**：一手来源 [Your AI isn't stupid. It's blind.](https://tessl.io/blog/your-ai-isnt-stupid-its-blind)，定位至「Why agent memory matters now / 1. Store claims, not chunks / 2. Make time and absence explicit / 3. Decide permissions before the model runs」及上方事实摘要。
  - **边界**：文章由系统作者撰写，关键 benchmark 数字未在本轮独立复现；LongMemEval 的检索命中率不能等同端到端答案正确率。

### 关联概念

- [[Agent-Knowledge-Management]]
- [[Structured-Agent-Memory]]
- [[Memory-Architecture]]
