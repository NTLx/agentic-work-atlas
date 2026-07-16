---
type: entity
title: Vibe Coding
aliases:
  - Vibe Coding
definition: "Andrej Karpathy 提出的编程概念，提升所有人的编程能力底线，让任何人通过自然语言和 agent 交互生成软件，原型质量是其特征"
created: 2026-04-10
updated: 2026-07-16
evidence_level: high
claim_type: mixed
tags:
  - AI-Agent
  - coding-agents
  - programming
related_entities:
  - '[[Agentic-Engineering]]'
  - '[[Harness-Engineering]]'
  - '[[Code-Execution]]'
  - '[[Andrej-Karpathy]]'
  - '[[Software-2.0]]'
  - '[[AI-Capability-Gap]]'
  - '[[AI-Psychosis]]'
  - '[[Software-3.0]]'
  - '[[Jagged-Intelligence]]'
  - "[[Essential-Complexity]]"
  - "[[Friction-as-Design-Signal]]"
  - "[[Ownership]]"
  - "[[Founder-Mode]]"
  - "[[Guillermo-Rauch]]"
source_raw:
  - '[[Andrej Karpathy: From Vibe Coding to Agentic Engineering]]'
  - '[[What is agentic engineering? - Agentic Engineering Patterns]]'
  - '[[20260413-llm-wiki]]'
  - '[[20260413-why-ai-first-strategy-wrong]]'
  - '[[20260409-ai-capability-gap-ai-psychosis]]'
  - "[[20260127-claude-coding-notes]]"
  - "[[用Agent评测思路管理AI Coding —— 31万行代码AI重构的实践]]"
  - "[[Why I Don’t Vibe Code]]"
  - "[[20260530-ceo-knee-deep-building-ai]]"
  - "[[vibe-coding成瘾之后重建AI与生活的边界]]"
---

# Vibe Coding（氛围编程）

> **核心特征**：忘记代码存在，专注于氛围和直觉

## 定义

**Vibe Coding** 是 Andrej Karpathy 于 2025 年 2 月提出的术语，描述一种 LLM 编程方式：

> "I just see things, say things, run things, and copy paste things, and it mostly works."

### 核心特征

1. **忘记代码存在** - 不关心代码细节
2. **原型质量** - 快速产出，不追求生产级
3. **未经审查** - 直接使用 AI 输出
4. **氛围驱动** - 凭直觉迭代

## 与 Agentic Engineering 的区别

Simon Willison 强调保持术语的原意：

| 维度 | Vibe Coding | Agentic Engineering |
|------|-------------|---------------------|
| **代码质量** | 原型级 | 生产级 |
| **审查程度** | 无 | 深度审查 |
| **验证方式** | 凭感觉 | 自动测试 |
| **目标** | 快速原型 | 可工作软件 |
| **心态** | "忘记代码" | 验证和迭代 |

## 适用场景

### 适合 Vibe Coding

- 快速原型验证
- 个人实验项目
- 学习和探索
- 一次性脚本

### 需要 Agentic Engineering

- 生产环境代码
- 团队协作项目
- 长期维护系统
- 安全敏感应用

## 不要滥用术语

> [!warning] 重要区分
> 不要把 Vibe Coding 扩展定义为"任何 LLM 生成代码的情况"。
> 
> 保持原意：**未经审查、原型质量的 LLM 生成代码**，与已提升到生产标准的代码区分开来。

## 与 Software 3.0 的关系

Vibe Coding 更准确地说是 [[Software-3.0]] 的普及化实践：人不再直接写大量实现代码，而是通过提示词、运行反馈和复制粘贴驱动 LLM 生成软件。它继承了 Software 2.0 "程序由神经网络产生" 的方向，但操作界面从数据集和训练目标变成了上下文窗口与自然语言。

---

## Vibe Coding 的工程治理代价

美团实践揭示了 Vibe Coding 在团队场景下的系统性风险：当 90%+ 代码由 AI 生成，不同背景成员各自用 AI Coding，系统会**加速腐化**而非收敛复杂度。

核心矛盾：Vibe Coding 提升了个体编码效率，但如果没有统一规范约束，AI 会把代码风格差异进一步放大——"千人千面"的代码在 31 万行体量下变成灾难。

