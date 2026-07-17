# 03_KNOWLEDGE_BASE_INDEX.md

# TikTok Script Director v0.1｜Knowledge Base Index

**文档状态**：APPROVED_FOR_V0_1_VALIDATION  
**设计版本**：0.1  
**当前阶段**：SD-1｜Script Director 系统设计与知识工程  
**上游文档**：`00_MASTER_DESIGN.md`、`01_INPUT_CONTRACT.md`、`06_KNOWLEDGE_SKILLS_ARCHITECTURE_AND_FEEDBACK_LOOP.md`  
**适用系统**：TikTok Script Director v0.1  
**目标市场**：TikTok Shop US  

---

# 1. 文档目的和边界

本文件是 TikTok Script Director v0.1 的知识库索引。

它用于跟踪：

- 系统需要哪些知识主题；
- 每个主题解决什么问题；
- 每个主题需要哪些 Source；
- 当前哪些资料已经存在；
- 当前哪些资料只是计划收集；
- 当前哪些资料缺失；
- Source 如何进入 Source Digest；
- Source Digest 如何进入 Knowledge；
- 哪些 Skills 调用哪些 Knowledge；
- 哪些 Knowledge 是 Custom GPT v0.1 验证前的阻塞项；
- 哪些内容推迟到 v0.2 或更晚。

本文件不是最终知识库，不直接写业务规则，不替代 Source Digest，不补全 Skills。

本轮不执行：

- 抓取网页；
- 下载 GitHub 仓库；
- 下载竞品视频；
- 编写最终 Knowledge；
- 完善业务 Skills；
- 编写 System Instructions；
- 开发 Python、飞书 API、后端或前端。

---

# 2. V0.1 类目范围

v0.1 正式覆盖：

1. 车载无线吸尘器
2. 电动泡沫喷壶

便携冲牙器仅保留：

```text
DEFERRED_CATEGORY_PLACEHOLDER
```

规则：

- 不为便携冲牙器建立第一批 Source。
- 不为便携冲牙器建立第一批 Source Digest。
- 不为便携冲牙器建立第一批 Knowledge。
- 不为便携冲牙器建立第一批 Eval。
- 后续若重新纳入范围，必须先更新本索引和对应执行计划。

---

# 3. 状态枚举

## 3.1 Source 状态

| 状态 | 含义 |
|---|---|
| `AVAILABLE` | 资料已在仓库或已由项目文档确认，可作为当前索引事实使用。 |
| `PLANNED` | 已规划收集或整理，但尚未进入 `sources/`。 |
| `MISSING` | 已确认需要，但尚未明确具体来源或尚未获得资料。 |
| `NOT_RESEARCHED` | 尚未研究候选来源，不得列出具体名称或直接复用。 |
| `STALE` | 资料可能过时，必须重新确认日期、市场或有效性。 |
| `REJECTED` | 已确认不适合使用或不可复用。 |

## 3.2 Digest 状态

| 状态 | 含义 |
|---|---|
| `NOT_STARTED` | 尚未建立 Source Digest。 |
| `DRAFT` | 已有 Digest 草稿，尚未进入验证。 |
| `DRAFT_FOR_VALIDATION` | Digest 草稿等待人工验证。 |
| `APPROVED` | Digest 已批准，可进入 Knowledge。 |

## 3.3 Knowledge 状态

| 状态 | 含义 |
|---|---|
| `NOT_STARTED` | 尚未编写知识文件内容。 |
| `DRAFT` | 已有知识草稿，尚未进入验证。 |
| `DRAFT_FOR_VALIDATION` | 知识草稿等待人工验证。 |
| `APPROVED` | 知识已批准，可被 Skill 正式依赖。 |

文件存在不等于状态完成。只有文档内部状态和人工批准记录可以决定是否完成。

---

# 4. 当前资料状态总览

| 状态类型 | 当前内容 | 使用限制 |
|---|---|---|
| `AVAILABLE` | `00_MASTER_DESIGN.md`、`01_INPUT_CONTRACT.md`、`06_KNOWLEDGE_SKILLS_ARCHITECTURE_AND_FEEDBACK_LOOP.md`、当前 6 个 Skill 骨架 | 只作为系统边界、知识工程路径和 Skill 依赖依据；不能替代业务 Source 或最终 Knowledge。 |
| `PLANNED` | 第一批官方、内部测试、竞品表达和行业资料 Source 槽位 | 尚未进入 `sources/`，不得描述为已收集。 |
| `MISSING` | TikTok Shop US 官方规则原文、误导 Claim 规则、AI 内容规则、IP 规则、真实产品测试文件、经过 Digest 的业务结论 | 当前缺失，必须后续收集、Digest、验证。 |
| `NOT_RESEARCHED` | 开源 Agent / Skill、Evaluation / Rubric、脚本或内容规划结构参考 | 不列具体仓库名；许可证未检查前不得复用。 |

---

# 5. Source 优先级

v0.1 知识建设必须使用以下 Source 优先级：

```text
TikTok / TikTok Shop 官方资料
>
内部真实商品测试和拍摄经验
>
有明确许可证的高相关开源资料
>
可信行业资料
>
竞品视频和竞品评论
>
普通博客和个人经验
```

发生冲突时：

- 平台合规问题以 TikTok / TikTok Shop 官方资料为准。
- 商品能力问题以内部真实商品测试和拍摄经验为准。
- 供应商资料不能自动成为已验证商品事实。
- 竞品能力不能自动成为我方产品能力。

---

# 6. Source 使用限制

- 竞品只能作为表达、结构、节奏、场景、动作、CTA 或用户语言参考。
- 竞品视频和竞品评论不能证明我方产品能力。
- AI 视频不能作为真实 Product Proof。
- 供应商口头说法不得进入内部已验证 Source。
- 供应商资料必须标记为 `supplier_claim`，不得直接进入 `已验证商品事实`。
- 没有明确 LICENSE 的 GitHub 仓库不能直接复用。
- 开源 Agent / Skill 类资料主要服务于仓库维护，不得与 TikTok 业务知识混合。
- 平台政策必须记录获取日期、适用市场和有效性。
- 过期资料必须标记 `STALE`，不得无标记继续使用。

