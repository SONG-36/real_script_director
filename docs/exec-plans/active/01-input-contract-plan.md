# Execution Plan｜01_INPUT_CONTRACT.md

**Status**: ACTIVE  
**Owner**: Codex + project owner  
**Started**: 2026-07-17  
**Target**: Freeze `docs/01_INPUT_CONTRACT.md` as the v0.1 input contract for TikTok Script Director.

## 1. Goal

Create `docs/01_INPUT_CONTRACT.md` to define how one Feishu video concept and its related product, evidence, and competitor references are converted into a stable Script Input Pack for Custom GPT.

The document must make clear:

- which fields the Script Input Pack accepts;
- which fields are required, optional, or conditionally required;
- how the four Feishu tables map into the input pack;
- how missing, provisional, or conflicting input changes generation status;
- how single-selling-point and multi-selling-point concepts should be represented;
- what input examples and invalid examples should look like.

## 2. Non-goals

This task will not:

- modify `docs/00_MASTER_DESIGN.md`;
- write or populate `docs/02_SYSTEM_INSTRUCTIONS.md`, `docs/03_KNOWLEDGE_BASE_INDEX.md`, `docs/04_SCRIPT_OUTPUT_SCHEMA.md`, or `docs/05_EVALUATION_RUBRIC.md`;
- start knowledge base writing;
- ingest or scrape TikTok, GitHub, or other external sources;
- develop Python tooling, Feishu API integration, backend services, frontend pages, database logic, or multi-agent orchestration;
- create final shooting scripts;
- create automatic Feishu export or Script Input Pack generation logic.

## 3. Current upstream facts

Current source of truth:

- `docs/00_MASTER_DESIGN.md` is the approved v0.1 validation design boundary.
- `docs/06_KNOWLEDGE_SKILLS_ARCHITECTURE_AND_FEEDBACK_LOOP.md` defines the knowledge, Skills, evaluation, feedback, and versioning architecture.
- `docs/PROJECT_STATUS.md` marks `docs/01_INPUT_CONTRACT.md` as the active next design item.

Facts to carry forward:

- TikTok Script Director v0.1 is a single-agent, Custom GPT + human input + human review system.
- The system starts from a spoken or rough video concept and ends at a formal shooting script.
- The current chain is `01_商品卡 -> 02_输入证据库 -> 03_竞品参考 -> 04_自有视频构想卡 -> Script Input Pack -> TikTok Script Director`.
- The first version allows manual copy,整理, and paste into Custom GPT; automation is deferred.
- The first validation products are car cordless vacuum and electric foam sprayer; portable water flosser is deferred for the first script validation round.
- The system must distinguish verified product facts, unverified supplier claims, user problems, scenarios, core selling points, auxiliary selling points, visual proof, risks, competitor expression references, and missing input.
- Competitor videos are expression references only. They must not be treated as proof of our product's capability.
- AI video effects must not be treated as real Product Proof.
- Output generation status must be `READY`, `PROVISIONAL`, or `BLOCKED`.

## 4. Files to read

Required:

- `AGENTS.md`
- `README.md`
- `ARCHITECTURE.md`
- `docs/index.md`
- `docs/PROJECT_STATUS.md`
- `docs/00_MASTER_DESIGN.md`
- `docs/06_KNOWLEDGE_SKILLS_ARCHITECTURE_AND_FEEDBACK_LOOP.md`
- `docs/07_REPOSITORY_OPERATING_MODEL.md`
- `docs/exec-plans/TEMPLATE.md`

Optional only if needed during drafting:

- `docs/01_INPUT_CONTRACT.md`, if it exists before implementation begins
- `templates/`, if existing input templates are added before or during this task
- `.agents/skills/tsd-input-fact-validation/SKILL.md`, only to check future Skill compatibility without changing the Skill
- `evals/`, only to check whether example case directories already exist without filling them

## 5. Files to change

Primary file:

- `docs/01_INPUT_CONTRACT.md`

Status and tracking files, only if the final document is created or materially updated:

- `docs/PROJECT_STATUS.md`
- this execution plan
- `CHANGELOG.md`, if the repository is already using it for this design milestone

Do not modify:

- `docs/00_MASTER_DESIGN.md`
- `docs/02_SYSTEM_INSTRUCTIONS.md`
- `docs/03_KNOWLEDGE_BASE_INDEX.md`
- `docs/04_SCRIPT_OUTPUT_SCHEMA.md`
- `docs/05_EVALUATION_RUBRIC.md`

## 6. Work steps

