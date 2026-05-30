---
type: entity
title: AI Psychosis
aliases:
  - AI Psychosis
  - AI 震撼错位
  - AI 能力震撼
  - CEO AI Psychosis
definition: "因与 AI 实际工作的'最后一英里'脱节而产生的认知错位——深度用户过度外推高峰体验，CEO 过度相信 AI 能替代人类工作"
created: 2026-04-16
updated: 2026-05-30
tags:
  - AI-agent
  - perception-gap
  - organization
related_entities:
  - '[[Andrej-Karpathy]]'
  - '[[Aaron-Levie]]'
  - '[[Agentic-Engineering]]'
  - '[[Claude-Code-CLI]]'
  - '[[AI-Capability-Gap]]'
  - '[[Ghost-Intelligence]]'
  - '[[Jagged-Intelligence]]'
  - '[[AI-Washing]]'
source_raw:
  - '[[Andrej Karpathy: From Vibe Coding to Agentic Engineering]]'
  - '[[20260409-ai-capability-gap-ai-psychosis]]'
  - '[[20260529-ceo-ai-psychosis-equity-podcast]]'
---

# AI Psychosis

> [!definition] 定义
> 因与 AI 实际工作的"最后一英里"脱节而产生的认知错位。原始含义（Karpathy, 2025）：深度使用前沿 agentic coding 模型的人因亲历能力跃迁而对 AI 进步速度产生强烈紧迫感。扩展含义（Levie, 2026）：CEO 因远离实际工作流程，只看到 AI 的 happy path，却据此做出大规模裁员等组织决策。

## 为什么重要

AI Psychosis 不是临床心理学概念，而是 Karpathy 用来描述一种能力感知错位：一部分人长期使用 Claude Code、Codex 等前沿 agentic coding 模型，让模型读代码、改代码、跑测试、查漏洞；另一部分人仍以免费聊天机器人、语音助手或普通问答体验评估 AI。

这两边看到的现实都可能是真的。普通用户会遇到幻觉和低级错误，专业用户也确实可能看到模型在代码、数学、科研等可验证领域完成原本需要数天的任务。认知鸿沟来自任务域、模型代际、付费层级、工具接入和验证机制的差异。

这个概念的价值不是渲染焦虑，而是提醒：讨论 AI 能力时必须先说明使用的是哪一代模型、什么价格层、什么任务、是否接入真实工具链、结果如何验证。

## 关键数据点

- Karpathy 将震撼感与"使用 AI 编程的程度"联系起来，尤其是把终端交给 agent 完成真实工程任务的体验。
- [[20260409-ai-capability-gap-ai-psychosis]] 指出，编程、数学、研究等任务更容易形成可验证 reward，因此能力跃迁更陡。
- 免费助手用户、旧模型用户、付费专业用户和顶尖 AI researcher 看到的是不同产品形态。
- OpenAI 与 NBER 相关研究中，编程在 ChatGPT 查询中占比不高，而非工作类查询占比较高，这会让大众体验低估 coding agent 的冲击。
- [[Jagged-Intelligence]] 解释了为什么模型能在某些技术任务上很强，同时在普通常识上犯错。

## 风险与用法

AI Psychosis 的风险有两面。

一面是低估。没有见过前沿 agentic 模型接入真实代码库的人，可能把 AI 仍理解为聊天网站，从而低估工程流程、网络安全、组织岗位和知识工作被重写的速度。

另一面是过度外推。深度用户容易把 coding agent 的高峰体验外推到所有领域，忽略 [[Ghost-Intelligence]] 和 [[Jagged-Intelligence]] 的限制：模型在训练回路、可验证任务和高投入领域极强，但不代表它拥有均匀、稳定、类人的通用判断。

更稳妥的用法是把 AI Psychosis 当作能力评估提示器：当两个人对 AI 的判断差异极大时，不急着争论谁对，而是先比较他们实际使用的模型、任务、工具链和验证条件。

## CEO AI Psychosis（Levie, 2026）

2026 年 5 月，Box CEO [[Aaron-Levie]] 在 X 上提出了 AI Psychosis 的组织层扩展：CEO 群体因结构性地远离"最后一英里"工作，成为 AI 认知错位的高发人群。

### 机制

CEO 看到 AI 的 happy path（生成原型、起草合同），但不需要：
- 审查代码、发现 bug、识别幻觉库调用
- 在公司特有的合同条款上训练 AI 模型
- 花数天时间逐行审查合同中的隐藏条款

