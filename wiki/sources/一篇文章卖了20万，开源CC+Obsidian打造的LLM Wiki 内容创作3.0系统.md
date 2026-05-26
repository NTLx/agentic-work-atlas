---
type: source-summary
title: "一篇文章卖了20万，开源CC+Obsidian打造的LLM Wiki 内容创作3.0系统"
source_raw:
  - "[[一篇文章卖了20万，开源CC+Obsidian打造的LLM Wiki 内容创作3.0系统]]"
created: 2026-05-24
updated: 2026-05-25
tags:
  - source-summary
  - llm-wiki
  - knowledge-compilation
  - content-system
---

# 一篇文章卖了20万，开源CC+Obsidian打造的LLM Wiki 内容创作3.0系统

## 编译摘要

### 1. 浓缩

- **核心结论1**: 内容创作 2.0 的瓶颈不是写作自动化，而是底层知识库仍然是“信息垃圾场”。
  - 关键证据: 作者描述自己的 2.0 系统能管理 4 个矩阵公众号、35 个 AI 技能包，覆盖选题、写稿、评审、排版、发布和短视频拆条；但三个月后发现 200 多篇资料中存在同问不同答、37 处概念定义冲突、4 处事实矛盾、60 多篇从未被引用。
  - 关键含义: 自动化写作只能放大已有知识质量。若知识层混乱，输出层会更快地产生不一致、幻觉和重复。
- **核心结论2**: LLM Wiki 的关键转变是从 runtime RAG 转向 compile-time Wiki：知识在使用前就被编译、消歧、链接和维护。
  - 关键证据: 作者对比 NotebookLM、ChatGPT 文件上传式的“提问时才翻”和 Karpathy 的 LLM Wiki：原始文档先被编译成 summaries、concepts、methods、indexes，再在新资料加入时增量更新。
  - 关键机制: raw 只读，wiki 承载结构化知识；LLM 不是每次临时拼答案，而是持续维护一个可复用的语义层。
- **核心结论3**: 三步编译法的价值在于让摘要产生判断：浓缩提核心，质疑暴露前提，对标生成迁移。
  - 关键证据: 作者认为 Karpathy 原方案如果只做摘要，可能把两篇相反文章压成相似结论；质疑步骤能指出数据的市场、样本和条件限制，对标步骤能把 AI 多步推理失控与供应链多环节可靠性下降联系起来。
  - 对本库的意义: 这篇文章与本仓库的工作流高度同构，尤其支持 source summary、entity、topic、comparison 与 audit 之间的知识复利循环。

### 2. 质疑

- **关于“卖 20 万”的质疑**: 销售结果属于个案，受账号基础、产品、流量窗口、信任资产和定价影响，不能直接作为 LLM Wiki 方法可复制的证据。
- **关于“维护成本接近零”的质疑**: LLM 能降低交叉引用、定义合并和冲突标注的成本，但并不会让审计成本消失。越是要卖知识资产，越需要人工确认事实、边界和责任。
- **关于目录结构的质疑**: 文中 `summaries/concepts/methods/indexes` 结构适合内容团队，但本库采用 `sources/entities/topics/comparisons/outputs`，更强调 source 可追溯、稳定概念、主题综合和输出回填。
- **关于 raw 不可变性的质疑**: 作者展示的 3.0 已经接近本库原则，但实际执行中仍要明确禁止向 raw 追加分析，否则证据层和解释层会混在一起，长期破坏可审计性。

### 3. 对标

- **对标 [[LLM-Wiki]]**: 本文是 LLM Wiki 方法在中文内容生产场景的实践化版本，提供了从 Runtime RAG 到 Compile-time Wiki 的业务动因。
- **对标 [[Knowledge-Compilation]]**: 三步编译法说明知识编译不是摘要，而是把原文转化成可复用判断、前提边界和跨域关系。
- **对标 [[RAG-vs-LLM-Wiki]]**: 文章给出清晰区分：RAG 在查询时检索资料，LLM Wiki 在资料进入系统时就完成编译和链接。
- **可迁移场景**: 内容矩阵、行业研究库、客户知识产品、内部 onboarding、销售 enablement、投研资料库。共同前提是资料会被反复复用，且概念冲突会真实影响输出质量。

### 关联概念

- [[LLM-Wiki]]
- [[Knowledge-Compilation]]
- [[RAG-vs-LLM-Wiki]]
- [[Context-Engineering-vs-Knowledge-Compilation]]
- [[Agent-Knowledge-Management]]
