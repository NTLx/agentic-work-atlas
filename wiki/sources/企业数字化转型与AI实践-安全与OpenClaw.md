---
type: source-summary
title: "企业数字化转型与AI实践——智能体时代安全风险与OpenClaw实践"
source_raw:
  - "[[20260618-cio-conference-ai-practices]]"
created: 2026-06-18
updated: 2026-06-18
tags:
  - source-summary
  - ai-safety
  - agent-harness
  - OpenClaw
  - china-enterprise
  - skill-system
evidence_level: medium
claim_type: mixed
---

# 企业数字化转型与AI实践——智能体时代安全风险与OpenClaw实践

## 编译摘要

### 1. 浓缩
- **核心结论1**: Agent AI 安全风险从"输出内容合规"升级为"执行任务危险"——Skill 投毒、文件勒索、改写业务数据成为新威胁
  - 关键证据: 网信办+发改委+工信部联合发布《智能体规范应用与创新发展实施意见》；四道防线：合规+校验→评测+加固→监测+防护→持续运营
- **核心结论2**: OpenClaw 实践的核心洞察——不要让 Agent 干能让脚本干的事，大模型只在"判断与创意"环节插手
  - 关键证据: Fork OpenClaw 仓库→自打镜像→cron 预装→Agent subprocess 执行内部工具；交付物必须是可复用资产而不是对话气泡
- **核心结论3**: Agent 认知三阶段——L1 玩具级（对话）→L2 工具级（Agent skill）→L3 雷达级（cron + Agent 主动观察）
  - 关键证据: "最贵的错觉：我买了大模型，所以我完成数智化转型了"；传统对话模型"你不问它不动"，个人智能体应是"信息雷达/值夜班运维"

### 2. 质疑
- **关于"四道防线"**: 框架合理但缺乏量化标准；"持续运营优化"如何度量？安全投入的 ROI 如何证明？
- **关于"不让 Agent 干脚本能干的事"**: 这个原则在实践中如何界定？许多"脚本能干的事"正是 agent 需要自动化的——边界判断本身需要 agent 能力
- **关于"L3 雷达级"**: cron + Agent 的主动观察模式是否会导致信息过载？如何在"主动感知"和"噪声过滤"之间平衡？

### 3. 对标
- **Agent-Containment**: 四道防线与 [[Agent-Containment]] 中 agent 隔离/遏制机制形成互补——前者偏组织治理，后者偏技术架构
- **Agent-Harness**: OpenClaw 的"自打镜像+cron+subprocess"是 [[Agent-Harness]] 的轻量级中国实践——harness 不一定需要复杂框架
- **Skill-Internalization**: "交付物必须是可复用资产而不是对话气泡"直接呼应 [[Skill-Internalization]] 中 Skill 内化为组织能力的原则
- **AI-Policy-Framework**: 《智能体规范应用与创新发展实施意见》是中国 AI 治理的具体政策信号，与 [[AI-Policy-Framework]] 中公众问责维度相关

### 关联概念
- [[Agent-Containment]]
- [[Agent-Harness]]
- [[Skill-Internalization]]
- [[AI-Policy-Framework]]
