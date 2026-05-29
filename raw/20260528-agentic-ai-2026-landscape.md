---
type: raw
title: "Agentic AI 2026：当黑客松式的狂欢冷却下来"
source: "https://mp.weixin.qq.com/s/sYpVDlaEpNvZYDCeP421sA"
author:
  - "王旭"
published: "2026-05-28"
created: "2026-05-29"
tags:
  - clippings
  - agentic-ai
  - open-source
  - developer-ecosystem
  - agent-infrastructure
---

**从去年末到今年初，在 Coding Model 的推动下，以 OpenClaw 的爆火为高潮的 Agent 陡增现象，让我们感觉到 Agentic 就是答案。** 而我们的开源社区数据似乎也印证了这个感受，套用古罗马诗人贺拉斯的句式，我们可以说 Agens uno minor est modulo —— 「模型之下，Agent 凌驾一切」。当然，我们的数据对于碳基和硅基开发者们的行为和趋势也做了一系列分析，下面就是我们的详细报告了。

**蚂蚁开源技术委员会副主席**

**王旭**

过去一年，我们一直用"真实世界里的黑客松"来形容大模型开发生态。这个比喻很准确。它有热闹、速度、偶然、天才时刻，也有混乱、重复、短命项目，以及那些一夜之间被全世界看到、又很快被新的热点盖过去的仓库。

但到了 2026 年中，体感已经不太一样了。变化不再只是"又多了几个 Agent 项目"。更底层的东西开始松动：软件生产模式本身在移动。

过去，人使用软件。软件围绕人的手、眼睛和注意力设计：按钮、表单、编辑器、聊天框。现在，Agent 开始成为软件的新用户。它读文件，调用 API，跑命令，发 PR，写测试，做代码审查，等待人类确认后继续下一步。它不总是坐在聊天框里，也不只是回答问题。它开始进入软件世界的内部工作流。

所以，"Agentic AI 有没有泡沫"不是最值得纠缠的问题。泡沫当然有，而且不会少。更值得问的是：

- 当黑客松式的狂欢冷却下来，软件会走向哪里？
- 开发者会变成什么？
- 开源还剩下什么位置？
- 以及，为什么我们需要一个 inclusive AGI 的未来？

## 平台传来的生态信号

### 模型没有让软件变少，反而让软件的边界变宽了

如果只看发布会，我们很容易以为 AI 的主角只有模型。但如果把 GitHub 和 Hugging Face 的数据在一起看，会看到另一幅图景。

GitHub 告诉我们开发者在造什么。Octoverse 2025 显示，GitHub 已有 1.8 亿以上开发者，2025 年新增超过 3,600 万开发者，平均每秒新增 1 人。2026 年 1 月到 4 月，OpenDigger 事件流里活跃过的开发者达到 1301.6 万，活跃仓库达到 2710.7 万。软件生产没有因为模型变强而萎缩，它仍然在扩张。

更有意思的是自动化账号。2017 年前四个月，GitHub 事件流里活跃的 bot/app actor 只有 112 个；到 2026 年同期，这个数字变成 17,285 个。十年窗口里增长了 **154** 倍，而且 2026 年前四个月已经超过 2025 年同期的两倍。今天的开源协作现场，已经很难再想象成"人类开发者在 GitHub 上协作，旁边有几个 CI bot 打杂"。自动化账号正在进入软件生产链路，成为协作网络的一部分。

HuggingFace 提供的是另一种信号。它告诉我们模型如何被发布、下载、改造和再生产。公开模型数量已经达到 200 万，过去一年数量增长超过 100%，2026 年截至 5 月也已经新增 54 万以上。模型平台早就不只是论文模型的陈列柜了，更像一个很忙的加工厂：有人发布 foundation model，有人 fine-tune，有人量化，有人转换格式，有人上传 adapter，有人把同一个能力搬到不同设备和运行环境里。

再看 GitHub 协作榜和 Star 增长榜，AI 项目已经挤进核心工程世界，开发者的情绪和好奇心更是集中在 **Agent**、**Claude Code**、**Skills** 这些新词儿的周边仓库上。但真实协作仍然围绕软件世界的长期工程底座和复杂系统展开。换句话说，模型没有把软件吃掉，它在重写软件的分工。

