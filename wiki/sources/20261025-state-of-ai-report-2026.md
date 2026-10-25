---
type: source-summary
title: "State of AI Report 2026 - FINAL"
canonical_url: "https://www.stateof.ai/State-of-AI-Report-2026.pdf"
raw_state: index
original_raw_file: "20261025-state-of-ai-report-2026.pdf"
body_sha256: "93f9a0202726d90446ac4954339ba529e446a88de40e338aeb68db0a0298c739"
indexed_at: "2026-10-25T06:57:45+00:00"
created: 2026-10-25
updated: 2026-10-25
tags:
  - source-summary
  - agentic-engineering
  - ai-industry
evidence_level: medium
claim_type: mixed
---

# State of AI Report 2026 - FINAL

## 编译摘要

### 1. 浓缩
- **Harness 会显著改变同一模型的任务表现，跨模型/Agent 比较必须披露执行 harness 并控制变量**：报告引述实验称，同一模型更换 harness 在 SWE-Bench Mobile 上有 6 倍提升；另一个 3 模型 × 3 harness、100 个 SWE-bench Verified 任务的实验中，GLM-5.1 从 minimal harness 的 52.5% 到 full harness 的 65.5%，该实验中 harness 引起的表现方差是模型方差的 7.8 倍（PDF 第 8 页，印刷页/slide 7，“Same model, better harness = stronger agent”）。这些是报告转述的研究结果，不是 Air Street 自行实验。
- **AI 正进入研究工作的执行环节，但“活动量”不能直接等同于完整研究能力**：报告摘要称 Claude 在 Anthropic 被测模型研发工作中“led 26%”，并强调选择值得做的实验仍是下一前沿（PDF 第 4 页，印刷页/slide 3）；另处称 OpenAI 报告每个人类工作日对应 3.1 agent-workdays，并明确这是活动度量而非等价产出（PDF 第 42 页，印刷页/slide 41）。前者的原始口径依赖 Anthropic 的测量，后者是 OpenAI 自报指标。
- **报告用增长、供给约束与未兑现预测并列描绘产业状态，不能把趋势叙事当成确定预测**：例如它列出 OpenAI 与 Anthropic 合计约 1,050 亿美元年化收入运行率，同时在预测部分单列未来 12 个月的九项判断（PDF 第 83–84 页/印刷页 82–83；第 239 页/印刷页 238）。运行率是特定月份的年化截面，不是全年确认收入；报告将预测与已发生事项分开呈现。

### 2. 质疑
- **关于 harness 效应的质疑**：slide 7 借用了多个 benchmark/论文结果；任务集、模型版本、harness 实现和评测时间不同，单个 7.8 倍方差比不能普遍外推。报告本身提出比较时要披露并控制 harness，这也限制了对汇总数字的解释。
- **关于 AI 执行研究工作的质疑**：Anthropic 的“26%”和 OpenAI 的“3.1 agent-workdays”均来自公司披露，计数边界和质量校准未在报告摘要页完整展开；活动、辅助完成或执行环节不等于研究议程选择、可靠发现或可替代的人类工作量。
- **关于收入与产业规模的质疑**：slide 82 的 `40B 美元`（OpenAI，2026-08）与 `65B 美元`（Anthropic，2026-07）是公司 run rate/投资者信函口径；报告同时转述 OpenAI 对 Anthropic 收入口径的异议，以及 Financial Times 对 Anthropic 毛利率口径的说明。slide 83 还提醒广义 AI 收入估计因范围和日期不同而有 `150B` / `229B 美元`差异。不得把这些口径混成已审计收入、利润率或市场份额。
- **关于预测的质疑**：报告回顾 2025 年预测时给出 YES/NO/部分支持等结果（slide 237），并列出 2026 年九项前瞻（slide 238）；这是作者的判断框架与预测，不是事实。预测命中与否受定义、时间截面和可观察性影响。
- **关于来源可靠性与利益关系的质疑**：报告说明其内容由 Nathan Benaich/Air Street Capital 编制，并经 AI labs、创业公司、政策与学术界人士 peer review（PDF 第 3 页/印刷页 2）；作者另披露本人或基金投资/顾问关系覆盖被引用公司，投资组合列于 airstreet.com/portfolio（PDF 第 241 页/印刷页 240）。同行审阅提高可讨论性，但不消除投资激励、选择偏差或被投公司自报口径的限制。

### 3. 对标
- **跨域关联**：把 harness 当成实验中的控制变量，类似工程系统的干预变量与测量仪器；如果不报告工具链、流程和环境，产出差异就不能简单归因于模型本身。这一方法适用于 Agent benchmark、内部生产率评估和 agentic workflow rollout。
- **约束分析**：能力与商业结论分别受 benchmark 覆盖、任务定义、公司披露口径、运行率时间截面、外部算力/能源供给及作者投资关系约束。报告中的观点不等于独立审计结论。

### 证据定位与类型
- **报告作者归纳/判断**：slide 3 的年度摘要、slide 7 的“harness matters”叙事、slide 238 的 2026 预测；属综合叙事/预测，不作为独立观测事实。
- **公司披露**：Anthropic 的模型研发工作占比（slide 3）、OpenAI 的 agent-workdays（slide 41）、OpenAI / Anthropic 的运行率（slide 82）。这是被报告转述的当事方披露。
- **二手引用/外部研究**：slide 7 的 benchmark 结果；slide 82 对 Financial Times 的毛利率口径引用；slide 83 对 Exponential View 与 The Economist 行业规模估计的并列转述。需沿报告页脚引用回到原始研究或报道再做投资/决策用途。
- **时间边界**：封面日期 2026-10-08；正文主要分析此前 12 个月，收入数字明确截至 2026 年 7–8 月，2025 预测复盘与未来 12 个月预测各自有单独时间窗。
- **本报告核验结果**：未在此 PDF 中找到“AI 产品毛利率约 52%”或“推理成本占收入约 23%”这两个精确表述；同名旧年份/其他统计口径不能据此视为本版报告的佐证。

### 关联概念
- [[Agent-Harness]]
- [[Agent-Verification]]
- [[Agentic-Engineering]]
