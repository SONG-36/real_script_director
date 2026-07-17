# Execution Plan: First Source Collection

**Status**: ACTIVE  
**Owner**: Codex + project owner  
**Started**: 2026-07-17  
**Target**: Plan Batch 1 Source Collection for TikTok Script Director v0.1

## 1. Goal

Plan the first high-priority Source Collection batch for TikTok Script Director v0.1.

This batch supports the following P0 knowledge areas:

- TikTok Shop US compliance
- Misleading content and unsupported Claim restrictions
- AI content limits
- Intellectual property restrictions
- Hook and first three seconds
- Product Proof
- Main communication proposition and selling point organization

The required flow is:

```text
Source
-> Source metadata
-> human review
-> Source Digest
```

This plan must not allow raw Source to be written directly into Knowledge.

## 2. Non-goals

This planning task does not include:

- accessing or scraping webpages;
- downloading files;
- downloading GitHub repositories;
- writing Source Digest files;
- writing or modifying Knowledge files;
- completing business Skills;
- collecting open-source repositories;
- screening licenses;
- collecting competitor videos in bulk;
- collecting competitor comments in bulk;
- collecting ordinary blogs or industry articles;
- developing automated scraping tools;
- developing Source freshness monitoring.

This plan also does not modify:

- `sources/`
- `source_digests/`
- `knowledge/`
- `.agents/skills/`
- `docs/02_SYSTEM_INSTRUCTIONS.md`
- `docs/04_SCRIPT_OUTPUT_SCHEMA.md`
- `docs/05_EVALUATION_RUBRIC.md`
- `docs/03_KNOWLEDGE_BASE_INDEX.md`

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
- `sources/README.md`
- `sources/AGENTS.md`
- `source_digests/TEMPLATE.md`
- `templates/SOURCE_METADATA.yaml`
- `docs/exec-plans/TEMPLATE.md`
- `docs/exec-plans/completed/03-knowledge-base-index-plan.md`

Key constraints from upstream:

- `docs/03_KNOWLEDGE_BASE_INDEX.md` is `APPROVED_FOR_V0_1_VALIDATION`.
- First batch Source slots `SRC-01` to `SRC-14` are planned, not collected.
- `SRC-15` open-source materials are out of this batch.
- v0.1 officially covers only car wireless vacuum and electric foam sprayer.
- Portable water flosser remains `DEFERRED_CATEGORY_PLACEHOLDER`.
- Competitor materials cannot prove product capability.
- Supplier claims cannot become verified product facts without internal validation.
- AI video cannot be used as real Product Proof.

## 4. Files to Read

Before executing this plan later, re-read:

- `AGENTS.md`
- `docs/PROJECT_STATUS.md`
- `docs/03_KNOWLEDGE_BASE_INDEX.md`
- `docs/06_KNOWLEDGE_SKILLS_ARCHITECTURE_AND_FEEDBACK_LOOP.md`
- `sources/README.md`
- `sources/AGENTS.md`
- `source_digests/TEMPLATE.md`
- `templates/SOURCE_METADATA.yaml`
- this execution plan

## 5. Files to Change

For this planning-only task:

- `docs/exec-plans/active/04-first-source-collection-plan.md`
- `docs/PROJECT_STATUS.md`

For later execution of Source Collection, expected file changes may include only approved Source records under:

- `sources/official/`
- `sources/policy_and_compliance/`
- `sources/product_tests/foam_sprayer/`
- `sources/product_tests/car_vacuum/`

Later Source Digest work must be handled by a separate execution plan before modifying:

- `source_digests/`

Batch 1A execution files created on 2026-07-17:

- `sources/policy_and_compliance/SRC-01_tiktok-shop-us-content-policy/metadata.yaml`
- `sources/policy_and_compliance/SRC-01_tiktok-shop-us-content-policy/source_record.md`
- `sources/policy_and_compliance/SRC-02_tiktok-shop-misleading-content/metadata.yaml`
- `sources/policy_and_compliance/SRC-02_tiktok-shop-misleading-content/source_record.md`
- `sources/policy_and_compliance/SRC-03_tiktok-shop-ai-content-restrictions/metadata.yaml`
- `sources/policy_and_compliance/SRC-03_tiktok-shop-ai-content-restrictions/source_record.md`
- `sources/policy_and_compliance/SRC-04_tiktok-shop-intellectual-property-policy/metadata.yaml`
- `sources/policy_and_compliance/SRC-04_tiktok-shop-intellectual-property-policy/source_record.md`
- `docs/source-collection/01_BATCH_1A_OFFICIAL_POLICY_COLLECTION_REPORT.md`

Batch 1A canonical correction files updated on 2026-07-17:

- `sources/policy_and_compliance/SRC-01_tiktok-shop-us-content-policy/metadata.yaml`
- `sources/policy_and_compliance/SRC-01_tiktok-shop-us-content-policy/source_record.md`
- `sources/policy_and_compliance/SRC-02_tiktok-shop-misleading-content/metadata.yaml`
- `sources/policy_and_compliance/SRC-02_tiktok-shop-misleading-content/source_record.md`
- `sources/policy_and_compliance/SRC-03_tiktok-shop-ai-content-restrictions/metadata.yaml`
- `sources/policy_and_compliance/SRC-03_tiktok-shop-ai-content-restrictions/source_record.md`
- `sources/policy_and_compliance/SRC-04_tiktok-shop-intellectual-property-policy/metadata.yaml`
- `sources/policy_and_compliance/SRC-04_tiktok-shop-intellectual-property-policy/source_record.md`
- `docs/source-collection/01_BATCH_1A_OFFICIAL_POLICY_COLLECTION_REPORT.md`
- `docs/PROJECT_STATUS.md`
- `CHANGELOG.md`

## 6. Work Steps

### Phase 1: Confirm Scope

- Confirm this is a planning task only.
- Confirm no external page is accessed during planning.
- Confirm no Source file, Source Digest, Knowledge file, or Skill file is created.
- Confirm first batch includes only `SRC-01` to `SRC-14`.
- Confirm `SRC-15` open-source materials are excluded.

### Phase 2: Batch 1A Planning

Batch 1A plans official policy and compliance collection for `SRC-01` to `SRC-04`.

| Source slot | Scope | Primary topics | Intended files |
|---|---|---|---|
| `SRC-01` | TikTok Shop US content rules | KBI-11 | `knowledge/06_COMPLIANCE_RULES.md` |
| `SRC-02` | Misleading content and unsupported Claim rules | KBI-06, KBI-11 | `knowledge/04_PRODUCT_PROOF.md`, `knowledge/06_COMPLIANCE_RULES.md` |
| `SRC-03` | TikTok official AI content rules | KBI-12 | `knowledge/06_COMPLIANCE_RULES.md` |
| `SRC-04` | TikTok / TikTok Shop intellectual property rules | KBI-11 | `knowledge/06_COMPLIANCE_RULES.md` |

Batch 1A gate:

- Each Source must have an official URL.
- Each Source must have a capture date.
- Market scope must be explicit.
- If market is not explicitly TikTok Shop US, mark `NEEDS_REVIEW`.
- Human review must approve metadata before any Digest is started.

### Phase 3: Batch 1B Planning

Batch 1B plans official creative reference collection for `SRC-05` to `SRC-06`.

| Source slot | Scope | Primary topics | Intended files |
|---|---|---|---|
| `SRC-05` | TikTok Creative Center official materials | KBI-02, KBI-05 | `knowledge/02_CONTENT_FORMATS.md`, `knowledge/03_HOOK_RULES.md` |
| `SRC-06` | TikTok official creative guidance | KBI-01, KBI-02, KBI-05, KBI-10 | `knowledge/01_GOOD_SCRIPT_STANDARD.md`, `knowledge/02_CONTENT_FORMATS.md`, `knowledge/03_HOOK_RULES.md` |

Batch 1B gate:

- Only official TikTok / TikTok Ads / TikTok Shop material is allowed.
- Creative examples cannot override compliance rules.
- Hook and creative guidance must be treated as guidance, not product proof.
- Human review must approve metadata before any Digest is started.

