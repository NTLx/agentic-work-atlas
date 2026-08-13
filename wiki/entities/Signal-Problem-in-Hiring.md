---
type: entity
title: Signal Problem in Hiring
aliases:
  - Signal Problem in Hiring
  - 招聘信号问题
  - Interview Signal Problem
definition: "传统技术面试只能收集几小时的信号，却要做出持续数年的招聘决策，导致假阳性和假阴性率居高不下"
created: 2026-05-31
updated: 2026-08-13
evidence_level: medium
claim_type: mixed
tags:
  - hiring
  - software-engineering
  - decision-making
related_entities:
  - "[[Campfire-Hiring]]"
  - "[[Steve-Yegge]]"
  - "[[Decision-Quality]]"
source_raw:
  - "[[20260529-last-technical-interview]]"
  - "[[20260810-the-playbook-for-building-high-talent]]"
---

# Signal Problem in Hiring（招聘信号问题）

> [!definition] 定义
> **Signal Problem in Hiring** 是传统技术面试的根本缺陷：面试只能收集"几小时的信号"，却要做出持续数年的招聘决策。这导致公司"招了大量假阳性（不合格者）"同时"拒绝了合格的候选人"。

## 信号链条断裂

Yegge 识别了招聘信号链条中的四个断裂点：

| 信号来源 | 问题 | 现状 |
|---------|------|------|
| 简历 | 信噪比差 | AI 写作进一步恶化 |
| 电话筛选 | 曾是较好的信号 | 已被淘汰/过时 |
| 现场面试 | "和真实工作出了名的不像" | 仍是主流 |
| 离线评估 | 编码测试 | AI 作弊毒化 |

## 系统性修复的失败

大公司已经意识到信号问题，但所有修复都是打补丁：

- **Amazon Bar Raiser**：专门角色来保证招聘质量——存在本身就说明"你不能信任面试团队"
- **Microsoft As-Appropriate**：类似机制
- **Google Hiring Committee**：匿名审查面试包——实验发现否决了 2/3 的候选人，包括面试官自己被面试时的包

Yegge 的结论：这些修复都没有改变根本流程——"短时间面试"这个模式 50 年没有本质变化。

## 关键数据点

- Google Hiring Committee 审查匿名面试包后否决约 2/3——而这些正是面试官们自己被面试时的包
- Amazon 和 Microsoft 分别设立 Bar Raiser 和 As-Appropriate 角色来弥补面试团队的判断缺陷
- 简历 AI 写作和编码评估 AI 作弊同时恶化了信号质量

## 另一视角：Funnel of Doom 与 Work Sample（Adam Ward，2026-08）

Signal Problem 不止存在于"评估环节"，也存在于"候选池环节"。Adam Ward（Cursor 招聘负责人）提出 **funnel of doom**：传统招聘先 reach 100 人 → 20% 回复 → 逐级剔除 → hire 剩余者。"回复你的 20% 是你抓到他们倒霉天的 20%，不是 top 20%"——**remainder hiring 从源头就是有偏样本**，且随时间回归均值。解法是把信号问题前移：先定义 top 1% 是什么（scoping）→ mapping 全世界 50 人 → relentless pursuit（把每个 hire 当高管招聘），"atomic unit of hiring 是 person，不是 job spec"。

对"评估信号"环节，Ward 与 Yegge 完全收敛：**work sample 是预测力最高的信号**，Cursor 用长时真实工作（side-by-side 项目、围绕餐食、精编见面人选）替代提问式评估；Michael Terrell 曾移除 work trial 后"signal 完全崩溃"，被迫恢复。这给 Signal-Problem 提供了正向解法样本：把信号窗口从"几小时模拟"拉到"几天真实工作"。

## 前提与局限性

- Yegge 的分析基于美国大型科技公司（Google、Amazon、Microsoft）的经验，可能不适用于初创公司或非科技行业
- "信号问题"的严重程度取决于岗位类型——对于高度标准化的角色（如前端开发），面试信号可能比 Yegge 描述的更强
- 面试的信号问题可能被夸大：有研究表明结构化面试的预测效度实际上相当高（约 0.51）

## 关联概念

- [[Campfire-Hiring]] — 对信号问题的系统性解决方案
- [[Steve-Yegge]] — 问题识别者
- [[Decision-Quality]] — 更广泛的决策质量问题：如何在有限信息下做出高质量决策
