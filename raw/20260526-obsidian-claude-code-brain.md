---
type: raw
title: "如何让 Obsidian 成为 Claude Code 的大脑，让你的 Agent 越用越聪明"
source: "https://mp.weixin.qq.com/s/9Bvxk04qXp4GwFaqbQhQdQ"
author:
  - "李祥瑞"
published: "2026-05-26"
created: "2026-05-29"
tags:
  - clippings
  - agent-memory
  - obsidian
  - claude-code
  - knowledge-management
  - skill-engineering
---

万涂幻象 MAGAZINEVOL.241 · 2026.05.26

ISSUE FEATURE: Obsidian × Claude Code × 知识管理

# 三层记忆 + 项目交班 + 自检体检：6 件小事让 Agent 每天比昨天更像我

我是祥瑞，万涂幻象多维表格社区的主理人，一个深耕飞书多维表格的 AI 落地实践者。

5 月 26 日今天下午两点二十五分，我们的社群里，一位群友扔了一句话进来：

我最近在各种研究 Token 都花哪去了。莫非真得用开源的 agent 来自定义。之前一直没研究，直到我发现，我发个你好，都能 8 万 Token 消耗。

群里一下就炸开了。

另一位伙伴接了一句："瘦身优化一下 obsidian。"

那位群友跟着补："经过各种学习，把 skill、记忆、工具调用都关掉了，agent 都傻了，发个你好，依然 2 万 Token。"

我看到的时候，心里咯噔了一下。

因为这就是大多数人开始养自己 AI Agent 时撞上的第一堵墙：你越往库里塞东西，它就越胖；它越胖，每次说话就越贵；可你又不敢给它减肥，怕减完它就傻了。

这篇文章就是这么来的。从看到题目到现在，半小时不到。

四月份我写过一篇《00 后一人公司，我是如何用 Obsidian、Claude Code 和 OpenClaw 做知识管理的》。那篇讲的是三端架构怎么打通：Obsidian 编辑、Claude Code 干活、OpenClaw 接飞书，共享同一个 Vault。

今天这篇接着写下面这件事：

架子搭起来之后，怎么让住在 Vault 里那个 Agent，每天比昨天更聪明一点。

先抛一个反直觉的结论。

让 Agent 越用越聪明这件事，跟 Agent 本身关系不大。你换 Claude、换 GPT、换 Gemini，差别没有想象中那么大。真正决定它聪不聪明的，是它住的那个文件夹长什么样。

换句话说：**聪明的不是 AI，是你的 Vault。**

这一个多月，我把 Vault 里专门给 Claude Code 用的那一层，拆成了六件事。下面一件件说。

## Vault 入口结构

Vault 的根目录有一份 CLAUDE.md，是 Claude Code 启动时第一份必读的文件。里面写着核心工作纪律、加载顺序、所有协议清单。CLAUDE.md 再指向 AGENTS.md，AGENTS.md 是通用的跨 Agent 规则：PARA 结构、frontmatter 规范、范围纪律之类。这两份加起来三百多行，是所有 AI 都要读的"公约"。

往下一层，是给 Claude Code 单独准备的 agent 目录。`00.系统/agent/` 下面挂着五个文件：

- `soul.md` —— 性格、交流风格、对人感的拿捏。需要确认语气时才读。
- `user.md` —— 用户档案，L1 持久画像。需要理解我背景时才读。
- `xianrui.md` —— 祥瑞调用手册，从过去几个月的对话历史和三份长画像里蒸馏出来的一份操作层手册。
- `memory.md` —— 程序性记忆，L2 索引。
- `skill.md` —— 技能索引。执行任务前匹配 skill。

这五个文件 Claude Code 不是一上来全读，而是按需加载。CLAUDE.md 第一节里就规定了什么场景读哪一份。

## 01 三层记忆，分开放

刚开始养 Claude Code 的时候，我把所有东西全塞在一个叫 memory.md 的文件里。今天聊出一个新判断，往里追加一段；明天跟群友讨论了个新观点，也追加一段；后天踩了个坑，再追加一段。两周下来，memory.md 长到三千多行。

每次对话开起来，Claude Code 先把这三千行 memory.md 全部读一遍，光这一项就吃掉它三万多 token。然后我跟它说一句"今天写个公众号"，它再去读一遍 skill，再去翻 Vault 总览，再读今天的对话日志。一句话还没说完，已经烧了八万 token。

后来我去翻 NousResearch 开源的 hermes-agent，看到他们把记忆分了三层，看完我整个人通透了。

通透在：记忆这件事，从来就不应该是一个文件。它至少是三件不同的事。

**L1 持久画像**：回答"用户是谁"。比如祥瑞是 00 后、INTP、做飞书多维表格社区。这种东西半年一年都不会变，是底层人设。