- [ ] Confirm whether `docs/01_INPUT_CONTRACT.md` already exists and whether it has content to preserve.
- [ ] Draft the document header with status, version, upstream documents, scope, and non-goals.
- [ ] Define the Script Input Pack top-level structure.
- [ ] Map Feishu tables `01_商品卡`, `02_输入证据库`, `03_竞品参考`, and `04_自有视频构想卡` into Script Input Pack sections.
- [ ] Define required, optional, and conditionally required fields.
- [ ] Define `READY`, `PROVISIONAL`, and `BLOCKED` status rules.
- [ ] Add single-selling-point video input example.
- [ ] Add multi-selling-point video input example.
- [ ] Add insufficient-input and conflicting-input examples.
- [ ] Add manual copy/paste formatting guidance.
- [ ] Add validation checklist for future input packs.
- [ ] Update required project tracking files if the final document is created.
- [ ] Run `python3 scripts/validate_structure.py`.
- [ ] Record validation result and final outcome in this plan.

## 7. Feishu table to Script Input Pack mapping tasks

### 7.1 `01_商品卡`

Define how product identity fields map into `商品基础信息`:

- product name;
- product image or visual reference;
- category;
- functional purpose;
- accessories and package notes.

Clarify that `01_商品卡` does not decide script selling points by itself.

### 7.2 `02_输入证据库`

Define how evidence rows map into:

- `已验证商品事实`;
- `已验证用户问题`;
- `已验证使用场景`;
- `核心卖点候选`;
- `辅助卖点候选`;
- `可用于剧本的画面证明`;
- `待验证内容`;
- `风险与限制`.

The mapping must preserve evidence status:

- `未核实`;
- `待测试`;
- `已确认`;
- `不成立`.

The document must state that only `已确认` and `可用于剧本 = 是` content can become deterministic script claims.

### 7.3 `03_竞品参考`

Define how competitor reference fields map into `竞品参考`:

- reference video name;
- related product;
- video link;
- video type;
- reference function;
- reference conclusion.

Clarify allowed reference functions:

- Hook;
- scene;
- operation;
- visual proof method;
- structure;
- CTA.

Clarify forbidden uses:

- copying competitor parameters;
- copying competitor-specific accessories;
- treating competitor capability as our capability;
- treating AI video as real product evidence.

### 7.4 `04_自有视频构想卡`

Define how one concept row maps into `本次任务` and `口语构想`:

- concept name or video theme;
- product;
- reference video;
- user pain point;
- how the product solves it;
- how the picture proves it;
- shooting conditions;
- current missing information.

Clarify that one `04_自有视频构想卡` row represents one future video concept, not a final script.

## 8. Field design tasks

### 8.1 Required fields

Define fields that must exist before any script strategy can be generated:

- product identity;
- concept name or video theme;
- target market;
- user problem or usage scenario;
- proposed product solution;
- at least one candidate visual proof path;
- evidence status for any product claim used as a selling point;
- known risks or explicit statement that no known risk has been recorded.

### 8.2 Optional fields

Define fields that improve quality but do not necessarily block generation:

- target duration;
- competitor reference;
- product image;
- accessory notes;
- CTA preference;
- shooting style preference;
- actor or hand model availability;
- specific prop details;
- prior hook idea.

### 8.3 Conditionally required fields

Define fields required only when the concept depends on them:

- accessories, if the concept demonstrates an accessory or attachment;
- cleaning agent ratio or material, if a result depends on detergent, foam, stains, debris, water pressure, or surface condition;
- comparison baseline, if the concept uses before/after or manual-vs-electric contrast;
- real test result, if the claim says a capability has been proven;
- competitor reference conclusion, if a competitor video is cited;
- compliance review note, if the concept touches medical, health, safety, absolute performance, or platform-sensitive claims;
- shooting condition, if the proof requires a specific location, vehicle, lighting, water source, model, or continuous take.

## 9. READY / PROVISIONAL / BLOCKED design tasks

### 9.1 `READY`

Define `READY` as:

- product and concept are clear;
- core selling point has verified supporting fact;
- visual proof is realistic and shootable;
- required conditional fields are present;
- competitor references are used only as expression references;
- no unresolved critical risk blocks the concept.

### 9.2 `PROVISIONAL`

Define `PROVISIONAL` as:

- concept direction is usable;
- core logic can be drafted;
- one or more supporting shots, auxiliary selling points, exact wording, or proof details still need verification;
- the output must visibly mark all provisional content and pre-shoot validation tasks.

### 9.3 `BLOCKED`

Define `BLOCKED` as:

- product identity is unclear;
- core capability is unverified or contradicted;
- proposed visual proof cannot be shot truthfully;
- the concept relies on competitor-only capability;
- risk is too serious to write a formal script;
- missing input prevents determining the main user problem, product solution, or proof path.