---

# 7. 16 个知识主题清单

## 7.1 Output Schema 文件职责边界

TikTok Script Director v0.1 冻结两套 Output Schema 相关文件的职责：

| 文件 | 职责 | 权威性 |
|---|---|---|
| `docs/04_SCRIPT_OUTPUT_SCHEMA.md` | TikTok Script Director v0.1 的唯一权威输出合同。负责定义必须输出哪些区块、字段名称、字段类型、输出顺序、`READY / PROVISIONAL / BLOCKED` 的呈现、逐镜头表最小字段、Hook 变体数量、审核结果结构。 | 四个运行时 Skills 最终必须遵守该文档。 |
| `knowledge/07_SCRIPT_OUTPUT_SCHEMA.md` | 输出设计知识和使用指导。负责字段设计理由、正确和错误示例、英文字幕和旁白指导、信息密度、人工可读性、常见输出错误。 | 不得覆盖或改变 `docs/04_SCRIPT_OUTPUT_SCHEMA.md`。 |

若二者冲突，以 `docs/04_SCRIPT_OUTPUT_SCHEMA.md` 为准。

---

## 7.2 知识主题明细

说明：

- `current_sources` 中的 `AVAILABLE_PROJECT_DESIGN` 指当前项目设计文档提供的方向性依据，不等于已完成业务 Source。
- `PLANNED_INTERNAL_SOURCE` 表示用户已确认的内部 Source 候选，但文件当前尚未进入 `sources/`。
- 所有 `source_digest_status` 和 `knowledge_status` 当前均不得因为目标文件名存在而标记为完成。

## KBI-01

| 字段 | 内容 |
|---|---|
| `knowledge_topic_id` | `KBI-01` |
| `knowledge_topic_name` | TikTok 好脚本标准 |
| `purpose` | 定义 v0.1 脚本质量底线：真实、可拍、主线清晰、画面证明、TikTok 节奏、合规。 |
| `questions_answered` | 什么是可用脚本；什么是不可用脚本；审核时先看哪些维度。 |
| `required_for_v0_1` | `YES` |
| `priority` | `P0` |
| `target_knowledge_file` | `knowledge/01_GOOD_SCRIPT_STANDARD.md` |
| `related_skills` | `tsd-concept-strategy-design`、`tsd-script-quality-review`、`tsd-input-fact-validation` |
| `preferred_source_types` | 官方创意指导、内部拍摄经验、可信行业资料、竞品表达参考 |
| `current_sources` | `AVAILABLE_PROJECT_DESIGN` |
| `missing_sources` | TikTok 官方创意指导、内部脚本审核样例、真实拍摄复盘 |
| `freshness_requirement` | 官方资料需记录获取日期；内部复盘按项目版本更新。 |
| `market_scope` | TikTok Shop US |
| `category_scope` | 车载无线吸尘器、电动泡沫喷壶 |
| `source_digest_status` | `NOT_STARTED` |
| `knowledge_status` | `NOT_STARTED` |
| `open_questions` | 是否需要先形成 5 到 10 条内部脚本样例后再批准该知识。 |
| `risks` | 把通用短视频建议误写成 TikTok Shop US 转化脚本标准。 |

## KBI-02

| 字段 | 内容 |
|---|---|
| `knowledge_topic_id` | `KBI-02` |
| `knowledge_topic_name` | TikTok 内容形式 |
| `purpose` | 定义痛点对比、测评、演示、场景清洁、多卖点展示等内容形式的适用边界。 |
| `questions_answered` | 当前构想适合什么内容形式；真人 UGC 和非真人展示如何选择。 |
| `required_for_v0_1` | `YES` |
| `priority` | `P1` |
| `target_knowledge_file` | `knowledge/02_CONTENT_FORMATS.md` |
| `related_skills` | `tsd-concept-strategy-design` |
| `preferred_source_types` | TikTok Creative Center、官方创意指导、竞品表达参考、内部拍摄经验 |
| `current_sources` | `AVAILABLE_PROJECT_DESIGN` |
| `missing_sources` | 官方内容形式资料、竞品结构样例、内部形式适配复盘 |
| `freshness_requirement` | 平台创意资料每次引用需记录获取日期；竞品案例按收集批次标记。 |
| `market_scope` | TikTok Shop US |
| `category_scope` | 车载无线吸尘器、电动泡沫喷壶 |
| `source_digest_status` | `NOT_STARTED` |
| `knowledge_status` | `NOT_STARTED` |
| `open_questions` | v0.1 是否限定 3 到 5 种首批内容形式。 |
| `risks` | 过度追求形式多样导致脚本不可拍或证据不足。 |

## KBI-03

| 字段 | 内容 |
|---|---|
| `knowledge_topic_id` | `KBI-03` |
| `knowledge_topic_name` | 主传播命题 |
| `purpose` | 定义一条视频的中心表达，避免只有功能堆叠没有清晰主线。 |
| `questions_answered` | 主传播命题是什么；它如何连接痛点、解决方式和画面证明。 |
| `required_for_v0_1` | `YES` |
| `priority` | `P0` |
| `target_knowledge_file` | `knowledge/01_GOOD_SCRIPT_STANDARD.md` |
| `related_skills` | `tsd-concept-strategy-design`、`tsd-script-quality-review` |
| `preferred_source_types` | 项目设计文档、内部脚本审核经验、官方创意指导 |
| `current_sources` | `AVAILABLE_PROJECT_DESIGN` |
| `missing_sources` | 真实构想到主传播命题的内部案例 |
| `freshness_requirement` | 随内部案例迭代更新。 |
| `market_scope` | TikTok Shop US |
| `category_scope` | 车载无线吸尘器、电动泡沫喷壶 |
| `source_digest_status` | `NOT_STARTED` |
| `knowledge_status` | `NOT_STARTED` |
| `open_questions` | 是否需要为单卖点和多卖点各保留命题模板。 |
| `risks` | 把主传播命题写成空泛口号或商品功能列表。 |

