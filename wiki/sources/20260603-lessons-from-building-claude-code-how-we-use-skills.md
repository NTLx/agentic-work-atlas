---
type: source-summary
title: "Lessons from building Claude Code: How we use skills"
source_raw:
  - "[[20260603-lessons-from-building-claude-code-how-we-use-skills]]"
created: 2026-06-13
updated: 2026-06-13
tags:
  - source-summary
  - claude-code
  - skills
  - progressive-disclosure
---

# Lessons from building Claude Code: How we use skills

## 编译摘要

### 1. 浓缩
- **核心结论1**: Skills 是 Claude Code 中最常用的扩展点，分为 9 种类型
  - 关键证据: 库/API 参考、产品验证、数据获取与分析、业务流程自动化、代码脚手架、代码质量与审查、CI/CD 与部署、运行手册、基础设施运营
- **核心结论2**: 创建高质量 Skills 的最佳实践包括 4 个关键原则
  - 关键证据: 不陈述显而易见的内容，专注于"品味"和非默认模式；基于常见故障点构建"常见问题"部分；使用文件系统进行渐进式披露；为模型（触发器）而非仅为人类编写描述
- **核心结论3**: Skills 的设计哲学强调"品味"和非默认模式
  - 关键证据: 专注于"品味"和非默认模式，而非显而易见的内容

### 2. 质疑
- **关于"9种类型"的质疑**: 这些类型是否覆盖了所有可能的 Skills 场景？是否有新的类型正在出现？
- **关于"最佳实践"的质疑**: 这些实践是否适用于所有规模的团队？对于小型团队或个人开发者，是否需要调整？
- **关于"为模型编写描述"的质疑**: 这是否意味着 Skills 的设计需要更多考虑 AI 模型的理解能力，而非人类可读性？

### 3. 对标
- **跨域关联1**: 此现象类似软件工程中的"设计模式"，Skills 是 AI 时代的"Agent 设计模式"
- **跨域关联2**: 渐进式披露原则类似 UI/UX 设计中的信息架构，可迁移到 AI 工具设计领域

### 关联概念
- [[Progressive-Disclosure]]
- [[Claude-Code-CLI]]
- [[Agent-Harness]]