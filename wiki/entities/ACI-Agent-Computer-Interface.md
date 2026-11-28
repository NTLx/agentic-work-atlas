---
type: entity
title: ACI (Agent-Computer Interface)
aliases:
  - ACI Agent Computer Interface
definition: "Agent 与计算机交互的接口设计，类比 HCI 但针对 AI Agent 优化"
created: 2026-04-10
updated: 2026-11-28
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

**ACI (Agent-Computer Interface)** 在Yang et al. [SWE-agent（2024-05-06预印本，NeurIPS 2024）](https://arxiv.org/abs/2405.15793)中被明确提出和实验研究；Anthropic在2024-12-19《Building effective agents》中将其用作工具设计原则，不主张Anthropic首创：

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
| **Markdown 代码块** | 可直接表达长代码 | 依模型与接口验证 |
| **JSON 内嵌代码** | 适合结构化参数 | 转义可能增加负担 |
| **Diff 格式** | 局部变更、易审计 | 需精确定位，结构化编辑工具可降低负担 |
| **重写整个文件** | 小文件/新文件可能适合 | 长文件成本、并发覆盖和误改风险需评估 |

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
   - 例如：该SWE-bench案例采用绝对路径避免CWD变化；固定工作目录的相对路径或资源ID也可防错，均需资源端授权

## 案例研究：SWE-bench Agent

> [!tip] 实践经验
> Anthropic 团队在构建 SWE-bench Agent 时，**工具优化时间超过整体 prompt 优化**。
> 
> 发现问题：Agent 移出根目录后，相对路径工具出错。
> 解决方案：该工具要求绝对路径，作者报告模型不再犯此类路径错误；非所有任务成功或普适路径规范。

## Computer Use：从 GUI 模仿到多表示接口（2026-09）

OpenAI Computer Use 的一手访谈（[[20260930-latentspace-devday-2026]]）提供了 ACI 演化的生产案例：Agent 不再只看 screenshot 再逐个点击，而是可以同时使用 screenshot、accessibility representation、DOM、Playwright，并在合适时生成 JavaScript 一次执行多步动作。App Shots 也不是普通截图，而是把可访问性文本和结构化元数据一起交给模型。

**判断**：按任务选择所需的视觉、结构化表示及动作接口，而非默认全部开放，让模型按任务选择最经济、信息最完整的路径：

| 层 | 作用 |
|---|---|
| Pixels / screenshot | 视觉状态、布局、真实渲染 |
| Accessibility tree | 文本、控件语义、可操作结构 |
| DOM / structured state | 全页状态、链接目标、隐藏于截图之外的信息 |
| Programmatic action | 批量动作、减少逐步 GUI 操作 |
| Event signal | 在真实状态变化后触发下一步，减少固定等待 |

这使 ACI 的优化目标从“让工具描述更清楚”扩展到 **representation selection + action granularity + timing**。当模型本身越来越快，页面加载和外部服务响应会成为新的瓶颈，ACI 也必须考虑 event-driven 调度而不只是输入格式。

- **证据**：[[20260930-latentspace-devday-2026]]（00:05:20–00:15:17）。
- **边界**：这些机制来自 OpenAI Computer Use 的具体实现；不同环境可获得的DOM/accessibility/programmatic surface不同。结构化数据可能包含隐私或不可见指令；工具返回状态不等于真实副作用，需独立授权和核验。本轮未重审访谈全部转录。

## 与 HCI 的对比

| 维度 | HCI | ACI |
|------|-----|-----|
| 用户 | 人类 | AI Agent |
| 设计目标 | 直观、易学 | 明确、无歧义 |
| 反馈机制 | 视觉/触觉 | 文本/工具结果 |
| 错误处理 | 容错、引导 | 防错、清晰报错 |

## 关键数据点

- Anthropic 在构建 SWE-bench Agent 时，**工具优化时间超过整体 prompt 优化时间**
- 案例：CWD变化导致相对路径错误，绝对路径消除作者观察的该类误用
- Anthropic建议减少不必要的行号计算/转义；不是不同工具格式的普适性能排序。

## 前提与局限性

- ACI 设计原则假定 Agent 是 LLM 驱动，对非 LLM Agent 可能不适用
- "给 Agent 足够 Token 思考" 的前提是上下文窗口足够大，成本可接受
- 工具格式选择需权衡：自然格式（如 Markdown）对 Agent 友好但可能增加 token 消耗
- SWE-bench 的优化经验不一定直接迁移到非代码场景

## 关联概念

- [[Coding-Agents]] - ACI 的主要使用者
- [[Agent-Workflow-Patterns]] - 使用 ACI 的模式
- [[Agentic-Engineering]] - ACI 设计的上下文
- [[ALIGN-Framework]] - 自动化接口设计的一种研究方法
- [[Agent-Environment-Misalignment]] - ACI 设计不足导致的具体失败模式

---

## 与 ALIGN 的对比

| 维度 | ACI设计（通用） | ALIGN（特定自动生成方法） |
|------|------------|---------------|
| 设计方式 | 人工或自动 | LLM生成、真实环境验证 |
| 适用环境 | 可为多环境设计 | 各环境分别生成 |
| 优化机制 | 可迭代 | 从失败轨迹生成并验证 |
| 成本 | 按设计和维护核算 | 离线生成、验证及维护成本 |
| 维护 | 版本管理、回归 | 测试冻结，变更后重验 |
| 跨 agent 迁移 | 取决于任务与契约 | 同环境内已测跨Agent与模型；存在动作语法失配 |

ALIGN是ACI原则的自动化实例，不能免除人工设计、代码/权限审查或发布责任。[v3](https://arxiv.org/html/2505.21055v3) Appendix D/E补充过度引导、额外动作、生成器能力与成本；详见[[ALIGN-Framework]]。**综合判断**：先修正最小接口缺陷，只有可验证增量才增加自动优化层。

---

> **来源**：Anthropic, "Building Effective AI Agents", 2024-12-19
> **对比来源**：Liu et al., "Agent-Environment Alignment via Automated Interface Generation", arXiv:2505.21055, 2025-05
