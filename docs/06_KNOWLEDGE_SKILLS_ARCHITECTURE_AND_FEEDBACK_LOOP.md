# 06_KNOWLEDGE_SKILLS_ARCHITECTURE_AND_FEEDBACK_LOOP.md

# TikTok Script Director｜知识库、Skills 与反馈优化架构

**文档状态**：DRAFT_FOR_VALIDATION  
**设计版本**：0.1  
**所属阶段**：SD-1｜Script Director 系统设计  
**上游文档**：`00_MASTER_DESIGN.md`  
**适用系统**：TikTok Script Director v0.1  
**目标市场**：TikTok Shop US

---

# 1. 文档目的

本文件用于冻结 TikTok Script Director 的知识生产、技能设计、评测和持续优化路线。

它回答以下问题：

- 原始 Source 资源如何整理；
- 如何把 Source 转换成可执行知识；
- 自有知识库应该如何编写；
- Skills 应该如何设计；
- Custom GPT 如何调用知识与 Skills；
- 如何建立真实案例评测集；
- 如何记录人工修改、拍摄问题和发布反馈；
- 如何判断应该修改知识库、Skill、输入结构还是系统提示词；
- 如何避免系统在迭代过程中反复失控或回退。

本架构不追求一次性完成所有文件，而是建立一条可持续迭代的生产链路。

---

# 2. 核心架构

TikTok Script Director 的知识和能力不应直接由零散 Source 驱动。

完整链路应为：

```text
Source 原始资料
↓
Source Digest 结构化消化
↓
Domain Knowledge 自有知识库
↓
Skills 执行流程
↓
System Instructions 统一调度
↓
Script Director 实际生成
↓
人工审核与拍摄
↓
发布数据与问题反馈
↓
问题归因
↓
更新知识库 / Skills / 输入合同 / 系统指令
↓
回归评测
↓
发布新版本
```

系统必须明确区分：

```text
原始资料
≠
内部知识
≠
执行技能
≠
系统提示词
≠
评测标准
```

---

# 3. 各层职责

---

## 3.1 Source 层

Source 是外部或内部依据。

它回答：

> 我们依据什么资料形成判断？

Source 可以包括：

```text
TikTok 官方课程
TikTok Shop 官方规则
平台政策与合规说明
优秀竞品视频
竞品评论
团队真实拍摄经验
产品测试记录
供应商资料
已有导演、编剧、拍摄类 Skills
此前项目文档
内部复盘记录
```

Source 层只负责保存原始依据，不直接承担智能体执行规则。

---

## 3.2 Source Digest 层

Source Digest 是对原始资料的结构化消化。

它回答：

> 这份资料对当前 Script Director 有什么实际价值？

Source Digest 不只是摘要，而是把原始资料转成可执行结论。

每份 Digest 至少包含：

```text
原始观点
可执行结论
适用条件
不适用情况
常见误用
风险
对当前系统的影响
建议进入哪个知识文件
建议关联哪个 Skill
```

---

## 3.3 Domain Knowledge 层

Domain Knowledge 是经过筛选和整理后的内部标准。

它回答：

> 对于当前业务，我们认为什么是正确的？

知识库不应是 Source 的复制，也不应是课程笔记堆叠。

它必须体现：

- 当前目标市场；
- 当前商品类型；
- 当前团队拍摄能力；
- 当前 TikTok Shop 转化目标；
- 当前阶段人工审核机制；
- 当前对真实性、可拍摄性和画面证明的要求。

---

## 3.4 Skills 层

Skills 是把知识转成可重复执行动作的流程。

它回答：

> 拿到输入以后，系统具体应该怎么做？

Skill 不是知识文件的摘要，而是一个固定执行程序。

它需要明确：

```text
输入
前置条件
执行步骤
判断规则
调用哪些知识文件
输出
失败条件
异常处理
自检
```

---

## 3.5 System Instructions 层

System Instructions 负责统一调度。

它回答：

> 一个 Custom GPT 如何按正确顺序调用不同能力？

系统指令不应塞入全部知识。

它主要负责：

- 定义角色；
- 定义边界；
- 定义处理顺序；
- 指定何时调用哪个 Skill；
- 指定输出结构；
- 指定禁止事项；
- 指定遇到资料不足时的处理方式。

---

## 3.6 Evaluation 层

Evaluation 用于判断系统是否真的变好。

它回答：

> 新版本是否比旧版本更可靠？

Evaluation 不只看语言质量，而应检查：

```text
真实性
构想理解
主传播命题
核心卖点与辅助卖点
画面证明
可拍摄性
TikTok 节奏
合规
输出稳定性
人工修改成本
```

