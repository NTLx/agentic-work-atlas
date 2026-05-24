---
type: source-summary
title: "20260420-ontology-enterprise-ai-agent"
source_raw:
  - "[[20260420-ontology-enterprise-ai-agent]]"
created: 2026-05-24
updated: 2026-05-24
tags:
  - source-summary
  - AI-Agent
  - Ontology
  - Enterprise-AI
---

# 20260420-ontology-enterprise-ai-agent

## 编译摘要

### 1. 浓缩
- **核心结论1**: 企业 AI Agent 失败率高（幻觉、跑偏、不可控），根源是"有数据缺语义" — LLM 不理解企业业务规则
  - 关键证据: 同词不同义（ALLOCATED 状态在不同系统含义不同）、规则缺失（VIP 才能加急）、难以解释和修复
- **核心结论2**: 现有工程手段（Skills/RAG、Workflow）只能局部缓解，无法治本
  - 关键证据: Skills 是"提示"而非约束、Workflow 仍依赖 LLM 判断或陷入规则爆炸
- **核心结论3**: 本体作为"语义层"，承载概念框架和业务规则，让推理有据可依
  - 关键证据: 本体区分 TBox（规则）和 ABox（事实）、推理机自动分类而非 LLM 概率推理

### 2. 质疑
- **关于"结论1"的质疑**: 本体假设企业有明确的业务规则可形式化，但很多企业规则是隐性的、模糊的、依赖经验的
- **关于"结论2"的质疑**: Skills/Workflow 在某些场景足够用，本体是否过度工程？当规则只有几条时，if/else 更简单
- **关于数据可靠性的质疑**: 本体推理依赖准确的事实数据注入，如果企业系统数据质量差，推理结论也会出错

### 3. 对标
- **跨域关联1**: 本体类似编程领域的"类型系统" — 约束行为、提供保证、增强可解释性
- **跨域关联2**: 本体类似法律领域的"判例法" — 先定义概念框架，再根据具体事实判定是否适用

### 关联概念
- [[Ontology]]
- [[TBox]]
- [[ABox]]
- [[Ontology-Agent]]
- [[Enterprise-Ontology-Application]]