## KBI-04

| 字段 | 内容 |
|---|---|
| `knowledge_topic_id` | `KBI-04` |
| `knowledge_topic_name` | 核心卖点与辅助卖点组织 |
| `purpose` | 定义多卖点可用但必须有主次，避免短视频信息过载。 |
| `questions_answered` | 核心卖点如何确定；辅助卖点如何服务主线；一条视频能承载多少信息。 |
| `required_for_v0_1` | `YES` |
| `priority` | `P0` |
| `target_knowledge_file` | `knowledge/01_GOOD_SCRIPT_STANDARD.md` |
| `related_skills` | `tsd-concept-strategy-design`、`tsd-shooting-script-generation`、`tsd-script-quality-review` |
| `preferred_source_types` | 项目设计文档、内部脚本复盘、可信行业资料 |
| `current_sources` | `AVAILABLE_PROJECT_DESIGN` |
| `missing_sources` | 多卖点脚本成功和失败样例 |
| `freshness_requirement` | 随真实脚本评测更新。 |
| `market_scope` | TikTok Shop US |
| `category_scope` | 车载无线吸尘器、电动泡沫喷壶 |
| `source_digest_status` | `NOT_STARTED` |
| `knowledge_status` | `NOT_STARTED` |
| `open_questions` | v0.1 是否明确限制 0 到 2 个辅助卖点。 |
| `risks` | 把多个互不相关卖点塞进同一短视频。 |

## KBI-05

| 字段 | 内容 |
|---|---|
| `knowledge_topic_id` | `KBI-05` |
| `knowledge_topic_name` | Hook 与前三秒 |
| `purpose` | 定义视频开头如何快速建立观看理由，并和后续 Product Proof 对齐。 |
| `questions_answered` | 什么样的 Hook 可用；前三秒应该呈现问题、结果、反差还是动作。 |
| `required_for_v0_1` | `YES` |
| `priority` | `P0` |
| `target_knowledge_file` | `knowledge/03_HOOK_RULES.md` |
| `related_skills` | `tsd-concept-strategy-design`、`tsd-shooting-script-generation`、`tsd-script-quality-review` |
| `preferred_source_types` | TikTok 官方创意指导、TikTok Creative Center、可信行业资料、竞品表达参考 |
| `current_sources` | `AVAILABLE_PROJECT_DESIGN` |
| `missing_sources` | 官方 Hook 指导、行业 Hook 资料、竞品开场样例 Digest |
| `freshness_requirement` | 官方资料记录获取日期；竞品样例按批次更新。 |
| `market_scope` | TikTok Shop US |
| `category_scope` | 车载无线吸尘器、电动泡沫喷壶 |
| `source_digest_status` | `NOT_STARTED` |
| `knowledge_status` | `NOT_STARTED` |
| `open_questions` | Hook 类型是否在 03 知识中统一枚举，还是留给 Skill 派生。 |
| `risks` | 为吸引注意而引入夸张、误导或无法证明的开场。 |

## KBI-06

| 字段 | 内容 |
|---|---|
| `knowledge_topic_id` | `KBI-06` |
| `knowledge_topic_name` | Product Proof / 画面证明 |
| `purpose` | 定义什么画面可以证明产品能力，什么只能作为表达或待验证。 |
| `questions_answered` | Product Proof 是否成立；哪些镜头必须真实拍；AI 或竞品视频能否作为证明。 |
| `required_for_v0_1` | `YES` |
| `priority` | `P0` |
| `target_knowledge_file` | `knowledge/04_PRODUCT_PROOF.md` |
| `related_skills` | `tsd-input-fact-validation`、`tsd-concept-strategy-design`、`tsd-shooting-script-generation`、`tsd-script-quality-review` |
| `preferred_source_types` | 内部真实商品测试、拍摄经验、官方误导内容规则、竞品表达参考 |
| `current_sources` | `AVAILABLE_PROJECT_DESIGN`; no internal Source currently in `sources/` |
| `missing_sources` | `PLANNED_INTERNAL_SOURCE`: 实际喷射测试、泡沫状态测试、车内清洁测试、失败记录、Product Proof Digest |
| `freshness_requirement` | 每次商品批次或拍摄条件变化后需要复核。 |
| `market_scope` | TikTok Shop US |
| `category_scope` | 车载无线吸尘器、电动泡沫喷壶 |
| `source_digest_status` | `NOT_STARTED` |
| `knowledge_status` | `NOT_STARTED` |
| `open_questions` | 哪些内部测试文件先进入第一批 Source。 |
| `risks` | 把供应商说法、竞品能力或 AI 效果当作真实 Product Proof。 |

## KBI-07

| 字段 | 内容 |
|---|---|
| `knowledge_topic_id` | `KBI-07` |
| `knowledge_topic_name` | 分镜与拍摄执行 |
| `purpose` | 定义如何把策略和 Proof 转成可拍镜头、动作、景别、连续拍摄和准备清单。 |
| `questions_answered` | 每个镜头拍什么；哪些镜头必须连续；哪些道具和场景必须提前准备。 |
| `required_for_v0_1` | `YES` |
| `priority` | `P1` |
| `target_knowledge_file` | `knowledge/05_SHOT_PRODUCTION.md` |
| `related_skills` | `tsd-shooting-script-generation`、`tsd-script-quality-review` |
| `preferred_source_types` | 内部拍摄经验、拍摄限制和失败记录、可信行业资料 |
| `current_sources` | `AVAILABLE_PROJECT_DESIGN`; no internal Source currently in `sources/` |
| `missing_sources` | `PLANNED_INTERNAL_SOURCE`: 泡沫喷壶拍摄限制、吸尘器拍摄限制、失败镜头复盘 |
| `freshness_requirement` | 随设备、场景和拍摄能力变化更新。 |
| `market_scope` | TikTok Shop US |
| `category_scope` | 车载无线吸尘器、电动泡沫喷壶 |
| `source_digest_status` | `NOT_STARTED` |
| `knowledge_status` | `NOT_STARTED` |
| `open_questions` | 是否建立固定镜头字段和连续拍摄标记。 |
| `risks` | 生成看似专业但实际无法拍摄的镜头。 |

