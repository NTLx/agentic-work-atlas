---
type: source-summary
title: "AI Mania Is Eviscerating Global Decision-Making"
source_raw:
  - "[[20260718-ai-mania-eviscerating-decision-making]]"
created: 2026-07-27
updated: 2026-07-27
tags:
  - source-summary
  - ai-hype
  - organizational-decision-making
  - ai-failure
  - institutional-capture
  - ai-governance
evidence_level: medium
claim_type: mixed
---

# AI Mania Is Eviscerating Global Decision-Making

> Ludicity（独立咨询公司创始人）基于 1.5 年一线销售与交付经验，报告观察到的所有 AI 项目均失败（0% 成功率），并描述了一个由真信者、博弈论均衡和恐惧驱动的组织性 AI 狂热生态。来源：个人博客（2026-07-18）。证据等级：medium（一手观察但未量化、无第三方验证）。

## 编译摘要

### 1. 浓缩

- **核心结论1**: 作者团队观察到的所有 AI 项目在 1.5 年内 100% 失败——不仅是参与的项目，也包括顺带观察到的项目
  - 关键证据: 即使承认 AI 在特定工作负载上有加速，投资的方法和规模也是无意义的；多数失败来自企业本就无法有效管理软件项目，AI 项目承受普通项目的所有失败模式加上新增的技术不确定性
  - 内部聊天机器人案例: 员工不使用，因为公司文档质量低，LLM 无法获取未被写下的知识；Mitsubishi 客服机器人案例——技术表面完善但六个月未回电，失败被隐藏在指标中
- **核心结论2**: 组织中已形成"信仰宣告"文化——质疑 AI 策略的人被解雇，顺从者被奖励，导致 AI-washing 普遍化
  - 关键证据: 500+ 人企业中，晋升和继续就业要求反复"宣誓"AI 转型信念；工程师 AI-wash 工作（实际不用 AI 但声称用了）；"token leaderboard"——token 消费越高越好，工程师设置 AI 自我循环刷 token 然后看 Netflix；唯一被解雇的人是表达怀疑的人
  - 极端案例: 一位从未使用过 ChatGPT 的高管为 $2B+ 收入企业制定了以 AI 为核心的技术战略；一位老板解雇了最高绩效员工，因为他们没有使用 LLM 达成业绩
- **核心结论3**: 供应商-客户之间存在博弈论均衡（round-robin）——双方都不相信 100x 生产力声明，但谁先说实话谁就被惩罚
  - 关键证据: Fortune 500 匿名高管证词——客户高管声称 100x 生产力以免被供应商 AM 报告给投资者显得落后，供应商声称 100x 以免被客户高管视为否定其公信力；结果是所有人都向各自董事会报告繁荣，没人知道是否有任何真实产出
  - 传导机制: 不知情的善意管理者看到市场声明后启动自己的 AI 项目，完全不知道声明是无根据的

### 2. 质疑

- **关于"0% 成功率"的质疑**: 这是单一咨询公司视角，存在严重选择偏差——他们接触的客户多是需要外部帮助的企业（即已有问题的企业），且"成功"的定义未明确。Anthropic 经济指数、Cursor 开发者习惯报告等数据源显示部分 AI 工具确实在提升个体开发者效率。0% 是一个情绪驱动的强修辞，不应被当作行业统计数据
- **关于"信仰宣告"文化的质疑**: 作者的例子极端但数量有限（"several occasions"、"one extreme case"）。组织中存在技术热潮期的从众行为是历史常态（云计算、区块链、移动优先都有类似现象），需区分 AI 特有的结构性问题和所有新技术采纳周期的共性表现
- **关于博弈论均衡的质疑**: round-robin 动态解释力强，但其推论（"没人能停下"）过于决定论。历史上的商业泡沫（dot-com、housing）同样有类似的 nobody-can-stop-first 结构，但最终由外部冲击（资金链断裂、监管）打破。更关键的问题不是均衡是否存在，而是什么力量足以打破它
- **关于作者立场的质疑**: Ludicity 经营数据咨询公司（部署 Snowflake 等分析工具），其商业模式隐含"AI 不是答案，好的数据治理才是"的立场。文章虽坦诚声明了利益相关，但批评 AI 项目同时推销自己的非 AI 方案，激励结构值得注意

### 3. 对标

- **跨域关联1: 安然式 mark-to-market 会计 → AI 绩效声明的 round-robin**: 安然用 mark-to-market 会计法把未来预期收入记为当期收入，交易对手也必须配合以维持自己的账面。AI 生产力声明的 round-robin 结构几乎完全同构——双方都报告"100x 生产力"以维持对方的估值叙事，真实绩效被推迟到无人追溯的未来
- **跨域关联2: 苏联农业产量报告 → token leaderboard**: 基层干部虚报产量以满足上级指标，上级据此制定更高目标，形成指标通胀螺旋。工程师刷 token leaderboard 是同一机制的微型版本——Goodhart 定律在 AI 采纳中的活体案例
- **跨域关联3: Overton Window 与"可说空间"**: 文章描述的"表达 AI 怀疑 = 被解雇"本质上是企业内部 Overton Window 的急剧收窄。可类比宗教改革前的异端裁判——不是信仰的正确性，而是表达怀疑的成本决定了公共话语

### 关联概念

- [[AI-Psychosis]] — 文章为 AI Psychosis 提供了最详细的企业行为实证（真信者 vs 博弈者的区分）
- [[AI-Washing]] — AI-wash 工作（工程师假装用 AI）是 AI Washing 概念的个体层面延伸
- [[Goodharts-Law]] — token leaderboard 是 Goodhart 定律在 AI 采纳场景的鲜活案例
- [[Decision-Quality]] — round-robin 动态系统性降低了组织决策质量
- [[AI-Capability-Gap]] — 作者的观察从供给侧（项目失败率）印证了需求侧的能力鸿沟
- [[Cognitive-Surrender]] — "宣誓 AI 信仰"文化是组织层面的认知投降
- [[AI-Deployment-Valley-of-Death]] — 0% 成功率指向部署死亡谷问题
- [[AI-Ready-Organization]] — 文章隐含的论点：多数组织不具备 AI-ready 的基础条件
