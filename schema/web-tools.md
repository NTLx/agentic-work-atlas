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

## Substack/Lenny's Newsletter 抓取模式

当 Jina 返回 `AuthenticationRequiredError: ... bad network reputation (AS36352)`，
或文章主页面是付费墙但页内嵌了 podcast transcript（如 Lenny's Newsletter）时，
用以下路径绕过：

### 1. 抓 HTML 找 transcript URL

```bash
curl -sL -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 ..." \
  "https://www.lennysnewsletter.com/p/<slug>" -o /tmp/article.html

# 在 HTML 中 grep Substack CDN 上的 transcription.json（带签名参数）
grep -oE "https://substackcdn.com/video_upload/post/20[0-9]+/[a-f0-9-]+/[0-9]+/transcription.json[^\"\\\\]+" \
  /tmp/article.html | sort -u
```

### 2. 定位当前文章的 post_id

文章 slug（`/p/<slug>`）和 post_id 都在 HTML 里。post_id 与文章 slug 在 React initial state 中**位置相邻**，
可用 Python 找 URL 偏移最接近 slug 出现位置的 transcription.json：

```python
import re
html = open('/tmp/article.html').read()
slug_pos = html.find('<article-slug>')
url_re = re.compile(r'https://substackcdn\.com/video_upload/post/(\d+)/[a-f0-9-]+/\d+/transcription\.json\?[^\"\\]+')
candidates = [(abs(m.start() - slug_pos), m.group()) for m in url_re.finditer(html)]
candidates.sort()
print(candidates[0][1])  # 最近的 = 当前文章的 transcript
```

### 3. 抓 transcript JSON 并清洗

```bash
curl -sL "<transcription_url>" -o /tmp/transcript.json
```

JSON 结构：`[{"start": 0.1, "end": 5.9, "text": "...", "words": [...]}, ...]`，含 word-level Whisper 置信度。
Raw 文件只保留 `text` 字段、合并段落即可：

```python
import json
data = json.load(open('/tmp/transcript.json'))
text = ' '.join(seg['text'].strip() for seg in data if seg.get('text','').strip())
```

### 4. 注意事项

- **签名 URL 短期有效**（小时级）：HTML 和 transcription.json 必须在同一会话内抓取，跨会话会 403
- post_id 是 Substack 内部递增 id，与发布时间正相关但**不**等于 slug
- 同时存在 `transcription.json`（带 speaker 对齐）和 `unaligned_transcription.json`（无 speaker label），
  选前者质量更好
- transcript 不属付费内容——这是 Substack 公开给搜索引擎索引的版本