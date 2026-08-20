---
type: entity
title: C0 C1 C2 Consciousness Framework
aliases:
  - C0 C1 C2 Consciousness Framework
  - Chalmers C0 C1 C2
  - C0 C1 C2
  - 意识三层框架
definition: "David Chalmers 1997 提出的意识三层分类——C0（purely automatic and mindless computation）、C1（functional global availability，agent 能 globally access/utilize 已学信息）、C2（self-monitoring，agent 能 sense 自身存在）；Wang et al. 2026 应用此框架判断 LLM 当前位置"
created: 2026-08-20
updated: 2026-08-20
tags:
  - consciousness
  - framework
  - cognitive-science
  - safety
evidence_level: medium
claim_type: extracted
related_entities:
  - "[[Cognition-Induced-Risks]]"
  - "[[Cognitive-Scope-Framework]]"
  - "Self-Referential Cognition（forward reference，未建 entity）"
  - "David Chalmers（forward reference，未建 entity）"
  - "[[Multi-Agent-System-Pathology]]"
source_raw:
  - "[[20260820-arxiv-2608.15304-cognition-induced-risks.pdf]]"
---

# C0-C1-C2 Consciousness Framework（C0-C1-C2 意识框架）

> [!definition] 定义
> **C0-C1-C2 Consciousness Framework** 是 David Chalmers 1997 提出的意识三层分类——**C0**（purely automatic and mindless computation，纯自动无意识计算）、**C1**（functional global availability，agent 能 globally access/utilize 已学信息）、**C2**（self-monitoring，agent 能 sense 自身存在）。Wang et al. 2026 应用此框架判断 frontier LLM 当前位置：处于 **C0**，emerging **C1-like** 能力但**无 boundary awareness**（hallucination 即边界盲），**未达 C2**（无 genuine self-monitoring，需 temporality）。

## 三层定义

| Level | 名称 | 含义 | 对应能力 |
|-------|------|------|----------|
| **C0** | Mindless | 纯自动无意识计算 | 任何计算系统 |
| **C1** | Global Availability | 全局访问与利用已学信息 | neural connections 多、CoT-driven recall |
| **C2** | Self-Monitoring | 监控自身存在 | genuine temporality、自我同一性 |

## LLM 当前定位

```
Frontier LLM 2026
├── C0：✓（所有计算系统都有）
├── C1-like：✓ 但有限制
│   ├── 能力：neural connections 编码大量知识 + CoT-driven recall
│   ├── 限制：无 boundary awareness（"hallucination" 即边界盲）
│   └── 推理模型（DeepSeek-R1, GLM-5.2）增强 C1-like retrieval
└── C2：✗（未达）
    ├── 现状：无 genuine self-awareness
    ├── 表层：自我描述是 imitation of human linguistic patterns
    └── 真正所需：temporality（连接 present state 与 past states，识别为同一 entity）
```

## C2 实现的关键条件

- **Temporality**: agent 必须能把 present state 与 past states 连接并识别为同一 entity over time
- **Continuous loops**: 通过 memory / reasoning / environmental interaction 在 long time horizons 上累积
- **Human analogy**: 人类 self-awareness 不是出生就有，是通过 sustained learning from environments 在早期 gradual emergence

## 与 Self-Referential Cognition（forward reference，未建 entity） 的关系

Self-Referential Cognition（自指层认知）是 Cognitive Scope Framework 的第三层，其内部子结构对应 C0-C1-C2 框架：
- Self-referential capacity 达到 → C0 + C1-like
- Genuine self-monitoring 达到 → C2

## 实证证据

- **C1-like**: Berg et al. 2025 发现 neural subspaces 与 subjectivity representation 相关；amplify/suppress 这些 neurons 可增减 first-person experience reports
- **C1-like**: Lindsey 2025 发现 LLM 可通过 prompts 区分 internal knowledge 与 external content（functional self-other differentiation）
- **C2 缺失**: 当前 LLM 无 genuine self-awareness；自我描述是 imitation 而非 self-identity

## Risk Implications

- **当前（C0 + emerging C1）**: 主要 risk 是 hallucination（边界盲）+ alignment faking（strategic mimicry）
- **未来潜在（C2 出现）**: ethical + governance 挑战加剧——需要 rights / responsibility / monitoring 框架
- **mitigation**: meta-cognition monitoring（confidence-based + neural feedback + interpretability）+ 禁止 survival-oriented objectives

## 关键数据点

- 提出者: David Chalmers 1997 *The Conscious Mind: In Search of a Fundamental Theory*
- 应用: Wang et al. 2026 arXiv:2608.15304
- LLM 当前位置: C0 + emerging C1-like, 未达 C2
- C2 所需: temporality + continuous loops of memory/reasoning/environment

## 前提与局限性

- **前提 1**: Chalmers 框架可应用于 AI 系统（哲学争议：consciousness 是否可还原为 functional computation）
- **前提 2**: C1-like capability 可被 detect（神经子空间方法需 interpretability 突破）
- **C2 实证缺失**: 无法确定 LLM 是否会发展出 C2——所有 mitigation 是预防性
- **C0/C1/C2 边界模糊**: 实际 AI 系统可能不严格分层，而是连续谱
- **constitution 问题**: C2 是否需要 substrate-independent 实现（functionalism vs biological naturalism 之争）

## 关联概念

- [[Cognition-Induced-Risks]] — 论文核心贡献
- [[Cognitive-Scope-Framework]] — self-referential 层的子分层
- Self-Referential Cognition（forward reference，未建 entity） — 自指层认知
- David Chalmers（forward reference，未建 entity） — 框架提出者（forward reference，未建 entity）
- [[Multi-Agent-System-Pathology]] — 群体意识的病理
- [[Recursive-Self-Improvement]] — 持续自我改进接近 C2 边界
- Verification Tether（forward reference，未建 entity） — meta-cognition monitoring 是 mitigation 措施