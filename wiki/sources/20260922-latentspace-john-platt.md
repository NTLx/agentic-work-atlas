---
type: source-summary
title: "An Oscar, Two Asteroids, and the Algorithm in Your sklearn: John Platt on AI for Science"
canonical_url: "https://www.latent.space/p/john-platt"
raw_state: index
original_raw_file: "20260922-latentspace-john-platt.md"
original_body_sha256: "8f21491a314e38c132df378260014169513076e7ecc4d13185fa1e7516501f46"
indexed_at: "2026-09-23T11:43:35+08:00"
created: 2026-09-23
updated: 2026-09-23
tags:
  - source-summary
  - ai-for-science
  - scientific-discovery
  - goodhart
evidence_level: medium
claim_type: mixed
source_locator:
  - "00:03:25–00:20:20：ERA、scorable tasks、specialized harness、MCTS/UCB、shared exploration history"
  - "00:22:27–00:40:34：predictive vs descriptive、multiple-hypothesis testing、hidden holdouts、Goodhart、human outer loop"
  - "01:33:39–01:38:17：training vs exploit、20% time、不要 overfit productivity、rigor/domain knowledge"
  - "01:59:28–02:00:49：AI-for-science human role 与 everything lab physical bottleneck"
---

# An Oscar, Two Asteroids, and the Algorithm in Your sklearn: John Platt on AI for Science

> Latent Space Science 访谈，John Platt 为 Google Fellow、Google Research Head of Applied Science。编译时 Raw 保存了约 2 小时 1 分钟公开 transcript；结算为 index 后，Source Summary 与 Registry 保留正文哈希、时间定位和 speaker provenance。

## 编译摘要

### 1. 浓缩

- **核心结论 1：ERA 展示了一条“先把科研问题变成可评分任务，再让 LLM 引导搜索可执行方案”的 AI-for-Science 路线。**
  - 关键证据：Platt 介绍 ERA 时说，许多科研问题可以重写为“写一段使某个 score 最大化的代码”；系统先帮助科学家定义 scorable task，再在 specialized harness 中维护数百到数千个 notebook 候选，用 Monte Carlo Tree Search / UCB 选择、变异与重组候选。并行度默认约 10 个叶节点，以平衡并行搜索与从上一批试验中学习（00:04:16–00:14:42）。
- **核心结论 2：代码搜索越强，人的稀缺工作越向上游迁移到 score 定义、科学解释与独立验证。**
  - 关键证据：Platt 明确说 score 往往不是第一天就能定义正确，Agent 会找到“cheat or hole”，科学家需要不断重写 scoring function；对 descriptive science，还必须处理 multiple-hypothesis testing、false discovery、隐藏 holdout 与 extrapolation，不能把 predictive fit 直接等同于“世界就是这样”（00:15:01–00:18:13；00:22:27–00:34:26）。
- **核心结论 3：当前 ERA 仍是计算闭环，不是端到端实验科学闭环。**
  - 关键证据：访谈末尾 Platt 把自己最想消除的瓶颈描述为一个可接收 JSON、自动执行任意实验的 “everything lab”；他强调当前 ERA “it's all computational”，现实世界数据仍需要人或实验设施采集（02:00:21–02:00:49）。

### 2. 质疑

- **关于泛化性的质疑**：这是项目负责人对自身系统的长访谈，不是跨学科对照实验。ERA 在哪些科学领域、何种任务分布上稳定优于专家工作流，访谈没有给出系统性测量。
- **关于 scoreability 的质疑**：能被压成 executable score 的任务天然更适合 ERA；“什么是好理论”“哪个问题值得问”等开放问题不一定存在稳定 score。Platt 自己也说，当前系统还不能真正独立发现“completely new physics or completely new science”（约 00:31:44–00:31:59）。
- **关于模型进步的质疑**：Platt 认为 Gemini 2.0 时几乎不可行、后续版本突然变得有用，这是经验性判断；访谈没有给出控制变量一致的版本消融，不能据此量化模型升级带来的科学产出增益。
- **关于人类角色的质疑**：“科学家不会被替代、会转向创造性/严谨性/哲学性工作”是受访者的预测与规范性期待，不是已建立的劳动市场事实。
- **关于防 Goodhart 的质疑**：隐藏 holdout、简单基线和多层 rigor 能降低自欺风险，但不能消除 proxy 与 scientific truth 之间的结构性差距。

### 3. 对标与约束

- **与 [[Scientific-Discovery-AI]] 对标**：ERA 为已有“组合搜索 + objective”路线补充了更具体的 Agentic 实现：问题表述 → scoring contract → LLM 生成/变异 notebook → tree search/UCB → executable evaluation → human scientific adjudication。它的关键不是随机 evolutionary search，而是 LLM 的世界知识、代码能力和共享试验历史共同提供“有方向的变异”。
- **与 [[Goodharts-Law]] 对标**：同一个 score 既是 Agent 的控制接口，也是最直接的攻击面。ERA 原型源于 Auto-Kaggle；Platt 用 contrail competition 的半像素标签偏差说明，人类和 Agent 都会沿指标漏洞优化，并明确指出每个 leaderboard 都会重新引入 Goodhart 风险（00:35:11–00:37:28）。
- **硬约束**：predictive performance 不等于 descriptive truth；高吞吐搜索必须绑定独立 holdout、外部科学知识和可复核实验。
- **物理边界**：如果真实世界实验、传感和数据采集没有自动化，科研 Agent 仍只能加速计算部分，无法形成完整的 autonomous discovery loop。
- **组织边界**：Platt 保护 20% time 的经验提醒，组织若把所有时间都压向短期可测生产率，也可能“overfit to productivity”；这一点更适合作为组织设计假设，而非本文主结论。

## 证据边界

- 证据主要来自受访者本人对 Google Research / ERA 实践的一手描述，适合支持机制和设计模式判断，但项目效果数字缺乏独立复现，因此 evidence_level 为 medium。
- Transcript 为公开自动转录，个别专有名词存在识别误差；本 Summary 只使用上下文高度明确的机制与时间段。
- 访谈中的科学、量子计算、融合能源等大量旁支未全部沉淀，避免把单篇来源扩张成多领域知识图谱。

## 关联概念

- [[Scientific-Discovery-AI]]
- [[Goodharts-Law]]
- [[Agent-Harness]]
- [[Agent-Verification]]
- [[Taste]]