---

## 3.7 Feedback 层

Feedback 用于吸收真实业务结果。

它回答：

> 实际使用后，哪些问题需要反馈到系统？

反馈来源包括：

```text
人工审核修改
拍摄执行问题
剪辑问题
素材缺口
发布数据
商品点击数据
转化数据
团队使用意见
平台政策变化
```

反馈不能直接无条件改写知识库，必须先归因。

---

# 4. Source 管理规范

---

## 4.1 Source 类型

建议将 Source 分为以下几类：

```text
official
internal
competitor_cases
product_tests
imported_skills
policy_and_compliance
publishing_results
```

---

## 4.2 每份 Source 的最小元数据

每份 Source 至少记录：

```yaml
source_id:
source_name:
source_type:
source_path_or_url:
publisher:
captured_at:
market:
category:
language:
credibility:
validity_status:
notes:
```

字段含义：

| 字段 | 说明 |
|---|---|
| source_id | 唯一编号 |
| source_name | 来源名称 |
| source_type | 官方、内部、竞品、测试等 |
| source_path_or_url | 文件路径或链接 |
| publisher | 来源发布者 |
| captured_at | 获取时间 |
| market | 美国、东南亚等 |
| category | 车载清洁、口腔护理等 |
| language | 原始语言 |
| credibility | 高、中、低 |
| validity_status | 有效、待确认、过时 |
| notes | 备注 |

---

## 4.3 Source 使用原则

Source 必须遵守：

1. 保留原始出处；
2. 平台政策必须记录获取时间；
3. 竞品视频只能作为表达参考；
4. 供应商资料不能直接作为已验证事实；
5. 内部测试结果优先于供应商描述；
6. AI 视频不能作为真实产品能力证据；
7. 多份资料冲突时，必须保留冲突记录；
8. 过期资料不能继续无标记使用。

---

# 5. Source Digest 设计

---

## 5.1 Digest 标准模板

每份 Digest 使用统一结构：

```markdown
# Source Digest 标题

## Source 信息

## 原始观点

## 可执行结论

## 适用条件

## 不适用或例外

## 常见误用

## 风险与限制

## 对 TikTok Script Director 的影响

## 建议进入的知识文件

## 建议关联的 Skills

## 待验证问题
```

---

## 5.2 Digest 示例

```markdown
## 原始观点

TikTok 视频前三秒需要快速建立观看理由。

## 可执行结论

前三秒至少出现以下一种：

- 明确问题；
- 明显结果；
- 视觉反差；
- 异常动作；
- 直接利益点。

## 适用条件

适用于：

- 转化视频；
- 种草视频；
- 测评视频；
- 生活场景视频。

## 不适用或例外

部分 ASMR 或沉浸式清洁内容可以弱化语言 Hook，
但仍然需要视觉变化、清洁进度或结果预期。

## 常见误用

- 强行加入夸张字幕；
- 前三秒只展示 Logo；
- 开头只拍静态产品；
- Hook 与后续内容无关。

## 对系统的影响

进入：

- `03_HOOK_RULES.md`
- `concept_strategy_design`
- `shooting_script_generation`
- `script_quality_review`
```

---

# 6. Domain Knowledge 设计

---

## 6.1 第一版知识库结构

v0.1 建议建立以下知识文件：

```text
01_GOOD_SCRIPT_STANDARD.md
02_CONTENT_FORMATS.md
03_HOOK_RULES.md
04_PRODUCT_PROOF.md
05_SHOT_PRODUCTION.md
06_COMPLIANCE_RULES.md
07_SCRIPT_OUTPUT_SCHEMA.md
```

---

## 6.2 每份知识文件的统一结构

每个知识文件至少包含：

```markdown
# 标题

## 1. 定义

## 2. 为什么需要

## 3. 适用场景

## 4. 不适用或例外

## 5. 核心规则

## 6. 执行标准

## 7. 正确示例

## 8. 错误示例

## 9. 常见误用

## 10. 风险与限制

## 11. 来源依据

## 12. 关联 Skills

## 13. 版本记录
```

---

## 6.3 Knowledge 与 Source 的关系

正确关系：

```text
多个 Source
↓
一个或多个 Digest
↓
一条稳定内部知识
```

不应直接：

```text
把 20 份网页
直接上传到 Custom GPT
```

原因包括：

- 重复；
- 冲突；
- 过时；
- 语言风格不统一；
- 适用市场不同；
- 模型难以判断优先级。

---

## 6.4 Knowledge 与 Skills 的区别

### Knowledge 回答

