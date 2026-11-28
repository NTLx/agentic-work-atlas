---
type: source-summary
title: "Designing AI Evals: Clarity Now and Visualization Next"
source_raw:
  - "[[20260819-google-ai-evals-inspect-skill]]"
created: 2026-08-19
updated: 2026-11-28
tags:
  - source-summary
  - evals
  - verification
  - agent-skills
evidence_level: medium
claim_type: mixed
---

# Designing AI Evals: Clarity Now and Visualization Next

## 编译摘要（2026-11-28 原文与实现复核）

Google DevRel 的教学实验比较两个 solver 模型、两个 skill 及对应 baseline；使用 Inspect AI、Docker sandbox、独立低成本 grader、逐项判据及日志诊断。它展示一种可复现实验设计，并不证明特定 grader、模型或分类在所有任务中有效。

### 1. Solver / grader 职责与评分

- 原文使用 Gemini 3.5-flash-lite、3.6-flash 作为 solver，3.1-flash-lite 作 grader；2 epochs、300s timeout、max-tasks=4、web_access=false。配置、题目与 system prompt 独立于脚本；固定 Gemini CLI 版本 0.51.0 是该实验的历史配置。
- 分开选择 solver 与 grader 可降低评分配额竞争，便于控制实验变量；不同模型不等于错误独立。更昂贵的 grader 可能更有效，但必须用独立标注和重复判决校准，不能由模型价格推断置信区间宽度。
- 每个 fact 用二元评分，保留逐项 breakdown。程序化 reduction 并不能消除 grader 的语义误判，也不能自动保证所有判据有效。
- **公式勘误**：原博客称 5/6 → 0.65。本库曾简写为 mean²，遗漏向下量化。原文链接的 [README](https://github.com/GoogleCloudPlatform/devrel-demos/blob/main/agents/inspect-agent-skills-eval/README.md) §3、[skills-eval.py](https://github.com/GoogleCloudPlatform/devrel-demos/blob/main/agents/inspect-agent-skills-eval/skills-eval.py) 的 custom_reducer 及 [questions.json](https://github.com/GoogleCloudPlatform/devrel-demos/blob/main/agents/inspect-agent-skills-eval/questions.json) 的 scoring_scale=20.0 确认：score = floor(20 × mean²) / 20。5/6 的平方约 0.6944，向下量化为 0.65，原博客正确。此函数是作者选择的惩罚规则，不是校准或抗 Goodhart 的数学保证；不同重要性判据及关键禁止行为不能仅靠平均分处理。

### 2. Skill 与 baseline 的五种示例诊断

原 README 的分类是经验例示，不是完备互斥的二维分类；保留原义而不把它当自动发布门禁。

| 原文分类 | 观察 | 建议诊断 |
|---|---|---|
| High-Efficiency Capability Lift（best） | 准确度提高，token 和延迟下降 | 扩大代表性测试，检查过拟合 |
| High-Efficiency Capability Lift（good） | 准确度明显提高，token 和延迟适度增加 | 比较增量价值和成本 |
| Cost-Bloated Pyric Victory | 准确度小幅提高，token 和延迟大增 | 检查循环与失败调用 |
| Baseline Parity / Superfluous Skill | 准确度、延迟近似相同 | 检查 skill 是否加载或知识重复 |
| Context Overload & Skill Regression | 准确度未提高，token 和延迟大增 | 检查指令冲突、上下文和逐项判决 |

旧独立页将第二类误写为成本不变、第三类误写为仅降低成本、第四类误写为成本膨胀；以上按官方 README 修复。准确度下降但成本降低等其他组合也可能发生，需按真实质量门和成本/延迟目标裁决。

### 3. 结果与局限

- 作者观察同模型加入 skill 时得分改善或持平，duration 均增加，但某组 token 用量减少；duration 不等于货币成本。跨模型的 gcloud 得分下降是不同对照轴，不是同模型 skill 导致退化的证据。
- 题目、重复次数有限；作者明确要求更多样本和 epochs，未证明统计显著的普遍效果。
- 分开报告 skill 提供条件的总体效果和激活后的条件性诊断。未激活是产品真实失败模式之一，不应只保留激活或成功完成样本来美化总体成绩。日志用于辨别 sandbox 故障、重复调用、激活及逐事实误判。
- 原代码通过 prompt 表达 web_access=false，不能由此推断网络层实际不可达；应验证运行环境。
- 更强 grader、binary rubric 和量化分数分别属于成本/误差、判据设计、聚合策略三个维度；参见 [[LLM-as-a-Judge]]、[[Rubric-Based-Evaluation]]、[[Evaluator-Miscalibration]]。

## 关联概念

- [[Skills-as-Products]] — 按真实质量、成本和激活结果评估技能。
- [[LLM-as-a-Judge]]、[[Rubric-Based-Evaluation]] — solver/grader 分工与逐项判据。
- [[Evaluator-Miscalibration]]、[[Goodharts-Law]] — 聚合指标不等于实际质量。
- [[Evals-as-PRD]]、[[Agent-Verification]] — 评测与实际验收。