模型负责理解、生成、推理和调用工具；软件负责把模型放进可靠的工作流里，管理数据、权限、状态、成本、审计和交付。越是让模型接近真实工作，越需要软件去定义边界、保存过程、连接系统、处理失败。模型没有让软件变少，反而让软件的边界变宽了。

## Agentic AI 生态架构

### 生态结构从 LLM 工具链，转变为通往 Agentic AI 的一整套执行栈

去年我们做大模型开发生态全景时，核心问题还是：哪些项目值得放进这张图里？那时生态还在围绕 LLM SDK、RAG、Agent Framework、应用平台、推理基础设施慢慢分层。大家关心怎么接模型、怎么做 RAG、怎么写一个 Agent、怎么把推理服务跑起来。

到了 2026 年，这个问题变难了。项目太多，变化太快，连很多老项目也在重新定义自己。

OpenClaw 从 2025 年 11 月上线，到 2026 年 2 月冲过 20 万关注，只用了 84 天。而定义了现代前端开发的软件基础设施 React，达到这个数字用了将近十年。这并不意味着它已经拥有 React 那样的长期工程影响力，但它说明 GitHub 的注意力分发机制、AI 时代的传播速度，以及开发者对 Agentic 软件的期待，都变了。

项目冒出来太快，热度也变得太快。只做一张静态图，很容易只留下某个瞬间。于是这次我们把两件事分开做：全景图负责判断，选出当下最有代表性、最值得关注的一批项目；动态排行榜负责看水温，追踪开发者真实参与过的 Agentic AI 项目，看看哪些项目突然热起来，哪些热度留下来了，哪些开始出现真正的协作。

这个和 OpenDigger 合作的动态排行榜已经在 inclusionAI 官网上线：https://www.inclusion-ai.org/insight

最新一月的 OpenRank Top 10 很像一张生态横截面：Claude Code、Codex、OpenCode、Gemini CLI 站在任务入口这一侧，vLLM、SGLang、TensorRT-LLM、PyTorch 站在底层基础设施这一侧。入口项目离开发者和用户更近，issue 和 PR 会更热闹；基础设施项目参与者没那么分散，但协作密度很高。真正升温的不是某一个入口，而是一整套执行系统。

生态结构的变化也很清楚：2025 年，landscape 还在梳理 SDK、RAG、ChatUI 和 MLOps；2026 年，头部项目已经围绕 Agent 的任务执行系统重排。

去年 5 月的 landscape 还带着很强的 LLM 工具链味道。那时我们主要在看，用什么 SDK 构建 LLM 应用，用什么 RAG 和向量库接数据，用什么推理框架把模型跑起来。到了 2026 年 5 月，重点已经从"怎么写 Agent"，变成"Agent 如何进入任务执行"。

所以我们再看 2026 年的 Agentic AI 三层架构，就会更容易理解：上面有人机协作和任务入口，中间有 token 的供应和调度，下面还有模型能力本身。

- **Agent Infra 决定 AI 能替谁做事。** 它包括用户直接遇到的入口，比如 Coding Agents；也包括 Agent Runtime Infra，比如 Context、Tool Use、Sandbox、AgentOps；还包括 Agent Builder、Orchestrator 和 Operator。
- **Model Infra 决定这件事能不能规模化。** 它包括数据、训练、推理服务、部署、调度和运维。Agent 如果只是回答一句话，底层成本还可以被忽略；一旦它开始连续读代码、查资料、调用工具、等待反馈再继续执行，token 就从聊天消耗变成了生产资料。
- **Model 决定能力边界在哪里。** 模型层仍然重要，但它已经不能只用"谁的 benchmark 更高"来理解。前沿和基座语言模型探索上限，端侧小模型解决低成本、低延迟和隐私场景，专有模型适配代码、金融、服务业。真实任务会越来越像模型组合，而不是单模型统治。

这三层不是简单的上下游，更像互相推着往前走。Agent 想做更长的任务，会逼着 Model Infra 降低推理成本、提高上下文吞吐和可观测性；Model Infra 变强，小模型和专用模型才更容易进入生产；模型层在推理、工具调用、多模态上的提升，又会把 Agent 继续推出聊天框。

## Agent Infra：重新定义软件如何被使用

Agent Infra 是这次数据里最热闹、也最容易被误读的一层。表面上看，是 OpenClaw、Claude Code、Codex、这些产品在抢注意力；往深处看，其实在重新定义"软件如何被使用"。**Agent Infra 做的事，可以说是把"硅基执行者"接进软件世界。**

