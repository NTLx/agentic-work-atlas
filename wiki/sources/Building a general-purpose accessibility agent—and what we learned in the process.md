---
type: source-summary
title: "Building a general-purpose accessibility agent—and what we learned in the process"
source_raw:
  - "[[Building a general-purpose accessibility agent—and what we learned in the process]]"
created: 2026-05-24
updated: 2026-05-25
tags:
  - source-summary
  - accessibility
  - AI-Agent
  - agent-harness
---

# Building a general-purpose accessibility agent—and what we learned in the process

## 编译摘要

### 1. 浓缩
- **核心结论1**: GitHub 的 accessibility agent 不是"自动解决 accessibility"的银弹，而是增强现有无障碍团队和工程流程的专业 agent。
  - 关键证据: 它有两个明确目标：在 Copilot CLI 与 VS Code 中给工程师提供 just-in-time accessibility answer；在前端代码变更进入生产前，自动发现并修复简单、客观、可判断的问题。
  - 试点数据是已 review 3,535 个 PR，resolution rate 为 `68%`。高频问题集中在语义结构、交互控件名称、状态消息、非文本替代文本和焦点顺序。
- **核心结论2**: 专业 agent 的效果来自组织已有的结构化知识资产，而不是一句"遵守最佳实践"。
  - 关键证据: GitHub 早已集中记录 accessibility issue，包含问题模板、复现步骤、severity、服务区域、WCAG criterion、修复 PR、acceptance criteria。这些人工审计和修复记录成为 agent 可引用的高质量语料。
  - 作者明确说，LLM 训练语料中充满几十年的 inaccessible code，模糊要求它"使用 accessibility best practices"效果不好。组织内部经过验证的历史问题和修复 PR 才是最强资产。
- **核心结论3**: 该 agent 的 harness 设计重点是降 token、保 trace、分职责、顺序执行。
  - 关键证据: 单体 agent 很快遇到限制，GitHub 改为父 agent 编排两个 sandboxed sub-agents：只读 reviewer/researcher 和可写 implementer。二者不能直接通信，而是用 structured, templatized output 传给父 agent 统一验证和路由。
  - 文章特别反对盲目创建大量并行 sub-agents。对 accessibility 这种上下文强、细节密集的工作，固定顺序、template schema、phase/step 约束和 re-review 更重要。
- **核心结论4**: 生产级 accessibility agent 必须内置"不行动"能力和人工升级路径。
  - 关键证据: GitHub 用 shell script 给代码复杂度评分，超过阈值就不允许 agent 改代码，只给出 guidance 并建议找 accessibility team；还列出 drag and drop、toast、rich text editor、tree view、data grid 等高风险模式，禁止 agent 自动生成修复。
  - 作者指出，55 个 WCAG A/AA success criteria 中只有 35 个可由 deterministic automated checkers 检测，约 `36%` 仍需人工评估。agent 可以缩小缺口，但不能替代设计和原型阶段的人工判断。

### 2. 质疑
- **关于 resolution rate 的质疑**: `68%` 表示 agent review 后问题被解决的比例，但不直接等同于真实辅助技术体验改善，也不能说明复杂交互模式是否被有效覆盖。
- **关于可复制性的质疑**: 这套方案依赖 GitHub 已有的 accessibility team、issue corpus、WCAG interpretation、internal skills 和 review sentiment tooling。没有历史审计资产的组织，很难从零复刻同等效果。
- **关于边界的质疑**: Agent 能在 objective issue 上发挥作用，但 accessibility 的根因很多来自设计和产品决策。若设计阶段没有介入，代码阶段修复会变成昂贵返工。
- **关于 anti-gaming 的质疑**: 文中提到 LLM 会想绕开"不要改代码"的限制，这说明高风险 agent 必须对模型的 bias to action 做专门防护，而不是只靠善意 instruction。

### 3. 对标
- **与 [[Verifiable-Agent-Engineering]] 对标**: 这是高质量案例。Agent 的成功不靠一次 prompt，而靠可审计模板、结构化输出、复杂度门控、人工升级和周期性人工复核。
- **与 [[Agent-Harness]] 对标**: Parent orchestrator、reviewer sub-agent、implementer sub-agent、schema、escalation gate、re-audit loop 共同构成完整 harness。
- **与 [[Bias-to-Action-LLM]] 对标**: "模型想生成代码"在 accessibility 场景会制造真实风险，因此需要设计不生成代码的路径，而不是默认越主动越好。
- **与 [[Social-Model-of-Disability]] 对标**: 文章采用社会模型，把问题定义为环境造成 access barriers，而不是把无障碍看作少数用户的附加需求。

### 关联概念
- [[Accessibility-Agent]]
- [[Verifiable-Agent-Engineering]]
- [[Agent-Harness]]
- [[Bias-to-Action-LLM]]
- [[Accessibility-Complexity-Evaluation]]
- [[Accessibility-High-Risk-Patterns]]
- [[WCAG]]
- [[Social-Model-of-Disability]]
