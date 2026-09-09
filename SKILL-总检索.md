# 茂茂 Skill 总检索

> 自动生成时间：2026-09-06T12:12:52.338269+00:00
> 机器可读正本：`skills-catalog.json`
> 重建命令：`python3 build_skill_catalog.py`

## 使用规则

1. 总经理开工前先读 `skills-catalog.json`，按目标语义选择 Skill，不靠用户记关键词。
2. `RUNTIME_REGISTERED` 表示已有 Codex 运行入口；`VISIBLE_ONLY` 只表示桌面资料存在，不能冒充可执行。
3. 同一 Skill 有多个桌面副本时，以 `runtime_path` 指向的正本为准。

## 运行入口

| 名称 | 调用 | 运行正本 | 状态 |
|---|---|---|---|
| imagegen | `$imagegen` | `/Users/xingxuan/.codex/skills/.system/imagegen/SKILL.md` | RUNTIME_REGISTERED |
| openai-docs | `$openai-docs` | `/Users/xingxuan/.codex/skills/.system/openai-docs/SKILL.md` | RUNTIME_REGISTERED |
| plugin-creator | `$plugin-creator` | `/Users/xingxuan/.codex/skills/.system/plugin-creator/SKILL.md` | RUNTIME_REGISTERED |
| review-agent | `$review-agent` | `/Users/xingxuan/.codex/skills/.system/review-agent/SKILL.md` | RUNTIME_REGISTERED |
| skill-creator | `$skill-creator` | `/Users/xingxuan/.codex/skills/.system/skill-creator/SKILL.md` | RUNTIME_REGISTERED |
| skill-installer | `$skill-installer` | `/Users/xingxuan/.codex/skills/.system/skill-installer/SKILL.md` | RUNTIME_REGISTERED |
| active-agent | `$active-agent` | `/Users/xingxuan/.codex/skills/active-agent/SKILL.md` | RUNTIME_REGISTERED |
| ad-copywriting | `$ad-copywriting` | `/Users/xingxuan/.codex/skills/ad-copywriting/SKILL.md` | RUNTIME_REGISTERED |
| advanced-xhs-visual-design | `$advanced-xhs-visual-design` | `/Users/xingxuan/.codex/skills/advanced-xhs-visual-design/SKILL.md` | RUNTIME_REGISTERED |
| agent-eval-loop | `$agent-eval-loop` | `/Users/xingxuan/.codex/skills/agent-eval-loop/SKILL.md` | RUNTIME_REGISTERED |
| ai-animation-factory | `$ai-animation-factory` | `/Users/xingxuan/.codex/skills/ai-animation-factory/SKILL.md` | RUNTIME_REGISTERED |
| ai-master | `$ai-master` | `/Users/xingxuan/.codex/skills/ai-master/SKILL.md` | RUNTIME_REGISTERED |
| ai-master-manager | `$ai-master-manager` | `/Users/xingxuan/.codex/skills/ai-master-manager/SKILL.md` | RUNTIME_REGISTERED |
| ai-master-toolkit | `$ai-master-toolkit` | `/Users/xingxuan/.codex/skills/ai-master-toolkit/SKILL.md` | RUNTIME_REGISTERED |
| ai-polish | `$ai-polish` | `/Users/xingxuan/.codex/skills/ai-polish/SKILL.md` | RUNTIME_REGISTERED |
| ai-task-compiler | `$ai-task-compiler` | `/Users/xingxuan/.codex/skills/ai-task-compiler/SKILL.md` | RUNTIME_REGISTERED |
| animation-dream-factory | `$animation-dream-factory` | `/Users/xingxuan/.codex/skills/animation-dream-factory/SKILL.md` | RUNTIME_REGISTERED |
| animation-factory | `$animation-factory` | `/Users/xingxuan/.codex/skills/animation-factory/SKILL.md` | RUNTIME_REGISTERED |
| api-gateway | `$api-gateway` | `/Users/xingxuan/.codex/skills/api-gateway/SKILL.md` | RUNTIME_REGISTERED |
| asset-allocation-risk-review | `$asset-allocation-risk-review` | `/Users/xingxuan/.codex/skills/asset-allocation-risk-review/SKILL.md` | RUNTIME_REGISTERED |
| best-minds | `$best-minds` | `/Users/xingxuan/.codex/skills/best-minds/SKILL.md` | RUNTIME_REGISTERED |
| better-accessibility | `$better-accessibility` | `/Users/xingxuan/.codex/skills/better-accessibility/SKILL.md` | RUNTIME_REGISTERED |
| better-colors | `$better-colors` | `/Users/xingxuan/.codex/skills/better-colors/SKILL.md` | RUNTIME_REGISTERED |
| better-interface | `$better-interface` | `/Users/xingxuan/.codex/skills/better-interface/SKILL.md` | RUNTIME_REGISTERED |
| better-layout | `$better-layout` | `/Users/xingxuan/.codex/skills/better-layout/SKILL.md` | RUNTIME_REGISTERED |
| better-typography | `$better-typography` | `/Users/xingxuan/.codex/skills/better-typography/SKILL.md` | RUNTIME_REGISTERED |
| better-ui | `$better-ui` | `/Users/xingxuan/.codex/skills/better-ui/SKILL.md` | RUNTIME_REGISTERED |
| better-writing | `$better-writing` | `/Users/xingxuan/.codex/skills/better-writing/SKILL.md` | RUNTIME_REGISTERED |
| brand-voice-system | `$brand-voice-system` | `/Users/xingxuan/.codex/skills/brand-voice-system/SKILL.md` | RUNTIME_REGISTERED |
| break | `$break` | `/Users/xingxuan/.codex/skills/break/SKILL.md` | RUNTIME_REGISTERED |
| browser-automation | `$browser-automation` | `/Users/xingxuan/.codex/skills/browser-automation/SKILL.md` | RUNTIME_REGISTERED |
| browser-research-agent | `$browser-research-agent` | `/Users/xingxuan/.codex/skills/browser-research-agent/SKILL.md` | RUNTIME_REGISTERED |
| business-dashboard-analyst | `$business-dashboard-analyst` | `/Users/xingxuan/.codex/skills/business-dashboard-analyst/SKILL.md` | RUNTIME_REGISTERED |
| code-review-ci | `$code-review-ci` | `/Users/xingxuan/.codex/skills/code-review-ci/SKILL.md` | RUNTIME_REGISTERED |
| coding-agent | `$coding-agent` | `/Users/xingxuan/.codex/skills/coding-agent/SKILL.md` | RUNTIME_REGISTERED |
| content-repurposing | `$content-repurposing` | `/Users/xingxuan/.codex/skills/content-repurposing/SKILL.md` | RUNTIME_REGISTERED |
| content-rewrite | `$content-rewrite` | `/Users/xingxuan/.codex/skills/content-rewrite/SKILL.md` | RUNTIME_REGISTERED |
| content-scraper | `$content-scraper` | `/Users/xingxuan/.codex/skills/content-scraper/SKILL.md` | RUNTIME_REGISTERED |
| context-engineering-agent | `$context-engineering-agent` | `/Users/xingxuan/.codex/skills/context-engineering-agent/SKILL.md` | RUNTIME_REGISTERED |
| cool-webpage | `$cool-webpage` | `/Users/xingxuan/.codex/skills/cool-webpage/SKILL.md` | RUNTIME_REGISTERED |
| course-design-agent | `$course-design-agent` | `/Users/xingxuan/.codex/skills/course-design-agent/SKILL.md` | RUNTIME_REGISTERED |
| dan-koe-inspired-writing | `$dan-koe-inspired-writing` | `/Users/xingxuan/.codex/skills/dan-koe-inspired-writing/SKILL.md` | RUNTIME_REGISTERED |
| docx-report-builder | `$docx-report-builder` | `/Users/xingxuan/.codex/skills/docx-report-builder/SKILL.md` | RUNTIME_REGISTERED |
| dynamic-data | `$dynamic-data` | `/Users/xingxuan/.codex/skills/dynamic-data/SKILL.md` | RUNTIME_REGISTERED |
| dynamic-memory | `$dynamic-memory` | `/Users/xingxuan/.codex/skills/dynamic-memory/SKILL.md` | RUNTIME_REGISTERED |
| editable-pptx-builder | `$editable-pptx-builder` | `/Users/xingxuan/.codex/skills/editable-pptx-builder/SKILL.md` | RUNTIME_REGISTERED |
| elegant-style | `$elegant-style` | `/Users/xingxuan/.codex/skills/elegant-style/SKILL.md` | RUNTIME_REGISTERED |
| enterprise-strategy-analysis | `$enterprise-strategy-analysis` | `/Users/xingxuan/.codex/skills/enterprise-strategy-analysis/SKILL.md` | RUNTIME_REGISTERED |
| explain-interface | `$explain-interface` | `/Users/xingxuan/.codex/skills/explain-interface/SKILL.md` | RUNTIME_REGISTERED |
| falling-leaves | `$falling-leaves` | `/Users/xingxuan/.codex/skills/falling-leaves/SKILL.md` | RUNTIME_REGISTERED |
| finance-assistant | `$finance-assistant` | `/Users/xingxuan/.codex/skills/finance-assistant/SKILL.md` | RUNTIME_REGISTERED |
| financial-modeling | `$financial-modeling` | `/Users/xingxuan/.codex/skills/financial-modeling/SKILL.md` | RUNTIME_REGISTERED |
| financial-risk-literacy | `$financial-risk-literacy` | `/Users/xingxuan/.codex/skills/financial-risk-literacy/SKILL.md` | RUNTIME_REGISTERED |
| grok-marketing-bots | `$grok-marketing-bots` | `/Users/xingxuan/.codex/skills/grok-marketing-bots/SKILL.md` | RUNTIME_REGISTERED |
| hook-angle-lab | `$hook-angle-lab` | `/Users/xingxuan/.codex/skills/hook-angle-lab/SKILL.md` | RUNTIME_REGISTERED |
| hot-interview-radar | `$hot-interview-radar` | `/Users/xingxuan/.codex/skills/hot-interview-radar/SKILL.md` | RUNTIME_REGISTERED |
| humanizer | `$humanizer` | `/Users/xingxuan/.codex/skills/humanizer/SKILL.md` | RUNTIME_REGISTERED |
| insight | `$insight` | `/Users/xingxuan/.codex/skills/insight/SKILL.md` | RUNTIME_REGISTERED |
| interface-review | `$interface-review` | `/Users/xingxuan/.codex/skills/interface-review/SKILL.md` | RUNTIME_REGISTERED |
| investment-risk-review | `$investment-risk-review` | `/Users/xingxuan/.codex/skills/investment-risk-review/SKILL.md` | RUNTIME_REGISTERED |
| knowledge-cards | `$knowledge-cards` | `/Users/xingxuan/.codex/skills/knowledge-cards/SKILL.md` | RUNTIME_REGISTERED |
| knowledge-palace | `$knowledge-palace` | `/Users/xingxuan/.codex/skills/knowledge-palace/SKILL.md` | RUNTIME_REGISTERED |
| last30days | `$last30days` | `/Users/xingxuan/.codex/skills/last30days/SKILL.md` | RUNTIME_REGISTERED |
| lead-followup-automation | `$lead-followup-automation` | `/Users/xingxuan/.codex/skills/lead-followup-automation/SKILL.md` | RUNTIME_REGISTERED |
| learning-loop | `$learning-loop` | `/Users/xingxuan/.codex/skills/learning-loop/SKILL.md` | RUNTIME_REGISTERED |
| market-monitoring | `$market-monitoring` | `/Users/xingxuan/.codex/skills/market-monitoring/SKILL.md` | RUNTIME_REGISTERED |
| market-research-analyst | `$market-research-analyst` | `/Users/xingxuan/.codex/skills/market-research-analyst/SKILL.md` | RUNTIME_REGISTERED |
| mcp-builder | `$mcp-builder` | `/Users/xingxuan/.codex/skills/mcp-builder/SKILL.md` | RUNTIME_REGISTERED |
| meeting-notes-actions | `$meeting-notes-actions` | `/Users/xingxuan/.codex/skills/meeting-notes-actions/SKILL.md` | RUNTIME_REGISTERED |
| memory-boost | `$memory-boost` | `/Users/xingxuan/.codex/skills/memory-boost/SKILL.md` | RUNTIME_REGISTERED |
| mimeng-topic-method | `$mimeng-topic-method` | `/Users/xingxuan/.codex/skills/mimeng-topic-method/SKILL.md` | RUNTIME_REGISTERED |
| multi-agent-orchestrator | `$multi-agent-orchestrator` | `/Users/xingxuan/.codex/skills/multi-agent-orchestrator/SKILL.md` | RUNTIME_REGISTERED |
| notes-research | `$notes-research` | `/Users/xingxuan/.codex/skills/notes-research/SKILL.md` | RUNTIME_REGISTERED |
| novel-art | `$novel-art` | `/Users/xingxuan/.codex/skills/novel-art/SKILL.md` | RUNTIME_REGISTERED |
| novel-characters | `$novel-characters` | `/Users/xingxuan/.codex/skills/novel-characters/SKILL.md` | RUNTIME_REGISTERED |
| novel-outline | `$novel-outline` | `/Users/xingxuan/.codex/skills/novel-outline/SKILL.md` | RUNTIME_REGISTERED |
| novel-script | `$novel-script` | `/Users/xingxuan/.codex/skills/novel-script/SKILL.md` | RUNTIME_REGISTERED |
| novel-storyboard | `$novel-storyboard` | `/Users/xingxuan/.codex/skills/novel-storyboard/SKILL.md` | RUNTIME_REGISTERED |
| obsidian | `$obsidian` | `/Users/xingxuan/.codex/skills/obsidian/SKILL.md` | RUNTIME_REGISTERED |
| original-writing | `$original-writing` | `/Users/xingxuan/.codex/skills/original-writing/SKILL.md` | RUNTIME_REGISTERED |
| personal-investment-workflow | `$personal-investment-workflow` | `/Users/xingxuan/.codex/skills/personal-investment-workflow/SKILL.md` | RUNTIME_REGISTERED |
| proactive-agent | `$proactive-agent` | `/Users/xingxuan/.codex/skills/proactive-agent/SKILL.md` | RUNTIME_REGISTERED |
| quant-trading-literacy | `$quant-trading-literacy` | `/Users/xingxuan/.codex/skills/quant-trading-literacy/SKILL.md` | RUNTIME_REGISTERED |
| repo-context-compiler | `$repo-context-compiler` | `/Users/xingxuan/.codex/skills/repo-context-compiler/SKILL.md` | RUNTIME_REGISTERED |
| research-to-article | `$research-to-article` | `/Users/xingxuan/.codex/skills/research-to-article/SKILL.md` | RUNTIME_REGISTERED |
| self-improvement | `$self-improvement` | `/Users/xingxuan/.codex/skills/self-improvement/SKILL.md` | RUNTIME_REGISTERED |
| short-video-script-lab | `$short-video-script-lab` | `/Users/xingxuan/.codex/skills/short-video-script-lab/SKILL.md` | RUNTIME_REGISTERED |
| skill-finder | `$skill-finder` | `/Users/xingxuan/.codex/skills/skill-finder/SKILL.md` | RUNTIME_REGISTERED |
| skill-vetter | `$skill-vetter` | `/Users/xingxuan/.codex/skills/skill-vetter/SKILL.md` | RUNTIME_REGISTERED |
| social-media-strategy | `$social-media-strategy` | `/Users/xingxuan/.codex/skills/social-media-strategy/SKILL.md` | RUNTIME_REGISTERED |
| songwriting-and-ai-music | `$songwriting-and-ai-music` | `/Users/xingxuan/.codex/skills/songwriting-and-ai-music/SKILL.md` | RUNTIME_REGISTERED |
| sonoscli | `$sonoscli` | `/Users/xingxuan/.codex/skills/sonoscli/SKILL.md` | RUNTIME_REGISTERED |
| spreadsheet-analyst | `$spreadsheet-analyst` | `/Users/xingxuan/.codex/skills/spreadsheet-analyst/SKILL.md` | RUNTIME_REGISTERED |
| suno-songwriter | `$suno-songwriter` | `/Users/xingxuan/.codex/skills/suno-songwriter/SKILL.md` | RUNTIME_REGISTERED |
| variant | `$variant` | `/Users/xingxuan/.codex/skills/variant/SKILL.md` | RUNTIME_REGISTERED |
| video-account-analysis | `$video-account-analysis` | `/Users/xingxuan/.codex/skills/video-account-analysis/SKILL.md` | RUNTIME_REGISTERED |
| video-transcribe | `$video-transcribe` | `/Users/xingxuan/.codex/skills/video-transcribe/SKILL.md` | RUNTIME_REGISTERED |
| visual-moment | `$visual-moment` | `/Users/xingxuan/.codex/skills/visual-moment/SKILL.md` | RUNTIME_REGISTERED |
| wealth-advisor | `$wealth-advisor` | `/Users/xingxuan/.codex/skills/wealth-advisor/SKILL.md` | RUNTIME_REGISTERED |
| web-story | `$web-story` | `/Users/xingxuan/.codex/skills/web-story/SKILL.md` | RUNTIME_REGISTERED |
| wechat-content-pipeline | `$wechat-content-pipeline` | `/Users/xingxuan/.codex/skills/wechat-content-pipeline/SKILL.md` | RUNTIME_REGISTERED |
| wechat-mp-auto | `$wechat-mp-auto` | `/Users/xingxuan/.codex/skills/wechat-mp-auto/SKILL.md` | RUNTIME_REGISTERED |
| workflow-automation-builder | `$workflow-automation-builder` | `/Users/xingxuan/.codex/skills/workflow-automation-builder/SKILL.md` | RUNTIME_REGISTERED |
| xiaohongshu-auto | `$xiaohongshu-auto` | `/Users/xingxuan/.codex/skills/xiaohongshu-auto/SKILL.md` | RUNTIME_REGISTERED |
| xiaohongshu-conversion-path | `$xiaohongshu-conversion-path` | `/Users/xingxuan/.codex/skills/xiaohongshu-conversion-path/SKILL.md` | RUNTIME_REGISTERED |
| xiaohongshu-profile | `$xiaohongshu-profile` | `/Users/xingxuan/.codex/skills/xiaohongshu-profile/SKILL.md` | RUNTIME_REGISTERED |
| xiaohongshu-topic-planner | `$xiaohongshu-topic-planner` | `/Users/xingxuan/.codex/skills/xiaohongshu-topic-planner/SKILL.md` | RUNTIME_REGISTERED |
| xingye-music-company | `$xingye-music-company` | `/Users/xingxuan/.codex/skills/xingye-music-company/SKILL.md` | RUNTIME_REGISTERED |
| xingye-web-company | `$xingye-web-company` | `/Users/xingxuan/.codex/skills/xingye-web-company/SKILL.md` | RUNTIME_REGISTERED |
| xingye-wechat-writer-company | `$xingye-wechat-writer-company` | `/Users/xingxuan/.codex/skills/xingye-wechat-writer-company/SKILL.md` | RUNTIME_REGISTERED |
| maomao-animation-studio | `$maomao-animation-studio` | `/Users/xingxuan/.codex/skills/maomao-animation-studio/SKILL.md` | RUNTIME_REGISTERED |
| maomao-expression-coach | `$maomao-expression-coach` | `/Users/xingxuan/.codex/skills/maomao-expression-coach/SKILL.md` | RUNTIME_REGISTERED |
| maomao-multi-ai-production | `$maomao-multi-ai-production` | `/Users/xingxuan/.codex/skills/maomao-multi-ai-production/SKILL.md` | RUNTIME_REGISTERED |
| maomao-ppt | `$maomao-ppt` | `/Users/xingxuan/.codex/skills/maomao-ppt/SKILL.md` | RUNTIME_REGISTERED |
| maomao-screenshot-news-video | `$maomao-screenshot-news-video` | `/Users/xingxuan/.codex/skills/maomao-screenshot-news-video/SKILL.md` | RUNTIME_REGISTERED |
| maomao-skill-creator | `$maomao-skill-creator` | `/Users/xingxuan/.codex/skills/maomao-skill-creator/SKILL.md` | RUNTIME_REGISTERED |
| maomao-thinking | `$maomao-thinking` | `/Users/xingxuan/.codex/skills/maomao-thinking/SKILL.md` | RUNTIME_REGISTERED |
| maomao-x-evidence-collector | `$maomao-x-evidence-collector` | `/Users/xingxuan/.codex/skills/maomao-x-evidence-collector/SKILL.md` | RUNTIME_REGISTERED |

