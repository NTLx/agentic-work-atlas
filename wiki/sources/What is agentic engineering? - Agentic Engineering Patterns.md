---
type: source-summary
title: "What is agentic engineering? - Agentic Engineering Patterns"
source_raw:
  - "[[What is agentic engineering? - Agentic Engineering Patterns]]"
created: 2026-05-24
updated: 2026-05-24
tags:
  - source-summary
---

# What is agentic engineering? - Agentic Engineering Patterns

## 编译摘要

### 1. 浓缩
- **核心结论1**: Agentic engineering 是"在 coding agents 协助下开发软件"的实践
  - 关键证据: Coding agents 是能写能执行代码的代理（如 Claude Code、OpenAI Codex、Gemini CLI）
- **核心结论2**: Agent 的核心定义——"循环调用工具达成目标"
  - 关键证据: Agent 调用 LLM，传递工具定义，执行 LLM 请求的工具，将结果反馈给 LLM
- **核心结论3**: 代码执行是让 agentic engineering 成为可能的关键能力
  - 关键证据: 没有直接运行代码的能力，LLM 输出的价值有限；有代码执行能力，代理可以迭代出真正可工作的软件
- **核心结论4**: Vibe coding 是特指"未审查的原型质量代码"——与生产就绪代码有本质区别
  - 关键证据: Andrej Karpathy 2025年2月提出这个词，描述"忘记代码存在"的提示方式

### 2. 质疑
- **关于"代理不学习过去错误"的质疑**: 如果 LLM 不从错误中学习，如何积累经验？是否完全依赖人类的指令更新？
- **关于"vibe coding"定义扩展的质疑**: 将任何 LLM 生成代码都叫 vibe coding 是否有害？是否模糊了质量标准？

### 3. 对标
- **跨域关联1**: 类似"软件工程"到"AI 辅助软件工程"——从完整控制到意图指导
- **跨域关联2**: 类似"自动驾驶分级"——L0 完全人到 L5 完全 AI，有渐进过渡

### 关联概念
- [[Agentic-Engineering]]
- [[Coding-Agents]]
- [[Vibe-Coding]]
