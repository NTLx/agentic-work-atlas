---
type: source-summary
title: "Loops: AI 编码世界重新发现了控制论"
source_raw:
  - "[[20260624-loops-rediscovering-cybernetics]]"
created: 2026-07-08
updated: 2026-07-08
tags:
  - source-summary
  - agentic-engineering
evidence_level: medium
claim_type: synthesized
---

# Loops: AI 编码世界重新发现了控制论

## 编译摘要

### 1. 浓缩
- **核心结论1**: Loop Engineering 本质上是 Norbert Wiener 1948 年控制论（Cybernetics）在 AI Agent 时代的重新发现——一个有决策者在体内、感知环境并朝目标纠正的循环，就是反馈回路。80 年的控制论原理直接适用于 Agent 自动化
  - 关键证据: "A loop with a decision-maker in the body, sensing its environment and correcting toward a goal, already has a name. It's a feedback loop." Wiener 的词源是希腊语 steersman（舵手）
- **核心结论2**: 五条从控制论提取的结构原则——(1) Loop 是工作单元而非任务，作者负责 loop，模型是子程序；(2) Permission ≠ Correctness，guardrails 和 verification 是不同问题；(3) 无停止条件的 loop 不是自主而是无限回归，需要 governor（上限、停滞检测、升级）；(4) Skills 复合积累，prompts 蒸发；(5) Encode the what not the how，每次模型升级让硬编码步骤更脆弱、目标/护栏/验证 spec 更有价值
  - 关键证据: 每条原则都有控制论对应——系统视角、独立观测器、governor/调速器、模块化、目标导向控制
- **核心结论3**: 人类在 loop engineering 中的角色从"loop 内的 prompt 打字者"升级为"loop 的作者"——定义目标、画边界、检查结果、命名负责人，然后去散步
  - 关键证据: "Define the goal, draw the envelope, check the result, name the owner. Then go for a walk."

### 2. 质疑
- **关于"控制论直接适用"的前提**: 经典控制论假设系统是线性的、可微的、有明确的误差信号。LLM agent 是非线性的、非确定性的，且"误差"常常不可量化。将控制论原理从恒温器迁移到 agent 需要额外的工程工作
- **关于五条原则的独立性**: "Skills compound" 和 "Encode the what not the how" 更像是工程最佳实践而非控制论原理。将它们与控制论并列可能赋予过度的理论权威
- **关于文章的信息密度**: 511 词的短文提供了概念框架但缺乏实证——没有具体案例、数据或工程细节支撑五条原则的有效性

### 3. 对标
- **跨域关联1**: "Permission ≠ Correctness" 直接映射到 [[Agent-Harness]] 中验证循环的设计——guardrails 是输出护栏（三级安全），verification 是正确性检查（测试/linter/LLM-as-Judge）。没有 verification 的 agent 是危险的
- **跨域关联2**: "Encode the what not the how" 与 [[Thin-Harness-Fat-Skills]] 的设计哲学一致——指定目标和边界，让模型选择路径。每次模型升级使硬编码步骤更脆弱
- **跨域关联3**: "Governor" 概念对应 [[Human-Governor-Agent-Operator]] 和 [[Escalation-Based-Human-Oversight]] 中的升级机制——控制理论中调速器的职责是防止系统超速，agent harness 中的 governor 做同样的事
- **跨域关联4**: Cybernetics 的"steersman"隐喻与 [[Cybernetic-Teammate]] 形成有趣的呼应——前者强调人作为 steersman 控制 agent，后者强调 AI 作为 cybernetic teammate 辅助人。两者共同指向人机协作的双向性
- **跨域关联5**: "Loop is the unit of work" 与 [[Role-Merging]] 中的角色升级一致——人从 loop 内的执行者变成 loop 的作者，正如工程师从 QA 变成产品决策者

### 关联概念
- [[Agent-Loops]]
- [[Agent-Harness]]
- [[Agent-Verification]]
- [[Human-Governor-Agent-Operator]]
- [[Thin-Harness-Fat-Skills]]
- [[Cybernetic-Teammate]]
