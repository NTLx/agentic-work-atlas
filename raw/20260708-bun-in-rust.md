---
type: raw
source: "https://bun.com/blog/bun-in-rust"
author:
  - "Jarred Sumner"
published: "2026-07-08"
created: "2026-07-10"
tags:
  - clippings
  - agentic-engineering
  - ai-assisted-development
  - memory-safety
---

# Rewriting Bun in Rust

## Background

Bun originally began as a line-for-line port of esbuild's JavaScript and TypeScript transpiler from Go to Zig. Written entirely by Jarred Sumner in about a year prior to modern LLMs, the project quickly expanded to include a vast array of features: a Jest-like test runner, an npm-compatible package manager, HTTP clients, and dozens of Node.js API implementations.

While extensive efforts were made to ensure stability—including Address Sanitizer checks and 24/7 fuzzing—the complexity of managing manually-allocated memory alongside a garbage-collected runtime led to recurring bugs. Many of these issues involved memory corruption, such as `heap-use-after-free` crashes in Node streams and resource leaks in file watching and TLS sockets.

## Why Rust?

To systematically prevent these stability issues, the project moved away from relying purely on style guides and manual oversight. In languages like Zig or C++, developers must rely on explicit cleanup keywords like `defer` or destructors, which can easily be missed on obscure error paths.

Rust provides compiler-enforced memory safety through its ownership model and RAII-style automatic cleanup via the `Drop` trait. By shifting to Rust, the project aimed to make impossible memory errors—such as double-frees or accessing freed memory—into compile-time failures rather than runtime crashes.

## The AI-Assisted Rewrite

Rather than executing a standard incremental rewrite (historically taking a team of engineers about a year), a novel approach using AI-driven workflows was adopted. Utilizing a pre-release version of Anthropic's Claude Fable 5 within Claude Code, the rewrite was executed over **11 days**.

### Process

1. **Preparation:** Establishing a mapping document (`PORTING.md`) and lifecycle guidelines (`LIFETIMES.tsv`) to translate Zig concepts directly to Rust.

2. **Mechanical Translation:** Approximately **64 concurrent AI instances** ran across four separate worktrees, generating roughly **1 million lines of code**.

3. **Adversarial Review:** For every chunk of code written by an "implementer" agent, two separate "reviewer" agents examined the diffs strictly looking for faults, memory leaks, and behavioral mismatches.

4. **Error Resolution:** Once compiled, roughly **16,000 compiler errors** were divided and fixed crate-by-crate, navigating intricate cyclical dependencies.

The execution required billions of input tokens and cost an estimated **$165,000 in API credits**, saving an estimated year of traditional engineering labor.

## Results and Improvements

Following successful CI testing across Linux, macOS, and Windows:

- **Reduced Memory Leaks:** Rust's `Drop` mechanism resolved lingering issues in error handling, mitigating multi-megabyte leaks during bundling operations
- **Binary Size:** Combined with linker optimizations and ICU data reductions, overall binary sizes shrunk by approximately **20%**
- **Stack Efficiency:** Improved LLVM IR codegen allowed stack variables to reuse memory slots more efficiently, significantly lowering stack requirements for recursive parsers
- **Performance:** Through cross-language link-time optimizations, HTTP throughput and app build times saw gains ranging from **2% to 5%**

## Regressions

Despite comprehensive testing, semantic differences between the languages caused **19 distinct regressions**, which were subsequently patched. Common causes:

- `debug_assert!` macros eliminating side-effects in release builds
- Rust's retention of bounds checks versus Zig's optimized builds
- Changes in how formatting strings handled escape sequences

The new Rust-native runtime has already entered production environments, notably serving as the foundation for newer iterations of Claude Code and Prisma Compute.