**L2 程序性记忆**：回答"这种事的标准做法"。比如"做完任何动作要 verify 一遍 final state 再上报"、"写公众号文章要先去 Vault 搜素材再下笔"。这种东西是程序性的、可复用的、被某次踩坑沉淀出来的判断。

**L3 历史检索**：回答"过去做过什么"。比如 5 月 17 日跟阿瑞调支付宝商户号那次、4 月 21 日 Vault 全面整改那次。这种东西是按天发生的事件流水。

改完之后：

- L1 持久画像放在 `00.系统/agent/user.md`，单文件，半年改一次。Claude Code 每次对话只在需要理解我背景的时候才去读它。
- L2 程序性记忆放在 `00.系统/agent/memory.md`，外加按主题切碎的小文件。Claude Code 启动时只读一个超薄的 MEMORY.md 索引，里面是几十行"标题 + 一句话钩子"。命中哪条再去读对应小文件。
- L3 历史检索放在按天分的日志里，超过一个月自动归档。Claude Code 平时根本不读它，只在我说"翻一下 5 月 11 日那次"的时候才去捞。

L3 这个层，光按关键词 grep 还不够。我还挂了一个叫 OpenViking 的开源工具做语义检索层。它是字节跳动火山引擎今年 1 月开源的一个上下文数据库，专门给 AI Agent 用的。

这三层一分开，最直接的效果是：每次对话启动 Claude Code 真正读进去的东西，从原来三万 token 砍到了不到三千。

更深层的效果是：Agent 不再"记忆腐化"。

**记忆腐化**是 hermes-agent 用的一个词。意思是：当你把"我是谁""我该怎么做""昨天发生了啥"全混在一个文件里时，时间一长，这三种东西会互相污染。昨天的临时决定被当成了长期判断，半年前的画像被今天的情绪覆盖掉。

分开放，每一层都按自己的节奏老老实实长着，不打架。

我在 CLAUDE.md 里给 Claude Code 写了一条死规矩：

- 写"祥瑞是什么样的人" → L1
- 写"这种事的标准做法" → L2
- 写"今天这件事发生了" → L3
- 混淆 = 记忆腐化

### obsidian_bridge.py

Obsidian 是个图形界面软件，它的搜索、标签、反向链接、孤岛检测，全都藏在 GUI 里。AI 拿不到。

所以我给它写了一座桥 `obsidian_bridge.py`，把 Obsidian 内部的所有能力全部暴露成命令行：search、tag、backlinks、orphans、unresolved、property read/set、outline、tasks 等。

## 02 让它自己交个班

每次对话结束的时候，Claude Code 自己得做一次交班。每次对话开始的时候，它也会自己"打卡上班"。

**打卡（开班）两件事**：

1. 跑 `vault_hook.py register`，注册 Obsidian 内部的文件变更监听。
2. 跑 `memory_recall.py "用户话题关键词"`，把跟当前话题相关的历史记忆从 OpenViking 语义索引里捞出来，作为暗背景上下文。

**交班（收班）五步协议**：

- **A. 跨对话有用的经验/决策/偏好**：聊出了可复用的经验教训？跑 `memory_update.py` 写进 L2。
- **B. 本次对话的事实流水**：完成了什么任务？跑 `conversation_log.py` 写进当天的 L3 日志。
- **C. 知识编译**：产出了值得让下次 AI 直接引用的东西？跑 `conversation_log.py distill` 编译成独立笔记。
- **D. 文件统计变动**：新增/删除/移动了笔记？跑 `update_vault_stats.py` 刷新 Vault 总览。
- **E. Self-check**：如果下一个新 session 完全没有当前对话的记忆，它能从 memory.md、对话日志、distill 里拿到所有需要的信息吗？

### memory_update.py 语义去重

`memory_update.py` 在写入前，会把"这次要写的这条"跟"已经在 memory.md 里的每一条"做一次语义比对。如果发现已经有一条说着差不多的事，就跳过不写；如果是补充细节，就 merge 进现有那条；只有真正新的判断，才会被追加进去。

### "吃一堑长一智"的闭环

举一个具体例子：5 月初我让 Claude Code 发公众号到飞书 wiki，标准 markdown 图片语法在飞书里全部解析失败。修通之后发现飞书云文档对图片的处理是两阶段的：先用 `media-insert` 拿 token，再用 `<image token>` 语法替换。

我让它记下来，写进了 L2 程序性记忆。三周之后，全新对话中让它发另一篇文章到飞书 wiki，没有任何提示，它自己先提取图片跑 media-insert，图全在。

三周前那一下午的踩坑，被它自己一次性买断了。

### distill：把对话变成资产

当一次对话产出了一份高密度内容，跑 `distill` 把它单独提取出来，编译成一篇独立笔记，挂到 `20.领域` 里。下次再有人问类似问题，Claude Code 不需要重新推导，直接引用蒸馏笔记就行。

