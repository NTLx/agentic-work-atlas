---
type: source-summary
title: "Work at the Frontier: How AI is expanding what people do at work"
canonical_url: "https://openai.com/index/how-ai-is-expanding-what-people-do-at-work/"
raw_state: index
original_raw_file: "20260727-openai-work-at-the-frontier.pdf"
original_body_sha256: "3ffb4cc2bb97aaac8dc0f5bf715ee17f6f4b4629097b89558aa9d8ab199d4781"
indexed_at: "2026-08-25T01:10:28+08:00"
created: 2026-07-28
updated: 2026-08-25
tags:
  - source-summary
  - ai-labor
  - economy
  - organization
evidence_level: medium
claim_type: mixed
---

# Work at the Frontier: How AI is expanding what people do at work

> Raw 生命周期：本地 PDF 已降级为可恢复索引；样本量与 task crossover 数据的精确引用从 canonical URL 回到 OpenAI 原始报告核验。

> OpenAI Economic Research（Caroline Chin, Alex Martin Richmond, 2026-07）分析 80 万+ 条美国 ChatGPT 用户的工作相关消息，以 O*NET 职业数据库为历史基线测量 **task crossover**（任务跨界）：16.8% 的工作消息涉及其他职业的历史任务，职业专属消息中跨界比例达 43.5%。核心发现：AI 不仅改变工作如何做，更改变**谁来做**——职业边界在职位描述修改之前就已经开始松动。来源：OpenAI 官方研究页面（2026-07-27）。证据等级：medium（大样本一手使用数据 + 严谨方法论与局限性声明，但测量单位为消息而非工作成果，且 OpenAI 研究自家产品影响的立场需纳入考量）。

## 编译摘要

### 1. 浓缩

- **核心结论1**: AI 使用数据揭示了一个先于职位描述变化的现象——任务跨界（task crossover）：历史上与某职业关联的工作，大量出现在其他职业从业者的 AI 使用中
  - 关键证据: 80 万+ 条消息三分类——Generic（61.5%，写作/摘要/排程等跨职业通用任务）、Within occupation（21.8%）、Cross-occupation（16.8%）；剔除通用任务后，**43.5% 的职业专属消息跨界**。五组职业的跨界消息占本组职业专属消息的多数：客户体验 77%、设计 75%、人力资源 69%、法务 56%、营销 53%
- **核心结论2**: 跨界是不对称的，八个职业分化为三种角色——借用者、被借用者、双向者；营销与工程的任务流动最远
  - 关键证据:
    - **借用者（design 型）**: 设计师 35.2% 的消息涉及外职业任务，但设计任务只占其他职业消息的 1.7%——大量吸收、几乎不被借用
    - **被借用者（engineering 型）**: 工程师自身跨界仅 18.5%（八组最低），但工程任务占其他职业消息的 7.4%——任务外流的主要源头
    - **双向者（marketing 型）**: 营销人员 24.3% 跨界，营销任务占其他职业消息 8.9%（样本最高）
    - 高频跨界任务: 财务计算（出现在 7/7 非财务职业的前三）、计算机故障排查（7/7 非工程职业）、营销材料制作（非营销用户营销类消息的 25%）
- **核心结论3**: 小规模职场的典型用户跨界更多——AI 在"没有专家可委派"时成为专家的替代
  - 关键证据: 中位 50% 消息量用户中，2-5 人工作区跨界 18.9% vs 101+ 人工作区 16.3%；该模式在重度用户（top quartile）中消失——重度用户的额外消息量可能是核心职业内的重复深化（迭代编码/编辑/分析）而非职能扩张

### 2. 质疑

