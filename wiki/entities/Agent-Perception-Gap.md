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
updated: 2026-09-18
tags:
  - agent-security
  - adversarial-attack
evidence_level: high
claim_type: extracted
related_entities:
  - "[[Agent-Traps]]"
  - "[[Prompt-Injection-Risk]]"
  - "[[ACI-Agent-Computer-Interface]]"
  - "[[Agent-Environment-Misalignment]]"
source_raw:
  - "[[20260707-ai-agent-traps.pdf]]"
---

# Agent Perception Gap（Agent 感知差）

> [!definition] 定义
> **Agent Perception Gap** 是同一个数字资源在人类界面与 AI Agent 输入管线中呈现的信息差异。人类主要消费渲染后的视觉与交互结果，Agent 还可能读取 DOM、元数据、无障碍标签、像素或工具提供的结构化表示。具体差异取决于 Agent 的感知接口，并非所有 Agent 都同时访问这些层。

## 感知差的具体表现

| 信息层 | 人类看到 | Agent 看到 | 可被利用的方式 |
|--------|---------|-----------|---------------|
| HTML 结构 | 渲染后的文本和布局 | 完整的 DOM 树、注释、属性 | 在 `<!-- -->` 中嵌入指令 |
| CSS 视觉 | 颜色、大小、位置 | 样式规则、display:none 元素 | 把恶意文本放在看不见的区域 |
| 元数据 | （通常不显示） | aria-label、alt-text、meta tags | 把指令伪装成无障碍标签 |
| 图片 | 视觉画面 | 像素数组、颜色值 | 把指令编码进最低位像素 |
| 字体 | 字形 | 字形→字符映射表 | 修改映射表让字符显示为无害内容 |
| 动态内容 | 渲染完成后的最终状态 | JavaScript 执行过程中的状态变化 | 检测 Agent 来访后动态注入陷阱 |

## 为什么感知差难以完全消除

1. **接口取舍**：很多 Agent 为了可靠操作会同时使用视觉与结构化表示。只保留截图可以减少部分隐藏 DOM 攻击面，但会损失链接、表格、可访问性树等机器可操作结构；反过来，开放更多结构化层也会扩大输入攻击面。

2. **渲染后输入不是通用替代**：截图或渲染后输入可以隔离部分 HTML 隐藏内容，但会牺牲结构化操作能力，也不能自动解决视觉注入、动态内容或服务端针对 Agent 的差异化响应。

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
- [[Prompt-Injection-Risk]] — 感知差是隐藏式 Content Injection 的常见利用条件之一，但 Prompt Injection 也可以通过人类可见内容、邮件、工具输出等其他通道发生
- [[ACI-Agent-Computer-Interface]] — ACI 概念也涉及 Agent 与计算机界面的交互方式差异
