---
source: "https://arxiv.org/abs/2606.24597"
title: "Qwen-AgentWorld: Language World Models for General Agents"
author: "Yuxin Zuo, Zikai Xiao, Li Sheng, Fei Huang et al. (Qwen Team + Tsinghua University)"
date: 2026-06-23
tags:
  - world-model
  - agent-simulation
  - language-model
  - reinforcement-learning
  - agentic-benchmark
---

# Qwen-AgentWorld: Language World Models for General Agents

## 一句话

Qwen-AgentWorld 是首个能够通过长链思维推理（long CoT）模拟 7 个领域 agentic 环境的语言世界模型（Language World Model, LWM），支持解耦环境仿真和统一 agent 基础模型两种范式。

## 核心贡献

1. **首个语言世界模型**：Qwen-AgentWorld-35B-A3B 和 Qwen-AgentWorld-397B-A17B，能模拟 Terminal、OS、Android、浏览器、搜索引擎、API、软件工程等 7 个领域的 agentic 环境。

2. **三阶段训练管线**：
   - CPT（持续预训练）：从状态转换动态和增强专业语料中注入通用世界建模能力
   - SFT（监督微调）：激活 next-state-prediction 推理
   - RL（强化学习）：通过混合 rubric-and-rule 奖励的定制框架提升仿真保真度

3. **AgentWorldBench**：从 5 个前沿模型在 9 个已有 benchmark 上的真实交互构建的综合评测。

4. **两种互补范式**：
   - **解耦环境仿真器**：支持数千个真实环境的可扩展可控仿真，用于 agentic RL，增益超过仅真实环境训练
   - **统一 agent 基础模型**：世界模型训练作为高效 warm-up，提升下游 7 个 agentic benchmark 性能

5. **数据规模**：超过 1000 万条 7 个领域的真实环境交互轨迹。

## 关键洞见

- 世界模型从"预测下一个 token"升级为"预测下一个状态"——这要求模型理解环境的因果结构
- 语言世界模型可以作为 agent 训练的"无限环境"——可扩展、可控、低成本
- World model training as warm-up 表明：先学会预测环境，再学会在环境中行动，是一条有效的迁移路径

## 意义

这篇论文代表了 Agent 训练基础设施的一个重要方向：**用语言世界模型替代/增强真实环境**。如果 LWM 的仿真保真度足够高，Agent 训练将不再受限于真实环境的交互成本——这是一个类似于"从真实数据到合成数据"的范式转移。
