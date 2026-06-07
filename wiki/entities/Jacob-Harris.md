---
type: entity
title: Jacob Harris
aliases:
  - Jacob Harris
definition: "软件开发者、数据新闻从业者，关注 Vibe Coding 的本质复杂性与工程责任"
validated_source: "https://jacobharr.is/"
validated_at: "2026-05-22"
created: 2026-05-22
updated: 2026-05-27
tags:
  - person
  - software-engineering
  - data-journalism
related_entities:
  - "[[Vibe-Coding]]"
  - "[[Essential-Complexity]]"
  - "[[Friction-as-Design-Signal]]"
  - "[[Code-as-Conceptual-Infrastructure]]"
  - "[[Ownership]]"
  - "[[Cognitive-Debt]]"
source_raw:
  - "[[Why I Don’t Vibe Code]]"
---

# Jacob Harris

> [!definition] 定义
> **Jacob Harris** 是软件开发者、jacobharr.is 作者，从数据新闻和 civic technology 经验出发，关注 Vibe Coding 的本质复杂性与工程责任

## 可验证履历

| 时间 | 角色 | 组织/项目 |
|------|------|----------|
| 2010s | 数据新闻开发者 | 纽约时报等媒体 |
| 2010s-2020s | civic technology 开发者 | 公共服务系统 |
| 2026-05 | 发表 "Why I Don’t Vibe Code" | 个人博客 jacobharr.is |

**专业背景**：数据新闻、civic technology、高风险系统
**验证来源**：[jacobharr.is](https://jacobharr.is/)

## 核心观点

### Vibe Coding 的本质复杂性

Harris 在 [[Why I Don’t Vibe Code]] 中提出，AI 主要降低写代码的偶然复杂性（accidental complexity），却不能消除问题本身的本质复杂性（essential complexity）：

- **真正难的是什么**：把现实建模为清晰、可维护、能容纳例外的抽象，而不是把想法翻译成语法正确的代码
- **LLM 的边界**：LLM 可以被引导参与设计过程，但如果人类已经能做出正确引导，人类仍然是在做核心设计工作
- **反对的不是 LLM**：Harris 承认会用 LLM 处理 ImageMagick 参数这类低风险、可描述、可快速验收的小任务；真正反对的是把设计判断、抽象选择和责任承担交给 LLM

### 摩擦作为设计信号

Harris 强调 close reading 代码、逐行理解陌生系统、写 ADR、暂停思考和散步的重要性：

> 当某段代码写起来很痛苦时，问题可能不是"需要更多生成"，而是抽象边界错了、系统已经在发出结构性警报。

这与 [[Friction-as-Design-Signal]] 的核心观点一致：某些阻力提示系统模型不对，AI 若只负责绕过阻力，可能把架构问题包进更多生成代码里。

### 代码作为概念基础设施

Harris 从数据新闻经验出发，指出软件抽象不是中性容器：

- 森林、性别、日期、姓名、种族分类和诊断边界的建模都会压扁现实、遮蔽例外
- 在制度系统中，这些抽象会被放大并产生真实后果
- 代码不只是机器指令，也是 [[Code-as-Conceptual-Infrastructure|概念基础设施]]

### 责任与 ownership

Harris 指出软件是社会责任的一部分，LLM 可以模拟 care，却不能承担后果：

- 软件错误可能引发诉讼、公共服务失败或真实伤害
- 供应商在模型删除基础设施、虚构测试通过等事故中往往把责任推回用户
- [[Ownership|责任]] 仍留在人类与组织身上

## 关联概念
| 本库主题 | Harris 的贡献 |
|---------|--------------|
| [[Vibe-Coding]] | 提供 Vibe Coding 的强反面样本：不是怀旧地反对效率，而是指出认知债 |
| [[Essential-Complexity]] | 用 Brooks 的 accidental/essential complexity 区分定位 AI 的边界 |
| [[Friction-as-Design-Signal]] | 强调痛苦是架构警报，不是需要更多生成的信号 |
| [[Code-as-Conceptual-Infrastructure]] | 展示软件抽象如何压扁现实并在制度系统中放大 |
| [[Ownership]] | 指出 AI 不能承担法律、道德、维护和协作后果 |
| [[Cognitive-Debt]] | 警告当开发者不再理解抽象、边界和后果时，速度会变成认知债 |
| [[Agentic-Engineering-vs-Vibe-Coding]] | 提醒 AI Coding 的正确目标不是消灭思考，而是把判断力放在更高杠杆位置 |

## 研究边界

Harris 的立场建立在其已有抽象能力、项目风险意识和对编程本身的热爱之上。他承认：

- 新手、一次性脚本、低风险原型、内部工具可能得到不同结论
- 并非所有摩擦都值得保留（环境配置、API 参数、样板代码常常只是浪费认知带宽）
- 严谨的 harness、测试、类型系统、ADR、review 与人类引导可以把一部分设计探索转化为可验证过程

## 外部链接

- [个人网站](https://jacobharr.is/)
- [Why I Don’t Vibe Code](https://jacobharr.is/why-i-dont-vibe-code)
