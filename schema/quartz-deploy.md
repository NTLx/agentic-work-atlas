---
title: "Quartz 网站部署"
type: schema-subdoc
---

> 本文档是 Agentic Work Atlas Schema 子文档，由 README.md 路由表按需加载。

# Quartz 网站部署

Agentic Work Atlas 通过 Quartz 自动部署为 GitHub Pages 网站。

## 关键配置

- **部署方案**: 仓库根目录作为 content，通过 `ignorePatterns` 排除无关文件
- **链接解析**: `markdownLinkResolution: "shortest"` 支持短链接跨目录

## ignorePatterns 排除内容

- 系统文件：`.obsidian`, `.git`, `.DS_Store`
- 配置文件：`package.json`, `quartz.config.ts`, `tsconfig.json`
- Schema 文件：`README.md`, `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`（兼容其他 AI 工具）
- 日志文档：`lint-report.md`
- 工具/插件目录：`tools`, `.agents`, `.claude`
- 其他目录：`docs`, `node_modules`