---
type: source-summary
title: "Analyzing technical documents with Deep Review"
canonical_url: "https://research.google/blog/analyzing-technical-documents-with-deep-review/"
raw_state: index
original_raw_file: "20261014-google-deep-review.md"
original_body_sha256: "9a3a68175cf8c97491b49badf19fd14df0df5ce0940e20fd011240906042bb03"
indexed_at: "2026-10-22T16:52:33+08:00"
created: 2026-10-22
updated: 2026-10-22
tags:
  - source-summary
  - verification
  - technical-review
  - multi-agent
  - scientific-review
evidence_level: medium
claim_type: mixed
source_locator:
  - "Raw L13-L40：validation bottleneck、16,000+ opt-in manuscripts、产品范围与数据政策"
  - "Raw L42-L63：74,000+ conference submissions、review burden、Deep Review 的逻辑/数学/grounding 任务边界"
  - "Raw L70-L87：四阶段 agentic pipeline：segmentation、adaptive budgeting、parallel verification、global synthesis/grounding"
  - "Raw L89-L106：从论文扩展到 design/presentation/legal/finance；Antigravity Teamwork pattern"
  - "Raw L108-L132：public/API 使用、human reviewer 定位与后续 multi-file 方向"
---

# Analyzing technical documents with Deep Review

> Google Research 于 2026-10-14 发布的 Deep Review 产品/研究总结。其前身 Paper Assistant Tool（PAT）已在 STOC 2026、ICML 2026、NeurIPS 2026、ICLR 2027 的 opt-in pre-submission 场景覆盖 16,000+ 篇稿件；本文同时描述公开版 Deep Review 的四阶段多 Agent 架构。来源适合支持系统设计、部署范围和 Google 自报使用数据；对 review correctness、跨领域泛化和相对专家质量仍需论文或独立评估，因此按 `medium / mixed` 处理。

## 编译摘要

### 1. 浓缩

#### 核心结论 1：生成吞吐增长正在把“验证容量”变成知识工作的独立瓶颈

Google 把问题明确命名为 **validation bottleneck**：AI 已显著压低论文、技术文档、代码和实验设计的生成成本，但专业 review 仍受人类时间与领域知识约束。本文给出的会议规模信号是：ICLR、NeurIPS、ICML 三会 2026 年合计投稿超过 74,000，较 2025 年约 45,000、2024 年约 32,000、2023 年约 23,000 持续上升。

**判断**：验证不是生成流程的尾部附属步骤，而正在成为需要单独扩容的 production system。这个趋势与软件工程中 coding throughput → CI/review bottleneck 同构，只是对象从 code artifact 扩展到 knowledge artifact。

#### 核心结论 2：长文档 review 的扩展方式不是“一个更长 prompt”，而是结构化分解 + 不均匀 compute allocation

Deep Review 的四阶段 pipeline：

1. **Document segmentation**：覆盖全文的逻辑分段，可重叠；
2. **Adaptive budgeting**：按 information density 给不同 section 分配不同 reasoning compute；
3. **Deep parallel verification**：多个 specialised agents 并行审查局部，同时保留 full-document context 以处理 cross-reference；
4. **Global synthesis and agentic grounding**：合并局部报告，重新检查跨段一致性，并做 external grounding/tool calls。

这把长上下文 verification 从“扩大一次推理”改写为 **hierarchical review scheduling**：分割检查对象、把算力放到高风险/高密度区域，再用全局 synthesis 恢复跨段一致性。

#### 核心结论 3：review agent 的合理自动化边界是 lower-level verification，不是替代 high-level judgment

Google 明确把 Deep Review 定位为处理 logical consistency、mathematical statements、fact grounding、prior-work comparison 和 improvement suggestions，同时把 higher-level judgments 留给人类。

**判断**：这与 [[Agent-Verification]] 的“verification capacity ≠ decision authority”一致。一个系统即使能扩大检查覆盖面，也不等于拥有论文价值、法律风险、商业意义或 scientific priority 的最终裁决权。

#### 核心结论 4：技术 review 是一种可迁移的 Agent workload，但迁移的是 review mechanics，不是领域 oracle

Google 将同一结构扩展到 design docs、presentations、legal/financial documents。可迁移的是：

```text
segment
→ allocate reasoning
→ local verification
→ cross-section consistency
→ external grounding
→ synthesized critique
```

不能直接迁移的是“什么算正确/重要”的领域标准。法律条款、财务解释、数学证明和系统架构需要不同 oracle、rubric 与责任人。

### 2. 证据边界

- 16,000+ 是 opt-in pre-submission feedback 部署规模，不是 16,000 个独立 correctness benchmark。
- 作者反馈“extremely positive”是产品方总结；本文没有给出完整 response rate、对照组或误报/漏报曲线。
- PAT feedback 与官方 conference review 明确 decoupled，因此不能把 pilot 使用等同于“AI 参与正式录用裁决”。
- Deep Review 公开版使用 Gemini 4 Argon，本文也明确旧 PAT pilot 与当前模型能力不同，历史 pilot 结果不能直接当作当前版本性能测量。

### 3. 跨来源综合

- 与 [[AI-Labor-Bottleneck-Shift]]：补充 knowledge-work review ceiling——生成量扩大后，人类专家验证吞吐成为 binding constraint。
- 与 [[Agent-Verification]]：给出文档域的 verification pipeline；验证覆盖可由 Agent 扩容，但高层 judgement 与责任没有自动转移。
- 与 [[Agent-Orchestration]]：segmentation + specialised parallel agents + synthesis 是 multi-agent orchestration 的具体验证型 topology。
- 与 [[Context-Engineering]]：每个局部 reviewer 同时需要 target segment 与 full-document cross-reference context，说明“局部专注”与“全局可恢复上下文”必须共存。

## 编译决策

暂不新增 `Deep Review` 或 `Validation Bottleneck` Entity：前者是单一产品，后者已有 [[AI-Labor-Bottleneck-Shift]] 与 [[Agent-Verification]] 两个成熟承载点。优先把本篇作为新的文档域一手证据编入现有结构。