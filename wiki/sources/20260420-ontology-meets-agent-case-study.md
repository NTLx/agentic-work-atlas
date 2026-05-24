---
type: source-summary
title: "20260420-ontology-meets-agent-case-study"
source_raw:
  - "[[20260420-ontology-meets-agent-case-study]]"
created: 2026-05-24
updated: 2026-05-24
tags:
  - source-summary
  - Ontology
  - AI-Agent
  - Enterprise-AI
---

# 20260420-ontology-meets-agent-case-study

## 编译摘要

### 1. 浓缩
- **核心结论1**: 本体不是数据库，应作为 Agent 与企业系统之间的语义层，而非数据源
  - 关键证据: 本体承载"地图"（语义与规则），数据库承载"仓库"（海量数据）
- **核心结论2**: 本体 Agent 工具选择原则：日常查询用数据库，规则判定用本体推理
  - 关键证据: OntologyReasoner 注入事实 → 推理机分类 → 读取结论，而非 LLM 判断
- **核心结论3**: 本体规则声明式定义，改模型文件即可，Agent 代码不动 — 优于传统规则引擎
  - 关键证据: IF/THEN 规则引擎问题：概念口径不一致、跨规则复用困难；本体先定义概念再判断

### 2. 质疑
- **关于"本体定位"的质疑**: 本体作为语义层需要企业有统一的业务概念，但很多企业概念本身就是混乱的
- **关于"推理性能"的质疑**: 注入数据 + 运行推理机 相比 直接查询较慢，高频实时场景是否适用？
- **关于"规则声明式"的质疑**: OWL 等价类表达有限，复杂规则（如时间窗口、跨系统条件）可能需要 SWRL 或代码

### 3. 对标
- **跨域关联1**: 本体推理类似"编译器类型检查" — 声明式约束，自动验证，无需手动判断
- **跨域关联2**: Ontology Agent 类似"规则驱动的微服务" — 业务逻辑集中在语义层，Agent 调用而非实现

### 关联概念
- [[Ontology]]
- [[Ontology-Agent]]
- [[TBox]]
- [[ABox]]
- [[OWL]]
- [[HermiT]]
- [[Owlready2]]
- [[Enterprise-Ontology-Application]]
