---
type: topic
title: CEO 亲手用 AI
description: "高管直接AI实践、组织学习、原型治理与生产验收之间的候选关系及证据边界"
created: 2026-06-01
updated: 2026-11-28
evidence_level: medium
claim_type: mixed
tags:
  - management
  - ceo-ai-hands-on
  - founder-mode
  - vibe-coding
related_entities:
  - "[[Paul-Graham]]"
  - "[[Guillermo-Rauch]]"
  - "[[Founder-Mode]]"
  - "[[Vibe-Coding]]"
  - "[[Coding-Agents]]"
  - "[[Forward-Deployed-Engineer]]"
  - "[[AI-Psychosis]]"
  - "[[Agentic-Engineering]]"
source_raw:
  - "[[20260530-ceo-knee-deep-building-ai]]"
---

# CEO 亲手用 AI（CEO Hands-On AI）

> [!definition] 主题描述
> CEO亲手用AI是管理者获取直接经验的一种学习方式，而非所有CEO必须写代码的普适规律；区分直接体验、生产交付、资源分配及授权责任。

## 原始争议与证据身份（2026-11-28）

- Graham 2026-05-30 X帖倡导深度参与；其同期邮件态度是个人沟通偏好。Rauch 5-31帖以客户私信及PLG解释企业采用，同时明确趋势能否持续未知。两帖按原Raw保存，本轮未独立打开X原帖，不以浏览量证明代表性。
- **作者勘误**：[Dear Vibe-Coding CEO: Please Stop](https://aboard.com/dear-vibe-coding-ceo-please-stop/) 2026-05-20正式页面署名Rich Ziade，而非Paul Ford（文中引用合伙人Ford）。Ziade警告周末原型成为高管指令、后续工程负担被忽略；他也理解CEO亲自尝试的动机。与Graham/Rauch的主张可以互补，而非必须二选一。
- [Forbes 2026-03-17](https://www.forbes.com/sites/richardnieva/2026/03/17/vercel-guillermo-rauch/) 报道Vercel使用Claude的客户略高于1%、部署量近15%；2025-06至2026-02 agent相关部署近5%至超过21%，后者近70%来自Claude Code。平台历史自报经媒体转述，不是CEO占比、生产率、质量或全行业份额。
- Perez建议每位CEO配FDE，是原Raw中的聚合转引观点，不是岗位配置必要条件。Founder Mode原文也未定义统一参与深度，见 [[Founder-Mode]]。

## 组织治理设计（综合判断）

| 阶段 | 候选机制 | 验收对象 |
|---|---|---|
| 管理者直接体验 | 用真实但受控的任务、失败案例和必要支持形成认知 | 是否能识别能力/风险/成本边界，而非使用时长 |
| 探索性原型 | 清楚标记实验性质、权限、数据与预算 | 是否回答业务问题、是否可复现 |
| 产品/工程决策 | 原型不自动进入backlog；责任人可拒绝、重做或停止 | 用户价值、替代方案、总成本、维护及安全 |
| 实际运行 | 经过既有质量门、上线授权、监控、回退及实际效果检查 | 验收成功、失败/返工/维护成本和用户结果 |

高管直接实践、专业团队演示、现场观察及独立评估均可提供学习证据。选择与角色、企业阶段、任务风险、时间机会成本有关；不因职级跳过既有质量门。

## 关键数据点与反向证据

- [BetterUp×Stanford](https://www.betterup.com/workslop) 2025-09在线调查1,150名美国全职desk workers，官网40%过去一月收到workslop（HBR版摘要41%，未统一版本）；不是定期发生率，也非CEO原型专门调查。53%恼火与另篇53%自报曾发送属于不同题目，不能混用。主观估计、样本选择及未测实际业务结果限制外推。
- [Ohio State 2023](https://news.osu.edu/ai-can-help-write-a-message-to-a-friend--but-dont-do-it/) 208名成人在线情景研究，AI或他人帮助修改给朋友的消息均使投入努力的感知下降；非企业邮件或实际编码质量测量。
- [Bandiera et al., JPE 2020](https://doi.org/10.1086/705331) 6国1,114名CEO日程数据；行为类型与生产率相关，作者的匹配模型允许不同企业最适合不同CEO类型（[作者综述](https://www.nber.org/reporter/2023number1/ceos-and-firm-performance)）。非AI研究、不随机指派CEO或验证亲自编码。外部候选待晋升。

## 前提与局限性

原工厂主不碰机器即淘汰、Blockbuster因CEO不使用互联网而失败、Linux因参与而成功等类比未识别因果，退役稳定身份。高管的能力外推可直接用[[AI-Capability-Gap]]及验收结果描述，不用临床标签解释工作判断。更多接触AI既可能校准也可能强化偏差。未找到直接比较高管是否亲自编码与企业AI成效的可靠因果研究；本页为候选治理设计，不是已经证实的最佳管理方式。

## 关联主题

- [[Karpathy-AI-Thought]] — AI 编程范式、能力鸿沟和知识管理的思想演化
- [[Agentic-Engineering-Patterns]] — Simon Willison 的 AI 编程代理工程范式指南
- [[Forward-Deployed-AI-Enablement]] — FDE 式 AI 赋能路径
- [[AI-Mediated-Organization]] — AI 中介组织的协作、权力、责任重塑

## 来源

- [[20260530-ceo-knee-deep-building-ai]] — Paul Graham 与 Guillermo Rauch 的原帖及衍生讨论