## 03 项目工作笔记：PROGRESS.md

项目跟对话不一样。一次对话最长一两小时，项目可能持续两个月、半年。

给每个项目挂一个 PROGRESS.md 文件，作为这个项目永续存在的"工作笔记"。

每次 Claude Code 进项目目录干活之前，先跑 `project_init.py brief xxx`，把 PROGRESS.md 里的"项目目标/当前状态/最近三条决策/下一步"压成大概 300 字的摘要。300 字成本不到 500 token。

干活过程中：

- 完成任务：`project_init.py done xxx "做完的事"`
- 做决策：`project_init.py decision xxx "决策内容" "原因"`
- 发现下一步：`next xxx "下一步内容"`

**对话日志是会话级**，按天多文件，记录"今天我跟 AI 都聊了啥"。**PROGRESS.md 是项目级**，永续单文件，记录"这个项目从启动到现在走到哪儿了"。两个不会打架。

## 04 能力地图：一张表当员工手册

我电脑上装着的工具多得离谱。如果让 Claude Code 每次干活前自己去 `which` `--help` 摸索，光摸索就把 token 烧完了。

解法是一张能力地图 `reference_local_capabilities.md`。它的组织方式不是按"工具名"组织，而是按"我要做什么"组织——**反向索引**。

每一行格式：左边是"我要做什么"，右边是"用哪个工具最省事"。

CLAUDE.md 里的死规矩：执行任务前必查能力地图。按场景反向索引找最快工具链。禁止 which/--help 摸索。

对比：没有能力地图发一条飞书群消息要 5 分钟 5000+ token；有能力地图直接翻到"消息推送"那一行，2 秒 200 token。

能力地图本身也是活的。Claude Code 每次发现地图里没有但又用上了的工具，会自己提一句"能力地图需要更新这条"。

### Skill 系统

Skill 是一段给 Agent 看的工作流说明书。每个 skill 有 SKILL.md 主说明书、references 详细规则文件、scripts 脚本。

SKILL.md 不超过 200 行，只在触发时加载。里面用相对路径指向 references 目录的细则，真正要执行的那一刻才去读。

**Skill 内化**：我不直接安装别人的 skill。而是让 Claude Code 把别人的 skill 完整读一遍，提炼设计思想，结合我自己的语料和判断，重新长出一份属于我自己的版本。

安装是把别人的工具直接搬进你的工具栏，硬拼。内化是让 AI 把别人工具里的设计思想读懂，结合你自己的语料和判断，重新长出一份属于你的版本。

## 05 自己当自己的 QA

### 动作完成后必自检

CLAUDE.md 第 0 节，最顶上，写了一张自检表：

- 文件写入后立刻 verify 内容
- 脚本写入后跑 status 不 trust stdout
- iCloud 目录操作等 5-10 秒再查
- 大动作主动派复检 agent
- 完成后 verify final state 再上报

### PostToolUse Hooks

在 `~/.claude/settings.json` 里挂了三个 PostToolUse hook：

- `verify_edit.py` — Edit/Write/NotebookEdit 后自动跑 py_compile/shellcheck/validator
- `path_validator.py` — 校验路径是否落在 Vault 规定的目录里
- `frontmatter_enforcer.py` — 校验 frontmatter 合规（标题中文、tags 前缀、type 白名单）

### 定期自审

两个专门的体检 skill：

**vault-gardener**（每周日自动扫一遍整个 Vault）：

- 孤岛笔记（无反向链接）
- 坏链（wikilink 失效）
- 缺 frontmatter / 标签拼写不一致
- 目录命名违反 PARA 规则
- 三个月未更新且未被引用的笔记建议归档

**cc-health**（每月跑一次，专门扫 Claude Code 配置栈）：

- CLAUDE.md 规则与实际行为一致性
- rules 细则是否过时
- 90 天零命中 skill 候选下线
- hooks 执行链是否正常
- MCP 服务在线状态和调用频率
- 权限白名单是否过期

三层叠加：动作级自检 + 工具级 PostToolUse hooks + 系统级定期体检。

## 总结

Agent 越用越聪明，从来不是 Agent 本身变聪明，是它身后那个 Vault 越长越厚。

六件事：

1. **三层记忆**把它的脑子分清楚
2. **对话交班**让它自己沉淀经验
3. **PROGRESS.md** 让它跨对话续上故事
4. **能力地图**让它一眼找到工具
5. **Skill** 让它把工作流变成肌肉记忆
6. **自检 + Hooks + 定期体检**让它写出来的东西能直接用，也能自己代谢更新

本质上就是把人脑子里那些只有人知道的判断、规矩、习惯、踩过的坑，一点点搬到 AI 也能读到、能跑通、能照着做的地方。

Token 这件事，从来不是越少越好。它是越用得对，越值。
