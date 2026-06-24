---
title: "Obsidian 渲染规范"
type: schema-subdoc
---

> 本文档是 Agentic Work Atlas Schema 子文档，由 README.md 路由表按需加载。

# Obsidian 渲染规范

知识库的 Wiki 层 `.md` 文件最终在 Obsidian 中渲染。编写 `wiki/`、`index.md`、`README.md` 等 Agent 生成或维护的文档时，必须遵循 Obsidian Flavored Markdown 规范，避免渲染崩溃。`raw/` 是只读证据层，原文正文不因渲染清洗而改写；raw 渲染问题应在 source summary 或 lint 报告中记录。

## MathJax 冲突 — `$` 符号必须转义或包裹

Obsidian 使用 `$` 作为行内 LaTeX 公式分隔符。**任何 `$` 出现在正文中都会触发 MathJax 解析**，如果没有配对闭合的 `$`，会导致段落乃至整个文件渲染崩溃。

| 写法 | 效果 | 示例 |
|------|------|------|
| `$200` | ❌ 渲染崩溃（MathJax 当作公式起始符） | `Even if people paid $200/month...` |
| `$$value$$` | ❌ 渲染为数学公式 | `$$E=mc^2$$` |
| `` `$200` `` | ✅ 内联代码，正确显示美元符 | 价格、金额用反引号包裹 |
| `\$200` | ✅ 转义，渲染为文本 | `Even if people paid \$200...` |

**规则**: 编写 Wiki 层内容时，包含 `$`、`$xx`、`$$$` 等美元符号的文本必须用**反引号包裹**或用**反斜杠转义**。raw 原文中的美元符号不作为编译阶段改写理由。

## 常见渲染问题对照表

| 问题 | 原因 | 修复 |
|------|------|------|
| 整段文字消失或变成公式 | `$` 触发 MathJax | 反引号包裹 `` `$200` `` 或转义 `\$200` |
| 粗体/斜体不生效 | `*` 数量不匹配 | 检查配对 `*text*` / `**text**` |
| 引用块断裂 | 空行未加 `>` 或加了多余 `>` | 多段引用用 `>` 开头 + 空行分隔 |
| 表格列不对齐 | 每行 `|` 数量不一致 | 确保表头、分隔线、数据行列数一致 |
| 链接变文本 | wikilink 含空格 | 使用 kebab-case：`[[AI-Psychosis]]` |
| YAML 解析失败 | frontmatter 中出现特殊字符未引号包裹 | 值用双引号包裹 `"value"` |
| YAML 解析失败 | 值含弯引号 `""` (U+201C/201D) | 改用单引号包裹 `'value'` |

## 编写前检查清单

在写入任何 `.md` 文件前，Agent 必须调用 **obsidian-markdown** 技能进行格式校验。

1. **调用 obsidian-markdown 技能**：确保 Obsidian Flavored Markdown 合规（wikilink、callout、properties 语法，避免 MathJax 冲突、emphasis 错位、frontmatter 错误）
2. **aliases 字段**：Entity 必须包含 `aliases` 字段，值为自然语言名称（供 Obsidian "未链接提及" 识别）
3. **`$` 符号扫描**：新写入的 Wiki/Schema 正文无裸露的 `$`；raw 原文正文不做清洗式改写
4. **emphasis 配对**：`*` / `_` / `~` 成对出现
5. **YAML 有效性**：frontmatter 中 special chars（`#`, `:`, `{}`, `[]`, `&`, `*`）必须用引号包裹
6. **wikilink 格式**：双括号内使用 kebab-case，无空格；正文引用优先使用管道语法 `[[Kebab-Case|Natural Name]]`
7. **无隐藏字符**：无 BOM、零宽字符（U+200B 等）

## 快速诊断命令

对可疑文件运行 Python 检查：

```bash
python3 << 'PYEOF'
import re
path = "/path/to/file.md"
with open(path, 'r') as f:
    content = f.read()
for i, line in enumerate(content.split('\n'), 1):
    clean = re.sub(r'`[^`]+`', '', line)
    for m in re.finditer(r'(?<!\\)\$', clean):
        print(f"Line {i}: Unwrapped $ at: ...{line[max(0,m.start()-15):m.start()+15]}...")
PYEOF
```