---
type: entity
title: ACI (Agent-Computer Interface)
aliases:
  - ACI Agent Computer Interface
definition: "Agent 与计算机交互的接口设计，类比 HCI 但针对 AI Agent 优化"
created: 2026-04-10
updated: 2026-10-01
evidence_level: medium
claim_type: mixed
tags:
  - AI-Agent
  - best-practices
related_entities:
  - '[[Coding-Agents]]'
  - '[[Agentic-Engineering]]'
  - '[[ALIGN-Framework]]'
  - '[[Agent-Environment-Misalignment]]'
source_raw:
  - '[[building-effective-agents-complete]]'
  - '[[20260801-align-agent-environment-interface.pdf]]'
  - '[[20260930-latentspace-devday-2026]]'
---

# ACI (Agent-Computer Interface)

> **核心类比**：ACI = Agent-Computer Interface，正如 HCI = Human-Computer Interface

## 定义

**ACI (Agent-Computer Interface)** 是 Anthropic 在"Building Effective AI Agents"中提出的概念：

> 思考人机交互 (HCI) 投入了多少努力，就应该在 Agent-计算机接口 (ACI) 上投入同等努力。

## 设计原则

### 1. 给 Agent 足够 Token 思考

> 不要让 Agent 在写代码时把自己逼入死角。

### 2. 保持格式自然

> 格式应接近模型在网上自然见过的文本。

### 3. 避免格式开销

> 不要让 Agent 计算数千行代码的行数，或转义引号。

## 工具格式选择建议

| 格式 | 适用性 | Agent 难度 |
|------|--------|-----------|
| **Markdown 代码块** | 高 | 低（自然格式） |
| **JSON 内嵌代码** | 低 | 高（需转义） |
| **Diff 格式** | 低 | 高（需计算行号） |
| **重写整个文件** | 高 | 低（无格式开销） |

## ACI 设计检查清单

1. **模型视角测试**
   - 根据描述和参数，使用方式是否明显？
   - 需要深思熟虑吗？（如果需要，对 Agent 也难）

2. **命名清晰性**
   - 参数名/描述是否让事情更明显？
   - 想象为初级开发者写文档字符串

3. **测试迭代**
   - 在 workbench 运行多组示例输入
   - 观察模型犯什么错误并迭代

4. **Poka-yoke（防错设计）**
   - 改变参数让错误更难发生
   - 例如：始终使用绝对路径而非相对路径

## 案例研究：SWE-bench Agent

> [!tip] 实践经验
> Anthropic 团队在构建 SWE-bench Agent 时，**工具优化时间超过整体 prompt 优化**。
> 
> 发现问题：Agent 移出根目录后，相对路径工具出错。
> 解决方案：工具改为始终要求绝对路径 → Agent 完美使用。

## Computer Use：从 GUI 模仿到多表示接口（2026-09）

OpenAI Computer Use 的一手访谈（[[20260930-latentspace-devday-2026]]）提供了 ACI 演化的生产案例：Agent 不再只看 screenshot 再逐个点击，而是可以同时使用 screenshot、accessibility representation、DOM、Playwright，并在合适时生成 JavaScript 一次执行多步动作。App Shots 也不是普通截图，而是把可访问性文本和结构化元数据一起交给模型。

**判断**：成熟 ACI 不应强迫 Agent 模仿人类唯一的视觉—点击通道，而应提供多层表示与动作接口，让模型按任务选择最经济、信息最完整的路径：

| 层 | 作用 |
|---|---|
| Pixels / screenshot | 视觉状态、布局、真实渲染 |
| Accessibility tree | 文本、控件语义、可操作结构 |
| DOM / structured state | 全页状态、链接目标、隐藏于截图之外的信息 |
| Programmatic action | 批量动作、减少逐步 GUI 操作 |
| Event signal | 在真实状态变化后触发下一步，减少固定等待 |

这使 ACI 的优化目标从“让工具描述更清楚”扩展到 **representation selection + action granularity + timing**。当模型本身越来越快，页面加载和外部服务响应会成为新的瓶颈，ACI 也必须考虑 event-driven 调度而不只是输入格式。

- **证据**：[[20260930-latentspace-devday-2026]]（00:05:20–00:15:17）。
- **边界**：这些机制来自 OpenAI Computer Use 的具体实现；不同桌面、移动端和受限企业环境可获得的 DOM/accessibility/programmatic surface 并不相同。

## 与 HCI 的对比

| 维度 | HCI | ACI |
|------|-----|-----|
| 用户 | 人类 | AI Agent |
| 设计目标 | 直观、易学 | 明确、无歧义 |
| 反馈机制 | 视觉/触觉 | 文本/工具结果 |
| 错误处理 | 容错、引导 | 防错、清晰报错 |

## 关键数据点

- Anthropic 在构建 SWE-bench Agent 时，**工具优化时间超过整体 prompt 优化时间**
- 问题案例：Agent 移出根目录后，相对路径工具出错；改为绝对路径后 Agent 完美使用
- Markdown 代码块格式适用性高、Agent 难度低（自然格式）；JSON 内嵌代码和 Diff 格式适用性低、难度高

## 前提与局限性

- ACI 设计原则假定 Agent 是 LLM 驱动，对非 LLM Agent 可能不适用
- "给 Agent 足够 Token 思考" 的前提是上下文窗口足够大，成本可接受
- 工具格式选择需权衡：自然格式（如 Markdown）对 Agent 友好但可能增加 token 消耗
- SWE-bench 的优化经验不一定直接迁移到非代码场景

## 关联概念

- [[Coding-Agents]] - ACI 的主要使用者
- [[Agent-Workflow-Patterns]] - 使用 ACI 的模式
- [[Agentic-Engineering]] - ACI 设计的上下文
- [[ALIGN-Framework]] - ACI 的工业化、自动化版本：用 LLM 自主合成接口而非手工 handcraft
- [[Agent-Environment-Misalignment]] - ACI 设计不足导致的具体失败模式

---

## 与 ALIGN 的对比

| 维度 | ACI（手工） | ALIGN（自动） |
|------|------------|---------------|
| 设计方式 | 人类 handcraft | LLM 自主生成 |
| 适用环境 | 单一环境 | 跨环境通用 |
| 优化机制 | 一次性 | 迭代（从失败轨迹学习） |
| 成本 | 高（需人工调优） | 中（多轮 LLM 调用） |
| 维护 | 改环境需重新设计 | 自动更新 |
| 跨 agent 迁移 | 不一定 | Plug-and-play（5 种 agent 一致受益） |

ALIGN（清华 NLP, 2025）可视为**"ACI 原则的算法化实现"**——不再需要人工精心设计接口，而是让 LLM 从失败轨迹中自动合成对齐接口。Anthropic "Building Effective Agents" 的三大原则之一 "Well-crafted ACI" 在 ALIGN 这里获得了一个可规模化落地的版本。

---

> **来源**：Anthropic, "Building Effective AI Agents", 2024-12-19
> **对比来源**：Liu et al., "Agent-Environment Alignment via Automated Interface Generation", arXiv:2505.21055, 2025-05
