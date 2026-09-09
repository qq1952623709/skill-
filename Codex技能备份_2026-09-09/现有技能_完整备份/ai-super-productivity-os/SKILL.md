---
name: ai-super-productivity-os
description: Apply the user's AI Super Productivity Operating System V3.0.1 to complex goals, especially multi-file delivery, engineering, research, automation, multi-agent work, formal outputs, and long-running projects. Use professional diagnosis, capability checks, frozen contracts, evidence-based gates, bounded retries, and explicit human acceptance. Do not force the full framework onto simple low-risk tasks.
metadata:
  short-description: Govern complex work with the AI Super Productivity OS V3.0.1
---

# AI Super Productivity Operating System V3.0.1

Use this as an operating framework, not as a reason to over-engineer ordinary requests. The user's real-world goal outranks the user's initial proposed method.

## Core operating behavior

For complex work, compile:

`real-world goal → professional diagnosis → hidden requirements → capability/tool boundary → minimum validation → frozen execution contract → execution → independent audit → human acceptance → validated completion`

Before execution, identify task class (T0–T5), freeze `FINAL_GOAL`, `IN_SCOPE`, `OUT_OF_SCOPE`, deliverables, acceptance criteria/oracle, loop budget, and human-acceptance points. Infer what is reliable from context; ask only for gaps that materially affect success.

Apply these invariants:

- Protect and version SOURCE; keep REFERENCE and DERIVED content visibly separate.
- Never convert claims, hypotheses, or inferences into verified facts.
- Distinguish `CLAIMED`, `OBSERVED`, `PROVEN`, `PARTIAL`, `UNSUPPORTED`, and `BLOCKED` capability states.
- Probe the smallest critical capability and test the most dangerous assumption before batch work.
- Build a Golden Unit before scaling; attack it with materially different examples and an early end-to-end vertical slice when dependencies matter.
- Separate engineering tests, AI self-review, independent audit, and human acceptance; do not overstate audit level or evidence level.
- Use minimum necessary change, bounded failure loops, and explicit stop conditions. After frozen criteria pass, stop; non-blocking improvements go to Backlog.
- Do not perform publishing, sending, deletion, payment, production changes, permission changes, or other irreversible actions without separate authorization.
- Preserve durable project state and checkpoints for long-running work; do not rely on chat history alone.

## Default response for complex tasks

Briefly cover, in this order as relevant: classification, real-world goal, professional diagnosis, hidden requirements, capability boundary, options, fatal assumption, minimum validation, architecture, risks, permissions/environment, acceptance design, and stop conditions. Only then produce an execution contract or Codex prompt.

For simple T5 and low-risk reversible T4 work, use a lightweight goal and acceptance check instead.

## Required contract fields

When an execution contract is warranted, include:

`PROJECT / FINAL_GOAL / CURRENT_STATE / SOURCE_OF_TRUTH / INPUT / SCOPE / OUT_OF_SCOPE / DELIVERABLES / SCHEMA / TOOLS / PERMISSIONS / BEFORE_WRITE / CAPABILITY_PROBE / EXECUTION / QUALITY_GATES / FAILURE_LOOP / LOOP_BUDGET / CHECKPOINT / WATCHDOG / RESUME_PROTOCOL / STOP_CONDITIONS / ACCEPTANCE_CRITERIA / ORACLE / FINAL_REPORT`

## Status and completion

Use explicit status values only, such as `NOT_STARTED`, `RUNNING`, `PASS_PARTIAL`, `FAIL_RETRYING`, `BLOCKED_FOR_HUMAN`, `READY_FOR_REVIEW`, `WAITING_FOR_USER_APPROVAL`, `ACCEPTED`, `REJECTED`, `DEFERRED`, `ENGINE_COMPLETE`, and `VALIDATED_COMPLETE`. Claim `VALIDATED_COMPLETE` only when the real deliverables exist, core criteria pass, blockers are zero, major issues are accepted or zero, and required human acceptance is complete.

## Full reference

For detailed rules, schemas, audit levels, worker handoff, state recovery, failure records, experience capture, browser conditions, and version protocols, read [V3.0.1 full reference](references/v3.0.1-full.md) when the current task needs them.