```text
什么是好的 Hook？
什么是可信的画面证明？
多卖点视频如何组织？
什么时候适合真人 UGC？
什么样的 Claims 有风险？
```

### Skills 回答

```text
拿到一条构想后先做什么？
怎么判断能不能写？
怎么确定主传播命题？
怎么区分核心卖点和辅助卖点？
怎么生成逐镜头脚本？
怎么审核脚本？
```

结论：

> Knowledge 是判断依据，Skills 是执行方法。

---

# 7. Skills 架构

第一版保持单智能体，但内部包含四个核心 Skills。

---

## 7.1 Skill 1：input_fact_validation

### 目标

判断输入是否足以支持脚本生成。

### 输入

```text
Script Input Pack
```

### 调用知识

```text
01_GOOD_SCRIPT_STANDARD.md
04_PRODUCT_PROOF.md
06_COMPLIANCE_RULES.md
07_SCRIPT_OUTPUT_SCHEMA.md
```

### 执行步骤

```text
1. 识别商品
2. 识别已验证事实
3. 识别未核实信息
4. 识别待测试内容
5. 识别竞品能力
6. 识别风险和限制
7. 判断画面证明是否成立
8. 输出 READY / PROVISIONAL / BLOCKED
```

### 输出

```text
输入检查结果
可用事实
不可直接使用的信息
待验证项
风险项
生成状态
```

### 失败条件

```text
商品不明确
核心功能不存在
关键 Proof 无法验证
主要 Claim 存在严重风险
```

---

## 7.2 Skill 2：concept_strategy_design

### 目标

把口语化构想转换成清晰的视频策略。

### 输入

```text
通过 input_fact_validation 的输入
```

### 调用知识

```text
01_GOOD_SCRIPT_STANDARD.md
02_CONTENT_FORMATS.md
03_HOOK_RULES.md
04_PRODUCT_PROOF.md
```

### 执行步骤

```text
1. 保留原始构想意图
2. 规范化视频主题
3. 确定主传播命题
4. 识别核心问题
5. 确定核心卖点
6. 整理辅助卖点
7. 判断卖点之间是否相关
8. 选择内容形式
9. 选择脚本结构
10. 选择目标时长
11. 选择 Hook 方向
12. 确定画面证明方式
```

### 输出

```text
规范化构想
主传播命题
核心问题
核心卖点
辅助卖点
内容形式
脚本结构
目标时长
Hook 方向
```

### 失败条件

```text
构想与商品无关
核心问题与核心卖点不匹配
卖点之间完全无主线
目标时长无法承载信息量
```

---

## 7.3 Skill 3：shooting_script_generation

### 目标

生成团队可直接执行的 TikTok 拍摄脚本。

### 输入

```text
已确认的视频策略
```

### 调用知识

```text
03_HOOK_RULES.md
04_PRODUCT_PROOF.md
05_SHOT_PRODUCTION.md
07_SCRIPT_OUTPUT_SCHEMA.md
```

### 执行步骤

```text
1. 分配总时长
2. 设计前三秒
3. 设计核心问题镜头
4. 设计产品动作镜头
5. 设计画面证明镜头
6. 安排辅助卖点
7. 设计 CTA
8. 编写字幕
9. 编写旁白
10. 标记连续镜头
11. 生成拍摄准备清单
12. 生成两个 Hook 变体
```

### 输出

```text
核心脚本
逐镜头表
英文字幕
英文旁白
中文审核含义
拍摄准备清单
Hook A
Hook B
```

### 失败条件

```text
镜头无法执行
画面无法证明
字幕依赖未验证 Claim
信息密度超出目标时长
```

---

## 7.4 Skill 4：script_quality_review

### 目标

对生成脚本进行真实性、可拍摄性和 TikTok 适配审核。

### 输入

```text
生成后的完整脚本
```

### 调用知识

```text
01_GOOD_SCRIPT_STANDARD.md
03_HOOK_RULES.md
04_PRODUCT_PROOF.md
05_SHOT_PRODUCTION.md
06_COMPLIANCE_RULES.md
07_SCRIPT_OUTPUT_SCHEMA.md
```

### 审核维度

```text
真实性
主传播命题
构想理解
核心卖点
辅助卖点
前三秒
画面证明
可拍摄性
节奏
合规
信息密度
字幕与画面关系
```

### 执行步骤

```text
1. 逐项评分
2. 识别严重问题
3. 识别普通问题
4. 自动修订一次
5. 再次审核
6. 输出最终状态
```

### 输出

```text
审核结果
通过项
风险项
待验证项
修改记录
最终状态
```

---

# 8. System Instructions 的职责

System Instructions 不应复制整个知识库。

