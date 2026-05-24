---
type: source-summary
title: "MachinaCheck: Building a Multi-Agent CNC Manufacturability System on AMD MI300X"
source_raw:
  - "[[MachinaCheck Building a Multi-Agent CNC Manufacturability System on AMD MI300X]]"
created: 2026-05-24
updated: 2026-05-24
tags:
  - source-summary
---

# MachinaCheck: Building a Multi-Agent CNC Manufacturability System on AMD MI300X

## 编译摘要

### 1. 浓缩
- **核心结论1**: CNC 小型车间可制造性分析完全依赖人工（30-60 分钟/图），MachinaCheck 用 5 组件多 Agent 流水线在 30 秒内完成，消除人工判断误差
  - 关键证据: 10-20 RFQ/周 × 30-60 分钟 = 5-20 小时/周人工投入；STEP 文件通过 cadquery（OpenCASCADE）精确解析几何特征，100% 数学精度
- **核心结论2**: 制造业客户 NDA 要求 STEP 文件（专有几何 IP）不能离开本地——AMD MI300X（192GB HBM3）使本地运行 Qwen 2.5 7B 成为隐私合规的必要条件
  - 关键证据: 零字节 STEP 几何数据外传；gpu-memory-utilization 0.5 仅用 96GB，留充足余量；推理延迟 < 3 秒
- **核心结论3**: "选择性 LLM 使用"是关键架构决策——只在需要推理的地方用 LLM（操作分类/可行性决策/报告生成），数据库查询用纯 Python（工具匹配），避免不必要的延迟和幻觉风险
  - 关键证据: Agent 2（工具匹配）是纯 Python 数据库查询，不用 LLM；全流水线 25-40 秒端到端

### 2. 质疑
- **关于"正确性"的质疑**: 文章称"correct manufacturability assessment on all test parts"，但未给出测试零件数量、复杂度分布、与人工评估的对比。7B 模型对复杂 5 轴加工零件、非常规材料的推理能力存疑
- **关于可扩展性的质疑**: 当前仅支持 3 个输入（材料、公差、螺纹规格），真实车间场景还包括表面处理、热处理、装配约束等，Qwen 2.5 7B 的领域知识深度是否足够？
- **关于成本的质疑**: MI300X 硬件成本未提及，对小型车间而言本地部署的 ROI 需要量化——对比云 API 的成本节省 vs 硬件投入

### 3. 对标
- **跨域关联1**: 与 [[OncoAgent A Dual-Tier Multi-Agent Framework for Privacy-Preserving Oncology Clinical Decision Support]] 高度相似——两者都是"多 Agent + 本地推理 + 隐私合规"架构，只是领域不同（医疗 vs 制造）
- **跨域关联2**: "选择性 LLM 使用"模式与 [[Agentic-Engineering]] 中"LLM 只在需要推理处使用"的工程原则一致——Agent 2 纯 Python 是对这一原则的直接实践
- **跨域关联3**: 硬件选择逻辑与 [[Hardware-Sovereignty]] 概念直接对应——MI300X 的 192GB HBM3 使隐私合规的本地推理成为可能

### 关联概念
- [[Hardware-Sovereignty]]
- [[Agent-Orchestration]]
- [[Agentic-Engineering]]
- [[Dual-Tier-LLM-Architecture]]
