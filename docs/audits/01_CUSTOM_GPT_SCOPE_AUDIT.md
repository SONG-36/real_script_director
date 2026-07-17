# Custom GPT Scope Audit

**Audit ID**: `01_CUSTOM_GPT_SCOPE_AUDIT`  
**Date**: 2026-07-17  
**Status**: COMPLETED_SCOPE_LOCKED  
**Audited target**: TikTok Script Director v0.1 Custom GPT scope  

---

# 1. 审核范围

本次审计检查当前仓库是否始终收敛为：

> 将一条已经确定的自有视频构想，转换成正式 TikTok Shop US 拍摄脚本。

实际纳入文件级矩阵的文件数：42。

审计范围包括：

- 根目录项目文件；
- `docs/00` 至 `docs/08`；
- `knowledge/` 全部文件；
- `.agents/skills/` 全部 `SKILL.md`；
- `templates/` 全部模板；
- `sources/README.md` 和 `sources/AGENTS.md`；
- `source_digests/README.md` 和 `source_digests/TEMPLATE.md`；
- 当前 active 和 completed execution plans。

本次没有访问外部资料，没有抓取网页，没有修改业务设计、Knowledge、Skills、Templates、Sources 或 Source Digests。

---

# 2. 当前 Custom GPT 的准确职责

当前 Custom GPT 只负责：

```text
一条人工整理好的 Script Input Pack
→ 输入完整性和事实检查
→ READY / PROVISIONAL / BLOCKED
→ 保留并规范化用户构想
→ 派生主传播命题
→ 区分核心卖点和辅助卖点
→ 在给定构想内部选择内容形式和脚本结构
→ 设计 Hook
→ 设计 Product Proof
→ 生成逐镜头正式拍摄脚本
→ 生成英文字幕或旁白和中文审核含义
→ 生成拍摄准备清单
→ 生成两个 Hook 变体
→ 执行脚本质量审核
```

输出目标是一份正式、真实、可拍、可审核的 TikTok Shop US 拍摄脚本。

---

# 3. 当前输入

唯一批准输入为 `docs/01_INPUT_CONTRACT.md` 中的人工扁平 Script Input Pack：

```yaml
视频构想:
  视频主题: ""
  商品: ""
  视频目标: "转化"
  市场: "TikTok Shop US"
  用户痛点: ""
  产品怎么解决: ""
  画面怎么证明: ""
  拍摄条件: ""
  目前缺什么: ""

已验证商品事实:
  - ""

待验证内容: []

风险限制: []

参考视频: []
```

不得重新引入：

- 飞书原始行结构；
- 市场数据字段；
- 达人数据字段；
- 产品路线决策字段；
- `GO / TEST / NO-GO` 字段。

---

# 4. 当前输出

`docs/04_SCRIPT_OUTPUT_SCHEMA.md` 是唯一权威输出合同，但当前状态仍为 `NOT_STARTED`。

现有占位范围符合当前职责，应冻结为：

- 生成状态；
- 构想规范化；
- 视频策略；
- 主传播命题；
- 核心与辅助卖点；
- 逐镜头表；
- 字幕与旁白；
- 拍摄清单；
- Hook 变体；
- 审核结果。

不得输出：

- 产品市场结论；
- 达人路线结论；
- 账号策略；
- 产品级内容组合；
- 发布计划；
- 销量、GMV 或转化预测。

---

# 5. 允许的内部决策

当前 Custom GPT 可以在单条已确定构想内部做：

- 输入是否足以支持脚本；
- 哪些内容可作为已验证事实；
- 哪些内容待验证；
- `READY / PROVISIONAL / BLOCKED`；
- 主传播命题；
- 核心卖点和辅助卖点；
- 内容形式；
- 脚本结构；
- Hook；
- Product Proof；
- 是否需要真人、手部操作或旁白；
- 镜头执行方式；
- 脚本质量审核。

这些都是脚本策略，不是产品级路线策略。

---

# 6. 禁止的上游决策

当前 Custom GPT 不得执行：

- 市场研究；
- 选品；
- 商品是否值得做；
- 商品整体应该走达人路线还是产品内容路线；
- 达人依赖判断；
- 官方号、渠道号、达人总体分工；
- 账号定位；
- 产品级内容组合；
- 整个产品的内容排期；
- 市场销量和竞品数据抓取；
- 达人数据抓取；
- 爆款概率判断；
- GMV、销量和转化预测；
- 价格、优惠和投流策略；
- 发布排期；
- 自动生成大量构想；
- 发布数据归因；
- `GO / TEST / NO-GO` 内容路线决策；
- 多 Agent 编排；
- 后端和飞书自动化。

