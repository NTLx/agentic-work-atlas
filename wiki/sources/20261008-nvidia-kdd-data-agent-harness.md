---
type: source-summary
title: "Building Reliable Data Analytics Agents: Lessons from the KDD Cup"
canonical_url: "https://developer.nvidia.com/blog/building-reliable-data-analytics-agents-lessons-from-the-kdd-cup/"
raw_state: index
original_raw_file: "20261008-nvidia-kdd-data-agent-harness.md"
original_body_sha256: "c2465c035059338bf29fe5dedcd87f79af0378d1534349b5321208db90190385"
indexed_at: "2026-11-06T00:57:55.293Z"
created: 2026-11-06
updated: 2026-11-06
tags:
  - source-summary
  - data-analytics
evidence_level: medium
claim_type: mixed
source_locator:
  - "Original article section: Two principles behind the system"
  - "Original article section: 1. Convert structured sources into one query surface"
  - "Original article section: 2. Seed the agent with schema context up front"
  - "Original article section: 3. Build a small, opinionated tool harness"
  - "Original article section: 4. Treat prose as a first-class input, but keep it separate from structured data"
  - "Original article section: 5. Preprocess video when it is part of the task"
  - "Original article section: 6. Log traces so another agent or a human can inspect failures"
  - "Original article section: 7. Evaluate multiple attempts, but watch the cost"
  - "Original article section: 8. Use improvement loops carefully"
  - "Original article section: 9. Keep humans in the right part of the loop"
---

# Building Reliable Data Analytics Agents: Lessons from the KDD Cup

> 证据来源：https://developer.nvidia.com/blog/building-reliable-data-analytics-agents-lessons-from-the-kdd-cup/（2026-10-08，Eduardo Rocha de Andrade、Jiwei Liu、Maximilian Jeblick、Raja Biswas、Isabel Hulseman）。2026-11-06 读取官方网站公开正文并逐节核对。原文以 canonical URL 为权威；本 Wiki 保存自撰释义、章节定位和推理边界，不存储网页逐字全文；original_body_sha256 仅记录临时来源索引记录的哈希，**不是**网页全文校验值。**本文数据若未注明独立验证，均为该来源的报道/作者陈述。**

## 编译摘要

### 1. 浓缩

- **核心结论 1：小模型的可靠分析更依赖有约束的操作界面，而不是放开更多工具。**
  - **原文证据**：NVIDIA KGMON 在 KDD Cup 2026 Data Agents 竞赛排名第二；赛制要求固定较小 LLM。团队把 CSV/JSON 和已有 SQL 数据集中到 SQLite，用 schema() 与 sql(query) 统一结构化访问，先执行 schema scout 排查 join key、粒度、null 与同名字段，再进入主推理。

- **核心结论 2：把非结构化证据纳入分析，但不把整篇文档注入主上下文。**
  - **原文证据**：受控预览/正则搜索定位证据，再由 prose_helper 用独立模型调用返回具体事实或重复记录表；视频则预处理音轨、关键帧与时间对齐。单一 write_answer(df) 确保最终输出路径，持久 Python state 和工具修复中间件减少损坏。

- **核心结论 3：将 traces、重复尝试和人为审核用于有限度自进化。**
  - **原文证据**：每次运行保存 SQL、工具、结果和修复 trace；Inspector 定位首次偏离步骤。多尝试按答案值进行投票并考虑额外成本；作者警告训练样例硬编码、脆弱修补和 benchmark overfit，主张 held-out tasks 与人工验收。

### 2. 质疑与证据边界

- 竞赛成绩来自作者团队叙述，不构成跨任务或生产可靠性的独立证明。
- SQLite 只是竞赛内统一临时分析界面，不表示生产数据仓库应迁往 SQLite。
- 文档表抽取适合特定题型，重复尝试与视觉预处理存在成本和规模门槛。

### 3. 对标与应用约束

- **跨域迁移（综合判断，非原文证实）**：适用于 [[Agentic-Analytics]] 和 [[Agent-Harness]]：可将 preflight 数据契约、受限查询面、原子答案写入、审计轨迹与 held-out regressions 作为分析 Agent 的验收基线。
- **使用前提**：任何架构类比只能用于提出评测与工程变更候选；生产推广需真实权限、失败恢复、成本与回归实测。

## 重要判断（Claim / Evidence / Boundary）

- **判断**：小模型的可靠分析更依赖有约束的操作界面，而不是放开更多工具。
  - **证据**：一手来源 [Building Reliable Data Analytics Agents: Lessons from the KDD Cup](https://developer.nvidia.com/blog/building-reliable-data-analytics-agents-lessons-from-the-kdd-cup/)，定位至「Two principles behind the system / 1. Convert structured sources into one query surface / 2. Seed the agent with schema context up front / 3. Build a small, opinionated tool harness」及上方事实摘要。
  - **边界**：竞赛成绩来自作者团队叙述，不构成跨任务或生产可靠性的独立证明。

### 关联概念

- [[Agentic-Analytics]]
- [[Agent-Harness]]
- [[Agent-Verification]]
