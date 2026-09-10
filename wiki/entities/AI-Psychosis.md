---
type: entity
title: AI Psychosis
aliases:
  - AI Psychosis
  - AI 震撼错位
  - AI 能力震撼
  - CEO AI Psychosis
definition: "一个被混用于不同现象的总称：临床语境中的真实精神病性体验，以及 AI 工作语境中由能力外推或产出—价值脱钩造成的现实校准失败"
created: 2026-04-16
updated: 2026-09-10
tags:
  - AI-agent
  - perception-gap
  - organization
evidence_level: medium
claim_type: mixed
related_entities:
  - '[[Andrej-Karpathy]]'
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
  - '[[20260616-why-is-meta-destroying-its-engineering]]'
  - '[[20260718-ai-mania-eviscerating-decision-making]]'
  - '[[20260901-jeff-clark-defining-ai-psychosis-part-1-true]]'
  - '[[20260908-jeff-clark-defining-ai-psychosis-part-2-prolific]]'
---

# AI Psychosis

> [!definition] 定义
> 一个被混用于不同现象的总称：临床语境中的真实精神病性体验，以及 AI 工作语境中由能力外推或产出—价值脱钩造成的现实校准失败。后者包括深度用户把 coding agent 的高峰体验外推到全领域，也包括 CEO 只看到 AI 的 happy path 就推动组织重组。

## 三种用法：先分层

Jeff Clark, MD 在 2026 年 9 月的系列文章中指出，`AI psychosis` 至少被用于三种不同现象：

| 用法 | 对象 | 核心问题 | 当前证据边界 |
|------|------|----------|--------------|
| **True AI Psychosis** | LLM 使用相关的真实精神病性体验 | 是否出现固定、虚假且具有个体化特征的信念，及其对现实判断和生活功能的影响 | 临床概念；不能由网络标签或单次模型对话直接诊断 |
| **Prolific AI Psychosis** | 过度投入 AI 工具的工作者 | AI 产出数量上升，却没有同步增加真实价值，甚至破坏质量与可维护性 | 非临床修辞；尚无量表、阈值或发生率数据 |
| **Parasocial AI Psychosis** | 与 LLM 建立失衡单向关系的人 | 把拟人化、迎合性的对话系统当作真实社会关系 | 当前已剪藏材料只完成术语登记，尚未编译其后续机制 |

### 判断

`AI Psychosis` 最有用的用法不是给人贴标签，而是先识别究竟发生了症状、行为模式，还是由 AI 能力错位引发的组织叙事。

- **证据**：[[20260901-jeff-clark-defining-ai-psychosis-part-1-true]]；[[20260908-jeff-clark-defining-ai-psychosis-part-2-prolific]]
- **边界**：Jeff Clark 的系列文章是单一作者的概念性说明；其中临床因果关系未知，`prolific` 与 `parasocial` 也不是医学诊断。

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
- **Meta 案例（2026-06）**：30-50% 核心团队工程师被强制调去做数据标注（ADO 组约 6500 人）；所有工程师键盘/鼠标点击被追踪用于 AI 训练（无 opt-out）；30 天使用 60.2 万亿 tokens（价值约 `$900M`）；Instagram 安全漏洞（零认证密码重置）由 AI 生成 + AI 审查代码导致；CISO 在事件次日辞职（[[20260616-why-is-meta-destroying-its-engineering]]）

## 风险与用法

AI Psychosis 的风险有两面。

一面是低估。没有见过前沿 agentic 模型接入真实代码库的人，可能把 AI 仍理解为聊天网站，从而低估工程流程、网络安全、组织岗位和知识工作被重写的速度。

另一面是过度外推。深度用户容易把 coding agent 的高峰体验外推到所有领域，忽略 [[Ghost-Intelligence]] 和 [[Jagged-Intelligence]] 的限制：模型在训练回路、可验证任务和高投入领域极强，但不代表它拥有均匀、稳定、类人的通用判断。

更稳妥的用法是把 AI Psychosis 当作能力评估提示器：当两个人对 AI 的判断差异极大时，不急着争论谁对，而是先比较他们实际使用的模型、任务、工具链和验证条件。

