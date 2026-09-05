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

从 Research 中选择一个通过 Retry hard gate 且当前可行动的 Claim，识别它最重要的一个知识缺口，采取一个最小有效动作，然后沉淀一次认识变化。如果 Retry hard gate 后没有 eligible Claim，输出“本次无可行动 Claim，退出”，不创建日志、不修改仓库、不提交。"blocked" 或 "no_delta" 只适用于已经选中的 eligible Claim，并在该 Claim 的实际 Action / SETTLE 阶段得出的结果。

本任务无人值守。所有可由证据和任务逻辑决定的事项自行裁决，不询问用户、不等待用户输入。只有在已经选中的 eligible Claim 执行中，确实需要用户权威、偏好或外部缺失材料才能继续时，才按 Workflow 记录为 "blocked" 并结束。

当前 Root/Main Agent 是本轮 Control Plane。按照
`schema/recompile-workflow.md` 完成 Claim、Gap、Action 规划和最终 Delta 裁决。

实际 Action 采用 direct execution、Execution Delegate 或当前 Runtime 其他原生
执行机制，由 Agent 根据任务、上下文、Skill、成本和 Runtime capability 自行判断。

如果声称使用 Skill，实际执行上下文必须真实加载并执行该 Skill；不得模拟。

不要为了消耗预算继续思考。

按 "schema/recompile-workflow.md" 的完成门结束任务，并将最终摘要输出到 stdout。
