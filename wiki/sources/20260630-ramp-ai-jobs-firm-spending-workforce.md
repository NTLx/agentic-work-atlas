---
type: source-summary
title: "A New Look at AI's Impact on Jobs: Firm-Level AI Spending and Workforce Adjustment"
source_raw:
  - "[[20260630-ramp-ai-jobs-firm-spending-workforce]]"
canonical_url: "https://ssrn.com/abstract=7024799"
raw_state: full
source_locator:
  - "Ramp AI spending × Revelio workforce records"
  - "21,559 U.S. firms"
  - "high-intensity adopters: roughly +10% employment / +12% entry-level headcount"
created: 2026-09-19
updated: 2026-11-28
tags:
  - source-summary
  - labor-economics
  - ai-adoption
evidence_level: high
claim_type: mixed
---

# Ramp × Revelio: firm AI spending and workforce adjustment

## 编译摘要

### 测量身份

- **单位**：企业。
- **处理变量**：observed AI spending per employee after adoption。
- **结果**：workforce stock / role headcount。
- **样本**：21,559 家美国企业。

### 核心证据

- [原论文](https://ramp.com/data/ai-jobs-impact/paper) §§3、5–6 / Table3（2026-06-30）：21,559家企业，2021-01至2026-02月度匹配；采用定义为连续三月每月可见AI支出≥100美元的首月，按采用后前三月人均月支出分组，上1/3为High（平均33.67美元）、下2/3为Low（2.78美元）。
- 同最终强度组较晚采用者尚未采用时作为对照；Callaway–Sant’Anna、行业固定效应。0–24月**平均ATT**：总headcount log系数0.097（SE .022，作者换算+10.2%），entry-level log(1+人数)系数.113（SE .030，作者近似+12%）。不是第24个月末增幅、绝对招聘数或全部企业平均效应。
- Low总人数−.006（SE .016）、初级−.017（SE .018），未检出显著差异，不等于零效应。
- 增长分布跨工程、销售、行政、客服等角色，而非只集中于单一职能。

### 选择与识别边界

- adopters 本来就更大、更技术密集、更快增长；首选对照改善预趋势但High总人数/初级分别3/11、2/11个采用前事件期点wise 95% CI排除0，条件平行趋势仍不能视为已证实；强度由处理后支出定义，可能反映增长计划或其他同期决策。
- AI spending 是 Ramp 平台内可见的采用 proxy，不是企业全部 AI use。
- 研究是 observational linkage，不是随机实验。
- Revelio由公开职业档案构造并加权，非行政工资单；entry-level为七级seniority字段的1–2级，不是年龄、首份工作、hire流量、晋升或能力。log(1+y)变换在小计数时也不是普通百分比。

### 对标

- 对 [[Labor-AI-Empirical-Calibration]]：提供特定样本中high-intensity adoption与entry-level stock相对增长的观察性证据；不能推出加大支出即可增加就业或净创造就业。
- 对 CR-005：反驳“高采用必然立即消灭入门岗位”的强版本，但不能证明能力再生被内部化。

## 关联概念

- [[Labor-Market-Impact]]
- [[Labor-AI-Empirical-Calibration]]
- [[Skill-Atrophy-and-Knowledge-Debt]]