**Coding Agent 是 Agentic AI 第一波真正规模化的入口，因为代码世界天然适合 Agent 工作。它有文件，有测试，有日志，有版本控制，有 diff，有 PR，有 review，有回滚。机器需要的反馈系统，代码世界几乎都已经准备好了。**

过去，软件默认的使用者是人。我们为人设计 UI，为人写文档，为人提供按钮和表单。Agent 时代，软件多了一个新使用者。这个使用者不一定需要漂亮界面，但需要稳定 API、工具协议、权限边界、可读状态、可执行命令、可验证结果、可回滚操作。

一个 Agent 如果没有上下文，只是短暂清醒；没有工具，只能停留在建议；没有权限控制，无法进入真实系统；没有沙箱和回滚，企业不敢让它动手；没有观测和评估，人类无法知道它为什么失败。

软件正在被重新包装为 Agent 可进入的运行环境，API、MCP、工具协议、上下文、沙箱和观测成为新的基础部件。

我们把 226 个项目的 description 和 README 交给模型，做了一套多标签分类。结果很有意思：

- **Coding Agent** 有 78 个项目、14,019 名参与者
- **MCP** 有 59 个项目、6,651 名参与者；
- **Memory** 有 70 个项目、7,609 名参与者
- **Observability** 有 71 个项目、5,463 名参与者
- **Gateway** 有 31 个项目、2,637 名参与者。

标签之间有重叠，不能简单相加，但横向看已经够了：注意力正在从"做一个会聊天、会写代码的产品"，转向把上下文、工具、网关、沙箱和观测装进一套运行时。

## Model Infra：规模化供应 Token 是重心

**推理层正在出现几种分工。** 以 vLLM、SGLang 为代表的高吞吐引擎负责把模型更快、更稳、更便宜地跑起来；以 llama.cpp 为代表的边缘和本地推理把模型带到个人电脑、私有环境和端侧设备；以 Dynamo、Ray Serve 为代表的数据中心级调度负责多模型、多租户、多 GPU、多地域运行；以 LiteLLM、OpenRouter 为代表的网关和代理负责模型路由、降级、统一接口、成本追踪和审计。

**后训练也是这一层的重心之一。** AReaL、Slime 这些项目代表 Reasoning 训练和 agenticRL 的上升。Agent 时代的 RL，目标不止是让模型回答得更好，还要让它更会调用工具、更会遵守约束、更会在长任务里保持状态，也更知道什么时候该停下来问人。

**未来的 AI 成本优势，不只来自更便宜的模型，也来自更好的 token 供应链管理。** Model Infra 的价值，就是把这些能力像电力、物流和数据库一样编排起来。谁能让 token 稳定、便宜、可观测、可治理，谁就在 Agent 时代掌握真正的生产基础设施。

这很像云计算早期的演化。最开始大家关心"能不能把服务跑起来"，后来真正的竞争变成调度、弹性、观测、成本、SLA、供应链和开发者体验。Model infra 也在走这条路。

更硬的证据来自社区本身。2026 年 5 月中旬，头部的 Serving 项目保持着高频 build 节奏。Release note、roadmap issue 和 bug report 里反复出现的词语是：PD disaggregation、KV cache、router、scaling、fault tolerance、health check。

SGLang issue #21846 把最新的路线图命名为 "Distributed KVCache System For Agentic Workload"，明确写到 agentic workloads 正在带来 KV cache storage 与 transfer volumes 的快速增长，现有 PD 分离和 HiCache 已出现瓶颈。**Agent 改变了 token 的消费结构。**

Dynamo issue #5506 的 H1'26 roadmap 强调的是请求如何被调度、KV cache 如何复用、不同 worker 如何扩缩容、服务如何在 Kubernetes 和多节点环境里保持可用。**Serving 战场正在从单个推理引擎扩展到推理系统。**

还有一条 Issue（SGLang issue #20252）记录了一个很真实的大规模部署故障：qwen3-32b-fp8，90 个 prefill 加 30 个 decode，跑在 H20 集群上。部分 prefill 节点重启或迁移后，decode 不断重试，健康检查失败，router 移除 worker，流量压到剩余节点，最后在高 QPS 下出现 cascading failure 和 503。这个案例很有提醒意义：模型能跑起来只是第一步，一台节点的波动会不会顺着路由、健康检查和流量转移放大成全局故障，才是工业化推理绑不开的问题。**工业场景真正痛的是稳定性。**

