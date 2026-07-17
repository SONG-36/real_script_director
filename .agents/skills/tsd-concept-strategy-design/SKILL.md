---
name: tsd-concept-strategy-design
description: Convert a validated conversational concept into a video strategy with main proposition, core selling point, supporting selling points, format, and proof direction.
---

# tsd-concept-strategy-design

**Status**: SCAFFOLD_ONLY

## Purpose

Repository skill scaffold for future concept strategy design.

## Inputs

- Script Input Pack that has passed input fact validation

## Outputs

- normalized concept
- main communication proposition
- core problem
- core selling point
- supporting selling points
- content format
- script structure
- target duration
- Hook direction
- visual proof direction

## Boundaries

- Does not change the user's core intent.
- Does not add unsupported product claims.
- Does not choose multiple unrelated selling points for a short video.

## Failure Conditions

- concept is unrelated to the product
- core problem and core selling point do not match
- selling points have no clear main line
- target duration cannot carry the requested information

## Evaluation Placeholder

Future eval cases should cover single-selling-point and multi-selling-point concepts.
