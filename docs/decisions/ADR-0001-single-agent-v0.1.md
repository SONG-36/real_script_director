# ADR-0001｜V0.1 使用单智能体

**Status**: ACCEPTED  
**Date**: 2026-07-17

## Context

业务流程和知识标准尚未完成真实案例验证。

## Decision

V0.1 使用一个 Custom GPT，内部按四个固定 Skills 顺序执行。

不建立多 Agent 业务编排。

## Consequences

优点：

- 调试简单；
- 输出链路清楚；
- 更容易判断问题属于输入、知识、Skill 还是审核规则。

代价：

- 不追求并行；
- 暂不提供自主长链路运行。
