---
type: output
title: "Delegative UI：慢速对话的认知经济学"
created: 2026-07-19
updated: 2026-11-28
status: published
tags:
  - interaction-design
  - human-agent-interaction
  - cognitive-science
  - organization
related_entities:
  - "[[Delegative-UI]]"
  - "[[Judgment-Degradation-Cascade]]"
  - "[[Flattening-as-Governance-Consequence]]"
  - "[[AI-Native-Testing]]"
---

# Delegative UI：慢速对话的认知经济学

> [!warning] 2026-11-28 知识消化修订
> 原文根据模型模拟圆桌与 think 推演形成。撤回错误心智模型必然指数增长、固定反馈周期、目标/路径可预判的充分必要条件、组织必然扁平化及学者真实背书等未经验证的命题。旧版由 Git 保留。

## 关键问题不是对话快慢，而是控制权如何分配

逐轮对话、直接操作、异步委派和主动通知可以组合。委派改变的是谁负责推进工作、何时需要用户判断、用户如何获得证据和介入。它不要求用户在开始时穷尽所有目标，也不等于只能事后验收。

对于明确任务，确定性程序可能比 Agent 更合适；对于路径不确定但探索边界明确的任务，也可以委派搜索、试验和方案比较。若目标仍在形成，应保留澄清和可逆试探。

## 交互经济学：降低摩擦，也降低失控成本

| 交互方式 | 可能收益 | 需要检查的成本 |
|---|---|---|
| 逐轮协作 | 快速澄清与纠正方向 | 等待、切换、重复确认 |
| 有界委派 | 减少持续占用注意力，允许并行 | 歧义、发现偏差延迟、返工、接管 |
| 主动通知 | 及时暴露异常与变化 | 无关中断、重复提醒、遗漏真正紧急事项 |

不是反馈越快越好，也不是反馈越少越好。需要依据任务风险、信息价值和可恢复性选择反馈时机。错误假设可能传播，但也可能被后续证据纠正，不能预先指定固定乘法增长。

## 从一次委派到可验证闭环

- 约定目标、可用工具、权限、质量门和停止条件，不必提前指定所有实现细节。
- 对开放任务设置阶段产物，遇到实质歧义或高影响操作时升级。
- 结果验收检查实际状态及外部效果，不能以 Agent 自述代替证据。
- 允许暂停、重新规划与交接；取消、撤销、补偿分别设计。
- 主动通知支持合并、静默、频率控制和退出；通知率与点击率不等于用户价值。

## 如何验证设计

比较同一类任务在不同交互策略下的人工主动时间、交付周期、成功率、返工、错误发现延迟和接管成本。若涉及专业能力再生，应另测无 AI 条件下的保持与迁移。任务绩效、用户主观负担与能力保持是不同结局。

组织内，前提表达和验收能力可能改变实际影响力；正式责任、专业知识、协调职能和授权制度仍需单独分析，不从界面设计直接推出组织扁平化。

## 本文使用的 Wiki 页面

- [[Delegative-UI]]
- [[Agent-First-vs-Traditional-Automation]]
- [[Verifiable-Agent-Engineering]]
- [[Judgment-Degradation-Cascade]]
- [[Flattening-as-Governance-Consequence]]
- [[Permission-Ratchet-Mechanism]]

## 回填检查

| 判断 | 支撑依据 | 处理 |
|---|---|---|
| 交互方式、决策逻辑与授权深度可独立设计 | Wiki: [[Delegative-UI]]、[[Agent-First-vs-Traditional-Automation]] | 保留 |
| 验收真实结果、区分停止与撤销 | Wiki: [[Verifiable-Agent-Engineering]]、[[Permission-Ratchet-Mechanism]] | 保留 |
| 延迟是否导致长期判断力下降 | Wiki: [[Judgment-Degradation-Cascade]] | 补 source（待实测） |
| 固定级联公式及必然组织扁平化 | 无独立实证 | 不处理（撤回普遍命题） |

历史来源：2026-07-17 至 07-19 模拟圆桌、think 与 qa 综合；不是被模拟学者的真实发言记录。
