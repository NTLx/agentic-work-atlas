---
type: entity
title: Hardware Sovereignty
aliases:
  - 硬件主权
definition: "企业对 AI 计算、模型运行、数据路径与基础设施拥有可选择、可迁移和可本地化的控制能力；严格全本地只是其中一种实现，核心是把数据驻留、运行依赖和退出路径置于组织可控边界。"
created: 2026-05-10
updated: 2026-09-19
tags:
  - infrastructure
  - Privacy
  - Enterprise-AI
evidence_level: high
claim_type: mixed
related_entities:
  - "[[Zero-PHI-Policy]]"
  - "[[Agent-First-Enterprise]]"
  - "[[Layered-AI-Sourcing]]"
  - "[[Evaluation-Set]]"
source_raw:
  - "[[OncoAgent A Dual-Tier Multi-Agent Framework for Privacy-Preserving Oncology Clinical Decision Support]]"
  - "[[MachinaCheck Building a Multi-Agent CNC Manufacturability System on AMD MI300X]]"
  - "[[The Return of the Deployment Company]]"
  - "[[20260831-the-price-of-entry-to-the-frontier]]"
---

> [!definition] 定义
> **Hardware Sovereignty** 更准确地指组织对 AI 计算、模型运行和数据路径拥有可控制、可替换、可本地化的能力。严格 air-gapped / 全本地部署是最强形态，但不是定义本身。HIPAA、GDPR 等法规并不普遍要求“必须本地运行 AI”；实际要求取决于数据类别、处理目的、合同、地域和安全措施。本地化的价值在于降低外部依赖并增强数据驻留与退出控制。

## 关键数据点

- **OncoAgent 实例**: 完整栈（训练+推理+RAG+UI）运行在单块 AMD Instinct MI300X（192 GB HBM3）
- **训练栈**: Unsloth + QLoRA + ROCm，无需 CUDA
- **推理栈**: OncoAgent 主路径使用本地 BF16 推理，同时保留 Featherless.ai API 降级路径，因此它更适合视为“local-first / dual-tier”案例，而非严格零外部依赖。
- **向量存储**: ChromaDB 本地持久化索引。
- **合规含义**: 本地化可减少敏感数据外传面，但是否满足 HIPAA/GDPR 仍取决于完整处理流程、访问控制、协议与组织措施，不能由“本地部署”单独推出。
- **ROI**: 56 倍合成数据生成加速 + 6 倍训练时间压缩，单卡即可完成
- **企业部署判断**: Caffein Chen 文章认为，到 2026 年，开源模型、本地 GPU、vLLM/TGI/Ollama、RAG 框架和开源 UI 已让多数企业任务的本地部署从 R&D 项目接近 IT 采购项目。

## 2026-08 补充：主权还包括访问权与退出权

[[20260831-the-price-of-entry-to-the-frontier]] 提醒，模型主权不只发生在“云 vs 本地”这一轴。frontier 模型还可能受到地区、组织白名单、配额、产品默认集成或政府许可影响。因此企业即使接受云 API，也应评估供应商可得性、数据关系、替代模型、迁移成本和退出路径。反过来，开放权重只有在许可证、硬件、运维与安全成本都可承受时，才真正形成可执行的替代方案。

## 前提与局限性

- **前提**: 需要高端本地硬件（如 MI300X 的 192 GB HBM3），成本较高
- **前提**: 需要开源模型和框架支持（如 Qwen、Unsloth、ChromaDB）
- **局限性**: 高端硬件获取门槛高，多数中小机构难以部署
- **局限性**: 缺乏云服务的弹性扩展能力，高峰期可能需要排队
- **局限性**: 本地部署仍需要 AI operations 人才、模型维护能力和较长 ROI 周期；它更适合高频、高敏感、长期运行的核心工作流，不适合所有场景。

## 关联概念

- [[Zero-PHI-Policy]] — 硬件主权为 Zero-PHI 策略提供基础设施保障
- [[Agent-First-Enterprise]] — 硬件主权是企业 Agent 化转型的基础设施前提
- [[Layered-AI-Sourcing]] — 决定哪些 AI 能力应本地化，哪些可外部采购
- [[Evaluation-Set]] — 本地部署时必须保留在企业内部的关键评测资产
