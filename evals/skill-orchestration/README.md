# Skill Orchestration Eval

这是 Agent Skills 行为级测试集，不是 Skill Router，也不规定某个 case 必须激活
哪个 Skill。每个 case 只约束 operation、可观察结果和禁止副作用；
`routing.exact_skill_set_required` 必须为 `false`。

运行方式：

```bash
uv run --with pytest pytest tests/test_skill_orchestration_eval.py
```

测试只校验 Eval 文件契约，不调用 LLM。真实运行时可额外记录短 routing trace，
例如：

```text
case: query-concept-boundary
result: pass
routing_summary: 当前缺口是概念边界；选择了一个匹配的能力
activated: [当前实际激活的 Skill 或 none]
after_activation: sufficient | needs_reselection
evidence_boundary: pass
side_effects: none
```

`routing trace` 是决策摘要，不保存 Chain of Thought、完整 Skill transcript 或
外部笔记。case 的通过条件是 outcome、Evidence 边界和 side-effect 约束满足，
不是 Skill 名称与预设一致。
