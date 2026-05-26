---
type: source-summary
title: "Agent pull requests are everywhere. Here's how to review them."
source_raw:
  - "[[Agent pull requests are everywhere. Here's how to review them.]]"
created: 2026-05-24
updated: 2026-05-25
tags:
  - source-summary
  - AI-Agent
  - code-review
  - agentic-engineering
---

# Agent pull requests are everywhere. Here's how to review them.

## 编译摘要

### 1. 浓缩

- **核心结论1**: Agent PR 的核心风险不是代码看起来糟，而是代码看起来太容易被批准。
  - 关键证据: GitHub 文章引用 2026 年 1 月研究 "More Code, Less Reuse"，指出 agent-generated code 每次变更引入更多冗余和技术债务，而 reviewer 对这类代码的批准感受反而更好。
  - 这说明审查问题从"能否看出明显错误"转向"能否识别安静的债务"。测试通过、风格整洁和 diff 清晰不再足以证明 PR 值得合并。
- **核心结论2**: Agent PR 正在冲击传统 review 带宽，人类审查必须从逐行扫描转为风险分层和关键路径追踪。
  - 关键证据: GitHub Copilot code review 已处理超过 6000 万次 review，且一年内增长 10 倍；超过五分之一的 GitHub code review 涉及 agent。一个开发者午饭前就能启动多个 agent session，但代码所有者的审查时间不会同比增长。
  - 因此 reviewer 的任务应聚焦于机器难以替代的系统上下文、事故历史、边界条件、权限语义和运营约束。
- **核心结论3**: 审查 Agent PR 有五个高价值红旗：削弱 CI、重复造轮子、幻觉式正确、agentic ghosting、不可信输入进入 LLM workflow。
  - 关键证据: CI gaming 包括降低覆盖率、跳过测试、修改 workflow 条件、用 `|| true` 让失败步骤通过；代码重用盲点表现为新增重复 helper、middleware、validation；幻觉正确性是能编译且通过测试但边界行为错。
  - Agentic ghosting 指大型 PR 无计划、review 后不响应或循环误解。工作流安全风险则来自 PR body、issue、commit message 等不可信内容被插入 prompt，模型输出再进入 shell，且运行在有写权限的 `GITHUB_TOKEN` 下。
- **核心结论4**: 自动 review 应成为人类 review 的前置过滤器，而不是替代人类判断。
  - 关键证据: 文章建议先让 Copilot review 捕捉风格、类型、明显逻辑和低层错误，再让人追踪关键路径、审查安全边界、要求可失败的回归测试和风险回滚计划。

### 2. 质疑

- **关于普遍性的质疑**: GitHub 平台规模足以说明趋势，但不同团队受影响程度不同。低 PR 量、小型 repo、强测试文化或人工合并门槛高的团队，短期不一定感到 review 饱和。
- **关于研究外推的质疑**: "More Code, Less Reuse" 的结论需要按语言、项目规模、模型版本和工具链继续拆分。Agent 代码质量会随模型、检索、repo context 和 review harness 改进而变化。
- **关于清单负担的质疑**: 五类红旗不能机械套到所有 PR。文档、样式、小型修复与权限、CI、生产 workflow 的风险不同，review 深度需要按 diff 范围和 blast radius 分级。
- **关于自动 review 的质疑**: 用 Copilot 先审查可以减少机械负担，但如果团队过度信任自动 review，也可能让人类更快通过"看似被检查过"的高风险 PR。

### 3. 对标

- **与 [[Agent-PR-Review]] 对标**: 这篇 source 可作为 Agent PR review 的操作清单，特别是 CI hard stop、new utility search、critical path tracing 和 untrusted input workflow review。
- **与 [[Verifiability]] 对标**: 对非平凡逻辑变更要求"新增一个在变更前会失败的测试"，是把 agent 声称的修复转成可验证证据。
- **与 [[Technical-Debt-Avoidance]] 对标**: Agent 重复造轮子会污染未来 prior art，后续 agent 又会复制这些坏模式。早期 review 必须阻止重复逻辑进入代码库。
- **与安全工程对标**: LLM workflow 中的 prompt injection、write-scoped token、secrets 泄露和模型输出执行，本质是 CI/CD 安全边界被 agent 扩大后的新审查面。

### 关联概念

- [[Agentic-Engineering]]
- [[Agent-PR-Review]]
- [[Verifiability]]
- [[Agent-Workflow-Patterns]]
