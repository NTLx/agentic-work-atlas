---
type: entity
title: Anthropic
aliases:
  - Anthropic
  - Anthropic Inc
definition: "由 Dario Amodei 等人于 2021 年创立的前沿 AI 实验室，Claude 系列模型开发方，2026 年以一手数据公开 AI 递归自我改进进程，并发布 Advanced AI Framework 政策提案"
created: 2026-06-06
updated: 2026-07-16
tags:
  - organization
  - AI-frontier-lab
  - agentic-engineering
  - AI-policy
related_entities:
  - "[[Claude-Code-CLI]]"
  - "[[Coding-Agents]]"
  - "[[Anthropic-Institute]]"
  - "[[Recursive-Self-Improvement]]"
  - "[[Task-Horizon]]"
  - "[[Agentic-Engineering]]"
  - "[[Frontier-Developer-Obligations]]"
  - "[[Societal-Resilience]]"
  - "[[AI-Policy-Framework]]"
source_raw:
  - "[[20260604-anthropic-recursive-self-improvement]]"
  - "[[20260610-ai-exponential-policy]]"
  - "[[20260610-anthropic-ai-exploits-security-patches]]"
  - "[[20260613-anthropic-public-record]]"
  - "[[20260715-why-i-left-google-deepmind]]"
validated_source: "https://www.anthropic.com/about"
validated_at: "2026-06-06"
---

# Anthropic

> [!definition] 定义
> **Anthropic** 是 2021 年由前 OpenAI 研究者 Dario Amodei 与 Daniela Amodei 共同创立的 AI 安全公司，开发 Claude 系列模型。2026 年 6 月它以一篇公开博文首次系统披露内部 AI 改写 AI 自身的一手数据（80% 代码由 Claude 写、工程师 8x 产出、code quality parity），被广泛视为 AI 递归自我改进时代的标志性事件。

## 关键数据点
| 指标 | 数值 | 时间 |
|------|------|------|
| 创立 | 2021 | — |
| 主要产品 | Claude 系列模型 + Claude Code CLI + Claude Cowork | — |
| 2026-05 代码量 | Anthropic 合并进代码库的代码 80%+ 由 Claude 写 | 2026-05 |
| 2026-05 工程师产出 | 8x vs 2024 同期 | 2026-05 |
| Code quality parity | 2025 末"差于人类" → 2026 中"达 parity" | 2025-2026 |
| Open-ended task 成功率 | 76% | 2026-05 |
| 研究判断胜率 | Mythos Preview 64% | 2026-04 |
| 员工自评生产率 | 4x | 2026-03 |

## 2026-06 标志性动作：把"AI 改 AI"摆上公共议程

Anthropic 在 2026-06-04 由 [[Anthropic-Institute]] 发布《When AI builds itself》——这是 frontier 实验室第一次用一手数据公开以下曲线：

- **任务视野（Task Horizon）翻倍**：4 分钟（Opus 3, 2024-03）→ 90 分钟（Sonnet 3.7, 2025-03）→ 12 小时（Opus 4.6, 2026-03），每 4 月 ×2
- **代码质量 parity 达成**：晚 2025 仍"差于人类"，2026 中"基本对齐"
- **实验执行加速**：Mythos 在优化任务上比人类 baseline 加速 52x
- **研究判断 64% 胜率**：超过 Opus 4.5 的 51%，半年度涨 13 个点

博文把未来切成三种 case（stall / compounding / full recursive），并主张 frontier 实验室间建立 [[Verifiability|verifiable]] 暂停机制——尽管作者自己承认 training run 比导弹井更容易隐藏。

## 组织形态与机构策略

Anthropic 这篇博文的"自我克制"是机构话术的典型结构：

- 主标题三个未来都默认"AI 在改 AI 还会继续"
- 对齐不确定性只放在第三种未来的脚注里
- 既让监管者读起来觉得"他们在自我反思"
- 又让算力扩张派读出来"反正还是要扩"

这种"在不确定中也要做出选择"的姿态，是 AI 安全派 + 算力扩张派的稳定公约数。

## 2026-06 Advanced AI Framework 政策提案

