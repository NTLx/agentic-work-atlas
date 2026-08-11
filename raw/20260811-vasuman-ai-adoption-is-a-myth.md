---
type: raw
source: "https://x.com/vasuman/status/2085806422072418632"
author:
  - "Vas (vasuman)"
  - "Varick Agents"
published: "2026-08-07"
created: "2026-08-11"
description: "Varick Agents CEO Vas 现场观察:企业 AI 落地的 barbell 分布、adoption 是 myth 的诊断、训练作为诊断而非补救、background agent 路线。"
tags:
  - "clippings"
  - "ai-adoption"
  - "barbell-distribution"
  - "fde"
  - "agent-rollout"
  - "enterprise-ai"
  - "varick-agents"
---

# AI Adoption is a Myth — vas (Varick Agents CEO)

> 推文原始 URL: https://x.com/vasuman/status/2085806422072418632
> 发布时间: 2026-08-07 19:12 (UTC+8/X 显示)
> 作者: Vas (@vasuman),CEO of Varick Agents(@varickagents) — 为大型企业实施 AI agents 与战略
> Views: 149.1 万

---

## TL;DR

- 你可能已经在 AI 用户的前 1%。前面有人,但后面是 chasm。
- 一般 Claude Cowork 类 rollout 的实际分布:**5–10% power users、20% 用得差、70% 几乎不用**,组织速度没变,但烧了百万美元。
- 用工具和"用得好"是两套技能,任何组织里至少一半人永远用不到好。
- 即使完美的 rollout 也产生 barbell:10% 的人烧 90% 的 token。
- Adoption 指标把连续谱折叠成二元 yes/no,于是出现"88% 采纳但只有 6% 看到 EBIT 影响"。
- 对顶部切片训练 + 让他们发布成果;对其余大多数人,把 AI 塞进他们已有系统的后台。

---

## 一、你已经在前 1%

你已经和前沿(20 终端齐开、知识库每次跑完自改写的人)有差距,但那个差距**远小于**你和组织里 median employee 之间的鸿沟。Median employee 可能两年里只打开过 ChatGPT 4 次,用过 3.5-turbo 然后认定 AI 是垃圾,不知道 GPT-5.6 Sol Ultra 刚证明了一个开放 50 年的图论猜想。每篇 AI 战略文章都默认这个人会追上,**他不会**。

> "You're likely in the top 1%. You're using a model every day, you have opinions about how best to use it, and you maybe even tinker with agents or have set up Hermes on your own machine."

---

## 二、The best AI tool in the world did not make them faster

Vas 接触过一家非技术企业的 ops org(数千人):

- 没 AI 时团队节奏正常,无大投诉
- 推了 Claude Cowork 后,**节奏完全一样**。领导问:why?

**他在每个组织都见过同样的分裂**——不管 50 人还是 5000 人,永远是 barbell:

| 占比 | 行为 |
|------|------|
| **5–10%** | power users。天天用 Cowork,使用 skill files、Outlook connectors 等。这是 evangelist——他们推了 Cowork 上线,因为他们工作外就在玩 AI |
| **20%** | 每天用几次,但用得很糟。拿到一点价值,但只是前沿人群的零头 |
| **70%** | 几乎不用 |

> "The dashboards in his org would indicate that the rollout counts as adoption. But to him, nothing got faster. Both of these were true simultaneously."

---

## 三、Using it and using it well are different skills

即使在用 AI 的人里,技能鸿沟也巨大。**不会用 AI 的人,用了 AI 之后比之前更糟**。

Vas 给的"安装 Claude + 指向 repo + 4 个词 prompt + 看结果"剧本 = 大量垃圾 PR 的源头。

**用得好是另一门手艺**:
- 知道何时清空 context
- 知道刚做过两次的事应该成为 skill file(模型每次都读),而不是重新打字
- 知道自动化项目里**哪 15% 需要模型做判断**、哪 85% 只需要确定性代码
- 最关键的:**在 accept 之前读 diff 读对**

### 两个工程师的对比

同样 ticket:

- **Engineer #1**: 粘 Jira 文本 → submit → Claude 改 6 个文件 → 扫一眼 → 测试还过 → merge。三周后 prod 出问题,有人发现这个 PR 无故改了一个 config 值。
- **Engineer #2**: 同样起点,但先标仓库位置、哪些文件夹/文件该碰哪些不该碰、有 skill file 确保每个 Claude PR 都极简且测试充分。然后读 diff,发现一个 stray change,一个 prompt 改掉,merge 出 Engineer #1 一半大小的 PR。

> "At least half of any organization is never going to get to that second version. Using AI well is a craft. It takes enormous iteration to get really good at using AI, and the inertia of someone who isn't on AI is insurmountable for many. **Turning a slop-cannon into a refined power user is just as hard.**"

---

## 四、A perfect rollout still produces a barbell

常见反驳:"你们公司只是做得烂。我会做得更好。"

**Vas:不。即使你完美 rollout,barbell 仍会出现**。

另一个 exec 刚签了 8 位数美元年单,推了企业 license。结果:**约 10% 的人烧 90% 的 token**。

规模感:
- 剩下 90% 的人按 top decile 用法用 AI → 花费大约 **10x**
- $10M 承诺变 $100M,**best case 变 worst case**

---

## 五、Adoption is binary, skill is a spectrum

McKinsey 2025 调研:**88% 的组织至少在一个业务职能用了 AI,但只有 6% 的 EBIT 超过 5% 来自它**。

MIT NANDA 的 GenAI Divide:5% 的集成试点榨出数百万价值,其余 95% 在 P&L 上无可测影响。

