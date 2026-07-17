# Execution Plan: 03_KNOWLEDGE_BASE_INDEX.md

**Status**: COMPLETED
**Target document**: `docs/03_KNOWLEDGE_BASE_INDEX.md`
**Created**: 2026-07-17
**Scope**: Create the formal plan for the v0.1 Knowledge Base Index only.

## 1. Goal

Create `docs/03_KNOWLEDGE_BASE_INDEX.md` as the v0.1 knowledge index for TikTok Script Director.

The final index must clarify:

- which knowledge topics the system needs;
- what problem each knowledge topic solves;
- what Source each topic requires;
- what materials currently exist;
- what materials are missing;
- how Source enters Source Digest;
- how Digest enters Knowledge;
- which Skills call which Knowledge;
- which Knowledge is required before Custom GPT v0.1 validation;
- which topics can be deferred.

## 2. Non-goals

This task does not include:

- crawling or scraping webpages;
- downloading GitHub repositories;
- downloading competitor videos;
- writing final knowledge files;
- completing business Skill logic;
- writing System Instructions;
- developing Python tools;
- developing Feishu API integration;
- developing backend services;
- building Custom GPT runtime.

The task must not modify:

- `knowledge/`;
- `source_digests/`;
- `.agents/skills/`;
- `docs/02_SYSTEM_INSTRUCTIONS.md`;
- `docs/04_SCRIPT_OUTPUT_SCHEMA.md`;
- `docs/05_EVALUATION_RUBRIC.md`.

## 3. Inputs and Sources of Truth

Primary upstream files:

- `AGENTS.md`
- `README.md`
- `ARCHITECTURE.md`
- `docs/index.md`
- `docs/PROJECT_STATUS.md`
- `docs/00_MASTER_DESIGN.md`
- `docs/01_INPUT_CONTRACT.md`
- `docs/03_KNOWLEDGE_BASE_INDEX.md`
- `docs/06_KNOWLEDGE_SKILLS_ARCHITECTURE_AND_FEEDBACK_LOOP.md`
- `docs/07_REPOSITORY_OPERATING_MODEL.md`
- `docs/exec-plans/TEMPLATE.md`
- `sources/README.md`
- `sources/AGENTS.md`
- `source_digests/TEMPLATE.md`
- `knowledge/README.md`
- `knowledge/AGENTS.md`
- `.agents/skills/*/SKILL.md`

Important upstream constraints:

- v0.1 uses a manually prepared flat Script Input Pack.
- Feishu raw table mapping is deferred to v0.2 automation.
- Knowledge engineering flow is `Source -> Source Digest -> Knowledge -> Skill -> Eval -> Feedback`.
- Source files are raw evidence, not executable rules.
- Source Digests extract usable conclusions but are not final knowledge.
- Knowledge files must trace back to approved Source Digests.
- Current business Skills are `SCAFFOLD_ONLY`; file existence does not mean business capability is implemented.

## 4. Files to Read

Before editing `docs/03_KNOWLEDGE_BASE_INDEX.md`, read or re-check:

- `AGENTS.md`
- `README.md`
- `ARCHITECTURE.md`
- `docs/index.md`
- `docs/PROJECT_STATUS.md`
- `docs/00_MASTER_DESIGN.md`
- `docs/01_INPUT_CONTRACT.md`
- `docs/03_KNOWLEDGE_BASE_INDEX.md`
- `docs/06_KNOWLEDGE_SKILLS_ARCHITECTURE_AND_FEEDBACK_LOOP.md`
- `docs/07_REPOSITORY_OPERATING_MODEL.md`
- `sources/README.md`
- `sources/AGENTS.md`
- `source_digests/TEMPLATE.md`
- `knowledge/README.md`
- `knowledge/AGENTS.md`
- `.agents/skills/tsd-input-fact-validation/SKILL.md`
- `.agents/skills/tsd-concept-strategy-design/SKILL.md`
- `.agents/skills/tsd-shooting-script-generation/SKILL.md`
- `.agents/skills/tsd-script-quality-review/SKILL.md`
- `.agents/skills/repo-source-digest/SKILL.md`
- `.agents/skills/repo-exec-plan-maintenance/SKILL.md`

