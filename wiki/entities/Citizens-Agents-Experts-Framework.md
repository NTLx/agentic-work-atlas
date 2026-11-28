---
type: entity
title: Citizens Agents Experts Framework
aliases:
  - Citizens Agents Experts Framework
  - Citizens Build Agents Execute Experts Govern
  - CAE Framework
  - 三分法
definition: "Rachel Laycock (Thoughtworks CTO, 2026-08) 提出的 AI 时代价值流动框架——Citizens 任何能 turn ideas into working software 的人 + Agents 执行（write/refactor/test/fix/iterate）+ Experts 治理（架构/安全/韧性/operability/compliance/cost）；作者提出的价值流动视角，不是岗位分类；共享治理机制可能放大专家决策影响，未量化效果"
created: 2026-08-20
updated: 2026-11-28
tags:
  - organization
  - engineering-judgment
  - ai-era
  - framework
evidence_level: medium
claim_type: mixed
related_entities:
  - "[[Rachel-Laycock]]"
  - "[[AI-Era-Career-Skills]]"
  - "[[Captain-Mindset]]"
  - "[[AI-Native-Engineering-Org]]"
  - "[[Taste-vs-Judgment]]"
  - "[[Operational-Responsibility]]"
  - "[[Jevons-Paradox-for-Knowledge-Work]]"
  - "[[Agent-Adoption-Curve]]"
  - "[[Knowledge-Debt]]"
source_raw:
  - "[[20260820-rachel-laycock-citizens-agents-experts.md]]"
---

# Citizens Agents Experts Framework（公民·代理·专家三分法）

> [!definition] 定义
> **Citizens Agents Experts Framework** 是 Rachel Laycock（Thoughtworks CTO，2026-08）提出的 AI 时代价值流动框架——**Citizens**（任何能 turn ideas into working software 的人）+ **Agents**（执行：write/refactor/test/fix/iterate）+ **Experts**（治理：架构/安全/韧性/operability/compliance/cost）。不是 role 分类而是 value-flow 描述：作者认为 AI 扩大软件创造的可及性，Agent 可承担部分执行，专家治理可能获得杠杆；不是全部执行移交或组织结构定律。

## 三个 Buckets 的职责

| Bucket | 做什么 | 价值贡献 |
|--------|------|----------|
| **Citizens** | 把 ideas 转化为 working software（不限于工程师） | 扩展创造力的可及性 |
| **Agents** | write code、refactor、generate tests、fix bugs、iterate at speed | 执行速度的杠杆 |
| **Experts** | 决定 software 是否 deserve to exist in production；design guardrails、platforms、practices、feedback loops | judgment 的杠杆 |

## 与传统角色的区别

- **不是 role 分类**：citizens / agents / experts 表达三类贡献，不是固定阶段、角色或互斥权限
- **AI 降低部分创造门槛**：作者举周末应用案例；不能推出每个人都具备交付能力
- **Agents 承担部分 execution**：范围依任务风险、能力、控制及验收而定
- **Experts 的杠杆假说**：共享平台与治理可能减少逐项重复工作，也可能引入审查排队和维护瓶颈；不预测岗位数量

## 作者的稀缺性假说：Engineering Judgment

```
过去几十年：稀缺是 coding（engineer 难找且贵）
                  ↓
AI 时代：稀缺是 judgment
        ↓
  知道什么算好
  知道风险是否理解
  知道 works today 是否能 trust in production
```

Rachel 自陈："I'm not convinced that was ever the real scarcity, but that's probably another ramble."

## 关键论点："Organisations don't run on code. They run on trust."

- 当 agents 生成大量 code 时，**good design matters more, not less**
- judgment 的杠杆来自**decisions 的下游影响放大**（千 features 共用 platforms/guardrails）
- experts 的工作 = 设计让 chaos 不发生的 environment

## Demo 阶段 vs Production 阶段的鸿沟