> "If you track adoption as a metric, you're very likely asking (at most) an abstraction of a yes-or-no question. 'Did this person log in this month?' 'Did this person log in this year?' 'Did this person send at least 5 prompts per day?' If you want to differentiate between 'has never opened it' and 'pastes emails in for reformatting' and 'has three agents in production touching the general ledger,' you need a better system of measurement."

99.9% 的企业 AI 采纳追踪没这个精度。**但数字在技术上是真实的,人也确实没在撒谎**——只是它们度量了一个比"人用 AI 多熟练、每个 token ROI 是多少"更容易的问题。

> "That's why AI adoption is a myth. If you actually tracked this metric, you would realize there is no hope for the vast majority of people to become AI-native in the enterprise."

---

## 六、Every incentive keeps the chasm open

- 每个 AI 厂商的路线图都在推销 agent 能力,**完全不提团队有效使用的能力**。
- 结果:唯一能高效使用的是前沿用户,他们声音最大所以有发言权。
- 他们也是"建造产品最讨好"的对象——清晰双赢。每个新特性都抬高了"用好产品"的技能门槛,**鸿沟只会越来越大**。

### 训练是 10%

> "I keep seeing enterprises seduced by the idea of 'train your employees how to prompt!' This is **10% of the game**. The other 90% is 'train your employees to understand which workflows should never touch a model vs which workflows should be entirely automated.'"

原因:prompt 训练是标准化商品,这个训练却**每家公司答案不同**,需要数周驻场才能搞出来。所以不好卖。

### 公司内部的 AI 高手也没动力修鸿沟

他们的杠杆**就是鸿沟**:
- 他们的工作快 70%,可以摸鱼
- 或者一人干三人活
- 一旦全员上同一波,他们就丢了 edge

> 凭什么让他们在没额外激励的情况下修这件事?

---

## 七、So what's the solution?

### 1. 训练(当作诊断而非补救)

> "You won't know who's in the top slice vs who's not until you do. In this sense, training is diagnostic, not remedial."

公司里肯定有"对 AI 感兴趣但没时间/杠杆深挖"的人,训练是暴露每个人的能力与舒适度。

### 2. 顶部切片: 给发表的地方

给他们一个共享数据库,每个 skill 都发布、排名、被他人安装。**这是 Vas 见过唯一能把一个人的突破变成可分享物的机制**。

激励点:**power users 愿用 edge 换 status**。

> 但 gap 仍在:即使你推给所有人,50% 的人永远不会用 skill。

### 3. 其他人: 把 AI 塞进后台

> "For everybody else, the work has to get done without them changing how they work, which means the AI goes into the background."

关键洞察:**人不需要一个帮忙做完工作的工具,他们只想工作做完**。

所以不要再问"为什么人不 prompt"——直接找出最重复的流程,在他们已有的系统(Salesforce、NetSuite、Dynamics 等)里 build agents,只在需要二次确认时拉人进来。

**例**:AP analysts 整天移发票。**90% 完全可自动化**。你不能指望他们可靠地 spin up agents 或 prompt 通流程还不爆生产。所以建 agents 每天跑,这些 analyst 变成 approve/reject/edit 自动化结果的接口人。

### 4. 改汇报口径

> "So stop reporting 'adoption' to your board. Report **what share of the work today is manual vs hybrid vs fully automated**. This is the only reporting and conversation that matters."

---

## 八、Varick Agents 的方法 (植入段落)

> 怎么 build background agents 并把它们站起来?那是另一篇文章。但更多背景:这正是 Varick 在做的事,也是给我们客户 rollout AI 唯一 work 的事。这些是非常大的公司、几千人,playbook 一样:
>
> 我们审计工作实际在哪里发生,然后 build agents 进既有 systems of record,让工作在不要求五千人变成某个他们没签字入伙的 craft 高手的情况下做完。
>
> 服务对象:收入 $500M+ 的公司,跨 finance、sales、procurement、operations、HR 等。varickagents.com
> 内容订阅: varickagents.com/newsletter

---

## 九、X 评论区选摘 (高赞回复)

### @richvieren(8月7日)

> "Me: running 20 terminal windows... Also me: 👋" (附放大视频缩略图)

### @prakshaljain_(8月7日)

> "This is incredibly true. Really like reading your self-man, are u planning on setting a sub-stack for this? I'd read it everyday!"

### @triolojules(8月8日)

> "i'm the kid running 20 terminals at the same time. **the truth is, you're not far from us, really not. however, the more you wait the more you will be far from us. create your own os that auto improve in the long terme, every action you do should feed your os. do it now**"

---

## 关键引用卡 (供未来 wiki 编译引用)

- "You're likely in the top 1%. The gap in front of you is far smaller than the gap behind you." — adoption 不是滞涨问题,而是分化问题
- "Turning a slop-cannon into a refined power user is just as hard." — 顶端 user 的稀缺本身就是企业 AI ROI 的瓶颈
- "$10M of commitment becomes $100M, and your best-case scenario is now your worst." — 完美 rollout 的隐性成本
- "Adoption is binary, skill is a spectrum." — 衡量错位是 adoption 神话的根因
- "People are not in the market for a tool that helps them get the work done. They just want the work done." — 决定你应该把 AI 塞进后台 vs 前台
- "Report what share of the work today is manual vs hybrid vs fully automated." — 改汇报口径而非改指标名

> 注:raw 是只读证据层,本文件不创建 wiki 关系链接。相关 entity / topic 关系留待 compile 阶段写入 wiki/。