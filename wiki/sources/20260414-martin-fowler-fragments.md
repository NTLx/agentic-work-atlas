---
type: source-summary
title: "Martin Fowler fragments on AI, laziness, TDD and restraint"
source_raw:
  - "[[20260414-martin-fowler-fragments]]"
created: 2026-05-24
updated: 2026-05-25
tags:
  - source-summary
  - AI
  - TDD
  - Software-Engineering
---

# Martin Fowler fragments on AI, laziness, TDD and restraint

## 编译摘要

### 1. 浓缩
- **核心结论1**: Fowler 借 Bryan Cantrill 的观点强调，程序员的"懒惰"不是偷懒，而是因为人类时间有限而追求抽象、简化和认知负担下降。
  - 关键证据: Cantrill 认为 laziness 驱动我们把系统做得尽可能简单但不过度简单，发展出强抽象，从而用更少代码达成更多功能。
  - Fowler 用自己的音乐 playlist generator 例子说明，他一度想让 LLM 直接实现新能力，但进一步思考后发现自己正在做不必要的复杂功能，应用 YAGNI 后几十行代码即可解决。
- **核心结论2**: LLM 缺少这种由有限时间形成的懒惰约束，因此更容易让系统变大，而不是变好。
  - 关键证据: Cantrill 的警告是，LLM 不会为自己或未来维护者节约时间，工作对它几乎没有痛感，容易在已有垃圾层上继续堆东西。AI 生成能力越强，越需要人类守住抽象质量和系统简洁性。
  - 这不是反对 AI 写代码，而是提醒：若人只看"它很快完成了任务"，忽略是否引入不必要复杂性，未来维护成本会由人和后续 agent 一起承担。
- **核心结论3**: TDD 的精神可以迁移到 agent prompting，先建立验证条件，再写或强化指令。
  - 关键证据: Jessica Kerr 的例子是，希望所有代码更新都同步更新文档。可以改 `AGENTS.md` 增加 instruction，也可以增加 reviewer agent 检查 PR 是否遗漏文档。Fowler 认为按 TDD 思路应先做 verification，因为没有检查，指令是否被遵守不可知。
  - 这里的深层原则是：对 agent 的要求不能只停留在 prompt，必须落到可检查的正确性条件、reviewer、test 或流程门禁。
- **核心结论4**: AI 系统需要被设计出"克制"，尤其在错误代价不对称或不可逆的场景中。
  - 关键证据: Mark Little 借电影 Dark Star 讨论 AI 的过度确定性：许多系统被优化为给出输出、消解歧义、做出推断，但在开放系统中，正确行为有时是延迟、拒绝或不行动。Fowler 认同怀疑和克制是高风险决策能力的一部分。

### 2. 质疑
- **关于"AI 缺乏懒惰"的质疑**: 这更像当前系统激励和默认行为，而不是永恒属性。未来模型若被明确奖励简洁性、可维护性和删除代码，可能表现出类似懒惰的行为。
- **关于个人经验的质疑**: Playlist generator 是单个个人案例，不能证明 LLM 普遍过度设计。但它提供了一个强提醒：人在动手过程中发现问题更简单，而把任务外包给 agent 可能跳过这种重新理解。
- **关于 TDD 迁移的质疑**: 不是所有 agent 任务都有清晰测试。文档更新、架构一致性、可读性、用户体验等质量要求需要 reviewer、lint、人工判断和示例集组合，不能只靠传统单元测试。
- **关于克制的质疑**: "不行动"本身也可能带来风险。高风险系统应设计何时拒绝、何时升级给人、何时继续搜证，而不是笼统要求 AI 更保守。

### 3. 对标
- **与 [[20260410-code-is-cheap|Writing code is cheap now]] 方向对标**: 代码生成成本下降后，人的新职责不是接受更多代码，而是维护简洁性、YAGNI 和长期可理解性。
- **与 [[Verifiability]] 对标**: TDD-for-agents 说明，agent 工作质量要靠可验证反馈闭环，而不是更长的指令文本。先有检查，再谈自动执行。
- **与 [[AI-Restraint]] 对标**: 克制是 autonomy 的配套能力。系统越能自主执行，越需要知道何时停下、何时承认不确定、何时请求人类确认。
- **与 [[Laziness-Virtue]] 对标**: 人类有限时间是一种设计压力。AI 让产出变便宜后，这种压力不会自然存在，必须通过架构原则、review、测试和文化重新引入。

### 关联概念

- [[Martin-Fowler]]
- [[Laziness-Virtue]]
- [[AI-Restraint]]
- [[Agentic-Engineering]]
- [[YAGNI]]
- [[Verifiability]]
