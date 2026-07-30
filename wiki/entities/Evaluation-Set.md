---
type: entity
title: Evaluation Set
aliases:
  - Evaluation Set
  - 评测集
  - AI 评测集
definition: "把真实业务判断、边界案例和验收规则显式化为可复用测试样本，用来评估、迭代和迁移 AI 系统行为的关键资产"
created: 2026-05-23
updated: 2026-07-30
tags:
  - AI-evaluation
  - AI-deployment
  - enterprise
evidence_level: medium
claim_type: mixed
related_entities:
  - "[[Forward-Deployed-Engineer]]"
  - "[[Tacit-Knowledge-Lock-In]]"
  - "[[Integration-Wall]]"
  - "[[Hardware-Sovereignty]]"
  - "[[Distributional-Alignment]]"
  - "[[Specialized-Small-Models]]"
  - "[[Transparent-Tool-Handoff]]"
source_raw:
  - "[[The Return of the Deployment Company]]"
  - "[[Specialization Beats Scale A Strategic Variable Most AI Procurement Decisions Overlook]]"
  - "[[20260730-palantir-responsible-ai-evals-prototype-to-production]]"
  - "[[20260730-lenny-anthropic-first-technical-pm-dianne-penn]]"
---

# Evaluation Set（评测集）

> [!definition] 定义
> **Evaluation Set（评测集）** 是把真实业务判断、边界案例和验收规则显式化为可复用测试样本的资产。它不只是模型评分工具，也是企业工作流知识的载体：谁有权访问、导出和复用评测集，谁就掌握了 AI 系统持续迭代的关键控制点。

## 关键数据点

- Caffein Chen 文章将 FDE 的共同假设概括为：AI 商业化不能只靠 SaaS 式自助上手，需要有人进入客户现场，把客户隐性知识编码进评测集。
- 保险理赔例子说明，真正的业务规则常常不在 SOP 里，而在资深员工对例外、争议、客户等级和签核习惯的判断中。
- 文章建议企业在签 FDE 合同时明确评测集 IP、合同终止后的删除或移交、导出格式、是否可被供应商用于同业客户。
- 在 on-prem 或内部能力建设场景中，评测集、提示配置和交互日志留在企业内部，是保持数据主权和模型迁移能力的基础。
- DharmaOCR 案例说明，评测集也是模型采购的判别器：只有在真实任务 benchmark 上比较质量、成本和稳定性，企业才能发现专门化小模型是否优于更大的通用模型。

## 运行时生命周期：评测集作为迭代引擎

Palantir AIP Evals 文（2024-10）把评测集从"资产"升级为"迭代引擎"，给出单元测试范式的完整生命周期：

1. **构建 Test Bench**：用 ontology 历史数据生成 Object Set-backed Test Cases（如用专家标注的历史召回决策作 ground truth）。
2. **定义 Evaluators**：内置 no-code 比较器（如 Exact Boolean Match）/ 自定义 Python/TypeScript / LLM-as-judge。
3. **重复运行**：每个 test case 默认跑 3 次以应对 LLM 非确定性。
4. **Drill-down 迭代**：aggregate 指标定位失败案例 → 检查 inputs/intermediate outputs/final response → 三种修复路径（改 prompt / 补数据 / 加 tool handoff）→ re-run 防回归。

示范曲线：产品召回系统准确率 41.3% → 修 prompt（补充 expert review 触发条件）→ 93.3% → 剩余失败定位为 LLM 数学错误（1.865 vs 正确 1.864）→ handoff 给 Calculator tool（[[Transparent-Tool-Handoff]]）→ 通过。

Anthropic 产品团队的 "evals are the new PRDs"（[[20260730-lenny-anthropic-first-technical-pm-dianne-penn]]）从 PM 工作流侧确认同一趋势：用户反馈 → 读失败轨迹 → 凝结为 eval set → 可度量改进，evals 取代 PRD 承担需求定义功能。两条线索（平台基础设施视角 + PM 工作流视角）互为验证。

⚠️ 边界：ground truth 来自人类历史决策时，evals 只能收敛到人类历史判断，不能超越它；3x 重复是朴素处理，pass@k 阈值与分布偏差校正才是真正的工程难点（参见 [[Evaluator-Miscalibration]]）。

## 前提与局限性

- 评测集的价值取决于样本是否覆盖真实工作流、边界案例和失败模式；只收集 demo 成功案例会制造虚假的可靠性。
- 评测集不是中立资产。它可能间接包含客户数据、商业规则和敏感决策逻辑，因此也会成为合规和商业秘密问题。
- 评测集可导出并不等于可迁移。若格式、标注规范、业务语义和运行环境都绑定在单一供应商平台上，迁移成本仍然很高。

## 关联概念

- [[Forward-Deployed-Engineer]] — FDE 在现场提取和维护评测集
- [[Tacit-Knowledge-Lock-In]] — 评测集如果不可导出，会成为新的供应商锁定机制
- [[Integration-Wall]] — 评测集必须覆盖真实生产约束，而不是只验证沙盒能力
- [[Hardware-Sovereignty]] — 本地部署让评测集和推理日志保留在企业控制范围内
- [[Distributional-Alignment]] — 评测集把训练历史是否贴近部署任务变成可观察证据
- [[Specialized-Small-Models]] — 小模型是否足以进入生产，取决于评测集上的质量、稳定性和成本表现