| Demo 阶段问题 | Production 阶段问题 |
|--------------|---------------------|
| Features work | Is customer data protected? |
| Looks polished | What happens when dependency fails? |
| Demo impresses | Can someone understand this in 2 years? |
| Solves stated problem | Will it survive audit? |
| | Can it cope 1000×more users? |
| | How will we know something's wrong before customers do? |

**核心**：这些是独立的生产验收问题，不由演示成功保证。经验、明确标准、自动检查和实际责任人均可帮助发现问题。

## FOSE 2026 观察（Rachel 转述）

- FOSE 讨论"spent surprisingly little time talking about coding"
- 主导话题：design / architecture / governance / learning / judgement
- 典型实践：design specification → agents work overnight → review next morning
- 作者观察：生成加速时设计依旧重要；不是会议全体或产业共识测量

## 关键数据点

- 提出者: Rachel Laycock, Thoughtworks CTO
- 文章日期: 2026-08-19
- 引用事件: FOSE（Future of Software Development）
- 类别: value-flow framework（非 role taxonomy）

## 与相关 concept 的关系

- **[[AI-Era-Career-Skills]]**: 本文是 AI-Era-Career-Skills 的浓缩框架
- **[[Captain-Mindset]]**: experts 角色对应 captain（design vessel 让 crew 自由航行）
- **[[AI-Native-Engineering-Org]]**: 组织形态调整支持本框架
- **[[Taste-vs-Judgment]]**: judgment 的稀缺是本文核心论断
- **[[Operational-Responsibility]]**: "Organisations run on trust" 与 OR 同源
- **[[Jevons-Paradox-for-Knowledge-Work]]**: execution 便宜后 judgment 更关键——paradox 同一机理
- **[[Agent-Adoption-Curve]]**: citizens 扩大对应 adoption 普及
- **[[Knowledge-Debt]]**: demo vs production 鸿沟来自 deployment 后才暴露的 concerns

## 前提与局限性

- **前提 1**: AI 可能扩展软件创造可及性，原文仅有个人观察与案例
- **前提 2**: Agent 可承担部分执行，需按实际任务评估，不以本文证明占比
- **前提 3**: 生产风险与判断必须有可靠验收和责任归属，不预判所有判断只能由某类岗位完成
- **边界**: 三分法是 value-flow 描述而非 role boundary，实际工作中边界模糊
- **selection bias**: Rachel 是 Thoughtworks CTO（enterprise consulting 视角）；startup / scale-up 可能 lean agents + minimal experts
- **未量化**: experts 数量与杠杆变化未给出 metric

## 实施建议

1. **重新定位 expert role**：从"写每个 feature"翻转到"design guardrails/platforms"
2. **承认 citizens 价值**：让更多人 turn ideas into software
3. **按授权、可逆性和验收能力委派 agents 执行**：但生产就绪必须由有明确责任与胜任能力的验收机制确认
4. **建立 production check 清单**：责任归属、风险分级、验收、监控与回退；作者明确反对非工程人员先建好再把维护责任扔给工程师。比较交付周期、返工、事故和治理队列负载（本库综合建议）。

## 关联概念

- [[Rachel-Laycock]] — 框架提出者
- [[AI-Era-Career-Skills]] — skill 转型展开
- [[Captain-Mindset]] — experts 对应 captain
- [[AI-Native-Engineering-Org]] — 组织形态调整
- [[Taste-vs-Judgment]] — judgment 稀缺
- [[Operational-Responsibility]] — production ownership
- [[Jevons-Paradox-for-Knowledge-Work]] — 可比较需求与治理成本变化，非已证同一机制
- [[Agent-Adoption-Curve]] — citizens 扩大
- [[Knowledge-Debt]] — deployment 后 concerns
- [[Distinct-Principal-Identity]] — agent 的 identity 边界
- [[Agent-First-Enterprise]] — 企业形态演变