## 5. Files to Change

For the later execution task:

- `docs/03_KNOWLEDGE_BASE_INDEX.md`
- `docs/PROJECT_STATUS.md`
- `docs/index.md`
- this execution plan

For the original planning-only task:

- `docs/exec-plans/active/03-knowledge-base-index-plan.md`

Files modified during execution:

- `docs/03_KNOWLEDGE_BASE_INDEX.md`
- `docs/PROJECT_STATUS.md`
- `docs/index.md`
- `CHANGELOG.md`
- `docs/exec-plans/active/03-knowledge-base-index-plan.md`

## 6. Work Steps

### Phase 1: Confirm Scope and Current State

- Confirm that `docs/01_INPUT_CONTRACT.md` is `APPROVED_FOR_V0_1_VALIDATION`.
- Confirm that `docs/03_KNOWLEDGE_BASE_INDEX.md` is still `NOT_STARTED`.
- Confirm that no source collection, source digestion, knowledge writing, or Skill completion is part of this task.
- Confirm that v0.1 knowledge work supports the chain: fact validation, strategy design, shooting script generation, and script quality review.

### Phase 2: Define Knowledge Topic Inventory

Create a topic inventory in `docs/03_KNOWLEDGE_BASE_INDEX.md`.

Each knowledge topic must record:

- `knowledge_topic_id`
- `knowledge_topic_name`
- `purpose`
- `questions_answered`
- `required_for_v0_1`
- `priority`
- `target_knowledge_file`
- `related_skills`
- `preferred_source_types`
- `current_sources`
- `missing_sources`
- `freshness_requirement`
- `market_scope`
- `category_scope`
- `source_digest_status`
- `knowledge_status`
- `open_questions`
- `risks`

First version topics must include at least:

| ID | Topic | Target knowledge file | Required for v0.1 | Priority |
|---|---|---|---|---|
| KBI-01 | TikTok good script standard | `knowledge/01_GOOD_SCRIPT_STANDARD.md` | Yes | P0 |
| KBI-02 | TikTok content formats | `knowledge/02_CONTENT_FORMATS.md` | Yes | P1 |
| KBI-03 | Main communication proposition | `knowledge/01_GOOD_SCRIPT_STANDARD.md` | Yes | P0 |
| KBI-04 | Core and supporting selling point organization | `knowledge/01_GOOD_SCRIPT_STANDARD.md` | Yes | P0 |
| KBI-05 | Hook and first three seconds | `knowledge/03_HOOK_RULES.md` | Yes | P0 |
| KBI-06 | Product Proof / visual proof | `knowledge/04_PRODUCT_PROOF.md` | Yes | P0 |
| KBI-07 | Shot planning and production execution | `knowledge/05_SHOT_PRODUCTION.md` | Yes | P1 |
| KBI-08 | Human UGC and non-human demonstration | `knowledge/02_CONTENT_FORMATS.md` | Yes | P1 |
| KBI-09 | English subtitles and voiceover | `knowledge/07_SCRIPT_OUTPUT_SCHEMA.md` | Yes | P1 |
| KBI-10 | CTA | `knowledge/01_GOOD_SCRIPT_STANDARD.md` | Yes | P1 |
| KBI-11 | TikTok Shop US content compliance | `knowledge/06_COMPLIANCE_RULES.md` | Yes | P0 |
| KBI-12 | AI content and AI competitor reference limits | `knowledge/06_COMPLIANCE_RULES.md` | Yes | P0 |
| KBI-13 | Script output structure | `docs/04_SCRIPT_OUTPUT_SCHEMA.md` as authoritative contract; `knowledge/07_SCRIPT_OUTPUT_SCHEMA.md` as guidance | Yes | P0 for minimum contract; P1 for guidance |
| KBI-14 | Script quality evaluation | `knowledge/01_GOOD_SCRIPT_STANDARD.md` and `knowledge/06_COMPLIANCE_RULES.md` | Yes | P1 |
| KBI-15 | Single-selling-point and multi-selling-point videos | `knowledge/01_GOOD_SCRIPT_STANDARD.md` | Yes | P0 |
| KBI-16 | Category-specific difference rules | Category sections inside relevant knowledge files | Partial | P2 |

