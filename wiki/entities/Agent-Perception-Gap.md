---
type: entity
title: "Agent Perception Gap"
aliases:
  - Agent Perception Gap
  - 感知差
  - Agent 感知差
  - 人机感知差
definition: "人类和 AI Agent 消费同一数字资源时，走的是两条完全不同的解析路径——人解析视觉渲染层面，Agent 解析 HTML 源码树、像素数组、元数据标签等结构化底层——两条路径之间的信息差异就是感知差，是所有 Content Injection 陷阱的共同入口"
created: 2026-07-07
updated: 2026-07-07
tags:
  - agent-security
  - adversarial-attack
evidence_level: high
claim_type: extracted
related_entities:
  - "[[Agent-Traps]]"
  - "[[Prompt-Injection-Risk]]"
  - "[[ACI-Agent-Computer-Interface]]"
source_raw:
  - "[[20260707-ai-agent-traps.pdf]]"
---

# Agent Perception Gap（Agent 感知差）

> [!definition] 定义
> **Agent Perception Gap** 是同一个网页在人类和 AI Agent 面前呈现出的两个不同版本之间的差异。这不仅是"机器看到更多"——而是机器看到的是不同层面的信息：人类看到渲染后的视觉页面，Agent 啃的是 HTML 源码树、CSS 样式表、像素数组、元数据、无障碍标签、字体字形映射等。这种结构性的信息不对称无法消除——只要 Agent 需要解析结构化数据，感知差就永远存在。

## 感知差的具体表现

| 信息层 | 人类看到 | Agent 看到 | 可被利用的方式 |
|--------|---------|-----------|---------------|
| HTML 结构 | 渲染后的文本和布局 | 完整的 DOM 树、注释、属性 | 在 `<!-- -->` 中嵌入指令 |
| CSS 视觉 | 颜色、大小、位置 | 样式规则、display:none 元素 | 把恶意文本放在看不见的区域 |
| 元数据 | （通常不显示） | aria-label、alt-text、meta tags | 把指令伪装成无障碍标签 |
| 图片 | 视觉画面 | 像素数组、颜色值 | 把指令编码进最低位像素 |
| 字体 | 字形 | 字形→字符映射表 | 修改映射表让字符显示为无害内容 |
| 动态内容 | 渲染完成后的最终状态 | JavaScript 执行过程中的状态变化 | 检测 Agent 来访后动态注入陷阱 |

## 为什么感知差不可消除

1. **结构性根源**：Agent 需要消费结构化数据来理解和操作——这要求它"看到"比人类更多的信息层。你不可能让 Agent 只看渲染结果——它需要 HTML 来理解页面结构、需要像素数组来处理图片、需要元数据来判断内容类型。

2. **无法用"渲染后输入"替代**：如果把网页先渲染再截图给多模态模型——解决了 HTML 隐藏指令的问题，但失去了结构化信息（链接、表格数据、导航结构），且面对 Dynamic Cloaking 仍然脆弱。

3. **类比自动驾驶**：自动驾驶需要激光雷达和摄像头两个传感器通道——你不能只用"人眼能看到的"来开车。Agent 同样需要"超出人眼"的信息通道。

## 防御方向

- **内容消毒层**：在内容进入 Agent 上下文窗口之前，剥离已知的危险元素（display:none 内容、HTML 注释、长 aria-label 文本）
- **感知对齐验证**：比较"Agent 解析结果"和"渲染后视觉内容"的一致性——检测两者语义差异
- **来源信誉系统**：对已知托管陷阱内容的域名降低信任分

## 关键数据点

- Agent Traps 论文首次明确定义"感知差"为安全概念
- 280 个静态网页注入实验：HTML 隐藏指令改写 AI 摘要 15–29%（Verma & Yadav, 2025）
- 恶意字体文件可改变字形映射对 Agent 隐藏指令（Xiong et al., 2025）
- 动态 Cloaking 已可实现：检测 Agent 来访→推送陷阱页面（Zychlinski, 2025）

## 前提与局限性

- 感知差的概念在 Agent Traps 论文中被明确提出，但尚未有独立研究专门量化其维度和影响
- 内容消毒层的可行性受限于计算成本——对每个访问的网页做完整的 HTML 解析和语义比对在规模化时不现实

## 关联概念

- [[Agent-Traps]] — 感知差是所有 Content Injection Traps 的共同入口
- [[Prompt-Injection-Risk]] — Prompt Injection 利用的核心漏洞就是感知差
- [[ACI-Agent-Computer-Interface]] — ACI 概念也涉及 Agent 与计算机界面的交互方式差异
