---
type: source-summary
title: "A Field Guide to Fable: Finding Your Unknowns"
source_raw:
  - "[[20260703-fable-field-guide-finding-unknowns]]"
created: 2026-07-03
updated: 2026-07-03
tags:
  - source-summary
  - agentic-coding
  - unknowns
  - human-agent-collaboration
  - fable-5
evidence_level: high
claim_type: extracted
---

# A Field Guide to Fable: Finding Your Unknowns

## 编译摘要

### 1. 浓缩
- **核心结论1**: Agentic Coding 的核心技能不是 prompt engineering，而是"发现和管理未知物的能力"。作者将未知物分为四象限——Known Knowns（prompt 中已写明）、Known Unknowns（知道自己不知道）、Unknown Knowns（太显然以至于不会写下来，但看到就认得出）、Unknown Unknowns（完全未考虑的维度）。Fable 5 是第一个让工作质量瓶颈从"模型能力"转移到"用户澄清未知物能力"的模型。
  - 关键证据: 作者用 Fable 5 完全通过 Claude Code 编辑了 Fable 发布视频，从零学习视频编辑、转录、调色，每一步都通过"发现未知物"推进。
- **核心结论2**: 未知物管理贯穿实现全周期——实现前（Blind Spot Pass / Brainstorm / Interview / Reference / Implementation Plan）、实现中（Implementation Notes 记录偏差）、实现后（Pitch + Quiz 验证理解）。每种技术都对应特定类型的未知物。过细的指令让 Agent 无法在必要时转向；过粗的指令让 Agent 按行业惯例做不适合的假设。
  - 关键证据: "Blind Spot Pass"直接问 Claude 找出你的 Unknown Unknowns；"Interview"让 Claude 逐个提问，优先问会改变架构的模糊点。
- **核心结论3**: 最好的 Agentic Coder 相对未知物很少——他们与代码库和模型行为深度同步。但即使最好的人也有未知物，减少和规划未知物是可以练习的技能。每次 brainstorm、interview、prototype、reference 都是"在修复变贵之前发现你不知道的东西"的低成本手段。
  - 关键证据: 作者引用 Boris Cherny 和 Jarred Sumner 的 prompt 习惯作为"未知物极少"的标杆。

### 2. 质疑
- **关于"四象限框架"的普适性**: Rumsfeld 的 Known/Unknown 矩阵是认知框架而非工程方法。作者将其映射到 Agentic Coding 是创造性应用，但四象限之间的边界在实践中可能模糊——"Unknown Knowns"和"Unknown Unknowns"的区分依赖自我觉察，而自我觉察本身可能是未知的。
- **关于"Quiz 验证"的局限**: "只在通过测验后才 merge"假设 Claude 的测验能覆盖关键行为。但对于深层逻辑错误或跨模块副作用，测验可能也无法覆盖。
- **关于 Fable 5 的特殊性**: 作者称 Fable 5 是"第一个"转移瓶颈的模型，但未对比其他模型。这种判断可能受用户近期体验偏差影响。

### 3. 对标
- **跨域关联1**: "Unknown Knowns"（太显然以至于不写下来）直接对应知识管理中的"隐性知识"（Polanyi）。作者的解决方案——brainstorm + prototype + interview——本质上是"将隐性知识显性化"的 Agent 辅助版本。这与知识系统层面的"知识编译"命题形成闭环。
- **跨域关联2**: "Implementation Notes 记录偏差"与 SGLang 的 Loop Engineering（记录失败尝试 + 重验证）结构同构——都是通过持久化执行历史来控制 Agent 的状态漂移。
- **跨域关联3**: "Quiz 验证"与 Skill Engineering 中的 Verification 类 Skill 功能重叠——都是在 Agent 产出后强制人类理解并确认。但 Quiz 的独特之处在于它同时是"知识转移"和"质量门禁"。

### 关联概念
- [[Unknowns-Framework]]
- [[Agentic-Coding]]
- [[Context-Engineering]]
- [[Human-Agent-Collaboration]]
- [[Skill-Engineering]]
