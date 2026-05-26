---
type: source-summary
title: "20260410-hoard-things-you-know"
source_raw:
  - "[[20260410-hoard-things-you-know]]"
created: 2026-05-24
updated: 2026-05-25
tags:
  - source-summary
  - AI-Agent
  - agentic-engineering
  - coding-agents
  - knowledge-management
---

# 20260410-hoard-things-you-know

## 编译摘要

### 1. 浓缩
- **核心结论1**: “囤积你知道如何做的事情”不是资料收藏癖，而是为 Agent 准备可执行先例库。
  - 关键证据: Willison 强调，软件能力的一部分是知道什么可能、什么不可能，以及大致如何实现。最可靠的证明不是听说可以，而是有一段跑得通的代码。
- **核心结论2**: 对 coding agents 来说，可运行示例比抽象说明更有杠杆。
  - 关键证据: 作者长期维护博客、TIL、上千个 GitHub repo、单 HTML 工具集合和研究仓库；这些资产可以直接作为 Agent 的上下文输入。
- **核心结论3**: Agent 把“个人经验库”升级成“可重组能力库”。
  - 关键证据: OCR 工具案例中，作者把 Tesseract.js 的浏览器 OCR 示例和 PDF.js 的 PDF 渲染示例交给模型组合，生成新的 PDF OCR 工具。
- **核心结论4**: 只要一次把技巧以工作代码保存下来，未来同形问题就可以由 Agent 检索、模仿、改造和组合。
  - 关键证据: 作者给 Agent 的典型指令不是“从头实现”，而是“读取这些旧项目/网页源码/研究仓库，参考其中的模式来做当前任务”。

### 2. 质疑
- **关于囤积质量的质疑**: 示例库只有在可查、可运行、可解释时才是资产。没有索引、环境说明、依赖版本和验证命令的“代码堆”会变成 Agent 的噪声源。
- **关于运行证明的质疑**: 能跑只是第一层证明，不代表安全、性能、可维护或适合生产。示例应标注用途边界：demo、PoC、生产模式、反例或废弃方案。
- **关于组合风险的质疑**: Agent 擅长拼接先例，也容易拼出能工作但概念边界混乱的系统。重组后需要人类检查命名、抽象、数据流和长期维护成本。
- **关于公共代码输入的质疑**: 让 Agent 克隆公开仓库或抓网页源码会引入许可、供应链和过时代码风险。企业环境需要白名单、许可证检查和依赖审计。

### 3. 对标
- **对标 Memex**: 这篇文章是 [[Memex]] 在 Agentic Engineering 里的工程化版本：不是保存文本记忆，而是保存可被机器重放和组合的工作示例。
- **对标 LLM Wiki**: [[LLM-Wiki]] 把文章编译成 entity/topic/comparison；Willison 的示例库把技巧编译成可运行代码。两者都是把一次性经验变成未来可调用的中间层。
- **对标 Context Engineering**: 好的示例库是上下文工程的一部分。它把“怎么做”从 prompt 叙述转化为 Agent 可以直接读取、模仿和测试的上下文资产。
- **迁移场景**: 数据分析 notebook、内部工具脚手架、UI 原型、自动化脚本、测试夹具、文档模板都可以用同样方式积累为 Agent 可重组资产。
- **对组织的启发**: 企业内部如果想让 Agent 复用专家经验，最小起点不是写长手册，而是收集“一个任务如何被成功做完”的可运行样例、测试数据和验收命令。

### 关联概念
- [[Multi-Layer-Memory]]
- [[Context-Engineering]]
- [[Compound-Engineering]]
- [[Knowledge-Compilation]]
- [[Agentic-Engineering]]
- [[Coding-Agents]]
- [[Memex]]