这些内容只能作为上游或未来模块边界说明出现。

---

# 7. 文件级审核矩阵

分类枚举：

- `IN_SCOPE`: 完全符合当前 Script Director 职责。
- `BOUNDARY_REFERENCE_ONLY`: 只用于说明上游、反馈或未来边界，不进入当前运行逻辑。
- `FUTURE_MODULE`: 明确属于完整系统未来模块。
- `AMBIGUOUS`: 表述可能让 Codex 或 Custom GPT 误以为属于当前职责。
- `SCOPE_DRIFT`: 已经将市场、达人、账号或产品级内容路线加入当前 Custom GPT。

| 文件 | 当前作用 | 分类 | 问题 | 严重度 | 建议 |
|---|---|---|---|---|---|
| `AGENTS.md` | 仓库边界和工作规则 | `IN_SCOPE` | 明确当前链路，不扩展成完整平台。 | NONE | 保持。 |
| `README.md` | 项目入口说明 | `AMBIGUOUS` | 当前阶段和下一项仍提到早期状态，存在轻微过时。 | LOW | 后续状态清理时更新，不影响运行边界。 |
| `ARCHITECTURE.md` | 仓库信息架构 | `IN_SCOPE` | 无。 | NONE | 保持。 |
| `CHANGELOG.md` | 版本记录 | `IN_SCOPE` | 无。 | NONE | 保持。 |
| `docs/index.md` | 文档状态索引 | `IN_SCOPE` | 无。 | NONE | 保持。 |
| `docs/PROJECT_STATUS.md` | 当前项目状态 | `IN_SCOPE` | 无。 | NONE | 保持。 |
| `docs/00_MASTER_DESIGN.md` | v0.1 总设计 | `IN_SCOPE` | 已在 Section 8 旧 Script Input Pack 前增加 `RUNTIME_INPUT_SUPERSEDED`，明确运行时输入以 01 为准。 | NONE | 保持。 |
| `docs/01_INPUT_CONTRACT.md` | 已批准输入合同 | `IN_SCOPE` | 明确使用人工扁平输入包，排除飞书原始结构和派生策略字段。 | NONE | 保持。 |
| `docs/02_SYSTEM_INSTRUCTIONS.md` | 系统指令占位 | `IN_SCOPE` | 尚未开始，没有越界内容。 | NONE | 后续编写时必须显式拒绝市场/达人/路线请求。 |
| `docs/03_KNOWLEDGE_BASE_INDEX.md` | 已批准知识索引 | `IN_SCOPE` | Source 和 Knowledge 规划只服务脚本生成知识。 | NONE | 保持。 |
| `docs/04_SCRIPT_OUTPUT_SCHEMA.md` | 输出合同占位 | `IN_SCOPE` | 尚未开始，没有越界输出字段。 | NONE | 后续不得加入路线、达人、账号、预测输出。 |
| `docs/05_EVALUATION_RUBRIC.md` | 评测占位 | `IN_SCOPE` | 尚未开始，维度符合脚本质量。 | NONE | 后续不得把商业数据作为成功标准。 |
| `docs/06_KNOWLEDGE_SKILLS_ARCHITECTURE_AND_FEEDBACK_LOOP.md` | 知识、评测、反馈架构 | `BOUNDARY_REFERENCE_ONLY` | 已增加 `FEEDBACK_LAYER_NOT_CURRENT_RUNTIME_SCOPE`，明确发布数据只用于后续归因，不是当前运行职责。 | NONE | 保持。 |
| `docs/07_REPOSITORY_OPERATING_MODEL.md` | 仓库运行方式 | `IN_SCOPE` | 无。 | NONE | 保持。 |
| `docs/08_FULL_CONTENT_DECISION_AND_SCRIPT_SYSTEM_ARCHITECTURE.md` | 完整系统长期架构 | `FUTURE_MODULE` | 已在文件顶部增加 `FULL_SYSTEM_REFERENCE / NOT_CURRENT_CUSTOM_GPT_SCOPE`，明确未来模块不得进入当前运行职责。 | NONE | 保持。 |
| `docs/exec-plans/TEMPLATE.md` | 执行计划模板 | `IN_SCOPE` | 无。 | NONE | 保持。 |
| `docs/exec-plans/active/04-first-source-collection-plan.md` | Source Collection 规划 | `IN_SCOPE` | 明确排除开源、竞品批量、自动抓取，服务 P0 脚本知识。 | NONE | 保持。 |
| `docs/exec-plans/completed/01-input-contract-plan.md` | 输入合同历史计划 | `BOUNDARY_REFERENCE_ONLY` | 包含早期复杂 Feishu mapping 任务，但后续决策记录已明确降级并批准扁平输入。 | LOW | 作为历史记录保留，不作为当前输入规则。 |
| `docs/exec-plans/completed/03-knowledge-base-index-plan.md` | 知识索引历史计划 | `IN_SCOPE` | 无。 | NONE | 保持。 |
| `knowledge/README.md` | Knowledge 目录说明 | `IN_SCOPE` | 无。 | NONE | 保持。 |
| `knowledge/AGENTS.md` | Knowledge 写作规则 | `IN_SCOPE` | 无。 | NONE | 保持。 |
| `knowledge/01_GOOD_SCRIPT_STANDARD.md` | 好脚本知识占位 | `IN_SCOPE` | NOT_STARTED，没有越界规则。 | NONE | 后续只写脚本质量规则。 |
| `knowledge/02_CONTENT_FORMATS.md` | 内容形式知识占位 | `IN_SCOPE` | NOT_STARTED，没有产品级内容组合规则。 | NONE | 后续只写单条构想内容形式。 |
| `knowledge/03_HOOK_RULES.md` | Hook 知识占位 | `IN_SCOPE` | NOT_STARTED。 | NONE | 保持。 |
| `knowledge/04_PRODUCT_PROOF.md` | Product Proof 知识占位 | `IN_SCOPE` | NOT_STARTED。 | NONE | 保持。 |
| `knowledge/05_SHOT_PRODUCTION.md` | 分镜拍摄知识占位 | `IN_SCOPE` | NOT_STARTED。 | NONE | 保持。 |
| `knowledge/06_COMPLIANCE_RULES.md` | 合规知识占位 | `IN_SCOPE` | NOT_STARTED。 | NONE | 保持。 |
| `knowledge/07_SCRIPT_OUTPUT_SCHEMA.md` | 输出指导知识占位 | `IN_SCOPE` | NOT_STARTED；职责已由 03 限定为指导，不覆盖 04。 | NONE | 保持。 |
| `.agents/skills/repo-exec-plan-maintenance/SKILL.md` | 仓库维护 Skill | `IN_SCOPE` | 维护流程，不是业务运行能力。 | NONE | 保持。 |
| `.agents/skills/repo-source-digest/SKILL.md` | Source Digest 维护 Skill | `IN_SCOPE` | 明确不抓取、不跳过元数据。 | NONE | 保持。 |
| `.agents/skills/tsd-input-fact-validation/SKILL.md` | 输入事实检查骨架 | `IN_SCOPE` | SCAFFOLD_ONLY；未加入市场或路线判断。 | NONE | 保持。 |
| `.agents/skills/tsd-concept-strategy-design/SKILL.md` | 单条构想策略骨架 | `IN_SCOPE` | “strategy” 限定在构想内部，没有产品路线策略。 | NONE | 保持；后续可强调不是 content route strategy。 |
| `.agents/skills/tsd-shooting-script-generation/SKILL.md` | 脚本生成骨架 | `IN_SCOPE` | 无。 | NONE | 保持。 |
| `.agents/skills/tsd-script-quality-review/SKILL.md` | 脚本质量审核骨架 | `IN_SCOPE` | 无发布批准或商业判断。 | NONE | 保持。 |
| `templates/EVAL_CASE_TEMPLATE.md` | Eval 案例模板 | `IN_SCOPE` | 已给 `Publishing results` 增加 feedback-only 说明，排除市场、达人、账号、路线和预测用途。 | NONE | 保持。 |
| `templates/SCRIPT_INPUT_PACK.yaml` | 输入模板 | `IN_SCOPE` | 符合 01 扁平输入。 | NONE | 保持。 |
| `templates/SCRIPT_OUTPUT_TEMPLATE.md` | 输出模板 | `IN_SCOPE` | 只包含脚本输出块，无市场/达人/路线结论。 | NONE | 保持。 |
| `templates/SOURCE_METADATA.yaml` | Source 元数据模板 | `BOUNDARY_REFERENCE_ONLY` | 包含 `publishing_result` 类型，但作为 Source 类型合理。 | LOW | 保留；后续确保 publishing data 不进入当前运行职责。 |
| `sources/README.md` | Source 目录说明 | `BOUNDARY_REFERENCE_ONLY` | 包含 publishing_results 目录，但只是原始资料层。 | LOW | 保留。 |
| `sources/AGENTS.md` | Source 目录规则 | `IN_SCOPE` | 明确供应商和竞品限制。 | NONE | 保持。 |
| `source_digests/README.md` | Digest 目录说明 | `IN_SCOPE` | 无。 | NONE | 保持。 |
| `source_digests/TEMPLATE.md` | Digest 模板 | `IN_SCOPE` | 无。 | NONE | 保持。 |