The final document may split or merge target files only if it keeps traceability from each topic to a knowledge file.

### Phase 3: Freeze Source Priority and Use Rules

The final index must freeze this Source priority:

```text
TikTok / TikTok Shop official materials
>
Internal real product tests and shooting experience
>
Highly relevant open-source materials with explicit LICENSE
>
Trusted industry materials
>
Competitor videos and competitor comments
>
Ordinary blogs and personal experience
```

The final index must also state:

- Competitor materials can only be used as expression, structure, pacing, or audience-language references.
- Competitor materials cannot prove our product capability.
- Supplier materials cannot automatically become verified product facts.
- AI-generated video cannot be used as real Product Proof.
- GitHub repositories without clear LICENSE cannot be directly reused.
- Platform policy sources must record capture date and applicable market.
- If official policy conflicts with industry advice or competitor examples, official policy wins.
- If internal verified testing conflicts with supplier claims, internal testing wins for product capability.

### Phase 4: Define Source Inventory Planning Rules

The final index must include a first-batch Source Inventory plan, but this execution must not collect the sources.

First batch size: 10 to 15 planned items.

Planned first-batch Source Inventory slots:

| Slot | Planned source type | Purpose | Priority |
|---|---|---|---|
| SRC-01 | TikTok Shop US official content policy | Establish market compliance boundaries | P0 |
| SRC-02 | TikTok / TikTok Shop official misleading-content or claim policy | Prevent exaggerated or unsupported claims | P0 |
| SRC-03 | TikTok official AI-generated content policy | Define AI content and AI reference limits | P0 |
| SRC-04 | TikTok / TikTok Shop official intellectual-property policy | Avoid IP and copied-creative risks | P0 |
| SRC-05 | TikTok Creative Center official material | Identify platform-native creative patterns | P1 |
| SRC-06 | TikTok official creative guidance | Support Hook, pacing, and content-form rules | P1 |
| SRC-07 | Internal foam sprayer product test or shooting notes | Ground Product Proof and category limits | P0 |
| SRC-08 | Internal car vacuum product test or shooting notes | Ground Product Proof and category limits | P0 |
| SRC-09 | Internal shooting constraints and production experience | Ground shootability and shot-planning rules | P1 |
| SRC-10 | Licensed high-relevance open-source agent or prompt workflow material | Support repo/Skill operation patterns only | P2 |
| SRC-11 | Licensed high-relevance open-source evaluation or rubric material | Support script review and eval structure only | P2 |
| SRC-12 | Licensed high-relevance open-source script or content-planning material | Support output structure only if license allows | P2 |
| SRC-13 | Trusted industry source on short-form video hooks | Secondary support for Hook rules | P2 |
| SRC-14 | Curated competitor video examples | Expression reference only | P2 |
| SRC-15 | Curated competitor comment examples | Audience-language reference only | P2 |

The final index must mark all uncollected slots as planned or missing, not as current evidence.

### Phase 5: Define Source -> Digest -> Knowledge Flow

The final index must explain:

- Source enters `sources/` with metadata, provenance, date, market, category, and credibility.
- Source is summarized into `source_digests/` using `source_digests/TEMPLATE.md`.
- Digest records original claims, executable conclusions, exceptions, misuse, risks, affected knowledge files, affected Skills, and open questions.
- Knowledge files only receive approved conclusions from Digest.
- Knowledge files must separate official platform facts, internal experience, and project-level inference.
- A Source may feed multiple Digests; a Digest may feed multiple Knowledge files.
- Skill references must point to Knowledge files, not raw Source files.