## 10. Single-selling-point video input example task

Create one complete Script Input Pack example for a single-selling-point video.

Recommended product:

- car cordless vacuum.

Recommended concept direction:

- seat gap cleaning with a narrow nozzle.

The example should demonstrate:

- one core problem;
- one core selling point;
- clear Product Proof;
- minimal auxiliary information;
- `READY` or narrowly scoped `PROVISIONAL` status reasoning.

## 11. Multi-selling-point video input example task

Create one complete Script Input Pack example for a multi-selling-point video.

Recommended product:

- electric foam sprayer.

Recommended concept direction:

- manual pump fatigue versus electric continuous spraying, with one or two related auxiliary selling points such as nozzle adjustment or coverage flow.

The example should demonstrate:

- one main communication proposition;
- one core selling point;
- related auxiliary selling points;
- information density constraints;
- proof requirements for each selling point;
- `READY` or `PROVISIONAL` status reasoning.

## 12. Insufficient and conflicting input example tasks

Create at least two negative examples:

- insufficient input example: missing product capability proof, missing shooting condition, or missing user problem;
- conflicting input example: supplier claim conflicts with internal test result, competitor capability is copied to our product, or visual proof contradicts risk notes.

Each negative example must show:

- problematic input;
- why it is insufficient or conflicting;
- expected status: `PROVISIONAL` or `BLOCKED`;
- what information is needed to recover.

## 13. Acceptance criteria

The task is complete when:

- `docs/01_INPUT_CONTRACT.md` exists and has explicit document status;
- the document states v0.1 scope and non-goals;
- all four Feishu tables are mapped to Script Input Pack sections;
- required, optional, and conditionally required fields are defined;
- `READY`, `PROVISIONAL`, and `BLOCKED` rules are clear enough for `tsd-input-fact-validation` to use later;
- the document includes one single-selling-point input example;
- the document includes one multi-selling-point input example;
- the document includes insufficient-input and conflicting-input examples;
- examples do not invent final product capabilities beyond the upstream facts available in design documents;
- no prohibited files are modified;
- `python3 scripts/validate_structure.py` passes, or any failure is recorded with cause and next action.

## 14. Risks and unknowns

- The exact current Feishu field names may differ from the typical fields listed in `00_MASTER_DESIGN.md`.
- Product-specific verified facts for the car cordless vacuum and electric foam sprayer may not yet exist in structured evidence files.
- Some examples may need to be clearly marked as sample input shapes rather than confirmed product claims.
- `READY` versus `PROVISIONAL` boundaries may require project owner confirmation, especially when a core idea is plausible but proof has not been filmed yet.
- Compliance-sensitive categories are not yet supported by a completed compliance knowledge file.
- If `docs/01_INPUT_CONTRACT.md` becomes too large, examples may later need to move into `evals/cases/`, but this task should keep first examples in the input contract for readability.

## 15. Validation method

Use repository structural validation:

```bash
python3 scripts/validate_structure.py
```

Manual validation checklist:

- compare the document against `docs/00_MASTER_DESIGN.md` section 8 and section 18;
- confirm it does not introduce automation or backend scope;
- confirm it does not turn competitor references into product evidence;
- confirm every example has a clear generation status;
- confirm missing or conflicting information does not produce a full unconditional script path.

## 16. Progress log

- 2026-07-17: Execution plan created from required upstream documents.
- 2026-07-17: Ran repository structure validation after plan creation; validation failed because required Skill skeleton files are missing.

## 17. Decision log

- 2026-07-17: Keep examples inside `docs/01_INPUT_CONTRACT.md` for the first contract draft so reviewers can validate field rules and example usage in one place.
- 2026-07-17: Treat exact Feishu field names as an open confirmation item unless current exported field definitions are provided.

## 18. Validation performed

Ran:

```bash
python3 scripts/validate_structure.py
```

Result:

```text
Validation failed with 6 issue(s).
```

Failures:

- missing skill: `.agents/skills/tsd-input-fact-validation/SKILL.md`
- missing skill: `.agents/skills/tsd-concept-strategy-design/SKILL.md`
- missing skill: `.agents/skills/tsd-shooting-script-generation/SKILL.md`
- missing skill: `.agents/skills/tsd-script-quality-review/SKILL.md`
- missing skill: `.agents/skills/repo-source-digest/SKILL.md`
- missing skill: `.agents/skills/repo-exec-plan-maintenance/SKILL.md`

The final input contract still needs validation after `docs/01_INPUT_CONTRACT.md` is drafted.

## 19. Final result

Pending.