## KBI-08

| 字段 | 内容 |
|---|---|
| `knowledge_topic_id` | `KBI-08` |
| `knowledge_topic_name` | 真人 UGC 与非真人展示 |
| `purpose` | 定义真人出镜、手部操作、纯产品演示、场景清洁展示的使用条件。 |
| `questions_answered` | 当前构想是否需要真人；非真人展示如何保持可信和有节奏。 |
| `required_for_v0_1` | `YES` |
| `priority` | `P1` |
| `target_knowledge_file` | `knowledge/02_CONTENT_FORMATS.md` |
| `related_skills` | `tsd-concept-strategy-design`、`tsd-shooting-script-generation`、`tsd-script-quality-review` |
| `preferred_source_types` | TikTok 官方创意指导、内部拍摄条件、竞品表达参考 |
| `current_sources` | `AVAILABLE_PROJECT_DESIGN` |
| `missing_sources` | 真人和非真人脚本样例、内部拍摄条件限制 |
| `freshness_requirement` | 随团队拍摄条件更新。 |
| `market_scope` | TikTok Shop US |
| `category_scope` | 车载无线吸尘器、电动泡沫喷壶 |
| `source_digest_status` | `NOT_STARTED` |
| `knowledge_status` | `NOT_STARTED` |
| `open_questions` | v0.1 是否默认支持手部操作优先于真人出镜。 |
| `risks` | 缺真人后误以为视频不可做，或强行真人出镜增加成本。 |

## KBI-09

| 字段 | 内容 |
|---|---|
| `knowledge_topic_id` | `KBI-09` |
| `knowledge_topic_name` | 英文字幕和旁白 |
| `purpose` | 定义英文字幕、旁白备注和中文审核含义的基本边界。 |
| `questions_answered` | 字幕要多短；旁白是否必须；中文审核含义如何辅助人工审核。 |
| `required_for_v0_1` | `YES` |
| `priority` | `P1` |
| `target_knowledge_file` | `knowledge/07_SCRIPT_OUTPUT_SCHEMA.md` |
| `related_skills` | `tsd-shooting-script-generation`、`tsd-script-quality-review` |
| `preferred_source_types` | 官方创意指导、内部审核经验、可信行业资料 |
| `current_sources` | `AVAILABLE_PROJECT_DESIGN` |
| `missing_sources` | 英文表达样例、字幕长度和节奏规则 Digest |
| `freshness_requirement` | 随输出 Schema 和审核反馈更新。 |
| `market_scope` | TikTok Shop US |
| `category_scope` | 车载无线吸尘器、电动泡沫喷壶 |
| `source_digest_status` | `NOT_STARTED` |
| `knowledge_status` | `NOT_STARTED` |
| `open_questions` | 是否先规定字幕最大长度和旁白可选策略。 |
| `risks` | 英文表达夸大产品能力或超出画面证明。 |

## KBI-10

| 字段 | 内容 |
|---|---|
| `knowledge_topic_id` | `KBI-10` |
| `knowledge_topic_name` | CTA |
| `purpose` | 定义 TikTok Shop US 转化视频的结尾行动引导边界。 |
| `questions_answered` | 什么时候要 CTA；CTA 如何不压过 Proof；哪些 CTA 可能夸张或误导。 |
| `required_for_v0_1` | `YES` |
| `priority` | `P1` |
| `target_knowledge_file` | `knowledge/01_GOOD_SCRIPT_STANDARD.md` |
| `related_skills` | `tsd-shooting-script-generation`、`tsd-script-quality-review` |
| `preferred_source_types` | TikTok Shop 官方资料、官方创意指导、竞品表达参考 |
| `current_sources` | `AVAILABLE_PROJECT_DESIGN` |
| `missing_sources` | TikTok Shop CTA 合规和表达资料、竞品 CTA Digest |
| `freshness_requirement` | 官方资料记录获取日期。 |
| `market_scope` | TikTok Shop US |
| `category_scope` | 车载无线吸尘器、电动泡沫喷壶 |
| `source_digest_status` | `NOT_STARTED` |
| `knowledge_status` | `NOT_STARTED` |
| `open_questions` | 是否限定首版 CTA 模板数量。 |
| `risks` | CTA 引入未经验证促销、承诺或绝对化表达。 |

## KBI-11

| 字段 | 内容 |
|---|---|
| `knowledge_topic_id` | `KBI-11` |
| `knowledge_topic_name` | TikTok Shop US 内容合规 |
| `purpose` | 定义平台和市场合规边界，特别是商品 Claim、误导内容、IP 和风险表达。 |
| `questions_answered` | 哪些内容不能写；哪些 Claim 需要证据；合规风险如何阻断脚本。 |
| `required_for_v0_1` | `YES` |
| `priority` | `P0` |
| `target_knowledge_file` | `knowledge/06_COMPLIANCE_RULES.md` |
| `related_skills` | `tsd-input-fact-validation`、`tsd-script-quality-review` |
| `preferred_source_types` | TikTok Shop US 官方政策、TikTok 官方政策、平台合规资料 |
| `current_sources` | `AVAILABLE_PROJECT_DESIGN` |
| `missing_sources` | TikTok Shop US 内容规则、误导内容规则、IP 规则、政策 Digest |
| `freshness_requirement` | 必须记录获取日期、适用市场和有效性；政策变化时复核。 |
| `market_scope` | TikTok Shop US |
| `category_scope` | 车载无线吸尘器、电动泡沫喷壶 |
| `source_digest_status` | `NOT_STARTED` |
| `knowledge_status` | `NOT_STARTED` |
| `open_questions` | 哪些官方政策页作为首批 P0 Source。 |
| `risks` | 合规知识未完成前宣布 Custom GPT 具备正式业务使用条件。 |

