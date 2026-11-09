---
type: source-summary
title: "Why PMs are suddenly valuable again | Tulsee Doshi (Head of Product, Gemini)"
source_raw:
  - "[[20261108-lenny-tulsee-doshi-frontier-model-pm]]"
canonical_url: "https://www.lennysnewsletter.com/p/what-it-actually-takes-to-build-frontier"
raw_state: full
created: 2026-11-09
updated: 2026-11-09
tags:
  - source-summary
  - product-management
  - model-evaluation
  - agentic-engineering
evidence_level: medium
claim_type: mixed
source_locator:
  - "用户附件原始 Transcript L66–L110：模型组合、训练目标与训练后能力发现"
  - "用户附件原始 Transcript L122–L150：Google 全栈与质量/成本 Pareto 战略"
  - "用户附件原始 Transcript L162–L200：安全监控和网络防御自述"
  - "用户附件原始 Transcript L220–L282：不同用户的产品 UX，以及模型行为 spec→rubric→data→reward"
  - "用户附件原始 Transcript L286–L340：PM taste/判断、hands-on、从 5 到 20 个 prompts 建立评测"
  - "用户附件原始 Transcript L344–L410：eval 与 vibe 互补、Fitzpatrick→Monk 尺度及端到端 serving"
  - "用户附件原始 Transcript L422–L446：Flash Teams 与专业 Agent 的有限类比"
  - "用户附件原始 Transcript L466–L540：60/20/20、模型升级后的 Harness 重测及定义"
  - "用户附件原始 Transcript L546–L620：团队技能库、workshops、重复任务自动化"
  - "用户附件原始 Transcript L650–L724：过劳、文档噪声、数据和洞察分工"
  - "用户附件原始 Transcript L726–L742：PM 应亲自提供 prototype/evaluation/data evidence"
---

# Why PMs are suddenly valuable again — Tulsee Doshi

