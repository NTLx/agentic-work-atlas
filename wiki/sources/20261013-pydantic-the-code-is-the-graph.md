---
type: source-summary
title: "The code is the graph | Pydantic"
canonical_url: "https://pydantic.dev/articles/the-code-is-the-graph"
original_raw_file: "20261013-pydantic-the-code-is-the-graph.md"
body_sha256: "15b34a121bb842c311a1e2ce64e32c2fb62ce1380360746c70c8d73d7f46df4e"
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

# The code is the graph | Pydantic

## 编译摘要

### 1. 浓缩
- **作者主张把 Agent 编排表达为普通代码**：函数、条件、循环、异常和 `asyncio.gather` 已能表达分支、重试、并行与汇合；作者认为通用 graph library 会增加第二套状态表示，令调试、类型检查和 Agent 生成代码更复杂（“Every graph fights the call stack”）。
- **类型安全、并行与节点边界快照之间存在状态合并难题**：并行分支若共享并修改状态，持久化需要定义冲突更新如何合并；类型系统可以检查函数签名，却不能证明 reducer 满足交换性或跨字段不变量。作者将不同框架的取舍概括为：并行加快照但把语义移到 reducer、类型加快照但顺序执行、类型加并行但不提供自身快照（“Typed, snapshotted, parallel: pick two”）。
- **耐久执行和沙箱被放到运行时边界处理**：文章以 Temporal 的活动回放和作者的 Monty 解释，普通代码可以由外部引擎重放，或在无 OS 资源的解释器中暂停于宿主函数调用；调用边界仍需明确副作用和重试安全性（同节）。
- **Agent 编排工作会更偏向问题形式化和评测**：作者把工程师的价值描述为选择优化指标、约束和 eval，并让 Agent 快速迭代；这属于作者立场，而非文中比较实验的结论（“Introduction”）。

### 2. 质疑
- **这是供应商观点文章**：作者参与构建 Pydantic Graph、Monty 与 Pydantic AI Harness，论证能说明设计取舍，但不能视为对所有 graph API 的中立比较。
- **“CAP theorem”是类比而非形式化定理**：文章提供状态一致性推理，但没有形式化证明所有图系统都无法同时实现类型、并行和快照；不同语义、事务模型或受限状态更新可能改变取舍。
- **普通代码并不会自动带来耐久性**：仍需执行引擎提供 replay/snapshot、定义副作用边界、保证确定性，并处理外部调用重试；可读代码本身不能解决分布式失败。
- **沙箱的执行能力和限制需独立验证**：Monty 的资源隔离、恢复成本和生产可用性是产品主张，文章未提供独立安全评估或广泛负载数据。

### 3. 对标
- **与 Google ADK 优化案例互补**：Google 展示 Agent 使用仓库规则、测试和基准做现存代码优化；Pydantic 讨论工作流本身如何表达、执行和恢复。共同关注点是把 Agent 的灵活性约束在可检查的工程接口内。
- **对 Agent Harness 的启示**：当控制流随任务变化时，让 Agent 编写受类型检查的普通程序可能比预先固定图更直接；固定流程、可审计状态转换或需要节点级恢复的场景仍可能适合显式图运行时。

### 证据定位
- “Introduction”：作者关于问题定义、指标、约束与 eval 的判断。
- “Every graph fights the call stack”：Python 控制流和 graph library 状态表示对比。
- “Typed, snapshotted, parallel: pick two”：并发状态更新、reducer、Temporal 与 Monty 的取舍。
- “Long live graphs”：Pydantic AI Harness 的动态工作流和 trace 例子。

### 关联概念
- [[Agentic-Engineering-Patterns]]
- [[Agent-Harness]]