## KBI-12

| 字段 | 内容 |
|---|---|
| `knowledge_topic_id` | `KBI-12` |
| `knowledge_topic_name` | AI 内容和 AI 竞品参考限制 |
| `purpose` | 定义 AI 视频、AI 效果和 AI 竞品参考的使用边界。 |
| `questions_answered` | AI 视频能否当 Product Proof；AI 竞品视频哪些部分可以参考。 |
| `required_for_v0_1` | `YES` |
| `priority` | `P0` |
| `target_knowledge_file` | `knowledge/06_COMPLIANCE_RULES.md` |
| `related_skills` | `tsd-input-fact-validation`、`tsd-concept-strategy-design`、`tsd-shooting-script-generation`、`tsd-script-quality-review` |
| `preferred_source_types` | TikTok 官方 AI 内容规则、项目设计文档、竞品表达案例 |
| `current_sources` | `AVAILABLE_PROJECT_DESIGN` |
| `missing_sources` | TikTok AI 内容政策、AI reference misuse Digest |
| `freshness_requirement` | 官方 AI 政策需记录获取日期并定期复核。 |
| `market_scope` | TikTok Shop US |
| `category_scope` | 车载无线吸尘器、电动泡沫喷壶 |
| `source_digest_status` | `NOT_STARTED` |
| `knowledge_status` | `NOT_STARTED` |
| `open_questions` | 是否建立 AI 参考视频标注字段或审核标签。 |
| `risks` | 把 AI 清洁、吸除、泡沫覆盖效果当作真实商品表现。 |

## KBI-13

| 字段 | 内容 |
|---|---|
| `knowledge_topic_id` | `KBI-13` |
| `knowledge_topic_name` | 脚本输出结构 |
| `purpose` | 定义正式输出合同与输出指导知识的职责边界，确保四个运行时 Skills 遵守同一输出结构。 |
| `questions_answered` | 权威输出合同在哪里；输出是否包含状态、策略、逐镜头、字幕、准备清单、Hook 变体和审核结果；输出知识文件能否改变合同。 |
| `required_for_v0_1` | `YES` |
| `priority` | `P0 for minimum contract`; `P1 for guidance knowledge` |
| `target_knowledge_file` | `docs/04_SCRIPT_OUTPUT_SCHEMA.md` as authoritative output contract |
| `related_guidance_knowledge_file` | `knowledge/07_SCRIPT_OUTPUT_SCHEMA.md` |
| `related_skills` | `tsd-input-fact-validation`、`tsd-concept-strategy-design`、`tsd-shooting-script-generation`、`tsd-script-quality-review` |
| `preferred_source_types` | 项目设计文档、内部审核经验、开源脚本结构参考 |
| `current_sources` | `AVAILABLE_PROJECT_DESIGN` |
| `missing_sources` | 输出结构样例、脚本字段评审、可复用开源资料 license review; open-source slots are `NOT_RESEARCHED` |
| `freshness_requirement` | 随评测和人工审核反馈更新。 |
| `market_scope` | TikTok Shop US |
| `category_scope` | 车载无线吸尘器、电动泡沫喷壶 |
| `source_digest_status` | `NOT_STARTED` |
| `knowledge_status` | `NOT_STARTED`; `docs/04_SCRIPT_OUTPUT_SCHEMA.md` contract status is also `NOT_STARTED` |
| `open_questions` | `docs/04_SCRIPT_OUTPUT_SCHEMA.md` 最小合同应包含哪些字段和输出顺序。 |
| `risks` | 输出结构过重，增加人工阅读成本；或让 `knowledge/07_SCRIPT_OUTPUT_SCHEMA.md` 反向覆盖权威输出合同。 |

## KBI-14

| 字段 | 内容 |
|---|---|
| `knowledge_topic_id` | `KBI-14` |
| `knowledge_topic_name` | 脚本质量评测 |
| `purpose` | 定义脚本审核维度和失败条件，为后续 Eval 和人工审核提供依据。 |
| `questions_answered` | 怎样判定脚本通过、暂定或阻塞；哪些问题应反馈到知识、Skill 或输入合同。 |
| `required_for_v0_1` | `YES` |
| `priority` | `P1` |
| `target_knowledge_file` | `knowledge/01_GOOD_SCRIPT_STANDARD.md`; `knowledge/06_COMPLIANCE_RULES.md` |
| `related_skills` | `tsd-script-quality-review` |
| `preferred_source_types` | 内部审核记录、Evaluation / Rubric 开源参考、项目设计文档 |
| `current_sources` | `AVAILABLE_PROJECT_DESIGN` |
| `missing_sources` | 真实失败脚本样例、审核记录、开源 rubric license review; open-source rubric slot is `NOT_RESEARCHED` |
| `freshness_requirement` | 随评测案例和人工反馈更新。 |
| `market_scope` | TikTok Shop US |
| `category_scope` | 车载无线吸尘器、电动泡沫喷壶 |
| `source_digest_status` | `NOT_STARTED` |
| `knowledge_status` | `NOT_STARTED` |
| `open_questions` | 是否在 05 评测文档之前先冻结最小审核维度。 |
| `risks` | 把评测写成语言审美，而忽略事实、Proof 和合规。 |

## KBI-15