## Model：没有单一冠军

模型层仍然是整个生态的能力源，但它已经不能只用"谁的参数更多、谁的 benchmark 更高"来理解。

Hugging Face 的衍生和下载的数据提醒我们，模型的生命力不会停在发布那一刻。Qwen、Gemma 等模型家族之所以重要，不只是因为它们本身强，也因为它们被 fine-tune、量化、转换、蒸馏、迁移到各种边缘设备和应用场景里。模型开始像开源软件包一样拥有下游生态：有人 fork，有人 patch，有人做轻量版，有人做领域版，有人做兼容层。

OpenRouter 的 token 调用榜则把"单一冠军模型"的叙事拆开了。写代码可能用一个，长上下文研究用一个，低成本批处理用一个，语音、图像、视频再用另一个，本地隐私场景又是另一套选择。真实使用很难稳定收敛到一个永远的冠军。用户会在价格、速度、上下文、工具调用、编程能力和免费额度之间来回路由。

这个判断已经有论文和工程实践在支撑。ICLR 2025 的 RouteLLM 做了一个很直观的对照实验：先判断问题难度，再决定用强模型还是便宜模型，而不是每个问题都交给最贵、最强的模型。在一些 benchmark 上，这种路由方式能在效果接近强模型的情况下，把成本降到原来的二分之一以下。EMNLP Industry 2025 的 IPR 把这件事放到了大型云平台部署环境里验证：它在 Claude 系列模型之间做 prompt routing，在质量达到最强 Claude 模型水平的同时，把成本降低了 43.9%。

开源社区里的需求也在往这个方向走。最火的模型 API 路由项目 LiteLLM 仓库中的 GitHub Search API 检索显示，和成本、预算、花费治理相关的路由关键词频繁出现在 issue 和 PR 里：cost based routing 相关结果 23 条、lowest cost 相关结果 18 条、budget routing 相关结果 37 条、spend tracking 相关结果 76 条（检索时间：2026 年 5 月 22 号）。工程团队已经在问：在保证质量和稳定性的前提下，如何把请求路由到更合适、更便宜、更可治理的模型上。

## 趋势与项目故事

### 技术趋势的变化，也发生在项目如何描述自己

### Description Signals：项目正在重写自己的自我介绍

分类和排行榜能看到结构，但它们还是有点抽象。很多更有味道的变化，藏在项目自己的 description 里，也藏在 README 里那些反复出现的"我不是什么"。

把历史 landscape 快照和当前项目数据对齐后，我们发现 226 个项目里有 96 个改过 description。新增最明显的词包括 agent、harness、context、workflow、mcp。这些表述上的更新，是项目在重新给自己找生态位置。

这些变化沿着一些典型迁移路径往 Agent 执行栈靠拢。

1. 一条常见路径是 **Workflow Builder → Agent Orchestrator**。Dify、Flowise、Langflow、Activepieces 这类项目，本来解决的是"怎么搭一个 LLM 应用或自动化流程"，现在越来越强调 agentic orchestration。Deer-flow 是这条线里更锋利的一个样本：它之前说自己是 community-driven Deep Research framework，强调 web search、crawling、Python execution；现在则把自己改成 long-horizon SuperAgent harness，能够 research、code、create。Deep Research 开始从"帮你查资料"，走向"长周期任务执行器"。

2. 另一条路径是 **RAG / Data / Vector DB → Context / Memory Infra**。RAGFlow、Chroma、DataChain、Letta 这组项目让人看到，RAG 和数据正在从"给模型补知识"往外长，变成 Agent 的长期上下文、记忆层和可检索工作台。DataChain 从 ETL / analytics / versioning 变成 unstructured data 的 Context Layer，Chroma 从 embedding database 变成 Search infrastructure for AI，Letta 从 memory services 变成 stateful agents platform，都是同一条暗线。

3. 还有一条靠近用户入口的迁移：**Chatbot / AI Client → Agent Workspace / Personal Assistant**。lobehub/lobehub 特别值得单独看。它以前的 description 还叫 Lobe Chat，是一个 modern-design AI chat framework；现在的表述变成用户可以 find、build、collaborate with agent teammates。LobeChat 这样的 chatbot 项目，正在主动逃离"聊天框"这个名字和想象力。它没有停在"我也是 agent"的表态上，而是在把产品从 Chat 改写成 Hub：从人和模型对话，变成人和 agent teammates 共处、协作、分工。

