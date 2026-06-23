---
type: entity
title: Skill-Chains
aliases:
  - Skill Chains
  - 技能链
  - Macro Skill
definition: "将多个 skill 按顺序串联为 macro skill 的执行模式——skill 1 的输出作为 skill 2 的输入，实现端到端工作流。核心价值是通过 QA skill 约束幻觉，让 agent 产出基于真实数据而非模型编造。LCA (2026) 的提案 skill chain = 构建微站 → 文案打磨 → QA 审查。"
created: 2026-06-23
updated: 2026-06-23
evidence_level: medium
claim_type: mixed
tags:
  - skill-engineering
  - agentic-engineering
  - workflow
related_entities:
  - "[[Skill-Internalization]]"
  - "[[Progressive-Disclosure]]"
  - "[[Validation-Pipeline]]"
  - "[[Agent-Loops]]"
  - "[[Thin-Harness-Fat-Skills]]"
  - "[[Agentic-Engineering]]"
source_raw:
  - "[[20260608-become-ai-native-org]]"
---

> [!definition] 定义
> Skill Chain 是一个 macro skill，内部按顺序触发多个子技能。每个子技能的输出成为下一个的输入，形成端到端工作流。关键区别：不是让一个 skill 做所有事，而是让每个 skill 专注一个环节，通过串联提升整体质量。

## 核心模式

```
Skill 1: Build → Skill 2: Polish → Skill 3: QA → Output
```

LCA 的提案 skill chain 实例：

| 顺序 | Skill | 职责 | 约束 |
|------|-------|------|------|
| 1 | Proposal Microsite | 构建品牌化提案微站 | 基于客户 context 个性化 |
| 2 | Copy Polish | 打磨文案，确保语气一致 | 匹配团队声音，不像 AI |
| 3 | QA Review | 审查每个声明的来源 | 确保来自会议记录和数据 |

## 关键数据点

- **幻觉约束**: QA skill 确保每个声明来自会议记录和数据，降低"fake it until you make it"风险
- **个性化注入**: 从过去会议记录中提取个人化时刻（如 Maya 的唱片店隐喻），将速度转化为信任
- **触发方式**: 可自动触发（cron job 检测到 RFP 请求）或手动触发
- **产出速度**: 正常提案流程 3 天，skill chain 几分钟
- **与 Agent 自主性的关系**: Skill chains 让 agent 从 Level 2（等待批准）升级到 Level 3（完全自主运行数天）

## 与单次 Skill 的区别

| 维度 | 单次 Skill | Skill Chain |
|------|-----------|-------------|
| 复杂度 | 单一任务 | 端到端工作流 |
| 质量控制 | 依赖单次输出 | 每个环节专注+最终 QA |
| 幻觉风险 | 高（无约束） | 低（QA skill 验证来源） |
| 可复用性 | 低（特定场景） | 高（可按需组合） |
| 自主性 | 需要人监督 | 可无人值守运行 |

## 前提与局限性

- **依赖前置 Context**: Skill chain 的产出质量直接依赖 context 层（[[Company-Brain]]）的丰富度和准确性
- **QA skill 的覆盖率**: QA 只能检查已知规则（如"声明必须来自会议记录"），无法检测所有类型的幻觉
- **顺序执行延迟**: 多 skill 串联增加总执行时间，复杂 chain 可能需要数分钟
- **错误传播**: 上游 skill 的错误输出会被下游 skill 当作输入，可能放大错误
- **编排复杂度**: 管理 skill 间的依赖、输入输出格式和错误处理增加工程成本

## 关联概念

- [[Skill-Internalization]] — 吸收而非安装 skill，是 skill chain 中每个子技能的质量保证
- [[Progressive-Disclosure]] — Skill chain 中的每个 skill 按需加载，不一次性塞进 context
- [[Validation-Pipeline]] — QA skill 约束幻觉与对抗性审查是同一思路
- [[Agent-Loops]] — Skill chain 可嵌入 agent loop 中循环执行
- [[Thin-Harness-Fat-Skills]] — Skill chain 是 fat skills 的具体实现形式
- [[Company-Brain]] — Skill chain 的产出质量依赖 context 层