> **一手来源**：[Lenny's Newsletter / Podcast（2026-11-08）](https://www.lennysnewsletter.com/p/what-it-actually-takes-to-build-frontier)。访谈者 Lenny Rachitsky；受访者 Tulsee Doshi（Google Gemini 等 frontier models 产品负责人）。**本次编译依据用户提供的 956 行完整英文 Transcript**，并保留全部原文于 `raw/20261108-lenny-tulsee-doshi-frontier-model-pm.md`（`raw_state: full`）。官方 URL 可回查标题与采访页；由于网页订阅限制，完整逐句证据依据附件，不声称已在网页端独立复核全文。此页中的“L”均为**用户附件原始行号**；Raw 为遵循 schema 增加 `type: raw` 一行，Raw 相应行号比附件大 1。广告和闲聊不作为核心商业/技术证据。

## 编译摘要

### 1. 浓缩

#### 结论一：Frontier Model 的产品开发必须同时“设定目标”与“发现训练后的意外能力”

- **原文依据（L80–L110）**：Doshi 承认研究者会追踪预训练运行、指标和干预时点，模型训练不是漫无目的；但“通过某项 eval”的能力提升如何转化为行为、交互气质、产品差异化仍难提前完全预测。产品负责人要在训练后亲自探索模型在哪些场景呈现异常突出的价值，并把发现接入真实用户体验与下一轮反馈。
- **原文依据（L122–L150）**：她介绍 Google 从硬件、模型到终端产品的全栈路径，以及用不同质量/成本 Pareto 点满足不同用户；在 frontier 能力和应用广度之间并行竞争。这是 Google 负责人的战略描述，不是经独立测量的用户收益或领先地位证明。“14 个十亿用户产品”的口述本人也表示待确认，不作为已验证事实。
- **编译判断（综合）**：`目标/假说 → 训练与评测观察 → 实际探索 → 找到新的 affordance → 产品原型 → 用户反馈 → 更新能力规格`。不能以“模型能力不可预测”否定可观测实验，也不能以单一 benchmark 胜利替代产品验证。

#### 结论二：模型本身有 UX，模型行为规格要变成可以校准的评估器

- **原文依据（L236–L272）**：大众搜索、视频创作与 IDE/CLI 专业用户需要不同的交互形态；Doshi 认为模型“如何问回问题、是否透明、怎么交流、行为与 persona”也是产品体验。她描述 PM 与 research 协作的链路：`用户反馈 → 期望模型行为 spec → rubric → 训练数据 → reward modeling`。这不等于所有模型行为都仅由 reward model 决定。
- **原文依据（L402–L410）**：模型质量、Judge 质量、部署时的 guard/filter、服务端实现都会影响用户实际体验；音频还受声音自然度、语调和抑扬变化影响。只测裸模型返回的文字，可能遗漏产品层失效。
- **编译判断（综合）**：独立保存 `model_quality`、`behavior_spec`、`end_to_end_user_experience`、`business_outcome`，明确谁拥有 rubric 及其更新权限；让产品负责人直接审查样本和长轨迹，而不是把 UI/UX 只理解为前端框架。

#### 结论三：Evals 与 Vibes 并不矛盾；从 5–20 条真正关心的任务建立质量直觉

- **原文依据（L312–L366）**：Doshi 招聘倾向于每天实际使用模型、有独立判断、能看数据与长轨迹、能亲手做 eval、能够迅速调整路线图的 PM。她建议先挑 **5 个 prompt** 做小规模自评，再积累到能区分模型 A/B 的 **20 个 prompt**，以熟悉且切身相关的场景开始。对长程、多轮行为而言，“怎样才算好”本身就是产品研究。
- **原文依据（L380–L410）**：她举出 Fitzpatrick 六档肤色尺度与目标场景失配的经历：原尺度为不同的医疗目的而设计，并不能充分表示全球肤色分布。团队采纳 Monk 十档肤色表征并修改产品/模型评价方式。这里的因果机制是**指标是否测量正确对象**，不是“从六档变成十档就自动公平”；访谈未给出可复核的公平性改善幅度。
- **编译判断（综合）**：`可观察用户任务 → 专家/用户示例 → 失败与反例 → rubric → 人类校准 → 真正生产栈的回放/运行`。Vibe 适合发现评测没有提出的新问题；Judge/benchmark 适合稳定比较，但也会错；少量探索样本不等于风险发布门禁或统计稳健性。

#### 结论四：60/20/20 是能力演进下的产品期权组合，不是固定投资指令

- **原文依据（L466–L512）**：Doshi 提出一个可调的分层启发式：大约 **60% 是今天即可工作的体验**，**20% 尚不完美但接近可用**，**20% 只有初步潜力、希望随着模型进步实现“魔法”体验**。她明确说比例可变，并坦承即使是 frontier model 的 PM，也不能精确预测三个月后的能力。
- **原文依据（L510–L540）**：模型升级可能让针对旧弱点修筑的特定 prompt、skill 或 wrapper 限制新模型发挥。她建议**持续重测旧 Harness**；其定义包含 system instructions、tools、skills、context 等模型运行环境。
- **编译判断（综合）**：为路线图建立 `works_now / capability_near_ready / speculative_option` 三个类别，并分别记录业务价值、成功判据、回退条件、观察窗口和模型变化带来的门槛变化。
- **边界**：60/20/20 不是统计估计、预算配比、组织强制 KPI、交付承诺或安全场景可允许的失败比例。重测并剥离过时的性能脚手架，**不等于取消最小权限、可靠状态机、审计、授权和独立测试 Oracle**。

#### 结论五：AI 降低“做出来”的成本后，PM 的价值更多是判断、评测、协调与对结果负责

- **原文依据（L286–L324）**：Doshi 认可 PM 的 `taste`、识别有价值信号、决定什么值得做和跨团队形成共识更重要；她更看重动手使用模型、独立判断、阅读数据、能构建评测与适应频繁变化的能力。她的立场有职业角色利益相关性，不能当作完整就业市场的因果分析。
- **原文依据（L546–L620）**：她谈到让技术 Skill 变成团队共享资产、组织模型实验/trace 阅读工作坊及把重复事务自动化；提到的两天 workshop 是拟实施计划，而非已达到的效率结果。
- **原文依据（L704–L742）**：AI 可帮助抽取 dashboard、用户反馈、社交讨论，生成状态报告；产品负责人应产生差异化 insight 和决策，而非堆积 AI 文档。PM 应在传统 PRD 之外亲手拿出 prototype、evaluation 或数据分析来推动团队对齐。
- **局限（L650–L700）**：Doshi 直接承认团队工作负荷很高，关于 burnout 和可持续安排尚在探索，不能把“共享 Skills”外推成已经降低过劳或完成组织转型。

### 2. 质疑、证据与适用边界

1. **自述的证据等级**：Google 模型研发/产品负责人访谈能说明内部策略、工作方法与判断，但不能独立证明模型优劣、PM 产出增长或安全风险降低。`evidence_level: medium` 表示单一高质量访谈加明确限定。
2. **“训练有魔法”是比喻**：模型有训练时控制和指标；不可预测的是具体能力形态和对用户的下游影响。PM 的 vibe 是探索方法，不是可以替代对照测试的 oracle。
3. **生产级安全评测不是 20 个 prompt**：极端失败、跨语言/人群公平性、隐私、临床或不可逆操作必须有更多覆盖、多次运行、专业人员批准的 rubric、部署环境约束和真实回执。
4. **评价尺度的目标偏差**：Fitzpatrick/Monk 案例说明先对齐适用对象，再决定分箱/指标；引用结果若要进入高风险业务需查独立研究、受试人群和测量方法。
5. **Chain-of-thought monitoring 的自述（L162–L200）**：Doshi 谈到用监控判断行为与意图是否偏离并作干预，及与 Wiz 开展网络防御。没有提供可见推理与真实内部过程一致性的证据、误报漏报或独立监测效果，不能将监视文本等同于完整可解释的安全认证。
6. **Flash team 类比（L422–L446）**：受访者把自己与 Michael Bernstein 合作研究的人类众包临时团队，与专业 Agent 协作类比；主持人关于其它 Agent 事件的描述不能被当成这项类比已被实证验证。
7. **模型产品现况有时效**：Gemini 4 Argon、Nano Banana、Omni、音频等具体产品名称是采访发生时的叙述；版本、接口及能力需按需另查，不能自动转为最新规格。
8. **组织投入与过劳并存**：自动化可减少重复劳动，但高产也可能创造更多需要审核的文档和上下文切换。区分有效洞察、阅读负担、完成质量与工作量，不用生成速度推导心理/组织收益。

### 3. 对标与可迁移原则

| 原文机制 | 已有知识 | 新增可检验思路 |
|---|---|---|
| 模型训练后发现新强项与 UX | [[PM-in-AI-Era]]、[[Taste]] | 从“写需求”延伸到“提出任务、亲测能力、发现新行为并形成反馈” |
| 5–20 个任务、Monk 案例、真实 serving | [[Evaluator-Miscalibration]]、[[Evaluation-Integrity]] | 问题/评价器/实际产品三者对齐；先发现，再形成受保护的评测 |
| 随模型升级复测 Harness | [[Agent-Harness]]、[[Agentic-Engineering-Patterns]] | 比较有/无旧 Skill/上下文脚手架的行为差异，保留确定性治理不变量 |
| 60/20/20 技术期权 | [[PM-in-AI-Era]] | 管理当前可交付与未来模型能力机会，明确每档验证和撤退条件 |
| 团队技能共享与洞察所有权 | [[Organization-as-Agent-Harness]]、[[AI-Native-Engineering-Org]] | 组织可用共享 Skill 降低重复劳动，但成果由真实业务结果而非文档篇数衡量 |

#### 对 LLM WiKi、ChatGPT Worker、n8n 的具体启示（综合建议，非受访者项目）

- **保留可替换的智能层和不可绕过的控制层**：对不同模型/版本基于固定质量样本对比旧 Prompt/Skill/Context 的边际作用；允许移除妨碍能力的过时适配，但不撤销来源证据、Claim ownership、状态持久化、工具权限、发布 ACK 及独立审计。
- **以真实缺陷构建小规模起步的 eval 库**：例如来源 URL 未真正读取、知识推断越界、Raw/summary 证据链断裂、双重消费队列和终态回执错误。以 5–20 个案例**起步**，逐步加入困难样本、随机扰动和专家对照。
- **产品路线按可验证的“现已能做—尚未稳定—未来能力”分层**；每类的完成标准与投入预算另按本身业务风险决定，不机械执行 60/20/20。
- **降低信息噪声**：将数据抽取、状态汇总交给 AI，而洞察必须给出来源、为什么值得关注、与现有知识不同在哪里、谁对采纳后果负责。不要用自动产文量代替知识效用。

## 重要判断（Claim / Evidence / Boundary）

- **判断（综合）**：模型与应用实现成本下降后，高价值产品判断来自能否发现具有产品意义的真实能力、选择正确的测量指标、提出切实的产品试验，并对用户结果负责。
  - **证据**：原附件 L80–L110、L258–L340、L704–L742。
  - **边界**：人物采访的一手观点，不构成产品负责人就业价值的因果统计证明。
- **判断（综合）**：Harness 是模型外的运行时能力适配层，可以因模型变化而改进；治理不变量必须超越模型能力变化继续有效。
  - **证据**：原附件 L466–L540，并与 [[Agent-Harness]] 的已编译资料交叉参照。
  - **边界**：原文建议“持续重测”，不等于主动取消全部 Skills、状态/安全约束或独立验证。

## 关联概念

- [[PM-in-AI-Era]]
- [[Evaluator-Miscalibration]]
- [[Agent-Harness]]
- [[Agentic-Engineering-Patterns]]
- [[Organization-as-Agent-Harness]]
- [[Evaluation-Integrity]]
