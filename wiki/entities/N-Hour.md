---
type: entity
title: N-Hour
aliases:
  - N-Hour
  - N 小时
  - N-Hour Paradigm
definition: "Anthropic 一项 Mythos Preview 研究提出的风险框架：补丁发布后数小时内即可完成部分漏洞分析与利用构建；N-Hour 是对该时间尺度的命名，不是所有模型或真实攻击链的普遍替代指标"
created: 2026-06-12
updated: 2026-11-28
evidence_level: medium
claim_type: mixed
tags:
  - cybersecurity
  - AI-capability
related_entities:
  - "[[Mythos]]"
  - "[[Cybersecurity-Proof-of-Work]]"
  - "[[Security-Hardening-Phase]]"
  - "[[Collingridge-Dilemma]]"
source_raw:
  - "[[20260610-anthropic-ai-exploits-security-patches]]"
---

# N-Hour

> [!definition] 定义
> Anthropic (2026) 在 Mythos Preview 研究中提出 **N-Hour** 这一命名：部分漏洞从补丁到崩溃证明或完整利用的时间可能压缩到小时级。它是该研究对风险窗口的框架化表达，不能据此宣布 N-Day 对所有模型、漏洞或真实攻击已经失效。

> [!note] 证据身份
> 本页主要依据Anthropic 2026-06-08研究及其二手摘要；实验比较多个Claude模型，重点结果来自受限Mythos Preview和选定漏洞样本。下列是特定研究的报告结果，非实际生产入侵记录；“补丁窗口普遍进入小时级”以及对防御体系的推论属于有限外推，真实攻击还需要侦察、投递、持久化和规避检测等环节。

## 关键数据点

- **Firefox**：选定18个补丁的研究报告14个PoC触发、8个完整验证结果；耗时是受控实验中基于补丁可得性的风险估计，而非在线观察到的攻击时间线
- **Windows**：21个已知补丁的受控研究报告18个PoC与8个完整验证结果；不是任意闭源二进制零日发现能力
- **成本**：作者的实验API开销与真实事故全过程成本、风险概率及防御成本是不同指标
- **评级边界**：原文报告14个较低利用可能性评级样本中13个触发PoC，不能解释为13个完整利用；作者建议重审评级校准，非全部Microsoft评级失效证明
- **补丁窗口期**: 原研究以Autopatch参考部署节奏作风险对照，并未观测真实设备更新与攻击的联合分布；各环境实际覆盖须独立核验
- **对比基准**: Source Summary 引用的 Mandiant 2020 分析显示，25 个漏洞中 16 个需一个月或更长时间被利用；这是历史对照，不是与 Mythos 样本完全同设计的实验

## 前提与局限性

- **前提**:
  1. 额外预算在所测任务中可能改善结果，不保证所有模型和漏洞
  2. 安全补丁的代码差异提供了足够的漏洞定位信息
  3. 模型能理解复杂的二进制代码和系统架构
- **局限性**:
  1. 真实攻击还需要目标侦察、投递、检测规避等额外步骤
  2. Mythos Preview 是受限访问模型，不代表所有公开可用模型的能力
  3. 防御方可能开发 AI 驱动的检测和响应系统
  4. 内存安全语言和硬件级保护可能长期改变攻防均衡

## 防御侧实践（2026-11-28）

回核[Anthropic原文](https://www.anthropic.com/research/n-days)引言和结论。N-day指已公开漏洞等，不是以天为最低单位；N-Hour是作者的风险时间尺度表述。**综合判断**：按实际暴露、严重度、补丁/缓解可用性及业务影响划分更新优先级，验证补丁是否真正覆盖运行中的系统；无法立刻更新时选择受控隔离或临时缓解并复验。长期减少缺陷类别的架构设计，与缩短发布、分发和生效时间互补。不制定普适小时级SLA，不复跑利用实验。

## 关联概念

- [[Mythos]] — 构建 N-Hour 范式的模型
- [[Cybersecurity-Proof-of-Work]] — N-Hour 加速了 token 成本博弈
- [[Security-Hardening-Phase]] — N-Hour 要求持续而非一次性的安全硬化
- [[Collingridge-Dilemma]] — N-Hour 是技术影响难以预见直到难以管理的经典案例
