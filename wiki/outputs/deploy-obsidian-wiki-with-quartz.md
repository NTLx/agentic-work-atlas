---
type: output
title: 将 Obsidian 知识库部署为 LLM Wiki 网站
created: 2026-04-13
updated: 2026-11-28
tags:
  - obsidian
  - llm-wiki
---

# 将 Obsidian 知识库部署为 LLM Wiki 网站

> [!warning] 2026-11-28 修订
> 旧教程以仓库根目录构建、未排除 Raw 为例，不能直接用于当前知识库或包含私有材料的 vault。本文改为基于当前 Agentic Work Atlas 仓库配置的部署设计与验收指南；旧版完整配置及历史 Clips 案例由 Git 保留。没有重新部署网站或检查线上实际产物。

## 1. 将知识编译与知识发布分开

LLM Wiki 的 Raw、稳定知识和 Schema 有不同职责。Quartz 是 Markdown 静态发布引擎，不执行知识编译、证据审查或权限治理。Obsidian 是本地编辑与导航工具；网页端可提供 wikilinks、搜索、图谱和反向链接，但不等于完整 Obsidian 功能或自动协作编辑。

现行仓库使用根目录作为 Quartz content 源，通过 ignorePatterns 限定发布范围。该方式便于维护同一份知识，但仓库内容默认不能视为可发布内容。

## 2. 发布边界

| 内容 | 当前仓库设计 |
|---|---|
| 正式公开知识 | index.md、wiki 下符合发布条件的 Entity、Topic、Comparison、Source Summary、Output、公开 Research |
| 原始证据 | raw/ 排除 |
| 内部运行状态与日志 | state/、wiki/research/research-logs/ 排除 |
| Schema、工具和测试 | schema/、tools/、evals/、tests/ 等排除 |
| Agent 配置、本地材料 | .agents/、.claude/、.obsidian/、docs/ 等排除 |

实际排除项以仓库当前 quartz.config.ts 和 schema/quartz-deploy.md 为准，而非本表的简化列表。

**重要区别**：Quartz 的 ignorePatterns 仅影响构建，不是 Git 仓库访问控制；将私有 vault 推送到公开仓库已经可能泄露其文件及历史。即使 Pages 不生成对应目录，搜索索引、摘要、附件、页面正文或其他公开文件仍可能泄露被引用的敏感信息。Explorer 隐藏与草稿过滤也不是访问控制。对外发布应优先使用经过授权的公开内容集，私有原始材料留在受控存储；在提交到 Git 之前检查秘密、版权及个人/企业数据。

## 3. 当前构建方案

仓库实际配置由以下文件控制：

- quartz.config.ts：发布过滤、Obsidian Markdown、短链接解析、搜索索引及静态资源。
- quartz.layout.ts：Explorer、Graph、Backlinks、Search、TOC 等布局。
- .github/workflows/deploy.yml：构建、验收、Pages 发布。
- schema/quartz-deploy.md：本库发布规范。

截至本次检查，workflow 固定 Quartz 源码 commit d25a6eabf96751ffca56f8a8139272def7a65041，使用 Node 22、npm ci，并复制仓库配置及可选 SCSS overrides。不要将旧版浮动 v4 分支或固定 Node 版本视为普遍兼容要求；以所用 Quartz 版本的依赖合同为准。

核心流程：

```text
checkout Atlas + pinned Quartz
  -> uv sync + wiki lint (as-of commit date)
  -> repository tests
  -> npm ci
  -> copy configuration
  -> npx quartz build -d ../atlas
  -> publication boundary check
  -> upload approved build artifact
  -> Pages deploy
```

当前 CI 明确检查 public/index.html 存在，并拒绝 public/raw、public/schema、public/state、public/tools、public/.agents、public/.claude、public/evals、public/wiki/research/research-logs 等目录出现。这是目录级门禁，不是所有内容安全的完整证明。

## 4. 独立部署的验收

先在非公开构建环境中验证：

1. 明确内容授权、Git 仓库可见性及部署访问控制；确认不向公开仓库上传私有 vault 或历史。
2. 核对锁定版本、构建依赖、Markdown 解析和链接解析。当前使用 shortest 模式，遇到同名页面时要检查实际解析结果。
3. 运行项目 lint 与测试，构建静态产物；检查实际输出的所有文件、搜索索引、附件和页面文本，不仅检查目录名称。
4. 在确认发布范围及权限后上传产物；检查实际部署 URL、访问权限、代表性页面与链接。若发生泄露，应停止发布、按实际暴露范围处置凭据与缓存等，不能仅靠删除导航链接。

上述流程是设计与验收建议，不表示本轮已运行 CI、执行部署或确认线上无泄露。

## 5. 参考

- [Quartz 官方文档](https://quartz.jzhao.xyz/)
- [Obsidian 官方网站](https://obsidian.md/)
- [[LLM-Wiki]]、[[Knowledge-Compilation]]、[[Obsidian-Wiki]]

## 本文使用的 Wiki 页面

- [[LLM-Wiki]]
- [[Knowledge-Compilation]]
- [[Memex]]
- [[Obsidian-Wiki]]

## 回填检查

| 判断 | 支撑依据 | 处理 |
|--------|----------|------|
| Raw、稳定知识与发布层分离 | Wiki: [[LLM-Wiki]]、[[Knowledge-Compilation]]；仓库实际 Schema | 保留 |
| Quartz 发布流程及目录门禁 | 本轮读取当前配置和 workflow | 保留在 Output，不升级为一般性部署结论 |
| ignorePatterns 不等同于访问控制 | 构建过滤与仓库权限是不同边界 | 保留为工程设计注意事项 |
| 实际线上部署及完整内容安全 | 未运行构建、未检查线上产物 | 待验证 |
