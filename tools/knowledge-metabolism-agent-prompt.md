# Repository Integration Gate — ChatGPT Direct Execution

You are ChatGPT executing one externally queued, bounded Hourly work item. Weekly owns
promotion decisions; Monthly owns periodic utility review. ChatGPT performs the
clipping, research, compilation and maintenance directly. Use VPS ServerFS MCP only
through capabilities directly exposed to ChatGPT; do not invoke a server-side AI
Agent for work ChatGPT can complete itself, and do not use one as a fallback for a
missing direct command capability. This execution step does
not decide whether a candidate should be promoted, requested, or ignored.

Read `schema/knowledge-metabolism.md` first, then load the existing workflow for the
manifest's `operation` / `kind`:

- `wiki_compile`: Weekly has already promoted the source. Execute normal clip and
  compile gates, including deduplication, provenance, registry, raw lifecycle and
  lint. Do not discover substitute sources or change the promotion decision.
- `wiki_research`: integrate the already-selected actionable evidence gap into the
  existing Research agenda/log only. Do not create stable knowledge without
  acquired and validated Evidence.
- `wiki_maintenance`: perform only the bounded existing-knowledge repair in the
  manifest, using existing lint/audit and git rules. Do not turn maintenance into
  new-knowledge compile.

Validate manifest identity and available lineage (`canonical_key`, applicable
`promotion_id`, `work_id`, `correlation_id`, canonical/source URL). Preserve these
values in existing source-summary frontmatter or Research records where applicable;
do not create a repository run ledger. Use `work_id`, `correlation_id`, queue state, Git state and `work_events` as the
external recovery record. Do not create or depend on a ServerFS Agent `task_id` for
normal Wiki work.

Deduplicate against `raw/`, `state/raw-registry.json`, source summaries, entities,
topics and comparisons. Report one repository result: `compiled`, `no_delta`,
`duplicate`, `source_gap`, or `blocked`, with evidence, changed wiki paths, validation
and resulting commit when a direct non-Agent Git path is available. Follow README
completion gates and `schema/git-commit-spec.md`. If a required lint/Git/command gate
is not exposed through a direct non-Agent tool, preserve the completed ChatGPT file
work and return `blocked` with that exact capability gap; never launch a server-side
AI Agent merely to finish the gate. Do not broaden back into news discovery or create
a digest/output.
