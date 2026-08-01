---
type: raw
source: "https://x.com/OpenBMB/status/2083175856563003724"
author:
  - "OpenBMB"
  - "TsinghuaNLP (THUNLP-MT)"
published: "2026-07-31"
created: "2026-08-01"
tags:
  - clippings
  - agentic-engineering
  - agent-environment-interface
  - llm-agent
  - harness
  - evaluation
---

# OpenBMB 推文：ALIGN 论文介绍（2026-07-31）

> 推文原始 URL：https://x.com/OpenBMB/status/2083175856563003724
> 论文：arXiv:2505.21055（TsinghuaNLP / THUNLP-MT）
> 代码：https://github.com/THUNLP-MT/ALIGN

## 推文正文

> Everyone building LLM agents pours effort into the agent's strategy or into harder environments. The interface between them gets almost no attention, and it is often where agents actually break.

推文开门见山：业界都把精力放在 agent 策略或环境难度上，但**真正卡住 agent 的接口几乎没人关注**。

### 核心例子（ALFWorld）

Agent 想 `examine shelf 1`，但环境要求先 `go to`。环境返回 `"Nothing happens"`，agent 推断 shelf 是空的——**错位**。简单改写反馈，Qwen2.5-7B agent 在 ALFWorld 上从 **13.4% → 31.3%**。

### ALIGN 框架（@TsinghuaNLP，OpenBMB 成员）

自动生成对齐接口修复上述错位。

论文链接：https://t.co/E4oUB5fnm9（解析后：https://arxiv.org/abs/2505.21055）
代码链接：https://t.co/LQT0R7Fel9（解析后：https://github.com/THUNLP-MT/ALIGN）

### 推文要点（1-4）

1. **问题：agent-environment misalignment** —— agent 对动作影响的内部预期与环境的实际状态转换不一致，因为隐式规则和欠规范的观察从未被显式化。论文显示这是**普遍存在的瓶颈**，不是 agent 推理失败。
2. **ALIGN 用两个模块包装环境**：INFERRULES（前置暴露静态规则和约束）与 WRAPSTEP（拦截动作并丰富观察的成功/失败条件）。轻量 Python wrapper，**不改 agent 逻辑或环境代码**。
3. **接口迭代生成**：Analyzer（从失败轨迹诊断错位）+ Optimizer（合成并精炼接口为 Python 函数），**两者都跑实验验证对抗幻觉**；消融实验证明去掉验证准确率崩塌。
4. **跨基准、跨架构、跨 backbone 泛化**：四个基准（embodied / web / tool-use），ALFWorld 成功率 **+45.67%**，连续无效动作 **-65%**。接口 plug-and-play 跨 ReAct / Self-Consistency / Planning 和 Qwen / Llama，**无需重新生成**。

### 附图

- HOjhoJra0AATmbq：错位示例
- HOjho-ha4AA-qRe：ALIGN 框架图