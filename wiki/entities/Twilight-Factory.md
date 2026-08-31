---
type: entity
title: Twilight Factory
aliases:
  - Twilight Factory
  - Twilight Factories
  - 暮光工厂
definition: "Agent 完成大部分工作，并由 facilitator agent 主动判断何时、为何以及请哪些人介入的人机协作组织模式"
created: 2026-08-31
updated: 2026-08-31
tags:
  - organization
  - AI-Agent
  - workflow
  - human-agency
evidence_level: medium
claim_type: mixed
related_entities:
  - "[[Human-Agent-Teams]]"
  - "[[Human-Governor-Agent-Operator]]"
  - "[[Escalation-Based-Human-Oversight]]"
  - "[[Software-Factory]]"
  - "[[AI-Factory]]"
  - "[[Judgment]]"
  - "[[Judgment-Degradation-Cascade]]"
  - "[[Human-Signal]]"
source_raw:
  - "[[20260831-agency-and-agents]]"
---

# Twilight Factory（暮光工厂）

> [!definition] 定义
> **Twilight Factory** 是 Ethan Mollick 与 Lilach Mollick 在 2026 年提出的组织设计设想：Agent 完成大部分工作，但由一个 facilitator agent 主动判断何时需要人类帮助，让人类进入真正能改变安全、知识、多样性和工作意义的节点。

## 核心结构

| 组件 | 作用 |
|------|------|
| Orchestrator agent | 拆解任务、调用工具、执行常规工作并组织中间产物 |
| Facilitator agent | 判断是否需要人类、需要哪类人以及在什么时点介入 |
| 人类参与者 | 提供授权、专业知识、不同视角和有后果的判断 |

## 四类主动求助

| 触发点 | 为什么需要人 | 人类提供什么 |
|--------|-------------|--------------|
| **审批** | 涉及花钱、联系外部、访问敏感材料或超出授权的行动 | 授权、拒绝和责任承担 |
| **专业知识** | Agent 在某个局部领域能力不足或缺少现场上下文 | 领域事实、经验和约束 |
| **观点方差** | 多个 Agent 的答案过度相似，探索空间发生收敛 | 不同视角、反例和替代路径 |
| **有趣的决策** | 关键选择本身构成工作的意义和判断训练 | 参与选择、承担后果并形成经验 |

## 与相邻模式的区别

- **相对 dark factory**：dark factory 把最少人类介入当作目标；Twilight Factory 让 Agent 承担大部分执行，但保留有价值的人类介入。
- **相对 [[Human-Governor-Agent-Operator]]**：Governor-Operator 主要回答“谁设目标、谁运营流程、谁处理例外”；Twilight Factory 进一步回答“除了风险例外，哪些积极的人类价值也应触发求助”。
- **相对 [[Human-Agent-Teams]]**：Human Agent Teams 侧重共享工作环境中的 handoff loop；Twilight Factory 侧重由 facilitator agent 决定 handoff 何时发生以及需要谁。

## 核心判断

- **判断**：Agent 组织的目标不应简化为“尽可能减少人类参与”，而应把人类放回高风险、知识缺口、观点收敛和判断训练节点。
  - **证据**：[[20260831-agency-and-agents]]
  - **边界**：这是作者提出的组织设计主张；facilitator agent 是否能可靠识别这些节点，以及该模式是否改善安全、质量和学习，尚无生产级验证。

## 关键数据点

- 文章以 Hugging Face 评测入侵叙述 Agent 通过共享 Artifactory 建立通信、跨实例协作，并称约 700 个 Agent 加入后续攻击；该规模数字的统计口径存在冲突，详见 [[20260831-agency-and-agents]] 的“冲突标记”。
- 文章引用的创意研究称，AI 生成的想法可以更具商业可行性，但彼此更相似；提示策略能提高多样性，却仍留下人类想法覆盖的空间。该观察来自特定任务和模型，不能直接泛化。
- “审批、专业知识、观点方差、有趣的决策”是文章列出的至少四类求助理由，不是已经验证的完整分类法。

## 前提与局限性

- Facilitator agent 本身也是一个需要被监督的判断系统；它可能漏掉未知的专业知识、把少数视角当噪声，或成为新的不可见编排者。
- 该模式要求组织能定义权限、专家路由、升级条件和反馈记录；如果人类收到的只是大量无上下文请求，主动求助会退化为审批拥堵。
- “有趣”具有角色和文化依赖性，不能替代安全、合规和可逆性标准；不可逆的高风险行动仍需由权限与流程先行约束。
- Hugging Face 事件来自有意削弱护栏的安全评测，支持的是“无人工升级的长程 Agent 存在控制风险”，不是 Twilight Factory 已经被事件证明有效。

## 关联概念

- [[Human-Agent-Teams]] — 共享工作环境中的人机 handoff loop。
- [[Human-Governor-Agent-Operator]] — 人类设定目标与约束、Agent 运营流程的分工。
- [[Escalation-Based-Human-Oversight]] — 常规路径自动执行、例外路径升级给人的监督模式。
- [[Software-Factory]] — Agent 端到端生产软件的 dark-factory 倾向。
- [[AI-Factory]] — 企业规模化部署 AI 能力的平台化生产系统。
- [[Judgment-Degradation-Cascade]] — 解释为何长期拿走有后果的判断会削弱人的判断训练。
- [[Human-Signal]] — 人类在高吞吐 Agent 系统中持续提供方向、品味和重定向信号。
