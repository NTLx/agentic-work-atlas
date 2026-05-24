---
type: topic
title: Enterprise AI Model Sourcing
description: "企业 AI 模型采购不应默认等于买最大 frontier API，而应按任务分布、评测证据、成本曲线、部署约束和组织能力分层选择"
created: 2026-05-24
updated: 2026-05-24
tags:
  - enterprise-AI
  - AI-deployment
  - model-selection
related_entities:
  - "[[Layered-AI-Sourcing]]"
  - "[[Specialized-Small-Models]]"
  - "[[Distributional-Alignment]]"
  - "[[Specialization-Compounds]]"
  - "[[Evaluation-Set]]"
  - "[[Hardware-Sovereignty]]"
source_raw:
  - "[[Specialization Beats Scale A Strategic Variable Most AI Procurement Decisions Overlook]]"
  - "[[The Return of the Deployment Company]]"
---

# Enterprise AI Model Sourcing（企业 AI 模型采购）

> [!summary] 核心洞察
> 企业 AI 采购的默认问题不应是“哪家 frontier API 最强”，而应是“这个工作流需要哪种模型来源、哪种部署形态、哪种评测证据和哪种组织能力”。最大模型仍然重要，但在可验证、高频、分布清楚的任务中，专门化小模型可能改写质量、成本和稳定性的排序。

## 为什么这是模型采购问题

过去三年，企业默认选择最大 frontier model 是合理的：通用 benchmark、供应商能力和风险规避都支持这个选择。

[[Specialization Beats Scale A Strategic Variable Most AI Procurement Decisions Overlook]] 提供了一个反例边界：在巴西葡萄牙语 OCR 这个具体企业域里，专门化 3B 模型在质量、成本和稳定性上同时胜出。它不证明“规模不重要”，但证明“规模不是唯一应该优先测试的变量”。

这让模型采购从品牌排序变成系统设计问题。

## 五个采购变量

| 变量 | 采购问题 | 相关实体 |
|------|----------|----------|
| 任务分布 | 模型训练历史离部署任务多近？ | [[Distributional-Alignment]] |
| 专门化层级 | 起点是通用模型、领域模型，还是业务域模型？ | [[Specialization-Compounds]] |
| 评测证据 | 是否有真实工作流评测，而不是只看公开榜单？ | [[Evaluation-Set]] |
| 成本曲线 | 高频调用时 API 成本、推理成本和运维成本如何变化？ | [[Specialized-Small-Models]] |
| 部署约束 | 数据、权限、合规和运维是否要求本地化或分层？ | [[Layered-AI-Sourcing]] |

## 专门化小模型适合的位置

[[Specialized-Small-Models|专门化小模型]]不是通用模型的全面替代，而是适合进入企业 AI 组合的一层。

更适合的场景：

- 任务边界清楚，输入输出稳定。
- 有大量重复调用，推理成本会变成主要变量。
- 输出可验证，能建立客观评测和回归测试。
- 企业拥有或能合法获得足够接近部署分布的数据。
- 任务涉及数据主权、延迟或本地部署要求。

不适合默认小模型化的场景：

- 任务开放、跨域、长尾、不确定。
- 缺少真实评测集，只能靠主观感受判断质量。
- 业务需求还在探索期，过早专门化会锁死方向。
- 运维能力不足，无法持续监控、更新和回滚模型。

## 与分层 AI 来源策略的关系

[[Layered-AI-Sourcing|分层 AI 来源策略]]原本强调 on-prem、cloud API、FDE 和内部团队之间的分工。专门化小模型把这个框架再推进一步：即使同样选择“模型能力”，也要继续区分 frontier generalist、开源通用模型、领域模型和业务域专门模型。

这意味着企业模型组合可能长这样：

- frontier API 负责开放推理、快速探索和低频复杂任务。
- 专门化小模型负责高频、可验证、成本敏感的核心流程。
- FDE 或外部部署团队负责穿越早期集成约束。
- 内部团队逐步接管评测集、数据管线和模型运维。

采购能力的成熟标志，不是替某一个模型站队，而是能把不同模型放到正确工作流里。

## 边界

DharmaOCR 的证据很强，但范围窄。它来自 OCR 任务、特定语言文档、特定 benchmark 和模型发布方文章。知识库应保留这个结论的边界：

> 专门化小模型已经足以挑战“最大模型默认最优”的采购假设；但每个企业域都需要自己的真实评测来决定是否成立。

没有评测集，专门化只是叙事。有评测集，采购才开始变成工程。

## 结论

企业 AI 模型采购正在从“买最强模型”转向“设计模型组合”。

这套组合的核心资产不是某个供应商账号，而是企业自己能否描述任务、构造评测、理解成本曲线、选择部署边界，并把每次模型选择的证据沉淀为下一次更好的选择。
