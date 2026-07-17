# TikTok Script Director

一个面向 TikTok Shop US 的脚本导演系统项目。

当前目标不是开发完整后端，而是先把以下链路做稳定：

```text
飞书商品与证据
→ 竞品参考
→ 口语化视频构想
→ Script Input Pack
→ 可拍摄 TikTok 脚本
→ 人工审核
→ 拍摄与反馈
```

## 当前阶段

`SD-1｜系统设计与知识工程`

已完成：

- `docs/00_MASTER_DESIGN.md`
- `docs/06_KNOWLEDGE_SKILLS_ARCHITECTURE_AND_FEEDBACK_LOOP.md`
- Codex-first 项目脚手架

下一项：

- `docs/01_INPUT_CONTRACT.md`

## 如何开始

1. 在 VS Code 中打开本目录。
2. 从仓库根目录启动 Codex。
3. 第一条指令使用：

```text
先阅读 AGENTS.md、docs/index.md 和 docs/PROJECT_STATUS.md。
不要写业务代码。
为 docs/01_INPUT_CONTRACT.md 创建一个执行计划，并放入 docs/exec-plans/active/。
```

4. 完成任务后运行：

```bash
python3 scripts/validate_structure.py
```

## 核心原则

- `AGENTS.md` 是地图，不是百科全书。
- `docs/` 是项目事实和决策的记录系统。
- `.agents/skills/` 保存 Codex 可重复调用的工作流。
- `sources/` 只保存原始材料。
- `source_digests/` 保存结构化消化结果。
- `knowledge/` 保存经过业务化重写的内部知识。
- `evals/` 用于防止优化一处、破坏另一处。
- `feedback/` 保存人工修改、拍摄问题和发布反馈。
- `.ai/` 不作为本项目约定目录使用。

## 当前禁止

- 多 Agent 业务系统
- FastAPI / React 后端
- 飞书自动回写
- AI 视频生成
- 自动发布
- 爆款预测
- 未验证业务流程时批量写代码
