---
type: entity
title: Labor-Market-Impact
aliases:
  - 劳动力市场影响
definition: "AI 对就业、招聘、工资、工作结构和技能形成的影响；分析时必须区分企业采用、职业暴露、个人实际使用，以及 headcount/FTE/招聘流量/培训/独立能力等不同 estimand。"
created: 2026-06-30
updated: 2026-09-19
tags:
  - ai-labor
related_entities:
  - "[[AI-Perception-Survey]]"
  - "[[AI-Labor-Bottleneck-Shift]]"
  - "[[Task-Crossover]]"
  - "[[Labor-AI-Empirical-Calibration]]"
source_raw:
  - "[[20260626-anthropic-economic-index-june-2026-report]]"
  - "[[20260702-ai-layoffs-reversed]]"
  - "[[the-ai-jobs-transition-framework-for-the-eu]]"
  - "[[How to 10x Your Value in the AI Era — Kunal Shah]]"
  - "[[20260727-openai-work-at-the-frontier.pdf]]"
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

# Labor-Market-Impact

## 定义

AI 技术对就业、工资、工作结构和劳动力市场动态的影响。Anthropic Economic Index 通过使用数据和调查研究这一影响。

## 关键数据点

- **观察到的暴露度**：基于 Claude 使用数据，某些职业的任务已有较高比例被 AI 执行。
- **报告的暴露度**：用户报告 AI 当前能完成的工作比例高于观察到的暴露度。
- **预期暴露度**：超过35%的受访者预期 AI 将在12个月内完成其大部分工作。
- **就业担忧**：10%的受访者认为自己很可能失业，38%将其归因于 AI。
- **性别差异**：女性更少使用 Claude Code 和自动化，更多迭代使用。

## 影响机制

- **任务自动化**：AI 自动化特定任务，而非整个工作。
- **任务跨界**：OpenAI Work at the Frontier（2026-07）测量到 [[Task-Crossover|任务跨界]]——职业专属 AI 使用中 43.5% 涉及其他职业的历史任务。这是任务再分配的**最上游信号**：先于就业数、工资、岗位发布等滞后指标，在职位描述修改之前就可观测。与 Anthropic Economic Index 的"暴露度"测量互补——一个测机器在执行什么，一个测人在用机器跨界做什么。
- **技能价值变化**：57%的受访者认为 AI 提高了其技能的市场价值。
- **工作重新定义**：AI 可能增强而非取代人类工作。

## 2026 跨层实证校准

第一批 7 个一手来源已编译进 [[Labor-AI-Empirical-Calibration]]。它们显示，“AI 对劳动力市场的影响”至少包含不同的测量层，不能用一个方向性的 headline 统一：

~~~text
firm adoption / firm action
        ×
occupation exposure
        ×
employment stock / hire / separation / FTE
        ×
training availability
        ×
unaided capability
~~~

### 企业层与职业层可以同时出现不同方向

[[20260901-nyfed-businesses-ai-transform-work-not-cut-jobs]] 显示，AI 使用企业可以同时报告少招、多招、裁员与再培训；这些是企业行动占比，不是净人数。

[[20260324-atlanta-fed-firm-data-on-ai]] 的四国企业调查又把过去三年的回溯归因与未来三年的预期分开：过去就业影响 pooled 约 0.00%，未来预期约 -0.68%。这里的 0.00% 仍不是行政工资单意义上的“就业没有变化”。

与此同时，[[20260305-anthropic-labor-market-impacts-ai]] 与 [[20260812-stanford-canaries-coal-mine-ai-employment]] 在职业/早期职业层看到高暴露组的青年 new-work / employment path 相对走弱。

这三类结果不直接互相证伪，因为 estimand 不同：

- 企业总体 stock / action；
- 职业层 exposure；
- 22–25 岁流量或存量路径。

一个企业完全可能扩大总 headcount，同时减少某些高暴露职业或青年入口，并把新增需求转向其他职能或资历层。

### adoption、exposure、actual use 不能互换

- [[20260624-prompting-change-denmark-ai-adoption]] 接近 firm adoption + administrative employment outcomes；
- [[20260305-anthropic-labor-market-impacts-ai]] / [[20260812-stanford-canaries-coal-mine-ai-employment]] 主要是 occupation exposure；
- [[20260414-nyfed-genai-training-access]] 是 worker-reported use / training access。

因此：

~~~text
high occupational exposure
      ≠
firm adopted AI
      ≠
worker actually used AI
~~~

任何跨来源比较都必须保留处理变量的类型和 vintage。

### stock、flow、FTE 不能互换

丹麦 [[20260624-prompting-change-denmark-ai-adoption]] 的结果包括 FTE、hiring、separation；Stanford/ADP 又把 employment stock、hire、separation 分开。它们共同支持一个更严格的读法：

> **“就业减少”必须先问减少的是人数、FTE、招聘流入、岗位发布还是新工作转换率。**

没有同一风险集和同一单位时，不计算综合净效应。

### 当前最小结论

- 企业总体用工影响有限，不能证伪特定职业/年龄组入口压力；
- 青年入口压力，不能直接证明长期技能再生已经恶化；
- 培训供给，不能替代培训完成和无 AI 独立能力结果。

详细字段契约见 [[Labor-AI-Empirical-Calibration]]。

第二批进一步增加了 firm-level spending、posting demand 与 administrative early-career hires 三种连接。[[20260630-ramp-ai-jobs-firm-spending-workforce]] 中 high-intensity adopters 的 total employment 与 entry-level headcount 都上升；[[20260901-dallasfed-ai-automation-job-postings]] 与 [[20260428-census-youre-not-hired-ai-early-career]] 则在高 exposure 的 occupation / industry-state 层看到 posting 与 22–24 岁 hires/employment 走弱。这个组合强化的不是“AI 同时创造和消灭工作”的泛结论，而是一个更具体的测量边界：**firm stock expansion 与 exposed-entry contraction 可以并存，只有共同 firm × occupation × person key 才能判断它们是否发生在同一组织链上。**

## 前提与局限性

- 数据仅基于 Claude 用户，可能不代表整个劳动力市场。
- 调查样本偏向知识工作者，可能不具代表性。
- AI 影响的长期趋势尚不明确。

## 关联概念

- [[AI-Perception-Survey]]：提供主观证据。
- [[AI-Labor-Bottleneck-Shift]]：劳动力瓶颈从生产迁移到判断和验证。
- [[AI-Autonomy]]：自主性可能影响劳动力市场结构。
- [[Task-Crossover]]：任务再分配的最上游测量，先于滞后指标。