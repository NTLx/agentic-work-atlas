---
type: comparison
title: Convergence vs. Generation
created: 2026-06-10
updated: 2026-11-28
evidence_level: medium
claim_type: synthesized
tags:
  - Agentic-Engineering
  - methodology
source_raw:
  - "[[20260610-qwen-constraint-driven-engineering-experiment]]"
---

# Convergence vs. Generation（收敛 vs. 生成）

本比较把两种工程取向抽象为“生成式”与“收敛式”。它主要来自 Qwen 的约束驱动实验与本库综合，用于分析质量控制方式；不是已经被跨项目验证的普遍“范式转移”定律。

| 维度 | 生成式（Generative） | 收敛式（Convergent） |
|------|---------------------|----------------------|
| **设计重心** | 候选产物生成与选择 | 有效判据、反馈与有界修正；并非约束越多越好 |
| **逻辑起点** | 模型一次性产出结果 | Harness 驱动多轮迭代 |
| **错误处理** | 可以重生成或审阅 | 基于真实失败反馈修正，必要时停止或升级 |
| **成功判据** | 语义相似度、肉眼观察 | [[Automated-Criteria\|自动化判据]]（协议、产物、环境） |
| **典型代表** | Vibe Coding、简单 Copilot | [[Constraint-Driven-Engineering\|约束驱动工程]]、Qwen 实验 |

## 核心差异

### 1. 质量的来源
- **生成式**：更依赖模型单轮能力与提示质量，验证环较弱。
- **收敛式**：把测试、约束、反馈与重试作为显式控制环，通过不断排除无效路径提高交付稳定性。Qwen 实验把这一思路概括为“质量由闭环收敛出来”；该表述目前应视为工程方法论主张。

### 2. 人类/Harness 的角色
- **生成式**: 人类是“提示词工程师”，通过调整输入来寻找最佳输出。
- **收敛式**: Harness 是“控制系统”，通过注入硬约束（如 [[Pixel-Facts\|像素事实]]）和分层验收，强制系统向目标状态逼近。

### 3. 长程任务的鲁棒性
生成与收敛并非互斥：迭代仍需生成候选，单轮生成也可被独立验收。[[20260610-qwen-constraint-driven-engineering-experiment]] 报告的是隔离环境中使用种子数据的双端应用能力验证，单端约 4 小时，并非跨项目生产可靠性或多天成功率对照。原文还明确指出更多模糊约束可能诱导哄骗校验，模型指令遵循是前提。退役“约束越严越收敛”的旧命题；保留正确的判据、代表性环境、预算与停止条件、真实终态验证等候选工程机制。循环可能收敛到错误目标，也可能无法收敛。
