---
type: entity
title: Tool-Use Architecture
aliases:
  - Tool-Use Architecture
  - 工具使用架构
definition: "AGI 系统架构理念：通用模型作为编排者调用专用系统（AlphaFold、模拟器等），而非将所有能力塞入一个巨型模型"
created: 2026-05-08
updated: 2026-05-26
tags:
  - AI
  - AGI
  - system-architecture
related_entities:
  - "[[Demis-Hassabis]]"
  - "[[Scientific-Discovery-AI]]"
  - "[[Agent-Orchestration]]"
  - "[[Model-Context-Protocol-MCP|MCP]]"
  - "[[Specialized-Small-Models]]"
  - "[[Thin-Harness-Fat-Skills]]"
  - "[[Continual-Learning]]"
source_raw:
  - "[[Demis Hassabis: Agents, AGI & The Next Big Scientific Breakthrough]]"
  - "[[Building an MCP Ecosystem at Pinterest]]"
---

# Tool-Use Architecture（工具使用架构）

> [!definition] 定义
> **Tool-Use Architecture（工具使用架构）** 是一种 AGI 系统架构理念：不把所有的知识和能力塞进一个巨大的通用模型（"如果在 Gemini 里放入所有蛋白质数据，它的语言能力会退化"），而是让通用模型成为编排者和工具使用者，将 AlphaFold、材料模拟器等专用系统当作可调用的工具。

## 关键数据点

- **信息效率原则**：Hassabis 明确指出一个巨型全能脑会导致"regression"——信息密度并非无限，专业能力和通用能力在单个模型中存在 tradeoff
- **工具使用 vs 大统一模型**：好的通用模型"可能甚至可以训练这些专用工具"，但工具本身保持独立
- **物理世界的延伸**：不仅是软件工具——"什么样的工厂要建"、"什么类型的金融系统"——物理基础设施也适用这一逻辑
- **与 MCP 的关系**：Hassabis 的 Tool-Use Architecture 与 [[Model-Context-Protocol-MCP|Anthropic MCP]] 协议在理念上高度一致——都是"通用 orchestrator + 标准化 tool connections"模式

## 前提与局限性

- 工具使用假设通用模型有足够智能来判断"何时调用哪个工具"——这个判断能力本身可能成为瓶颈。
- 专用系统版本升级可能导致与 orchestrator 的兼容性问题。
- 如果通用模型未来发展出更强的专业化能力而不损失通用性（逆 described tradeoff），这一架构可能被简化。

## 通用性与专业化的信息密度张力

Tool-Use Architecture 的底层假设是信息密度存在上限：一个模型不能同时在所有领域保持最优能力。Hassabis 用"如果在 Gemini 里放入所有蛋白质数据，它的语言能力会退化"来说明这种张力——通用能力和专业能力在单个模型中存在 tradeoff。

这个假设在多个层面得到验证：

- **模型层面**：[[Specialized-Small-Models|专门化小模型]] 在窄任务上超越大模型，证明训练历史与任务分布的对齐比参数规模更重要。
- **架构层面**：[[Thin-Harness-Fat-Skills|薄 Harness 厚 Skill]] 哲学把确定性任务留给 Harness、语义任务留给 Skill，本质上是同一原则的软件工程实现。
- **组织层面**：[[Cross-Disciplinary-Generalist|跨领域通才]] 管理者 + 专家团队的组合，是人类组织中的同构模式。

## 与 MCP 和 Agent 编排的共振

Tool-Use Architecture 与 [[Model-Context-Protocol-MCP|Anthropic MCP]] 协议在架构理念上高度一致——都是"通用 orchestrator + 标准化 tool connections"模式。Pinterest 的 MCP 生态实践印证了这一点：通用模型通过标准化协议调用各种专用工具（数据库、搜索引擎、内部 API），而不是把所有功能塞进一个 Agent。

这个模式对 Agent 系统有三层含义：

1. **编排层保持薄**：[[Agent-Orchestration|Agent 编排]] 的核心任务是"判断何时调用哪个工具"，而不是"自己做所有事"。
2. **工具层保持独立**：每个工具（AlphaFold、数据库、API）可以独立迭代和替换，不依赖特定模型版本。
3. **接口标准化**：MCP 等标准化协议降低了工具与 orchestrator 的耦合，使系统可以在不重建的情况下替换组件。

## 关联概念

- [[Scientific-Discovery-AI]] — AlphaFold、材料模拟器等作为科学发现工具被 orchestrator 调用。
- [[Agent-Orchestration]] — Agent 层面同样存在"编排 vs 单一大 Agent"的问题。
- [[Cross-Disciplinary-Generalist]] — 人类组织层面存在相同模式：通才管理者 + 专家团队。
- [[Specialized-Small-Models]] — 工具使用架构在模型层面的实现：通用模型编排，专用模型执行。
- [[Thin-Harness-Fat-Skills]] — 同一原则的软件工程实现：Harness 做路由，Skill 做专业任务。
- [[Continual-Learning]] — 工具使用架构的替代路径：如果未来模型实现持续学习而不灾难性遗忘，"大统一模型"的可行性会上升。
