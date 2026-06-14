---
type: source-summary
title: "The Minimill of AI"
source_raw:
  - "[[20260606-the-minimill-of-ai]]"
created: 2026-06-06
updated: 2026-06-06
tags:
  - source-summary
---

# The Minimill of AI

## 编译摘要

### 1. 浓缩
- **核心结论1**: 在 agentic work 里，任务分流层本身就是生产力设计，而不是附属优化。
  - 关键证据: 作者先把 Asana 任务分成 easy / hard，再决定交给本地模型还是云端模型；工作内容没变，但吞吐提升约 25%。
- **核心结论2**: local-first、cloud-escalation 让小模型从“廉价替代”变成高频工作负载的主力层。
  - 关键证据: 过去 7 天里，78% 的 AI 工作由本地模型处理，峰值达到 88%；复杂任务才升级到云端。
- **核心结论3**: 统一大模型队列的问题不只是成本高，还会制造等待和阻塞。
  - 关键证据: 双通道后平均任务时长从 47 秒降到 19 秒，queue age 从 73 秒降到 4 秒。

### 2. 质疑
- **关于数据可靠性的质疑**: 文章基于作者个人系统，没有公开任务分布、硬件配置和失败率，不能直接外推到团队级生产环境。
- **关于“本地优先”的质疑**: easy / hard 分类本身可能依赖先前的技能蒸馏成果；没有这层资产，复制成本可能高于文中表述。
- **关于经济性的质疑**: 文中强调吞吐和响应时间，但没有完整披露本地硬件折旧、维护成本和模型更新成本。

### 3. 对标
- **跨域关联1**: 这和 [[Lean-Stack|Lean-Stack]] 是同一思路在 AI 层的延伸：先压低固定成本，再用路由把昂贵资源留给真正困难的任务。
- **跨域关联2**: 这可视为 [[Token-Supply-Chain|Token 供应链]] 向端侧下沉的一种形态，不再只在数据中心里调度。
- **跨域关联3**: 它也补强了 [[Agentic-Workflow-Token-Efficiency|Agentic Workflow Token Efficiency]]：真正的效率提升不只来自便宜 token，更来自避免大任务阻塞小任务。

### 关联概念
- [[Specialized-Small-Models|Specialized Small Models]]
- [[Lean-Stack|Lean-Stack]]
- [[Token-Supply-Chain|Token 供应链]]
- [[Agentic-Workflow-Token-Efficiency|Agentic Workflow Token Efficiency]]