### Phase 6: Map Knowledge to Skills

The final index must map knowledge dependencies for these Skills.

#### `tsd-input-fact-validation`

Needs:

- `knowledge/01_GOOD_SCRIPT_STANDARD.md`
- `knowledge/04_PRODUCT_PROOF.md`
- `knowledge/06_COMPLIANCE_RULES.md`
- `knowledge/07_SCRIPT_OUTPUT_SCHEMA.md`
- `docs/04_SCRIPT_OUTPUT_SCHEMA.md` for formal output constraints

Purpose:

- validate Script Input Pack readiness;
- separate verified facts, unverified content, risks, and conflicts;
- produce READY / PROVISIONAL / BLOCKED input status.

#### `tsd-concept-strategy-design`

Needs:

- `knowledge/01_GOOD_SCRIPT_STANDARD.md`
- `knowledge/02_CONTENT_FORMATS.md`
- `knowledge/03_HOOK_RULES.md`
- `knowledge/04_PRODUCT_PROOF.md`
- `docs/04_SCRIPT_OUTPUT_SCHEMA.md` for formal output constraints

Purpose:

- derive main communication proposition;
- organize core and supporting selling points;
- choose content form and proof direction.

#### `tsd-shooting-script-generation`

Needs:

- `knowledge/03_HOOK_RULES.md`
- `knowledge/04_PRODUCT_PROOF.md`
- `knowledge/05_SHOT_PRODUCTION.md`
- `knowledge/07_SCRIPT_OUTPUT_SCHEMA.md`
- `docs/04_SCRIPT_OUTPUT_SCHEMA.md` for formal output constraints

Purpose:

- generate shootable shot-by-shot scripts;
- use Hook variants and proof shots;
- keep output structure consistent.

#### `tsd-script-quality-review`

Needs:

- `knowledge/01_GOOD_SCRIPT_STANDARD.md`
- `knowledge/03_HOOK_RULES.md`
- `knowledge/04_PRODUCT_PROOF.md`
- `knowledge/05_SHOT_PRODUCTION.md`
- `knowledge/06_COMPLIANCE_RULES.md`
- `knowledge/07_SCRIPT_OUTPUT_SCHEMA.md`
- `docs/04_SCRIPT_OUTPUT_SCHEMA.md` for formal output constraints

Purpose:

- review fact support, selling-point hierarchy, Hook strength, proof clarity, shootability, compliance, and output completeness.

The final index must explicitly state:

- current Skills are `SCAFFOLD_ONLY`;
- Knowledge files are not complete unless their status says so;
- file existence does not mean business capability has been implemented;
- no Skill may treat raw Source or competitor examples as verified product facts.

### Phase 7: Recommend First Knowledge Output Order

The final index must propose this first output order:

1. `knowledge/01_GOOD_SCRIPT_STANDARD.md`
2. `knowledge/03_HOOK_RULES.md`
3. `knowledge/04_PRODUCT_PROOF.md`
4. `knowledge/06_COMPLIANCE_RULES.md`
5. `knowledge/02_CONTENT_FORMATS.md`
6. `knowledge/05_SHOT_PRODUCTION.md`
7. `knowledge/07_SCRIPT_OUTPUT_SCHEMA.md`

Rationale:

- `01_GOOD_SCRIPT_STANDARD.md` defines the quality bar, main proposition, selling-point hierarchy, CTA, and review baseline.
- `03_HOOK_RULES.md` is needed early because Hook and first-three-second logic affect strategy and generation.
- `04_PRODUCT_PROOF.md` is a P0 boundary because v0.1 must avoid unsupported product claims.
- `06_COMPLIANCE_RULES.md` is a P0 boundary for TikTok Shop US validation, misleading claims, AI content, and IP risk.
- `02_CONTENT_FORMATS.md` can follow once the quality and risk boundaries are clear.
- `05_SHOT_PRODUCTION.md` turns proof direction into shootable execution after core proof rules exist.
- `07_SCRIPT_OUTPUT_SCHEMA.md` should be aligned after strategy, compliance, proof, and production rules are defined, so output fields reflect actual workflow needs.

