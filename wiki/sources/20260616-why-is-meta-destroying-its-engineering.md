---
type: source-summary
title: "Meta 正在摧毁其工程组织——AI psychosis 的企业级案例"
source_raw:
  - "[[20260616-why-is-meta-destroying-its-engineering]]"
created: 2026-06-21
updated: 2026-06-21
tags:
  - source-summary
  - meta
  - engineering-culture
  - ai-psychosis
  - organizational-change
  - layoffs
evidence_level: high
claim_type: mixed
---

# Meta 正在摧毁其工程组织——AI psychosis 的企业级案例

## 编译摘要

### 1. 浓缩

- **核心结论1**: Meta 从"利润中心"到"成本中心"的工程文化转变在数周内完成——这不是渐进式转型，而是系统性摧毁
  - 关键证据: (1) 30-50% 核心团队工程师被强制调去做数据标注（ADO 组约 6500 人，其中 4500+ 是软件工程师）；(2) 所有工程师的键盘和鼠标点击被追踪用于 AI 训练数据（无 opt-out）；(3) 10% 裁员在创收创利背景下进行
- **核心结论2**: Token 测量 + 绩效考核 + 裁员恐惧 = 表演性工作（tokenmaxxing）
  - 关键证据: Meta 工程师 30 天使用 60.2 万亿 tokens（按 Anthropic API 价格价值 $900M）；工程师为提升 token 指标而过度使用 AI；写手写代码可能丢工作，但 AI 生成代码导致故障不会
- **核心结论3**: AI 生成 + AI 审查的代码导致 Instagram 史上最尴尬的安全漏洞——零认证密码重置
  - 关键证据: 攻击者只需用户名 + VPN + 联系 Meta 支持 AI 即可获得密码重置链接；Instagram 安全团队 50% 人员被调去做数据标注；CISO 在事件次日辞职
- **核心结论4**: "AI psychosis" 不只是 Meta 问题——多位创始人看到类似行为
  - 关键证据: Mitchell Hashimoto（HashiCorp 创始人）观察到"整个公司处于 AI psychosis 状态，无法进行理性对话"；核心风险：MTTR 思维（快速修复）取代 MTBF 思维（预防故障），系统看似健康但架构在衰变

### 2. 质疑

- **关于"这是 AI 转型还是成本削减"的质疑**: 表面上是 AI 转型（Scale AI 收购、Llama 模型、数据标注），但实际执行更像成本削减——在创收创利背景下裁员，将工程师从产品开发调到数据标注。可能的解释：Zuckerberg 认为训练编码 LLM 比运营核心业务更重要
- **关于"这是 Meta 独有问题"的质疑**: Hashimoto 的观察表明类似行为在其他公司也存在。但 Meta 的特殊性在于：(1) 创始人是工程师且仍为 CEO；(2) 历史上极度工程中心；(3) 转变速度极快（数周而非数年）
- **关于"AI psychosis 定义"的质疑**: 文章将 AI psychosis 定义为"对 AI 的过度关注导致忽视人类"。但更精确的定义可能是：**将 AI 能力的潜在价值误判为当前可实现的价值，并据此做出不可逆的组织决策**

### 3. 对标

- **跨域关联1**: 类似 Knight Capital 2012 案例——过度自动化 + 人类监督缺失 = 灾难性故障。Meta 的 Instagram 安全漏洞是 AI 版本的 Knight Capital：AI 生成代码 + AI 审查 + 人类团队被掏空 = 生产环境安全漏洞
- **跨域关联2**: 与 [[Cognitive-Surrender]] 的关联——工程师被迫放弃专业判断，服从"使用 AI"的指令。但 Meta 的情况更极端：不是自愿认知投降，而是强制性认知替代
- **跨域关联3**: 与 [[AI-Psychosis]] 的关联——原文直接使用了这个术语。Meta 案例为 AI-Psychosis 提供了企业级实证：当领导层对 AI 的信念压过工程判断时会发生什么
- **跨域关联4**: 与 [[Role-Merging]] 的关联——表面上是"角色融合"（工程师做数据标注），实际上是角色降级和专业技能浪费

### 关联概念

- [[AI-Psychosis]]
- [[Cognitive-Surrender]]
- [[Role-Merging]]
- [[AI-Native-Engineering-Org]]
- [[Knowledge-Work]]
- [[AI-Era-Taste-and-Judgment]]
- [[Agent-Containment]]