4. 更靠近开发者工具的一条路径是 **Dev Tool / IDE / Terminal → Agentic Dev Environment**。Warp、Daytona、Coder、Continue、Cline 这些项目正在把开发工具改写成 Agent 的工作环境。Warp 从带 AI 的 terminal 变成 agentic development environment；Daytona 从 dev environment manager 变成 running AI-generated code 的安全弹性基础设施；Continue 从 AI code assistant 转向 source-controlled AI checks 和 CI 里的质量门禁。这里的变化很关键：软件入口正在从"人打开 IDE 写代码"，变成"人定义目标，Agent 在受控环境里执行"。

5. 在框架层，很多项目从 **Framework → Agent Harness**。LangChain、deepagents、Mastra、Agno、Hive 这类项目不再满足于说自己是 framework 或 SDK，开始向 platform、harness、production AI 靠拢。harness 是这组变化里很有味道的词。在 96 个 description 变化项目里，当前 description 含 harness 的有 6 个，其中 4 个是后来新增，包括 deer-flow、LobeHub、Hive。

6. 在工具和网关层，变化是 **Tool Integration → Agent Control Plane**。Composio、LiteLLM、OpenSandbox 这类项目，把工具调用从 "function calling / API wrapper" 推向了更像控制平面的东西：ComposioHQ/composio 原来强调 integrations / function calling，现在改成 powers 1000+ toolkits、tool search、context management、authentication 和 sandbox。它几乎把 Agent Infra 的几个关键词都写进了一句话里。

7. 在模型基础设施层，则出现了 **RL / Inference / Training → Agent Workload Infra**。AReaL、verl、SGLang、GPustack 等项目说明，Agentic AI 改写的不只是应用层，也包括 Model Infra。areal-project/AReaL 之前是 Distributed RL System for LLM Reasoning，现在变成 The RL Bridge for LLM-based Agent Applications。后训练正在被 Agent 任务重新定义：模型光"答得对"还不够，还要在工具调用、长任务、环境反馈和多步决策里"做得成"。

这类变化有时会被误读成"大家都在蹭 agent 热点"。蹭热点的项目当然存在，任何快速扩张的生态都会有这种噪音。但当一个成熟项目改 description，往往意味着它已经感受到了用户需求的变化。

Agentic AI 把原来分散在应用层、数据层、开发工具层、MLOps 层、云原生层和模型层的项目重新拉到一起。RAG 项目开始讲 context，数据治理项目开始讲 Agent 可用的语义层，开发环境开始讲 developers and their agents，网关项目开始讲模型路由和成本控制。每个项目都在问：如果我的用户不只是人，还有 Agent，我应该提供什么？

### README Evidence：项目说自己"不是什么"

README 里的否定句则提供了另一种证据。当一个项目反复说 "not a..."，它往往不是在解释功能，而是在摆脱上一代生态标签。

OpenFang 把自己称为 Agent Operating System，同时明确排除 chatbot framework、Python wrapper around an LLM、multi-agent orchestrator 这些标签。这个表达很直接：chat window、薄 SDK、简单编排，都已经不足以承载它想争夺的位置。它想把自己放在 OS / runtime 层。

Paperclip 也很类似。它一口气排除了 chatbot、agent framework、workflow builder、prompt manager、single-agent tool、code review tool，转而强调自己要运行由 agent 组成的 **0 人公司**。

这些否定句背后有一组正在退潮的标签：chatbot framework、LLM wrapper、workflow builder、prompt manager。

用户不再满足于一个漂亮的聊天页面、一个模型接口中转站、一个 demo workflow，而是在问更具体的问题：

- **Agent 如何接入真实软件？**
- **权限如何管理？上下文和记忆如何长期维护？**
- **失败如何观测？**
- **代码执行如何进沙箱？**
- **模型调用成本如何控制？**

这才是 Agentic AI 从玩具走向生产的分水岭。

## 开发者与 AI 工具

### AI 工具越强，人的责任越重

### 谁在参与 Agentic AI 生态？

在讨论"模型会不会吞噬软件和开源"之前，先看一眼开发者本身的变化。

