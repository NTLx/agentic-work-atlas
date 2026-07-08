---
title: "Gotchas 与调试技巧"
type: schema-subdoc
---

> 本文档是 Agentic Work Atlas Schema 子文档，由 README.md 路由表按需加载。

# Gotchas 与调试技巧

## 调试技巧

### 读取 git 状态中的 Unicode 文件名

```bash
# git status 显示的中文字符是编码格式，需要解码
python3 -c "import sys; print(sys.argv[1].encode().decode('unicode_escape').encode('latin1').decode('utf8'))" 'raw/文件名'
```

### GitHub Actions CI 构建失败诊断

```bash
# 1. 本地复现 CI 错误（--fix-index 自动修复 index 计数，--write-report 写入报告）
uv run --with pyyaml python tools/wiki-lint.py --fix-index --write-report
# 2. 只看阻断级问题（exit code 1 = 有阻断）；tag 问题是 non-blocking，不影响 CI
# 3. 修复后重新运行确认 "阻断问题: 0"
```

## Gotchas

### Unicode 文件名与 Read 工具

`Read` 工具无法直接读取含中文的文件名。改用 Python：
**根因**: Python 字符串中直接嵌入中文文件名会导致 SyntaxError（弯引号 U+201C/201D 与 ASCII 引号 U+0022 编码冲突）。
必须用 `os.listdir()` + `os.path.join()` 构建路径，不能硬编码文件名字符串。
```python
python3 << 'PYEOF'
import os
d = "/Users/lx/Obsidian/Clips/raw/"
files = [f for f in os.listdir(d) if "关键词" in f]
path = os.path.join(d, files[0])
with open(path, 'r') as f: content = f.read()
PYEOF
```

### 微信公众号文章剪藏不完整

Obsidian 浏览器插件剪藏 WeChat 文章会丢失正文段落。已入库 raw 不直接补写正文；应重新剪藏为新的 raw，或在 `wiki/sources/` 中记录缺口、补充来源与可信度。

补抓步骤：

1. 尝试用 Jina / Tavily Extract 抓取完整内容
2. 若被反爬拦截，尝试 `curl` 直接获取页面源码
3. 对比已有内容，确认缺失段落
4. 若需要完整原文，创建新的 raw 剪藏文件；不要在旧 raw 中补写正文
5. 清理新剪藏中的 `<!--rehype:style=...-->` HTML 注释标记

**图片缺失**: 微信图片使用 `data-src` 属性而非 `src`，需注意区分。

### source_raw Wikilink 引号编码一致性

Raw 文件名若含弯引号 `" "`（U+201C/201D），entity 的 `source_raw` wikilink 必须使用相同的弯引号，不能用 ASCII 直引号 `"`（U+0022）。验证时通过 Python `repr()` 逐字符检查 `ord(ch)`。
⚠️ 来源区块（## 来源）中的 wikilink 同样适用此规则。

### YAML 双引号值内含弯引号导致 Quartz 构建崩溃

YAML 双引号字符串 `"..."` 内包含弯引号 `"..."`（U+201C/201D）会导致解析器误判字符串边界，触发 `bad indentation of a sequence entry` 错误。
**修复**: 将包含弯引号的 YAML 值改用单引号包裹 `'...'`，单引号内弯引号无需转义。
扫描命令: `python3 -c "import os; [print(f) for f in os.listdir(path) if '“' in f or '”' in f]"`

### Quartz 日期格式要求

Quartz 构建要求所有日期字段（published/created/updated）为 ISO 8601 格式 `YYYY-MM-DD`。
- **中文日期**（如 `2025年12月29日`）不被接受，必须改为 `"2025-12-29"`
- **空 `published:`** 被 YAML 解析为 `null`，Quartz 报 warning。用 `created` 日期填充

### 编辑含中文文件名的文件

`edit` 工具同样受 Unicode 文件名限制。使用 Python `open(path, 'w')` 直接写入是可靠方案。

### ljg-learn 历史格式转换

部分 entity 文件仍保留 ljg-learn 八维拆解原始输出（`# 定锚 / # 八刀 / # 内观 / # 压缩`），
缺少标准 entity 格式。需转换为：`> [!definition] 定义` + `## 关键数据点` + `## 前提与局限性` + `## 关联概念`。
已修复 Taste/Judgment/Coding-Agents/Dan-Shipper，但仍需批量扫描确认。
**注意**: ljg-learn 技能已移除，新编译不再产生此格式；但历史遗留 entity 仍需清理。

### 文件末尾导航链接

部分 wiki 文件末尾有 `**返回**: [知识库索引](index.md)` 无意义链接。
Obsidian 不需要手动导航链接，应删除。扫描命令: `grep -r '\*\*返回\*\*' wiki/`

### X/Twitter Obsidian 剪藏 Author 格式

