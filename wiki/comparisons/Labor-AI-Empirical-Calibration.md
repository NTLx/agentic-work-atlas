---
type: comparison
title: Labor AI Empirical Calibration
created: 2026-09-19
updated: 2026-09-19
evidence_level: high
claim_type: mixed
tags:
  - labor-economics
  - ai-adoption
  - methodology
source_raw:
  - "[[20260901-nyfed-businesses-ai-transform-work-not-cut-jobs]]"
  - "[[20260324-atlanta-fed-firm-data-on-ai]]"
  - "[[20260624-prompting-change-denmark-ai-adoption]]"
  - "[[20260305-anthropic-labor-market-impacts-ai]]"
  - "[[20260812-stanford-canaries-coal-mine-ai-employment]]"
  - "[[20260414-nyfed-genai-training-access]]"
  - "[[20260201-how-ai-impacts-skill-formation]]"
  - "[[20260630-ramp-ai-jobs-firm-spending-workforce]]"
  - "[[20260901-dallasfed-ai-automation-job-postings]]"
  - "[[20260428-census-youre-not-hired-ai-early-career]]"
---

# Labor AI Empirical Calibration（AI 劳动经济学实证校准）

> [!summary] 核心用途
> 本比较页不回答“AI 到底增加还是减少就业”这一单一问题，而是固定不同一手证据到底测量什么。企业采用、职业暴露、就业存量、招聘流量、职位发布、培训可得性和无 AI 独立能力属于不同 estimand，只有先保留各自单位、分母和时间窗，才可能进一步做联合判断。

## 一张表看清当前 10 个来源

| 来源 | 观测单位 | 状态 | AI 变量 | 劳动/能力结果 | 关键数值 | 不能解释成 |
|---|---|---|---|---|---|---|
| [[20260901-nyfed-businesses-ai-transform-work-not-cut-jobs]] | 区域企业 | 行动自报 + 回溯归因 | 企业 AI 使用 | 少招/多招/裁员/再培训行动占比 | 服务业 15%/13%/4%/34% | 净 headcount 或培训完成率 |
| [[20260324-atlanta-fed-firm-data-on-ai]] | 四国企业高管 | 回溯归因 + 预期 | 企业 AI 采用 | 过去/未来三年就业影响 | 约 0.00% retrospective；-0.68% expected | 行政净就业变化 |
| [[20260624-prompting-change-denmark-ai-adoption]] | 企业—员工匹配行政记录 | 行政结果 + 非随机 event study | 企业采用调查 | FTE、招聘、离职、年龄异质性 | adopter FTE 相对预趋势约 -8% | 裁员 8% 或青年失业率 |
| [[20260305-anthropic-labor-market-impacts-ai]] | 任务→职业→CPS 人月 | 暴露估计 + 调查流量 | Claude observed-use occupation exposure | 22–25 岁 new-work flow | 高暴露组相对 2022 约 -14%，边缘显著 | 采用 AI 企业少招 14% |
| [[20260812-stanford-canaries-coal-mine-ai-employment]] | ADP worker–firm payroll match | 行政存量/流量 | 职业 exposure proxy | employment path、hire、separation | 22–25 岁高暴露 employment path 约 -19% | AI 导致 19% 裁员 |
| [[20260414-nyfed-genai-training-access]] | 就业者个人 | 使用/培训自报 + stated preference | 工作中 AI 使用 | 培训可得性 | 39% 使用 AI；15.9% 有培训 | 培训完成率或技能提升 |
| [[20260201-how-ai-impacts-skill-formation]] | 实验受试者 | 随机实验 | AI assistance | 无 AI 独立理解测验 | -4.15 分；d=0.738；p=0.010 | 职业长期能力再生产率 |
| [[20260630-ramp-ai-jobs-firm-spending-workforce]] | 美国企业 | 观察性 linked data | observed firm AI spending | total / entry-level headcount stock | high-intensity adopters 约 +10% employment；+12% entry-level headcount | entry-level hires、晋升、培训或因果效应 |
| [[20260901-dallasfed-ai-automation-job-postings]] | occupation-industry / firm postings | 劳动力需求观测 | automatable-task exposure | online job postings | 10pp exposure 差异：约 -5%（2023末）、-8%（2025Q1）；existing firms 到 2026初约 -8–9% | 实际 hire、employment 或 layoff |
| [[20260428-census-youre-not-hired-ai-early-career]] | industry-state × employer-employee admin | 行政 hires/employment | industry-state AI exposure | 22–24 岁 hires / employment | most-exposed quintile 10 个季度后 employment 约 -12%，主要由 hires 驱动 | observed firm adoption、培训或技能结果 |

## 不能把“方向相反”当作相互证伪

这些来源出现看似冲突的方向，并不意味着其中一组一定错。

例如：

- 企业层总体 headcount 可能扩大；
- 某些高暴露职业的职位或青年流入可能下降；
- 企业可能同时增加再培训；
- 个人在特定学习任务中又可能出现无 AI 独立能力下降。

这些可以同时成立，因为它们分别处于不同层：

~~~text
firm stock / action
    ×
occupation exposure
    ×
entry / early-career flow
    ×
training availability
    ×
independent capability
~~~

因此稳定规则是：

> **跨来源先对齐 estimand，再比较方向；没有共同单位、共同风险集和共同时间窗时，不计算“综合净效应”。**

## adoption、exposure、use 必须分列

三个最容易混淆的变量：

