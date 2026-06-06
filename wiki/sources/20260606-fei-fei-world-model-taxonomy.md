---
type: source-summary
title: "A Functional Taxonomy of World Models"
source_raw:
  - "[[20260606-fei-fei-world-model-taxonomy]]"
created: 2026-06-06
updated: 2026-06-06
tags:
  - source-summary
  - world-model
  - simulation
---

# A Functional Taxonomy of World Models

## 编译摘要

### 1. 浓缩
- **核心结论1**: “world model” 不是一个单一物种，至少应按功能拆成 renderer、simulator、planner 三类。
  - 关键证据: 文中把三类输出分别对应为 observation、state、action，并用 POMDP 回路统一解释它们的边界。
- **核心结论2**: simulator 是三者中最关键、也最被低估的一层，因为它同时支撑 render 和 plan。
  - 关键证据: 文中强调 renderer 的契约是视觉保真，planner 的契约是行动建议，而 simulator 的契约是几何、物理和动力学的结构正确性。
- **核心结论3**: unified world model 是合理终点，但当前瓶颈在 3D/物理数据稀缺、sim-to-real gap 和生成几何错误。
  - 关键证据: 作者明确指出显式几何、材质和物理注释数据远少于互联网视频，且生成式 simulator 还会带来自交、尺度错误等新风险。

### 2. 质疑
- **关于分类边界的质疑**: 现实系统常同时兼具 render、simulate、plan，多数产品不是纯单一类别，分类更适合作为分析框架而非硬边界。
- **关于证据类型的质疑**: 这是一篇定义型长文，不是实验报告；它提升了概念清晰度，但没有直接给出经验比较。
- **关于工作语境迁移的质疑**: POMDP 视角天然偏向具身或环境交互任务，把它迁移到知识工作 Agent 仍需额外中间层。

### 3. 对标
- **跨域关联1**: 这直接补强 [[World-Model|World Model]] 页面，把“内部表示”进一步切成 observation、state、action 三种输出职责。
- **跨域关联2**: 它与 [[Tool-Use-Architecture|Tool-Use Architecture]] 的关系在于：planner 负责给出动作，工具系统负责把动作真正落到世界中。
- **跨域关联3**: 对 [[Scientific-Discovery-AI|Scientific Discovery AI]] 和机器人类 Agent 来说，simulator 的价值类似实验环境或可计算假设空间。

### 关联概念
- [[World-Model|World Model]]
- [[Tool-Use-Architecture|Tool-Use Architecture]]
- [[Scientific-Discovery-AI|Scientific Discovery AI]]
- [[Continual-Learning|Continual Learning]]
