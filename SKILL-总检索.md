# 茂茂 Skill 总检索

> 自动生成时间：2026-09-14T04:33:39.347822+00:00
> 机器可读正本：`skills-catalog.json`
> 重建命令：`python build_skill_catalog.py`（Windows）或 `python3 build_skill_catalog.py`（macOS/Linux）

## 使用规则

1. 总经理开工前先读 `skills-catalog.json`，按目标语义选择 Skill，不靠用户记关键词。
2. `RUNTIME_REGISTERED` 表示已有 Codex 运行入口；`VISIBLE_ONLY` 只表示桌面资料存在，不能冒充可执行。
3. 同一 Skill 有多个桌面副本时，以 `runtime_path` 指向的正本为准。

## 运行入口

| 名称 | 调用 | 运行正本 | 状态 |
|---|---|---|---|
| imagegen | `$imagegen` | `C:\Users\MECHREVO\.codex\skills\.system\imagegen\SKILL.md` | RUNTIME_REGISTERED |
| openai-docs | `$openai-docs` | `C:\Users\MECHREVO\.codex\skills\.system\openai-docs\SKILL.md` | RUNTIME_REGISTERED |
| plugin-creator | `$plugin-creator` | `C:\Users\MECHREVO\.codex\skills\.system\plugin-creator\SKILL.md` | RUNTIME_REGISTERED |
| review-agent | `$review-agent` | `C:\Users\MECHREVO\.codex\skills\.system\review-agent\SKILL.md` | RUNTIME_REGISTERED |
| skill-creator | `$skill-creator` | `C:\Users\MECHREVO\.codex\skills\.system\skill-creator\SKILL.md` | RUNTIME_REGISTERED |
| skill-installer | `$skill-installer` | `C:\Users\MECHREVO\.codex\skills\.system\skill-installer\SKILL.md` | RUNTIME_REGISTERED |
| anti-ui-slop | `$anti-ui-slop` | `C:\Users\MECHREVO\.codex\skills\anti-ui-slop\SKILL.md` | RUNTIME_REGISTERED |
| higgsfield-prompt | `$higgsfield-prompt` | `C:\Users\MECHREVO\.codex\skills\higgsfield-prompt\SKILL.md` | RUNTIME_REGISTERED |
| active-agent | `$active-agent` | `C:\Users\MECHREVO\.codex\skills\personal\active-agent\SKILL.md` | RUNTIME_REGISTERED |
| ad-copywriting | `$ad-copywriting` | `C:\Users\MECHREVO\.codex\skills\personal\ad-copywriting\SKILL.md` | RUNTIME_REGISTERED |
| advanced-xhs-visual-design | `$advanced-xhs-visual-design` | `C:\Users\MECHREVO\.codex\skills\personal\advanced-xhs-visual-design\SKILL.md` | RUNTIME_REGISTERED |
| agent-eval-loop | `$agent-eval-loop` | `C:\Users\MECHREVO\.codex\skills\personal\agent-eval-loop\SKILL.md` | RUNTIME_REGISTERED |
| ai-animation-factory | `$ai-animation-factory` | `C:\Users\MECHREVO\.codex\skills\personal\ai-animation-factory\SKILL.md` | RUNTIME_REGISTERED |
| ai-master | `$ai-master` | `C:\Users\MECHREVO\.codex\skills\personal\ai-master\SKILL.md` | RUNTIME_REGISTERED |
| ai-master-manager | `$ai-master-manager` | `C:\Users\MECHREVO\.codex\skills\personal\ai-master-manager\SKILL.md` | RUNTIME_REGISTERED |
| ai-master-toolkit | `$ai-master-toolkit` | `C:\Users\MECHREVO\.codex\skills\personal\ai-master-toolkit\SKILL.md` | RUNTIME_REGISTERED |
| ai-polish | `$ai-polish` | `C:\Users\MECHREVO\.codex\skills\personal\ai-polish\SKILL.md` | RUNTIME_REGISTERED |
| ai-super-productivity-os | `$ai-super-productivity-os` | `C:\Users\MECHREVO\.codex\skills\personal\ai-super-productivity-os\SKILL.md` | RUNTIME_REGISTERED |
| animation-dream-factory | `$animation-dream-factory` | `C:\Users\MECHREVO\.codex\skills\personal\animation-dream-factory\SKILL.md` | RUNTIME_REGISTERED |
| animation-factory | `$animation-factory` | `C:\Users\MECHREVO\.codex\skills\personal\animation-factory\SKILL.md` | RUNTIME_REGISTERED |
| api-gateway | `$api-gateway` | `C:\Users\MECHREVO\.codex\skills\personal\api-gateway\SKILL.md` | RUNTIME_REGISTERED |
| asset-allocation-risk-review | `$asset-allocation-risk-review` | `C:\Users\MECHREVO\.codex\skills\personal\asset-allocation-risk-review\SKILL.md` | RUNTIME_REGISTERED |
| best-minds | `$best-minds` | `C:\Users\MECHREVO\.codex\skills\personal\best-minds\SKILL.md` | RUNTIME_REGISTERED |
| brand-voice-system | `$brand-voice-system` | `C:\Users\MECHREVO\.codex\skills\personal\brand-voice-system\SKILL.md` | RUNTIME_REGISTERED |
| browser-automation | `$browser-automation` | `C:\Users\MECHREVO\.codex\skills\personal\browser-automation\SKILL.md` | RUNTIME_REGISTERED |
| browser-research-agent | `$browser-research-agent` | `C:\Users\MECHREVO\.codex\skills\personal\browser-research-agent\SKILL.md` | RUNTIME_REGISTERED |
| business-dashboard-analyst | `$business-dashboard-analyst` | `C:\Users\MECHREVO\.codex\skills\personal\business-dashboard-analyst\SKILL.md` | RUNTIME_REGISTERED |
| code-review-ci | `$code-review-ci` | `C:\Users\MECHREVO\.codex\skills\personal\code-review-ci\SKILL.md` | RUNTIME_REGISTERED |
| coding-agent | `$coding-agent` | `C:\Users\MECHREVO\.codex\skills\personal\coding-agent\SKILL.md` | RUNTIME_REGISTERED |
| content-repurposing | `$content-repurposing` | `C:\Users\MECHREVO\.codex\skills\personal\content-repurposing\SKILL.md` | RUNTIME_REGISTERED |
| content-rewrite | `$content-rewrite` | `C:\Users\MECHREVO\.codex\skills\personal\content-rewrite\SKILL.md` | RUNTIME_REGISTERED |
| content-scraper | `$content-scraper` | `C:\Users\MECHREVO\.codex\skills\personal\content-scraper\SKILL.md` | RUNTIME_REGISTERED |
| context-engineering-agent | `$context-engineering-agent` | `C:\Users\MECHREVO\.codex\skills\personal\context-engineering-agent\SKILL.md` | RUNTIME_REGISTERED |
| course-design-agent | `$course-design-agent` | `C:\Users\MECHREVO\.codex\skills\personal\course-design-agent\SKILL.md` | RUNTIME_REGISTERED |
| docx-report-builder | `$docx-report-builder` | `C:\Users\MECHREVO\.codex\skills\personal\docx-report-builder\SKILL.md` | RUNTIME_REGISTERED |
| editable-pptx-builder | `$editable-pptx-builder` | `C:\Users\MECHREVO\.codex\skills\personal\editable-pptx-builder\SKILL.md` | RUNTIME_REGISTERED |
| enterprise-strategy-analysis | `$enterprise-strategy-analysis` | `C:\Users\MECHREVO\.codex\skills\personal\enterprise-strategy-analysis\SKILL.md` | RUNTIME_REGISTERED |
| finance-assistant | `$finance-assistant` | `C:\Users\MECHREVO\.codex\skills\personal\finance-assistant\SKILL.md` | RUNTIME_REGISTERED |
| financial-modeling | `$financial-modeling` | `C:\Users\MECHREVO\.codex\skills\personal\financial-modeling\SKILL.md` | RUNTIME_REGISTERED |
| financial-risk-literacy | `$financial-risk-literacy` | `C:\Users\MECHREVO\.codex\skills\personal\financial-risk-literacy\SKILL.md` | RUNTIME_REGISTERED |
| hook-angle-lab | `$hook-angle-lab` | `C:\Users\MECHREVO\.codex\skills\personal\hook-angle-lab\SKILL.md` | RUNTIME_REGISTERED |
| humanizer | `$humanizer` | `C:\Users\MECHREVO\.codex\skills\personal\humanizer\SKILL.md` | RUNTIME_REGISTERED |
| insight | `$insight` | `C:\Users\MECHREVO\.codex\skills\personal\insight\SKILL.md` | RUNTIME_REGISTERED |
| investment-risk-review | `$investment-risk-review` | `C:\Users\MECHREVO\.codex\skills\personal\investment-risk-review\SKILL.md` | RUNTIME_REGISTERED |
| knowledge-cards | `$knowledge-cards` | `C:\Users\MECHREVO\.codex\skills\personal\knowledge-cards\SKILL.md` | RUNTIME_REGISTERED |
| knowledge-palace | `$knowledge-palace` | `C:\Users\MECHREVO\.codex\skills\personal\knowledge-palace\SKILL.md` | RUNTIME_REGISTERED |
| last30days | `$last30days` | `C:\Users\MECHREVO\.codex\skills\personal\last30days\SKILL.md` | RUNTIME_REGISTERED |
| lead-followup-automation | `$lead-followup-automation` | `C:\Users\MECHREVO\.codex\skills\personal\lead-followup-automation\SKILL.md` | RUNTIME_REGISTERED |
| learning-loop | `$learning-loop` | `C:\Users\MECHREVO\.codex\skills\personal\learning-loop\SKILL.md` | RUNTIME_REGISTERED |
| life-coach | `$life-coach` | `C:\Users\MECHREVO\.codex\skills\personal\life-coach\SKILL.md` | RUNTIME_REGISTERED |
| maomao-animation-studio | `$maomao-animation-studio` | `C:\Users\MECHREVO\.codex\skills\personal\maomao-animation-studio\SKILL.md` | RUNTIME_REGISTERED |
| maomao-ppt | `$maomao-ppt` | `C:\Users\MECHREVO\.codex\skills\personal\maomao-ppt\SKILL.md` | RUNTIME_REGISTERED |
| maomao-skill-creator | `$maomao-skill-creator` | `C:\Users\MECHREVO\.codex\skills\personal\maomao-skill-creator\SKILL.md` | RUNTIME_REGISTERED |
| maomao-thinking | `$maomao-thinking` | `C:\Users\MECHREVO\.codex\skills\personal\maomao-thinking\SKILL.md` | RUNTIME_REGISTERED |
| market-monitoring | `$market-monitoring` | `C:\Users\MECHREVO\.codex\skills\personal\market-monitoring\SKILL.md` | RUNTIME_REGISTERED |
| market-research-analyst | `$market-research-analyst` | `C:\Users\MECHREVO\.codex\skills\personal\market-research-analyst\SKILL.md` | RUNTIME_REGISTERED |
| mcp-builder | `$mcp-builder` | `C:\Users\MECHREVO\.codex\skills\personal\mcp-builder\SKILL.md` | RUNTIME_REGISTERED |
| meeting-notes-actions | `$meeting-notes-actions` | `C:\Users\MECHREVO\.codex\skills\personal\meeting-notes-actions\SKILL.md` | RUNTIME_REGISTERED |
| memory-boost | `$memory-boost` | `C:\Users\MECHREVO\.codex\skills\personal\memory-boost\SKILL.md` | RUNTIME_REGISTERED |
| mimeng-topic-method | `$mimeng-topic-method` | `C:\Users\MECHREVO\.codex\skills\personal\mimeng-topic-method\SKILL.md` | RUNTIME_REGISTERED |
| multi-agent-orchestrator | `$multi-agent-orchestrator` | `C:\Users\MECHREVO\.codex\skills\personal\multi-agent-orchestrator\SKILL.md` | RUNTIME_REGISTERED |
| notes-research | `$notes-research` | `C:\Users\MECHREVO\.codex\skills\personal\notes-research\SKILL.md` | RUNTIME_REGISTERED |
| obsidian | `$obsidian` | `C:\Users\MECHREVO\.codex\skills\personal\obsidian\SKILL.md` | RUNTIME_REGISTERED |
| original-writing | `$original-writing` | `C:\Users\MECHREVO\.codex\skills\personal\original-writing\SKILL.md` | RUNTIME_REGISTERED |
| personal-investment-workflow | `$personal-investment-workflow` | `C:\Users\MECHREVO\.codex\skills\personal\personal-investment-workflow\SKILL.md` | RUNTIME_REGISTERED |
| proactive-agent | `$proactive-agent` | `C:\Users\MECHREVO\.codex\skills\personal\proactive-agent\SKILL.md` | RUNTIME_REGISTERED |
| quant-trading-literacy | `$quant-trading-literacy` | `C:\Users\MECHREVO\.codex\skills\personal\quant-trading-literacy\SKILL.md` | RUNTIME_REGISTERED |
| repo-context-compiler | `$repo-context-compiler` | `C:\Users\MECHREVO\.codex\skills\personal\repo-context-compiler\SKILL.md` | RUNTIME_REGISTERED |
| research-to-article | `$research-to-article` | `C:\Users\MECHREVO\.codex\skills\personal\research-to-article\SKILL.md` | RUNTIME_REGISTERED |
| self-improvement | `$self-improvement` | `C:\Users\MECHREVO\.codex\skills\personal\self-improvement\SKILL.md` | RUNTIME_REGISTERED |
| short-video-script-lab | `$short-video-script-lab` | `C:\Users\MECHREVO\.codex\skills\personal\short-video-script-lab\SKILL.md` | RUNTIME_REGISTERED |
| skill-creator | `$skill-creator` | `C:\Users\MECHREVO\.codex\skills\personal\skill-creator\SKILL.md` | RUNTIME_REGISTERED |
| skill-finder | `$skill-finder` | `C:\Users\MECHREVO\.codex\skills\personal\skill-finder\SKILL.md` | RUNTIME_REGISTERED |
| skill-vetter | `$skill-vetter` | `C:\Users\MECHREVO\.codex\skills\personal\skill-vetter\SKILL.md` | RUNTIME_REGISTERED |
| social-media-strategy | `$social-media-strategy` | `C:\Users\MECHREVO\.codex\skills\personal\social-media-strategy\SKILL.md` | RUNTIME_REGISTERED |
| sonoscli | `$sonoscli` | `C:\Users\MECHREVO\.codex\skills\personal\sonoscli\SKILL.md` | RUNTIME_REGISTERED |
| spreadsheet-analyst | `$spreadsheet-analyst` | `C:\Users\MECHREVO\.codex\skills\personal\spreadsheet-analyst\SKILL.md` | RUNTIME_REGISTERED |
| video-account-analysis | `$video-account-analysis` | `C:\Users\MECHREVO\.codex\skills\personal\video-account-analysis\SKILL.md` | RUNTIME_REGISTERED |
| video-transcribe | `$video-transcribe` | `C:\Users\MECHREVO\.codex\skills\personal\video-transcribe\SKILL.md` | RUNTIME_REGISTERED |
| wealth-advisor | `$wealth-advisor` | `C:\Users\MECHREVO\.codex\skills\personal\wealth-advisor\SKILL.md` | RUNTIME_REGISTERED |
| web-story | `$web-story` | `C:\Users\MECHREVO\.codex\skills\personal\web-story\SKILL.md` | RUNTIME_REGISTERED |
| wechat-mp-auto | `$wechat-mp-auto` | `C:\Users\MECHREVO\.codex\skills\personal\wechat-mp-auto\SKILL.md` | RUNTIME_REGISTERED |
| workflow-automation-builder | `$workflow-automation-builder` | `C:\Users\MECHREVO\.codex\skills\personal\workflow-automation-builder\SKILL.md` | RUNTIME_REGISTERED |
| xiaohongshu-auto | `$xiaohongshu-auto` | `C:\Users\MECHREVO\.codex\skills\personal\xiaohongshu-auto\SKILL.md` | RUNTIME_REGISTERED |
| skill-awesome | `$skill-awesome` | `C:\Users\MECHREVO\.codex\skills\skill-awesome\SKILL.md` | RUNTIME_REGISTERED |
| ui-design | `$ui-design` | `C:\Users\MECHREVO\.codex\skills\ui-design\SKILL.md` | RUNTIME_REGISTERED |

