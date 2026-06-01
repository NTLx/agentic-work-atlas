---
type: topic
title: CEO 亲手用 AI
description: "CEO 必须亲手使用 AI 构建软件的主张、争议与组织影响"
created: 2026-06-01
updated: 2026-06-01
tags:
  - management
  - ceo-ai-hands-on
  - founder-mode
  - vibe-coding
related_entities:
  - "[[Paul-Graham]]"
  - "[[Guillermo-Rauch]]"
  - "[[Founder-Mode]]"
  - "[[Vibe-Coding]]"
  - "[[Coding-Agents]]"
  - "[[Forward-Deployed-Engineer]]"
  - "[[AI-Psychosis]]"
  - "[[Agentic-Engineering]]"
source_raw:
  - "[[20260530-ceo-knee-deep-building-ai]]"
---

# CEO 亲手用 AI（CEO Hands-On AI）

> [!definition] 主题描述
> **CEO 亲手用 AI** 是 2026 年 5 月由 Paul Graham 和 Guillermo Rauch 引发的一场讨论，主张 CEO 必须亲手使用 AI 构建软件，而非完全依赖二手报告。这一主张与 Paul Ford 对"Vibe-Coding CEO"的批评形成张力，揭示了 AI 时代高管参与度与组织质量之间的核心矛盾。

## 核心主张

### Paul Graham：CEO 不参与比过度参与更危险

2026 年 5 月 30 日，Graham 在 X 上发帖：

> "The only thing worse than having the CEO knee-deep in building stuff with AI is not having the CEO knee-deep in building stuff with AI."

这一表述将 [[Founder-Mode]]（2024）扩展到 AI 使用场景。Graham 强调 CEO 必须亲手使用 AI 来理解其能力边界，而非完全依赖下属的报告。

**AI 使用的"right way"vs"wrong way"**：Graham 在同期批评创始人用 AI 写冷启动邮件（"It feels like being lied to"），但当被质疑"认知失调"时回应："You're supposed to use it, but in the right way. Like any technology." 这暗示：
- **Right way**: CEO 亲手用 AI 构建东西，理解能力边界
- **Wrong way**: 用 AI 替代自己的声音去欺骗收件人（如 AI 写的邮件）

### Guillermo Rauch：Coding agents 引发企业级 PLG 革命

2026 年 5 月 31 日，Rauch（Vercel CEO）发帖呼应：

> "Unclear if a durable trend, but CEOs and CTOs are back to coding with a fury, thanks to coding agents. I have public company CEOs sliding into my DMs telling me about falling in love with shipping software again thanks to Claude Code and Vercel."

Rauch 进一步提出 **PLG-fication of the enterprise**：

> "Coding agents are the ultimate PLG-fication of the enterprise. Bad, legacy software can't hide anymore. The stack that works is self-evident to the entire organization, from intern to CEO."

**Vercel 数据佐证**（Forbes, 2026-03）：
- Claude 用户占 Vercel 用户的 ~1%，但贡献 ~15% 部署量（15 倍超代表）
- AI agent 部署占比从 5%（2025-06）增至 21%（2026-02）
- 其中 ~70% 来自 [[Coding-Agents|Claude Code]]

## 反对声音

### Paul Ford：Vibe-Coding CEO 请停手

2026 年 5 月 20 日（Graham 发帖前 10 天），Paul Ford（Aboard 创始人）在 "Dear Vibe-Coding CEO: Please Stop" 中警告 CEO vibe coding 的组织风险：

- **高管的周末 demo 是终极 executive memo**："The boss built a thing and he wants you to take a look" 在全球走廊里回响，工程师、设计师、产品经理被迫跟进 CEO 用 Claude 周末 hack 出来的东西
- **AI 赋能对 CEO 是梦想，对员工是噩梦**：现代 CEO 想展示自己仍有技能，但 [[Vibe-Coding]] 的质量不达生产标准
- **品质仍然来自深度思考**："AI can produce outputs all day long, but it can't guarantee quality. Quality software is borne out of creative problem-solving and lots of little, tiny moves, not one-shot magic prompts."

Ford 的建议："Cut it out. Seriously, cut it out. Your interactive C-suite demo memo is not going to get you any results."

## 三条路线的张力

| 立场 | 代表 | 核心态度 | 关键词 |
|------|------|---------|--------|
| **CEO 必须亲手用 AI** | Paul Graham, Guillermo Rauch | CEO 不参与 AI 构建比参与更糟 | knee-deep, right way, PLG-fication |
| **CEO 回归编码是 PLG 革命** | Guillermo Rauch | coding agents 让 C-suite 重新爱上发布，legacy software 无处遁形 | mini CEO, leverage, software is like water |
| **Vibe-Coding CEO 请停手** | Paul Ford | CEO 的周末 demo 是终极 executive memo，对员工是噩梦 | cut it out, quality takes deep thought |

