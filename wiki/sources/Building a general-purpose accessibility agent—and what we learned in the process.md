---
type: source-summary
title: "Building a general-purpose accessibility agent—and what we learned in the process"
source_raw:
  - "[[Building a general-purpose accessibility agent—and what we learned in the process]]"
created: 2026-05-24
updated: 2026-05-24
tags:
  - source-summary
---

# Building a general-purpose accessibility agent—and what we learned in the process

## 编译摘要

### 1. 浓缩
- **核心结论1**: GitHub 的无障碍 Agent 不是“自动解决无障碍”的银弹，而是一个增强现有无障碍流程的生产级辅助系统。
  - 关键证据: 官方明确把目标限定为即时回答无障碍问题，以及在上线前自动发现并修复简单、客观的问题；并反复强调它只是 augment peers’ efforts。
- **核心结论2**: 这类专业 Agent 的效果高度依赖组织自己积累的高质量历史语料、结构化模板和线性工作流。
  - 关键证据: GitHub 把集中维护的无障碍 issue、PR、acceptance criteria 和 WCAG 元数据作为核心知识语料；同时采用 reviewer/implementer 两个顺序子 Agent、固定 phase 顺序和 template schema 传递信息。
- **核心结论3**: 生产级 Agent 的关键不只是“能不能修”，而是“知道什么时候不该修、什么时候该升级到人工”。
  - 关键证据: 文中给出复杂度评分、高风险模式禁改、anti-gaming 指令、人工复核和 escalation logic；并指出 55 个 WCAG A/AA 标准里只有 35 个可自动检测，约 `36%` 仍需人工评估。

### 2. 质疑
- **关于“68% resolution rate”的质疑**: 解决率说明问题被关闭或修复，但不直接等同于真实辅助技术体验改善，也不说明长尾复杂问题是否被覆盖。
- **关于“子 Agent + 模板 + 顺序执行”的质疑**: 这套设计依赖 GitHub 已有的无障碍团队、历史问题库和内部 skill 体系，其他团队未必能低成本复制。
- **关于“自动化边界”的质疑**: 即使 LLM 缩小了自动检测覆盖不到的 `36%` 缺口，它仍然无法替代设计阶段、原型阶段的人工无障碍判断。

### 3. 对标
- **跨域关联1**: 这篇文章是 [[Verifiable-Agent-Engineering|可验证 Agent 工程]] 的高质量案例：Agent 被设计成可升级、可审计、可拒绝，而不是一味自动执行。
- **跨域关联2**: 它也把 [[Agent-Harness|Agent Harness]] 的几个组件压得很实：顺序子 Agent 编排、结构化 schema 传递、复杂度门控和人工升级回路都不是 prompt 小技巧，而是 harness 设计。
- **跨域关联3**: 文中的 anti-gaming 指令和“拼命想生成代码”的观察，为 [[Bias-to-Action-LLM|LLM 的行动偏差]] 提供了具体工程场景。

### 关联概念
- [[Accessibility-Agent]]
- [[Verifiable-Agent-Engineering]]
- [[Agent-Harness]]
- [[Bias-to-Action-LLM]]