这种信息不对称导致 CEO 做出"agents 已经能做这些工作"的跳跃推断，进而推动大规模裁员。

### 关键数据

- 2026 年前 5 个月科技行业裁员 115,430 人，接近 2025 全年的 124,636 人（[[20260529-ceo-ai-psychosis-equity-podcast]]）
- ClickUp 裁掉 22% 员工（约 3,000 人），用 3,000 AI agents 替代，CEO Zeb Evans 称之为"100x org"
- Gartner 调查（350 位全球高管）：80% 试点 AI 的企业报告了裁员，但**不论技术是否真正产生回报都裁了**
- CMR 元分析（2025.10）：**无稳健证据**表明 AI 采纳与总体生产力提升有关
- NBER（2026.3）：发现"生产力悖论"——感知收益大于实际测量收益
- MIT（2026）：预测到 2029 年 AI 才能在大多数文本任务上达到 80%-95% 基线质量

### 与 Karpathy 版本的关系

| 维度 | Karpathy (2025) | Levie (2026) |
|------|----------------|--------------|
| 主体 | 深度 agentic coding 用户 | CEO / 高管 |
| 方向 | 紧迫感（可能过度外推） | 过度自信（低估剩余工作） |
| 来源 | 亲历高峰体验 | 远离实际工作 |
| 行为 | 渲染焦虑、加速主义 | 大规模裁员、组织重组 |
| 共同点 | 都基于与 AI 实际能力的脱节，都容易从有限体验做全局推断 |

### Levie 的建议

"Use AI a ton, to figure out the real implications of agents in the enterprise, and come out the other side with an appreciation for both the upside and the real work that goes into them."

但需注意：更多接触 AI 不等于自动校准判断。深度用户同样可能陷入 Karpathy 版本的 AI Psychosis——把 coding agent 的高峰体验外推到所有领域。

### 自上而下 vs 自下而上（播客新增维度）

历史上的技术变革（BYOD、Slack、GitHub）多是 worker 自发引入后管理层接受（自下而上）。AI 采纳似乎反过来了——executives 和 VCs 推动"小团队 = 大公司"的梦想，worker 被动适应。

> "a lot of the idea of these AI productivity gains seems to be embraced by the executives or... by the VCs who are funding you, who love this dream of... a tiny team and be as effective as a company with a much larger team" — Anthony Ha, Equity Podcast (30:17-31:29)

这意味着 AI Psychosis 不仅是认知偏差，还可能是**权力结构**问题：决策权与执行经验分离的人推动变革，执行者承受后果。

### AI 成本与裁员的隐性关系

播客 (33:16-33:49) 揭示了一个常被忽略的维度：裁员不完全是因为"AI 能替代"，部分是为了**offset AI 的高昂成本**。这让 AI Washing 的判断更复杂——公司可能同时在做两件矛盾的事：一边声称 AI 提升了效率，一边用裁员来填补 AI 的账单。

### Worker Burnout 风险

更少的人 + AI 工具 = 更高的个人产出，但也意味着更少的同事来分担认知负荷和情感支持。

> "there are trade-offs that don't get discussed... it maybe burns them out a lot quicker, especially because they have fewer people around them to commiserate with and collaborate with" — Anthony Ha, Equity Podcast (34:13-34:55)

这是 AI Psychosis 的组织层后果：CEO 看到效率提升，worker 体验到 burnout 加速，两边的现实再次分裂。

## 前提与局限性

- **非临床术语**：这里的 psychosis 是修辞，不应被当作医学诊断。
- **领域前提**：主要描述 agentic coding、数学、研究等可验证领域的震撼体验，不代表所有知识工作都有同等跃迁。
- **价格前提**：依赖前沿付费模型、工具权限和真实工作流接入，免费或旧模型体验不同。
- **时间前提**：能力鸿沟可能随模型普及和界面变化缩小，也可能因新一代模型继续扩大。
- **外推边界**：震撼感不是证据本身，仍需用任务成功率、测试、审查和生产后果校准。

## 关联概念

- [[AI-Capability-Gap]]：不同用户群体看到不同 AI 现实
- [[Jagged-Intelligence]]：能力分布不均导致体验差异巨大
- [[Ghost-Intelligence]]：不要把统计模型误读为动物智能
- [[Agentic-Engineering]]：让震撼体验进入生产工程的实践框架
- [[Claude-Code-CLI]]：触发 AI Psychosis 的典型 coding agent 工具
