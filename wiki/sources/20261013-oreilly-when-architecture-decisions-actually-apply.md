---
type: source-summary
title: "When Architecture Decisions Actually Apply"
canonical_url: "https://www.oreilly.com/radar/when-architecture-decisions-actually-apply/"
original_raw_file: "20261013-oreilly-when-architecture-decisions-actually-apply.md"
body_sha256: "54148e36ca321878effe740e78c42abbe397bc7fca24a6fc11b5426575965501"
indexed_at: "2026-10-24T23:52:29+08:00"
raw_state: index
created: 2026-10-24
updated: 2026-10-24
tags:
  - source-summary
  - agentic-engineering
evidence_level: low
claim_type: mixed
---

# When Architecture Decisions Actually Apply

## 编译摘要

### 1. 浓缩
- **检索相关决策不等于决策对当前变更有约束力**：Agent 还需要判断 decision 的 scope、lifecycle 和 precedence，确定它是否适用于正在修改的 artifact；否则相关文件可能被当作可权衡材料，丢失其权威性（“Retrieval finds; applicability governs”）。
- **适用性也不代表可自动阻断**：明确可观察的禁令（如禁止在某组件引入 SQLAlchemy）较适合确定性检查；“正确使用现有持久化抽象”往往是需要上下文判断的正向指导，不宜在证据边界不清时做二元阻断（“Blocking is easier than guiding”）。
- **小型受控实验显示指导提升架构合规，但不提升任务完成率**：七项任务在有/无决策上下文两种条件下重复；架构敏感任务的首次尝试合规从 15 次运行中的 6 次升至 10 次，任务完成基本不变。作者还报告相关决策曾诱发 Agent 扩大任务范围，说明决策适用性不等于授权新增工作（“What scope changed”）。
- **确定性执法必须让结果可复现和可解释**：一旦系统给出 blocking verdict，工程师应能知道哪条决定适用、适用范围、触发证据，以及相同检查是否会给另一位开发者相同结果（“When judgment becomes authority”）。

### 2. 质疑
- **实验规模很小**：七项任务、15 次运行的数字不足以概括不同仓库、模型或架构决策类型；文章未给出完整任务集与统计不确定性。
- **实验由作者设计和解读**：结果有助于发现“相关性/权威性”和“指导/阻断”的区分，但尚不足以证明其建议在广泛生产环境的效果。
- **决策作用范围并非总能形式化**：scope、生命周期、优先级可能跨越代码、部署配置和组织惯例；作者引用研究也承认后两类知识令模型更难判断。
- **拒绝所有模糊自动化会损失辅助价值**：模型仍可检索、解释、指出潜在冲突和建议路径；边界是不要把概率判断伪装成确定阻断。

### 3. 对标
- **与 Tessl 软件工厂开放性互补**：Tessl 强调 context 应携带来源、权限和关系；本篇进一步要求系统表达哪些 decision 对哪个 artifact 有 authority，以及何种判断可执行。
- **与 Google ADK 案例互补**：仓库 skills/规则帮助 Agent 了解维护约定，但需要人工 review 判断边界变更和质量；本篇说明规则的适用范围与确定性强度应分别建模。

### 证据定位
- “Retrieval finds; applicability governs”：决策检索、scope、lifecycle 与 precedence。
- “What scope changed”：受控实验、6/15 至 10/15 与任务扩张现象。
- “Blocking is easier than guiding”：负向禁止和正向指导的可执行性差异。
- “When judgment becomes authority”：阻断结果的可解释、可复现要求。

### 关联概念
- [[Agentic-Engineering-Patterns]]
- [[Agent-Knowledge-Management]]