Obsidian Web Clipper 自动生成的 author wikilink 带 `@` 前缀（如 `[[@intuitiveml]]`），
不符合 kebab-case 规范。必须替换为纯文本作者名（如 `"Peter Pang"`），
待创建 Author Entity 后再改为 `[[Peter-Pang]]`。

### Obsidian 数学公式冲突（MathJax）

**本知识库中最高频的渲染崩溃原因**。任何包含 `$` 符号的文本（金额如 `$200`、缩写如 `$$$` 等），
都会被 Obsidian 的 MathJax 引擎当作行内公式处理，导致该段落及后续文本渲染崩溃。

**规则**：写入 Wiki/Schema `.md` 文件前，必须扫描全文中的 `$` 符号。raw 原文正文不因该规则改写：
- **反引号包裹**：`` `$200` `` — 推荐，显示为内联代码
- **反斜杠转义**：`\$200` — 渲染为纯文本

**Python 扫描命令**：
```bash
python3 << 'PYEOF'
import re, sys
path = sys.argv[1]
with open(path) as f:
    content = f.read()
for i, line in enumerate(content.split('\n'), 1):
    clean = re.sub(r'`[^`]+`', '', line)
    for m in re.finditer(r'(?<!\\)\$', clean):
        print(f"Line {i}: {line[m.start()-10:m.end()+10]}")
PYEOF
```

### source_raw 引用不存在的 raw（论文未剪藏）

编译 entity 时引用了学术论文标题作为 source_raw，但论文从未作为 raw 入库。
lint 会报 `source_raw 目标不存在`。
**修复**: 移除断裂的 wikilink；论文引用保留在正文中（如"Refusal-Compliance Tradeoff 论文（2026）发现…"），source_raw 只指向实际存在的 raw 文件。
**预防**: 编译时如果引用了论文，应先剪藏论文到 raw/，再在 source_raw 中链接。

### Entity 标准章节名称必须精确匹配

lint 检查概念 Entity 必须包含 `## 关键数据点`、`## 前提与局限性`、`## 关联概念` 三个章节。
**陷阱**: `## 关键证据`、`## 数据`、`## 相关概念` 等变体名称不被识别，lint 仍报缺失。
**修复**: 章节标题必须一字不差地使用规范名称。

### PDF 文件作为 Raw 来源

`raw/` 支持直接存放 PDF 文件（`.pdf` 后缀）。Quartz 以可下载附件展示，Lint 和 Registry 均正常追踪。

**PDF 与 Markdown raw 的差异**：

| 特性 | Markdown raw | PDF raw |
|------|-------------|---------|
| Frontmatter | 有 YAML | 无（元数据记录在 source summary） |
| 正文读取 | `read_text()` | Read 工具 `pages` 参数 或 PyMuPDF |
| body_sha256 | 文本哈希 | 二进制哈希 |
| 编译后标记 | `mark-compiled` | 同（不可遗漏） |

**完整工作流**：

```bash
# 1. 下载 PDF 到 raw/
curl -sL "<url>" -o raw/<YYYYMMDD>-<slug>.pdf

# 2. 提取文本用于编译（二选一）
# 方式 A：Read 工具（适合短 PDF）
#   Read tool, file_path=raw/<filename>.pdf, pages="1-20"

# 方式 B：PyMuPDF（适合长 PDF，输出更完整）
uv run --with pymupdf python3 -c "
import fitz
doc = fitz.open('raw/<filename>.pdf')
text = '\n\n---\n\n'.join(page.get_text() for page in doc)
with open('/tmp/paper_full.md', 'w') as f: f.write(text)
"

# 3. 正常编译（创建 source summary、entity 等）

# 4. 标记为已编译（关键步骤，不可遗漏）
uv run python tools/compile_registry.py mark-compiled "<filename>.pdf" \
  --summary-path "wiki/sources/<filename-stem>.md"

# 5. 运行 lint 验证
uv run --with pyyaml python tools/wiki-lint.py --fix-index --write-report
```

**常见遗漏**：编译完成后忘记执行 `mark-compiled`，导致 PDF 在 registry 中停留在 `pending` 状态，lint 报 `registry-consistency` 阻断。

### arxiv 论文剪藏：优先用 PDF

arxiv `/html/` 版本从 LaTeX 自动转换，新论文或复杂排版常截断（缺 Discussion/Conclusion/References）。
**始终优先用 PDF 版本剪藏**，直接存入 `raw/`：

```bash
# 下载 PDF 直接存入 raw/（无需提取为 md）
curl -sL "https://arxiv.org/pdf/<arxiv_id>" -o raw/<YYYYMMDD>-<slug>.pdf

# 如需提取纯文本（编译时使用）
uv run --with pymupdf python3 -c "
import fitz
doc = fitz.open('raw/<filename>.pdf')
text = '\n\n---\n\n'.join(page.get_text() for page in doc)
with open('/tmp/paper_full.md', 'w') as f: f.write(text)
"
```

提取后验证 Discussion / Conclusion / References 齐全，然后按标准编译流程处理。