---
type: source-summary
title: "Measurements for understanding the pace of AI development inside frontier labs"
canonical_url: "https://www.anthropic.com/institute/measuring-pace-of-ai-development"
raw_state: index
original_raw_file: "20260922-anthropic-pace-ai-development.md"
original_body_sha256: "ba0f61fc8f9e47a68674eee66afbfbc79a33b19f7d17e389ad48ff3f3e7a56f6"
indexed_at: "2026-09-22"
created: 2026-09-22
updated: 2026-09-22
tags:
  - source-summary
  - ai-rd-automation
  - agent-oversight
  - frontier-labs
evidence_level: medium
claim_type: mixed
source_locator:
  - "(1) Measuring AI-led AI R&D：Automation Index、AL0–AL5 与 August 2026 snapshot"
  - "(2) Measuring oversight of AI agents：coverage、review latency、escalation rate"
  - "(3) Measuring compute allocation：July 13–20 compute snapshot"
  - "Appendix / Measuring AI-led R&D：15k granular tasks、542-node frozen tree、judge/human comparison"
  - "Appendix / Oversight of agents：persistent identity 与 open communication"
---

# Measurements for understanding the pace of AI development inside frontier labs

> 页面未可靠显示发布日期，因此本库文件日期使用剪藏日 2026-09-22；原文共同作者为 Marina Favaro 与 Phillie Wright。

## 编译摘要

### 1. 浓缩

- **核心结论 1：衡量“AI 改 AI”的速度需要测生产过程，而不仅是模型能力。**
  - 关键证据：Anthropic 构建 R&D Automation Index，把公司 AI R&D 拆成任务树并按 AL0–AL5 评级；截至 2026-08，Claude 未在任何测量子集达到 fully autonomous，约 26% 工作达到“AI leads”，90% 以上达到“AI collaborates”或更高。
- **核心结论 2：高规模 Agent 监督可以被拆成 coverage、review latency、escalation rate 三个可报告指标。**
  - 关键证据：其最常用内部平台在 2026-08 任一时刻约有 30,000 个 research/engineering agents；该平台动作 100% 经过 online monitor 且 100% 被 offline monitor ingest；超过十亿次决策中约 0.002% 被 online monitor 阻断，offline monitor 每周约 flag 100,000 transcripts，约 50 个最高优先级项目升级到人工。
- **核心结论 3：可公开、可复核的“发展速度”还需要资源投入指标，但 compute share 只是输入 proxy。**
  - 关键证据：Anthropic 对 7 月 13–20 日 compute snapshot 分类，报告 AI R&D compute 中约 6% 属 safety、AI-driven AI R&D compute 中约 12% 属 safety；作者明确说安全研究天然可能较少消耗 compute，因此绝对占比不能直接等同安全重视程度。

### 2. 质疑

- **关于 Automation Index 的质疑**：任务树、任务权重和自动化等级均依赖内部数据与 Claude 研究/裁判；虽然 model-human exact agreement 59%、human-human 35%，且 97% 在 ±1 level，但 borderline 分类仍有实质主观性。
- **关于 frozen basket 的质疑**：固定 2026-07 工作篮子有利于时间比较，却可能漏掉“旧工作被自动化后人类转向全新工作”的结构变化；Anthropic 做了 1–7 月 novelty check，但仍计划定期重建 basket。
- **关于 oversight 指标的质疑**：100% monitor coverage 是 instrumented platform 内的 coverage，不证明 monitor recall、false negative、对 unknown behaviors 的理解或对平台外活动的覆盖；作者也明确承认监控科学仍很年轻。
- **关于 compute allocation 的质疑**：安全/能力边界可争议，底层 workload labels 也有 best-effort 成分；一周 snapshot 不能证明长期趋势。

### 3. 对标与约束

- **与 [[Recursive-Self-Improvement]] 对标**：该来源把“RSI 已经发生多少”从宏观叙事收敛为任务篮子与自动化等级；26% AL4 与 >90% AL3+ 是比“代码多少由 AI 写”更细的过程指标，但仍不是 full recursive autonomy。
- **与 [[Agent-Observability]] 对标**：coverage、review latency、escalation rate 为行为监控层提供了直接生产指标；persistent agent identity 与 open communication 则把跨 Agent provenance 变成设计对象。
- **综合判断**：当 Agent fleet 达到数万并进入 R&D 主流程后，治理对象不再只是“单个模型是否安全”，而是“自动化比例、监控覆盖与延迟、资源配置是否随能力增长同步变化”。
- **硬约束**：外部治理若没有可验证的统一 methodology，跨实验室数字不可直接比较；内部自评需要第三方复核。
- **软约束**：compute、安全分类、review SLA 与 pacing trigger 都是可由组织和监管制度改变的治理接口。

## 证据边界

- 数据均来自 Anthropic 内部自报告，方法细节丰富但并非独立复现，因此 evidence_level 为 medium。
- “30,000 agents”仅覆盖其 most-used internal platform，不应外推为 Anthropic 全部 Agent 数量。
- “0.002% blocked”不能解释为“只有 0.002% 有风险”，因为它同时受 monitor policy、recall、行为分布和 blocking threshold 影响。
- 页面未可靠显示 publication date，本库不猜测日期。

## 关联概念

- [[Recursive-Self-Improvement]]
- [[Agent-Observability]]
- [[Distinct-Principal-Identity]]
- [[Escalation-Based-Human-Oversight]]