在工作语境中，还要把“生成了多少”与“产生了多少价值”分开。[[Agent-Harness]] 让 AI 可以持续生成、调用工具和循环执行，但也会放大隐藏的维护成本与失败；因此 [[Agent-Verification]]、外部结果和人类判断不能被 token、代码行数或任务数量替代。

## CEO AI Psychosis（Levie, 2026）

2026 年 5 月，Box CEO Aaron-Levie 在 X 上提出了 AI Psychosis 的组织层扩展：CEO 群体因结构性地远离"最后一英里"工作，成为 AI 认知错位的高发人群。

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

## Meta 案例：AI Psychosis 的企业级实证（2026-06）

Pragmatic Engineer 深度报道（Gergely Orosz, 2026-06-16）揭示了 Meta 工程文化在数周内被系统性摧毁的过程，为 AI Psychosis 提供了最极端的企业级实证。

### 执行机制

1. **监控**：所有工程师的键盘和鼠标点击被追踪用于 AI 训练数据，无 opt-out（英国因数据保护法规除外）
2. **强制调岗**：30-50% 核心团队工程师被调去 ADO 组（Agent Data Optimisation）做数据标注，约 6500 人（其中 4500+ 是软件工程师）
3. **Token 测量**：绩效考核（PSC）中测量 token 使用量，工程师为提升指标而过度使用 AI
4. **裁员恐慌**：在创收创利背景下宣布 10% 裁员，制造四周的不确定性

### 自我实现预言循环

```
"战时状态"宣言
    ↓
降低质量标准（AI 生成 + AI 审查即可）
    ↓
代码质量真的下降
    ↓
生产环境故障（Instagram 零认证密码重置）
    ↓
需要更多"紧急措施"
    ↓
强化"战时状态"叙事
    ↓
（循环）
```

### 与其他 AI Psychosis 案例的区别

| 维度 | Levie 描述的 CEO AI Psychosis | Meta 案例 |
|------|-------------------------------|-----------|
| 触发 | CEO 看到 AI happy path | 整个领导层将 AI 信念凌驾于工程判断 |
| 行为 | 大规模裁员 | 监控 + 强制调岗 + tokenmaxxing + 裁员 |
| 后果 | 岗位消失 | 工程文化系统性摧毁 + 生产环境灾难 |
| 可逆性 | 中等（可重新招聘） | 低（最佳工程师已流失、信任已崩塌） |

### Mitchell Hashimoto 的诊断

HashiCorp 创始人 Hashimoto 指出核心风险：**MTTR 思维（快速修复）取代 MTBF 思维（预防故障）**。当领导层说"AI 能快速修复 bug"时，他们忽略了：
- 系统看似健康（bug 报告下降），但架构在衰变
- 测试覆盖率上升，但语义理解下降
- 变化速度加快，但没人注意到底层架构腐烂

**简言之**：AI Psychosis 的极端形式是用"AI 能修好"替代"不要让坏代码上线"——这是工程哲学的根本性倒退。

## 前提与局限性

- **术语边界**：`True AI Psychosis` 在文章中指临床意义上的精神病性体验；`prolific` 和 `parasocial` 是工作/社会语境中的非临床修辞，三者不能混为一谈。
- **领域前提**：主要描述 agentic coding、数学、研究等可验证领域的震撼体验，不代表所有知识工作都有同等跃迁。
- **价格前提**：依赖前沿付费模型、工具权限和真实工作流接入，免费或旧模型体验不同。
- **时间前提**：能力鸿沟可能随模型普及和界面变化缩小，也可能因新一代模型继续扩大。
- **外推边界**：震撼感不是证据本身，仍需用任务成功率、测试、审查和生产后果校准。
- **系列边界**：当前只编译了系列第一、第二篇；第三种拟社会关系的机制与边界不在本次证据范围内。

## 关联概念

- [[AI-Capability-Gap]]：不同用户群体看到不同 AI 现实
- [[Jagged-Intelligence]]：能力分布不均导致体验差异巨大
- [[Ghost-Intelligence]]：不要把统计模型误读为动物智能
- [[Agentic-Engineering]]：让震撼体验进入生产工程的实践框架
- [[Claude-Code-CLI]]：触发 AI Psychosis 的典型 coding agent 工具