我们用 226 个 Agentic AI 项目做了一次开发者画像：统计 2026 年 1 月 1 日到 5 月 1 日之前参与过这些项目的 actor，保留 bot/app 账号，得到 563,973 个开发者或自动化账号；再按 2026 年 4 月在这些项目中的 community_openrank 贡献度取 Top 10,000，并补充 GitHub profile、company、location。其中，约 2.0% 是 likely bot / app actors，也就是 198 个自动化账号。

这 10,000 个高贡献参与者里，profile 可识别的公司有 2,920 个，标准化国家有 3,575 个。自报公司里，NVIDIA、Microsoft / GitHub、Intel、Google / DeepMind、Red Hat 都进入前列；标准化国家里，美国 1,113、中国 726、印度 229。这里看不到一个单一的"开源爱好者"群体，看到的是一张由模型公司、云厂商、芯片厂商、创业团队、大学实验室、独立开发者和自动化账号共同构成的网络。

这里有三个有意思的信号。

- **第一，Agentic AI 的贡献重心没有只落在"应用创业公司"上。** openclaw 这样的 Agent / model-native 项目当然显眼，但 apache、pytorch 也在前列。Agentic AI 的生产网络已经跨过应用层：有人在做 coding agent，有人在做模型和推理，有人在做数据、工作流和工程基础设施。
- **第二，自报 company 显示，芯片厂商、云与模型厂商、开源基础设施公司同时在场。** 底层算力和推理栈正在被 Agent 需求重新拉动；大厂也在通过开源项目进入工具链和开发者工作流；Red Hat、Databricks 这类基础设施公司，则代表企业级工程和数据平台正在接入 Agentic 叙事。
- **第三，地理分布并没有收敛成单一硅谷故事**。美国仍然是最大节点，但中国、印度、德国、加拿大共同构成了一张跨时区的生产网络。Agentic AI 很像一个全球协作的工程现场：模型发布可能发生在一个地方，推理优化在另一个地方，coding agent 的入口在第三个地方，最后由不同国家的维护者、bot 和 CI 系统一起把变更送进主干。

自动化能力正在沿着软件生产链一点点往上爬：先是跑测试、发报告、更新依赖，再到读代码、提建议、生成补丁、参与协作。

这里有两类 bot。第一类是传统自动化：github-actions[bot]、dependabot[bot]、codecov[bot]、copybara-service[bot]、pytorchmergebot。它们让大型工程能稳定流动。第二类是新一代 AI 工具：greptile-apps[bot]、coderabbitai[bot]、gemini-code-assist[bot]、chatgpt-codex-connector[bot]。它们已经越过固定脚本，开始读代码、理解上下文、评论变更、参与 review。

### 碳基定义者和硅基执行者

真人开发者的画像比"程序员使用 AI 写代码"丰富得多。Top 开发者里有独立工具作者、开源维护者、AI startup 创始人、云厂商/模型厂商工程师、研究者、工具作者和社区型项目维护者。有人在构建 Agent 本身，有人在维护推理和调度基础设施，有人在把模型接入 workflow，有人在写规则、维护社区、处理 issue 和 review。

而本次关注的 226 个 Agentic AI 项目，Coding Agent 相关项目达到 78 个，累计 Star 数 386 万，2026 年 4 月参与者高达 14,019。以 Claude Code、Codex 为代表 **CLI-first 路线**，直接进入本地 repo、shell、测试和 git；以 Cursor 为代表的 **IDE-first** 路线，保留开发者心智，让人随时介入；Devin、OpenHands、Multica 代表 **cowork / cloud worker**，试图从 issue 到 PR 后台推进任务；而各种和记忆、团队编排相关的 Harness 工具则在为 Agent 补长期工作环境。

头部项目自己也在大量使用 coding agent。我们扫描了 OpenRank Top 100 Agentic AI 项目的文件树，发现 92 个项目至少出现过一种 coding agent 相关配置，平均每个项目使用 2.8 种。Claude Code 的覆盖率最高，达到 81%；OpenAI Codex 也达到 69%。

