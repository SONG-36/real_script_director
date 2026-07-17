---
name: tsd-input-fact-validation
description: Validate a Script Input Pack for factual support, missing information, risks, and READY / PROVISIONAL / BLOCKED status.
---

# tsd-input-fact-validation

**Status**: SCAFFOLD_ONLY

## Purpose

Repository skill scaffold for future input fact validation.

## Inputs

- Script Input Pack defined by `docs/01_INPUT_CONTRACT.md`

## Outputs

- input check result
- usable facts
- information not directly usable
- pending validation items
- risks
- generation status

## Boundaries

- Does not generate a shooting script.
- Does not treat competitor capability as product evidence.
- Does not turn pending validation into confirmed facts.

## Failure Conditions

- product is unclear
- core function is unsupported
- key proof cannot be verified
- main claim has blocking risk

## Evaluation Placeholder

Future eval cases should include at least one READY, one PROVISIONAL, and one BLOCKED Script Input Pack.
