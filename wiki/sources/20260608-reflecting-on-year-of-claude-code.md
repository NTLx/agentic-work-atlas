---
type: source-summary
title: "Reflecting on a year of Claude Code"
source_raw:
  - "[[20260608-reflecting-on-year-of-claude-code]]"
created: 2026-06-12
updated: 2026-11-28
tags:
  - source-summary
  - claude-code
  - agentic-engineering
  - verification
  - context-engineering
---

# Reflecting on a year of Claude Code

## 编译摘要

### 1. 浓缩

- **实际运行与验证循环补充自动化测试**
  - 关键证据: Boris 描述 Claude 自己打开 CLI 测试自己写的 feature；Cat 用 desktop development skill 让 Claude 用 computer use 点击测试 UX
  - 关键区分: 人们误以为 verification = lint/type check/unit test，但 能运行是获取证据的能力，不等于结果已通过正确、独立的验收

- **Auto mode：以分类器减少重复审批的厂商经验**
  - 关键证据: 受访者称收集数千条轨迹与权限请求进行分类、红队/内部测试并改进；未披露训练/测试划分和对照错误率
  - 核心机制: 受访者认为分类器可减少注意力疲劳；99% 是访谈表述，不是代表性批准率、事故率或对照结果

- **Context minimalism 是按需上下文设计偏好**
  - 关键证据: Boris："Sonnet 3.5 时代需要 prompt engineering，Opus 4 时代需要 context engineering，今天的模型只需要最小 prompt + 工具，让模型自己拉取上下文"
  - 关键区分: Boris 的个人偏好；不是对照试验证明旧方法过时，也不意味着可以省略目标、约束、证据或权限

- **角色融合：PM/设计师/财务都在写代码**
  - 关键证据: Anthropic 内部设计师提 PR、PM 改代码、财务团队用 Claude Code 做预测
  - 组织影响: AI 让"谁写代码"不再重要，"谁有产品判断力"更重要

### 2. 质疑

- **关于"verification 是 agent 能自己跑"的质疑**: 这依赖 Claude 的工具使用能力足够强。如果 agent 无法访问运行环境（如 iOS 模拟器、生产数据库），verification 仍然是外部的。当前案例都在 Anthropic 内部，外部企业是否同样适用存疑。

- **关于"auto mode 更安全"的质疑**: 这是 Anthropic 自己训练的分类器评估自己的产品。存在 self-serving bias。来源提到红队和内部测试，但未披露独立性与第三方对照审计结果。

- **关于"context minimalism"的质疑**: 这是 Claude 特定模型能力下的建议。如果模型推理能力不足，过少 context 可能导致幻觉或错误决策。"minimal" 的边界在哪里没有给出。

- **关于"角色融合"的质疑**: 选择性偏差——Anthropic 招的人本来就技术素养高。设计师提 PR 不等于所有公司的设计师都能提 PR。

### 3. 对标

- **Verification 概念**: 类似软件工程中的"测试金字塔"——unit test 是底层，integration test 是中层，agent 自主验证是顶层。但 agent verification 更接近"探索性测试"而非"规范测试"。

- **Auto mode 安全机制**: 分类器是风险判定方式，不等于默认拒绝或确定性权限执行。仍需核查实际权限规则、执行点和错误率。

- **Context minimalism**: 类似 Unix 哲学"做一件事做好"——给 agent 最小指令，让它自己组合能力。按需取证是上下文工程的一种策略，预置与动态获取可以组合；按任务质量、成本及证据充分性评估。

- **角色融合**: 类似 1990 年代计算机进入办公室的转型期——不是"在旁边加一台电脑"，而是"电脑成为中心"。Boris 引用的 Harvard Business Review 案例直接对应。

### 关联概念

- [[Agent-Verification]]
- [[Auto-Mode]]
- [[Context-Minimalism]]
- [[Role-Merging]]
- [[Claude-Code-CLI]]
- [[Agent-Loops]]