解法：通过 [[人机对齐]] 方法论，先拉齐团队工程标准，再将标准落地为 AI Rule/Skill，从"氛围驱动"转向"约束驱动"。

## 反向案例：为什么不 Vibe Code

Jacob Harris 的 [[Why I Don’t Vibe Code]] 给 Vibe Coding 提供了一个有价值的反例。它不是从“AI 是否有用”切入，而是从软件工作的不可外包部分切入：

- [[Essential-Complexity]] 仍然存在：AI 可以降低写代码的偶然复杂性，但不能替代抽象设计、边界选择和长期维护判断。
- [[Friction-as-Design-Signal]] 不能被一概消除：阅读陌生代码、写 ADR、暂停实现，都是让真实约束浮现的过程。
- [[Ownership]] 不能转交给模型：模型可以生成代码，但不能为公共服务故障、数据误读或系统伤害承担后果。
- 软件是协作实践：把产品、设计、测试、合规和 review 都视为“摩擦”，会让系统更快但未必更好。
Vibe Coding 与 Software 2.0 / 3.0 的关系：

| Software 2.0 | Software 3.0 / Vibe Coding |
|--------------|----------------------------|
| 数据集和目标函数是主要接口 | 提示词和上下文窗口是主要接口 |
| 神经网络权重是程序 | LLM 在上下文中解释并生成程序 |
| 训练过程像编译 | 对话、运行和复制粘贴像交互式编程 |


### Karpathy 的新观察 (2026-01)

在 Claude Coding Notes 中，Karpathy 补充了 Vibe Coding 的常见陷阱：

> "They really like to overcomplicate code and APIs, they bloat abstractions, they don't clean up dead code after themselves... They will implement an inefficient, bloated, brittle construction over 1000 lines of code and it's up to you to
> be like 'umm couldn't you just do this instead?'"

**模型倾向**：
1. 过度复杂化代码和 API
2. 膨胀抽象层
3. 不清理死代码
4. 实现冗余、脆弱的 1000 行方案，经提示后可压缩为 100 行

## 关键数据点

- Andrej Karpathy 于 2025 年 2 月提出该术语
- Karpathy 的原始描述："I just see things, say things, run things, and copy paste things, and it mostly works."
- Claude Code 于 2025 年 3 月发布（Karpathy 提出术语后仅 3 周）
- 与 Software 3.0 的关系：提示词和上下文窗口成为编程接口

## 前提与局限性

- 依赖前提：人类愿意接受"忘记代码存在"的开发方式
- 适用边界：快速原型、个人实验、学习探索、一次性脚本
- 局限性：不适用于生产环境、团队协作、长期维护系统、安全敏感应用
- 质量标准：未经审查、原型质量，与生产就绪代码有本质区别
- 术语滥用风险：不应将"任何 LLM 生成代码"都定义为 Vibe Coding
- 反向边界：当任务需要本质复杂性判断、团队协作和责任承担时，Vibe Coding 的收益会被隐藏成本抵消

## Spec-Driven Development 边界（07-10 深度思考）

Vibe Coding 和 Spec-Driven Development 不是线性演化关系——它们永久共存，各自处理不同复杂度层的任务：

**路径选择矩阵**：本质复杂度 × 系统生命周期 → 三条路径共存：
- **A**: vibe → spec → production（高本质复杂度 + 长生命周期系统）
- **B**: vibe → 被 AI 消解 → 不需要 spec（低本质复杂度 + 可端到端 AI 处理，如 menu-gen）
- **C**: 永远 vibe（探索性/创意性/不可验证任务）

**Spec 三层定理**：规则层（可形式化，硬验证）→ 模式层（可传达，软验证）→ 品质层（不可传达，委托）。Vibe Coding 处理品质层和模式层的探索部分。

**框架创造边界**：Vibe Coding 的核心不可替代价值 = 框架创造——看到当前解空间之外的选项（如 Karpathy 的 menu-gen 顿悟："that app shouldn't exist"）。框架创造不可在当前框架内编码（哥德尔不完备的工程版本），需要外部他者的碰撞。来源：07-10 深度思考（roundtable+think+qa）

