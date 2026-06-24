---
title: "联网工具（事实核查/时间验证/溯源）"
type: schema-subdoc
---

> 本文档是 Agentic Work Atlas Schema 子文档，由 README.md 路由表按需加载。

# 联网工具（事实核查/时间验证/溯源）

Agent 根据任务性质自主选择最合适的联网工具，不强制绑定单一工具链。以下是各工具的适用场景和使用经验：

## 工具选择指南

| 工具 | 适用场景 | 说明 |
|------|---------|------|
| **Jina** (`r.jina.ai/{url}`) | 文章、博客、文档、PDF 等正文类页面 | 第三方服务，将网页转为 Markdown，大幅节省 token。URL 前加前缀，不保留原网址 http 前缀。限 20 RPM |
| **Tavily Extract** | 需要提取特定 URL 内容 | 返回 clean markdown，支持批量 URL |
| **Tavily Search** | 实时信息搜索 | 返回 snippets + source URLs |
| **Exa Web Search** | 语义丰富的搜索 | 返回 clean text content，适合需要高质量内容的场景 |
| **WebFetch** | 简单网页抓取 | 内置工具，返回 markdown/text/html |
| **curl** | 需要原始 HTML（meta、JSON-LD 等结构化字段） | 直接获取页面源码 |

**推荐策略**: 优先尝试轻量工具（Jina / Tavily），不满足需求时再升级到更重的工具。对微信公众号等反爬站点，Jina 和 Tavily 可能被拦截，需换用其他方式。

## Jina 使用经验

- **调用方式**: `curl -sL -H "Accept: text/markdown" "https://r.jina.ai/{url_without_http_prefix}"`
- **适合**: 文章、博客、文档、技术帖等以正文为核心的页面
- **不适合**: 数据面板、商品页、需要登录的页面、动态渲染重的 SPA
- **限制**: 20 RPM；微信公众号等反爬站点会返回 CAPTCHA 要求
- **注意**: 返回内容可能有信息损耗，关键数据需对照原文验证

## Edit 工具常见问题

- 字符串匹配失败时，尝试读取精确行内容查看实际字符
- 可先更新其他字段（如 updated 日期）作为突破口
- index.md 编辑时注意统计数字和 footer 分开更新