- **关于测量单位的质疑**: 分析单位是消息，不是工时、项目或工作成果；研究未观测产出是否被实际采用、质量如何、节省了多少时间。**跨界尝试 ≠ 成功完成 ≠ 替代专家**——一个销售用 AI 探索数据集，不等于他成了分析师
- **关于样本代表性的质疑**: 数据来自 ChatGPT Business 用户的**个人账号**（职业信息来自 Business，消息来自个人账号）、仅限美国、职业自报告；报告明确声明不可推广到 Enterprise 用户或全体劳动力。样本是"愿意自报职业的商务用户"，本身是 AI 早期采纳者的子集
- **关于分类边界的质疑**: Generic/Within/Cross 三分法本身决定跨界率——61.5% 被归为通用任务（写作、摘要、排程）。若分类器把更多任务判为通用，跨界率随之下降；O*NET 作为"历史基线"也预设了职业边界是固定的参照系，而边界本身正在变化（循环性问题）
- **关于因果方向的质疑**: 跨界可能反映"试探性尝试"而非"持久角色重组"。报告自列此为开放问题：反复的跨界使用是否会导致工作职责的持久变化，尚无纵向证据
- **关于激励结构的质疑**: OpenAI 研究自家产品对劳动力市场的影响，"AI 扩展角色而非替代工人"的叙事与其监管利益一致——与库内 langchain/咨询/部署服务商三源同构的激励审视（见 [[20260727-langchain-own-your-intelligence]] 质疑节）。但报告的局限性声明相当诚实，且同步开放了 External Research Exchange 引入独立劳动经济学家，部分对冲了立场问题

### 3. 对标

- **理论谱系: task-based framework 的 AI 时代测量**: 劳动经济学的任务框架（Autor/Levy/Murnane 2003 用任务分解理解计算机对职业的影响；Acemoglu/Restrepo 2019 强调技术通过"把既有任务重新分配给资本 + 创造劳动比较优势的新任务"改变劳动力需求）此前只能用就业数、工资、岗位发布等**滞后指标**推断。本报告第一次用**使用数据**测量"正在发生的任务再分配"——处于岗位演化链条的最上游，先于职位描述和职衔修改
- **跨源收敛: 定性观察获得定量验证**: [[Role-Merging]] 的既有证据是定性轶事（Anthropic 内部：设计师提 PR、PM 改代码、财务用 Claude Code）。本报告从另一数据源（ChatGPT 80 万消息 vs Claude 团队观察）独立收敛于同一现象；Yang et al. (2026) 对 Perplexity 的研究（查询经常落在用户主业之外）是第三源互证。三方数据源不同、方法不同、结论同向
- **测量传统对比: exposure vs agency**: Anthropic Economic Index 测"AI 在执行哪些任务"（暴露度，机器侧视角），本报告测"人在用 AI 跨界做哪些任务"（能动性，工人侧视角）——同一扇使用数据之窗的两个相反提问方向（综合判断）
- **跨域类比: adjacent possible**: 任务跨界 ≈ Kauffman 创新理论中的"相邻可能"——AI 扩张了个体可尝试任务的边界，创新首先发生在与现有能力相邻的边界上，而非任意远处（设计师借用营销/工程任务多，借用 distant 领域少）。小职场跨界更多 ≈ 生态学中"资源稀缺环境的生态位宽度扩张"——没有可委派的专家时，个体被迫（也被赋能）成为通才（综合判断）
- **与库内命题的连接**: 为 [[Cross-Disciplinary-Generalist]] 提供实证分布（三种角色 = 通才形态的三种实现路径）；"the list itself is changing"（任务清单本身在变）是 [[Knowledge-Work-Redefinition]] 中 Autor 移动边界定理的实证回响——边界定理预测"非例行认知是移动类别"，本报告测量到边界正在移动

### 关联概念

- [[Task-Crossover]] — 本报告命名的核心现象，新建 entity
- [[Role-Merging]] — 定性观察获得大样本定量验证
- [[Cross-Disciplinary-Generalist]] — 三种跨界角色 = 通才形态的实证分布
- [[Labor-Market-Impact]] — 任务再分配先于就业/工资等滞后指标的最上游测量