这里还有一个小细节很有意思：使用 Agent 标记最多的 google/adk-python，仓库里真正保留下来的配置目录只有 .gemini，但 .gitignore 里仍然写着 Codex、Claude、Cursor、Windsurf、Aider、Cline、Continue 等工具的痕迹。这些文件树里的 AGENTS.md、CLAUDE.md、.cursor/rules 像"给 AI 的小抄"。过去很多项目经验藏在维护者脑子里：这个模块为什么不能动，哪个测试最慢，release 前要检查什么，哪些依赖版本有坑，什么改动一定要先和谁沟通。Agent 时代，这些隐性经验如果不写出来，就无法被 Agent 可靠执行。

这是一件很有象征意义的事。过去开源项目为人类贡献者写 CONTRIBUTING.md；现在项目开始为 Agent 贡献者写入职文档。开源协作不再只是人和人之间的协议，也开始变成人和 AI 共同遵守的工作规范。

软件开发正在变成 **"碳基定义任务，硅基承担执行"**。所谓开发者被替代，很多时候其实是开发者从执行层移动到定义层。过去的核心能力是把需求翻译成代码；现在的核心能力，是把模糊目标翻译成 Agent 能执行、能验证、能回滚的任务系统。这会改变开发者的日常手感。过去写代码像是在一块一块砌墙，现在越来越多工作像是在带一个不稳定但学习很快的同事：先把任务讲清楚，给它足够上下文，告诉它哪些地方不能碰，让它提出方案，再看它改出的 diff。好的开发者会更在意 prompt 之外的东西：仓库结构是否清晰，测试是否可靠，错误信息是否可读，文档是否告诉 Agent 怎么运行，review 标准是否能被机器理解。

**这带来一个看似矛盾、其实很合理的变化：AI 工具越强，人的责任越重。** 因为当工具只能补全一行代码时，人只需要判断这一行；当工具能改几十个文件、跑测试、开 PR、回应 review 时，人要设计边界、写清验收标准、管理权限、检查结果、处理失败，并为最终合并负责。开发者的价值没有消失，只是位置在变：从"亲自完成每个动作"，移动到"定义目标、约束行动、验证结果、承担责任"。

因此，AI 工具越普及，工程组织反而越需要把规则、责任和知识显性化。一个团队如果没有测试、没有文档、没有清晰边界，Agent 只会把混乱放大；一个团队如果有良好的模块化、可运行的验证链路和明确的贡献规范，Agent 就会成为生产力放大器。

这对个人开发者同样成立。未来最稀缺的也许不再是"会不会使用某个 AI 工具"。更重要的是，能否把模糊目标变成可执行任务，能否把一次成功的交互沉淀成可复用规则，能否在 AI 生成的方案里看出真正的风险。AI 会降低写代码的门槛，但判断的价值不会因此变低。它让更多人可以进入软件生产，也让成熟开发者的经验变得更像一种系统设计能力。

## 软件会被重写，但开源仍不可替代

2011 年，Marc Andreessen 写下"Software is eating the world"。后来有人说，开源正在吞噬软件，因为开源基础设施成为现代软件的默认供应链。到 **2026 年，一个更尖锐的问题出现了：模型会不会吞噬软件和开源?**

答案更像是重分工。

模型会接管一部分过去由软件界面承载的动作，比如搜索、填写、整理、生成、跳转、调用。但它吃不掉软件背后的秩序。越是让模型接近真实工作，越需要软件去定义边界、保存状态、连接系统、控制权限、记录过程、处理失败。

软件不会消失。相反，软件会变得更多，只是长得不完全像过去。真正变化的是：很多过去由人手动完成的软件使用行为，会变成模型驱动的行动链。软件公司未来可能会先变成"Agent 可用的公司"。过去 SaaS 的核心是 UI、账号体系、业务数据和 workflow；Agent 时代，SaaS 还要提供稳定 API 和 machine-readable 文档。界面仍然重要，但 UI 不再是唯一入口。谁能让 Agent 安全地替用户做事，谁就可能成为新的平台。

Coding 只是第一站。真实世界比代码更脏，也更软。支付、金融、医疗、政务、教育、生活服务、具身智能，都涉及身份、责任、风险、监管、信任和人的处境。Agent 要进入这些场景，模型能力只是门票，制度、产品和系统设计才是长跑。

2025 年，我们看到大模型开发生态像一场黑客松。项目快速出现，迅速爆红，又快速消失。**到了 2026 年，这场比赛的场地慢慢变成了工地。**

软件还会被继续重写。Agent 会成为软件的用户。Token 会成为软件的能源。开发者会从亲手写每一行代码的人，越来越变成定义目标、设计约束、验证结果、承担责任的人。硅基负责执行，碳基负责定义什么值得执行。也许这就是 Agentic AI 时代最重要的分工。