## 桌面资料条目

- `context-engineering-agent` — `/Users/xingxuan/Desktop/skills 库/01-AI增强/上下文工程代理（context-engineering-agent）/SKILL.md` — RUNTIME_REGISTERED
- `proactive-agent` — `/Users/xingxuan/Desktop/skills 库/01-AI增强/主动型代理（proactive-agent）/SKILL.md` — RUNTIME_REGISTERED
- `active-agent` — `/Users/xingxuan/Desktop/skills 库/01-AI增强/主动执行代理（active-agent）/SKILL.md` — RUNTIME_REGISTERED
- `agent-eval-loop` — `/Users/xingxuan/Desktop/skills 库/01-AI增强/代理评测闭环（agent-eval-loop）/SKILL.md` — RUNTIME_REGISTERED
- `multi-agent-orchestrator` — `/Users/xingxuan/Desktop/skills 库/01-AI增强/多代理协作编排（multi-agent-orchestrator）/SKILL.md` — RUNTIME_REGISTERED
- `ai-master-manager` — `/Users/xingxuan/Desktop/skills 库/01-AI增强/总经理入口（ai-master-manager）/SKILL.md` — RUNTIME_REGISTERED
- `ai-master-toolkit` — `/Users/xingxuan/Desktop/skills 库/01-AI增强/总经理能力工具箱（ai-master-toolkit）/SKILL.md` — RUNTIME_REGISTERED
- `ai-master` — `/Users/xingxuan/Desktop/skills 库/01-AI增强/总经理（ai-master）/SKILL.md` — RUNTIME_REGISTERED
- `skill-finder` — `/Users/xingxuan/Desktop/skills 库/01-AI增强/技能发现与选型（skill-finder）/SKILL.md` — RUNTIME_REGISTERED
- `best-minds` — `/Users/xingxuan/Desktop/skills 库/01-AI增强/最强大脑（best-minds）/SKILL.md` — RUNTIME_REGISTERED
- `self-improvement` — `/Users/xingxuan/Desktop/skills 库/01-AI增强/自我优化代理（self-improving-agent）/SKILL.md` — RUNTIME_REGISTERED
- `ai-animation-factory` — `/Users/xingxuan/Desktop/skills 库/02-内容创作/AI动画工厂（ai-animation-factory）/SKILL.md` — RUNTIME_REGISTERED
- `content-repurposing` — `/Users/xingxuan/Desktop/skills 库/02-内容创作/内容矩阵复用（content-repurposing）/SKILL.md` — RUNTIME_REGISTERED
- `animation-factory` — `/Users/xingxuan/Desktop/skills 库/02-内容创作/动画工厂（animation-factory）/SKILL.md` — RUNTIME_REGISTERED
- `animation-dream-factory` — `/Users/xingxuan/Desktop/skills 库/02-内容创作/动画梦工厂（animation-dream-factory）/SKILL.md` — RUNTIME_REGISTERED
- `original-writing` — `/Users/xingxuan/Desktop/skills 库/02-内容创作/原创长文（original-writing）/SKILL.md` — RUNTIME_REGISTERED
- `ai-polish` — `/Users/xingxuan/Desktop/skills 库/02-内容创作/去AI味润色（ai-polish）/SKILL.md` — RUNTIME_REGISTERED
- `humanizer` — `/Users/xingxuan/Desktop/skills 库/02-内容创作/去AI味英文版（humanizer）/SKILL.md` — RUNTIME_REGISTERED
- `mimeng-topic-method` — `/Users/xingxuan/Desktop/skills 库/02-内容创作/咪蒙选题法（mimeng-topic-method）/SKILL.md` — RUNTIME_REGISTERED
- `brand-voice-system` — `/Users/xingxuan/Desktop/skills 库/02-内容创作/品牌声纹系统（brand-voice-system）/SKILL.md` — RUNTIME_REGISTERED
- `ad-copywriting` — `/Users/xingxuan/Desktop/skills 库/02-内容创作/商单文案写作（ad-copywriting）/SKILL.md` — RUNTIME_REGISTERED
- `content-rewrite` — `/Users/xingxuan/Desktop/skills 库/02-内容创作/改稿（content-rewrite）/SKILL.md` — RUNTIME_REGISTERED
- `maomao-animation-studio` — `/Users/xingxuan/Desktop/skills 库/02-内容创作/茂茂动画工厂（maomao-animation-studio）/SKILL.md` — RUNTIME_REGISTERED
- `last30days` — `/Users/xingxuan/Desktop/skills 库/02-内容创作/最近30天（last30days）/SKILL.md` — RUNTIME_REGISTERED
- `research-to-article` — `/Users/xingxuan/Desktop/skills 库/02-内容创作/调研成稿（research-to-article）/SKILL.md` — RUNTIME_REGISTERED
- `hook-angle-lab` — `/Users/xingxuan/Desktop/skills 库/02-内容创作/选题钩子实验室（hook-angle-lab）/SKILL.md` — RUNTIME_REGISTERED
- `advanced-xhs-visual-design` — `/Users/xingxuan/Desktop/skills 库/02-内容创作/高级图文设计（advanced-xhs-visual-design）/SKILL.md` — RUNTIME_REGISTERED
- `api-gateway` — `/Users/xingxuan/Desktop/skills 库/03-开发工具/API网关（api-gateway）/SKILL.md` — RUNTIME_REGISTERED
- `mcp-builder` — `/Users/xingxuan/Desktop/skills 库/03-开发工具/MCP构建器（mcp-builder）/SKILL.md` — RUNTIME_REGISTERED
- `repo-context-compiler` — `/Users/xingxuan/Desktop/skills 库/03-开发工具/仓库上下文编译器（repo-context-compiler）/SKILL.md` — RUNTIME_REGISTERED
- `code-review-ci` — `/Users/xingxuan/Desktop/skills 库/03-开发工具/代码评审与CI修复（code-review-ci）/SKILL.md` — RUNTIME_REGISTERED
- `skill-creator` — `/Users/xingxuan/Desktop/skills 库/03-开发工具/技能创建器（skill-creator）/SKILL.md` — RUNTIME_REGISTERED
- `skill-vetter` — `/Users/xingxuan/Desktop/skills 库/03-开发工具/技能安全审查（skill-vetter）/SKILL.md` — RUNTIME_REGISTERED
- `coding-agent` — `/Users/xingxuan/Desktop/skills 库/03-开发工具/编程代理（coding-agent）/SKILL.md` — RUNTIME_REGISTERED
- `web-story` — `/Users/xingxuan/Desktop/skills 库/03-开发工具/网页故事（web-story）/SKILL.md` — RUNTIME_REGISTERED
- `content-scraper` — `/Users/xingxuan/Desktop/skills 库/04-浏览器自动化/内容抓取（content-scraper）/SKILL.md` — RUNTIME_REGISTERED
- `browser-automation` — `/Users/xingxuan/Desktop/skills 库/04-浏览器自动化/浏览器自动化（browser-automation）/SKILL.md` — RUNTIME_REGISTERED
- `browser-research-agent` — `/Users/xingxuan/Desktop/skills 库/04-浏览器自动化/浏览器调研代理（browser-research-agent）/SKILL.md` — RUNTIME_REGISTERED
- `lead-followup-automation` — `/Users/xingxuan/Desktop/skills 库/04-浏览器自动化/线索跟进自动化（lead-followup-automation）/SKILL.md` — RUNTIME_REGISTERED
- `video-transcribe` — `/Users/xingxuan/Desktop/skills 库/04-浏览器自动化/视频转写（video-transcribe）/SKILL.md` — RUNTIME_REGISTERED
- `wechat-mp-auto` — `/Users/xingxuan/Desktop/skills 库/05-社交媒体/公众号自动化（wechat-mp-auto）/SKILL.md` — RUNTIME_REGISTERED
- `video-account-analysis` — `/Users/xingxuan/Desktop/skills 库/05-社交媒体/微信视频号分析（video-account-analysis）/SKILL.md` — RUNTIME_REGISTERED
- `short-video-script-lab` — `/Users/xingxuan/Desktop/skills 库/05-社交媒体/短视频脚本工坊（short-video-script-lab）/SKILL.md` — RUNTIME_REGISTERED
- `social-media-strategy` — `/Users/xingxuan/Desktop/skills 库/05-社交媒体/社媒策略分析（social-media-strategy）/SKILL.md` — RUNTIME_REGISTERED
- `xiaohongshu-auto` — `/Users/xingxuan/Desktop/skills 库/05-社交媒体/自动发小红书（xiaohongshu-auto）/SKILL.md` — RUNTIME_REGISTERED
- `meeting-notes-actions` — `/Users/xingxuan/Desktop/skills 库/06-知识与学习/会议纪要行动项（meeting-notes-actions）/SKILL.md` — RUNTIME_REGISTERED
- `learning-loop` — `/Users/xingxuan/Desktop/skills 库/06-知识与学习/学习闭环（learning-loop）/SKILL.md` — RUNTIME_REGISTERED
- `maomao-thinking` — `/Users/xingxuan/Desktop/skills 库/06-知识与学习/茂茂商业思考（maomao-thinking）/SKILL.md` — RUNTIME_REGISTERED
- `insight` — `/Users/xingxuan/Desktop/skills 库/06-知识与学习/洞察（insight）/SKILL.md` — RUNTIME_REGISTERED
- `知识卡片` — `/Users/xingxuan/Desktop/skills 库/06-知识与学习/知识卡片（knowledge-cards）/SKILL.md` — VISIBLE_ONLY
- `knowledge-palace` — `/Users/xingxuan/Desktop/skills 库/06-知识与学习/知识宫殿（knowledge-palace）/SKILL.md` — RUNTIME_REGISTERED
- `notes-research` — `/Users/xingxuan/Desktop/skills 库/06-知识与学习/笔记研究助手（notes-research）/SKILL.md` — RUNTIME_REGISTERED
- `memory-boost` — `/Users/xingxuan/Desktop/skills 库/06-知识与学习/记忆增强（memory-boost）/SKILL.md` — RUNTIME_REGISTERED
- `course-design-agent` — `/Users/xingxuan/Desktop/skills 库/06-知识与学习/课程设计代理（course-design-agent）/SKILL.md` — RUNTIME_REGISTERED
- `obsidian` — `/Users/xingxuan/Desktop/skills 库/07-效率工具/Obsidian笔记（obsidian）/SKILL.md` — RUNTIME_REGISTERED
- `sonoscli` — `/Users/xingxuan/Desktop/skills 库/07-效率工具/办公协同（sonoscli）/SKILL.md` — RUNTIME_REGISTERED
- `editable-pptx-builder` — `/Users/xingxuan/Desktop/skills 库/07-效率工具/可编辑PPT生成（editable-pptx-builder）/SKILL.md` — RUNTIME_REGISTERED
- `workflow-automation-builder` — `/Users/xingxuan/Desktop/skills 库/07-效率工具/工作流自动化搭建（workflow-automation-builder）/SKILL.md` — RUNTIME_REGISTERED
- `docx-report-builder` — `/Users/xingxuan/Desktop/skills 库/07-效率工具/报告文档生成（docx-report-builder）/SKILL.md` — RUNTIME_REGISTERED
- `maomao-ppt` — `/Users/xingxuan/Desktop/skills 库/07-效率工具/茂茂PPT（maomao-ppt）/SKILL.md` — RUNTIME_REGISTERED
- `market-research-analyst` — `/Users/xingxuan/Desktop/skills 库/08-数据分析/市场调研分析（market-research-analyst）/SKILL.md` — RUNTIME_REGISTERED
- `business-dashboard-analyst` — `/Users/xingxuan/Desktop/skills 库/08-数据分析/经营仪表盘分析（business-dashboard-analyst）/SKILL.md` — RUNTIME_REGISTERED
- `spreadsheet-analyst` — `/Users/xingxuan/Desktop/skills 库/08-数据分析/表格分析助手（spreadsheet-analyst）/SKILL.md` — RUNTIME_REGISTERED
- `finance-assistant` — `/Users/xingxuan/Desktop/skills 库/08-数据分析/财务分析助手（finance-assistant）/SKILL.md` — RUNTIME_REGISTERED
- `asset-allocation-risk-review` — `/Users/xingxuan/Desktop/skills 库/08-数据分析/资产配置风险复盘（asset-allocation-risk-review）/SKILL.md` — RUNTIME_REGISTERED
- `financial-risk-literacy` — `/Users/xingxuan/Desktop/skills 库/08-数据分析/金融风险识别（financial-risk-literacy）/SKILL.md` — RUNTIME_REGISTERED
- `personal-investment-workflow` — `/Users/xingxuan/Desktop/skills 库/09-金融/个人投资工作流（personal-investment-workflow）/SKILL.md` — RUNTIME_REGISTERED
- `enterprise-strategy-analysis` — `/Users/xingxuan/Desktop/skills 库/09-金融/企业策略分析（enterprise-strategy-analysis）/SKILL.md` — RUNTIME_REGISTERED
- `investment-risk-review` — `/Users/xingxuan/Desktop/skills 库/09-金融/投资风险辨析（investment-risk-review）/SKILL.md` — RUNTIME_REGISTERED
- `market-monitoring` — `/Users/xingxuan/Desktop/skills 库/09-金融/看盘盯盘（market-monitoring）/SKILL.md` — RUNTIME_REGISTERED
- `financial-modeling` — `/Users/xingxuan/Desktop/skills 库/09-金融/财务建模（financial-modeling）/SKILL.md` — RUNTIME_REGISTERED
- `wealth-advisor` — `/Users/xingxuan/Desktop/skills 库/09-金融/财富顾问（wealth-advisor）/SKILL.md` — RUNTIME_REGISTERED
- `quant-trading-literacy` — `/Users/xingxuan/Desktop/skills 库/09-金融/量化交易认知（quant-trading-literacy）/SKILL.md` — RUNTIME_REGISTERED
- `context-engineering-agent` — `/Users/xingxuan/Desktop/skills 库/网站制作/01-AI增强/上下文工程代理（context-engineering-agent）/SKILL.md` — RUNTIME_REGISTERED
- `proactive-agent` — `/Users/xingxuan/Desktop/skills 库/网站制作/01-AI增强/主动型代理（proactive-agent）/SKILL.md` — RUNTIME_REGISTERED
- `active-agent` — `/Users/xingxuan/Desktop/skills 库/网站制作/01-AI增强/主动执行代理（active-agent）/SKILL.md` — RUNTIME_REGISTERED
- `agent-eval-loop` — `/Users/xingxuan/Desktop/skills 库/网站制作/01-AI增强/代理评测闭环（agent-eval-loop）/SKILL.md` — RUNTIME_REGISTERED
- `multi-agent-orchestrator` — `/Users/xingxuan/Desktop/skills 库/网站制作/01-AI增强/多代理协作编排（multi-agent-orchestrator）/SKILL.md` — RUNTIME_REGISTERED
- `skill-finder` — `/Users/xingxuan/Desktop/skills 库/网站制作/01-AI增强/技能发现与选型（skill-finder）/SKILL.md` — RUNTIME_REGISTERED
- `best-minds` — `/Users/xingxuan/Desktop/skills 库/网站制作/01-AI增强/最强大脑（best-minds）/SKILL.md` — RUNTIME_REGISTERED
- `self-improvement` — `/Users/xingxuan/Desktop/skills 库/网站制作/01-AI增强/自我优化代理（self-improving-agent）/SKILL.md` — RUNTIME_REGISTERED
- `content-repurposing` — `/Users/xingxuan/Desktop/skills 库/网站制作/02-内容创作/内容矩阵复用（content-repurposing）/SKILL.md` — RUNTIME_REGISTERED
- `original-writing` — `/Users/xingxuan/Desktop/skills 库/网站制作/02-内容创作/原创长文（original-writing）/SKILL.md` — RUNTIME_REGISTERED
- `ai-polish` — `/Users/xingxuan/Desktop/skills 库/网站制作/02-内容创作/去AI味润色（ai-polish）/SKILL.md` — RUNTIME_REGISTERED
- `humanizer` — `/Users/xingxuan/Desktop/skills 库/网站制作/02-内容创作/去AI味英文版（humanizer）/SKILL.md` — RUNTIME_REGISTERED
- `mimeng-topic-method` — `/Users/xingxuan/Desktop/skills 库/网站制作/02-内容创作/咪蒙选题法（mimeng-topic-method）/SKILL.md` — RUNTIME_REGISTERED
- `brand-voice-system` — `/Users/xingxuan/Desktop/skills 库/网站制作/02-内容创作/品牌声纹系统（brand-voice-system）/SKILL.md` — RUNTIME_REGISTERED
- `ad-copywriting` — `/Users/xingxuan/Desktop/skills 库/网站制作/02-内容创作/商单文案写作（ad-copywriting）/SKILL.md` — RUNTIME_REGISTERED
- `content-rewrite` — `/Users/xingxuan/Desktop/skills 库/网站制作/02-内容创作/改稿（content-rewrite）/SKILL.md` — RUNTIME_REGISTERED
- `last30days` — `/Users/xingxuan/Desktop/skills 库/网站制作/02-内容创作/最近30天（last30days）/SKILL.md` — RUNTIME_REGISTERED
- `research-to-article` — `/Users/xingxuan/Desktop/skills 库/网站制作/02-内容创作/调研成稿（research-to-article）/SKILL.md` — RUNTIME_REGISTERED
- `hook-angle-lab` — `/Users/xingxuan/Desktop/skills 库/网站制作/02-内容创作/选题钩子实验室（hook-angle-lab）/SKILL.md` — RUNTIME_REGISTERED
- `advanced-xhs-visual-design` — `/Users/xingxuan/Desktop/skills 库/网站制作/02-内容创作/高级图文设计（advanced-xhs-visual-design）/SKILL.md` — RUNTIME_REGISTERED
- `api-gateway` — `/Users/xingxuan/Desktop/skills 库/网站制作/03-开发工具/API网关（api-gateway）/SKILL.md` — RUNTIME_REGISTERED
- `mcp-builder` — `/Users/xingxuan/Desktop/skills 库/网站制作/03-开发工具/MCP构建器（mcp-builder）/SKILL.md` — RUNTIME_REGISTERED
- `repo-context-compiler` — `/Users/xingxuan/Desktop/skills 库/网站制作/03-开发工具/仓库上下文编译器（repo-context-compiler）/SKILL.md` — RUNTIME_REGISTERED
- `code-review-ci` — `/Users/xingxuan/Desktop/skills 库/网站制作/03-开发工具/代码评审与CI修复（code-review-ci）/SKILL.md` — RUNTIME_REGISTERED
- `skill-creator` — `/Users/xingxuan/Desktop/skills 库/网站制作/03-开发工具/技能创建器（skill-creator）/SKILL.md` — RUNTIME_REGISTERED
- `skill-vetter` — `/Users/xingxuan/Desktop/skills 库/网站制作/03-开发工具/技能安全审查（skill-vetter）/SKILL.md` — RUNTIME_REGISTERED
- `coding-agent` — `/Users/xingxuan/Desktop/skills 库/网站制作/03-开发工具/编程代理（coding-agent）/SKILL.md` — RUNTIME_REGISTERED
- `web-story` — `/Users/xingxuan/Desktop/skills 库/网站制作/03-开发工具/网页故事（web-story）/SKILL.md` — RUNTIME_REGISTERED
- `content-scraper` — `/Users/xingxuan/Desktop/skills 库/网站制作/04-浏览器自动化/内容抓取（content-scraper）/SKILL.md` — RUNTIME_REGISTERED
- `browser-automation` — `/Users/xingxuan/Desktop/skills 库/网站制作/04-浏览器自动化/浏览器自动化（browser-automation）/SKILL.md` — RUNTIME_REGISTERED
- `browser-research-agent` — `/Users/xingxuan/Desktop/skills 库/网站制作/04-浏览器自动化/浏览器调研代理（browser-research-agent）/SKILL.md` — RUNTIME_REGISTERED
- `lead-followup-automation` — `/Users/xingxuan/Desktop/skills 库/网站制作/04-浏览器自动化/线索跟进自动化（lead-followup-automation）/SKILL.md` — RUNTIME_REGISTERED
- `video-transcribe` — `/Users/xingxuan/Desktop/skills 库/网站制作/04-浏览器自动化/视频转写（video-transcribe）/SKILL.md` — RUNTIME_REGISTERED
- `wechat-mp-auto` — `/Users/xingxuan/Desktop/skills 库/网站制作/05-社交媒体/公众号自动化（wechat-mp-auto）/SKILL.md` — RUNTIME_REGISTERED
- `video-account-analysis` — `/Users/xingxuan/Desktop/skills 库/网站制作/05-社交媒体/微信视频号分析（video-account-analysis）/SKILL.md` — RUNTIME_REGISTERED
- `short-video-script-lab` — `/Users/xingxuan/Desktop/skills 库/网站制作/05-社交媒体/短视频脚本工坊（short-video-script-lab）/SKILL.md` — RUNTIME_REGISTERED
- `social-media-strategy` — `/Users/xingxuan/Desktop/skills 库/网站制作/05-社交媒体/社媒策略分析（social-media-strategy）/SKILL.md` — RUNTIME_REGISTERED
- `xiaohongshu-auto` — `/Users/xingxuan/Desktop/skills 库/网站制作/05-社交媒体/自动发小红书（xiaohongshu-auto）/SKILL.md` — RUNTIME_REGISTERED
- `meeting-notes-actions` — `/Users/xingxuan/Desktop/skills 库/网站制作/06-知识与学习/会议纪要行动项（meeting-notes-actions）/SKILL.md` — RUNTIME_REGISTERED
- `learning-loop` — `/Users/xingxuan/Desktop/skills 库/网站制作/06-知识与学习/学习闭环（learning-loop）/SKILL.md` — RUNTIME_REGISTERED
- `maomao-thinking` — `/Users/xingxuan/Desktop/skills 库/网站制作/06-知识与学习/茂茂商业思考（maomao-thinking）/SKILL.md` — RUNTIME_REGISTERED
- `insight` — `/Users/xingxuan/Desktop/skills 库/网站制作/06-知识与学习/洞察（insight）/SKILL.md` — RUNTIME_REGISTERED
- `知识卡片` — `/Users/xingxuan/Desktop/skills 库/网站制作/06-知识与学习/知识卡片（knowledge-cards）/SKILL.md` — VISIBLE_ONLY
- `knowledge-palace` — `/Users/xingxuan/Desktop/skills 库/网站制作/06-知识与学习/知识宫殿（knowledge-palace）/SKILL.md` — RUNTIME_REGISTERED
- `notes-research` — `/Users/xingxuan/Desktop/skills 库/网站制作/06-知识与学习/笔记研究助手（notes-research）/SKILL.md` — RUNTIME_REGISTERED
- `memory-boost` — `/Users/xingxuan/Desktop/skills 库/网站制作/06-知识与学习/记忆增强（memory-boost）/SKILL.md` — RUNTIME_REGISTERED
- `course-design-agent` — `/Users/xingxuan/Desktop/skills 库/网站制作/06-知识与学习/课程设计代理（course-design-agent）/SKILL.md` — RUNTIME_REGISTERED
- `obsidian` — `/Users/xingxuan/Desktop/skills 库/网站制作/07-效率工具/Obsidian笔记（obsidian）/SKILL.md` — RUNTIME_REGISTERED
- `sonoscli` — `/Users/xingxuan/Desktop/skills 库/网站制作/07-效率工具/办公协同（sonoscli）/SKILL.md` — RUNTIME_REGISTERED
- `editable-pptx-builder` — `/Users/xingxuan/Desktop/skills 库/网站制作/07-效率工具/可编辑PPT生成（editable-pptx-builder）/SKILL.md` — RUNTIME_REGISTERED
- `workflow-automation-builder` — `/Users/xingxuan/Desktop/skills 库/网站制作/07-效率工具/工作流自动化搭建（workflow-automation-builder）/SKILL.md` — RUNTIME_REGISTERED
- `docx-report-builder` — `/Users/xingxuan/Desktop/skills 库/网站制作/07-效率工具/报告文档生成（docx-report-builder）/SKILL.md` — RUNTIME_REGISTERED
- `maomao-ppt` — `/Users/xingxuan/Desktop/skills 库/网站制作/07-效率工具/茂茂PPT（maomao-ppt）/SKILL.md` — RUNTIME_REGISTERED
- `market-research-analyst` — `/Users/xingxuan/Desktop/skills 库/网站制作/08-数据分析/市场调研分析（market-research-analyst）/SKILL.md` — RUNTIME_REGISTERED
- `business-dashboard-analyst` — `/Users/xingxuan/Desktop/skills 库/网站制作/08-数据分析/经营仪表盘分析（business-dashboard-analyst）/SKILL.md` — RUNTIME_REGISTERED
- `spreadsheet-analyst` — `/Users/xingxuan/Desktop/skills 库/网站制作/08-数据分析/表格分析助手（spreadsheet-analyst）/SKILL.md` — RUNTIME_REGISTERED
- `finance-assistant` — `/Users/xingxuan/Desktop/skills 库/网站制作/08-数据分析/财务分析助手（finance-assistant）/SKILL.md` — RUNTIME_REGISTERED
- `asset-allocation-risk-review` — `/Users/xingxuan/Desktop/skills 库/网站制作/08-数据分析/资产配置风险复盘（asset-allocation-risk-review）/SKILL.md` — RUNTIME_REGISTERED
- `financial-risk-literacy` — `/Users/xingxuan/Desktop/skills 库/网站制作/08-数据分析/金融风险识别（financial-risk-literacy）/SKILL.md` — RUNTIME_REGISTERED
- `personal-investment-workflow` — `/Users/xingxuan/Desktop/skills 库/网站制作/09-金融/个人投资工作流（personal-investment-workflow）/SKILL.md` — RUNTIME_REGISTERED
- `enterprise-strategy-analysis` — `/Users/xingxuan/Desktop/skills 库/网站制作/09-金融/企业策略分析（enterprise-strategy-analysis）/SKILL.md` — RUNTIME_REGISTERED
- `investment-risk-review` — `/Users/xingxuan/Desktop/skills 库/网站制作/09-金融/投资风险辨析（investment-risk-review）/SKILL.md` — RUNTIME_REGISTERED
- `market-monitoring` — `/Users/xingxuan/Desktop/skills 库/网站制作/09-金融/看盘盯盘（market-monitoring）/SKILL.md` — RUNTIME_REGISTERED
- `financial-modeling` — `/Users/xingxuan/Desktop/skills 库/网站制作/09-金融/财务建模（financial-modeling）/SKILL.md` — RUNTIME_REGISTERED
- `wealth-advisor` — `/Users/xingxuan/Desktop/skills 库/网站制作/09-金融/财富顾问（wealth-advisor）/SKILL.md` — RUNTIME_REGISTERED
- `quant-trading-literacy` — `/Users/xingxuan/Desktop/skills 库/网站制作/09-金融/量化交易认知（quant-trading-literacy）/SKILL.md` — RUNTIME_REGISTERED

