# Repository Operating Model

**Status**: APPROVED_FOR_SCAFFOLD  
**Version**: 0.1

## 1. 三个容易混淆的概念

### AGENTS.md

项目级长期指令和导航地图。

适合放：

- 项目是什么；
- 哪些文档是事实来源；
- 当前禁止做什么；
- 修改后要更新哪些记录；
- 如何验证结果。

不适合放完整知识库。

### `.agents/skills/<skill>/SKILL.md`

Codex 可按任务选择加载的重复工作流。

适合放：

- 什么时候触发；
- 输入；
- 固定步骤；
- 读取哪些知识；
- 输出；
- 失败条件。

### `.agent.md`

这是 VS Code 自定义 Agent 的文件格式，通常位于 `.github/agents/`。

它用于切换一个特定角色、工具集合或工作方式。

它不是 Codex 仓库 Skill 的替代品。

## 2. `.ai/` 是什么

`.ai/` 没有被本项目作为统一标准采用。

不同团队可能用它保存：

- prompts；
- memory；
- rules；
- agent 配置；
- 生成记录。

这种命名本身不会让 Codex自动理解内容。

本项目使用明确、可验证的目录：

```text
AGENTS.md
docs/
.agents/skills/
sources/
source_digests/
knowledge/
evals/
feedback/
```

## 3. “记录”不等于写长日志

Codex 不应依赖聊天记忆恢复项目状态。

仓库内应保留四种记录：

1. `PROJECT_STATUS.md`：现在做到哪里；
2. `exec-plans/`：复杂任务如何推进；
3. `decisions/`：为什么做出关键选择；
4. `CHANGELOG.md`：版本发生了什么变化。

不要把所有对话复制进仓库。

## 4. 核心层与适配层

### 核心层

```text
AGENTS.md
docs/
.agents/skills/
```

面向 Codex 和长期项目维护。

### 可选适配层

```text
.github/agents/
.github/prompts/
.github/instructions/
.github/copilot-instructions.md
```

用于 VS Code / GitHub Copilot 的自定义入口。

删除适配层不会破坏项目核心知识。

## 5. 当前工作模式

```text
人确定目标和边界
→ Codex 读取地图与事实
→ 复杂任务先写执行计划
→ Codex 修改文档或结构
→ 运行确定性验证
→ 更新状态与决策
→ 人审核
```

## 6. 何时新增文件

只在以下情况下新增：

- 存在独立且稳定的事实来源；
- 规则只适用于某个目录；
- 工作流会重复发生；
- 复杂任务需要跨会话继续；
- 需要回归评测；
- 关键决策未来可能被质疑。

不要为了“看起来 Agent 化”而创建空目录和重复规则。