## 关联概念

- [[Software-3.0]] - Vibe Coding 是 Software 3.0 的普及化、原型化实践
- [[Software-2.0]] - Vibe Coding 继承了神经网络生成程序的方向，但不是 Software 2.0 的直接实践
- [[Agentic-Engineering]] - 与 Vibe Coding 对比的工程范式
- [[Harness-Engineering]] - 超越 Agentic Engineering：不仅审查代码，而是构建让 Agent 有效工作的完整系统
- [[Code-Execution]] - Vibe Coding 不强调验证，Agentic Engineering 和 Harness Engineering 强调
- [[Andrej-Karpathy]] - 概念提出者

## CEO Vibe Coding 争议（2026）

2026 年 5 月，Paul Graham 和 Guillermo Rauch 主张 CEO 必须亲手使用 AI 构建软件（[[Founder-Mode]] 的 AI 时代延伸），但 Paul Ford 在 "Dear Vibe-Coding CEO: Please Stop" 中警告 CEO vibe coding 的组织风险：

- **高管的周末 demo 是终极 executive memo**："The boss built a thing and he wants you to take a look" 在全球走廊里回响，工程师、设计师、产品经理被迫跟进 CEO 用 Claude 周末 hack 出来的东西
- **AI 赋能对 CEO 是梦想，对员工是噩梦**：现代 CEO 想展示自己仍有技能，但 vibe-coded demo 的质量不达生产标准
- **品质仍然来自深度思考**："AI can produce outputs all day long, but it can't guarantee quality. Quality software is borne out of creative problem-solving and lots of little, tiny moves, not one-shot magic prompts."

**核心张力**：CEO 亲手 vibe coding 可以提高对 AI 能力边界的理解（Graham 的 "knee-deep" 主张），但产出质量可能不达生产标准（Ford 的 "cut it out" 警告）。解法是组织层面的质量门控——CEO 的 demo 不自动进入产品 backlog，而是作为探索性实验。

## Vibe Coding 成瘾机制（2026-07-16 编译新增）

一手体验报告 `[[vibe-coding成瘾之后重建AI与生活的边界]]` 揭示了 Vibe Coding 作为**成瘾性技术**的面向，补充了上述工程治理视角缺失的认知-主体性维度：

- **奖励回路与短视频同构**：vibe coding 是"高频、低门槛、强刺激"的奖励系统，区别在于奖励形式是"主动生成结果"而非"被动消费内容"。输入 prompt → AI thinking → 生成代码 → demo，全程无阻力且每步即反馈，通过多巴胺强化"行为-回报"路径。
- **比刷短视频更难觉察**：披着"创造/学习/效率"外衣，关联创造欲、成就感、价值感与自我扩张想象——主体性让渡发生在"自觉在做正经事"的伪装下。这正是 07-15 深度思考判断的"创造型成瘾 > 消费型成瘾"的一手实证。
- **慢反馈耐受力下降**：大脑适应高强度短周期刺激后，对需长期投入、低刺激之事的耐受力下降——与 Lembke《多巴胺国度》的高多巴胺基线上调框架吻合。
- **感知钝化与记忆模糊**：密集决策导致"决策疲劳"→ 判断力下降 + 感知钝化 + offline time 被挤占 → 短期记忆难巩固。觉察迟滞（书桌上的发财树长新叶而不自知）。

**对抗（个人层，与 [[SHIELD]] 互证）**：定时记录（日记/手帐）作为"硬信号"让生活重新可见，把觉察窗口从"月"压缩到"天"；时间切割 + 工作流沉淀为 skill 的"复利工程" + 允许停下来。作者红线："绝对不会在社交平台上发表 AI 生成的观点"——主体性边界的人格化。

> 此面向与 [[AI-Psychosis]]、[[Friction-as-Design-Signal]]、07-15 增强陷阱热力学修正形成闭合：vibe coding 的"即时闭环 + 创造欲绑定"使其成瘾性结构性高于消费型 AI 使用。详见 [[vibe-coding成瘾之后重建AI与生活的边界]] source summary。
