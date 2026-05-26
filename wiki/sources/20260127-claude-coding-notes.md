---
type: source-summary
title: "Claude Coding Notes (2026-01)"
source_raw:
  - "[[20260127-claude-coding-notes]]"
created: 2026-05-24
updated: 2026-05-25
tags:
  - source-summary
  - ai-coding
  - claude-code
  - software-engineering
---

# Claude Coding Notes (2026-01)

## 编译摘要

### 1. 浓缩

- **核心结论1**: AI 辅助编程在 2025 年 12 月发生"相变"，工作流从 80% 手动编码转变为 80% agent 编码（用英语编程），这是 Karpathy 20 年编程生涯最大的工作流变革
  - 关键证据: "This is easily the biggest change to my basic coding workflow in ~2 decades of programming and it happened over the course of a few weeks"

- **核心结论2**: 模型仍存在显著局限性——不再犯语法错误，而是犯"概念性错误"（类似粗心初级开发者），过度复杂化代码、不清理死代码、过于迎合用户、不寻求澄清
  - 关键证据: "They will implement an inefficient, bloated, brittle construction over 1000 lines of code and it's up to you to be like 'umm couldn't you just do this instead?'"

- **核心结论3**: Agent 的核心优势是"韧性"（Tenacity）——永不疲劳、永不气馁，能持续尝试直到成功；杠杆来自"声明式"而非"命令式"的指令方式
  - 关键证据: "It's a 'feel the AGI' moment to watch it struggle with something for a long time just to come out victorious 30 minutes later"
- **核心结论4**: 这次相变带来的不只是 speedup，而是 work expansion：开发者会去做原本不值得做、不会做或不敢碰的代码工作。
  - 关键证据: Karpathy 明确说速度提升很难衡量，主要效果是自己会做更多原本不会做的事；这说明 AI Coding 的组织影响不只是节省时间，也会扩大需求、实验和代码变更总量。

### 2. 质疑

- **关于"结论1"的质疑**: 工作流转变的前提是用户已配置好 Agent 环境（CLAUDE.md、工具集成），且能接受"用英语编程"的心理落差；对未适应的用户，这可能不是改进而是混乱
- **关于"结论2"的质疑**: 模型局限性是否可通过更好的 prompt/instruction 解决？Karpathy 提到"All of this happens despite a few simple attempts to fix it via instructions in CLAUDE.md"，说明简单指令无效，但系统化 instruction engineering 可能改善
- **关于数据可靠性的质疑**: 这是 Karpathy 个人体验，非量化研究；样本量为 1，推广到"double digit percent of engineers"需更多证据

### 3. 对标

- **跨域关联1**: Agent Tenacity 类似科学实验中的"反复试错"（Trial-and-error），区别是 Agent 不受情绪影响——跨域到心理学，揭示"韧性"可能是人类工作瓶颈而非智力
- **跨域关联2**: Slopocalypse 预警类似工业革命初期对"劣质产品泛滥"的担忧——历史模式：新技术降低门槛 → 初期质量下降 → 标准/规范建立 → 质量回升

### 关联概念

- [[Slopocalypse]]
- [[Agent-Tenacity]]
- [[Vibe-Coding]]
- [[Agentic-Engineering]]
- [[Claude-Code-CLI]]
- [[Agentic-Engineering-Patterns]]
