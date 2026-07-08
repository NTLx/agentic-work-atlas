---
type: source-summary
title: "Getting Started with Loops — Claude Code 官方循环分类法"
source_raw:
  - "[[20260706-getting-started-with-loops-claude-code]]"
created: 2026-07-08
updated: 2026-07-08
tags:
  - source-summary
  - agentic-engineering
  - agent-loops
  - claude-code
evidence_level: high
claim_type: extracted
---

# Getting Started with Loops — Claude Code 官方循环分类法

## 编译摘要

### 1. 浓缩
- **核心结论1**: Claude Code 官方将 Loop 按触发机制和停止条件分为四种类型——Turn-based（手动 prompt 驱动）、Goal-based（`/goal`，定义可验证完成标准）、Time-based（`/loop` + `/schedule`，时间间隔驱动）、Proactive（事件/计划驱动，无人工实时参与，可组合 auto mode + dynamic workflows）
  - 关键证据: 来自 Anthropic Claude Code 团队博客（delba_oliveira 撰写），每种 loop 有明确的触发条件、停止条件、Claude Code primitive 映射和适用场景
- **核心结论2**: Loop 输出质量取决于**围绕 loop 的系统设计**而非 loop 本身——四个要素：保持代码库整洁（Claude 遵循已有模式）、给 Claude 自验证能力（编码为 SKILL.md）、文档易达（框架最佳实践）、独立 agent 做代码审查（fresh context 避免自我偏见）
  - 关键证据: "When an individual result doesn't meet the standard, don't stop at fixing the individual issue, try to encode it to improve the system for all future iterations."
- **核心结论3**: Token 管理需要分层策略——选择正确的 primitive 和模型（小任务不需要多 agent）、定义清晰的成功和停止条件、pilot before large run、用脚本替代确定性工作、匹配 routine 频率与被监控对象变化频率
  - 关键证据: `/usage` 按 skills/subagents/MCPs 分解消耗；`/goal` 无参数显示 turn 数和 token 用量；`/workflows` 显示每个 agent 的 token 用量

### 2. 质疑
- **关于分类法的普适性**: 四种 loop 类型是 Claude Code 产品视角的分类，未必是通用 agent 架构理论。其他平台（Cursor Automations、Codex）可能有不同的 loop primitive
- **关于 proactive loop 的成本控制**: Proactive loop 组合了 `/schedule` + `/goal` + auto mode + dynamic workflows，可能产生大量 agent 和 token 消耗。文章提到"pilot before large run"但缺乏具体的成本效益数据或 guardrail 示例
- **关于"用第二个 agent 做代码审查"**: 建议用独立 agent 做 code review 以减少偏见，但这引入了额外的 LLM 调用成本和延迟，且两个 agent 可能共享同样的系统性偏见

### 3. 对标
- **跨域关联1**: 与 [[Agent-Loops]] 中 Andrew Ng 的三层循环模型互补——Ng 按时间尺度和角色划分（coding / developer feedback / external feedback），ClaudeDevs 按触发-停止机制划分。两者是同一现象的不同切面
- **跨域关联2**: LangChain 四层堆叠模型（Agent loop → Verification → Event-driven → Hill climbing）按功能层级分类，ClaudeDevs 按操作原语分类。Proactive loop 大致对应 Event-driven + Hill climbing 的组合
- **跨域关联3**: SKILL.md 作为自验证工具直接映射到 [[Agent-Harness]] 的验证循环组件——skills 不只是给 Agent 的能力说明，更是 Agent 检查自身工作的 instruments
- **跨域关联4**: "Use a second agent for code reviews" 与 [[Agent-Verification]] 中的独立观察者模式一致——新鲜 context 比自我反思更可靠

### 关联概念
- [[Agent-Loops]]
- [[Agent-Harness]]
- [[Agent-Verification]]
- [[Agentic-Workflow-Token-Efficiency]]
- [[Skill-Chains]]
