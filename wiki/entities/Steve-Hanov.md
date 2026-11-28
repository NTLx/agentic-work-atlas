---
type: entity
title: Steve Hanov
aliases:
  - Steve Hanov
definition: "加拿大 Waterloo 独立开发者；个人案例报告运营多个产品、基础技术栈约 `$20/月`，Lean-Stack 实践者，laconic/llmhub 开源作者"
created: 2026-04-15
updated: 2026-11-28
tags:
  - person
  - indie-developer
  - bootstrap
source_raw:
  - '[[How I run multiple USD10K MRR companies on a USD20month tech stack]]'
validated_source: "https://stevehanov.ca/"
validated_at: "2026-04-15"
---

# Steve Hanov

## 简介

Steve Hanov 是加拿大 Waterloo 的独立开发者。其 2026 年文章自报多个 `$10K` MRR 业务及约 `$20/月` 基础技术栈成本；不将其扩展为每个产品收入均超 `$10K`、总收入六位数或完整经营成本，未取得独立财务验证。

## 产品组合

| 产品 | 创建年份 | 商业模式 | 备注 |
|------|---------|---------|------|
| websequencediagrams.com | 2008 | Freemium + 企业版 | 18 年老产品，SEO 第一 |
| zwibbler.com | 2011-2013 | B2B 永久许可 `$5,999` | 嵌入式白板 SDK |
| rhymebrain.com | 2009-2010 | 广告 + API | 8 语种押韵词典 |
| rapt.ink | 2015-2018 | C 端 Freemium | 浏览器矢量图形编辑器 |
| xreplyextension.com | 2024 | 一次性点数 `$9` / `$19` / `$49` | X/Twitter AI 回复扩展 |
| eh-trade.ca | 2025-2026 | 金融订阅 | 加美股智能分析 |

## 技术栈

- **服务器**: Linode / DigitalOcean, 1GB RAM, `$5/月`
- **数据库**: SQLite + WAL (非 Postgres)
- **语言**: Go (非 Python/Node)
- **认证**: 自写 30 行 OAuth2
- **部署**: systemd service 文件
- **AI 开发（历史案例）**：GitHub Copilot 旧请求制；2026-06-01 后计费已变更（旧年付例外），见 [[Lean-Indie-Engineering]]，不作当前价格建议。
- **本地 AI**: RTX 3090 + VLLM + Ollama

## 开源工具

- **[laconic](https://github.com/smhanov/laconic)** — Go 写的 agentic researcher, 专为受限 8K 上下文窗口优化。像 OS 虚拟内存管理器一样管理 LLM 上下文——将不相关的对话部分 "swap out"，只保留最关键事实在活跃上下文中
- **[llmhub](https://github.com/smhanov/llmhub)** — LLM 统一接口抽象层（provider/endpoint/apikey），统一处理文本和图像 I/O，无论模型跑在桌子下面还是云端。配合 OpenRouter 实现故障自动回退
- **[smhanov/auth](https://github.com/smhanov/auth)** — Go 用户认证库，集成 Google/Facebook/X/SAML 登录，无重量级依赖

## 核心哲学

> "Keeping costs near zero gives you the exact same runway as getting a million dollars in funding."

> "The tech industry wants you to believe that building a real business requires complex orchestration. It doesn't."