| 字段 | 内容 |
|---|---|
| `knowledge_topic_id` | `KBI-15` |
| `knowledge_topic_name` | 单卖点和多卖点视频 |
| `purpose` | 定义单卖点和多卖点视频的输入、策略和脚本组织差异。 |
| `questions_answered` | 什么时候使用单卖点；多卖点如何保持主线；辅助卖点何时应拆成后续视频。 |
| `required_for_v0_1` | `YES` |
| `priority` | `P0` |
| `target_knowledge_file` | `knowledge/01_GOOD_SCRIPT_STANDARD.md` |
| `related_skills` | `tsd-concept-strategy-design`、`tsd-shooting-script-generation`、`tsd-script-quality-review` |
| `preferred_source_types` | 项目设计文档、内部脚本样例、可信行业资料 |
| `current_sources` | `AVAILABLE_PROJECT_DESIGN` |
| `missing_sources` | 单卖点和多卖点真实案例、失败样例 Digest |
| `freshness_requirement` | 随 5 到 10 条真实构想验证更新。 |
| `market_scope` | TikTok Shop US |
| `category_scope` | 车载无线吸尘器、电动泡沫喷壶 |
| `source_digest_status` | `NOT_STARTED` |
| `knowledge_status` | `NOT_STARTED` |
| `open_questions` | 是否把多卖点视频的最大承载时长写入输出 Schema。 |
| `risks` | 把单卖点原则误解为禁止所有辅助卖点。 |

## KBI-16

| 字段 | 内容 |
|---|---|
| `knowledge_topic_id` | `KBI-16` |
| `knowledge_topic_name` | 不同商品类目的差异规则 |
| `purpose` | 定义车载无线吸尘器和电动泡沫喷壶在 Proof、风险和拍摄上的类目差异。 |
| `questions_answered` | 吸尘器哪些 Claim 风险高；泡沫喷壶哪些表达不能写；哪些类目只保留 deferred。 |
| `required_for_v0_1` | `PARTIAL` |
| `priority` | `P2` |
| `target_knowledge_file` | Category sections inside `knowledge/04_PRODUCT_PROOF.md`、`knowledge/05_SHOT_PRODUCTION.md`、`knowledge/06_COMPLIANCE_RULES.md` |
| `related_skills` | `tsd-input-fact-validation`、`tsd-shooting-script-generation`、`tsd-script-quality-review` |
| `preferred_source_types` | 内部商品测试、拍摄失败记录、官方合规资料 |
| `current_sources` | `AVAILABLE_PROJECT_DESIGN`; no internal Source currently in `sources/` |
| `missing_sources` | `PLANNED_INTERNAL_SOURCE`: 泡沫喷壶和吸尘器测试记录、拍摄限制和失败记录 |
| `freshness_requirement` | 每个商品批次、配件或测试条件变化后复核。 |
| `market_scope` | TikTok Shop US |
| `category_scope` | 车载无线吸尘器、电动泡沫喷壶；便携冲牙器为 `DEFERRED_CATEGORY_PLACEHOLDER` |
| `source_digest_status` | `NOT_STARTED` |
| `knowledge_status` | `NOT_STARTED` |
| `open_questions` | 类目规则应写入各知识文件，还是后续建立独立类目知识文件。 |
| `risks` | 把便携冲牙器提前纳入 v0.1，或把供应商/竞品能力写成我方类目规则。 |

---

# 8. 第一批 Source Inventory 槽位

本表只规划第一批 Source Inventory，不代表已收集。

| source_slot_id | source_name_or_scope | source_type | status | marker / license | target_topics | purpose | notes |
|---|---|---|---|---|---|---|---|
| `SRC-01` | TikTok Shop US 内容规则 | official / policy_and_compliance | `PLANNED` | capture date required | KBI-11 | 建立市场合规边界 | 后续必须记录适用市场。 |
| `SRC-02` | TikTok / TikTok Shop 误导内容与无依据 Claim 规则 | official / policy_and_compliance | `PLANNED` | capture date required | KBI-06, KBI-11 | 防止夸张、绝对化、不可证明 Claim | P0。 |
| `SRC-03` | TikTok 官方 AI 内容规则 | official / policy_and_compliance | `PLANNED` | capture date required | KBI-12 | 定义 AI 内容和 AI 参考限制 | P0。 |
| `SRC-04` | TikTok / TikTok Shop 知识产权规则 | official / policy_and_compliance | `PLANNED` | capture date required | KBI-11 | 避免复制竞品品牌资产和 IP 风险 | P0。 |
| `SRC-05` | TikTok Creative Center 官方资料 | official | `PLANNED` | capture date required | KBI-02, KBI-05 | 支持内容形式、Hook 和节奏参考 | 不直接变成业务规则。 |
| `SRC-06` | TikTok 官方创意指导 | official | `PLANNED` | capture date required | KBI-01, KBI-02, KBI-05, KBI-10 | 支持好脚本、Hook、CTA 等基础规则 | 可与合规和 Proof 并行收集。 |
| `SRC-07` | 泡沫喷壶 02 输入证据库中的已确认商品事实 | internal / product_tests | `PLANNED` | `PLANNED_INTERNAL_SOURCE` | KBI-06, KBI-16 | 支撑泡沫喷壶 Product Proof | 当前不得描述为已进入 `sources/`。 |
| `SRC-08` | 泡沫喷壶实际喷射测试记录 | internal / product_tests | `PLANNED` | `PLANNED_INTERNAL_SOURCE` | KBI-06, KBI-07, KBI-16 | 验证电动喷射和可拍性 | 供应商口头说法不得替代。 |
| `SRC-09` | 泡沫喷壶泡沫状态测试记录 | internal / product_tests | `PLANNED` | `PLANNED_INTERNAL_SOURCE` | KBI-06, KBI-16 | 验证泡沫连续性、稳定性和表达限制 | AI 泡沫效果不得替代。 |
| `SRC-10` | 泡沫喷壶拍摄限制和失败记录 | internal / product_tests | `PLANNED` | `PLANNED_INTERNAL_SOURCE` | KBI-07, KBI-16 | 约束镜头、道具、场景和失败条件 | 用于 Shot Production。 |
| `SRC-11` | 车载无线吸尘器 02 输入证据库中的已确认商品事实 | internal / product_tests | `PLANNED` | `PLANNED_INTERNAL_SOURCE` | KBI-06, KBI-16 | 支撑吸尘器 Product Proof | 当前不得描述为已进入 `sources/`。 |
| `SRC-12` | 车载无线吸尘器配件和功能测试记录 | internal / product_tests | `PLANNED` | `PLANNED_INTERNAL_SOURCE` | KBI-06, KBI-16 | 验证配件、功能和表达边界 | 竞品能力不得替代。 |
| `SRC-13` | 座椅缝、杯架、脚垫等真实清洁测试 | internal / product_tests | `PLANNED` | `PLANNED_INTERNAL_SOURCE` | KBI-06, KBI-07, KBI-16 | 验证真实车内清洁 Proof | 避免跳剪冒充效果。 |
| `SRC-14` | 车载无线吸尘器拍摄限制和失败记录 | internal / product_tests | `PLANNED` | `PLANNED_INTERNAL_SOURCE` | KBI-07, KBI-16 | 约束镜头、道具、场景和失败条件 | 用于 Shot Production。 |
| `SRC-15` | 开源 Agent / Skill、Evaluation / Rubric、脚本或内容规划结构参考槽位 | imported_skills / open_source | `NOT_RESEARCHED` | `license_status: NOT_CHECKED`; `reuse_status: BLOCKED_UNTIL_REVIEW` | KBI-13, KBI-14 | 只服务仓库维护、评测或输出结构参考 | 本轮不得列具体仓库名称。 |

