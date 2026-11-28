---
type: entity
title: Headless Mode
aliases:
  - Headless Mode
definition: "Claude Code 的非交互模式，通过 -p 参数实现单次执行并输出到 stdout，适合自动化和 CI/CD 场景"
created: 2026-04-09
updated: 2026-11-28
evidence_level: medium
claim_type: mixed
tags:
  - AI-Agent
  - Claude-Code
  - Automation
related_entities:
  - '[[Claude-Code-CLI]]'
  - '[[Agent-Orchestration]]'
source_raw:
  - '[[OpenClaw + 6 个 Agent 运转半个月，从聊天到干活的完整工程实践]]'
  - '[[OpenClaw + CodexClaudeCode Agent Swarm The One-Person Dev Team Full Setup]]'
---

# Headless Mode

> [!definition] 定义
> Headless Mode（非交互模式）是 Claude Code 通过 `-p` 或 `--print` 参数运行的模式，实现单次执行、输出到 stdout，适合自动化脚本、CI/CD 和 OpenClaw 编排场景。

## 基本语法

```bash
# 基本用法：-p 或 --print
claude -p "分析这个项目的架构"

# 指定输出格式
claude -p "总结项目" --output-format text    # 纯文本（默认）
claude -p "总结项目" --output-format json    # JSON 带元数据
claude -p "总结项目" --output-format stream-json  # 实时流式 JSON
```

## 关键 Flags

| Flag | 用途 | 示例 |
|-----|------|------|
| `--allowedTools` | 匹配的工具调用免交互确认，不等于排除其他工具 | `--allowedTools "Read,Grep,Glob"` |
| `--tools` / `--disallowedTools` | 前者限制内置工具集合，后者设置拒绝规则；仍需核对 MCP、配置与 OS 边界 | `--tools "Read,Grep,Glob"` |
| `--max-turns` | 限制执行轮次（防止无限循环） | `--max-turns 5` |
| `--model` | 选择模型 | `--model opus` / `--model sonnet` |
| `--permission-mode` | 设置权限模式 | `--permission-mode plan` |
| `--session-id` | 指定有效 UUID，不是恢复命令 | `--session-id 550e8400-e29b-41d4-a716-446655440000` |
| `--resume` / `--continue` | 恢复指定会话或最近会话 | `--resume <session-id>` |
| `--output-format` | 输出格式 | `text` / `json` / `stream-json` |

## OpenClaw 调用模式

**关键原则**：不要尝试"驱动 TUI"，把 Claude Code 当作 CLI 工具用。

```bash
# 模式一：单次任务（最常用）
claude -p "实现用户认证功能，运行测试，总结变更" \
  --allowedTools "Read,Write,Edit,Bash" \
  --max-turns 10 \
  --output-format json

# 模式二：管道输入
cat error.log | claude -p "分析错误日志，找到根本原因"
git diff HEAD~1 | claude -p "审查这个 diff，列出潜在问题"

# 模式三：使用首次运行返回的 session_id 恢复会话
claude -p "分析 src/ 目录的代码" --output-format json
# 将 SESSION_ID 替换为实际返回的 session_id
claude -p "刚才发现了什么 bug？" --resume "$SESSION_ID" --output-format json
```

## JSON 输出格式

使用 `--output-format json` 时，返回结构化数据：

```json
{
  "result": "Claude 的回答文本",
  "session_id": "xxx-xxx",
  "total_cost_usd": 0.05,
  "duration_ms": 15000,
  "num_turns": 3,
  "usage": {
    "input_tokens": 5000,
    "output_tokens": 1200
  }
}
```

## CI/CD 集成示例

```yaml
# GitHub Actions 示例
- name: Review PR
  env:
    ANTHROPIC_API_KEY: `${{ secrets.ANTHROPIC_API_KEY }}`
  run: |
    claude -p "Review the code changes for security issues" \
      --tools Read,Grep,Glob \
      --allowedTools Read,Grep,Glob \
      --permission-mode dontAsk \
      --max-turns 3 \
      --output-format json > review.json
```

## 与交互模式的对比

| 特性 | 交互模式 | Headless 模式 |
|-----|---------|--------------|
| 启动方式 | `claude` | `claude -p "..."` |
| 适用场景 | 人工操作、实时调试 | 自动化、CI/CD、编排 |
| 输出方式 | 终端交互 | stdout（可捕获） |
| 权限处理 | 依实际权限模式/配置 | 预配置规则、权限回调或拒绝无法批准的请求 |

## 关键数据点

- 基本语法：`claude -p "任务描述"` 或 `claude --print "任务描述"`
- 三种输出格式：text（默认）、json（带元数据）、stream-json（实时流式）
- 关键 flags：--allowedTools、--max-turns、--model、--permission-mode、--session-id、--output-format
- JSON 输出包含：result、session_id、total_cost_usd、duration_ms、num_turns、usage
- 在 OpenClaw 中，通过 PTY 模式调用 Headless 模式实现自动化编程
- Elvis Sun 的实践：使用 tmux 而非直接的 -p 模式，支持 mid-task 重新定向（`tmux send-keys`）

## 前提与局限性

- **前提**：使用该运行环境支持的认证与模型访问方式；API key 并非所有使用方式的必要条件。
- **边界条件**: Headless 模式适合单次任务和自动化流程，不适合需要频繁交互的探索性开发
- **局限性**：JSON 消息封装及业务结构不同；当前官方支持 `--json-schema` 约束结构化结果，仍应解析、检查实际错误与终态。示例字段仅作示意。
- **局限性**：无人值守应有明确拒绝策略；SDK/权限提示 host 可提供交互式审批，不能笼统说 headless 无法实时授权。
- **局限性**: `--max-turns` 限制可能导致复杂任务未完成就被截断，需要合理设置
- **局限性**：会话恢复不等于持久任务状态或成功恢复外部副作用，仍需检查点及幂等策略。以上 CLI 语义据 [官方 CLI reference](https://code.claude.com/docs/en/cli-reference) 与 [headless 文档](https://code.claude.com/docs/en/headless)（2026-11-28 核验），旧版本须核对实际帮助，未在本机执行。

## 关联概念