---
type: entity
title: Taste
aliases:
  - Taste
definition: "在不确定条件下做出独特判断的能力，表现为能注意到什么、拒绝什么，以及精确解释哪里感觉不对的能力"
created: 2026-04-09
updated: 2026-11-28
evidence_level: medium
claim_type: mixed
tags:
  - AI-era
  - competitive-advantage
  - human-skill
related_entities:
  - '[[Judgment]]'
  - '[[Specificity]]'
  - '[[Ownership]]'
  - '[[Competent-Output]]'
  - '[[Paul-Graham]]'
  - '[[Jagged-Intelligence]]'
  - '[[Verifiability]]'
  - '[[Ghost-Intelligence]]'
  - '[[Research-Taste]]'
  - '[[Context-Advantage]]'
  - '[[Human-Curation]]'
  - '[[Wisdom-Work]]'
  - '[[Friction-as-Design-Signal]]'
source_raw:
  - '[[Andrej Karpathy: From Vibe Coding to Agentic Engineering]]'
  - '[[Good Taste the Only Real Moat Left]]'
  - '[[Taste for Makers]]'
  - '[[If You Want Taste, You''re Gonna Have to Eat]]'
  - '[[20260810-the-playbook-for-building-high-talent]]'
  - '[[20260920-lenny-peter-sellis-product-advice]]'
  - '[[20260918-oneusefulthing-the-overhang]]'
  - '[[20260810-railcode-vibe-coded-website]]'
  - '[[20261101-lenny-hector-serrano-wispr-flow-growth]]'
---

# Taste（品味）

> [!definition] 定义
> **Taste** 是在缺乏明确规则或标准时，对"什么是好的"做出准确判断的能力。AI可改变生成与选择成本，但品味不是已证明的最后护城河。按任务目标、受众、质量标准及反馈评估选择能力。

## Taste vs 个人偏好

品味涉及偏好、可讨论的领域标准与目标约束；三者并不完全等同。判别能力可以作为训练目标，不能把不同偏好诊断为无品味。

## 核心要点

### AI 时代 Taste 的重新发现

工业时代 Taste 被民主化为"个人偏好"。AI 时代 Taste 再次被重新定义为稀缺能力：

- 某些候选的生成成本降低，可能提高选择和验收的相对重要性。
- 生成、执行、验证、维护及资源协调仍可能是瓶颈；不预设人只能策展。

### Taste 的构成

候选因素：经验、反思、敏感度与反馈（非量化公式）

- **经验**：暴露于好/坏样本的次数
- **反思**：对差异的主动分析
- **敏感度**：先天的模式识别能力

Taste 是滞后指标——当环境分布发生剧变（如 AI 突然改变了"好"的边界），已有 Taste 会短暂失效，需要重新校准。

### Paul Graham 的创作型品味

[[Taste for Makers]] 把品味从审美偏好拉回“做出好东西”的实践问题：好设计通常更简单、更耐久、解决正确问题，并且经过多次再设计。这里的关键不是风格，而是创作者能否在约束下不断剔除伪复杂度。

AI 时代重新放大了这点。模型可以生成大量“看起来像好设计”的表面形态，但如果人类没有能力判断问题是否正确、复杂度是否必要、结果是否能在真实环境中承担后果，AI 只会加速平均化。

### Taste 的不可言说性

Taste 的美在于它的不可言说性。就像一个调酒师闭着眼睛知道比例对了——不是通过测量，而是通过某种全身共振的确认。但这不意味着 Taste 无法训练：它通过反复对比好/坏样本而强化，是可培养的模式识别肌肉，而非纯粹的直觉。

## 关键数据点

- 原公式缺量纲与实测参数；环境变化可能要求重新校准，但非必然失效。
- Paul Graham 在 2002 年的 [[Taste for Makers]] 中提出，品味可以通过持续设计、承认旧品味更差、研究好设计原则来训练
- 布迪厄《区分》揭示品味是阶级再生产的隐秘机制
- 18 世纪休谟试图将 Taste 客观化，提出"理想的批评家"标准
- 2025年前后部分作者提出此观点，未有代表性共识测量。
- 原幂次公式退役，保留可检验的样本、反馈、练习及评价变量。