## 当前工具与员工能力

| 员工/工具 | 职能 | 状态 | 证据 |
|---|---|---|---|
| `ai-master` / `/Users/xingxuan/.codex/skills/ai-master/SKILL.md` | AI总经理 | `UNKNOWN` | `/Users/xingxuan/.codex/skills/ai-master/SKILL.md` |
| `ai-task-compiler` / `/Users/xingxuan/.codex/skills/ai-task-compiler/SKILL.md` | 任务编译员 | `UNKNOWN` | `/Users/xingxuan/.codex/skills/ai-task-compiler/SKILL.md` |
| `agent-eval-loop` / `/Users/xingxuan/.codex/skills/agent-eval-loop/SKILL.md` | 评测与回归工程师 | `UNKNOWN` | `/Users/xingxuan/.codex/skills/agent-eval-loop/SKILL.md` |
| `animation-factory` / `/Users/xingxuan/.codex/skills/maomao-animation-studio/SKILL.md` | 动画工厂总控 | `UNKNOWN` | `/Users/xingxuan/.codex/skills/maomao-animation-studio/scripts/startup_adapter.py` |
| `novel-characters` / `/Users/xingxuan/.codex/skills/novel-characters/SKILL.md` | 角色设定师 | `UNKNOWN` | `/Users/xingxuan/.codex/skills/novel-characters/SKILL.md` |
| `novel-art` / `/Users/xingxuan/.codex/skills/novel-art/SKILL.md` | 场景与道具美术师 | `UNKNOWN` | `/Users/xingxuan/.codex/skills/novel-art/SKILL.md` |
| `novel-script` / `/Users/xingxuan/.codex/skills/novel-script/SKILL.md` | 剧本与节拍师 | `UNKNOWN` | `/Users/xingxuan/.codex/skills/novel-script/SKILL.md` |
| `novel-storyboard` / `/Users/xingxuan/.codex/skills/novel-storyboard/SKILL.md` | 分镜与运镜师 | `UNKNOWN` | `/Users/xingxuan/.codex/skills/novel-storyboard/SKILL.md` |
| `chatcut-video-gen` / `chatcut:video-gen` | 视频生成执行员 | `UNKNOWN` | `/Users/xingxuan/.codex/plugins/cache/chatcut-inc/chatcut/0.2.26/skills/video-gen/SKILL.md` |
| `chatcut-edit` / `chatcut:verification + chatcut:export` | 剪辑与导出执行员 | `UNKNOWN` | `/Users/xingxuan/.codex/plugins/cache/chatcut-inc/chatcut/0.2.26/skills/verification/SKILL.md` |
| `chatcut-voice-music` / `chatcut:voice + chatcut:music + chatcut:transcription` | 声音与音乐执行员 | `UNKNOWN` | `/Users/xingxuan/.codex/plugins/cache/chatcut-inc/chatcut/0.2.26/skills/voice/SKILL.md` |
| `browser-research` / `/Users/xingxuan/.codex/skills/browser-research-agent/SKILL.md` | 研究员 | `UNKNOWN` | `/Users/xingxuan/.codex/skills/browser-research-agent/SKILL.md` |
| `video-transcribe` / `/Users/xingxuan/.codex/skills/video-transcribe/SKILL.md` | 参考片分析员 | `UNKNOWN` | `/Users/xingxuan/.codex/skills/video-transcribe/SKILL.md` |
| `skill-discovery` / `skill-finder + skill-vetter` | 技能发现与安全审查员 | `UNKNOWN` | `/Users/xingxuan/.codex/skills/skill-finder/SKILL.md` |
| `blender` / `/Applications/Blender.app/Contents/MacOS/Blender` | 白模与动作工程师 | `CALLABLE` | `/Applications/Blender.app/Contents/MacOS/Blender --version` |
| `motion-capture` / `GVHMR + mixamo-llm-mocap` | 动作捕捉研究员 | `UNKNOWN` | `/Users/xingxuan/Documents/ChatGPT/codex开发工程师 2/AI动画公司/06_动作工具链` |
| `grok-chairman` / `Grok Bot 董事长会话` | 独立董事长/审计员 | `CALLABLE` | `Grok Bot 董事长会话` |
| `independent-shot-auditor` / `待绑定独立Bot或审片流程` | 独立看片审计员 | `BLOCKED` | `/Users/xingxuan/Documents/ChatGPT/codex开发工程师 2/AI动画公司/00_公司总控/验收等级与审计协议.md` |
