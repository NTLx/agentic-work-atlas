---
type: source-summary
title: "Gemini co-leads on project origins and what's next"
source_raw:
  - "[[20260529-gemini-co-leads-origins]]"
created: 2026-05-30
updated: 2026-05-30
tags:
  - source-summary
  - Gemini
  - Google-DeepMind
  - unified-model
  - distillation
  - world-model
  - agentic
  - organization
---

# Gemini co-leads on project origins and what's next

> Google for Developers 圆桌对话（2026-05-29），Gemini 3.5 Flash 发布之际。参与者：Jeff Dean、Koray Kavukcuoglu、Noam Shazeer、Oriol Vinyals，主持人 Logan Kilpatrick。讨论 Gemini 项目起源、统一模型决策、Flash 代际超越 Pro 的机制、以及对 IO 2027 的预测。

## 编译摘要

### 1. 浓缩

- **核心结论1**: 统一模型是组织决策，不只是技术决策
  - 关键证据: Jeff Dean 写了半页 memo 论证"分散团队和算力是愚蠢的"，推动 Google Brain + DeepMind 合并为一个模型项目
  - 关键证据: Koray 指出 10 年前 AI 研究更学术化，探索速度比组织结构更重要；但当模型规模变大，"focused operation"变得必要
  - 关键证据: 名称 "Gemini"（双胞胎）正来自"把两个团队合并"的隐喻
- **核心结论2**: 蒸馏是 Gemini 代际进步的核心引擎，且基本方法出奇简单
  - 关键证据: 每一代 Flash 都超越前代 Pro（3.5 Flash > 3.0 Pro），且这个趋势似乎在加速
  - 关键证据: Jeff Dean 确认方法"甚至比最初的蒸馏论文更简单"——一个好老师 + 一个学生，基本沿用原始论文 recipe
  - 关键证据: Oriol 的"挤柠檬"隐喻：把大模型的"汁液"（好的部分）压进小模型
- **核心结论3**: Agent 暴露了工具生态的延迟瓶颈，这是 IO 2027 前必须解决的全栈问题
  - 关键证据: Jeff Dean 预测 "agents 将暴露所有工具都太慢"——如果模型无限快，真实工作加速仍受限于为人类延迟设计的工具
  - 关键证据: 要跑 30 天的自主 Agent 需要 memory + continual learning + 更好的硬件（因为消耗 "a zillion tokens"），且硬件延迟必须低
  - 关键证据: Noam 指出 "30 天里有 29.5 天是在等待"

### 2. 质疑

- **关于"统一模型"的质疑**:
  - 前提假设: 顶级 AI 人才和算力可以被有效合并到一个项目中。这对资源有限的组织未必成立——分散探索在早期可能是对的
  - 边界条件: Google 有独特的资源优势。小公司或创业团队可能受益于分散探索的竞争机制（OpenAI vs Google 本身就是这种竞争的证据）
  - 反例: 早期 Google Brain 本身就是一个小团队挤在 30 人工位里，Jeff 称之为"somehow I managed to convince you to come"
- **关于"蒸馏简单性"的质疑**:
  - 前提假设: 蒸馏效果可以无限持续。但"每代 Flash > 前代 Pro"可能遇到信息论地板——不可能把无限知识压进有限参数
  - 数据可靠性: Oriol 自己也说"I'm still mesmerized how can we pack so much intelligence per parameter"——连创造者都不完全理解为什么有效，这暗示可能存在尚未理解的边界
  - 对比: [[Adversarial-Distillation|对抗性蒸馏]]讨论的是组织层面的知识抽取阻力；技术层面的蒸馏似乎没有遇到同等阻力，这可能因为 LLM 的"知识"与人类隐性知识结构不同
- **关于"Agent 自主运行 30 天"的质疑**:
  - 前提假设: 当前的 Agent 能力足以做有意义的长期研究。但当前 Agent 仍然难以在几小时内稳定工作
  - 边界条件: 30 天 Agent 的价值取决于它能否自主发现问题、修正方向。如果只是执行预定计划，那更像是批处理而非自主研究
  - Jeff 自己承认"it takes the full stack"——memory + continual learning + better hardware——任何一个缺失都做不到

### 3. 对标

- **跨域关联1**: 统一模型策略类似企业软件中的**平台工程 vs 微服务过度分散**。当团队规模和数据规模超过某个阈值，统一基础设施比各自为战更高效。但过早统一也可能扼杀创新——Jeff 承认早期分散探索（Google Brain、DeepMind、Pathways）各自产生了重要想法
- **跨域关联2**: 蒸馏的"每代小模型超越前代大模型"类似**软件工程中的编译器优化**。每一代编译器让同样的代码跑得更快，用户无需修改代码。模型蒸馏让用户用更小、更快、更便宜的模型获得昨天的旗舰能力
- **跨域关联3**: 工具延迟瓶颈类似[[Integration-Wall|集成之墙]]的微观版本——AI 从"demo"进入"生产"时遇到 legacy system 约束；Agent 从"快速对话"进入"长期自主"时遇到为人类设计的工具约束

### 其他高价值洞察

- **LLM 数据效率差距**: Jeff Dean 指出人类一生听到约 10 亿词，而 LLM 在万亿词上训练——效率差 1000 倍。这是算法创新的核心空间
- **One Box 哲学实现**: Noam 指出 Google 早期的"一个搜索框做所有事"梦想终于通过 Gemini 实现——后端不再是分散的定制系统
- **评估难题**: Oriol 认为评估"surprisingly hard"——从论文的表格数字到真实用户反馈，社区对评估的重视不够
- **Jeff 的差异化时间分配**: Jeff 聚焦推理硬件、Noam 聚焦模型架构、Oriol 深入 agent、Koray 关注产品方向——这种分工本身是统一模型成功后的组织红利

### 关联概念

- [[Model-Distillation]] — 蒸馏是 Gemini 代际能力的核心引擎
- [[Unified-Model-Strategy]] — 统一模型作为组织+技术双重决策
- [[World-Model]] — Gemini Omni 通过联合多模态训练构建世界模型
- [[Continual-Learning]] — Koray 认为需要"更有机的架构"突破
- [[Tool-Latency-Bottleneck]] — Agent 暴露工具为人类延迟设计的瓶颈
- [[Agentic-Engineering]] — IO 2027 预测：Agent 自主研究、自我改进

## 本文使用的 Wiki 页面

- [[World-Model]] — 被更新：Gemini Omni 联合训练作为新证据
- [[Continual-Learning]] — 被更新：Koray 的"有机架构"需求
- [[Adversarial-Distillation]] — 对照参考：组织蒸馏 vs 技术蒸馏
- [[Integration-Wall]] — 对标引用：工具延迟是微观版集成之墙
- [[Agentic-Engineering]] — 对照参考：IO 2027 Agent 自主研究预测