### Phase 4: Batch 1C Planning

Batch 1C plans internal Source intake for foam sprayer records `SRC-07` to `SRC-10`.

| Source slot | Scope | Primary topics | Intended files |
|---|---|---|---|
| `SRC-07` | Foam sprayer confirmed facts from `02_输入证据库` | KBI-06, KBI-16 | `knowledge/04_PRODUCT_PROOF.md`, category notes for compliance / proof |
| `SRC-08` | Foam sprayer actual spray test record | KBI-06, KBI-07, KBI-16 | `knowledge/04_PRODUCT_PROOF.md`, `knowledge/05_SHOT_PRODUCTION.md` |
| `SRC-09` | Foam sprayer foam-state test record | KBI-06, KBI-16 | `knowledge/04_PRODUCT_PROOF.md` |
| `SRC-10` | Foam sprayer shooting constraints and failed records | KBI-07, KBI-16 | `knowledge/05_SHOT_PRODUCTION.md` |

Batch 1C gate:

- Internal files or exports must be provided by the project owner.
- Supplier oral claims must remain separate from verified internal results.
- Each test record must include test conditions and test date.
- Attachments must be indexed, not silently embedded.
- Human review must approve intake before any Digest is started.

### Phase 5: Batch 1D Planning

Batch 1D plans internal Source intake for car vacuum records `SRC-11` to `SRC-14`.

| Source slot | Scope | Primary topics | Intended files |
|---|---|---|---|
| `SRC-11` | Car vacuum confirmed facts from `02_输入证据库` | KBI-06, KBI-16 | `knowledge/04_PRODUCT_PROOF.md`, category notes for compliance / proof |
| `SRC-12` | Car vacuum accessory and function test record | KBI-06, KBI-16 | `knowledge/04_PRODUCT_PROOF.md` |
| `SRC-13` | Seat gap, cup holder, floor mat real cleaning test | KBI-06, KBI-07, KBI-16 | `knowledge/04_PRODUCT_PROOF.md`, `knowledge/05_SHOT_PRODUCTION.md` |
| `SRC-14` | Car vacuum shooting constraints and failed records | KBI-07, KBI-16 | `knowledge/05_SHOT_PRODUCTION.md` |

Batch 1D gate:

- Internal files or exports must be provided by the project owner.
- Test records must identify sample, accessories, surface, debris, environment, and whether the result was repeatable.
- Jump cuts, competitor effects, and AI effects cannot be accepted as Product Proof.
- Human review must approve intake before any Digest is started.

### Phase 6: Human Review Gates

Each batch must stop at human review before the next stage.

Required review outcomes:

- `APPROVED_FOR_DIGEST`: metadata and Source intake are sufficient to start Source Digest work.
- `NEEDS_REVIEW`: Source exists but has market, date, provenance, or content ambiguity.
- `REJECTED`: Source is not official, not relevant, not usable, or violates scope.
- `WAITING_FOR_INTERNAL_INPUT`: internal record has not been provided or lacks required test information.

No batch may automatically create Source Digest or Knowledge.

## 7. Official Source Metadata Requirements

Each official Source must record:

- `source_id`
- `source_name`
- `official_url`
- `publisher`
- `source_type`
- `captured_at`
- `page_updated_at` if visible on the page
- `market_scope`
- `category_scope`
- `language`
- `credibility`
- `validity_status`
- `applicable_topics`
- `intended_knowledge_files`
- `intended_skills`
- `key_sections`
- `use_limitations`
- `local_record_path`

Rules for official Sources:

- Use only TikTok, TikTok Shop, or TikTok Ads official domains verified at collection time.
- Do not treat search result snippets, AI summaries, or browser previews as Sources.
- Open the original page and confirm visible page content before recording it.
- Record capture date for every official Source.
- If a page does not explicitly state TikTok Shop US applicability, do not describe it as US Shop policy.
- If a page is unavailable, redirects unexpectedly, or has unclear market scope, set `validity_status: NEEDS_REVIEW`.
- Do not copy long copyrighted passages.
- Save the URL, metadata, and only necessary short excerpts or section references.

