---
type: source-summary
title: "Demis Hassabis: Agents, AGI & The Next Big Scientific Breakthrough"
source_raw:
  - "[[Demis Hassabis: Agents, AGI & The Next Big Scientific Breakthrough]]"
created: 2026-05-24
updated: 2026-05-24
tags:
  - source-summary
  - agi
  - agents
---

# Demis Hassabis: Agents, AGI & The Next Big Scientific Breakthrough

## 编译摘要

### 1. 浓缩

- **核心结论1: AGI 当前范式的组件（预训练、RLHF、Chain-of-Thought）将是最终架构的一部分，但仍缺 1-2 个关键突破——持续学习、长期推理和一致性是明确短板。**
  - 关键证据: Hassabis 判断"不可能几年后证明这是死胡同"——现有技术已经走了太远。但当前做法是"用胶带拼凑"（shove everything into context window）：百万 token 上下文窗口相当于工作记忆，人类只有约 7 位数字，但问题是"所有东西都塞进去，包括不重要的和错误的，这看起来很暴力且不对"。如果要处理实时视频，百万 token 只有 20 分钟。
  - 关键证据: Hassabis 的 PhD 研究正是海马体如何将新知识优雅整合进已有知识库——大脑通过睡眠（尤其是 REM 睡眠）回放重要情景。DeepMind 2013 年的 DQN 就借用了这个"经历回放"机制。但今天的 LLM 完全是 stateless，"无法适应上下文环境"——这是 agent 不能"fire and forget"的根本原因。

- **核心结论2: 小模型蒸馏没有理论极限——半年到一年后，前沿模型的能力会进入极小的 edge 模型。推理速度带来的迭代优势超过精度损失。**
  - 关键证据: DeepMind/Google 需要为 15+ 个十亿级用户产品（搜索、Gemini App、Maps、YouTube 等）提供低延迟推理——这是蒸馏技术的 directly economic incentive。Hassabis 认为"目前没看到任何信息密度极限"。
  - 关键证据: "90-95% 能力和 1/10 价格 + 更快的速度"——更快的迭代速度"换回的比那丢失的 10% 更多"。Edge 模型不仅是成本问题——隐私、安全、机器人本地处理是关键价值。

- **核心结论3: 科学发现 AI 有一个通用模式——巨大的组合搜索空间 + 明确的客观函数 + 足够的数据/模拟器。AI 将首先在单个 root node 问题突破（AlphaFold 是原型），然后向虚拟细胞等更复杂系统推进。**
  - 关键证据: AlphaFold 2 后，300 万+ 研究人员在全球使用它，"几乎所有新药发现都会用到 AlphaFold 的某个环节"。Hassabis 定义成功模式：(1) 组合搜索空间越大越好、(2) 清晰的目标函数（蛋白质自由能最小化/赢棋）、(3) 足够数据或模拟器生成合成数据。
  - 关键证据: 虚拟细胞约需 10 年。突破口可能是硬件（无需杀死细胞的纳米级活体成像——将生物学变成 vision problem）或软件（更好的学习型模拟器）。先做相对自包含的子系统——细胞核。
  - 关键证据: "创造新千年难题"（Einstein Test）比解题更难——用 1901 年的知识训练模型，能自己推出 1905 年狭义相对论吗？Hassabis 认为目前系统缺少"类比推理"——不只是在已知模式中插值。

### 2. 质疑

- **关于 AGI 2030 时间线的质疑**: Hassabis 的 2030 预测基于"deep tech 是一个 10 年旅程"的假设——如果你今天开始，AGI 出现在途中。但这个时间线依赖"只有 1-2 个 big ideas 缺失"的前提，如果实际上有更多，时间线会大幅延后。
- **关于推理"只差一两个调整"的质疑**: Hassabis 指出象棋案例中模型"发现某步是 blunder 但找不到更好的，所以就走了那步 blunder"——这是元认知的系统性缺陷。他说可能只需要"一两个调整"，但这恰是 Karpathy 说的"锯齿状智能"——你不知道那一两个调整是下个版本就到，还是需要根本性的架构创新。
- **关于"AA 游戏没出来=工具还不够"的质疑**: Hassabis 用"还没有三年级的 vibe coding 者做出卖千万份的游戏"论证工具尚不成熟。但这忽略了一个因素——创作需要 taste 和 craft，而这些可能是工具成熟后仍然稀缺的。也可能是有人已经做到了但不愿承认用了 AI。
- **关于蒸馏无极限的质疑**: 虽然目前看不到理论极限，但信息密度的物理极限最终会到来——只是我们可能还很远。另外蒸馏本身可能产生"模型同质化"风险——越来越小的模型使用相似的训练信号，能力趋同。

### 3. 对标

- **跨域关联1: 海马体记忆整合 ↔ DQN Experience Replay**: Hassabis 的认知神经科学 PhD 研究与 DeepMind 首个突破性算法之间的直接跨域映射——大脑通过 REM 睡眠回放记忆来学习，AI 系统通过 experience replay 回放成功轨迹来优化策略。这是生物智能启发 AI 设计的教科书案例。
- **跨域关联2: AlphaFold 模式 ↔ 药物发现通用逻辑**: "存在一种化合物能治愈这种疾病，只要能找到它"——Hassabis 将药物发现和围棋视为同一类问题（needle in a haystack in massive combinatorial space）。只要物理学允许其存在，找到它就是搜索效率问题。
- **跨域关联3: Tool-Use 架构 ↔ 企业组织管理**: Hassabis 设想 AGI 将是一般的工具使用者 + 专用系统（"我们不希望 Gemini 在语言能力退化的情况下去折叠蛋白质"），这与企业管理中"通才管理者 + 专家团队"结构高度一致。也呼应了 Boris Cherny 的 Cross-Disciplinary Generalist 模型。

### 关联概念

- [[Continual-Learning]]
- [[World-Model]]
- [[Scientific-Discovery-AI]]
- Virtual Cell
- [[Einstein-Test]]
- [[Tool-Use-Architecture]]
- [[Jagged-Intelligence]]
- [[Jevons-Paradox-for-Knowledge-Work]]
- [[Taste]]
