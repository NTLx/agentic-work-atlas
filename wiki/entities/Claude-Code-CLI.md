---
type: entity
title: Claude Code CLI
aliases:
  - Claude Code CLI
definition: "Anthropic 出品的终端原生 AI 编程助手，代理式编码环境，可读取文件、执行命令、编辑代码、运行测试并自主解决问题"
created: 2026-04-09
updated: 2026-11-28
tags:
  - AI-Agent
  - Claude-Code
  - Developer-Tools
evidence_level: medium
claim_type: mixed
related_entities:
  - '[[Product-Overhang]]'
  - '[[Agent-Loops]]'
  - '[[Boris-Cherny]]'
  - '[[Headless-Mode]]'
  - '[[Agent-Orchestration]]'
  - '[[AI-Native-SDLC]]'
source_raw:
  - "[[Anthropic's Boris Cherny: Why Coding Is Solved, and What Comes Next]]"
  - '[[OpenClaw + 6 个 Agent 运转半个月，从聊天到干活的完整工程实践]]'
  - '[[OpenClaw + CodexClaudeCode Agent Swarm The One-Person Dev Team Full Setup]]'
  - '[[20260409-ai-capability-gap-ai-psychosis]]'
  - '[[The-Founders-Playbook-05062026_v3]]'
  - "[[20260703-anthropic-skill-engineering-practices]]"
  - "[[20260609-whats-new-in-claude-managed-agents]]"
  - "[[20260822-the-ai-native-sdlc-playbook]]"
  - "[[20260822-claude-code-guide-for-startups]]"
---

# Claude Code CLI

> [!definition] 定义
> Claude Code 是 Anthropic 出品的**终端原生 AI 编程助手**（CLI 工具）。它不是聊天机器人——它是一个**代理式编码环境（agentic coding environment）**，可以读取文件、执行命令、编辑代码、运行测试，并在你观察或离开时自主解决问题。

## 核心特征

- **终端原生**：运行在终端中，理解整个代码库的文件结构、依赖关系和 Git 历史
- **模型选择**：按任务、实际支持的模型和运行配置选择；旧模型代际排序不作当前推荐。
- **Agentic Loop**：拥有专有的代理循环：收集上下文 → 执行操作 → 验证结果，循环进行
- **上下文管理**：窗口依模型与配置而异，不能保证全项目始终进入有效上下文；需要选择性读取、压缩及外部状态。
- **多界面支持**：支持 VS Code、JetBrains、桌面应用、Web 界面等多种使用方式

## 核心能力

| 能力 | 说明 |
|-----|------|
| 文件操作 | Read、Write、Edit 文件内容 |
| 命令执行 | 执行 Bash shell 命令 |
| 代码搜索 | Glob 文件模式匹配、Grep 文本搜索 |
| Git 操作 | 原生理解 Git，可创建分支、提交、解决冲突 |
| 测试运行 | 可自主运行测试并修复失败 |
| 子代理 | 可启动独立的 Subagents 进行并行任务 |

## 权限模式

按 [官方权限文档](https://code.claude.com/docs/en/permissions)（2026-11-28 核验），权限模式控制调用审批，不等于 OS 沙箱或所有工具的可用集合：

| 模式 | 行为 | 适用场景 |
|------|------|----------|
| **default / Manual** | 多数编辑、命令及网络请求需批准，存在内置及配置例外 | 交互式审批 |
| **acceptEdits** | 自动批准部分文件编辑与常见文件系统命令 | 受限工作区内的编辑 |
| **plan** | 探索与规划，不编辑源文件；可用 auto classifier 等配置影响实际命令行为 | 规划，不是独立只读沙箱 |
| **auto** | 由后台分类器检查部分动作，减少常规审批 | 需校准风险与权限边界 |
| **dontAsk** | 默认拒绝原本需要提示且未获批准的调用；本来无需批准的动作仍可运行，注意扩展机制与例外 | 无人值守的显式策略 |
| **bypassPermissions** | 跳过大部分权限提示，仍有例外；危险 | 仅在独立验证的低权限隔离环境中考虑，CI 本身不等于隔离 |

## 与 OpenClaw 的关系

既有 OpenClaw 剪藏介绍个别使用 Claude Code 作为编码执行者的案例，PTY、非交互接口与 ACP 是不同接入方式，不代表官方默认或必选架构。参见 [[Headless-Mode]]、[[Claude-Code-Automation]]。

## 关键数据点

- 模型、上下文与权限行为按实际安装版本和配置核验，不把历史产品规格当当前保证。
- 在 OpenClaw 系统中，通过 ACP 协议委派，最大 6 并发实例、120min TTL
- OpenClaw 系统架构：1 个编排者 + 5 个专业 Agent + 6 类 ACP 编码专家（含 Claude Code）
- OpenClaw 每天几千次 LLM 调用、52 个 cron 定时任务、118 个 Skills

## 前提与局限性

- **前提**：使用支持的认证与模型访问方式，不要求所有方式同时具备 API key 与订阅。
- **边界条件**：跳过审批不是沙箱；隔离必须限制真实资源、凭证、文件与网络。
- **局限性**：上下文预算有限，项目理解与测试覆盖需要实际检查。
- **局限性**: 作为 agentic coding environment，其代码生成质量依赖模型能力，复杂架构设计仍需人类参与
- **局限性**: 在 OpenClaw 系统中，Claude Code 只是 6 种编码专家之一，不同任务需要选择不同的编码 Agent

## 关联概念