---

# 8. 发现的 AMBIGUOUS 项

Cleanup status: scope-lock cleanup completed on 2026-07-17 for A1 through A4.

## A1. `docs/00_MASTER_DESIGN.md` 的早期复杂输入包

问题：

- `docs/00_MASTER_DESIGN.md` Section 8 仍保留较复杂的旧 Script Input Pack 示例。
- 当前批准输入以 `docs/01_INPUT_CONTRACT.md` 的人工扁平输入包为准。

影响：

- Codex 或后续作者若只读 00，可能误以为运行时输入仍需要商品基础信息、用户问题、使用场景、卖点候选等扩展字段。

处理结果：

- 已在旧示例前增加 `RUNTIME_INPUT_SUPERSEDED`。
- 已明确 v0.1 唯一批准运行时输入以 `docs/01_INPUT_CONTRACT.md` 为准。

## A2. `docs/06_KNOWLEDGE_SKILLS_ARCHITECTURE_AND_FEEDBACK_LOOP.md` 的发布数据反馈

问题：

- 文档包含发布数据、商品点击、成交、评论反馈等反馈层内容。
- 文档同时说明低数据不能直接改规则，但该层容易被误读为当前 Custom GPT 要做发布数据归因。

处理结果：

- 已增加 `FEEDBACK_LAYER_NOT_CURRENT_RUNTIME_SCOPE`。
- 已明确发布数据只作为后续人工归因与系统改进资料，不作为当前生成、状态判定或脚本质量评分依据。

