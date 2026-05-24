---
type: source-summary
title: "Andrej Karpathy: From Vibe Coding to Agentic Engineering"
source_raw:
  - "[[Andrej Karpathy: From Vibe Coding to Agentic Engineering]]"
created: 2026-05-24
updated: 2026-05-24
tags:
  - source-summary
  - vibe-coding
  - agentic-engineering
---

# Andrej Karpathy: From Vibe Coding to Agentic Engineering

## 编译摘要

### 1. 浓缩

- **核心结论1: 编程范式正在经历第三次根本性转变，2025年12月是明确拐点。**
  - 关键证据: Software 1.0（人写代码规则）→ Software 2.0（人通过数据训练神经网络，2017年）→ Software 3.0（人通过提示词和上下文窗口编程，LLM 成为新的"计算机"——上下文窗口是内存，提示词是程序语言，模型是解释器）。Karpathy 自述 2025年12月后 agent 输出从"需要不断纠正"变为"几乎不需要纠正"，从此他完全进入 Vibe Coding 状态。
  - 关键证据: OpenClaw 安装方式是"复制粘贴一段文本给 agent"，而非传统的 shell 脚本——因为在 Software 3.0 范式下，agent 自带智能，能感知环境、调试循环，远比精确拼写每个步骤的脚本强大。
  - 关键证据: MenuGen 案例——Karpathy 用传统方式写了一个 OCR+图像生成的 app，但 Gemini + NanoBanana 直接在像素层面把图片渲染到菜单照片上。App 本身变得多余——"那个 app 不应该存在"。

- **核心结论2: LLM 是"锯齿状幽灵"（Jagged Ghosts），不是动物智能。理解这一点决定使用效能。**
  - 关键证据: Opus 4.7 能重构 10 万行代码库、发现零日漏洞，但会建议你"走路去 50 米外的洗车店"——你想洗的是车，车不能走路。草莓有几个字母 R 的问题也长期失败。
  - 关键证据: "锯齿状"（jaggedness）的根源是训练机制——RLVR（基于可验证奖励的强化学习）使模型在可验证领域（数学、代码）极强，在不在 RL 训练回路中的领域脆弱。再加上实验室的经济投入选择（哪个领域 ROI 高就加数据、建 RL 环境），能力分布就更不均匀。
  - 关键证据: "Ghosts vs Animals" 框架——LLM 没有进化带来的内在动机（好奇心、乐趣、empowerment）、没有意识，它们是"统计数据模拟回路"（statistical simulation circuits）。你骂它们不会让它们工作得更好。

- **核心结论3: Vibe Coding 与 Agentic Engineering 是两个不同层次的能力，前者提升底线，后者保证上限。**
  - 关键证据: Vibe Coding = 提升所有人的能力底线（"人人能 vibe code 任何东西"）；Agentic Engineering = 在保持专业软件质量标准（安全、可靠）的前提下，用 agents 实现远超 10x 的速度提升——是一门正经的工程学科。
  - 关键证据: Karpathy 观察到最优秀的 agentic engineer 的生产力远超 10x，"10x 已经不是上限了"。

### 2. 质疑

- **关于"Software 3.0 让 app 消失"的质疑**: MenuGen 案例倾向激进——Gemini 直接渲染图片的范式忽略了隐私（本地处理）、离线需求、用户定制化等场景。不是所有 app 都能被"大模型直接输出最终结果"替代。
- **关于"Taste/Judgment 永远是人类的"质疑**: Karpathy 自己也承认，这个判断的前提是"实验室还没有好的美学奖励函数"。这不是不可逾越的壁垒——如果有足够好的 RL 环境来定义"好代码"/"好设计"，模型可能在这方面也不再需要人类。
- **关于可验证性框架的局限**: 可验证性是当前 RL 训练机制的自然结果，但 Karpathy 指出它依赖两个条件：(1) 领域有客观的验证方式，(2) 实验室愿意投入该领域。如果一个领域可验证但没有经济价值，模型不会自动变好。
- **关于"outsource thinking but not understanding"的边界**: Karpathy 引用这条推文说人类仍负责"理解"，但什么是理解？如果理解意味着能做出好的设计决策，而好决策又可以被验证，那么理解本身是否可被 RL 攻克？这个边界可能是暂时的。

### 3. 对标

- **跨域关联1: LLM Wiki ↔ Memex (Vannevar Bush, 1945)**: Karpathy 描述的 LLM 知识库——"任何时间看到不同的信息投影都会获得洞察"——与 Bush 的 Memex 愿景高度一致。区别在于 Memex 是机械辅助人类关联，LLM Wiki 是 AI 主动重组信息，人是最终理解者。
- **跨域关联2: 锯齿状智能 ↔ 学者症候群 (Savant Syndrome)**: LLM 在特定领域超常（代码、数学）但在基本常识上脆弱，与人类中的 savant 现象相似——超常的计算或记忆能力与基本的社交/生活能力形成鸿沟。
- **跨域关联3: Ghost vs Animal ↔ Daniel Dennett 的"意向姿态" (Intentional Stance)**: Karpathy 的"幽灵"隐喻与 Dennett 的哲学框架相通——我们将 LLM 当作有意向性的存在对待（intentional stance），但它们实际上是没有内在意图的统计系统。这种认知偏差是 AI Psychosis 的来源之一。

### 关联概念

- [[Vibe-Coding]]
- [[Agentic-Engineering]]
- [[Software-2.0]]
- [[Jagged-Intelligence]]
- [[Verifiability]]
- [[Ghost-Intelligence]]
- [[Software-3.0]]
- [[Agent-Native]]
- [[Taste]]
- [[Judgment]]
- [[AI-Psychosis]]
- [[AI-Capability-Gap]]
- [[LLM-Wiki]]
- [[Memex]]
