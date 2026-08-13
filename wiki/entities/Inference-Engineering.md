---
type: entity
title: Inference-Engineering
aliases:
  - Inference Engineering
  - 推理工程
definition: "把训练好的模型权重变成快、可靠、可负担、能规模化服务产品的工程学科——独立于训练，关注 KV cache、prefill/decode 分离、speculative decoding、量化、结构化输出等推理层优化"
created: 2026-08-13
updated: 2026-08-13
tags:
  - ai-infra
  - inference
related_entities:
  - "[[Token-Supply-Chain]]"
  - "[[Generation-Verification-Asymmetry]]"
  - "[[Self-Hosted-Models]]"
  - "[[Model-Distillation]]"
  - "[[AI-Deployment-Invisible-Costs]]"
source_raw:
  - "[[20260803-latent-space-inference-engineering-baseten]]"
---

# Inference-Engineering（推理工程）

> [!definition] 定义
> 推理工程（Inference Engineering）：把训练好的权重变成快、可靠、可负担、能规模化服务产品的工程学科，独立于模型训练。来源：Philip Kiely《Inference Engineering》（Baseten，2026）。三年前几乎不存在，如今是 AI Infra 的核心品类（Baseten 以此成为 `$13B` decacorn）。

## 核心技术栈

| 技术 | 机制 | 解决的问题 |
|------|------|-----------|
| **Cache-aware routing** | 复用已算过的 KV cache，跳过 prefill | 长上下文（如 200K token 的 agent 请求）的重复计算 |
| **Prefill/decode 分离** | 一组 GPU 处理输入生成 KV cache 与首 token，另一组迭代解码 | 两种工作负载的异构资源需求 |
| **Speculative decoding** | 小草稿模型快跑预测、大模型一次验证接受/拒绝 | 逐 token 串行解码的墙 |
| **量化校准** | 权重降精度（如 NVFP4），层间误差可相互抵消 | 内存与吞吐 |
| **结构化输出** | 状态机构束输出格式（如 JSON） | tool calling 的格式幻觉 |

## 两个关键区分

1. **"能吐 token" ≠ "产品级 API"**：开源栈（vLLM/SGLang）让"跑出 token"变容易，但产品级支持需重做量化校准、训练 traffic 定制的 speculator、为新架构（GLM-5.2 稀疏注意力、DeepSeek novel 架构）扩展 runtime。
2. **开源模型可拼接**：冻结主体权重、只训练小 adapter（projector），可把 Kimi 视觉 encoder 嫁接到 GLM-5.2 上——纯文本输入时行为不变。这是封闭 API 无法提供的模块化自由度。

## 与知识库主线的接合

- 推理工程是 [[Token-Supply-Chain|token 供应链]] 的底层实现：KV cache 管理、推理调度、成本路由的工程实体。
- speculative decoding（小模型起草、大模型验证）是 [[Generation-Verification-Asymmetry|生成-验证不对称]] 在推理层的解法。
- "能吐 token 到产品级"的鸿沟是 [[AI-Deployment-Invisible-Costs|部署隐性成本]] 的推理侧版本。
- 训练与推理正在收敛：模型帮助优化运行自己的 kernels，持续学习与 KV cache compaction 使二者边界模糊。

## 关键数据点

- Baseten 以推理工程完成 `$13B` Series F，成为 AI Infra decacorn
- GLM-5.2 实验：量化更多反而保住 benchmark 质量 + 吞吐 +20%（层间误差抵消）
- 推理优化增益范围 20%/100%/200%，目标让前沿模型提速至 10×

## 前提与局限性

- 主要证据来自 Latent Space 播客（Baseten 厂商视角），"20%/100%/200% 增益、10× 加速"属语境依赖的营销性表述。
- "量化误差相互抵消"目前是单一 GLM-5.2 实验的轶事。
- 模型改造/拼接是研究项目级成果（MMLU Pro 56%，非 frontier），真实产品受 license/评测/稳定性约束。

## 关联概念
- [[Token-Supply-Chain]]
- [[Generation-Verification-Asymmetry]]
- [[Self-Hosted-Models]]
- [[Model-Distillation]]
- [[AI-Deployment-Invisible-Costs]]