## 前提与局限性

- **前提**：AI 时代 Taste 稀缺性的前提是生产成本趋近于零
- **前提**：Taste 判别力依赖充足的好/坏样本暴露经验
- **局限**：Taste 是滞后指标，环境剧变时短期失效，需要重新校准
- **局限**：领域、文化与目标差异仍可能改变评价；跨文化视觉艺术样本不能推出通用品味客观性。
- **局限**：Taste 训练需要时间和大量对比经验，无法速成

### 产品中的负向品味：知道什么不该加入

Peter Sellis 提供了一个与“生成好方案”互补的产品例子：他把拒绝高质量想法、让产品保持未被全部填满，视为产品领导者可以练习的品味动作；Lenny 随后指出 AI 更容易添加而不是删除，因而 PM 和设计师需要主动承担删减责任（[[20260920-lenny-peter-sellis-product-advice]]，35:24–38:30）。

**判断**：在 AI 使新增功能变便宜的环境里，品味的可操作表现不只是识别什么值得做，也包括证明什么不值得进入产品。
- **证据**：[[20260920-lenny-peter-sellis-product-advice]]（35:24–37:00、36:57–38:30）。
- **边界**：该来源是产品领导者的经验访谈；“AI 总是添加”不是已验证的模型普遍性质，删减判断仍需用户数据、产品目标与可逆性约束。

### 生成供给过剩后的选择函数

Ethan Mollick 从 capability overhang 的工作实践给 Taste 补了一个更直接的操作定义：当生成速度和数量不再稀缺，人类价值从“多生成一个候选”迁移到保留、拒绝、要求重做，以及把已有输出重新组合成模型不会主动生成的方向。

**判断**：在生成供给充足的场景中，Taste 更接近一个持续的**选择函数**，而不是作品末端的审美评价；它决定哪些候选获得后续资源、哪些被丢弃，以及何时要求探索另一条路径。
- **证据**：[[20260918-oneusefulthing-the-overhang]]；Mollick 在视频制作案例中拒绝第一版 joke、要求更 cinematic 的版本，并明确将 Taste 描述为“知道哪些 AI outputs 保留、丢弃或作为新作品原料”。
- **边界**：这是作者的工作框架与个人案例，不证明 Taste 永久属于人类，也没有证明这种选择机制在所有任务上都优于模型自选；其价值仍依赖领域知识、目标和真实反馈。

### Marketing 中的反自动化判断：知道哪一层不该追求 throughput（2026-11）

[[20261101-lenny-hector-serrano-wispr-flow-growth]] 给“生成供给过剩后的选择函数”补了一个 customer-facing creative 案例。Wispr Flow 的 Hector Serrano 用“best marketers are allergic to AI”做了强修辞，但完整语境更精确：内部研究与流程可以自动化；他反对的是在当前阶段为了提高产量，让最终公开的 video、design、editing、post-production 失去 human endpoint。理由包括 AI slop 的品牌反噬风险，以及 AI 已经让各渠道内容供给快速上升，因此单纯“更多”越来越难形成差异化（1:03:53–1:06:38）。

**判断**：Taste 的一个可操作表现是 **automation boundary judgment**——不是只在 AI 生成之后挑最好的一版，而是在流程设计时判断哪些环节可以追求吞吐，哪些环节一旦自动化会稀释客户可感知质量、真实性或品牌责任。换言之，Taste 也包括“拒绝错误的效率优化”。

- **证据**：[[20261101-lenny-hector-serrano-wispr-flow-growth]]（0:41–0:55；1:03:53–1:06:38）。
- **边界**：这是单一营销操作者在 2026-11 的经验判断，不是 AI 生成 creative 的技术上限。模型、验证和品牌工作流进步后，human endpoint 可以移动；真正稳定的原则是保留明确的质量 owner，而不是永久禁止 AI 参与最终输出。

