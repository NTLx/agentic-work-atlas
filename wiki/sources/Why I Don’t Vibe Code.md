---
type: source-summary
title: "Why I Don’t Vibe Code"
source_raw:
  - "[[Why I Don’t Vibe Code]]"
created: 2026-05-24
updated: 2026-05-24
tags:
  - source-summary
---

# Why I Don’t Vibe Code

## 编译摘要

### 1. 浓缩
- **核心结论1**: 作者反对的不是把 LLM 当工具，而是把编程本身的判断、抽象设计和责任承担外包给 LLM。
  - 关键证据: 他承认 LLM 适合 ImageMagick 参数这类低风险、可描述的任务，但用 Brooks 的 accidental complexity / essential complexity 区分指出：AI 主要消除写代码的偶然复杂性，不能替代系统抽象、边界选择和长期维护判断。
- **核心结论2**: 摩擦不是纯成本，而是学习、代码理解和架构纠偏的信号。
  - 关键证据: 作者强调 close reading、逐行理解陌生代码、写 ADR 和暂停思考；当写代码变难时，这往往说明当前架构路径有问题，而不是应该让 LLM 继续堆代码穿过去。
- **核心结论3**: LLM 无法承担软件后果，因此不能替代工程团队中的 care、协作和 ownership。
  - 关键证据: 作者引用数据新闻和 civic technology 的高风险经验，强调错误可能导致诉讼或公共服务失败；LLM 可以模拟关心，但不会为错误承担道德和法律责任。

### 2. 质疑
- **关于“我不 Vibe Code”的边界**: 这是一位有经验开发者的自我叙述，强烈依赖其技能、审美、项目类型和风险偏好；对新手、一次性脚本或低风险原型不一定成立。
- **关于“LLM 不能处理 essential complexity”的质疑**: 当前 LLM 直接处理复杂抽象确实薄弱，但严谨的 Agent Harness、测试、ADR 和人类 review 可能把部分复杂度转化为可验证流程。
- **关于伦理批评的外推**: 文中关于 LLM 供应链、安全和社会伤害的批评重要，但与“是否在工程中使用 coding agents”的机制关系需要逐案拆开，不宜直接替代具体工程评估。

### 3. 对标
- **跨域关联1**: 这篇文章为 [[Vibe-Coding|Vibe Coding]] 提供了一个反向样本：它不是从效率出发，而是从 [[Essential-Complexity|Essential Complexity]]、责任和软件作为协作实践出发。
- **跨域关联2**: 它与 [[Code-as-Conceptual-Infrastructure|代码作为概念基础设施]] 同构：代码不只是可执行文本，也是现实的抽象模型；每个抽象都会遮蔽一部分现实。
- **跨域关联3**: 它补强了 [[Ownership]]：AI 可以生成方案，但不能承担后果；人类价值不只是验收输出，而是对选择、失败和影响负责。

### 关联概念
- [[Essential-Complexity]]
- [[Friction-as-Design-Signal]]
- [[Vibe-Coding]]
- [[Ownership]]
