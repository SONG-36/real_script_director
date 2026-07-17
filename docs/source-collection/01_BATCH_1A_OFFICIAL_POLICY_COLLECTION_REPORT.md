# Batch 1A Official Policy Source Collection Report

**Status**: HUMAN_REVIEWED_WITH_ONE_PENDING_SOURCE  
**Batch**: 1A  
**Scope**: SRC-01 to SRC-04 official policy Source collection and canonical Source correction  
**Captured at**: 2026-07-17  
**Reviewed at**: 2026-07-17  
**Collector**: Codex  

This report records Source collection and canonical Source correction only. It does not create Source Digest, Knowledge, Skills, System Instructions, Output Schema, or Evaluation Rubric content.

---

# 1. 成功收集的 Source

| Source ID | Source name | Final human review status | Local path |
|---|---|---|---|
| SRC-01 | Content Policy | APPROVED_SOURCE | `sources/policy_and_compliance/SRC-01_tiktok-shop-us-content-policy/` |
| SRC-02 | Avoid Misleading Content | COLLECTED_PENDING_HUMAN_REVIEW | `sources/policy_and_compliance/SRC-02_tiktok-shop-misleading-content/` |
| SRC-03 | AI-Generated Content Restrictions and Requirements | APPROVED_SOURCE | `sources/policy_and_compliance/SRC-03_tiktok-shop-ai-content-restrictions/` |
| SRC-04 | Intellectual Property Policy | APPROVED_SOURCE | `sources/policy_and_compliance/SRC-04_tiktok-shop-intellectual-property-policy/` |

Each Source has:

- `metadata.yaml`
- `source_record.md`

---

# 2. Canonical URL Review

| Source ID | Canonical page title | Canonical official URL | Publisher |
|---|---|---|---|
| SRC-01 | Content Policy | https://seller-us.tiktok.com/university/essay?knowledge_id=6837891779151617&lang=en | TikTok Shop |
| SRC-02 | How to Avoid Misleading Content | https://seller-us.tiktok.com/university/essay?knowledge_id=4581457528194817&lang=en | TikTok Shop |
| SRC-03 | AI-Generated Content Restrictions and Requirements | https://seller-us.tiktok.com/university/essay?knowledge_id=491489038501663&lang=en | TikTok Shop |
| SRC-04 | Intellectual Property Policy | https://seller-us.tiktok.com/university/essay?knowledge_id=6837901778306818&lang=en | TikTok Shop |

---

# 3. Legacy URL Review

| Source ID | Legacy or alternate URL | Status | Notes |
|---|---|---|---|
| SRC-01 | none | none | Existing canonical URL remains valid. |
| SRC-02 | https://seller-us.tiktok.com/university/essay?knowledge_id=1058688291165954 | LEGACY_OR_UNRESOLVED | Previous collected URL. Not accepted as canonical. No redirect or duplicate relationship confirmed in this pass. |
| SRC-03 | https://seller-us.tiktok.com/university/essay?knowledge_id=3902911834068738 | LEGACY_OR_UNRESOLVED | Previous collected URL. Retained as legacy/alternate. No redirect or duplicate relationship confirmed in this pass. |
| SRC-04 | https://seller-us.tiktok.com/university/essay?knowledge_id=2326301033883393 | LEGACY_OR_UNRESOLVED | Previous collected URL. Retained as legacy/alternate. No redirect or duplicate relationship confirmed in this pass. |

Local command-line `curl` checks to `seller-us.tiktok.com` timed out during this pass. Canonical review used the official page URLs and visible official page metadata; unresolved legacy redirect behavior is preserved instead of guessed.

---

# 4. Current Page Date and Capture Date

| Source ID | Current page date recorded | Expected date from review request | Captured at | Notes |
|---|---:|---:|---:|---|
| SRC-01 | 2026-07-01 | 2026-07-01 | 2026-07-17 | Matches review request. |
| SRC-02 | 2026-06-25 | 2026-03-13 | 2026-07-17 | Date mismatch retained; Source remains pending. |
| SRC-03 | 2026-05-13 | 2026-05-13 | 2026-07-17 | Matches review request. |
| SRC-04 | 2026-06-30 | 2026-03-19 | 2026-07-17 | Current official page date differs from review request; approved with mismatch noted. |

