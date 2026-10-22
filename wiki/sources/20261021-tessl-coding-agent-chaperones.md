---
type: source-summary
title: "There Aren’t Enough Chaperones for All Your Coding Agents"
canonical_url: "https://tessl.io/blog/there-arent-enough-chaperones-for-all-your-coding-agents"
raw_state: index
original_raw_file: "20261021-tessl-coding-agent-chaperones.md"
original_body_sha256: "11765ef9c642863850e6486416eca1afda5a62099bbcafb817e8bfcbad9aa554"
indexed_at: "2026-10-22T09:55:17+08:00"
created: 2026-10-22
updated: 2026-10-22
tags:
  - source-summary
  - coding-agents
  - engineering-management
  - verification
evidence_level: medium
claim_type: mixed
source_locator: "正文：The agent trust problem, in two charts；The review bottleneck is an ROI problem；How to build trust faster。"
---

# There Aren’t Enough Chaperones for All Your Coding Agents

## 编译摘要

### 1. 浓缩

- **核心结论 1**：Coding Agent 的 adoption 已明显快于 autonomous review / merge。文章引用 Jellyfish 的 2026-09 数据：覆盖约 30 万工程师、1,300 家公司和 1 亿+ PR；中位公司已有 22% 的 merged PR 由 autonomous agent 参与作者工作，90 分位达到 53%，但“无人工 review 直接由 agent review+merge”的比例中位数只有约 0.6%，前 10% 公司约 9%。
- **核心结论 2**：这形成一个结构性 review bottleneck：上游代码生成吞吐增长快于下游验证吞吐。作者称 2026 年整体 PR 数约翻倍，而 features shipped 等产品输出只增加约 40–50%；agent-authored PR 的 abandon rate 约 40%，人类 PR 约 20%，而成功 merge 的 agent PR 所需 human reviews 在一年内增加到两倍以上。
- **核心结论 3**：问题不是“人类审查是否合理”，而是如果每个 Agent 产物都必须按同等强度人工检查，Agent throughput 会把稀缺的人类 attention 变成系统上限。
- **核心结论 4**：作者观察到自治比例较高的团队并不是直接取消监督，而是先做平台化：按风险 routing 工作、sandbox/staging、自动化测试，再逐步放宽 human gate。也就是先提高可验证性与可控性，再提高 autonomy。

### 2. 质疑

- 数据来自 Jellyfish 平台覆盖的客户样本，不能当作全球软件行业的随机样本；“median company”只代表该观测集合。
- “autonomous agent activity”“agentically merged PRs”“product output”等指标依赖 Jellyfish 的内部识别和归因口径，文章没有给出完整 measurement methodology 或置信区间。
- PR 数量翻倍与产品输出增长较慢之间存在相关性，但文章没有做因果识别；需求结构、团队规模、产品周期或宏观变化都可能解释一部分差异。
- agent PR abandon rate 高不一定意味着 Agent 质量差两倍；Agent 可能被更多用于探索性、低成本、可放弃任务。

### 3. 对标与约束

- **与 [[AI-Native-Engineering-Org]] 的连接**：该来源为“生成不再是主要瓶颈，review/verification 成为新瓶颈”提供了罕见的大样本生产数据锚点。
- **与 [[Software-Development-Autonomy-Levels]] 的连接**：22% agent-authored PR 与 0.6% AI-only merged PR 的巨大差距，可以看作 Level I 代码自治已快速扩散、Level II 流水线自治仍被 trust/verification 约束的经验信号。
- **与 [[Agent-Verification]] 的连接**：可扩展监督的方向不是简单增加 reviewer，而是提高 low-risk routing、自动 oracle、sandbox 和 staged deployment 的覆盖率，把人工注意力留给不可自动判定的高风险变更。
- **硬边界**：任何“减少 human review”都必须按 risk class 分层；文章没有证明 9% agent-only merge 的团队在长期 defect/security/outage 指标上优于或等同于人工审查团队。

## 关联概念

- [[AI-Native-Engineering-Org]]
- [[Software-Development-Autonomy-Levels]]
- [[Agent-Verification]]
- [[Agentic-Engineering]]