- **firm adoption / spending**：企业是否部署/使用 AI，以及可观察到的采用强度；
- **occupation exposure**：一个职业的任务是否技术上/观察上暴露给 AI；
- **worker/tool use**：具体员工是否实际使用 AI。

它们不是同一个处理变量。

[[20260624-prompting-change-denmark-ai-adoption]] 接近 firm adoption survey，[[20260630-ramp-ai-jobs-firm-spending-workforce]] 使用 observed AI spending 作为 adoption-intensity proxy；[[20260305-anthropic-labor-market-impacts-ai]]、[[20260812-stanford-canaries-coal-mine-ai-employment]]、[[20260901-dallasfed-ai-automation-job-postings]] 与 [[20260428-census-youre-not-hired-ai-early-career]] 主要使用 occupation / industry exposure；[[20260414-nyfed-genai-training-access]] 则是 worker-reported use。

因此：

~~~text
high exposure
  ≠
employer adopted AI
  ≠
worker actually used AI
~~~

## stock、flow、FTE、job posting 不能互换

- **headcount stock**：某一时点在岗人数；
- **hire / separation flow**：一段时间内进入或离开的流量；
- **FTE**：工时折算，不等于人数；
- **job posting**：劳动力需求信号，不等于实际招聘；
- **new-work rate**：个人状态转换，不等于企业 hire count。

这意味着：

- 丹麦 FTE 下降不能直接翻译成裁员人数；
- Stanford 的 22–25 岁 employment-path gap 不能翻译成 layoff rate；
- Anthropic/CPS 的 new-work rate 不能翻译成企业招聘率；
- Dallas 的 online postings 不能翻译成实际 hires；
- Ramp 的 entry-level headcount stock 不能翻译成 entry-level hiring flow；
- Census 的 22–24 岁 administrative hires 不能反推企业真实 AI spending。

## 青年、初级、首次就业不是同一群体

当前来源中：

- 丹麦材料使用 <30；
- Anthropic/CPS 与 Stanford/ADP 使用 22–25；
- Census 使用 22–24；
- Ramp 使用其 workforce 数据中的 entry-level 分类；
- Skill Formation 实验只是“不熟 Trio”的程序员；
- none of these automatically equals “entry-level job”。

因此必须分别记录：

~~~text
age
graduation_year
occupation_experience
firm_tenure
job_level
first_job_flag
~~~

不能用年龄自动补职级，也不能用新库初学者替代青年劳动者。

## 培训链必须拆成多个阶段

当前来源只覆盖不同环节：

~~~text
training offered
  → participation
  → completion
  → mentored / independent practice
  → unaided capability
  → delayed retention / transfer
  → promotion / qualification
~~~

- [[20260901-nyfed-businesses-ai-transform-work-not-cut-jobs]]：企业说“做了再培训”；
- [[20260414-nyfed-genai-training-access]]：员工说“雇主提供培训”；
- [[20260201-how-ai-impacts-skill-formation]]：随机实验直接测撤去 AI 后的短期能力。

三者不能串成同一批人的训练结果。

## 最小 evidence long-table schema

后续所有劳动经济学来源至少保留：

| 字段组 | 最小字段 |
|---|---|
| 来源版本 | source_id / publication_date / version / observation_period |
| 样本 | country / population / observation_unit / sample_n / weight |
| AI 状态 | adoption_definition / exposure_type / use_definition / vintage |
| 劳动结果 | headcount / FTE / hire / separation / job-posting / new-work flow |
| 职业阶段 | age / graduation_year / tenure / level / first_job |
| 培训 | offered / participated / completed / hours / mentored practice |
| 能力 | unaided_score / delayed_score / transfer_score / qualification |
| 估计状态 | administrative / reported / retrospective-attribution / expected / experiment |
| 审计边界 | denominator / comparison_group / uncertainty / missing_fields / linkage_access |

## 当前稳定判断

前两批共 10 个来源已足以支持四个稳定判断：

1. **“企业总体用工影响有限”不能证伪青年/高暴露职业入口收缩。**
2. **“青年入口收缩”不能直接证明专业能力再生已经恶化。**
3. **“提供培训”不能替代“完成培训并在无 AI 条件下形成独立能力”。**
4. **企业层 entry-level stock 增长与高暴露职业/地区的 early-career hiring 收缩可以同时出现。** Ramp 的 +12% entry-level headcount 与 Census/Dallas 的入口需求下降不处于同一 estimand，不能相减或互相否定。

真正能闭合“AI 采用 → 劳动力结构 → 专业能力再生”的证据，需要同一企业—职业—个人—时期链上同时看到：

~~~text
firm adoption
  → occupation / task allocation
  → hire / separation / promotion
  → training participation / completion
  → unaided capability
  → delayed retention / qualification
~~~

当前公开材料尚未形成这条共同链。Ramp 已把 firm AI spending 与 workforce stock 连起来；Census 已把 exposure 与 early-career administrative hires 连起来；Dallas 已把 exposure 与 firm posting composition 连起来，但三者仍没有共同 firm × occupation × person key。

## 与稳定 Topic 的关系

- [[Labor-Market-Impact]]：承载就业/招聘/流量的事实边界。
- [[Skill-Atrophy-and-Knowledge-Debt]]：承载训练与独立能力再生问题。
- [[AI-Labor-Bottleneck-Shift]]：承载组织/任务瓶颈迁移，不承担单一宏观就业结论。