---

# 9. Source -> Digest -> Knowledge -> Skill 关系

```text
Source 原始资料
↓
Source Digest 结构化消化
↓
Domain Knowledge 自有知识库
↓
Skills 执行流程
```

## 9.1 Source 进入 Digest 的条件

Source 必须先满足：

- 有来源、路径或 URL；
- 有获取日期；
- 有市场；
- 有类目；
- 有可信度判断；
- 有有效性状态；
- 有使用限制；
- 平台政策有适用市场；
- 开源资料有 LICENSE 检查结果；
- 内部测试有测试条件、拍摄条件或记录来源。

## 9.2 Digest 进入 Knowledge 的条件

Source Digest 必须记录：

- 原始观点；
- 可执行结论；
- 适用条件；
- 不适用或例外；
- 常见误用；
- 风险与冲突；
- 对当前系统的影响；
- 建议进入的知识文件；
- 建议关联的 Skills；
- 待验证问题。

未经 Digest 的 Source 不得直接写入 Knowledge。

## 9.3 Knowledge 进入 Skill 的条件

Knowledge 必须：

- 追溯到 Source Digest；
- 区分官方事实、内部经验、供应商说法、竞品参考和项目推断；
- 标明适用场景和例外；
- 标明风险和常见误用；
- 达到 `APPROVED` 后才可作为正式 Skill 依赖。

---

# 10. Knowledge 与四个运行时 Skills 映射

当前四个业务 Skills 均为：

```text
SCAFFOLD_ONLY
```

这表示：

- Skill 文件存在；
- 输入、输出、边界和失败条件已有骨架；
- 业务规则尚未实现；
- Knowledge 尚未完成；
- 文件存在不代表业务能力已实现。

统一输出依赖规则：

- 四个运行时 Skills 的正式输出约束依赖 `docs/04_SCRIPT_OUTPUT_SCHEMA.md`。
- 输出解释、示例、英文字幕、旁白和人工可读性指导依赖 `knowledge/07_SCRIPT_OUTPUT_SCHEMA.md`。
- `knowledge/07_SCRIPT_OUTPUT_SCHEMA.md` 不得覆盖或改变 `docs/04_SCRIPT_OUTPUT_SCHEMA.md`。

## 10.1 `tsd-input-fact-validation`

依赖 Knowledge：

- `knowledge/01_GOOD_SCRIPT_STANDARD.md`
- `knowledge/04_PRODUCT_PROOF.md`
- `knowledge/06_COMPLIANCE_RULES.md`
- `knowledge/07_SCRIPT_OUTPUT_SCHEMA.md`

正式输出约束：

- `docs/04_SCRIPT_OUTPUT_SCHEMA.md`

用途：

- 检查 Script Input Pack 是否足以支持脚本；
- 区分可用事实、不可用信息、待验证项和风险项；
- 输出 `READY / PROVISIONAL / BLOCKED`。

当前限制：

- 不能把竞品能力当作商品事实；
- 不能把待验证内容升级为已确认事实；
- 不能把 AI 视频效果当作 Product Proof。

## 10.2 `tsd-concept-strategy-design`

依赖 Knowledge：

- `knowledge/01_GOOD_SCRIPT_STANDARD.md`
- `knowledge/02_CONTENT_FORMATS.md`
- `knowledge/03_HOOK_RULES.md`
- `knowledge/04_PRODUCT_PROOF.md`

正式输出约束：

- `docs/04_SCRIPT_OUTPUT_SCHEMA.md`

用途：

- 派生主传播命题；
- 区分核心卖点和辅助卖点；
- 选择内容形式、Hook 方向和画面证明方向。

当前限制：

- 不改变用户核心意图；
- 不添加无依据 Claim；
- 不把多个无关卖点拼成同一条短视频。

## 10.3 `tsd-shooting-script-generation`

依赖 Knowledge：

- `knowledge/03_HOOK_RULES.md`
- `knowledge/04_PRODUCT_PROOF.md`
- `knowledge/05_SHOT_PRODUCTION.md`
- `knowledge/07_SCRIPT_OUTPUT_SCHEMA.md`

正式输出约束：

- `docs/04_SCRIPT_OUTPUT_SCHEMA.md`

用途：

