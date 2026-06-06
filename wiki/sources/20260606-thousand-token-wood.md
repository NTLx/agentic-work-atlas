---
type: source-summary
title: "Thousand Token Wood: shipping a multi-agent economy on a 3B model"
source_raw:
  - "[[20260606-thousand-token-wood]]"
created: 2026-06-06
updated: 2026-06-06
tags:
  - source-summary
  - multi-agent
  - small-models
---

# Thousand Token Wood: shipping a multi-agent economy on a 3B model

## 编译摘要

### 1. 浓缩
- **核心结论1**: 多智能体“涌现”往往先取决于环境中的稀缺性和激励结构，而不是模型尺寸。
  - 关键证据: 初始版本因供给过剩而几乎不交易；加入 diet variety、spoilage 和 winter fuel crisis 后，市场才持续活跃起来。
- **核心结论2**: 小模型在这类系统里的优势更像可并发、可控、结构稳定，而不是更强推理。
  - 关键证据: Qwen2.5-3B 驱动 5 个 agents，每 turn 可 batched 推理；100% 调用生成有效 JSON，但经济判断本身仍然脆弱。
- **核心结论3**: 让系统稳定运转的关键工作在 prompt sharpening 和 repair layer，而不在“换更大模型”。
  - 关键证据: 作者通过“禁止买自己生产的商品”、显式短缺清单和 worked example 修正判断；malformed JSON 则降级为 no-op，而非让模拟崩溃。

### 2. 质疑
- **关于“涌现”的质疑**: 这是单个 hackathon demo，没有与更大模型或不同激励设计做系统对照，难分离环境设计与模型能力的贡献。
- **关于外推的质疑**: 5 个角色、5 种商品和戏剧化 shock 更像可视化实验，不等于真实组织或市场的复杂度。
- **关于成功标准的质疑**: valid JSON 和价格漂移证明系统稳定，但不自动证明 agent 的内部策略质量足够高。

### 3. 对标
- **跨域关联1**: 这补强了 [[Multi-Agent-Pathology-and-Governance|多 Agent 系统病理与治理]]：群体行为先由激励拓扑决定，再由模型能力放大。
- **跨域关联2**: 它和 [[Specialized-Small-Models|Specialized Small Models]] 的关系，不是“小模型更聪明”，而是“小模型让高并发、多轮系统可承受”。
- **跨域关联3**: 这也提示 [[Verifiability|可验证性]] 的边界：valid JSON 只是结构层通过，不等于判断层通过。

### 关联概念
- [[Specialized-Small-Models|Specialized Small Models]]
- [[Multi-Agent-Pathology-and-Governance|Multi-Agent Pathology and Governance]]
- [[Verifiability|Verifiability]]
- [[Emergence-World|Emergence World]]
