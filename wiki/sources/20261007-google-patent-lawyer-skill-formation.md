---
type: source-summary
title: "Does better work always mean better workers?"
canonical_url: "https://research.google/blog/does-better-work-always-mean-better-workers/"
raw_state: index
original_raw_file: "20261007-google-patent-lawyer-skill-formation.md"
original_body_sha256: "32456454c51be3aad77e11540954878cfa844a1cf03d99251f2ee073d9aa2ea9"
indexed_at: "2026-11-06T00:57:55.293Z"
created: 2026-11-06
updated: 2026-11-06
tags:
  - source-summary
  - skill-atrophy
evidence_level: medium
claim_type: mixed
source_locator:
  - "Original article section: Better work with AI"
  - "Original article section: When AI is removed"
  - "Original article section: Further directions"
---

# Does better work always mean better workers?

> 证据来源：https://research.google/blog/does-better-work-always-mean-better-workers/（2026-10-07，David Autor、Tanya Rodchenko）。2026-11-06 读取官方网站公开正文并逐节核对。原文以 canonical URL 为权威；本 Wiki 保存自撰释义、章节定位和推理边界，不存储网页逐字全文；original_body_sha256 仅记录临时来源索引记录的哈希，**不是**网页全文校验值。**本文数据若未注明独立验证，均为该来源的报道/作者陈述。**

## 编译摘要

### 1. 浓缩

- **核心结论 1：AI 提高即时作品质量并不能自动保证专业人员的无辅助能力同比增长。**
  - **原文证据**：Google/NBER 文中描述 11 家专利律师事务所共 133 人进行为期三个月的随机试验，按律师事务所分组分配 AI 工具使用权。10 天和 90 天 AI 辅助专利起草质量分别提高 0.34、0.38 个标准差；提升主要来自减少低分而非增加极佳作品。

- **核心结论 2：经验层级影响 AI 辅助之后的独立判断增益。**
  - **原文证据**：第 90 天在禁止 AI 的专利 redlining 测试中，整体可观察提升约 0.32 SD；资深律师（7 年以上）约 0.45 SD，初级律师平均未出现可辨识改善，评分呈现两极分化。

- **核心结论 3：经验者可将 AI 用作逻辑审计辅助，新手可能错过形成判断的训练。**
  - **原文证据**：定性分析显示初级律师常按顺序润色低重要性段落或只描述缺陷不真正修改，而资深人员重写专利权利要求并重审商业法律边界。

### 2. 质疑与证据边界

- 随机分配的是工具访问权而非强制实际使用强度；11 家合作律所、专利起草领域和 90 天时限限制外推。
- 无辅助的结果不能证明每位初级律师技能下降；正确结论是平均没有明显提升且分布分叉。
- 经验分组的差异不等于所有职业或长期重复使用的必然因果机制。

### 3. 对标与应用约束

- **跨域迁移（综合判断，非原文证实）**：对 [[Skill-Atrophy-and-Knowledge-Debt]]：将 assisted-output 质量与 unassisted judgment 作为两个独立 KPI；人员培养应保留无工具演练、解释性复盘和资深指导。
- **使用前提**：任何架构类比只能用于提出评测与工程变更候选；生产推广需真实权限、失败恢复、成本与回归实测。

## 重要判断（Claim / Evidence / Boundary）

- **判断**：AI 提高即时作品质量并不能自动保证专业人员的无辅助能力同比增长。
  - **证据**：一手来源 [Does better work always mean better workers?](https://research.google/blog/does-better-work-always-mean-better-workers/)，定位至「Better work with AI / When AI is removed / Further directions」及上方事实摘要。
  - **边界**：随机分配的是工具访问权而非强制实际使用强度；11 家合作律所、专利起草领域和 90 天时限限制外推。

### 关联概念

- [[Skill-Atrophy-and-Knowledge-Debt]]
- [[AI-Apprenticeship-and-Lehrwerkstatt]]
- [[Judgment]]