- 生成逐镜头拍摄脚本；
- 生成英文字幕、旁白备注、拍摄准备清单和 Hook 变体；
- 保持画面证明与输出结构一致。

当前限制：

- 不创建 AI 视频素材；
- 不发明未验证产品效果；
- 不替代人工审核。

## 10.4 `tsd-script-quality-review`

依赖 Knowledge：

- `knowledge/01_GOOD_SCRIPT_STANDARD.md`
- `knowledge/03_HOOK_RULES.md`
- `knowledge/04_PRODUCT_PROOF.md`
- `knowledge/05_SHOT_PRODUCTION.md`
- `knowledge/06_COMPLIANCE_RULES.md`
- `knowledge/07_SCRIPT_OUTPUT_SCHEMA.md`

正式输出约束：

- `docs/04_SCRIPT_OUTPUT_SCHEMA.md`

用途：

- 审核事实准确性、主线清晰度、卖点组织、Hook、画面证明、可拍摄性、节奏和风险。

当前限制：

- 不批准发布；
- 不覆盖人工审核；
- 不把失败的 Proof 改写成通过脚本。

---

# 11. V0.1 Blocking Knowledge

以下知识在形成可验证 Knowledge 前，会阻止 Custom GPT v0.1 被宣布为正式业务使用条件：

- TikTok Shop US 合规边界；
- 误导内容和无依据 Claim 限制；
- AI 内容和 AI 竞品参考限制；
- Product Proof / 画面证明规则；
- 主传播命题规则；
- 核心卖点与辅助卖点组织规则；
- Hook 与前三秒规则；
- 脚本输出结构最小合同。

说明：

- 合规、Hook 和 Product Proof 的 Source 后续允许并行收集。
- 但在合规和 Product Proof 未形成可验证知识前，不得宣布 Custom GPT v0.1 已具备正式业务使用条件。
- 在 `docs/04_SCRIPT_OUTPUT_SCHEMA.md` 达到 `DRAFT_FOR_VALIDATION` 前，不得开始正式 Custom GPT 回归验证。
- `knowledge/07_SCRIPT_OUTPUT_SCHEMA.md` 的完整语言优化可以稍后完善，但最小输出合同是 v0.1 阻塞项。

---

# 12. V0.1 Useful but Non-blocking Knowledge

以下知识对 v0.1 有用，但不应单独阻塞首批验证：

- TikTok 内容形式细分；
- 真人 UGC 与非真人展示细分；
- 英文字幕和旁白优化；
- CTA 表达优化；
- 分镜和拍摄执行的扩展模板；
- 脚本质量评测的细分评分；
- 车载无线吸尘器和电动泡沫喷壶以外的类目泛化。

---

# 13. V0.2 Deferred Knowledge

以下内容推迟到 v0.2 或更晚：

- 飞书原始字段级映射；
- 飞书关联记录自动展开；
- 自动生成 Script Input Pack；
- 自动 Source ingestion；
- 自动 Source freshness monitoring；
- 自动下载或同步 GitHub / TikTok / 竞品资料；
- 大规模竞品库；
- 发布结果和数据反馈驱动的优化规则；
- 多 Agent 编排；
- 后端、数据库和飞书 API；
- 便携冲牙器类目 Source、Digest、Knowledge 和 Eval。

---

# 14. 第一批 Knowledge 推荐编写顺序

1. `knowledge/01_GOOD_SCRIPT_STANDARD.md`
2. `knowledge/03_HOOK_RULES.md`
3. `knowledge/04_PRODUCT_PROOF.md`
4. `knowledge/06_COMPLIANCE_RULES.md`
5. `knowledge/02_CONTENT_FORMATS.md`
6. `knowledge/05_SHOT_PRODUCTION.md`
7. `knowledge/07_SCRIPT_OUTPUT_SCHEMA.md`

理由：

- `01_GOOD_SCRIPT_STANDARD.md` 提供整体质量标准、主传播命题、卖点组织和 CTA 基线。
- `03_HOOK_RULES.md` 直接影响策略设计、脚本生成和质量审核。
- `04_PRODUCT_PROOF.md` 是防止编造商品能力的关键边界。
- `06_COMPLIANCE_RULES.md` 是 TikTok Shop US、误导 Claim、AI 内容和 IP 风险的 P0 边界。
- `02_CONTENT_FORMATS.md` 应在质量、Hook 和 Proof 边界清楚后再细化。
- `05_SHOT_PRODUCTION.md` 应在 Product Proof 规则明确后转化为拍摄执行规则。
- `07_SCRIPT_OUTPUT_SCHEMA.md` 应在上述知识边界形成后承接为稳定输出结构。

---

# 15. 后续 Source Collection 的进入条件

开始收集第一批 Source 前，必须满足：

- 本文件通过人工审核；
- 第一批 Source Inventory 槽位获得确认；
- 每个 Source 有明确目标主题和目标 Knowledge；
- 内部 Source 文件或记录由人工提供或确认位置；
- 官方政策资料只按明确清单收集，不做无目标抓取；
- 开源资料先做许可证检查，未检查前保持 `reuse_status: BLOCKED_UNTIL_REVIEW`；
- 竞品资料只按表达参考收集，不进入商品能力证明；
- 收集后必须先进入 `sources/` 并配套元数据；
- 进入 Knowledge 前必须先形成 Source Digest。

---

# 16. 版本记录

| 版本 | 日期 | 状态 | 说明 |
|---|---|---|---|
| 0.1 | 2026-07-17 | DRAFT_FOR_VALIDATION | 首稿，建立 v0.1 知识主题、Source Inventory、状态枚举、Skill 映射和后续收集条件。 |
| 0.2 | 2026-07-17 | APPROVED_FOR_V0_1_VALIDATION | 冻结 `docs/04_SCRIPT_OUTPUT_SCHEMA.md` 与 `knowledge/07_SCRIPT_OUTPUT_SCHEMA.md` 的职责边界；批准 03 索引用于 v0.1 验证。 |
