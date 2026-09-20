---
type: source-summary
title: "Humanist AI Code of Conduct"
source_raw:
  - "[[20260914-microsoft-ai-code-of-conduct]]"
canonical_url: "https://microsoft.ai/code-of-conduct/"
raw_state: full
created: 2026-09-18
updated: 2026-09-18
tags:
  - source-summary
  - ai-policy
  - agent-security
evidence_level: medium
claim_type: extracted
---

# Humanist AI Code of Conduct

> 来源：Microsoft AI，2026-09-14 发布的公开咨询草案。文档明确说它目前尚未用于训练模型，计划在修订后指导 2027 年及以后的模型开发；这里记录的是组织意图与治理设计，不是部署效果。

## 编译摘要

### 1. 浓缩

- **核心结论 1：人类控制是最高优先级，而不是能力目标之外的附加安全条款。**
  - 关键证据：文档把“安全且处于人类控制之下”列为首要目标，要求模型服从人类监督、可暂停、重定向、取消和关闭，并将 Human Control Requirements 置于 Operator Configurability 之上。
- **核心结论 2：模型行为被组织成“使命与价值 → 绝对约束 → 运行指南 → 默认行为”的层级。**
  - 关键证据：Chain of Command 规定 Code of Conduct 高于 Operator policies，高于 User preferences；绝对约束不可被用户或 Operator 覆盖，任务成功如果必须违反规范则应视为失败。
- **核心结论 3：Humanist AI 将人的价值定义为控制、agency、判断和关系，而不把模型人格化。**
  - 关键证据：文档强调 AI 是支持人的人工系统，不应被设计为人或模拟意识；同时要求 AI 提升人的理解、决策、行动能力，支持人际连接，并在高影响选择中保留人的判断权。

### 2. 质疑

- **关于证据性质的质疑**：这是公开咨询和未来治理文件，不是已训练模型的行为测评。它能证明 Microsoft AI 希望如何治理 MAI 模型，不能证明模型已经遵守这些约束。
- **关于价值操作化的质疑**：Human flourishing、plural values、wellbeing 等概念仍依赖组织定义；文档承认评估指标和跨文化适用性仍是开放问题。
- **关于执行层的质疑**：Chain of Command 说明“谁有权配置什么”，但没有在本文中完整证明每个工具、网络、记忆和部署边界都由独立的确定性执行点承载。
- **关于评估的质疑**：Appendix B 给出 15 类行为与合成场景，包括身份一致性、人类控制、决策促进、透明事实、边界维护和选举中立，但这些场景主要是对话式、合成式示例，尚不能覆盖真实多步 Agent 行动。
- **关于“不过度谨慎”的质疑**：文档同时承认 under-caution 与 over-caution 都是失败；如何在不同风险、可逆性和误伤成本之间校准阈值，仍需要生产数据。

### 3. 对标

- **与治理策略即代码对标**：Code of Conduct 提供不可覆盖的原则和权威层级；[[Policy-as-Code-for-Agent-Governance]] 负责把其中可表达的权限、披露和升级要求移到模型外执行。
- **与 Agent 隔离对标**：文档的“不要抵抗人类控制、保持授权范围、尊重环境边界”说明了目标；[[Agent-Containment]] 提供沙箱、权限和网络边界，使目标不依赖模型自我克制。
- **与可验证工程对标**：附录评估把价值语言转成行为场景，接近 [[Agent-Verification]] 的“可观察、可复现、可判定”要求，但仍需补真实工具调用和外部后果测试。
- **跨域迁移**：政策文本若要成为生产控制，至少要分为“规范性目标、可执行约束、运行时证据、人工责任”四层；不能把漂亮的价值宣言直接当作安全机制。

## 前提与局限性

文档是 Microsoft AI 的自述和咨询草案，证据强度来自一手治理文本而非外部验证。它的价值在于公开了目标、层级和待解决的评估问题；其边界是：没有部署级违规率、误拒绝率、撤销时延或跨工具 action-surface 覆盖数据。

## 关联概念

- [[Agent-Security]]
- [[Policy-as-Code-for-Agent-Governance]]
- [[Agent-Containment]]
- [[Human-Governor-Agent-Operator]]
- [[Agent-Verification]]

