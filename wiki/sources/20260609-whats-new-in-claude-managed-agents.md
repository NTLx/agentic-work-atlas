---
type: source-summary
title: "New in Claude Managed Agents: run agents on a schedule and store environment variables in vaults"
source_raw:
  - "[[20260609-whats-new-in-claude-managed-agents]]"
created: 2026-06-13
updated: 2026-06-13
tags:
  - source-summary
  - deployment
---

# New in Claude Managed Agents: run agents on a schedule and store environment variables in vaults

## 编译摘要

### 1. 浓缩
- **核心结论1**: Claude Managed Agents 现在支持定时运行，无需构建或托管调度器
  - 关键证据: 调度部署为代理提供 cron 时间表；每次调度触发时，代理启动新会话并完成任务；可用于夜间数据同步、每周合规扫描或每日摘要等重复性工作
- **核心结论2**: Vault 现在支持环境变量，使 CLI 和其他工具能够进行身份验证
  - 关键证据: 代理通过直接 API 调用、CLI 和 MCP 连接外部系统；环境变量允许 CLI 进行身份验证请求；密钥在沙盒中仅以占位符形式存在，真实密钥在网络边界附加
- **核心结论3**: 安全性通过"密钥不进入代理"原则得到保障
  - 关键证据: 代理永远看不到密钥，因为沙盒只持有占位符；真实密钥仅在允许的域的请求上附加

### 2. 质疑
- **关于"定时运行"的质疑**: 调度粒度是否足够？是否支持复杂的依赖和重试逻辑？
- **关于"环境变量"的质疑**: 这种安全模型是否适用于所有类型的密钥？是否有更敏感的密钥需要更严格的控制？
- **关于"80%使用率"的质疑**: 这种部署模式的采用率如何？是否有组织级的安全顾虑？

### 3. 对标
- **跨域关联1**: 此现象类似 Kubernetes 的 CronJob 和 Secrets 管理，AI 代理正在获得类似容器化工作负载的运维能力
- **跨域关联2**: "密钥不进入代理"原则类似零信任架构中的"最小权限"原则

### 关联概念
- [[Agent-Loops]]
- [[Deployment-Product-Flywheel]]
- [[Agent-Harness]]
- [[Security-Hardening-Phase]]