在这个过程中，开源不会自动胜利，但开源仍然有不可替代的位置。**开放生态的意义不止是提供代码，也在于让更多人能理解、使用、改造和分享智能基础设施。**

模型厂商可以发布更强的模型，云厂商可以建设更大的 AI factory，应用公司可以做更顺滑的闭源产品。**但真正让一个生态长期健康的，仍然是开发者能不能参与，项目能不能被审计，标准能不能被共同制定，工具能不能被本地部署，知识能不能被共享。**

## Inclusive AGI：智能不应是少数人的特权

蚂蚁过去二十年的路径，其实一直在回答类似的问题。在线交易里，人与人为什么不敢互相信任？小商家为什么很难获得服务？复杂、昂贵、只属于少数人的能力，能不能变得更容易、更便宜、更可获得？二十年前，我们相信金融服务不应该是少数人的特权。今天面对 AGI，我们相信智能也不应该是少数人的特权。

这听起来像温和口号，其实是一个很硬的判断。现实世界远比抽象题目复杂。数学题有标准答案，代码有测试，棋局有规则；但服务业里有成本、信任、责任、情绪、合规、地域差异和人的处境。一个挂号流程、一次保险理赔、一笔跨境小额交易、一个小商家的经营建议，都不是单纯靠更高 benchmark 就能解决的。

这也是 Inclusion AI 的开放 AGI 实践要同时覆盖 **Model**、**Model Infra**、**Agent Infra** 和 **AI Service** 的原因。模型负责能力边界，后训练、推理、训练系统负责把能力变成可规模化供应的基础设施，Agent Infra 负责让开发者和行业专家把模型接进真实流程，AI Service 则将这些能力落到金融、医疗、生活服务等具体场景里。没有系统，模型只是能力展示；没有工具，模型很难进入行业；没有开放生态，普惠就会变成少数平台的租用权。

Towards inclusive AGI，并不要求每个人都成为模型公司，也不要求每个人都去写底层框架。它更像一个朴素但重要的愿望：**AI 不该成为少数人的黑箱，也不该只是大公司的产能机器。它应该是一种能被更多人理解、使用、改造和分享的公共技术。**

这可以被压成三个词：Available、Affordable、Inclusive。

- **Available**，意味着模型和工具应该尽可能开放，让开发者、研究者、行业专家和中小机构都能接触、看懂、调整。开放权重、数据工具、推理引擎与 Agent 协议，都是降低门槛的方式。智能要成为基础设施，必须能被更多人检查、适配和共同改进。
- **Affordable**，意味着 AI 要真正走进垂类场景，医疗、金融、政务、教育、公益、乡村和中小企业，而不只是高端订阅。真正困难的不是让 AI 解漂亮的题，而是以足够低的成本帮助一个老人挂号、一个小商家经营、一个普通家庭处理生活服务。
- **Inclusive**，意味着 AI 的价值不应该只被 token 消费大户或少数平台拿走。开发者、开源维护者、数据贡献者、行业专家和普通用户都应该在生态里有位置。要尊重真实流程和人的经验，让这些经验通过开放协作继续复利，变成可复用的工具和系统，而非单向发布。

这也许是开源在 AGI 时代最重要的工作。

## 数据口径简述

数据主要来自 Agentic AI landscape 仓库数据、OpenDigger、GitHub API、HuggingFace Hub、OpenRouter 公开榜单，以及对 vLLM、SGLang、TensorRT-LLM、llama.cpp、Dynamo、LiteLLM 等项目的 release、issue、PR 和 GitHub Search API 检索。

Agentic AI 项目趋势数据使用 2026 年 4 月 OpenRank 口径。开发者画像统计范围为 2026 年 1 月 1 日到 2026 年 5 月 1 日之前，保留 bot/app actor。

模型路由部分参考 RouteLLM（ICLR 2025）与 IPR（EMNLP Industry 2025）。RouteLLM 的表述采用"接近强模型质量时实现超过 2 倍成本节省"的保守口径；IPR 采用论文中的 "100% strongest-model quality" 工作点与 43.9% 成本下降结果。

本次报告的数据和洞察内容同步更新在 GitHub：https://github.com/antgroup/agentic-ai-landscape
