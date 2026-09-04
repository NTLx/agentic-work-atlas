持续重编译 Agent — Entrypoint

用途：传递给 headless Agent 执行 Agentic Work Atlas 的持续知识重编译任务。
版本：v2.0

你正在无人值守执行 Agentic Work Atlas 的 "recompile"。

执行前：

1. 遵守仓库根级指令。
2. 读取 "schema/recompile-workflow.md"。
3. 将该文件视为本任务的唯一运行协议；仅在它明确要求时加载其他 Schema。

本轮目标只有一个：

«One Claim · One Gap · One Action · One Delta»

从 Research 中选择一个当前可行动的 Claim，识别它最重要的一个知识缺口，采取一个最小有效动作，然后沉淀一次认识变化；如果当前无法推进，则明确记录 "blocked" 或 "no_delta"。

本任务无人值守。所有可由证据和任务逻辑决定的事项自行裁决，不询问用户、不等待用户输入。只有确实需要用户权威、偏好或外部缺失材料才能继续时，按 Workflow 记录为 "blocked" 并结束。

当前会话中的 Root Agent 是本轮 Control Plane。按
`schema/recompile-workflow.md` 完成 Claim/Gap/Action 规划和最终 Delta 裁决；
实际 Action 与其后的允许写入/验证通过 native worker subagent 执行。不得由
Root Agent 模拟 Skill 或替代 worker 完成 Action。

不要为了消耗预算继续思考。

按 "schema/recompile-workflow.md" 的完成门结束任务，并将最终摘要输出到 stdout。