### Phase 8: Record Required, Deferred, and Blocking Knowledge

The final index must separate:

- v0.1 blocking knowledge;
- v0.1 useful but non-blocking knowledge;
- v0.2 deferred knowledge.

Initial v0.1 blocking candidates:

- TikTok Shop US compliance boundaries;
- misleading or unsupported claim restrictions;
- AI content and AI competitor reference limits;
- Product Proof rules;
- main proposition and selling-point hierarchy;
- Hook and first-three-second rules;
- single-selling-point and multi-selling-point video rules;
- script output structure minimum.

Initial v0.2 deferred candidates:

- Feishu raw field mapping;
- automated Source ingestion;
- automated Source freshness monitoring;
- category expansion beyond current initial products;
- large-scale competitor library;
- publishing-result based optimization loops.

### Phase 9: Update Project Records

During the later execution task:

- update `docs/03_KNOWLEDGE_BASE_INDEX.md`;
- update `docs/index.md` status for `03_KNOWLEDGE_BASE_INDEX.md`;
- update `docs/PROJECT_STATUS.md`;
- update this execution plan with progress, decisions, validation, and final result.

Do not move this plan to `completed/` until the user asks for final approval or explicitly approves the completed document.

## 7. Acceptance Criteria

The final `docs/03_KNOWLEDGE_BASE_INDEX.md` is acceptable when:

- it covers all v0.1 necessary knowledge areas listed in this plan;
- every knowledge topic includes the required tracking fields;
- it clearly maps Source, Source Digest, Knowledge, and Skill relationships;
- it distinguishes current sources from missing or planned sources;
- it distinguishes official platform facts, internal experience, supplier claims, competitor references, and project inference;
- it includes the first-batch Source Inventory plan;
- it marks which knowledge topics block v0.1 validation;
- it avoids open-ended or unfocused source collection;
- it does not treat Source as final Knowledge;
- it does not treat Source Digest as final Knowledge;
- it does not treat Skill skeletons as implemented business capability;
- it preserves `SCAFFOLD_ONLY` status where applicable;
- it keeps v0.2 automation, Feishu raw mapping, and large-scale collection out of v0.1 scope.

## 8. Risks and Unknowns

- Official TikTok or TikTok Shop policy pages may change; source capture date and market scope are mandatory.
- Current internal product tests may be insufficient for some category-specific rules.
- Competitor examples may be tempting to overuse as product proof; this must be explicitly prohibited.
- Open-source repositories may not have usable licenses; no-license materials must not be reused directly.
- A knowledge file may exist before it is validated; status fields must prevent accidental overclaiming.
- The first batch of Source Inventory may need project-owner approval before collection begins.

Open questions for human confirmation:

- Which concrete internal files or Feishu exports will be placed into `sources/` for the planned foam sprayer records?
- Which concrete internal files or Feishu exports will be placed into `sources/` for the planned car vacuum records?
- Which official TikTok / TikTok Shop policy pages should be collected first for compliance, misleading Claim, AI content, and IP rules?
- Which open-source material categories, if any, should enter license review first?
- Should the first Source Collection execution plan run compliance, Hook, and Product Proof collection in parallel or in separate plans?

Resolved by user on 2026-07-17:

- v0.1 category scope is car wireless vacuum and electric foam sprayer only.
- Portable water flosser remains `DEFERRED_CATEGORY_PLACEHOLDER`.
- Open-source slots remain unnamed, `NOT_RESEARCHED`, `license_status: NOT_CHECKED`, and `reuse_status: BLOCKED_UNTIL_REVIEW`.
- `docs/03_KNOWLEDGE_BASE_INDEX.md` first draft status is `DRAFT_FOR_VALIDATION`.