它主要负责：

```text
定义智能体角色
定义系统边界
定义输入要求
规定四个 Skills 的调用顺序
规定 READY / PROVISIONAL / BLOCKED
规定禁止编造
规定输出结构
规定人工审核优先
规定遇到缺失信息时的处理方式
```

标准调用顺序：

```text
input_fact_validation
↓
concept_strategy_design
↓
shooting_script_generation
↓
script_quality_review
```

不得跳过事实检查直接生成脚本。

---

# 9. 评测集设计

---

## 9.1 为什么必须建立评测集

没有评测集时，系统优化容易出现：

```text
修好了多卖点视频
却写坏了单卖点视频

强化了 Hook
却增加了夸张 Claims

增加了镜头细节
却降低了可执行性
```

评测集用于验证新版本是否整体变好。

---

## 9.2 第一批案例数量

第一版建议：

```text
5～10 条真实构想
```

至少覆盖：

```text
单场景单卖点
单场景多卖点
完整功能展示
测评对比
多场景展示
资料不足
存在风险 Claim
参考视频为 AI
```

---

## 9.3 每个评测案例必须保存

```text
原始飞书构想
Script Input Pack
系统版本
知识库版本
Skills 版本
第一次生成结果
人工修改后的脚本
人工修改原因
最终拍摄版本
拍摄中遇到的问题
发布结果
复盘结论
```

---

## 9.4 推荐目录

```text
evals/
├── cases/
│   ├── case_001_foam_sprayer_manual_vs_electric/
│   ├── case_002_vacuum_seat_gap/
│   ├── case_003_vacuum_multi_attachment/
│   └── ...
├── expected_outputs/
├── regression_results/
└── evaluation_reports/
```

---

## 9.5 评测维度

每条脚本至少检查：

| 维度 | 说明 |
|---|---|
| 事实准确 | 是否使用了真实信息 |
| 构想保真 | 是否改变原始意图 |
| 主线清晰 | 是否有主传播命题 |
| 卖点组织 | 核心与辅助卖点是否有主次 |
| Hook | 前三秒是否成立 |
| Product Proof | 是否能真实证明 |
| 可拍摄性 | 团队是否能执行 |
| 合规 | 是否存在风险 Claim |
| 信息密度 | 是否匹配时长 |
| 输出完整 | 是否符合 Schema |
| 人工修改成本 | 是否需要大改 |

---

# 10. 反馈闭环

完整反馈路线：

```text
飞书构想
↓
智能体生成
↓
人工审核
↓
记录修改
↓
实际拍摄
↓
记录执行问题
↓
发布
↓
记录内容和转化数据
↓
问题归因
↓
更新对应模块
↓
回归评测
↓
发布新版本
```

---

## 10.1 反馈来源

```text
人工审核修改
拍摄执行问题
演员表达问题
镜头问题
素材缺口
剪辑问题
发布数据
商品点击
加购
成交
评论反馈
政策变化
```

---

## 10.2 反馈分类

| 反馈类型 | 典型问题 | 修改位置 |
|---|---|---|
| 事实错误 | 编造吸力、容量、效果 | 输入合同、事实检查 Skill |
| 构想误解 | 改变原始创意 | 构想策略 Skill |
| 主线问题 | 多个卖点没有主次 | 内容知识库、策略 Skill |
| Hook 问题 | 开头慢、无视觉动作 | Hook 知识库、脚本 Skill |
| Proof 问题 | 只能靠口播证明 | Product Proof 知识库 |
| 不可拍摄 | 镜头条件不现实 | Shot Production、脚本 Skill |
| 节奏问题 | 镜头冗余、信息过多 | Good Script、审核 Skill |
| 合规问题 | 夸张、医疗、绝对化 | Compliance、审核 Skill |
| 输出不稳定 | 格式经常变化 | Output Schema、系统指令 |
| 输入缺失 | 飞书字段不足 | Input Contract |

---

## 10.3 不应直接修改系统的情况

单次播放低，不等于脚本规则错误。

可能原因包括：

```text
账号权重
发布时间
发布频率
素材质量
演员表现
剪辑水平
商品价格
店铺信誉
评论区
平台分发
脚本本身
```

因此：

> 单条低数据只能记录，不能立即改写知识库。

只有以下情况才进入优化：

```text
同类问题重复出现
多条案例出现相同错误
人工修改方向高度一致
拍摄团队反复遇到同一执行问题
平台规则发生明确变化
```

---

# 11. 版本管理

每次生成脚本时，必须记录：

```yaml
system_version:
input_contract_version:
knowledge_base_version:
skills_version:
output_schema_version:
evaluation_rubric_version:
generated_at:
product:
concept_id:
```