## A3. `templates/EVAL_CASE_TEMPLATE.md` 的 `Publishing results`

问题：

- Eval 模板包含发布结果字段。
- 这可用于后续反馈闭环，但不应成为当前 Custom GPT 的成功标准。

处理结果：

- 已在 `Publishing results` 下增加 feedback-only 说明。
- 已排除市场、达人、账号、路线、GMV、销量和投流决策用途。

## A4. `docs/08_FULL_CONTENT_DECISION_AND_SCRIPT_SYSTEM_ARCHITECTURE.md` 与当前文档同处 `docs/`

问题：

- 08 包含大量上游路线、达人、账号、市场和组合规划内容。
- 文档自身已明确 `NOT_CURRENT_CUSTOM_GPT_SCOPE`，但若未来 System Instructions 错误引用该文件，可能造成 scope drift。

处理结果：

- 已在 08 顶部增加 `FULL_SYSTEM_REFERENCE` 和 `NOT_CURRENT_CUSTOM_GPT_SCOPE`。
- 已明确 SD-0、CP-0、市场判断、达人路线、账号策略、内容组合、发布反馈和 `GO / TEST / NO-GO` 不得进入当前运行职责。

---

# 9. 发现的 SCOPE_DRIFT 项

本次未发现已将市场、达人、账号或产品级内容路线加入当前 Custom GPT 运行职责的文件。

未发现以下 drift：

- 当前四个业务 Skills 没有路线决策步骤；
- `docs/01_INPUT_CONTRACT.md` 没有市场数据、达人数据、路线状态或 `GO / TEST / NO-GO` 字段；
- `templates/SCRIPT_INPUT_PACK.yaml` 没有重新引入上游字段；
- `templates/SCRIPT_OUTPUT_TEMPLATE.md` 没有产品市场结论、达人路线、账号策略、发布计划或预测字段；
- `docs/03_KNOWLEDGE_BASE_INDEX.md` 和 Source Collection 计划没有把达人销量、账号矩阵、产品市场机会、内容路线评分、发布策略或投流策略加入第一批业务 Knowledge。

