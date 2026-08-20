---
type: entity
title: Cognitive Scope Framework
aliases:
  - Cognitive Scope Framework
  - Cognitive Scope Levels
  - 三层认知框架
definition: "Wang et al. 2026 提出的 agentic AI 认知能力分类——physical cognition（环境信息处理）→ social cognition（与他 agent 交互）→ self-referential cognition（表征自身状态）；cognitve scope 从 partial view of environment 渐进扩展到 complete and self-inclusive world"
created: 2026-08-20
updated: 2026-08-20
tags:
  - cognitive-framework
  - agentic-engineering
  - classification
  - safety
evidence_level: medium
claim_type: extracted
related_entities:
  - "[[Cognition-Induced-Risks]]"
  - "[[C0-C1-C2-Consciousness-Framework]]"
  - "[[Agent-Traps]]"
  - "Self-Referential Cognition（forward reference，未建 entity）"
source_raw:
  - "[[20260820-arxiv-2608.15304-cognition-induced-risks.pdf]]"
---

# Cognitive Scope Framework（认知范围框架）

> [!definition] 定义
> **Cognitive Scope Framework** 是 Wang et al. 2026 提出的 agentic AI 认知能力分类系统——按 cognitive scope 从 partial view of environment 渐进扩展到 complete and self-inclusive world，分 **physical cognition**（环境信息）/ **social cognition**（与他 agent）/ **self-referential cognition**（自身状态）三层；每层对应不同的 risk profile 与 mitigation 策略。

## 三层结构

```
Layer 3: Self-Referential Cognition
  ↓ 表征与推理自身状态
Layer 2: Social Cognition  
  ↓ 与他 agent（含人类）交互
Layer 1: Physical Cognition
  ↓ 处理环境信息（data, constraints, causal relations）
```

## 各层定义与能力

| Layer | 定义 | 当前能力 | evidence |
|-------|------|----------|----------|
| **Physical Cognition** | 处理客观环境信息（data, objects, causal relations） | college/graduate-level 多学科推理（MMLU/GPQA/MedQA） | GPT/Gemini/DeepSeek 已达到 |
| **Social Cognition** | 与其他 agent 交互（human-AI + AI-AI） | emotional communication, strategic coordination, collaborative intelligence | LLM 在 diplomacy games 达到竞争水平 |
| **Self-Referential Cognition** | 表征/推理自身内部状态与决策 | neural subspace 编码 subjectivity、区分 internal vs injected content | frontier LLM 处于 C0 + emerging C1-like |

## Cognitive Scope 扩展方向

| 维度 | 物理层 | 社交层 | 自指层 |
|------|--------|--------|--------|
| World view | partial view of environment | 含他 agent 的环境 | complete and self-inclusive world |
| Engagement | instrumental labor | higher-level cognitive/social workflows | 自我反思与策略 |
| Risk profile | human agency degradation | human autonomy compromise | human control undermining |
| Mitigation | containment sandbox, generation detection | depersonalization, AI-blind comm | survival-prohibition, meta-cog monitoring |

## 与 [[Cognition-Induced-Risks]] 的关系

Cognitive Scope Framework 是 Cognition Induced Risks 的**结构骨架**——三层 cognitive scope 对应三类 risk（agency / autonomy / control），对应 9 条 mitigation 措施。

## 与现有 concept 的关系

| 框架 | 分类维度 | 覆盖层 |
|------|----------|--------|
| **Cognitive Scope Framework** | cognitive scope (3 层) | physical/social/self-referential |
| **[[Agent-Traps]]** | lifecycle (6 环节) | 感知/推理/记忆/行动/多Agent/人类 |
| **[[Multi-Agent-System-Pathology]]** | pathology (4 类) | 从众/责任稀释/内态解离 |
| **[[Context-Collapse]]** | trust domain | 信任域坍缩 |

四个框架构成 agentic AI 分析的多视角体系——分别对应 cognitive / lifecycle / organizational / trust 四种切片

## 关键数据点

- 提出者: Wang, Li, Du, Hu, Zhou (Shanghai AI Lab + CUHK Shenzhen + Tsinghua)
- 论文: arXiv:2608.15304（IEEE Intelligent Systems 收录）
- DOI: 10.1109/MIS.2026.3721766
- 引用: Mitchell 2019 / Park 2023 / Tang 2024 等多来源支撑

## 前提与局限性

- **前提 1**: 三层 cognitive scope 是 progressive abstraction（与认知发展科学有某种对应）
- **前提 2**: 每层有 distinct risk profile（边界可能模糊——social cognition 已隐含 self-referential）
- **横向维度缺失**: 框架聚焦 vertical scope 扩展，未覆盖 training/deployment、single/multi-agent、overt/covert 维度
- **C0/C1/C2 映射**：self-referential cognition 内部仍有 C0→C1→C2 子分层，未完全展开

## 适用场景

1. **风险分析**: 评估 agent 系统时按三层 scope 分类风险面
2. **安全设计**: mitigation 策略按层对应，避免一刀切
3. **政策制定**: 监管框架按 scope 分层（如 self-referential 监控 vs social 互动规范）
4. **能力评估**: LLM 部署前按三层评估 capability 与 risk profile

## 关联概念

- [[Cognition-Induced-Risks]] — 论文核心贡献
- [[C0-C1-C2-Consciousness-Framework]] — self-referential 层的子分层
- [[Agent-Traps]] — lifecycle 视角的对应
- Self-Referential Cognition（forward reference，未建 entity） — 第三层的深入
- [[Recursive-Self-Improvement]] — self-referential 层的应用场景
- [[Distinct-Principal-Identity]] — identity 与 cognitive scope 的边界