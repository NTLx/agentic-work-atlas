---
type: source-summary
title: Can we trust LLMs to judge whether a research idea is novel?
canonical_url: https://allenai.org/blog/novelty-bench
raw_state: index
original_raw_file: "20261027-ai2-novelty-bench.md"
original_body_sha256: "beb83ab9d78e20f41f8c6f3d18d298d889071c1312124dda52f4cac4a8c6d3b5"
indexed_at: "2026-11-26T12:31:43+08:00"
author: Ai2
published: '2026-10-27'
created: '2026-11-26'
updated: '2026-11-26'
tags:
- source-summary
- agent-evaluation
- evaluation
- verification
evidence_level: medium
claim_type: mixed
source_locator:
- Building a benchmark for novelty judges
- Small changes can produce very different verdicts
- Toward more reliable evaluation of novel research
---

# Can we trust LLMs to judge whether a research idea is novel?

> **原文保留边界**：来源为公开网页，按 canonical URL 与章节定位结算为可恢复索引（raw_state: index）。Registry 哈希对应临时来源登记摘录（非全文），不是原网页正文或全文哈希；原文需按来源链接回查。读取与结算日期：2026-11-26。

## 编译摘要

### 1. 浓缩

- **研究新颖性必须与论文接收结果区别。** 以 ICLR 2026 审稿人明确评价原创性的记录构造 Human-Only：154 个较高新颖性、145 个较低新颖性的人类构想。Human+Generated 则配对 154 个正向人类构想与 154 个简单生成器产出的构想；后者是弱标签，非逐项真值。专家核查 30 对（偏向最强 judge 判错案例），都偏好人类构想。定位：Building a benchmark。
- **评测设置敏感。** 六个 judge 进行 pointwise/pairwise 测试；GPT-5.4 在相同 Human+Generated 对比中，告知恰好一项获得审稿原创性认可与仅询问哪项新颖，两种提示分别得到 93.5% 和 40.9% 准确率。同一模型比较的 52.6 个百分点差异包含任务提示信息改变，不能称作单纯无意义的措辞变化。比较不同 AI 生成器时，跨提示约四分之一至三分之一判决翻转。定位：Small changes。
- **更多计算不必然改进判别。** 报告的一次调用配置中，迭代搜索 judge macro-F1 0.78，简单检索配置 Opus 4.6 为 0.89，前者成本约十倍。另一组实验中，Opus 4.6 三次低推理投票为 0.854，Idea Novelty Checker 0.642、AI Scientist 0.772。两组设置不同，不宜混作同一排行榜。定位：Small changes / more search。

### 2. 质疑

审稿意见是领域内代理证据而非绝对真值，选取极端论文可能夸大区分能力；Human+Generated 的简单生成器没有文献检索或迭代，不能代表最强科研 Agent。30 对复核非随机抽样。准确率受弱标签和提示先验影响，但同一输入判决翻转不依赖标签也能证明不稳定。宏 F1、费用和调用预算均是特定实验，不可外推。研究博客及其数据/代码入口已读取，未独立运行 benchmark。

### 3. 对标

- [[Evaluator-Miscalibration]]：用多模型、多提示、顺序交换、匿名样式和重复调用评估 judge 一致性。不要向生产 judge 暗示答案分布；模型/提示变更必须重新校准。
- [[Evaluation-Integrity]]：新颖性、可行性、正确性与价值分开评估。检索需保留原文定位、检索覆盖与未检到的限制；不因没有找到先例而断言首次提出。
- [[Agent-Knowledge-Management]]、[[Meta-Harness-Optimization]]：知识候选先与既有概念和来源比较；高分不自动晋升为新 Claim。以可独立核实的反例、跨任务回归和人工审查为准入条件。优先保留简单基线，并对额外搜索/推理进行消融。

## 前提与局限性

官方研究博客链接论文、数据和代码；本轮仅依据博客报告的实验结果，不声称已复现。尤其对于生信研究，新颖性应结合专业文献、方法细节、可证伪假设及可复现实验，不能用单个 LLM 分数代替同行评议。

## 关联概念

- [[Evaluator-Miscalibration]]
- [[Evaluation-Integrity]]
- [[Agent-Knowledge-Management]]
- [[Meta-Harness-Optimization]]