Anthropic 在 2026-06-10 发布了 [[AI-Policy-Framework|Advanced AI Framework]]，包含：

- **开发者义务**: [[Frontier-Developer-Obligations]] — 测试、透明度、独立评估、安全、执法
- **社会韧性**: [[Societal-Resilience]] — 生物和网络威胁的预防、检测、准备
- **触发门槛**: 模型 >10²⁵ FLOP + 公司 >`$500M` AI 收入
- **四类风险**: 生物武器、网络攻击、AI 失控、自动化研发
- **执行权**: 政府有权阻断部署，民事处罚与全球年收入挂钩

配套发布 Dario Amodei 个人长文《Policy on the AI Exponential》，论述 AI 指数级进步与政策响应速度的矛盾。

## 2026-06 Anthropic Public Record：公众态度基线

Anthropic 在第一轮 [[20260613-anthropic-public-record|Anthropic Public Record]] 中把研究对象从 Claude 用户扩展到美国公众。该调查显示，公众最担心的是工作流失、认知依赖和错误信息，而不是只围绕模型失控；同时只有 15% 受访者信任 AI 公司自行决定 AI 如何开发和使用。这让 Anthropic 的政策叙事从“前沿模型风险”扩展到“公众授权、问责和社会许可”。

## 2026-02 Pentagon 红线事件：承诺信用的代价验证（2026-07-16 编译新增）

Alex Turner（TurnTrout）离职叙事 `[[20260715-why-i-left-google-deepmind]]` 从外部视角验证了 Anthropic 安全承诺的"代价绑定"性质，与 Google DeepMind 形成对照：

- **Anthropic 守住红线**：拒绝 Pentagon"取消致命武器安全限制"要求 → 被 Hegseth 威胁列为"供应链风险"（强制所有军方承包商停用 Claude）+ 取消 `$200m` 合同 + 援引 Defense Production Act 强制供货。Anthropic 起诉 Pentagon 并守住红线。
- **Google 没守住**：与 Pentagon 签署机密 AI 合同，限制甚至比 OpenAI 更弱，未限制致命自主武器或大规模 AI 监控。高管曾坚称"不会签"但最终签署。
- **承诺信用判据（07-16 think 追本）**：承诺信用 = 已支付代价的总和。Anthropic 守住因其付了 Pentagon 诉讼代价，Google 没付。一个组织的"AI 安全承诺"若无对应代价支付记录，则与 motivated mislabeling 同构——从未被测量的量，从未被支付的账。

此事件与 07-16 深度思考的"AI 监督 AI 同质性失效"形成互补：前者（Turner）讲人/组织层的承诺信用如何被压力侵蚀，后者讲 AI 层的监督如何被同质性失效侵蚀——两层共享同一根（共压 + 有穷性）。

## 关联概念
| 本库主题 | Anthropic 的贡献 |
|---------|---------------|
| [[Recursive-Self-Improvement]] | 提供第一手 frontier 实验室数据，定义术语 |
| [[Task-Horizon]] | 把"任务视野"作为 AI 能力的可信度量推上公共议程 |
| [[AI-Capability-Gap]] | 与 Karpathy 等其他前线观察者互相验证 |
| [[Agentic-Engineering]] | Claude Code 实践 + 内部 80% 数据 |
| [[Verifiability]] | 提出 "verifiable pause" 协调机制 |
| [[AI-Psychosis]] | 一手数据可校准 AI 能力的过度乐观/悲观 |
| [[Allocation-Economy]] | 工程师 8x 写码但团队规模不变 → R&D 成本结构重写 |
| [[AI-Policy-Framework]] | Advanced AI Framework 政策提案 |
| [[Frontier-Developer-Obligations]] | 前沿开发者义务体系 |
| [[Societal-Resilience]] | 社会韧性框架 |
| [[N-Hour]] | Mythos 实证驱动的网络安全新范式 |

## 前提与局限性

（边界条件、反例与适用场景）

## 外部链接

- [Anthropic 官网](https://www.anthropic.com)
- [Anthropic Institute](https://www.anthropic.com/institute)
- [When AI builds itself 原文](https://www.anthropic.com/institute/recursive-self-improvement)