版本作用：

- 判断脚本来自哪套规则；
- 比较优化前后质量；
- 追踪某次错误由哪一版引入；
- 支持回归测试；
- 支持必要时回退。

---

## 11.1 推荐版本规则

```text
0.1：首版可验证
0.2：小范围规则调整
0.3：结构稳定
1.0：真实业务验证完成
```

重大变更示例：

```text
输入结构变化
输出 Schema 变化
Skills 调用顺序变化
审核标准变化
新增内容类型
新增类目规则
```

---

# 12. 推荐目录结构

```text
tiktok-script-director/
├── docs/
│   ├── 00_MASTER_DESIGN.md
│   ├── 01_INPUT_CONTRACT.md
│   ├── 02_SYSTEM_INSTRUCTIONS.md
│   ├── 03_KNOWLEDGE_BASE_INDEX.md
│   ├── 04_SCRIPT_OUTPUT_SCHEMA.md
│   ├── 05_EVALUATION_RUBRIC.md
│   └── 06_KNOWLEDGE_SKILLS_ARCHITECTURE_AND_FEEDBACK_LOOP.md
│
├── sources/
│   ├── official/
│   ├── internal/
│   ├── competitor_cases/
│   ├── product_tests/
│   ├── imported_skills/
│   ├── policy_and_compliance/
│   └── publishing_results/
│
├── source_digests/
│   ├── hook_sources_digest.md
│   ├── content_formats_digest.md
│   ├── product_proof_digest.md
│   ├── shooting_digest.md
│   └── compliance_digest.md
│
├── knowledge/
│   ├── 01_GOOD_SCRIPT_STANDARD.md
│   ├── 02_CONTENT_FORMATS.md
│   ├── 03_HOOK_RULES.md
│   ├── 04_PRODUCT_PROOF.md
│   ├── 05_SHOT_PRODUCTION.md
│   ├── 06_COMPLIANCE_RULES.md
│   └── 07_SCRIPT_OUTPUT_SCHEMA.md
│
├── skills/
│   ├── input_fact_validation/
│   ├── concept_strategy_design/
│   ├── shooting_script_generation/
│   └── script_quality_review/
│
├── evals/
│   ├── cases/
│   ├── expected_outputs/
│   ├── regression_results/
│   └── evaluation_reports/
│
└── feedback/
    ├── human_edits/
    ├── production_issues/
    ├── publishing_results/
    └── improvement_backlog/
```

---

# 13. 正确建设顺序

建议冻结为：

```text
1. 明确系统需求和边界
2. 整理 Source 清单
3. 为 Source 添加元数据
4. 对 Source 做结构化 Digest
5. 根据实际业务需求形成自有知识库
6. 根据知识库编写 Skills
7. 编写 System Instructions
8. 冻结 Script Output Schema
9. 建立 5～10 条真实评测案例
10. 搭建 Custom GPT
11. 生成人工审核版本
12. 实际拍摄和发布
13. 收集人工、拍摄和数据反馈
14. 对反馈进行问题归因
15. 更新知识库、Skills、输入合同或系统指令
16. 运行回归评测
17. 发布新版本
```

---

# 14. 当前阶段禁止事项

当前阶段禁止：

```text
未经 Digest 直接堆入大量 Source
把 Source 当成知识库
把 Knowledge 写成泛泛课程总结
把 Skills 写成空泛角色描述
没有评测集就频繁修改规则
因为一条视频数据低就重写系统
同时开发多 Agent 和完整后端
跳过人工审核
自动把脚本直接发布
```

---

# 15. 当前冻结结论

TikTok Script Director 的知识与技能建设路线冻结为：

```text
Source
→ Source Digest
→ Domain Knowledge
→ Skills
→ System Instructions
→ Script Output
→ Evaluation
→ Feedback
→ Versioned Improvement
```

当前系统必须坚持：

```text
原始资料保留出处
知识库经过业务化重写
Skills 负责执行而不是讲概念
单智能体内部调用多个 Skills
人工审核始终存在
真实案例形成评测集
反馈先归因再更新
每次更新必须回归测试
所有产物必须版本化
```

---

# 16. 下一步

下一阶段建议先建立：

```text
03_KNOWLEDGE_BASE_INDEX.md
```

用于明确：

- 第一版需要哪些 Source；
- 每个 Source 属于哪个主题；
- 哪些 Source 已获取；
- 哪些 Source 尚缺失；
- 哪些 Source 已完成 Digest；
- 每份知识文件依赖哪些 Digest；
- 哪个 Skill 调用哪些知识文件。