---

# 10. Source / Knowledge 是否跑偏

结论：未跑偏。

当前 Source / Knowledge 规划服务于：

- 好脚本标准；
- 内容形式；
- 主传播命题；
- 卖点组织；
- Hook；
- Product Proof；
- 分镜拍摄；
- 字幕和旁白；
- CTA；
- TikTok Shop US 合规；
- AI 内容限制；
- 输出结构；
- 脚本质量审核。

当前第一批 Source Collection 规划只覆盖：

- `SRC-01` 至 `SRC-04`: 合规、误导 Claim、AI 内容、IP；
- `SRC-05` 至 `SRC-06`: Creative Center 和官方创意指导；
- `SRC-07` 至 `SRC-14`: 泡沫喷壶和车载吸尘器内部 Product Proof / 拍摄限制资料。

明确排除了：

- `SRC-15` 开源资料；
- GitHub 搜索；
- 许可证筛选；
- 竞品批量收集；
- 达人销量分析；
- 达人分层；
- 账号矩阵；
- 产品市场机会；
- 内容路线评分；
- 发布策略；
- 投流策略。

---

# 11. 四个业务 Skills 是否跑偏

结论：未跑偏。

| Skill | 当前状态 | 审计结论 |
|---|---|---|
| `tsd-input-fact-validation` | `SCAFFOLD_ONLY` | 只做 Script Input Pack 事实、缺失、风险和状态检查。 |
| `tsd-concept-strategy-design` | `SCAFFOLD_ONLY` | 只在已验证构想内部做主传播命题、卖点组织、内容形式、Hook 和 proof direction。 |
| `tsd-shooting-script-generation` | `SCAFFOLD_ONLY` | 只生成可拍摄脚本、字幕、旁白、准备清单和 Hook 变体。 |
| `tsd-script-quality-review` | `SCAFFOLD_ONLY` | 只审核脚本事实、主线、卖点、Proof、可拍摄性、节奏和风险。 |

注意：

- `concept_strategy_design` 中的 `strategy` 是单条构想内部策略，不是 `content route strategy`。
- 未来完善 Skill 时，应在 Boundary 中显式排除市场研究、达人路线、账号策略、发布计划和 `GO / TEST / NO-GO`。

---

# 12. System Instructions 当前状态

`docs/02_SYSTEM_INSTRUCTIONS.md` 当前为 `NOT_STARTED`。

现有占位符合范围，列出：

- 角色；
- 输入检查；
- 四个核心 Skill 调用顺序；
- 缺资料处理；
- 输出 Schema；
- 自检与修订；
- 禁止编造。

后续编写时必须增加：

- 当前 Custom GPT 只接收已确定 Script Input Pack；
- 遇到市场研究、达人路线、账号策略、产品级内容组合、发布排期或预测请求时拒绝执行，并要求提供已确定构想；
- 08 只能作为边界参考，不可作为运行规则。

---

# 13. Scope Regression Cases

## Case 1: 正常构想到脚本

输入：

- 用户提供完整 Script Input Pack。

预期：

- 正常执行事实检查；
- 输出 `READY / PROVISIONAL / BLOCKED`；
- 若可写，生成正式 TikTok Shop US 拍摄脚本。

## Case 2: 要求市场研究

用户：

```text
帮我分析这个商品在 TikTok 是否值得做。
```

预期：

- 说明该请求超出 Script Director 职责；
- 不做市场研究；
- 要求用户提供已经确定的视频构想和 Script Input Pack。

## Case 3: 要求达人路线判断

用户：

```text
这个商品应该找达人还是拍产品视频？
```

预期：

- 不做路线决策；
- 说明该问题属于上游内容方向决策；
- 请求用户提供已确定构想。

## Case 4: 只有商品资料，没有构想

输入：

- 用户只给商品参数、图片或商品介绍。

预期：

- 要求补充视频构想；
- 不自动研究市场；
- 不替用户确定产品路线或内容组合。

## Case 5: 构想完整但事实不足

输入：

- 用户提供完整构想，但 `已验证商品事实` 不足或关键 proof 未验证。

预期：

- 输出 `PROVISIONAL` 或 `BLOCKED`；
- 列出缺失事实、待验证内容和风险；
- 不转为市场分析。

## Case 6: 上游构想可能商业上不合理

输入：

- 构想完整，但模型认为商业假设可能弱。

