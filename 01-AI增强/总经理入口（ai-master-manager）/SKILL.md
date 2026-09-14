---
name: ai-master-manager
description: 总经理的显式入口。用户要做任何复杂任务、需要补齐认知、选择工具、检查方向、调用本机技能或安排独立审计时使用。它先读取并执行 ai-master 的总经理流程，再决定是否调用动画工厂、研究、剪辑、配音或其他员工；不得跳过方向审计、能力探针、最小验证和风险门。
metadata:
  canonical_skill: ai-master
  role: ai-general-manager
---

# 总经理入口（显式入口）

这是给用户在 Skill 库里直接找到的入口，不是另一套独立能力。实际规则以
运行时技能目录中的 `ai-master/SKILL.md` 为唯一正本（Windows 通常为 `%USERPROFILE%\\.codex\\skills\\ai-master\\SKILL.md`；macOS/Linux 为 `~/.codex/skills/ai-master/SKILL.md`）。

调用本入口时必须先读取正本，并按其顺序执行：

1. 读取公司能力地图、roster 和当前项目状态；
2. 把用户目标编译成任务族，主动指出用户可能不知道的前置环节；
3. 检查现有技能与工具，缺能力时先研究、审查、探针，再提出安装或替代方案；
4. 做方向审计和最便宜的免费验证，未通过不得付费生产；
5. 只调度匹配的员工技能，完成后交给独立审计，不把自己的自评当成通过。

不得只靠关键词猜技能，也不得因为用户催促而跳过上述门槛。
