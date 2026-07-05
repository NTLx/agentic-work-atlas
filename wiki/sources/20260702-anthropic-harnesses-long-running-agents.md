---
type: source-summary
title: "Effective Harnesses for Long-Running Agents (Anthropic)"
source_raw:
  - "[[20260702-anthropic-harnesses-long-running-agents]]"
created: 2026-07-05
updated: 2026-07-05
tags:
  - source-summary
  - agent-harness
  - agent-engineering
  - AI-Agent
evidence_level: high
claim_type: extracted
---

# Effective Harnesses for Long-Running Agents (Anthropic)

## 编译摘要

### 1. 浓缩
- **核心结论1**: 长周期 Agent 的核心挑战是"跨 session 失忆"——每个新 session 从零开始，就像轮班工程师每次换班都失去前一班的记忆。仅靠 compaction 不够，需要专门的 harness 设计
  - 关键证据: Claude Agent SDK 实测——即使 Opus 4.5 在 loop 中跨多个 context window 运行，仅给 "build a clone of claude.ai" 这样的高层 prompt 也会失败。两种失败模式：One-shotting（一次做太多，半实现状态留给下个 session 猜测）和 Premature Declaration of Victory（看到部分进展就宣布完成）
- **核心结论2**: 解决方案是双 Agent 分工——Initializer Agent 负责环境搭建（init.sh、progress 文件、200+ feature 的 JSON 列表），Coding Agent 每次只做一个 feature，完成后必须 commit + 写 progress 更新
  - 关键证据: JSON 格式的 feature list（模型更不容易不恰当地修改 JSON 而非 Markdown）；强措辞指令 "It is unacceptable to remove or edit tests"；每次从 git log 和 progress 文件获取上下文后再选 feature
- **核心结论3**: Agent 需要显式提示才会做端到端测试——默认倾向于标记 feature 完成而不验证。使用 Puppeteer MCP 等浏览器自动化工具后改善明显，但仍有盲区（如浏览器原生 alert modal）
  - 关键证据: 缺少显式测试提示时 Agent 倾向于跳过验证；引入 Puppeteer MCP 后大部分 feature 可以端到端验证，但 alert modal 等特定 UI 元素仍无法被 Agent 感知

### 2. 质疑
- **关于"单 feature 增量"策略的质疑**: 200+ feature 逐个完成意味着需要 200+ 次 agent session。文中未讨论总时间成本和 token 成本。对于小项目，这种粒度可能过度；对于大项目，200+ feature 的线性执行可能不可行
- **关于 JSON vs Markdown 的质疑**: "模型更不容易修改 JSON"是基于经验观察，未提供定量证据。JSON 格式对 feature 描述的表达能力有限（如无法嵌套解释），可能不是最优格式
- **关于未来工作的质疑**: 文中承认 open question——单通用 coding agent vs 多 Agent 架构（测试/QA/代码清理专业化）。这意味着当前方案尚未收敛到最优

### 3. 对标
- **跨域关联1**: 双 Agent 分工（Initializer + Coding Agent）与 [[Plan-as-Agent-Checkpoint]] 的理念高度一致——通过外部 artifact（feature list、progress 文件、git log）为 Agent 提供"检查点"，解决跨 session 状态丢失问题
- **跨域关联2**: "One-shotting" 失败模式与 [[Agent-Tenacity]] 中的"过度雄心"对应——Agent 需要在"做足够多"和"做太多导致不可恢复"之间找到平衡。这里的"一次只做一个 feature"是解决该问题的具体 harness 约束
- **跨域关联3**: 这个方案本质上是一个薄 harness（[[Thin-Harness-Fat-Skills]]）——Initializer Agent 设置环境后，Coding Agent 依靠外部文件系统（git、progress 文件、feature list）而非内部状态维持长期进展

### 关联概念
- [[Agent-Harness]]
- [[Harness-Engineering]]
- [[Plan-as-Agent-Checkpoint]]
- [[Agent-Tenacity]]
- [[Thin-Harness-Fat-Skills]]
- [[Agent-Loops]]
- [[Agent-Verification]]