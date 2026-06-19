---
type: entity
title: Genomic Reanalysis
aliases:
  - Genomic Reanalysis
  - 基因组重分析
definition: "利用先进人工智能模型（尤其是具备深度推理和自主搜索能力的模型）对先前未解的基因测序和临床数据进行系统性重新评估，结合最新的医学文献和数据库，发现新的致病变异或分子解释的过程。"
created: 2026-06-19
updated: 2026-06-19
evidence_level: high
claim_type: mixed
tags:
  - concept
  - science
  - medical-AI
related_entities:
  - "[[Scientific-Discovery-AI]]"
  - "[[Model-Introspection]]"
  - "[[OpenAI]]"
source_raw:
  - "[[20260618-openai-rare-disease-diagnosis]]"
---

# Genomic Reanalysis（基因组重分析）

## 关键数据点
- **诊断检出率**: 针对 376 例先前未解的基因测序案例（包括神经发育、神经肌肉、早期精神分裂等），推理模型辅助的基因组重分析成功找到了 18 例诊断，产出率为 4.8%。
- **置信度表现**: 在重分析中，模型的自我评估最低平均置信度（min score）在诊断正确时为 85.6，而在错误/未知分类中为 42.1，显示出极高的判断一致性。
- **重新发现率**: 在 18 例被重新找到的诊断中，有 7 例此前已被认定为致病变异并记录在公共数据库中，但未能存在于研究前的院内记录中，暴露了临床数据整合与及时重分析的滞后。

## 前提与局限性
- **基因组版本与变异复杂性**: 当前研究未能系统评估超复杂的结构变异（SV）、重复扩增、内含子突变或嵌合体等情况。
- **回顾性限制**: 研究所使用的是回顾性评估数据，且审查者对模型置信度得分没有做双盲评估，需未来通过前瞻性多中心研究做进一步验证。

## 关联概念
- [[Scientific-Discovery-AI]]：基因组重分析所依托的更宏观科学发现 AI 形态。
- [[Model-Introspection]]：模型置信度自我追踪，对诊断可靠性有指导性意义。
- [[OpenAI]]：该研究所采用的前沿推理模型（o3 Deep Research）的提供方。