---

# 5. Market Applicability

| Source ID | Market scope recorded | Applicability notes |
|---|---|---|
| SRC-01 | TikTok Shop US | Official page shows Applies to: United States. |
| SRC-02 | TikTok Shop official guidance served through US Academy; not US-exclusive | Do not simplify to US-exclusive because guidance text references global TikTok Shop coverage. |
| SRC-03 | TikTok Shop policy; United States served through seller-us TikTok Shop Academy | TikTok Support AI page remains platform-general related reference only. |
| SRC-04 | TikTok Shop US | Official page served through seller-us TikTok Shop Academy and treated as TikTok Shop US policy Source after review. |

---

# 6. Correction Performed

| Source ID | Correction |
|---|---|
| SRC-01 | Added canonical URL fields, page title, applicability notes, review status, reviewed date, and review notes. Marked `APPROVED_SOURCE`. |
| SRC-02 | Corrected canonical knowledge_id to `4581457528194817`; retained old `1058688291165954` URL as `LEGACY_OR_UNRESOLVED`; updated page date and applicability notes; kept pending. |
| SRC-03 | Corrected canonical knowledge_id to `491489038501663`; retained old `3902911834068738` URL as `LEGACY_OR_UNRESOLVED`; confirmed TikTok Shop policy source; kept TikTok Support AI page as related reference only; marked `APPROVED_SOURCE`. |
| SRC-04 | Corrected canonical knowledge_id to `6837901778306818`; retained old `2326301033883393` URL as `LEGACY_OR_UNRESOLVED`; recorded trademark, copyright, knockoff products, and content usage sections; marked `APPROVED_SOURCE`. |

---

# 7. 关联 KBI

| Source ID | Related KBI |
|---|---|
| SRC-01 | KBI-11 |
| SRC-02 | KBI-06, KBI-11 |
| SRC-03 | KBI-12 |
| SRC-04 | KBI-11 |

---

# 8. 关联 Knowledge

| Source ID | Intended Knowledge files |
|---|---|
| SRC-01 | `knowledge/06_COMPLIANCE_RULES.md` |
| SRC-02 | `knowledge/04_PRODUCT_PROOF.md`, `knowledge/06_COMPLIANCE_RULES.md` |
| SRC-03 | `knowledge/06_COMPLIANCE_RULES.md` |
| SRC-04 | `knowledge/06_COMPLIANCE_RULES.md` |

No Knowledge files were modified in this batch.

---

# 9. NEEDS_REVIEW and Pending Items

No Source is marked `NEEDS_REVIEW`.

Pending item:

- SRC-02 remains `COLLECTED_PENDING_HUMAN_REVIEW` because the canonical page title/date observed in this pass does not fully match the review request, and market applicability should not be simplified to US-exclusive.

---

# 10. Unresolved Questions

1. Should SRC-02 be approved with page title `How to Avoid Misleading Content` and page date 2026-06-25, or should the reviewer provide another canonical page matching `Avoid Misleading Content` and 2026-03-13?
2. Should SRC-04 retain `APPROVED_SOURCE` despite the current official page date being 2026-06-30 rather than expected 2026-03-19?
3. Should the TikTok platform-general AI help page under SRC-03 become a separate future Source, or remain only a related reference?

---

# 11. Not Collected in This Batch

Not collected in this batch:

- SRC-05 TikTok Creative Center: excluded because Batch 1B was not executed.
- SRC-06 TikTok official creative guidance: excluded because Batch 1B was not executed.
- SRC-07 to SRC-14 internal product records: excluded because Batch 1C and Batch 1D were not executed.
- Open-source projects and GitHub repositories: excluded by the active execution plan.
- Competitor videos, competitor comments, creator data, sales data, account data, and market route materials: excluded by Custom GPT scope lock and active plan boundaries.
- Additional official IP subtopic pages: deferred to human review decision to avoid uncontrolled Source expansion.

---

# 12. Next Human Review Checklist

- Confirm whether SRC-02 should be approved or corrected again.
- Confirm whether SRC-04 date mismatch is acceptable as approved.
- Confirm whether approved Sources may enter a future Source Digest execution plan.
- Do not create Source Digest until human review explicitly authorizes Digest work.