## 桌面资料条目

- `context-engineering-agent` — `C:\Users\MECHREVO\Desktop\skills 库_副本\01-AI增强\上下文工程代理（context-engineering-agent）\SKILL.md` — RUNTIME_REGISTERED
- `proactive-agent` — `C:\Users\MECHREVO\Desktop\skills 库_副本\01-AI增强\主动型代理（proactive-agent）\SKILL.md` — RUNTIME_REGISTERED
- `active-agent` — `C:\Users\MECHREVO\Desktop\skills 库_副本\01-AI增强\主动执行代理（active-agent）\SKILL.md` — RUNTIME_REGISTERED
- `agent-eval-loop` — `C:\Users\MECHREVO\Desktop\skills 库_副本\01-AI增强\代理评测闭环（agent-eval-loop）\SKILL.md` — RUNTIME_REGISTERED
- `multi-agent-orchestrator` — `C:\Users\MECHREVO\Desktop\skills 库_副本\01-AI增强\多代理协作编排（multi-agent-orchestrator）\SKILL.md` — RUNTIME_REGISTERED
- `ai-master-manager` — `C:\Users\MECHREVO\Desktop\skills 库_副本\01-AI增强\总经理入口（ai-master-manager）\SKILL.md` — RUNTIME_REGISTERED
- `ai-master-toolkit` — `C:\Users\MECHREVO\Desktop\skills 库_副本\01-AI增强\总经理能力工具箱（ai-master-toolkit）\SKILL.md` — RUNTIME_REGISTERED
- `ai-master` — `C:\Users\MECHREVO\Desktop\skills 库_副本\01-AI增强\总经理（ai-master）\SKILL.md` — RUNTIME_REGISTERED
- `skill-finder` — `C:\Users\MECHREVO\Desktop\skills 库_副本\01-AI增强\技能发现与选型（skill-finder）\SKILL.md` — RUNTIME_REGISTERED
- `best-minds` — `C:\Users\MECHREVO\Desktop\skills 库_副本\01-AI增强\最强大脑（best-minds）\SKILL.md` — RUNTIME_REGISTERED
- `self-improvement` — `C:\Users\MECHREVO\Desktop\skills 库_副本\01-AI增强\自我优化代理（self-improving-agent）\SKILL.md` — RUNTIME_REGISTERED
- `ai-animation-factory` — `C:\Users\MECHREVO\Desktop\skills 库_副本\02-内容创作\AI动画工厂（ai-animation-factory）\SKILL.md` — RUNTIME_REGISTERED
- `content-repurposing` — `C:\Users\MECHREVO\Desktop\skills 库_副本\02-内容创作\内容矩阵复用（content-repurposing）\SKILL.md` — RUNTIME_REGISTERED
- `animation-factory` — `C:\Users\MECHREVO\Desktop\skills 库_副本\02-内容创作\动画工厂（animation-factory）\SKILL.md` — RUNTIME_REGISTERED
- `animation-dream-factory` — `C:\Users\MECHREVO\Desktop\skills 库_副本\02-内容创作\动画梦工厂（animation-dream-factory）\SKILL.md` — RUNTIME_REGISTERED
- `original-writing` — `C:\Users\MECHREVO\Desktop\skills 库_副本\02-内容创作\原创长文（original-writing）\SKILL.md` — RUNTIME_REGISTERED
- `ai-polish` — `C:\Users\MECHREVO\Desktop\skills 库_副本\02-内容创作\去AI味润色（ai-polish）\SKILL.md` — RUNTIME_REGISTERED
- `humanizer` — `C:\Users\MECHREVO\Desktop\skills 库_副本\02-内容创作\去AI味英文版（humanizer）\SKILL.md` — RUNTIME_REGISTERED
- `mimeng-topic-method` — `C:\Users\MECHREVO\Desktop\skills 库_副本\02-内容创作\咪蒙选题法（mimeng-topic-method）\SKILL.md` — RUNTIME_REGISTERED
- `brand-voice-system` — `C:\Users\MECHREVO\Desktop\skills 库_副本\02-内容创作\品牌声纹系统（brand-voice-system）\SKILL.md` — RUNTIME_REGISTERED
- `ad-copywriting` — `C:\Users\MECHREVO\Desktop\skills 库_副本\02-内容创作\商单文案写作（ad-copywriting）\SKILL.md` — RUNTIME_REGISTERED
- `content-rewrite` — `C:\Users\MECHREVO\Desktop\skills 库_副本\02-内容创作\改稿（content-rewrite）\SKILL.md` — RUNTIME_REGISTERED
- `last30days` — `C:\Users\MECHREVO\Desktop\skills 库_副本\02-内容创作\最近30天（last30days）\SKILL.md` — RUNTIME_REGISTERED
- `maomao-animation-studio` — `C:\Users\MECHREVO\Desktop\skills 库_副本\02-内容创作\茂茂动画工厂（maomao-animation-studio）\SKILL.md` — RUNTIME_REGISTERED
- `research-to-article` — `C:\Users\MECHREVO\Desktop\skills 库_副本\02-内容创作\调研成稿（research-to-article）\SKILL.md` — RUNTIME_REGISTERED
- `hook-angle-lab` — `C:\Users\MECHREVO\Desktop\skills 库_副本\02-内容创作\选题钩子实验室（hook-angle-lab）\SKILL.md` — RUNTIME_REGISTERED
- `advanced-xhs-visual-design` — `C:\Users\MECHREVO\Desktop\skills 库_副本\02-内容创作\高级图文设计（advanced-xhs-visual-design）\SKILL.md` — RUNTIME_REGISTERED
- `api-gateway` — `C:\Users\MECHREVO\Desktop\skills 库_副本\03-开发工具\API网关（api-gateway）\SKILL.md` — RUNTIME_REGISTERED
- `mcp-builder` — `C:\Users\MECHREVO\Desktop\skills 库_副本\03-开发工具\MCP构建器（mcp-builder）\SKILL.md` — RUNTIME_REGISTERED
- `repo-context-compiler` — `C:\Users\MECHREVO\Desktop\skills 库_副本\03-开发工具\仓库上下文编译器（repo-context-compiler）\SKILL.md` — RUNTIME_REGISTERED
- `code-review-ci` — `C:\Users\MECHREVO\Desktop\skills 库_副本\03-开发工具\代码评审与CI修复（code-review-ci）\SKILL.md` — RUNTIME_REGISTERED
- `skill-creator` — `C:\Users\MECHREVO\Desktop\skills 库_副本\03-开发工具\技能创建器（skill-creator）\SKILL.md` — RUNTIME_REGISTERED
- `skill-vetter` — `C:\Users\MECHREVO\Desktop\skills 库_副本\03-开发工具\技能安全审查（skill-vetter）\SKILL.md` — RUNTIME_REGISTERED
- `coding-agent` — `C:\Users\MECHREVO\Desktop\skills 库_副本\03-开发工具\编程代理（coding-agent）\SKILL.md` — RUNTIME_REGISTERED
- `web-story` — `C:\Users\MECHREVO\Desktop\skills 库_副本\03-开发工具\网页故事（web-story）\SKILL.md` — RUNTIME_REGISTERED
- `content-scraper` — `C:\Users\MECHREVO\Desktop\skills 库_副本\04-浏览器自动化\内容抓取（content-scraper）\SKILL.md` — RUNTIME_REGISTERED
- `browser-automation` — `C:\Users\MECHREVO\Desktop\skills 库_副本\04-浏览器自动化\浏览器自动化（browser-automation）\SKILL.md` — RUNTIME_REGISTERED
- `browser-research-agent` — `C:\Users\MECHREVO\Desktop\skills 库_副本\04-浏览器自动化\浏览器调研代理（browser-research-agent）\SKILL.md` — RUNTIME_REGISTERED
- `lead-followup-automation` — `C:\Users\MECHREVO\Desktop\skills 库_副本\04-浏览器自动化\线索跟进自动化（lead-followup-automation）\SKILL.md` — RUNTIME_REGISTERED
- `video-transcribe` — `C:\Users\MECHREVO\Desktop\skills 库_副本\04-浏览器自动化\视频转写（video-transcribe）\SKILL.md` — RUNTIME_REGISTERED
- `wechat-mp-auto` — `C:\Users\MECHREVO\Desktop\skills 库_副本\05-社交媒体\公众号自动化（wechat-mp-auto）\SKILL.md` — RUNTIME_REGISTERED
- `video-account-analysis` — `C:\Users\MECHREVO\Desktop\skills 库_副本\05-社交媒体\微信视频号分析（video-account-analysis）\SKILL.md` — RUNTIME_REGISTERED
- `short-video-script-lab` — `C:\Users\MECHREVO\Desktop\skills 库_副本\05-社交媒体\短视频脚本工坊（short-video-script-lab）\SKILL.md` — RUNTIME_REGISTERED
- `social-media-strategy` — `C:\Users\MECHREVO\Desktop\skills 库_副本\05-社交媒体\社媒策略分析（social-media-strategy）\SKILL.md` — RUNTIME_REGISTERED
- `xiaohongshu-auto` — `C:\Users\MECHREVO\Desktop\skills 库_副本\05-社交媒体\自动发小红书（xiaohongshu-auto）\SKILL.md` — RUNTIME_REGISTERED
- `meeting-notes-actions` — `C:\Users\MECHREVO\Desktop\skills 库_副本\06-知识与学习\会议纪要行动项（meeting-notes-actions）\SKILL.md` — RUNTIME_REGISTERED
- `learning-loop` — `C:\Users\MECHREVO\Desktop\skills 库_副本\06-知识与学习\学习闭环（learning-loop）\SKILL.md` — RUNTIME_REGISTERED
- `life-coach` — `D:\Codex\skills 库_副本\06-知识与学习\人生教练（life-coach）\SKILL.md` — RUNTIME_REGISTERED
- `insight` — `C:\Users\MECHREVO\Desktop\skills 库_副本\06-知识与学习\洞察（insight）\SKILL.md` — RUNTIME_REGISTERED
- `知识卡片` — `C:\Users\MECHREVO\Desktop\skills 库_副本\06-知识与学习\知识卡片（knowledge-cards）\SKILL.md` — VISIBLE_ONLY
- `knowledge-palace` — `C:\Users\MECHREVO\Desktop\skills 库_副本\06-知识与学习\知识宫殿（knowledge-palace）\SKILL.md` — RUNTIME_REGISTERED
- `notes-research` — `C:\Users\MECHREVO\Desktop\skills 库_副本\06-知识与学习\笔记研究助手（notes-research）\SKILL.md` — RUNTIME_REGISTERED
- `maomao-thinking` — `C:\Users\MECHREVO\Desktop\skills 库_副本\06-知识与学习\茂茂商业思考（maomao-thinking）\SKILL.md` — RUNTIME_REGISTERED
- `memory-boost` — `C:\Users\MECHREVO\Desktop\skills 库_副本\06-知识与学习\记忆增强（memory-boost）\SKILL.md` — RUNTIME_REGISTERED
- `course-design-agent` — `C:\Users\MECHREVO\Desktop\skills 库_副本\06-知识与学习\课程设计代理（course-design-agent）\SKILL.md` — RUNTIME_REGISTERED
- `obsidian` — `C:\Users\MECHREVO\Desktop\skills 库_副本\07-效率工具\Obsidian笔记（obsidian）\SKILL.md` — RUNTIME_REGISTERED
- `sonoscli` — `C:\Users\MECHREVO\Desktop\skills 库_副本\07-效率工具\办公协同（sonoscli）\SKILL.md` — RUNTIME_REGISTERED
- `editable-pptx-builder` — `C:\Users\MECHREVO\Desktop\skills 库_副本\07-效率工具\可编辑PPT生成（editable-pptx-builder）\SKILL.md` — RUNTIME_REGISTERED
- `workflow-automation-builder` — `C:\Users\MECHREVO\Desktop\skills 库_副本\07-效率工具\工作流自动化搭建（workflow-automation-builder）\SKILL.md` — RUNTIME_REGISTERED
- `docx-report-builder` — `C:\Users\MECHREVO\Desktop\skills 库_副本\07-效率工具\报告文档生成（docx-report-builder）\SKILL.md` — RUNTIME_REGISTERED
- `maomao-ppt` — `C:\Users\MECHREVO\Desktop\skills 库_副本\07-效率工具\茂茂PPT（maomao-ppt）\SKILL.md` — RUNTIME_REGISTERED
- `market-research-analyst` — `C:\Users\MECHREVO\Desktop\skills 库_副本\08-数据分析\市场调研分析（market-research-analyst）\SKILL.md` — RUNTIME_REGISTERED
- `business-dashboard-analyst` — `C:\Users\MECHREVO\Desktop\skills 库_副本\08-数据分析\经营仪表盘分析（business-dashboard-analyst）\SKILL.md` — RUNTIME_REGISTERED
- `spreadsheet-analyst` — `C:\Users\MECHREVO\Desktop\skills 库_副本\08-数据分析\表格分析助手（spreadsheet-analyst）\SKILL.md` — RUNTIME_REGISTERED
- `finance-assistant` — `C:\Users\MECHREVO\Desktop\skills 库_副本\08-数据分析\财务分析助手（finance-assistant）\SKILL.md` — RUNTIME_REGISTERED
- `asset-allocation-risk-review` — `C:\Users\MECHREVO\Desktop\skills 库_副本\08-数据分析\资产配置风险复盘（asset-allocation-risk-review）\SKILL.md` — RUNTIME_REGISTERED
- `financial-risk-literacy` — `C:\Users\MECHREVO\Desktop\skills 库_副本\08-数据分析\金融风险识别（financial-risk-literacy）\SKILL.md` — RUNTIME_REGISTERED
- `personal-investment-workflow` — `C:\Users\MECHREVO\Desktop\skills 库_副本\09-金融\个人投资工作流（personal-investment-workflow）\SKILL.md` — RUNTIME_REGISTERED
- `enterprise-strategy-analysis` — `C:\Users\MECHREVO\Desktop\skills 库_副本\09-金融\企业策略分析（enterprise-strategy-analysis）\SKILL.md` — RUNTIME_REGISTERED
- `investment-risk-review` — `C:\Users\MECHREVO\Desktop\skills 库_副本\09-金融\投资风险辨析（investment-risk-review）\SKILL.md` — RUNTIME_REGISTERED
- `market-monitoring` — `C:\Users\MECHREVO\Desktop\skills 库_副本\09-金融\看盘盯盘（market-monitoring）\SKILL.md` — RUNTIME_REGISTERED
- `financial-modeling` — `C:\Users\MECHREVO\Desktop\skills 库_副本\09-金融\财务建模（financial-modeling）\SKILL.md` — RUNTIME_REGISTERED
- `wealth-advisor` — `C:\Users\MECHREVO\Desktop\skills 库_副本\09-金融\财富顾问（wealth-advisor）\SKILL.md` — RUNTIME_REGISTERED
- `quant-trading-literacy` — `C:\Users\MECHREVO\Desktop\skills 库_副本\09-金融\量化交易认知（quant-trading-literacy）\SKILL.md` — RUNTIME_REGISTERED
- `higgsfield-prompt` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\01_动画与视频制作\Higgsfield视频提示词\SKILL.md` — RUNTIME_REGISTERED
- `skill-awesome` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\02_技能治理与安全\Agent技能规范与评估\SKILL.md` — RUNTIME_REGISTERED
- `anti-ui-slop` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\04_UI与产品设计\反低质界面审查\SKILL.md` — RUNTIME_REGISTERED
- `ui-design` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\04_UI与产品设计\界面设计\SKILL.md` — RUNTIME_REGISTERED
- `active-agent` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\active-agent\SKILL.md` — RUNTIME_REGISTERED
- `ad-copywriting` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\ad-copywriting\SKILL.md` — RUNTIME_REGISTERED
- `advanced-xhs-visual-design` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\advanced-xhs-visual-design\SKILL.md` — RUNTIME_REGISTERED
- `agent-eval-loop` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\agent-eval-loop\SKILL.md` — RUNTIME_REGISTERED
- `ai-animation-factory` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\ai-animation-factory\SKILL.md` — RUNTIME_REGISTERED
- `ai-master` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\ai-master\SKILL.md` — RUNTIME_REGISTERED
- `ai-master-manager` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\ai-master-manager\SKILL.md` — RUNTIME_REGISTERED
- `ai-master-toolkit` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\ai-master-toolkit\SKILL.md` — RUNTIME_REGISTERED
- `ai-polish` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\ai-polish\SKILL.md` — RUNTIME_REGISTERED
- `ai-super-productivity-os` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\ai-super-productivity-os\SKILL.md` — RUNTIME_REGISTERED
- `animation-dream-factory` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\animation-dream-factory\SKILL.md` — RUNTIME_REGISTERED
- `animation-factory` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\animation-factory\SKILL.md` — RUNTIME_REGISTERED
- `api-gateway` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\api-gateway\SKILL.md` — RUNTIME_REGISTERED
- `asset-allocation-risk-review` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\asset-allocation-risk-review\SKILL.md` — RUNTIME_REGISTERED
- `best-minds` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\best-minds\SKILL.md` — RUNTIME_REGISTERED
- `brand-voice-system` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\brand-voice-system\SKILL.md` — RUNTIME_REGISTERED
- `browser-automation` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\browser-automation\SKILL.md` — RUNTIME_REGISTERED
- `browser-research-agent` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\browser-research-agent\SKILL.md` — RUNTIME_REGISTERED
- `business-dashboard-analyst` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\business-dashboard-analyst\SKILL.md` — RUNTIME_REGISTERED
- `code-review-ci` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\code-review-ci\SKILL.md` — RUNTIME_REGISTERED
- `coding-agent` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\coding-agent\SKILL.md` — RUNTIME_REGISTERED
- `content-repurposing` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\content-repurposing\SKILL.md` — RUNTIME_REGISTERED
- `content-rewrite` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\content-rewrite\SKILL.md` — RUNTIME_REGISTERED
- `content-scraper` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\content-scraper\SKILL.md` — RUNTIME_REGISTERED
- `context-engineering-agent` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\context-engineering-agent\SKILL.md` — RUNTIME_REGISTERED
- `course-design-agent` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\course-design-agent\SKILL.md` — RUNTIME_REGISTERED
- `docx-report-builder` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\docx-report-builder\SKILL.md` — RUNTIME_REGISTERED
- `editable-pptx-builder` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\editable-pptx-builder\SKILL.md` — RUNTIME_REGISTERED
- `enterprise-strategy-analysis` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\enterprise-strategy-analysis\SKILL.md` — RUNTIME_REGISTERED
- `finance-assistant` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\finance-assistant\SKILL.md` — RUNTIME_REGISTERED
- `financial-modeling` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\financial-modeling\SKILL.md` — RUNTIME_REGISTERED
- `financial-risk-literacy` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\financial-risk-literacy\SKILL.md` — RUNTIME_REGISTERED
- `hook-angle-lab` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\hook-angle-lab\SKILL.md` — RUNTIME_REGISTERED
- `humanizer` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\humanizer\SKILL.md` — RUNTIME_REGISTERED
- `insight` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\insight\SKILL.md` — RUNTIME_REGISTERED
- `investment-risk-review` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\investment-risk-review\SKILL.md` — RUNTIME_REGISTERED
- `knowledge-cards` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\knowledge-cards\SKILL.md` — RUNTIME_REGISTERED
- `knowledge-palace` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\knowledge-palace\SKILL.md` — RUNTIME_REGISTERED
- `last30days` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\last30days\SKILL.md` — RUNTIME_REGISTERED
- `lead-followup-automation` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\lead-followup-automation\SKILL.md` — RUNTIME_REGISTERED
- `learning-loop` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\learning-loop\SKILL.md` — RUNTIME_REGISTERED
- `maomao-animation-studio` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\maomao-animation-studio\SKILL.md` — RUNTIME_REGISTERED
- `maomao-ppt` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\maomao-ppt\SKILL.md` — RUNTIME_REGISTERED
- `maomao-skill-creator` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\maomao-skill-creator\SKILL.md` — RUNTIME_REGISTERED
- `maomao-thinking` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\maomao-thinking\SKILL.md` — RUNTIME_REGISTERED
- `market-monitoring` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\market-monitoring\SKILL.md` — RUNTIME_REGISTERED
- `market-research-analyst` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\market-research-analyst\SKILL.md` — RUNTIME_REGISTERED
- `mcp-builder` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\mcp-builder\SKILL.md` — RUNTIME_REGISTERED
- `meeting-notes-actions` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\meeting-notes-actions\SKILL.md` — RUNTIME_REGISTERED
- `memory-boost` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\memory-boost\SKILL.md` — RUNTIME_REGISTERED
- `mimeng-topic-method` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\mimeng-topic-method\SKILL.md` — RUNTIME_REGISTERED
- `multi-agent-orchestrator` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\multi-agent-orchestrator\SKILL.md` — RUNTIME_REGISTERED
- `notes-research` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\notes-research\SKILL.md` — RUNTIME_REGISTERED
- `obsidian` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\obsidian\SKILL.md` — RUNTIME_REGISTERED
- `original-writing` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\original-writing\SKILL.md` — RUNTIME_REGISTERED
- `personal-investment-workflow` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\personal-investment-workflow\SKILL.md` — RUNTIME_REGISTERED
- `proactive-agent` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\proactive-agent\SKILL.md` — RUNTIME_REGISTERED
- `quant-trading-literacy` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\quant-trading-literacy\SKILL.md` — RUNTIME_REGISTERED
- `repo-context-compiler` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\repo-context-compiler\SKILL.md` — RUNTIME_REGISTERED
- `research-to-article` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\research-to-article\SKILL.md` — RUNTIME_REGISTERED
- `self-improvement` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\self-improvement\SKILL.md` — RUNTIME_REGISTERED
- `short-video-script-lab` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\short-video-script-lab\SKILL.md` — RUNTIME_REGISTERED
- `skill-creator` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\skill-creator\SKILL.md` — RUNTIME_REGISTERED
- `skill-finder` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\skill-finder\SKILL.md` — RUNTIME_REGISTERED
- `skill-vetter` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\skill-vetter\SKILL.md` — RUNTIME_REGISTERED
- `social-media-strategy` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\social-media-strategy\SKILL.md` — RUNTIME_REGISTERED
- `sonoscli` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\sonoscli\SKILL.md` — RUNTIME_REGISTERED
- `spreadsheet-analyst` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\spreadsheet-analyst\SKILL.md` — RUNTIME_REGISTERED
- `video-account-analysis` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\video-account-analysis\SKILL.md` — RUNTIME_REGISTERED
- `video-transcribe` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\video-transcribe\SKILL.md` — RUNTIME_REGISTERED
- `wealth-advisor` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\wealth-advisor\SKILL.md` — RUNTIME_REGISTERED
- `web-story` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\web-story\SKILL.md` — RUNTIME_REGISTERED
- `wechat-mp-auto` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\wechat-mp-auto\SKILL.md` — RUNTIME_REGISTERED
- `workflow-automation-builder` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\workflow-automation-builder\SKILL.md` — RUNTIME_REGISTERED
- `xiaohongshu-auto` — `C:\Users\MECHREVO\Desktop\skills 库_副本\Codex技能备份_2026-09-09\现有技能_完整备份\xiaohongshu-auto\SKILL.md` — RUNTIME_REGISTERED

## 当前工具与员工能力

| 员工/工具 | 职能 | 状态 | 证据 |
|---|---|---|---|
