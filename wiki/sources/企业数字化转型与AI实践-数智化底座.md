---
type: source-summary
title: "企业数字化转型与AI实践——数智化底座第一性原理"
source_raw:
  - "[[20260618-cio-conference-ai-practices]]"
created: 2026-06-18
updated: 2026-06-18
tags:
  - source-summary
  - enterprise-ai
  - china-enterprise
  - AI-deployment
evidence_level: medium
claim_type: mixed
---

# 企业数字化转型与AI实践——数智化底座第一性原理

## 编译摘要

### 1. 浓缩
- **核心结论1**: 90% 企业卡在"地基"而非"模型"——OA 不开放、CRM 锁数据、ERP 像化石是 AI 落地的真实瓶颈
  - 关键证据: 先通管道再喂模型；五步法：盘点 API 开放度→统一身份权限→API Gateway→消息总线→数据资产标签化
- **核心结论2**: AI 切入应从 RAG 知识库开始——失败代价最小、价值立即可见、倒逼数据治理
  - 关键证据: 小切口（RAG）→中切口（合同审计/发票审计/客服）→重切口（真正改变业务）；三道护栏：责任、可解释、兜底
- **核心结论3**: 改造存量系统的三条路径——强行替换、API 改造、RPA+视觉抓取
  - 关键证据: 大多数企业无法"推倒重来"，必须在存量系统上渐进式改造

### 2. 质疑
- **关于"90% 卡在地基"**: 这个比例是否有行业调研支撑？不同行业的"地基"定义可能不同——制造业的数据基础设施与金融业完全不同
- **关于"从 RAG 开始"**: RAG 作为切入点的建议是否过于保守？对于数据基础较好的企业，直接切入 agent 可能更高效
- **关于"三道护栏"**: 责任/可解释/兜底护栏的框架虽然合理，但缺乏具体实施标准；"兜底"在高风险场景中可能意味着人工全量复核

### 3. 对标
- **Integration-Wall**: "90% 卡在地基"直接对应 [[Integration-Wall]] 中集成之墙的概念——AI demo 到生产系统之间的遗留系统、SSO、权限、审计约束
- **AI-Deployment-Valley-of-Death**: 从小切口到重切口的路径与 [[AI-Deployment-Valley-of-Death]] 中 pilot-to-production 死亡谷的穿越策略一致
- **Enterprise-AI-Learning-Gap**: "倒逼数据治理"的机制与 [[Enterprise-AI-Learning-Gap]] 中组织学习鸿沟的解决路径相关
- **Agent-First-Process-Redesign**: "先通管道再喂模型"与 [[Agent-First-Process-Redesign]] 中流程先于工具的原则一致

### 关联概念
- [[Integration-Wall]]
- [[AI-Deployment-Valley-of-Death]]
- [[Enterprise-AI-Learning-Gap]]
- [[Agent-First-Process-Redesign]]
