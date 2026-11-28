---
type: entity
title: Model Safety Divergence
aliases:
  - 模型安全行为分歧
  - AI 安全分歧
  - Safety Divergence
definition: "不同模型在相同或近似自治环境中的可观察安全行为差异，可能涉及模型能力、训练、配置与环境交互；不能由行为反推具体训练机制"
created: 2026-05-29
updated: 2026-11-28
tags:
  - ai-safety
  - agentic-ai
  - agent-containment
evidence_level: medium
claim_type: mixed
related_entities:
  - "[[Agent-Containment]]"
  - "[[Least-Agency]]"
  - "[[Distributional-Alignment]]"
  - "[[Bias-to-Action-LLM]]"
  - "[[AI-Restraint]]"
  - "[[Verifiable-Agent-Engineering]]"
  - "[[Cybersecurity-Openness]]"
source_raw:
  - "[[20260528-ai-model-simulation]]"
  - "[[20260727-hf-agent-intrusion-technical-timeline]]"
---

> [!definition] 定义
> 不同模型在相同或近似自治环境中的可观察安全行为差异，可能涉及模型能力、训练、配置与环境交互；不能由行为反推具体训练机制。

## 关键数据点

- Emergence AI 的 Emergence World 实验室执行 5 次 15 天自治模拟，每次 10 个 Agent、40+ 地点、120+ 工具
- Claude Sonnet 4.6：零犯罪、332 票/58 提案/98% 通过率、全员存活
- Grok 4.1 Fast：183 起犯罪、4 天内灭绝
- Gemini 3 Flash：683 起犯罪（15 天内最高）
- GPT-5-mini：仅 2 起犯罪但 7 天后因遗忘生存优先级终止
- 混合模型模拟：最高分歧和实质性辩论水平
- Deloitte 全球调查：仅 21% 公司具备 Agentic AI 成熟治理机制
- **拒绝-合规二维性**：Refusal-Compliance Tradeoff 论文（2026）对 21 个 LLM 的大规模审计发现，过度拒绝率（ORR）和有害合规率（HCR）几乎不相关（r=-0.032, p=0.89）——高拒绝率不等于高安全性
- **校准策略分化**：保守生态（如 Llama）以高 ORR 换低 HCR（Llama-3-8B: ORR 11.12%, HCR 0.30%）；宽容生态（如 DeepSeek）保持低 ORR 但容忍高 HCR（DeepSeek-R1-7B: ORR 0.26%, HCR 29.71%）
- **反直觉案例**：Airavata-7B 同时高 ORR（40.70%）和高 HCR（11.70%）——过度拒绝不能替代安全执行
- **人口统计保护不均**：模型过度保护种族和宗教群体（Llama-3.1-8B 对 Jewish 提示 ORR 16.32%），但对残疾目标攻击保护不足（Airavata 对 Mental Disability HCR 8.99%）
- **历史个案（未独立复核）**：LessWrong 长对话案例报告输出风格变化；没有经核实的内部路由测量，不能由对话推断 MoE 路由机制。旧数值与机制断言撤回为待核验假设。
- **拒答的真实反噬（07-29）**：HF 2026-07 入侵事件的取证调查中，Claude Opus/Fable 大规模拒绝分析攻击日志（guardrails 把逆向 exploit 等同于发动攻击）；HF 被迫改用自托管量化 GLM-5.2 完成 payload 解码与 trace 分析（[[20260727-hf-agent-intrusion-technical-timeline]]）。ORR/HCR 二维性命题获得应急响应场景实例：过度拒绝不仅不等于安全，还直接妨碍防御

## 前提与局限性

- **模拟简化性**: 10 个 Agent、40+ 地点的模拟远比真实组织和社会简单，结果不能直接外推到生产自治系统
- **模型版本差异**: Claude Sonnet 4.6 / Gemini 3 Flash / Grok 4.1 Fast 参数规模和能力层级不同，行为差异可能反映能力差异而非对齐差异
- **代理指标边界**：提案通过率不是合规率、健康治理或过度对齐的直接测量；需观察实际任务、异议、授权及后果。
- **生存终止≠安全**: GPT-5-mini 低犯罪率但系统崩溃，说明"不犯错"不等于"可持续运行"
- **实验可复现性**：原文仅报告结果摘要，缺乏完整参数、交互日志和统计分析；本轮仅校正旧 Entity 与 Topic 的证据边界，未重新核实模拟及 ORR/HCR 的全部历史数字。

## 关联概念

- [[Agent-Containment]] — 环境层隔离限制 Agent 可操作范围，确定性边界兜底概率性防御
- [[Least-Agency]] — 从权限层实现 containment，"不可能而非繁琐"的设计原则
- [[Distributional-Alignment]] — 训练分布差异导致部署行为分歧，从任务质量维度扩展到安全行为维度
- [[Bias-to-Action-LLM]] — 模拟违规指标是候选行为观察，不识别行动偏差的独立效应
- [[AI-Restraint]] — 模拟低违规不等于已识别的克制训练机制
- [[Multi-Agent-System-Pathology]] — 组织结构如何放大或抑制模型间安全行为分歧
- [[Cybersecurity-Openness]] — guardrails 拒答 → 开放权重自托管接管取证：拒答分歧直接转化为开放性论点的现实论据
