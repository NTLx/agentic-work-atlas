---
type: source-summary
title: "Observability for developers building connectors"
source_raw:
  - "[[20260608-connector-observability-directory]]"
created: 2026-06-13
updated: 2026-06-13
tags:
  - source-summary
  - mcp
  - observability
  - connectors
---

# Observability for developers building connectors

## 编译摘要

### 1. 浓缩
- **核心结论1**: MCP 连接器现在拥有可观测性仪表板，提供采用指标、健康信号和使用分解
  - 关键证据: 采用指标包括活跃用户、总工具调用次数和目录排名；健康信号包括错误率和延迟，按工具细分；使用分解显示在 Claude、Claude Code 和 Cowork 中的参与度
- **核心结论2**: 开发者可以直接在 Claude 界面中将 MCP 服务器提交到目录
  - 关键证据: 目录中有超过 300 个第三方连接器；开发者可以在组织设置下直接提交 MCP 服务器
- **核心结论3**: 可观测性是连接器生态系统成熟的关键标志
  - 关键证据: 从简单的工具调用到有监控、调试和改进能力的完整生命周期管理

### 2. 质疑
- **关于"300+连接器"的质疑**: 这些连接器的质量和活跃度如何？有多少是生产就绪的？
- **关于"可观测性"的质疑**: 这些指标是否足够诊断复杂问题？是否需要更深入的追踪？
- **关于"目录提交"的质疑**: 提交流程的质量控制如何？如何防止低质量或恶意连接器？

### 3. 对标
- **跨域关联1**: 此现象类似云服务的"API 网关"监控，MCP 连接器正在成为 AI 时代的 API 网关
- **跨域关联2**: 目录提交流程类似 npm 或 PyPI 包注册，但增加了 AI 特定的安全和质量考量

### 关联概念
- [[Model-Context-Protocol-MCP]]
- [[MCP-Registry]]
- [[Tool-Use-Architecture]]
- [[Agent-Infra]]