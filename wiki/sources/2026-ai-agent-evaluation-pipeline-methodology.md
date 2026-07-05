---
type: source-summary
title: "Building an AI Agent Evaluation Pipeline: 2026 Methodology"
source_raw:
  - "[[2026-ai-agent-evaluation-pipeline-methodology]]"
created: 2026-07-05
updated: 2026-07-05
tags:
  - source-summary
  - agentic-engineering
  - verification
  - AI-Agent
evidence_level: medium
claim_type: extracted
---

# Building an AI Agent Evaluation Pipeline: 2026 Methodology

## 编译摘要

### 1. 浓缩
- **核心结论1**: 生产级 Agent 评测管线需要七步架构：可靠性数学（pass^k）→ 共享词汇 → Golden Dataset → 双类 Grader（deterministic + LLM-as-judge）→ LLM Judge 校准 → CI 门禁 → 生产反馈循环
  - 关键证据: Digital Applied (2026) 的实操方法论
- **核心结论2**: pass^k（连续 k 次全部通过才视为成功）是衡量 Agent 可靠性的关键指标——demo 中的单次成功不等于生产中的可靠性
  - 关键证据: 全输入分布下的表现 vs 单次 demo 成功的差异
- **核心结论3**: LLM-as-Judge 必须经人类 gold set 校准后才可信任——未校准的 judge 分数不可用于 CI 门禁
  - 关键证据: 对抗人类评审校准的具体要求

### 2. 质疑
- **关于 pass^k 的质疑**: k 值的选择没有通用标准——对低风险任务 k=1 可能足够，对高风险任务可能需要 k>10。文章未讨论 k 的选择策略
- **关于 LLM Judge 校准的质疑**: 人类 gold set 本身有偏见和局限性，用有偏的 gold set 校准 judge 可能导致系统性偏差
- **关于 CI 门禁的质疑**: 评测分数门禁可能导致过度保守——Agent 在某些边缘 case 上失败但整体质量提升时被 CI 阻断

### 3. 对标
- **跨域关联1**: 七步架构与 [[Agent-Verification]] 中的"验证循环三层（规则/视觉/LLM-judge）"形成互补——这里提供的是工程化落地路径
- **跨域关联2**: 生产 traces → golden dataset 的反馈循环与 [[Validation-Pipeline]] 的"对抗审查 + e2e + 证据生成"理念一致

### 关联概念
- [[Agent-Verification]]
- [[LLM-as-a-Judge]]
- [[Validation-Pipeline]]
- [[Automated-Criteria]]
- [[Evaluation-Set]]