Recommended official metadata extension:

```yaml
source_id: "SRC-01"
source_name: ""
official_url: ""
publisher: "TikTok | TikTok Shop | TikTok Ads"
source_type: "official | policy_and_compliance"
captured_at: "YYYY-MM-DD"
page_updated_at: ""
market_scope: "TikTok Shop US | global | unclear"
category_scope: "general | car cleaning | product claims | AI content | IP"
language: ""
credibility: "high"
validity_status: "valid | NEEDS_REVIEW | stale | rejected"
applicable_topics:
  - "KBI-11"
intended_knowledge_files:
  - "knowledge/06_COMPLIANCE_RULES.md"
intended_skills:
  - "tsd-input-fact-validation"
  - "tsd-script-quality-review"
key_sections:
  - ""
use_limitations:
  - ""
local_record_path: ""
notes: ""
```

## 8. Internal Source Minimum Intake Format

Each internal Source must use the following minimum intake fields:

- `source_id`
- `商品`
- `记录类型`
- `原始记录`
- `记录来源`
- `测试人`
- `测试日期`
- `商品样品或批次`
- `测试条件`
- `实际观察`
- `是否重复测试`
- `结论状态`
- `可用于什么脚本`
- `不能证明什么`
- `风险和限制`
- `附件路径`
- `关联知识主题`

Allowed conclusion statuses:

- `VERIFIED`
- `PARTIALLY_VERIFIED`
- `FAILED`
- `INCONCLUSIVE`
- `NOT_TESTED`
- `SUPPLIER_CLAIM_ONLY`

Recommended internal intake template:

```yaml
source_id: "SRC-08"
商品: "电动泡沫喷壶"
记录类型: "product_test | confirmed_fact_export | shooting_constraint | failed_record | supplier_claim"
原始记录: ""
记录来源: "02_输入证据库 | product test | shooting notes | manual note"
测试人: ""
测试日期: "YYYY-MM-DD"
商品样品或批次: ""
测试条件:
  场景: ""
  道具: []
  液体或清洁剂: ""
  表面或测试对象: ""
  环境条件: ""
  拍摄设备: ""
实际观察:
  - ""
是否重复测试: "yes | no | unknown"
结论状态: "VERIFIED | PARTIALLY_VERIFIED | FAILED | INCONCLUSIVE | NOT_TESTED | SUPPLIER_CLAIM_ONLY"
可用于什么脚本:
  - ""
不能证明什么:
  - ""
风险和限制:
  - ""
附件路径:
  - ""
关联知识主题:
  - "KBI-06"
  - "KBI-16"
notes: ""
```

Internal Source handling rules:

- Supplier Claim and internal verified fact must be stored separately.
- If a record comes from a supplier or salesperson only, use `SUPPLIER_CLAIM_ONLY`.
- `SUPPLIER_CLAIM_ONLY` cannot support Product Proof.
- Images, videos, spreadsheets, and text notes must be registered in `附件路径` or an attachment index.
- Test conditions and test date are required for `VERIFIED`, `PARTIALLY_VERIFIED`, `FAILED`, or `INCONCLUSIVE`.
- Missing required test information should set the review outcome to `WAITING_FOR_INTERNAL_INPUT`.

## 9. Directory and Naming Plan

Recommended later collection directories:

```text
sources/official/
sources/policy_and_compliance/
sources/product_tests/foam_sprayer/
sources/product_tests/car_vacuum/
```

Each Source should later have:

- original link or original record;
- `metadata.yaml`;
- necessary attachments or `attachments_index.md`.

Suggested directory naming:

```text
sources/policy_and_compliance/SRC-01_tiktok-shop-us-content-rules/
sources/policy_and_compliance/SRC-02_misleading-claims-rules/
sources/policy_and_compliance/SRC-03_ai-content-rules/
sources/policy_and_compliance/SRC-04_ip-rules/
sources/official/SRC-05_tiktok-creative-center/
sources/official/SRC-06_tiktok-creative-guidance/
sources/product_tests/foam_sprayer/SRC-07_foam-sprayer-confirmed-facts/
sources/product_tests/foam_sprayer/SRC-08_foam-sprayer-spray-test/
sources/product_tests/foam_sprayer/SRC-09_foam-sprayer-foam-state-test/
sources/product_tests/foam_sprayer/SRC-10_foam-sprayer-shooting-failures/
sources/product_tests/car_vacuum/SRC-11_car-vacuum-confirmed-facts/
sources/product_tests/car_vacuum/SRC-12_car-vacuum-accessory-function-test/
sources/product_tests/car_vacuum/SRC-13_car-vacuum-real-cleaning-test/
sources/product_tests/car_vacuum/SRC-14_car-vacuum-shooting-failures/
```

This plan does not create these directories or files.

## 10. Digest Handoff Plan

After a batch receives human review outcome `APPROVED_FOR_DIGEST`, a separate Source Digest execution plan should create Digest files.

Expected Digest routing:

| Source slots | Future Digest focus | Intended Knowledge |
|---|---|---|
| `SRC-01` to `SRC-04` | Compliance, misleading Claims, AI content, IP limits | `knowledge/06_COMPLIANCE_RULES.md`; selected rules for `knowledge/04_PRODUCT_PROOF.md` |
| `SRC-05` to `SRC-06` | Hook, creative formats, first-three-second guidance | `knowledge/01_GOOD_SCRIPT_STANDARD.md`, `knowledge/02_CONTENT_FORMATS.md`, `knowledge/03_HOOK_RULES.md` |
| `SRC-07` to `SRC-10` | Foam sprayer verified Product Proof and production constraints | `knowledge/04_PRODUCT_PROOF.md`, `knowledge/05_SHOT_PRODUCTION.md`, category sections |
| `SRC-11` to `SRC-14` | Car vacuum verified Product Proof and production constraints | `knowledge/04_PRODUCT_PROOF.md`, `knowledge/05_SHOT_PRODUCTION.md`, category sections |

Digest files must preserve original claims, executable conclusions, applicable situations, exceptions, misuse, risks, affected Knowledge files, affected Skills, and open questions.

## 11. Acceptance Criteria

This execution plan is acceptable when it defines:

- four batches: `1A`, `1B`, `1C`, and `1D`;
- all official Source metadata requirements;
- all internal Source intake fields;
- human review gates before Source Digest;
- strict separation between official Sources, internal tests, supplier Claims, competitor references, and AI effects;
- requirement that every official Source has official URL and capture date;
- requirement that market scope is explicit;
- requirement that internal tests include test conditions;
- rule that AI or competitor effects cannot be Product Proof;
- rule that Source cannot be written directly into Knowledge;
- rule that open-source project collection is not part of this batch;
- rule that Source count must not expand without an updated plan;
- mapping from each Source to KBI topics and future Digest focus.

Later Source Collection execution is acceptable only when:

- every official Source has official URL and capture date;
- official page content has been opened and confirmed;
- market scope is explicit or marked `NEEDS_REVIEW`;
- internal tests include test date, test conditions, actual observations, and conclusion status;
- supplier Claims are isolated from verified facts;
- attachments are indexed;
- each Source clearly maps to KBI topics;
- each Source clearly maps to future Digest targets;
- human review approves the Source before Digest work begins.

## 12. Risks and Unknowns

- Official policy pages may move, redirect, or be market-ambiguous.
- Some official pages may be global rather than TikTok Shop US-specific.
- Internal records may exist only as chat notes, screenshots, videos, or partial Feishu exports.
- Internal tests may lack sample/batch, date, or repeatability information.
- Supplier statements may be mixed with internal observations in the same note.
- Product tests may show partial or failed results that need to be preserved, not cleaned up.
- Batch 1A policy collection may block later compliance Knowledge if market scope is unclear.

Open questions for human confirmation before actual collection:

