---
name: ai-animation-factory
description: 茂茂 AI 动画工厂：把一句话、故事或参考片变成经过方向审计、角色/场景/分镜/动作/声音/剪辑与独立验收的动画短片；适用于不会专业流程、需要总经理自动补齐制作环节的任务。
metadata:
  canonical_skill: maomao-animation-studio
  version: "1.0.0"
---

# AI 动画工厂（可见入口）

这是 `maomao-animation-studio` 的正式可见入口。核心实现只有一份，避免两个 Skill 分叉；调用本入口时必须读取并执行：

运行时技能目录中的 `maomao-animation-studio/SKILL.md`（Windows 通常位于 `%USERPROFILE%\\.codex\\skills`；macOS/Linux 位于 `~/.codex/skills`）。

## 总经理开工顺序

1. 先运行 总经理预检，识别任务族、员工、工具、方向风险和最便宜验证：

   ```bash
   python <运行时 skills>/ai-master/scripts/ai_master.py preflight --request "用户原话"
   ```

2. 再运行动画启动器，读取公司盘点、能力地图和 Skill 哈希：

   ```bash
   python <运行时 skills>/maomao-animation-studio/scripts/startup_adapter.py "用户原话" --receipt <可写临时目录>/animation-startup.json
   ```

3. `WRONG_PROBLEM`、`NEEDS_RESEARCH`、缺工具或未知能力时，只能研究/探针/做代表段，不能付费扩量。

4. 角色重复出现必须先有角色锚点；多镜头必须先有分镜；打斗必须先有动作节拍和代表段；最终成片必须交独立审计，生产者不得自签 PASS。

## 缺工具处理

发现 `MISSING` 时，先研究官方/GitHub来源，再做安全和许可审查，取得必要授权后安装，最后跑无费用探针并写回公司花名册。下载 Skill 或仓库不等于已经能用。

## 边界

本 Skill 不宣称 ChatCut/MCP/浏览器原生入口已被完全锁死；未实测的能力必须标为 `UNKNOWN`。不要把提示词、方案文档或一次失败生成当成稳定生产能力。
