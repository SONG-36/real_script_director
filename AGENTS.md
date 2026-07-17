# AGENTS.md

## 1. 项目定位

本仓库是 `TikTok Script Director` 的设计、知识、Skills、评测与反馈仓库。

当前阶段只建设：

```text
口语构想
→ 事实检查
→ 策略设计
→ 正式拍摄脚本
→ 质量审核
```

不要擅自扩展为完整视频生产平台。

## 2. 每次工作前必读

按顺序阅读：

1. `docs/PROJECT_STATUS.md`
2. `docs/index.md`
3. 与当前任务直接相关的设计文档
4. 当前活动执行计划（如存在）
5. 相关目录下更深层的 `AGENTS.md`

## 3. 事实来源优先级

发生冲突时，优先级如下：

```text
已确认的内部产品测试
> 已批准的项目设计文档
> TikTok / 平台官方资料
> 内部结构化 Digest
> 供应商资料
> 竞品视频
> 未整理笔记
```

竞品能力不得自动视为我方产品能力。

## 4. 文档状态

文档必须显式标记状态：

```text
NOT_STARTED
DRAFT
DRAFT_FOR_VALIDATION
APPROVED
SUPERSEDED
```

未经批准的知识文件不得被描述为最终规则。

## 5. 工作方式

小任务可以直接修改。

复杂任务必须先创建：

```text
docs/exec-plans/active/<task-name>.md
```

执行计划必须记录：

- 目标
- 非目标
- 输入
- 修改文件
- 验收标准
- 风险
- 进度
- 决策
- 最终结果

完成后移动到：

```text
docs/exec-plans/completed/
```

## 6. 修改后必须更新

根据任务影响，更新以下一个或多个文件：

- `docs/PROJECT_STATUS.md`
- 当前执行计划
- `CHANGELOG.md`
- `docs/decisions/` 中的 ADR
- 相关知识文件版本记录
- 相关评测案例

不要维护无意义的逐分钟日志。

## 7. Scope 约束

当前禁止主动创建：

- Web 前端
- API 服务
- 数据库
- 飞书 API 集成
- 多 Agent 编排
- 视频生成链路
- 自动发布链路

除非上游设计文档已批准并明确允许实现。

## 8. Skills

仓库级 Skills 位于：

```text
.agents/skills/
```

产品运行时核心 Skills：

- `tsd-input-fact-validation`
- `tsd-concept-strategy-design`
- `tsd-shooting-script-generation`
- `tsd-script-quality-review`

仓库维护 Skills：

- `repo-source-digest`
- `repo-exec-plan-maintenance`

修改 Skill 时必须同步检查：

- 它引用的知识文件
- 输入和输出边界
- 失败条件
- 至少一个评测案例

## 9. 知识工程规则

```text
Source
→ Source Digest
→ Knowledge
→ Skill
→ Eval
→ Feedback
```

禁止跳过 Digest，把大批原始资料直接拼接成知识库。

## 10. 验证命令

```bash
python3 scripts/validate_structure.py
```

若验证失败，先修复结构和元数据，再声明任务完成。

## 11. 输出要求

提交结果时说明：

- 修改了什么
- 为什么修改
- 依据哪些文档
- 运行了什么验证
- 尚未解决什么

不要声称未实际运行的测试已经通过。