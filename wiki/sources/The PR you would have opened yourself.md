---
type: source-summary
title: "The PR you would have opened yourself"
source_raw:
  - "[[The PR you would have opened yourself]]"
created: 2026-05-24
updated: 2026-05-24
tags:
  - source-summary
---

# The PR you would have opened yourself

## 编译摘要

### 1. 浓缩
- **核心结论1**: 开源瓶颈不是打字速度，而是理解代码库以不破坏隐式契约——Agent 能自动生成 PR 但缺乏设计哲学上下文
  - 关键证据: transformers PR volume 上升 10 倍但维护者不变；Agent 按"最佳实践"重构实际破坏了库与用户的隐式契约
- **核心结论2**: Skills（Agent 配方）+ 独立 Test Harness 是让 Agent 辅助高质量开源贡献的可行模式
  - 关键证据: transformers-to-mlx Skill 包含近 15000 字的技术和文化规则；Test Harness 消除 LLM 幻觉不确定性
- **核心结论3**: Agent 辅助 PR 应比中位数人工 PR 提供更多信号（生成示例、数值比较、逐层对比），而非更少
  - 关键证据: PR 始终披露 agent-assisted；Skill 不自动打开 PR 需贡献者确认

### 2. 质疑
- **关于"Skills 模式可推广"的质疑**: transformers-to-mlx 有天然限制范围（从 transformers 端口），其他类型贡献（新功能、架构变更）是否适用？
- **关于"贡献者应参与审查循环"的质疑**: 文章假设贡献者愿意且有能力参与审查讨论，但大量 Agent 提交者可能只是"drive-by contributor"
- **关于 Test Harness 的局限**: 定性判断（如"输出是否正常"）仍依赖人类经验，Test Harness 能做的有限

### 3. 对标
- **跨域关联1**: 此现象类似 AI 时代内容创作——任何人都能生成内容，但质量审核成为瓶颈（Slopocalypse 概念）
- **跨域关联2**: Skills 模式可迁移到其他需要领域知识的 Agent 工作流（如代码审查、文档生成）

### 关联概念
- [[Agent-Generated-PRs]]
- [[Agent-PR-Review]]
- [[Compound-Engineering]]
