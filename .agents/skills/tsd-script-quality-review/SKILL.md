---
name: tsd-script-quality-review
description: Review generated TikTok shooting scripts for factual accuracy, main line clarity, selling point organization, visual proof, shootability, rhythm, and risk.
---

# tsd-script-quality-review

**Status**: SCAFFOLD_ONLY

## Purpose

Repository skill scaffold for future script quality review.

## Inputs

- generated shooting script

## Outputs

- review result
- passed items
- risk items
- pending validation items
- revision notes
- final recommendation

## Boundaries

- Does not approve publishing.
- Does not override human review.
- Does not convert failed proof into a passing script.

## Failure Conditions

- unverified product capability appears in the script
- competitor capability is copied as product fact
- core proof is not shootable
- compliance or misleading-claim risk is blocking

## Evaluation Placeholder

Future eval cases should include scripts with factual errors, weak proof, excessive selling points, and missing Hook.
