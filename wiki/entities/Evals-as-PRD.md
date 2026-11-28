---
type: entity
title: Evals-as-PRD
aliases:
  - Evals are the new PRDs
  - Evals as PRD
  - 评测即需求文档
definition: "将已明确且可评价的产品行为编译为可运行的评测契约，与意图、产品愿景、风险和跨职能对齐文档互补；评测结果支持迭代但不保证全部需求覆盖"
created: 2026-07-30
updated: 2026-11-28
tags:
  - product-management
  - ai-evaluation
  - agentic-engineering
evidence_level: medium
claim_type: mixed
related_entities:
  - "[[Evaluation-Set]]"
  - "[[Model-Introspection]]"
  - "[[Transparent-Tool-Handoff]]"
  - "[[Mechanical-Sympathy-for-LLMs]]"
  - "[[Anthropic]]"
topics:
  - "[[AI-Era-Career-Skills]]"
source_raw:
  - "[[20260730-lenny-anthropic-first-technical-pm-dianne-penn]]"
  - "[[20260730-palantir-responsible-ai-evals-prototype-to-production]]"
  - "[[20260930-openrouter-golden-eval-production-traffic]]"
---

# Evals-as-PRD（评测即需求文档）

> [!definition] 定义
> **Evals-as-PRD** 是 Anthropic 产品团队的内部命题（"evals are the new PRDs"，与 Garry Tan 的公开表述收敛）：在明确的行为问题上，可运行评测可以充当需求的简写或验收合同；不是对所有需求载体的普遍排序。Eval 同时是模型评估工具和产品定义工具——写 eval 就是在定义"产品应该怎样"。

## 机制链：从模糊抱怨到可运行需求

Dianne Penn 给出的完整路径（Anthropic 早期 JSON schema 失败案例）：

```
用户反馈（"Claude is not good at following instructions"）
  ↓ 追问具体情境、原始段落、确切响应
受访者回忆（早期此类抱怨约80%指向JSON输出错误；无抽样分母）
  ↓ 生成 30-40 个失败样例
Eval set（prompt + response + golden answer）
  ↓ 入库，每版模型运行
后续评测据受访者回忆约99.9%–100%；无独立统计或用户总体痛点测量
```

关键操作原则：

- **"you don't need hundreds, just 10 great evals"**——eval 质量重于数量，关键是覆盖真实失败分布（含"不应失败"的正例）。
- **sweat the tokens as much as you sweat the pixels**——PM 读对话 transcripts 定位失败轨迹，取代部分用户访谈功能。
- **缩短到可行动性的距离**——eval 的价值在于把"Claude hallucinated"这类不可行动抱怨，转译为研究者可行动的失败分类（tool use 失败 / search synthesis 失败 / alignment 问题）。

## 从用户反馈到 production-derived executable spec（2026-10）

[[20260930-openrouter-golden-eval-production-traffic]] 把“evals are the new PRDs”从一次性失败归因推进成持续运行的产品规格维护机制。Dianne Penn 的案例从用户抱怨追踪到具体失败样例；OpenRouter 的流程则从生产日志持续抽取真实分布、聚类去重、补风险尾部、由专家定义 expected behavior，再进入 CI。

```text
production logs
  → privacy scrub + provenance
  → dedup / cluster
  → frequency + risk weighting
  → expert expected behavior / rubric
  → evaluator QA
  → CI regression
  → new production failures
  → next eval epoch
```

**判断**：当产品已经进入生产，executable spec 不应只由 PM 主动“写出来”，还应被现实流量持续修正。用户实际怎么使用产品、出现了哪些新失败、哪些低频错误代价很高，都应该进入下一版 eval contract。

这使 eval 同时承担两种不同但互补的职责：

1. **需求表达**：什么行为算正确、哪些约束不能破；
2. **分布监测**：当前 production reality 是否已经偏离旧需求假设。

需要保持一个重要边界：golden set 可以跨产品阶段演化，但每次比较候选版本时必须冻结 dataset、rubric 与 baseline。否则“需求变了”和“系统回归了”会混在同一个分数变化里。

- **证据**：[[20260930-openrouter-golden-eval-production-traffic]]；production sampling、rubric calibration、Git/CI 与 refresh 流程。
- **边界**：生产流量本身不是完整 PRD；它倾向反映已有用户与已有产品形态，无法替代前沿能力探索、战略方向、品牌体验和尚未出现的用户需求。

## PRD 的剩余功能

Penn 在访谈48:01–49:01明确说每个模型仍有PRD，服务于产品、工程、法务和安全等利益相关方。她特别强调两个用途，而非限定为仅两种功能：

1. **多人对齐的 source of truth**：模型发布涉及工程、法务、安全等多方时，PRD 仍是"让大群人朝同一方向划船"的协调载体。
2. **模糊问题的 product vision**：尚无用户痛点数据的前沿能力（如早期 computer use），需要 vision 文档探索"如何让技术对某群人先可用"。

## 两侧证据

| 视角 | 来源 | 贡献 |
|------|------|------|
| PM 工作流 | Dianne Penn（Anthropic） | evals 如何取代需求定义、失败轨迹归因方法、PRD 功能收窄 |
| 平台基础设施 | [[20260730-palantir-responsible-ai-evals-prototype-to-production\|Palantir AIP Evals]] | test bench / evaluator / 3x 重复 / drill-down 迭代的运行时生命周期 |

## 关键数据点

- Dianne Penn 案例（公开转录44:29–46:42）：早期此类反馈约80%指JSON输出问题，建议先构造30–40例，后续该eval约99.9%–100%为口述回忆，非所有JSON任务准确率；[访谈转录](https://pod.wave.co/podcast/lennys-podcast-product-career-growth/anthropics-first-technical-pm-on-token-maxing-the-jagged-edge-and-living-in-the-future-dianne-penn)（2026-11-28定向复核）
- "you don't need hundreds, just 10 great evals"——质量重于数量
- Eval 同时承担产品评估工具 + 产品定义工具双重身份

## 前提与局限性

- **适用域**：命题成立的前提是产品质量可归约为可评测的行为维度。UX质感、品牌、情感共鸣等难以用单一指标完整表达的维度仍需 vision 文档——口号的适用域比表述窄。
- **ground truth 依赖**：evals 的 golden answer 多来自人类历史判断或 PM 判断，可能继承判断偏差；可通过客观结果、多人标注、反例和独立验收纠正，不能据此推出系统能力上界（参见 [[Evaluator-Miscalibration]]）。
- **角色门槛**：PM 需要理解任务及验收标准；实现评测所需工程能力可由本人或团队提供。Anthropic 的角色实践不等于所有团队的必要招聘条件。

## 关联概念

- [[Evaluation-Set]] — 资产层：eval 的构建、归属与生命周期
- [[Model-Introspection]] — 失败轨迹归因依赖对模型行为的自省式分析
- [[Transparent-Tool-Handoff]] — drill-down 后的定点修复路径之一
- [[Mechanical-Sympathy-for-LLMs]] — 写 eval 的能力前提是对模型行为边界的经验性理解
- [[Loss-Function-Development]] — evals 作为损失函数的另一形态（LFD 面向长周期优化，本命题面向产品迭代）
