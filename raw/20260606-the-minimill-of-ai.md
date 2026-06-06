---
type: raw
title: "The Minimill of AI"
source: "https://tomtunguz.com/using-local-ai-to-work-faster/"
author:
  - "Tomasz Tunguz"
published: 2026-06-05
created: 2026-06-06
description: "Tomasz Tunguz 分享把任务先交给本地模型、只把难任务路由到云端后的运行结果：78% 的 AI 工作由本地处理，吞吐提升约 25%，平均任务时长从 47 秒降到 19 秒。"
tags:
  - "clippings"
  - "local-ai"
  - "lean-stack"
  - "routing"
  - "token-efficiency"
---

# The Minimill of AI

## 剪藏价值判断

**中高价值，建议保留并视主题推进决定是否深编译。**

理由:

- 文章很短，但信息密度高，直接给出一个清晰的工作系统判断：不是所有 agent 任务都该上云，难度分流本身就是生产力设计。
- 和本库近期关于 [[Token-Supply-Chain]]、[[Lean-Stack]]、[[Specialized-Small-Models]]、[[Agentic-Workflow-Token-Efficiency]] 的问题高度相关。
- 它不是宏大叙事，而是一个很具体的操作模式：本地小模型先做分类与执行，复杂任务再升级到云端强模型。
- 局限也很明显：证据来自作者个人系统，不是系统研究或大规模 benchmark，更像一个值得追踪的工作模式样本。

## 关键事实摘录

- 作者称过去 7 天里，自己的 AI 工作有 78% 由桌面本地模型处理，峰值达到 88%。
- 系统把 Asana 任务先分成 easy / hard：简单任务由本地模型直接处理，复杂任务再路由到云端模型。
- 引入双通道后，吞吐提升约 25%，平均任务时长从 47 秒降到 19 秒，queue age 从 73 秒降到 4 秒。
- 作者把这种模式比作 Nucor 的 minimill：大量边缘设备会在企业内部吸收掉今天挂在 hyperscaler 发票上的一大块工作负载。

## 为什么适合本知识库

这篇文章值得收，不是因为“本地模型会更便宜”这种显然的结论，而是它提供了一个更适合 agentic work 的组织单位：**先做任务分流，再决定算力去向**。这和传统“统一进一个大模型队列”的思路不同，本质上是在重写任务调度层。

后续如果编译，适合重点提取：

- local-first / cloud-escalation 的工作流模式
- routing 对吞吐、等待时间和成本的影响
- “技能蒸馏 + 本地执行”是否会成为 agent-native 组织的常见基础设施

## 原文摘录

A laptop on my desk now handles 78% of my AI work, with the rest sent to the cloud. The shift came out of my [skill distillation work](https://tomtunguz.com/the-pi-agent-skill-distillation/).

Here's how it works.

I create tasks in Asana. An agent sees the task: scheduling, email triage, research, a CRM update; and classifies it as easy or hard. If it's straightforward, a local model on my Mac handles it in seconds. If it's complex, the same model routes it to a cloud model.

Across the last seven days, daily peaks reached 88%.

As the workload grew, the two-lane design paid off. Throughput jumped about 25%, average task duration fell from 47 seconds to 19, and queue age dropped from 73 seconds to four. Nothing about the work changed. Small, fast tasks simply stopped waiting behind big, slow ones.

The task factory that uses [distilled skills](https://tomtunguz.com/the-pi-agent-skill-distillation/) is now humming along with 25% more throughput, queue age down 94%, and a much more responsive system. For now, the cloud handles the hard fifth. The Mac handles the rest.

It's the minimill of agentic work. Nucor's minimills started small, capital-light, and close to demand; within a generation they outflanked the integrated steel giants.

Every laptop, phone, and edge device with enough memory to host a distilled model becomes its own minimill: routing locally, paying cloud rates only for the hard fifth. Tens of millions of these will proliferate inside companies in the next few years, each one quietly absorbing much of the work that today shows up on a hyperscaler invoice.

Nucor began in the 1960s by melting scrap steel in electric-arc furnaces rather than smelting iron ore in giant integrated blast-furnace mills. Each minimill was a fraction of the size and cost of an integrated plant, sited near regional demand, and ran on flexible, lower-cost labor. The integrated mills dismissed minimills as fit only for low-grade products like rebar. Over the next thirty years Nucor moved up-market into sheet steel and structural beams, and by 2014 had become the largest steel producer in the United States, while most of the integrated giants had gone bankrupt. Clayton Christensen used the story as the canonical example of disruptive innovation in _The Innovator's Dilemma_.