### Fork lineage：把品味训练从模糊记忆变成显式比较（2026-10）

Railcode 官网设计复盘（[[20260810-railcode-vibe-coded-website]]）把“生成供给过剩后的选择函数”再推进了一步。作者会保存设计 forks、不删除失败分支、并排比较只改变少数变量的版本；还会让 agent 构建颜色/字体/位置 playground，让自己直接操纵参数并实时观察结果。

**判断**：如果 Taste 依赖 exposure + attention + comparison，那么 branch lineage 本身就是一种 **taste-training infrastructure**。它把“我记得前一版好像更好”变成可直接比较的对象，并保留被拒绝方案中可能在后续重新有价值的 motif。

可以把这一过程写成：

```text
大量候选暴露
  → 保留 lineage
  → 局部变量对照
  → 人类感知差异
  → reject / keep / recombine
  → 判断规则逐渐内化
```

这也补充了 Taste 的一个操作维度：**rejection bandwidth**。当 agent 可以廉价生成 4–10 个甚至更多候选时，人的稀缺资源不再是“能不能想出一个方案”，而是能否稳定地快速否掉平庸分支，同时对少数不完整但有潜力的分支保持注意力。

- **证据**：[[20260810-railcode-vibe-coded-website]]，`Forks on forks`、`Inspiration` 及结尾 process summary。
- **边界**：候选越多不必然越好；大量分支同样会制造注意力成本。来源没有测量生成数量、比较负担与最终质量的最优关系。

## 品味、形成过程与责任（历史推演校准）

原2026-06-25/27圆桌提出判断力×责任×时间及存在论、时间性、身心耦合等解释。退役其“缺一必败”“三层叠加永不可复制”“身体经历是唯一训练机制”“AI训练分布封闭所以永远不能重新校准”等稳定断言。它们属于哲学论证，不是行为实验或未来技术边界。人类生活经历、情感及责任与模型生成行为可以不同，但不能由形成过程的差异推出所有输出能力永不可复制。实际授权与责任仍由制度规定。

