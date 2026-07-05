---
type: source-summary
title: "Introducing computer use in Gemini 3.5 Flash"
source_raw:
  - "[[20260624-gemini-3-5-flash-computer-use]]"
created: 2026-07-05
updated: 2026-07-05
tags:
  - source-summary
  - AI-Agent
  - enterprise-ai
  - automation
evidence_level: high
claim_type: extracted
---

# Introducing computer use in Gemini 3.5 Flash

## 编译摘要

### 1. 浓缩
- **核心结论1**: Computer Use 从独立模型演变为 Gemini 3.5 Flash 的内置工具——这标志着 agentic UI 交互正从"小众附加功能"变成"标准模型能力"
  - 关键证据: 此前 Computer Use 仅作为独立 Gemini 2.5 模型提供，现在原生集成到主力 Flash 模型中
- **核心结论2**: 安全措施预演了新兴的 Agent Control Plane 产品类别——定向对抗训练 + 两个可选企业防护系统（敏感操作确认 + 间接 prompt injection 检测）+ defense-in-depth 策略
  - 关键证据: 安全措施的三层设计：模型层（对抗训练）→ 企业防护层（确认/检测）→ 基础设施层（沙箱/人机回环/访问控制）
- **核心结论3**: Computer Use 支持浏览器、移动端和桌面三端环境，目标场景从消费者 demo 扩展到企业级长周期自动化任务（持续软件测试、跨专业应用的知识工作）

### 2. 质疑
- **关于"标准模型能力"的质疑**: Computer Use 作为内置工具目前只在 Gemini 3.5 Flash 上可用，其他厂商的路径不同（Anthropic 通过 API 提供 Computer Use，OpenAI 通过 Operator）——是否成为"标准"取决于行业收敛
- **关于安全措施的质疑**: Prompt injection 检测是可选功能，不是默认开启——这在实际部署中可能被跳过
- **关于企业采用的质疑**: 行业采用只有三家合作伙伴背书（Browserbase/Browser Use/UiPath），样本量小

### 3. 对标
- **跨域关联1**: Computer Use 作为内置工具与 [[ACI-Agent-Computer-Interface]] 理念一致——Agent 直接操作计算机界面而非通过 API
- **跨域关联2**: 安全措施的三层设计与 [[Constraint-Infrastructure]] 的"约束嵌入运行时"形成对应
- **跨域关联3**: 与 [[Agent-Ergonomics]] 的 "以 Agent 为第一公民" 呼应——模型原生支持 UI 操作意味着 Agent 不再需要额外的计算机界面适配层

### 关联概念
- [[ACI-Agent-Computer-Interface]]
- [[Constraint-Infrastructure]]
- [[Agent-Ergonomics]]
- [[Agent-Containment]]
- [[Prompt-Injection-Risk]]