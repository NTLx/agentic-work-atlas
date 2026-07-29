---
type: entity
title: Agent Verification
aliases:
  - Agent 自主验证
  - Agentic Verification
definition: "Agent 能自主运行验证循环的能力——不是 lint/type check，而是 agent 能自己启动测试环境、执行操作、观察结果并判断是否通过"
created: 2026-06-12
updated: 2026-07-28
evidence_level: medium
claim_type: mixed
tags:
  - agentic-engineering
  - verification
  - claude-code
related_entities:
  - "[[Claude-Code-CLI]]"
  - "[[Agent-Loops]]"
  - "[[Auto-Mode]]"
  - "[[Validation-Pipeline]]"
  - "[[Captain-Mindset]]"
  - "[[Rubric-Based-Evaluation]]"
  - "[[Software-Development-Autonomy-Levels]]"
source_raw:
  - "[[20260713-microsoft-ships-ai-agents-enterprise-scale]]"
  - "[[20260608-reflecting-on-year-of-claude-code]]"
  - "[[20260620-l8-principal-agentic-workflow]]"
  - "[[20260702-anthropic-harnesses-long-running-agents]]"
  - "[[20260727-github-harness-is-all-you-need]]"
  - "[[20260726-berkeley-auto-software-dev]]"
  - "[[20260708-towards-autonomous-software-dev.pdf]]"
  - "[[20260727-hf-agent-intrusion-technical-timeline]]"
  - "[[20260728-openai-scientific-computing-field-report.pdf]]"
---

> [!definition] 定义
> Agent 验证不是传统意义上的自动化测试（lint、type check、unit test），而是 agent 能**自主运行验证循环**——自己启动测试环境、执行操作、观察结果、判断是否通过，并在失败时自行修复。

## 关键数据点

- Claude Code 的 verification 路径: agent 打开 CLI → 测试自己写的 feature → 观察结果 → 修复
- Desktop development skill: Claude 启动本地 desktop app → 用 computer use 点击测试 UX → 测试 edge cases → 修复并重新检查
- 验证循环示例: iOS simulator / Android simulator / desktop computer use
- 从 Opus 4 开始实现 self-testing，到今天已成常态

## 异构验证与保障对象转移（07-28 扩展）

两篇同窗口来源（GitHub 2026-07-27 / Berkeley RDI 2026-07-26）从实践和理论两侧扩展了验证命题：

**实践侧：Rubber Duck 跨模型评审**（GitHub Copilot 机制）：请求**不同模型家族**审查实现——用 GPT 5.6 Terra 写的代码请 Sonnet 审查。原理：不同训练数据 → 不同盲点，单模型自审是盲点自洽。可与 Autopilot 组合成循环，直到双方同意只剩边际收益。这是异构验证的轻量工业形态。

**理论侧：保障对象从产物转移到 agent**（Berkeley position paper）：

> **CORE RISK**：当同一个 agent 既写实现又写测试，通过测试只证明**一致性**，不证明**正确性**。

自治 agent 会同时生成实现、测试、文档和理由——创造跨越所有"互相验证的产物"的**关联失败**。因此验证软件产物不再足够，还必须审计产出它的 agent（规格、技能、记忆、决策溯源、执行轨迹）。独立验证者 agent 只有在具备**真正独立的目标**、可信的评估机制、有原则的分歧解决协议时才有效。

**两侧配对的关键张力**：跨模型家族评审只是**训练数据级独立**——完整论文给出两个具体失败机制：verifier 与 generator 可能 **talk past each other**（互不理解、无法收敛），或 **co-adapt**（共同适应，直到测试仅仅背书实现的 bug）。这正是"不同模型家族不同盲点"不够的原因：Berkeley 要求的是**目标级独立**。Rubber duck 降低了自洽盲区风险，但未满足完全独立验证的条件——自治程度越高（[[Software-Development-Autonomy-Levels|Level II/III]]），这一缺口越致命。

## 科学域验证：四个细化命题（07-29 编译新增）

OpenAI 科学计算 field report（[[20260728-openai-scientific-computing-field-report.pdf]] 八案一手案例）在最严格正确性要求下（微妙数值错误即改变科学结论）压力测试了验证命题：

1. **plausible ≠ correct**：编译通过 + "看起来合理"的输出只是极弱证据。实际观察到的微妙错误：被改的数值默认值、不当的内存分配/流式行为、静默跳过的 case——"输出貌似合理但微妙错误"
2. **验证 harness 自身是错误来源**：HelixForge 中，下采样导致的假阳性 strand-balance 审计让 agent 去修改本来正确的 GPU 实现——人类审查需同时在两层：重写本身 + 验证 harness（后者常由 agent 辅助设计）
3. **真实数据不可替代**：RustQC 边缘 case 只在真实公开测序数据的真实规模显现（最小数据集不够）；hifiasm 在真实人类 reads 上的加速小于合成 benchmark——性能增益随数据集衰减
4. **技术正确性 vs 概念正确性**：agent 能提出并评估优化假设，但"下一步把优化压力投向哪里、尝试哪个高层策略"仍需人类反复决定——人类判断同时保证 technical correctness 与 conceptual correctness

佐证：agent "出错时照样表达自信"（七案贡献者均为成功的主要裁决者）；HI.SIM 是唯一近自主案例，恰因其验收目标是字节级一致（可验证性极强）——自主程度由可验证性决定，见 [[Grindability-vs-Verifiability]] 域边界节。

## 前提与局限性

- **依赖工具使用能力**: Agent 必须能访问运行环境（terminal、simulator、browser），无法访问时 verification 仍然是外部的
- **内部案例为主**: 当前最佳实践来自 Anthropic 内部，外部企业是否同样适用存疑
- **需要 skill 支撑**: 复杂验证（如 desktop app 测试）需要专门的 skill 教 agent 如何操作

## 关联概念

- [[Claude-Code-CLI]] — Agent verification 的主要载体
- [[Agent-Loops]] — Verification 是 loop 的核心环节
- [[Auto-Mode]] — Auto mode 让 verification 循环可以无人值守运行
- [[Validation-Pipeline]] — 系统化验证管线：对抗审查 + e2e 测试 + 证据生成 + PR babysitting
- [[Captain-Mindset]] — 验证能力的组织意义：人类从审 diff 转向看证据
- [[Software-Development-Autonomy-Levels]] — 自治级别越高，保障对象越从产物转向 agent（CORE RISK：一致性 ≠ 正确性）
