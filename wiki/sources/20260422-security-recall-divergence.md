---
type: source-summary
title: "Omission Constraints Decay While Commission Constraints Persist in Long-Context LLM Agents"
source_raw:
  - "[[20260422-security-recall-divergence]]"
canonical_url: "https://arxiv.org/abs/2604.20911"
raw_state: full
source_locator:
  - "4,416 trials / 12 models / 8 providers / six conversation depths"
  - "omission vs commission constraint asymmetry under schema/context pressure"
  - "formatting proxy limits; Arm C token-matched control only on two models"
created: 2026-09-20
updated: 2026-09-20
tags:
  - source-summary
  - agent-security
  - verification
evidence_level: medium
claim_type: mixed
---

# Omission Constraints Decay While Commission Constraints Persist in Long-Context LLM Agents

## 编译摘要

### 1. 浓缩

- **核心结论 1：控制状态“仍在上下文里”不保证禁止型规则仍被可靠执行。**
  - 论文把 suppression/prohibition 类 omission constraints 与 requirement 类 commission constraints 分开；在部分模型中前者随上下文压力明显衰减，而后者继续保持高合规。
- **核心结论 2：正常的正向审计信号可能掩盖禁止规则失效。**
  - Mistral Large 3 的示例中，omission compliance 从 turn 5 的 73% 降至 turn 16 的 33%，同时 commission compliance 保持 100%。
- **核心结论 3：可定义每模型/约束的 Safe Turn Depth，但它只是当前实验下的运行阈值。**
  - 周期性重新注入约束可恢复测得合规；token-matched Arm C 在两个模型上显示 schema semantic content 解释 62–100% dilution effect。

### 2. 质疑

- 八类约束全部是 formatting/style proxy，并通过 string/regex 判定；真实“不得泄露 credential / 不得执行未授权代码”等语义安全规则的相同衰减率尚未验证。
- Arm C 只覆盖 Gemini 2.5 Flash 和 Llama 3.3 70B，不能把 62–100% 的机制归因外推到全部 12 个模型。
- sandbox 工具输出是 deterministic mock data，没有真实外部 effect 或 provider post-state。

### 3. 对标

- 对 EX-006：补上 **carrier present but inhibitory control weakened**；它与 Governance Decay 的“约束被 compaction 删除”不同，也与 Sleeper Memory 的“恶意状态被写入”不同。
- 对 CR-004：只监控 commission/positive signals 可能得到“系统仍正常”的假象；需要单独观察 omission/prohibition control。
- 对 [[Agent-Security]]：长程 session 应把 control replay/preflight 与 action-boundary enforcement 分开；Safe Turn Depth 只能作为上下文层运行信号，不能替代确定性 guard。

## 关联概念

- [[Agent-Security]]
- [[Context-Rot]]
- [[Constraint-Infrastructure]]
- [[Verifiable-Agent-Engineering]]
