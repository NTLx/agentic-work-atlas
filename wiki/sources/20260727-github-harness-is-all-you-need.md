---
type: source-summary
title: "The harness is all you need (mostly)"
source_raw:
  - "[[20260727-github-harness-is-all-you-need]]"
created: 2026-07-28
updated: 2026-07-28
tags:
  - source-summary
  - agentic-engineering
  - coding-agents
  - agent-harness
evidence_level: medium
claim_type: mixed
---

# The harness is all you need (mostly)

> GitHub 的 Burke Holland（2026-07-27）提出 "the harness is all you need—mostly"：生产力增益不来自安装新工具/新 skill/新 prompt，而来自理解并熟练使用 harness。文章给出一套八步 Copilot 工作流（选工具 → YOLO+沙箱 → 原型 → plan 质询 → Autopilot 实现 → 人类评审迭代 → rubber duck 跨模型评审 → 提交），全部使用 Copilot 内置功能。来源：GitHub 官方博客。证据等级：medium（厂商一手实践文，工作流具体可操作，但示例为刻意简单案例，且"只用 Copilot 就够"恰是 Copilot 产品目录）。

## 编译摘要

### 1. 浓缩

- **核心结论1**: 命题——harness 理解优先于工具追逐。"Less is way more"：新工具/MCP/skill/prompt 多为 gimmick，真正的生产力杠杆是对 harness 的理解；且 harness 体验正在跨工具统一（CLI/app/VS Code/Visual Studio/JetBrains 收敛到同一核心工作流），学一次处处用
  - 关键证据: 作者自述"每天用 AI，最大增益来自如何使用 harness 以及对它的理解程度"；入门推荐 CLI（最接近 harness，纯文本交互，无 UI 学习成本）
- **核心结论2**: 八步工作流——一套只用内置功能的可重复流程
  - 关键证据:
    1. **选工具**: 优先 CLI（离 harness 最近）
    2. **YOLO 模式（allow-all）+ 沙箱**: agent 需要自主权才有生产力增益（"按 Approve 按到后来就不读审批内容了"），但不在本地机跑——Codespaces/devcontainer 隔离
    3. **原型先行**: "给我 20 个 date picker mock 放一个 HTML 里对比"；非视觉任务也做视觉原型（API 设计用 Mermaid 图列五种方案）——感官丰富的模型比密集文本处理更快，原型暴露文字描述隐藏的 nuance
    4. **plan mode 质询**: 边缘情况枚举（起止日期可否相同？部分选择有效吗？格式？粘贴？）；可叠 grill-me skill 加大质询强度；**关键：plan 的价值不是接受建议，而是深度介入问题、注入专业判断**
    5. **Autopilot 实现**: 内置 loop 强制模型完成计划每一项；自动编排——读文件用 Explore 子代理（小模型），复杂动作用 General Purpose 子代理（大模型），开箱即用无需配置
    6. **人类评审迭代**: 不满足于"good enough"，taste 决定最终质量；小修小补直接对话式给出（"if you've got the context, you've got the prompt"）
    7. **rubber duck 跨模型评审**: 请求不同模型家族的审查（用 GPT 5.6 Terra 实现则请 Sonnet 审查）——不同训练数据 = 不同盲点；可与 Autopilot 组合成循环，直到双方同意只剩边际收益
    8. **提交**: 聊天会话按主题隔离，偏题即新会话
- **核心结论3**: 配套机制——模型选中等档（GPT 5.6 Terra / Claude Sonnet + medium reasoning）且**全程固定不换**，利用 prompt caching 折扣；结尾反高潮："今天的神奇咒语很多会是明天的反模式"，专注用最简单的方式拿到可重复的高质量结果

### 2. 质疑

- **关于激励结构的质疑**: 厂商一手文——"只用 Copilot 内置功能就够"恰好是 Copilot 的产品目录（Autopilot、rubber duck、Codespaces 全是 GitHub 功能）。与库内 [[20260727-langchain-own-your-intelligence]]（框架厂商）、[[20260718-ai-mania-eviscerating-decision-making]]（咨询）、[[20260719-if-ai-is-so-great-why-isnt-it-working]]（部署服务商）的激励结构四连同构：结论可能为真，但"少装东西、用我的全家桶"的叙事方向与作者雇主利益一致
- **关于示例代表性的质疑**: 作者自认 date picker 是 "a bit of a contrived example"。八步流在简单独立组件上演示，对遗留系统、分布式服务、安全关键代码的适用性未论证；"build a date picker used to be one of the hardest things" 的感叹也说明选例偏向 AI 擅长的自包含任务
- **关于 YOLO 的质疑**: "审批疲劳训练人不读审批内容"是尖锐观察，但全文把自主性处理成二元开关（allow-all vs 逐项审批）；中间粒度（按工具类型授权、按风险分级）被跳过。沙箱方案是转移问题而非解决问题——数据出界与沙箱摩擦的成本未讨论
- **关于 rubber duck 证据强度的质疑**: "不同模型不同盲点"可信但无数据——跨家族评审实际多发现了多少问题，文章未给。且与 Berkeley 同期 position paper 的警告形成张力：独立验证需要**目标级独立**，跨模型家族只是训练数据级独立，而主流模型训练语料高度重叠（见 [[20260726-berkeley-auto-software-dev]] 质疑节）

### 3. 对标

- **命题谱系: "harness 优先"的第三源**: 标题戏仿 "Attention is all you need"，在架构层断言 harness 优先。与库内 [[Harness-Engineering]] 的 Addy Osmani 命题（"失效通常不是模型问题，而是 harness 问题"）从两个厂商视角（OpenAI 侧评论者 / GitHub 侧从业者）收敛于同一判断：模型是时钟，harness 是杠杆
- **同日配对: 实践机制 ↔ 理论警告**: rubber duck review（跨家族盲点互补）与 Berkeley position paper（2026-07-26，早一天）的 "independent verifier agents help only if they operate with genuinely independent objectives" 形成精确配对——GitHub 给出机制，Berkeley 给出机制成立的条件。两篇同窗口发表的材料在 [[Agent-Verification]] 上交汇（综合判断）
- **plan mode ≈ 判断力命题的操作化**: "plan 的价值不是接受 AI 建议，而是你深度介入、注入专业判断"——人类在回路中的位置从"生成答案"迁移到"判断问题"。与库内判断力/taste 命题同构；grill-me 式质询 = 把隐性边缘情况逼成显式规格
- **跨域类比: 瀑布模型的执行者替换**: 八步流 ≈ 经典原型-设计-评审工程循环，但每个环节的执行者换成 agent，人类角色收缩到三个点：原型选择、计划质询、质量坚持。这正是 Berkeley 三级框架中 **Level I（Code Autonomy）** 的微观实例——AI 拥有设计与实现，人类在 PR 粒度审查（综合判断）

### 关联概念

- [[Harness-Engineering]] — 八步工作流是 harness 工程在个人从业者层面的实例化
- [[Agent-Harness]] — "the harness is all you need" 命题的载体
- [[Agent-Verification]] — rubber duck 跨模型评审 = 异构模型盲点互补的验证机制
- [[Auto-Mode]] — YOLO/allow-all 与 Autopilot loop 的自主性配置
