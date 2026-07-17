# Repository Architecture

本文件描述仓库的信息架构，不代表未来后端软件架构。

## 顶层结构

```text
AGENTS.md                 Codex 入口地图与仓库规则
docs/                     项目事实、设计、决策、计划和状态
.agents/skills/           Codex 可重复调用的仓库级工作流
sources/                  原始资料
source_digests/           原始资料的结构化消化
knowledge/                经过业务化重写的内部知识
templates/                输入、输出、Digest、评测模板
evals/                    回归评测案例与结果
feedback/                 人工、拍摄、发布反馈
scripts/                  结构验证等确定性工具
.github/                  可选的 VS Code / Copilot 适配层
```

## 分层原则

### 1. 地图层

- `AGENTS.md`
- `docs/index.md`
- `docs/PROJECT_STATUS.md`

只负责告诉人和 Agent：当前是什么项目、去哪里找事实、下一步做什么。

### 2. 事实与决策层

- `docs/00_MASTER_DESIGN.md`
- `docs/01_INPUT_CONTRACT.md`
- `docs/02_SYSTEM_INSTRUCTIONS.md`
- `docs/decisions/`
- `docs/exec-plans/`

是项目的记录系统。

### 3. 知识层

- `sources/`
- `source_digests/`
- `knowledge/`

原始资料与内部规则严格分离。

### 4. 执行层

- `.agents/skills/`
- `templates/`

把稳定知识转换成可重复工作流。

### 5. 验证与反馈层

- `evals/`
- `feedback/`

用于判断系统是否真实变好，而不是只看输出是否更像“专业文案”。

## 不使用 `.ai/` 的原因

`.ai/` 不是本项目依赖的统一标准目录。为减少重复和工具锁定，本项目采用：

- Codex：`AGENTS.md`、`.agents/skills/`
- 项目事实：`docs/`
- 可选 VS Code/Copilot 适配：`.github/agents/`、`.github/prompts/`