**核心分歧**：
- Graham 和 Rauch 都认为 CEO 应该亲手用 AI，但 Graham 强调"in the right way"（暗示存在 wrong way），Rauch 更无条件地拥抱这一趋势
- Paul Ford 的批评不针对"CEO 用 AI"本身，而针对 CEO 用 AI 产出低质量 demo 然后要求团队跟进的组织行为
- Rauch 的"legacy software can't hide"暗示 CEO 亲手验证技术栈会加速淘汰旧系统——这既是机会也是威胁
- Ford 的"quality software takes deep thought"与 Rauch 的"software is like water"形成直接对立

## 组织层面的解法

### CEO 的 demo 不自动进入产品 backlog

CEO 亲手 vibe coding 可以提高对 AI 能力边界的理解（Graham 的"knee-deep"主张），但产出质量可能不达生产标准（Ford 的"cut it out"警告）。解法是组织层面的质量门控：
- CEO 的 demo 作为探索性实验，不自动进入产品 backlog
- 设立明确的"CEO demo → 工程师评估 → 产品决策"流程
- CEO 的参与目的是理解 AI 能力边界，而非替代工程师的生产工作

### FDE 作为 CEO 的 AI 能力补充

Carlos E. Perez 提出"每个 CEO 都需要一个 FDE 坐在办公室"，将 [[Forward-Deployed-Engineer]] 从"企业部署工程师"扩展为"CEO 的 AI 能力补充"——不是替代 CEO 亲自使用 AI，而是帮助非技术背景的高管理解和有效使用 AI 工具。

## AI Psychosis 风险

CEO 对 AI 能力的认知可能与实际存在偏差（[[AI-Psychosis]]）。BetterUp Labs 研究（1,150 人）显示：
- 40% 员工定期收到同事的低质量 AI 生成内容
- 53% 感到恼火
- 约一半人认为发送者更没创造力、更不可靠
- 42% 认为更不值得信赖

CEO 亲手使用 AI 可以减少这种认知偏差，但前提是 CEO 具备足够的 [[Taste]] 和 [[Judgment]] 来区分 AI 产出的质量。

## 历史类比

### 工业革命早期的"工厂主必须懂机器"

19 世纪工业革命时期，成功的工厂主（如 Josiah Wedgwood、Richard Arkwright）往往深入理解机器原理和生产流程，而非只做管理。不碰机器的工厂主被淘汰。

### 互联网早期的"CEO 必须懂互联网"

1990 年代末，成功拥抱互联网的 CEO（如 Jeff Bezos、eBay 的 Meg Whitman）亲自使用互联网产品、理解用户体验。回避互联网的 CEO（如 Blockbuster 的 John Antioco）被颠覆。

### 开源社区的"Linus Torvalds 模式"

Linux 的成功部分归因于 Linus Torvalds 既是技术领袖又是项目管理者，亲自审查代码、参与技术决策。CEO 的"knee-deep"参与可以提高决策质量和团队士气，但前提是 CEO 具备足够的技术判断力。

## 关键数据点

- Paul Graham 于 2024 年 9 月提出 [[Founder-Mode]] 概念
- 2026-05-30 Graham 发帖"CEO knee-deep in building stuff with AI"，231.2K 浏览
- 2026-05-31 Rauch 发帖"CEOs and CTOs are back to coding with a fury"，189.3K 浏览，971 likes
- 2026-05-20 Paul Ford 发表"Dear Vibe-Coding CEO: Please Stop"
- Vercel 数据：Claude 用户占 1% 但贡献 15% 部署量（Forbes, 2026-03）
- BetterUp Labs 研究：40% 员工定期收到低质量 AI 生成内容（1,150 人样本）
- Ohio State 研究：接收者认为 AI 生成的消息更懒惰、更不真诚（208 人样本）

## 前提与局限性

- **前提**：CEO 具备足够的技术直觉和学习能力来有效使用 AI 工具
- **适用边界**：对技术出身的创始人 CEO 更适用，对非技术背景的职业经理人 CEO 可能需要更多支持（如 FDE）
- **局限性**：过度参与可能导致微观管理（micromanagement），需要找到合适的参与深度
- **质量标准**：CEO 亲手 vibe coding 的产出需要组织层面的质量门控，避免低质量 demo 进入产品 backlog
- **样本偏差**：Rauch 的"CEO 回归编码"是轶事证据（"public company CEOs sliding into my DMs"），不代表普遍趋势；Rauch 自己承认"Unclear if a durable trend"

## 关联主题

- [[Karpathy-AI-Thought]] — AI 编程范式、能力鸿沟和知识管理的思想演化
- [[Agentic-Engineering-Patterns]] — Simon Willison 的 AI 编程代理工程范式指南
- [[Forward-Deployed-AI-Enablement]] — FDE 式 AI 赋能路径
- [[AI-Mediated-Organization]] — AI 中介组织的协作、权力、责任重塑

## 来源

- [[20260530-ceo-knee-deep-building-ai]] — Paul Graham 与 Guillermo Rauch 的原帖及衍生讨论
