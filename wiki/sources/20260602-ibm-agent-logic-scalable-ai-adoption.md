---
type: source-summary
title: "Beyond LLMs: Why Scalable Enterprise AI Adoption Depends on Agent Logic"
source_raw:
  - "[[20260602-ibm-agent-logic-scalable-ai-adoption]]"
created: 2026-06-02
updated: 2026-06-02
tags:
  - source-summary
  - enterprise-ai
  - agentic-ai
  - agent-harness
  - ai-adoption
---

# Beyond LLMs: Why Scalable Enterprise AI Adoption Depends on Agent Logic

## 编译摘要

### 1. 浓缩

- **核心结论1**: 企业 Agent 的规模化瓶颈不是模型上下文不够长，而是缺少运行在模型外的 workflow-specific logic。
  - 关键证据: IBM 将 agent logic 定义为 harness 内的知识图谱、程序分析、算法、策略执行、图遍历和自适应规划，用来缩小上下文空间并引导 LLM 沿企业工作流行动。
- **核心结论2**: 生产级企业 Agent 需要把确定性结构放回系统，而不是把所有推理都交给 LLM。
  - 关键证据: IBM 在主机代码理解、测试生成、IT incident investigation、合规自动化、医疗客服和工业资产维护案例中，都用程序分析、图结构、policy-as-code 或 DAG 验证降低 token、幻觉和 unsupported claims。
- **核心结论3**: Agent logic 的核心价值是把企业隐性约束变成可执行、可审计、可复用的系统资产。
  - 关键证据: 医疗 CUGA benchmark 中，policy-as-code 不依赖 prompt 或 fine-tuning，在多个模型族上提高任务正确率，并加入 least-privilege disclosure、人类升级路径和显式合规规则。

### 2. 质疑

- **关于来源的质疑**: 文章来自 IBM Research，案例多为 IBM 产品或内部 pilot，指标可能更适合说明 IBM 路线的可行性，而不是证明所有企业 Agent 都应采用同一架构。
- **关于 benchmark 的质疑**: ITBench、CUGA 和内部 pilot 能提供可比较信号，但真实企业部署还会受数据质量、权限、合规审批、组织采纳和长期维护成本影响。
- **关于 agent logic 的边界质疑**: 如果 workflow-specific logic 过重，系统可能退回传统企业软件工程；关键不在“逻辑越多越好”，而在把稳定、可验证、低熵的部分从 LLM 上移出。
- **关于可迁移性的质疑**: 主机代码、IT incident、医疗合规和工业资产维护都天然有较强结构。对开放式战略、创意和跨部门政治协调，agent logic 能缩小空间，但未必能直接产生正确判断。

### 3. 对标

- **与 [[Agent-Harness]] 对标**: agent logic 把 harness 从“模型调用与工具循环”推进到“企业流程逻辑层”，强调 harness 内应承载图谱、程序分析、策略执行和验证循环。
- **与 [[Verifiable-Agent-Engineering]] 对标**: agent logic 是可验证 Agent 工程的企业版本：把程序分析、图遍历、policy-as-code 和结构化证据链作为 LLM 外部的确定性骨架。
- **与 [[Enterprise-AI-Factory]] 对标**: AI factory 解决组织如何规模化生产 AI 能力；agent logic 解释这条生产线内部应如何把领域约束做成可复用软件原语。
- **与 [[AI-Deployment-Valley-of-Death]] 对标**: agent logic 可能降低从 pilot 到 production 的死亡谷风险，因为它减少上下文成本、幻觉空间和不可审计决策。

### 关联概念

- [[Agent-Logic]]
- [[Local-Bounded-Reasoning]]
- [[Policy-as-Code-for-Agent-Governance]]
- [[Graph-Guided-Agent-Investigation]]
- [[Agent-Harness]]
- [[Verifiable-Agent-Engineering]]
- [[Enterprise-AI-Factory]]
