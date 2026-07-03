---
type: source-summary
title: "Lessons from building Claude Code: How we use skills"
source_raw:
  - "[[20260703-anthropic-skill-engineering-practices]]"
created: 2026-07-03
updated: 2026-07-03
tags:
  - source-summary
  - skill-engineering
  - agentic-engineering
  - claude-code
evidence_level: high
claim_type: extracted
---

# Lessons from building Claude Code: How we use skills

## 编译摘要

### 1. 浓缩
- **核心结论1**: Skill 不是"markdown 文件"，而是包含脚本、资产、数据的文件夹。Anthropic 内部将数百个 Skill 归纳为 9 类：Library/API Reference、Product Verification、Data Fetching、Business Process Automation、Code Scaffolding、Code Quality/Review、CI/CD、Runbooks、Infrastructure Operations。最好的 Skill 只聚焦一类，试图做太多的会混淆 Agent。
  - 关键证据: Product Verification 类 Skill 对 Claude 输出质量的提升最可量化，值得工程师花一周专门打磨。
- **核心结论2**: Skill 设计的核心原则——Gotchas 是最高信号内容（从 Claude 实际失败中积累）、Description 写给模型而非人类（是触发条件而非摘要）、文件系统即渐进式披露（SKILL.md 指向 references/scripts/assets，Agent 按需读取）、不要过度指令化（给信息而非流程）。
  - 关键证据: Gotcha 示例："subscriptions 表是 append-only，你要的行是 version 最高的那条，不是 created_at 最新的"。
- **核心结论3**: Skill 的分发和治理走有机增长路径——无集中审批团队，先在 sandbox folder 试用，有 traction 后 PR 进 marketplace。On-demand hooks（如 `/careful` 阻止危险操作、`/freeze` 限制编辑范围）是按需激活的安全机制。Skill 内可存储日志/JSON/SQLite 实现"记忆"，`${CLAUDE_PLUGIN_DATA}` 提供稳定数据目录。
  - 关键证据: PreToolUse hook 日志揭示哪些 Skill 被过度/不足触发。

### 2. 质疑
- **关于"9 类分类法"的质疑**: 这是 Anthropic 内部的分类，可能偏向 coding agent 场景。对于非编程类 Agent（如数据分析、内容创作、客服），分类可能需要调整。
- **关于"Gotchas 是最高信号"的质疑**: Gotcha 积累依赖 Claude 的实际失败记录，但 Claude 的失败模式会随模型迭代改变。一个为 Sonnet 写的 gotcha 可能对 Fable 5 无效。Skill 的维护成本可能被低估。
- **关于"有机 marketplace"的质疑**: 无集中治理在小团队有效，但随着 Skill 数量增长，质量控制、安全审计、重复 Skill 合并可能成为问题。Pinterest MCP registry 的经验表明，生产级工具生态最终需要治理层。

### 3. 对标
- **跨域关联1**: Skill 的 9 类分类与 SGLang 的 Skill 体系（CUDA 调试、benchmark、profiling、production triage 等）形成对照——SGLang 的分类更偏"性能优化"垂直，Anthropic 的更偏"通用开发"水平。两者都验证了"Skill 是可执行的开发知识"这一核心命题。
- **跨域关联2**: "文件系统即渐进式披露"与 Context Engineering 中的"信息分层注入"思路一致——不在 prompt 中塞满所有信息，而是让 Agent 按需探索。这与人类"按需查阅文档"的认知模式匹配。
- **跨域关联3**: "Description 写给模型而非人类"揭示了 Agent 时代的一个根本转变——文档的首要读者不再是人，而是模型。这对技术写作的范式有深远影响。

### 关联概念
- Skill-Engineering（待建 entity）
- [[Context-Engineering]]
- [[Progressive-Disclosure]]
- [[Agent-Harness]]
