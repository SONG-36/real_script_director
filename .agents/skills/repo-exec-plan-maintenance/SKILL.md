---
name: repo-exec-plan-maintenance
description: Scaffold for creating and maintaining repository execution plans with goals, non-goals, files, acceptance criteria, risk, progress, decisions, validation, and final result.
---

# repo-exec-plan-maintenance

**Status**: SCAFFOLD_ONLY

## Purpose

Repository maintenance skill scaffold for future execution plan maintenance.

## Inputs

- task request
- relevant upstream documents
- current active execution plan, if present

## Outputs

- active execution plan updates
- progress log
- decision log
- validation record
- final result record

## Boundaries

- Does not move an execution plan to completed without explicit completion criteria.
- Does not replace project status updates when required.
- Does not record unnecessary minute-by-minute logs.

## Failure Conditions

- task goal or non-goal is unclear
- modified files are not recorded
- validation result is omitted

## Evaluation Placeholder

Future eval cases should check that plans preserve scope, decisions, validation, and review state.