预期：

- 可以提示“该构想的上游商业假设未由本系统验证”；
- 仍按输入事实判断脚本是否可写；
- 不擅自改成达人路线；
- 不否定整个商品。

---

# 14. 修正项与后续注意事项

本次 Scope Lock Cleanup 已完成的最小修正：

1. `docs/00_MASTER_DESIGN.md` 已给旧 Script Input Pack 示例加注：运行时输入以已批准的 `docs/01_INPUT_CONTRACT.md` 为准。
2. `docs/06_KNOWLEDGE_SKILLS_ARCHITECTURE_AND_FEEDBACK_LOOP.md` 已声明反馈闭环不是当前 Custom GPT 运行职责。
3. `docs/08_FULL_CONTENT_DECISION_AND_SCRIPT_SYSTEM_ARCHITECTURE.md` 已在顶部声明其为长期完整系统参考，不是当前 Custom GPT 执行依据。
4. `templates/EVAL_CASE_TEMPLATE.md` 已声明发布结果只作后续反馈归因，不作为当前脚本质量直接成功标准。

后续仍需注意：

1. 编写 `docs/02_SYSTEM_INSTRUCTIONS.md` 时加入越界请求拒绝规则。
2. 编写 `docs/05_EVALUATION_RUBRIC.md` 时继续保持发布结果只作反馈归因，不作为当前脚本质量主评分。
3. 完善四个业务 Skills 时，在 Boundary 中显式排除市场研究、达人策略、账号策略、产品路线、发布计划和预测。

---

# 15. 不应修改的内容

本次审计不建议修改：

- `docs/01_INPUT_CONTRACT.md` 的人工扁平 Script Input Pack；
- `templates/SCRIPT_INPUT_PACK.yaml`；
- 当前四个业务 Skill 骨架；
- `docs/03_KNOWLEDGE_BASE_INDEX.md` 的 P0 Source / Knowledge 范围；
- `docs/08_FULL_CONTENT_DECISION_AND_SCRIPT_SYSTEM_ARCHITECTURE.md` 的未来模块内容，只要其边界声明继续保留；
- 当前 Source Collection 执行计划中对 `SRC-01` 至 `SRC-14` 的范围限制。

---

# 16. 总体结论

总体结论：

```text
当前仓库没有发现 SCOPE_DRIFT。
```

当前 Custom GPT 范围总体收敛良好，核心运行文件、输入合同、知识索引、Skills 骨架和模板都围绕：

```text
已确定单条构想
→ Script Input Pack
→ 事实检查和脚本策略
→ 正式 TikTok Shop US 拍摄脚本
```

主要风险不是当前已经跑偏，而是未来实现时可能误用：

- `docs/08` 的 SD-0 / CP-0 未来模块；
- `docs/06` 的发布反馈闭环；
- `docs/00` 中早期较复杂的输入包草案；
- Eval 模板里的 publishing results 字段。

在后续 `02_SYSTEM_INSTRUCTIONS.md`、`04_SCRIPT_OUTPUT_SCHEMA.md`、`05_EVALUATION_RUBRIC.md` 和业务 Skills 完善时，应显式固化本次审计边界。

---

# 17. Scope Lock Cleanup 记录

2026-07-17 已完成最小范围 Scope Lock Cleanup：

- `docs/00_MASTER_DESIGN.md`: 旧 Script Input Pack 示例前新增 `RUNTIME_INPUT_SUPERSEDED`。
- `docs/06_KNOWLEDGE_SKILLS_ARCHITECTURE_AND_FEEDBACK_LOOP.md`: 反馈闭环前新增 `FEEDBACK_LAYER_NOT_CURRENT_RUNTIME_SCOPE`。
- `docs/08_FULL_CONTENT_DECISION_AND_SCRIPT_SYSTEM_ARCHITECTURE.md`: 顶部新增 `FULL_SYSTEM_REFERENCE` 与 `NOT_CURRENT_CUSTOM_GPT_SCOPE`。
- `templates/EVAL_CASE_TEMPLATE.md`: `Publishing results` 增加 feedback-only 说明。

Cleanup 后结论：

```text
SCOPE_DRIFT: none found
AMBIGUOUS: previously identified high-value ambiguities resolved or explicitly bounded
CURRENT_CUSTOM_GPT_SCOPE: locked to one determined concept -> formal TikTok Shop US shooting script
```
