---
type: entity
title: Genomic Reanalysis
aliases:
  - Genomic Reanalysis
  - 基因组重分析
definition: "利用更新的表型、基因-疾病关系、变异证据、分析流程及临床复核，重新评估既往未解或需重新解释的基因组数据；可用规则、统计、传统生信或LLM辅助，不以LLM为必要条件。"
created: 2026-06-19
updated: 2026-11-28
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
- [NEJM AI 2026原论文摘要](https://pubmed.ncbi.nlm.nih.gov/42529462/)：回顾性四队列未解376例（神经发育100、神经肌肉61、儿科意外猝死200、早期精神病性症状15），新本地诊断18/376（4.8%，95% CI 2.9–7.5%），分组10/100、4/61、2/200、2/15。预先定义为P/LP变异、CLIA实验室确认并返还家庭；专家ACMG/AMP裁定，不是模型直接诊断或相对传统重分析的净增益。
- [OpenAI项目说明](https://openai.com/index/diagnose-rare-childhood-diseases/) 的85.6 vs42.1为此前已解真值测试集的平均最小自报分数，不是376例未解队列的校准结果；组间均值差不等于个体概率校准、机制自省或安全阈值。
- 7/18重新发现为项目方对既有公共证据与本地记录差异的描述；非七项全球原创发现，未逐案核对数据库版本。

## 竞争性方法（候选，待正式晋升）

[Welland et al., Nature Medicine 2026](https://doi.org/10.1038/s41591-026-04477-5) 摘要及Fig1–3图注：Talos自动整合更新的基因-疾病与变异证据、遗传过滤及人工复核；1,089人验证，trio识别90%既有诊断、平均1.3候选/例，月度迭代约每200例1候选；未解4,735人队列241项诊断（5.1%）。78项新基因疾病关系、54项新变异证据、109项分析改进。非与LLM同队列随机对照，不比较4.8%和5.1%以裁决优劣。保留确定性流程、知识更新、复核工作量及增量收益作为独立基线；本轮仅核摘要和图注，未复跑或审逐例结果。

## 前提与局限性
- **基因组版本与变异复杂性**: 当前研究未能系统评估超复杂的结构变异（SV）、重复扩增、内含子突变或嵌合体等情况。
- **回顾性限制**: 研究所使用的是回顾性评估数据，且审查者对模型置信度得分没有做双盲评估，需未来通过前瞻性多中心研究做进一步验证。

## 关联概念
- [[Scientific-Discovery-AI]]：基因组重分析所依托的更宏观科学发现 AI 形态。
- [[Model-Introspection]]：自报分数需独立验证区分能力与校准，不能代替临床证据。
- [[OpenAI]]：该研究所采用的前沿推理模型（o3 Deep Research）的提供方。
