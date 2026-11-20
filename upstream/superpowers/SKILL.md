---
name: superpowers
description: Full software-development methodology as composable skills — brainstorming, writing plans, test-driven development, systematic debugging, verification before completion, subagent-driven development, git worktrees, and code review. Use whenever the user asks to build, plan, debug, test, or review code, especially for make.fun bounty builds. This is a local hub for the official Superpowers collection (github.com/obra/superpowers, installed verbatim via `git clone --depth 1` on 2026-11-17) — read the matching sub-skill below before doing the work.
---

# Superpowers (hub)

Local hub for the **official Superpowers** collection by Jesse Vincent (obra).
Source: https://github.com/obra/superpowers — installed verbatim via `git clone --depth 1` into this folder on 2026-11-17. The 15 real skills live in `skills/<name>/SKILL.md`. Do not edit the vendored files; this hub file is the only local addition.

## How to use

1. Pick the sub-skill that matches the task from the list below.
2. Read that sub-skill's `SKILL.md` first, then follow it. It contains the real instructions.
3. If unsure which one fits, start with `using-superpowers` — it is the router for all the others.
4. The `brainstorming` sub-skill can start a local visual-companion server (binds 127.0.0.1 only). Only start it when the user actually asks for a brainstorming session — never speculatively.
5. Overlap note: `test-driven-development` and `systematic-debugging` here are the Superpowers versions; the flat `test-driven-development` and `debugging-and-error-recovery` skills in `~/workspace/custom-skills/` are separate earlier installs. Prefer the Superpowers versions for make.fun builds (they tie into writing-plans + verification-before-completion); keep the flat ones for other work.

## Sub-skills

| Skill | When to use |
|---|---|
| `skills/using-superpowers/SKILL.md` | Router for all Superpowers skills; use when unsure which specific skill fits. |
| `skills/brainstorming/SKILL.md` | Turn a rough idea into a design before writing code; can open a local visual companion (localhost only, only when the user asks). |
| `skills/writing-plans/SKILL.md` | Write an implementation plan before coding. |
| `skills/executing-plans/SKILL.md` | Execute a written plan in batches. |
| `skills/test-driven-development/SKILL.md` | RED-GREEN-REFACTOR loop; write the failing test first. |
| `skills/systematic-debugging/SKILL.md` | Root-cause debugging, step by step, no guessing. |
| `skills/verification-before-completion/SKILL.md` | Verify the work against the original requirements before calling it done. |
| `skills/subagent-driven-development/SKILL.md` | Fan work out to subagents in parallel. |
| `skills/dispatching-parallel-agents/SKILL.md` | Dispatch multiple agents at once and coordinate them. |
| `skills/requesting-code-review/SKILL.md` | Ask for a code review the right way. |
| `skills/receiving-code-review/SKILL.md` | Handle review feedback without losing the thread. |
| `skills/finishing-a-development-branch/SKILL.md` | Wrap up a branch: verify, clean up, merge. |
| `skills/using-git-worktrees/SKILL.md` | Isolate work with git worktrees. |
| `skills/writing-skills/SKILL.md` | Write or improve an Agent Skill. |
| `skills/diagnosing-superpowers/SKILL.md` | Diagnose when Superpowers itself is misbehaving. |

## Notes and limits

- Vetted 2026-11-17: no exfiltration, no credential access, no remote code execution in scripts/hooks; the only network references are a brand image URL and a GitHub link inside the local brainstorm server page.
- The repo also ships Claude Code / Cursor / Codex plugin manifests and test suites under `tests/` — inert under Muse; ignore them.
- `AGENTS.md` in this folder is the upstream contributor guide (94% PR rejection rate) — it governs opening PRs against the Superpowers repo, not using the skills. Never open a PR upstream without following it; do not edit the vendored skill files.
