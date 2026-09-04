---
type: source-summary
title: "What is harness engineering and why should I care?"
canonical_url: "https://dev.to/googleai/what-is-harness-engineering-and-why-should-i-care-8n0"
raw_state: index
original_raw_file: "20260902-google-harness-engineering.md"
original_body_sha256: "ca4794f0599a8d40e10fa9161cd018d961d8b85089f21f9e50694eb8a9fbb096"
indexed_at: "2026-09-05T01:57:30+08:00"
created: 2026-09-05
updated: 2026-09-05
tags:
  - source-summary
  - harness
  - agentic-engineering
evidence_level: low
claim_type: mixed
---

# What is harness engineering and why should I care?

> Shir Meir Lador（DEV Community / Google AI，2026-09-02）。这是一篇实践型解释文，借助 OpenAI、Google ADK/Antigravity 和同事文章说明 harness；它适合提供设计线索，不足以独立证明产品效果或 SDK 行为。

## 编译摘要

### 1. 浓缩

- **核心结论 1：coding agent 的工程瓶颈从编写逻辑转向设计运行环境。**
  - 关键证据：文章以“3 名工程师、0 行手写代码”的 OpenAI 实验为引子，将 harness 定义为包裹 LLM 的确定性组件，并列出编排、沙箱、状态持久化和验证工具（raw 行 13–38）。
- **核心结论 2：可靠 harness 至少要把边界、修复反馈和渐进式上下文内建为结构。**
  - 关键证据：作者提出严格 sandbox 边界、把构建/测试失败日志反馈给 Agent 的 repair loop，以及“给地图而不是手册”的渐进式仓库结构（raw 行 39–43）。代码示例将工作区限制到 sandbox、把轨迹写入独立目录（行 45–81）。
- **核心结论 3：测试不是工作流外部的验收，而是 Agent 循环中的路由节点。**
  - 关键证据：ADK 2.0 示例把 test node 放进 graph；测试通过即结束，失败则把 traceback 回送 Agent，迭代次数超过 5 次触发 kill switch（raw 行 83–153）。

### 2. 质疑

- **关于来源强度的质疑**：文章主要是作者的解释和二手引用，不提供独立实验、样本、成功率或生产故障数据；“最重要的趋势”“少于五分钟”等表述属于倡议性判断。
- **关于示例可运行性的质疑**：Antigravity SDK、ADK 2.0 与示例 API 需要在目标版本中实际验证；source 中的 policy.allow_all() 只在受限 sandbox 这个更大边界内示例化，并不等于生产安全策略。
- **关于自愈的质疑**：repair loop 只能修复被测试和反馈捕获的故障；测试未覆盖的规格、数据破坏、权限越界和错误目标不会因为循环存在而自动消失。
- **关于停止条件的质疑**：固定 5 次是示例中的自设参数，不等同于所有项目的最优上限；更复杂的任务可能需要预算、风险和进展信号共同决定终止。

### 3. 对标与旁逸

#### 3a. 跨域对标

- **与 [[Agent-Harness|Agent Harness]] 的关系**：本文给出 harness 的低门槛工程实现：sandbox 是权限边界，trajectory 是状态外存，test node 是验证器，graph 是循环控制器。
- **与 [[Harness-Engineering|Harness Engineering]] 的关系**：本文把“棘轮纪律”落到三个最小组件：禁止 Agent 猜边界、把错误日志形成闭环、让仓库结构承担渐进式上下文。
- **与 [[Agent-Workflow-Patterns|Agent Workflow Patterns]] 的关系**：test node + failure feedback 是 Evaluator-Optimizer，graph route 是 Routing，sandbox 是自主 Agent 的安全前提。
- **跨域类比：航空/工业控制中的联锁**。harness 不替代决策单元，而是在危险动作前设置边界、在失败后提供可解释反馈、在失控时触发断路；迁移到生产系统时还需要权限和观测的独立验证。

#### 3b. 旁逸

“在普通聊天窗口里，人是 harness”是一个有用的边界判断：当人手动复制日志、决定下一步、替模型记住状态时，系统的可靠性来自人类临时承担的编排与验证。把这些动作外化为代码，才会形成可重复的 Agent 工作流（综合判断）。

#### 3c. 约束

- **硬约束**：Agent 能访问的文件和工具必须有明确边界；执行结果必须可反馈，循环必须有终止条件。
- **软约束**：测试覆盖、日志格式、状态目录和 repair 次数应按风险与任务类型配置。
- **自设约束**：采用 ADK graph、Antigravity 或五次上限是示例实现，不是 harness 的必要条件。

### 关联概念

- [[Agent-Harness]]
- [[Harness-Engineering]]
- [[Agent-Workflow-Patterns]]
- [[Agent-Verification]]
- [[Agent-Containment]]
- [[Context-Engineering]]
