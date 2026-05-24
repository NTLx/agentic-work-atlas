---
type: source-summary
title: "20260420-build-first-business-ontology"
source_raw:
  - "[[20260420-build-first-business-ontology]]"
created: 2026-05-24
updated: 2026-05-24
tags:
  - source-summary
  - Ontology
  - Enterprise-AI
  - RDF
  - OWL
---

# 20260420-build-first-business-ontology

## 编译摘要

### 1. 浓缩
- **核心结论1**: 本体工程分 TBox（概念框架）和 ABox（事实数据），类比 Schema vs Data
  - 关键证据: TBox 定义类、关系、约束；ABox 注入实例、建立关联；推理基于两者推导新知识
- **核心结论2**: RDF/OWL 是本体核心语言，Protégé + HermiT + GraphDB 构成工具链
  - 关键证据: RDF 表达事实（三元组）、OWL 定义规则（等价类）、推理机自动分类
- **核心结论3**: 实战构建"订单加急"本体：定义类、属性、等价类公理，推理机验证归类
  - 关键证据: ReadyToShipOrder（有库存+质检通过）、ExpediteEligibleOrder（可发货+VIP）

### 2. 质疑
- **关于"工具链"的质疑**: Protégé 主要用于开发期验证，生产环境需要 GraphDB + SPARQL，部署成本较高
- **关于"推理验证"的质疑**: 示例场景简单（2条规则），企业实际规则可能有几十上百条，建模复杂度会指数上升
- **关于"Owlready2"的质疑**: Python 库适合测试，但生产推理性能如何？大规模数据是否可行？

### 3. 对标
- **跨域关联1**: 本体建模类似数据库 Schema 设计 — 先定义结构，再填充数据，需要迭代验证
- **跨域关联2**: 等价类公理类似编程中的"派生类型" — 满足条件自动归类，无需手动维护

### 关联概念
- [[Ontology]]
- [[TBox]]
- [[ABox]]
- [[RDF]]
- [[OWL]]
- [[Protégé]]
- [[HermiT]]
- [[Owlready2]]
- [[GraphDB]]
- [[SPARQL]]
- [[Enterprise-Ontology-Application]]
