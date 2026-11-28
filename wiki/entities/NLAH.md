---
type: entity
title: NLAH
aliases:
  - NLAH
  - Natural-Language Agent Harnesses
  - 自然语言智能体驾驭层
definition: "将 Agent 驾驭策略从代码中外置为可执行的自然语言文档，由智能驾驭运行时（IHR）解释执行，使驾驭模式可检视、可移植、可消融"
created: 2026-06-13
updated: 2026-11-28
evidence_level: medium
claim_type: extracted
tags:
  - agent-harness
  - research
related_entities:
  - "[[Agent-Harness]]"
  - "[[Harness-Engineering]]"
  - "[[Context-Rot]]"
  - "[[Multi-Layer-Memory]]"
  - "[[Thin-Harness-Fat-Skills]]"
source_raw:
  - "[[20260613-NLAH-natural-language-agent-harnesses]]"
---

# NLAH（Natural-Language Agent Harnesses）

> [!definition] 定义
> 将 Agent 驾驭策略从代码中外置为可执行的自然语言文档，由智能驾驭运行时（IHR）解释执行，使驾驭模式可检视、可移植、可消融。

## 关键数据点

- **核心论文**: Pan et al., [Natural-Language Agent Harnesses, arXiv:2603.25723v2](https://arxiv.org/html/2603.25723v2)（2026-05-18）；本库Raw为6月13日二手解读，本轮直接核对论文§4–5、Tables 1–5。
- **任务结果（Table 1）**：按原代码/普通Prompt/IHR分别报告 SWE Verified 67.0/77.0/73.0；TB2 36.0/57.3/53.9；OSWorld 47.1/47.9/46.3。结果支持特定实现可行，不是统计等效检验；IHR未超过普通Prompt。
- **静态表示（Table 2）**：Live-SWE 60.1k→2.9k、MHTBA 10.5k→0.8k、SeeAct 47.5k→1.4k token；统计审计过的代码材料与策略文件，不是整个系统代码量或实际推理token。
- **代价**：当前原型常有额外调用/Token，但依配置不同；Live-SWE NLAH实际用时6.1分钟、原代码28.9分钟，不能概括为所有成本都增加。
- **模块干预（Table 5）**：在各自 Basic 条件上逐个添加模块，而非从完整配置逐个删除。SWE/OSWorld百分点变化：文件状态+2.6/+13.9，证据回答+2.8/+2.8，自我进化+5.8/+8.4，多候选−1.6/+2.8，压缩−1.0/−8.3，Markdown记忆−2.8/+5.6。仅支持这两个任务和当前运行条件的增量，未证明模块独立或普遍负收益。

## 四层架构

| 层 | 职责 | 比喻 |
|---|------|------|
| 基础智能体 | 最小 agent 循环（LLM + 终端工具），不含任务逻辑 | 马 |
| 运行时策略（IHR） | 固定 NL 指令，读取 NLAH 文档、调度子 agent、管理状态 | 骑手 |
| NLAH 文档 | 可替换的自然语言驾驭策略（阶段、角色、状态、验收、恢复、停止） | 路线图 |
| 脚本与适配器 | 确定性硬逻辑（JSON schema 校验、diff 计算、格式转换） | 信号灯 |

## 三种驾驭方式谱系

作者Fig.1给出的概念谱系（不是跨系统可测量的全序）：
1. **代码驾驭层（Code Harness）**: 程序逻辑硬性控制，最强确定性但策略与实现交织
2. **NLAH + IHR**: 自然语言承载策略 + 运行时解释执行，放弃硬确定性但获得可编辑性和可消融性
3. **自驾驭（Self-Harnessing）**: 控制器模型直接驾驭其他模型，无外部驾驭层

## 前提与局限性

- **前提**: NLAH 假设驾驭策略可以被自然语言充分精确地表达，且 LLM 能忠实遵循
- **机制遵循不均**：Table 4 的IHR artifact contract约1.00/0.96、handoff recall约0.32/0.55（Live-SWE/MHTBA）；Prompt为直接上下文、IHR为父子交接，指标口径需区分。高契约符合率不等于安全或整体正确。
- **自然语言不精确性**: 语义约束可能被欠定义、被不同模型不同解读
- **安全风险**: 可移植的驾驭逻辑可能降低传播危险工作流的门槛；驾驭层中介工具使用，可能引入提示注入和供应链污染攻击面

## 关联概念

- [[Agent-Harness]] — NLAH 是 Harness 的一种新范式表达
- [[Harness-Engineering]] — NLAH 使 Harness 工程从代码层上升到策略层
- [[Context-Rot]] — 该实验的压缩配置在两个任务上表现下降，不外推所有压缩策略
- [[Thin-Harness-Fat-Skills]] — NLAH 四层架构的关注点分离与此设计哲学相似