已有[中德审美研究](https://doi.org/10.1057/s41599-025-04806-y) 的摘要涉及中国84人与德国82人的视觉艺术评价；本轮全文访问受限，仅核对研究身份和样本，不能据此推翻整个社会建构理论或证明跨领域客观标准。参见 [[Judgment]] 与 [[AI-Era-Designer-Role]]。保留对比、反思、真实反馈与明确质量目标等候选训练方法。原推演可回查Git与历史日志。

### Ability-Taste Flip：AI 时代的范式反转（Jason Liu, 2026-07）

Jason Liu（@jxnlco）在 [[If You Want Taste, You're Gonna Have to Eat]] 中提出了 AI 时代 taste 的一个精确诊断：

```
艺术学校时代：Taste > Ability
（能看到好作品但做不出来，说不清哪里好）

AI 时代：Ability > Taste
（什么都能做，但不知道什么值得做）
```

**候选机制**：部分生产成本降低可改变生成与选择的相对负担，不代表生产成本为零或瓶颈固定迁移。Taste 不再只是审美判断——它是"建模别人会喜欢什么"的能力，是一种**偏离安全平均值的风险承担**（"taste is a kind of risk-taking"）。

**与 vibe coding 的同构**：这个翻转和 agentic engineering 领域 `vibe coding → spec-driven development` 的范式迁移是同构的。Vibe coding = 有 ability 无 taste（什么都能生成，不知道什么是好的）；Spec-driven = taste 前置（先定义"什么算好"再让 AI 执行）。

### Attention Friction：品味需要的摩擦正在被系统性地移除

Liu 的核心论证链：

```
候选机制：工具改变注意力与练习机会 → 可能改变品味形成；需测量，不是单向因果式
```

具体机制（四个层面的摩擦消失）：
1. **学习层**（Transcribing）：AI 直接给乐谱 → 跳过了反复聆听的"耳朵训练"。AI "strips the aura from learning"——消除的是技能形成所需的 "felt distance"
2. **导航层**（Wandering）：GPS 蓝线取代自由漫游 → 不再通过迷路来"知道东西在哪"
3. **消费层**（Eating Slowly）：二十年优化摩擦 → 摩擦才是品味的发生器——"the friction was where the taste was"
4. **创作者层**（Authorship Collapse）：TikTok 反转了 YouTube 模式——从"关注人→看到内容"变成"内容涌入→创作者是次要的"——人们消费对象而非对象背后的决策链

**应对原则**：如果工具一直在移除注意力，你必须刻意把它放回去——"If taste grows with attention, and the tools keep removing the attention, then you have to put it back on purpose."

### Taste 的训练方法：Eat → Notice → Record

Liu 提供了一套操作性方法，补充了已有讨论中缺失的"怎么练"维度：

1. **Eat（吃）**：像厨师一样——不能只看菜单，必须去吃。试穿不买、听整张专辑、追溯鼓手的其他作品
2. **Notice（注意）**：建立自己的感知层级——是材质触感还是垂坠感？结构和形式先于颜色。每个人的层级不同，只能通过"把东西放在身上并注意"来发现
3. **Record（记录）**：保持"为什么"的记录——不只是消费对象，而是消费"对象背后的决策链"（谁做的？什么时候？什么情境？）

### Rikyū Courage：品味 = 爱只有你能看到的东西

茶道史上的辩证法（来源：冈仓天心《茶之书》）：

| 人物 | 品味特征 | 社会反馈 |
|------|---------|---------|
| 千利休（Rikyū） | 只有利休能欣赏 | 孤独的好品味 |
| 小堀遠州（Enshū） | 人人都说好 | 共识的好品味 |

遠州承认自己**更低级**：他只是选了大多数人会喜欢的东西。利休有勇气爱只有自己能看到的东西。

**核心命题**：品味 ≠ 共识。好奇心必须先于判断力（否则永远不拓宽视野），勇气在好奇心之后——诚实到爱真正与你共振的东西，即使没人在穿、没人在听、没人在买。

## 关联概念

- [[Judgment]] — Taste 是 Judgment 在审美和创意领域的具体化
- [[Specificity]] — Taste 表现为拒绝通用选项，指向深入特定上下文的判别
- [[Ownership]] — 拥有 Taste 意味着承担判断后果的责任
- [[Competent-Output]] — AI 默认产出的"合格但平庸"内容，正是 Taste 要拒绝的对象
- [[Discernment]] — Taste 与 Discernment 同属判别力维度
- [[Decision-Quality]] — Taste 为 Decision Quality 提供审美和创意维度的判别力
- [[Refusal]] — Taste 的核心动作是"拒绝什么"

## 招聘侧印证：IC 品味与判断力的回归（2026-08）

Adam Ward（Cursor 招聘负责人）从人才市场侧独立给出同一信号："past 12 months, the rise of the power of IC——taste, decision-making, problem solving, curiosity are coming back up to the surface"。这与本实体"AI 时代 Taste 重新成为稀缺能力"互补：[[AI-Identity-Bifurcation]] 提供感受侧数据、[[Systems-Thinker-Demand]] 提供需求侧机制，此处是招聘词表侧的确认——IC 的 taste/judgment 明确进入一线 AI 公司的选人标准。

## 来源

- [[Good Taste the Only Real Moat Left]]
- [[20260413-why-ai-first-strategy-wrong]] — CREAO CTO Peter Pang: "产品感知或品味很重要。你能看着一个生成的UI，在用户开口之前就知道它不对吗？"
- [[If You Want Taste, You're Gonna Have to Eat]] — Jason Liu: ability-taste flip + attention friction + Rikyū courage
