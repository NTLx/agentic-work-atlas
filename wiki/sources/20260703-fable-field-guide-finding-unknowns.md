---
type: source-summary
title: "A Field Guide to Fable: Finding Your Unknowns"
source_raw:
  - "[[20260703-fable-field-guide-finding-unknowns]]"
created: 2026-07-03
updated: 2026-11-28
tags:
  - source-summary
  - agentic-engineering
  - AI-Agent
  - human-skill
evidence_level: medium
claim_type: mixed
---

# A Field Guide to Fable: Finding Your Unknowns

## 编译摘要（2026-11-28 回溯原文）

Thariq Shihipar（2026-07-03）以个人使用 Fable 5 与 Claude Code 编辑发布视频的经验说明如何识别需求与现实约束之间的缺口。原文是第一人称实践分享，不是模型间对照。作者称这是他首次感到质量受自己澄清未知物的能力限制；不能泛化为 Fable 5 是行业第一个转移瓶颈的模型。

### 1. 未知物框架（Unknowns Framework）

| 类型 | 原文含义 | 实践 |
|---|---|---|
| Known Knowns | 已表达的要求 | 实现并验收 |
| Known Unknowns | 自知未解决的决策 | 访谈、计划 |
| Unknown Knowns | 看到才认出的隐含标准 | 原型、头脑风暴 |
| Unknown Unknowns | 尚未考虑或不知道的维度 | 盲点扫描、参考材料 |

### 2. 全周期方法

- 实现前：blind spot pass、原型、访谈、参考源码、计划；优先澄清会改变数据模型、接口或用户流程的决策。过细指令可能阻碍合理调整，过粗指令可能导致不适合本项目的默认假设。
- 实现中：记录偏差与保守选择；若偏差触及授权、目标、风险边界，应重新确认而非任意继续。
- 实现后：用演示、说明与测验辅助理解和评审。作者个人采用通过 quiz 后合并的规则；测验不替代测试、diff、独立验收或权限检查。
- 原文案例涉及转录、视频原型与调色的探索；作者引用 Boris Cherny、Jarred Sumner 作为熟悉代码库与模型行为的个人观察，未有代表性统计。

### 3. 边界

四象限是实用认知分类，不是完整可测量的需求模型。盲点扫描可帮助发现问题，却不能证明没有剩余未知物；快速原型、访谈与参考的效果须按真实项目验证。减少昂贵返工是候选机制，而非已测定收益。历史独立页的可用方法已合入本摘要，保留 Raw 与 Git 恢复路径，不额外保留单源术语页。

## 关联概念

- [[Agentic-Engineering]]、[[Context-Engineering]] — 需求澄清与真实上下文。
- [[Captain-Mindset]]、[[Skill-Chains]] — 规划和审查的辅助方法。
- [[Tacit-Knowledge-Lock-In]] — 隐含标准的表达困难（类比而非同义）。