- Which internal foam sprayer files or Feishu exports will be provided for `SRC-07` to `SRC-10`?
- Which internal car vacuum files or Feishu exports will be provided for `SRC-11` to `SRC-14`?
- Who is allowed to approve internal test records as `VERIFIED` or `PARTIALLY_VERIFIED`?
- What attachment storage path should be used for large images and videos?
- Should Batch 1A and Batch 1B be executed by the same reviewer or separately?

## 13. Progress Log

- 2026-07-17: Created first Source Collection execution plan.
- 2026-07-17: Updated `docs/PROJECT_STATUS.md` to mark current phase as first Source Collection planning.
- 2026-07-17: Ran repository structure validation; validation passed.
- 2026-07-17: Executed Batch 1A only: collected `SRC-01` through `SRC-04` official policy Sources under `sources/policy_and_compliance/`.
- 2026-07-17: Created `docs/source-collection/01_BATCH_1A_OFFICIAL_POLICY_COLLECTION_REPORT.md`.
- 2026-07-17: Updated `docs/PROJECT_STATUS.md` and `CHANGELOG.md` for Batch 1A pending human review.
- 2026-07-17: Batch 1B, 1C, and 1D were not executed.
- 2026-07-17: Executed Batch 1A Human Review and Canonical Source Correction for `SRC-01` through `SRC-04`.
- 2026-07-17: Updated Source metadata and source records with `canonical_official_url`, `legacy_or_alternate_urls`, page title, page date, applicability notes, review status, and review notes.
- 2026-07-17: Updated Batch 1A report with canonical URL review, legacy URL review, market applicability, final review status, corrections performed, and unresolved questions.
- 2026-07-17: Confirmed no Source Digest, Knowledge, Skills, System Instructions, Output Schema, or Evaluation Rubric files were modified.

## 14. Decision Log

- 2026-07-17: First collection batch is limited to `SRC-01` through `SRC-14`.
- 2026-07-17: `SRC-15` open-source materials are excluded and require a later plan.
- 2026-07-17: Batch execution must stop for human review before Source Digest.
- 2026-07-17: Internal Source intake must isolate supplier Claims from verified facts.
- 2026-07-17: No Source may be written directly into Knowledge.
- 2026-07-17: Initial Batch 1A collection used `COLLECTED_PENDING_HUMAN_REVIEW`; no Source was marked `APPROVED` before human review.
- 2026-07-17: `SRC-02` is recorded as TikTok Shop global guidance, not US-exclusive policy.
- 2026-07-17: TikTok platform AI-generated content support page is recorded only as a related reference under `SRC-03`, not as a separate TikTok Shop US policy Source.
- 2026-07-17: Human review approved `SRC-01`, `SRC-03`, and `SRC-04` as `APPROVED_SOURCE`.
- 2026-07-17: `SRC-02` remains `COLLECTED_PENDING_HUMAN_REVIEW` because canonical page title/date and market applicability need final human confirmation.
- 2026-07-17: Legacy URLs for `SRC-02`, `SRC-03`, and `SRC-04` are retained as `LEGACY_OR_UNRESOLVED`; no legacy URL was deleted.
- 2026-07-17: Batch 1B, 1C, and 1D remain unexecuted; this execution plan remains active.

## 15. Validation Performed

- 2026-07-17: `python3 scripts/validate_structure.py` passed.
- 2026-07-17: `python3 scripts/validate_structure.py` passed after Batch 1A Source collection.
- 2026-07-17: `python3 scripts/validate_structure.py` passed after Batch 1A canonical Source correction.

## 16. Final Result

Execution plan created and validated.

Batch 1A has been executed for `SRC-01` through `SRC-04` only. The collected official policy Sources have received canonical Source correction. No Source Digest, Knowledge, Skill, System Instructions, Output Schema, or Evaluation Rubric files were modified.

Batch 1B, 1C, and 1D remain unexecuted. This execution plan remains active.

Canonical correction result:

- `SRC-01`: `APPROVED_SOURCE`
- `SRC-02`: `COLLECTED_PENDING_HUMAN_REVIEW`
- `SRC-03`: `APPROVED_SOURCE`
- `SRC-04`: `APPROVED_SOURCE`

No Source Digest has been created.
