---
type: source-summary
title: "Lessons from building Claude Code: How we use skills"
source_raw:
  - "[[20260703-anthropic-skill-engineering-practices]]"
created: 2026-07-03
updated: 2026-11-28
canonical_url: "https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills"
raw_state: full
tags:
  - source-summary
  - skill-engineering
  - agentic-engineering
  - claude-code
evidence_level: medium
claim_type: mixed
---

# Lessons from building Claude Code: How we use skills

## 编译摘要

### 1. 浓缩
- **核心结论1**: Skill 不是"markdown 文件"，而是包含脚本、资产、数据的文件夹。Anthropic 内部将数百个 Skill 归纳为 9 类：Library/API Reference、Product Verification、Data Fetching、Business Process Automation、Code Scaffolding、Code Quality/Review、CI/CD、Runbooks、Infrastructure Operations。最好的 Skill 只聚焦一类，试图做太多的会混淆 Agent。
  - 关键证据: 作者报告 Product Verification 类 Skill 在其内部使用中对输出质量的影响最易测量，建议投入工程时间；未披露比较数据或通用收益，不能由此推出固定一周投入的回报。
- **核心结论2**: Skill 设计的核心原则——Gotchas 是最高信号内容（从 Claude 实际失败中积累）、Description 写给模型而非人类（是触发条件而非摘要）、文件系统即渐进式披露（SKILL.md 指向 references/scripts/assets，Agent 按需读取）、不要过度指令化（给信息而非流程）。
  - 关键证据: Gotcha 示例："subscriptions 表是 append-only，你要的行是 version 最高的那条，不是 created_at 最新的"。
- **核心结论3**: Skill 的分发和治理走有机增长路径——无集中审批团队，先在 sandbox folder 试用，有 traction 后 PR 进 marketplace。On-demand hooks（如 `/careful` 阻止危险操作、`/freeze` 限制编辑范围）是按需激活的安全机制。Skill 内可存储日志/JSON/SQLite 实现"记忆"，`${CLAUDE_PLUGIN_DATA}` 提供稳定数据目录。
  - 关键证据: PreToolUse hook 使用日志可辅助发现调用频率与预期不符；触发频率不等于任务质量或增量效用。Hook 例子仅为当时产品能力与团队实践，不保证所有执行路径受控。

### 2. 质疑
- **关于"9 类分类法"的质疑**: 这是 Anthropic 内部的分类，可能偏向 coding agent 场景。对于非编程类 Agent（如数据分析、内容创作、客服），分类可能需要调整。
- **关于"Gotchas 是最高信号"的质疑**: Gotcha 积累依赖 Claude 的实际失败记录，但 Claude 的失败模式会随模型迭代改变。一个为 Sonnet 写的 gotcha 可能对 Fable 5 无效。Skill 的维护成本可能被低估。
- **关于"有机 marketplace"的质疑**: 无集中治理在小团队有效，但随着 Skill 数量增长，质量控制、安全审计、重复 Skill 合并可能成为问题。Pinterest MCP registry 的经验表明，生产级工具生态最终需要治理层。

### 3. 对标
- **跨域关联1（综合）**: Skill 文件夹将指令、参考资料与可执行脚本组合，可与软件设计模式及垂直工程知识复用比较；不能将两个团队的不同分类视为受控对照或质量证明。
- **跨域关联2**: "文件系统即渐进式披露"与 Context Engineering 中的"信息分层注入"思路一致——不在 prompt 中塞满所有信息，而是让 Agent 按需探索。这与人类"按需查阅文档"的认知模式匹配。
- **跨域关联3（综合）**: Skill description 是供模型选择能力的触发说明，同时应保持人类可审查性；不代表所有文档首要读者都变成模型。

## 来源身份与历史归并（2026-11-28）

- Canonical source：Thariq Shihipar，2026-06-03，原文同一 URL。保留 2026-07-03 捕获的 123 行 Raw（含完整九类说明、设计建议、hooks、分发及度量）。2026-06-10 捕获的 34 行短摘录（旧文件名 20260603-lessons-from-building-claude-code-how-we-use-skills.md）没有独立事实增量；旧摘要中的九类、四原则与设计模式/UI 信息架构类比已覆盖。早期来源为同一篇文章而非独立证据，原 Raw 正文哈希 fd42e8e2d96875f54c045014a12bb2328074b66cba658f4d9da496f595245eaf；原捕获及摘要历史可从 Git 基线 c973054776142aa1e482199f3cde9d4fdd927433 回查。
- 来源定位：原文 `Types of skills`、`Tips for making skills`、`Distributing skills`、`Managing a skills marketplace`、`Composing skills`、`Measuring skills`。九类是内部经验分类，Gotchas、按需披露、脚本、触发描述和治理是可检验的设计建议；保留可重复任务的质量、失败率、维护成本和实际调用结果作为验证对象。

### 关联概念
- [[Claude-Code-CLI]]
- [[Context-Engineering]]
- [[Progressive-Disclosure]]
- [[Agent-Harness]]