## 9. Progress Log

- 2026-07-17: Created execution plan for `docs/03_KNOWLEDGE_BASE_INDEX.md`.
- 2026-07-17: Ran repository structure validation; validation passed.
- 2026-07-17: Executed approved plan and drafted `docs/03_KNOWLEDGE_BASE_INDEX.md`.
- 2026-07-17: Updated `docs/index.md` and `docs/PROJECT_STATUS.md` to mark 03 as `DRAFT_FOR_VALIDATION`.
- 2026-07-17: Kept this execution plan in `active/` for human review.
- 2026-07-17: Resolved Output Schema responsibility boundary between `docs/04_SCRIPT_OUTPUT_SCHEMA.md` and `knowledge/07_SCRIPT_OUTPUT_SCHEMA.md`.
- 2026-07-17: Approved `docs/03_KNOWLEDGE_BASE_INDEX.md` as `APPROVED_FOR_V0_1_VALIDATION`.
- 2026-07-17: Updated `docs/index.md`, `docs/PROJECT_STATUS.md`, and `CHANGELOG.md`.
- 2026-07-17: Marked this execution plan as `COMPLETED` for archive.

## 10. Decision Log

- 2026-07-17: Plan freezes v0.1 knowledge index as a planning and traceability document, not a source-collection task.
- 2026-07-17: Plan treats Feishu raw structure mapping as v0.2 deferred work, consistent with approved `docs/01_INPUT_CONTRACT.md`.
- 2026-07-17: Plan requires all business Skill dependencies to be marked against `SCAFFOLD_ONLY` Skill status until implementation is explicitly approved.
- 2026-07-17: User confirmed v0.1 category scope as car wireless vacuum and electric foam sprayer only; portable water flosser remains `DEFERRED_CATEGORY_PLACEHOLDER`.
- 2026-07-17: User confirmed internal foam sprayer and car vacuum records are planned internal Source candidates only; they must be marked `PLANNED_INTERNAL_SOURCE` until they enter `sources/`.
- 2026-07-17: User confirmed open-source Source slots must remain unnamed, `NOT_RESEARCHED`, `license_status: NOT_CHECKED`, and `reuse_status: BLOCKED_UNTIL_REVIEW`.
- 2026-07-17: User confirmed P0 knowledge areas: TikTok Shop US compliance, misleading and unsupported Claims, AI content limits, Product Proof, main proposition, core/supporting selling points, and Hook / first three seconds.
- 2026-07-17: User confirmed `docs/03_KNOWLEDGE_BASE_INDEX.md` first draft status is `DRAFT_FOR_VALIDATION`.
- 2026-07-17: User confirmed `docs/04_SCRIPT_OUTPUT_SCHEMA.md` is the only authoritative v0.1 output contract.
- 2026-07-17: User confirmed `knowledge/07_SCRIPT_OUTPUT_SCHEMA.md` is output design and usage guidance only; conflicts must defer to `docs/04_SCRIPT_OUTPUT_SCHEMA.md`.
- 2026-07-17: User confirmed the minimum script output contract is v0.1 blocking knowledge.

## 11. Validation Performed

- 2026-07-17: `python3 scripts/validate_structure.py` passed.
- 2026-07-17: After drafting and project record updates, `python3 scripts/validate_structure.py` passed.
- 2026-07-17: After final wording cleanup, `python3 scripts/validate_structure.py` passed.
- 2026-07-17: After approval, project record updates, and archive move, `python3 scripts/validate_structure.py` passed.
- 2026-07-17: After archived plan consistency cleanup, `python3 scripts/validate_structure.py` passed.

## 12. Final Result

`docs/03_KNOWLEDGE_BASE_INDEX.md` has been approved as `APPROVED_FOR_V0_1_VALIDATION`. Output Schema responsibilities are frozen, project records are updated, and this execution plan is ready for archive under `docs/exec-plans/completed/03-knowledge-base-index-plan.md`.
