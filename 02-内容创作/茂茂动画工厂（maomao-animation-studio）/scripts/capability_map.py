#!/usr/bin/env python3
"""Resolve a user request against the personal AI manager capability map.

This is deliberately conservative: it maps goals to employees and probes
their registered state; it never treats a SKILL.md as proof of runtime
availability and never installs or calls paid tools.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
from typing import Any

from inventory_check import CONTROL_ROOT, ROSTER, check_inventory

MAP_PATH = CONTROL_ROOT / "capability_map.json"
CODEX_HOME = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex")).expanduser()
ROOTS = [CODEX_HOME / "skills" / "personal", CODEX_HOME / "skills"]
ROOTS.extend(CODEX_HOME.glob("plugins/cache/*/*/skills"))
ROOTS.extend(CODEX_HOME.glob("plugins/cache/*/*/*/skills"))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_map() -> dict[str, Any]:
    return json.loads(MAP_PATH.read_text(encoding="utf-8"))


def load_roster() -> list[dict[str, Any]]:
    if not ROSTER.exists():
        return []
    rows = []
    for raw in ROSTER.read_text(encoding="utf-8").splitlines():
        if raw.strip():
            rows.append(json.loads(raw))
    return rows


def locate_skill(name: str) -> Path | None:
    for root in ROOTS:
        direct = root / name / "SKILL.md"
        if direct.exists():
            return direct
        if ":" in name:
            candidate = root / name.split(":", 1)[1] / "SKILL.md"
            if candidate.exists():
                return candidate
    return None


def roster_match(name: str, roster: list[dict[str, Any]]) -> dict[str, Any] | None:
    folded = name.casefold()
    short = name.split(":", 1)[-1].casefold()
    for row in roster:
        rid = str(row.get("id", "")).casefold()
        tool = str(row.get("skill_or_tool", "")).casefold()
        if rid in {folded, short, f"skill:{short}"} or tool == folded or tool == short or tool.endswith(f"/{short}/skill.md"):
            return row
    return None


def family_for_request(request: str, route_id: str | None = None) -> str:
    if route_id and route_id != "RESEARCH_REQUIRED":
        if route_id == "consult_only":
            return "consult_or_tool_selection"
        return route_id
    text = request.casefold()
    if any(x in text for x in ("删两秒", "裁掉", "剪掉", "剪辑", "剪口播", "已有素材", "只保留片尾", "替换片段")):
        return "edit_only"
    if any(x in text for x in ("直接整段", "跳过分镜", "不做分镜", "只用提示词", "直接用一个提示词", "直接丢进生成器")):
        return "animation_combat_oneshot"
    if any(x in text for x in ("白模", "动作预演", "blender做", "blender 做")):
        return "animation_combat_oneshot"
    if any(x in text for x in ("pdf", "便携文档", "扫描件")):
        return "pdf_work"
    if any(x in text for x in ("开题报告", "论文", "word", "docx", "文档", "报告排版", "修改报告")):
        return "document_work"
    if any(x in text for x in ("做网页", "网站", "网页", "应用界面", "交互页面", "ui设计")):
        return "web_design"
    if any(x in text for x in ("ppt", "演示文稿", "幻灯片", "课件")):
        return "presentation"
    if any(x in text for x in ("excel", "表格", "工作簿", "数据透视")):
        return "spreadsheet"
    if any(x in text for x in ("美女生成器", "女性人像", "穿搭人像", "女性生活摄影")):
        return "beauty_portrait"
    if any(x in text for x in ("生成图片", "配图", "插画", "图片编辑", "图像生成")):
        return "image_creation"
    if "skill" in text and any(x in text for x in ("创建", "写一个", "新增", "安装", "接入", "修改", "开发", "适配")):
        return "skill_governance"
    if any(x in text for x in ("技能库", "skill治理", "skill 库", "skill治理", "总控正本", "roster.jsonl", "capability_map")):
        return "skill_governance"
    if any(x in text for x in ("帮我梳理人生", "梳理人生方向", "分析我的人生", "个人选择怎么想", "我想做人生规划", "自我认知梳理", "陪我反思一个决定", "人生复盘", "价值观梳理", "倾听我的烦恼")):
        return "personal_growth_coaching"
    if any(x in text for x in ("上网查", "搜索资料", "研究现状", "找 github", "找github", "github上面", "github 仓库", "github仓库", "核验最新", "对比来源")):
        return "research"
    production_intent = any(x in text for x in ("做动画", "动画短片", "动画", "踢球", "足球", "漫剧", "短剧", "成片", "出片", "做视频", "做短片", "视频：", "视频"))
    if any(x in text for x in ("写文章", "长文创作", "公众号文案", "原创内容", "润色文章")) and not production_intent:
        return "writing"
    consult_intent = any(x in text for x in ("哪个ai", "哪个 AI", "哪个模型", "什么工具", "怎么收费", "github", "skill", "适合用"))
    if consult_intent and not production_intent:
        return "consult_or_tool_selection"
    if any(x in text for x in ("观点", "资讯", "知识卡", "讲解")) and not any(x in text for x in ("角色动画", "打斗", "做动画")):
        return "knowledge_short"
    sports = any(x in text for x in ("踢球", "足球", "篮球", "排球", "运动比赛"))
    if not sports and (any(x in text for x in ("打斗", "打架", "对打", "死斗", "砍", "挥刀", "重心", "打击感", "动作参考", "受击", "碰撞")) or ("两个人" in text and any(x in text for x in ("视频", "动作", "打")))):
        return "animation_combat_oneshot"
    if any(x in text for x in ("漫剧", "短剧", "配音", "台词", "对白", "口型")):
        return "animation_dialogue_oneshot"
    if production_intent or any(x in text for x in ("做视频", "做短片", "做动画", "动画短片", "出片", "一个场景", "一个故事")):
        return "animation_dialogue_oneshot"
    return "consult_or_tool_selection"


def direction_audit(request: str, family: str) -> dict[str, Any]:
    text = request.casefold()
    flags: list[str] = []
    if any(x in text for x in ("直接整段", "跳过分镜", "不做分镜", "只用提示词", "直接用一个提示词", "直接丢进生成器")):
        flags.append("把提示词当作动作控制，试图跳过前置设计")
    if family == "animation_combat_oneshot" and any(x in text for x in ("50秒", "一分钟", "整条片", "直接出片")):
        flags.append("高成本长片尚未经过代表段验证")
    if family.startswith("animation_") and not any(x in text for x in ("角色", "人物", "定妆", "四视图", "一致")):
        flags.append("角色一致性锚点未在目标中明确，需由总经理主动补齐")
    if family == "animation_combat_oneshot" and not any(x in text for x in ("分镜", "节拍", "镜头", "动作")):
        flags.append("动作链与镜头节拍未明确，不能直接扩量")
    if any(x in text for x in ("我觉得", "应该就是", "肯定是", "看起来像")) and "参考" in text:
        flags.append("参考片来源/制作路线仍是假设，需要查证")
    if any(x in text for x in ("查清楚", "先查", "研究一下", "看github", "看 github", "参考视频怎么做")):
        flags.append("用户明确要求先研究路线，不能直接进入生产")
    wrong_method = any("跳过" in x or "提示词" in x for x in flags)
    if wrong_method:
        verdict = "WRONG_PROBLEM"
    elif family == "consult_or_tool_selection" or any("先研究" in x or "查证" in x for x in flags):
        verdict = "NEEDS_RESEARCH"
    else:
        # Heuristics can nominate a route, but cannot independently approve it.
        verdict = "DIRECTION_CANDIDATE" if family.startswith("animation_") else "DIRECTION_PASS"
    alternatives = []
    if family == "animation_combat_oneshot":
        alternatives = [
            "路线A：白模/Blender动作预演，先锁重心、接触、击退与节奏，再换皮肤",
            "路线B：角色锚点+分镜+3-8秒代表段，验证后再交给视频生成",
        ]
    elif family.startswith("animation_"):
        alternatives = ["先做静态角色/场景资产与单镜头样本，再进入多镜头生成"]
    else:
        alternatives = ["先做只读研究和证据清单，不进入制作"]
    return {
        "goal_text": request,
        "proposed_method_flags": flags,
        "verdict": verdict,
        "independent_review_required": family.startswith("animation_"),
        "cheapest_probe": "先做只读研究或一个免费/零额度代表段；禁止用整片结果证明单镜头能力",
        "materially_different_routes": alternatives,
        "ceo_decision_needed": ["预算", "可接受平台/会员", "最终审美硬标准"] if family.startswith("animation_") else [],
    }


def resolve(request: str, route_id: str | None = None) -> dict[str, Any]:
    inventory = check_inventory()
    if inventory["inventory_status"] != "PASS":
        return {
            "status": "BLOCKED",
            "reason": "personal control inventory is not valid",
            "personal_inventory": inventory,
            "capability_map_path": str(MAP_PATH),
        }
    capability_map = load_map()
    family = family_for_request(request, route_id)
    entry = next((x for x in capability_map["task_families"] if x["id"] == family), None)
    known_names = sorted({
        "Grok", "Grok Bot", "豆包", "MiniMax", "ChatCut", "Blender", "Kling", "Seedance", "即梦", "Suno",
    }, key=len, reverse=True)
    user_named_tools = [name for name in known_names if name.casefold() in request.casefold()]
    if entry is None:
        return {
            "status": "RESEARCH_REQUIRED",
            "task_family": family,
            "direction_audit": direction_audit(request, family),
            "capability_map_path": str(MAP_PATH),
            "capability_map_sha256": sha256(MAP_PATH),
            "personal_inventory": inventory,
            "user_named_tools": user_named_tools,
        }
    roster = load_roster()
    voice_intent = any(x in request.casefold() for x in ("声音", "配音", "台词", "对白", "旁白", "音效", "口型", "voice", "audio"))
    # The bridge itself is a mandatory control-plane dependency, so a route
    # cannot silently bypass the semantic dispatcher and its evidence rules.
    must_load = list(dict.fromkeys(["ai-master-toolkit"] + entry.get("must_load", [])))
    production_tools = list(entry.get("production_tools", []))
    if voice_intent and family.startswith("animation_") and "chatcut:voice" not in production_tools:
        production_tools.append("chatcut:voice")
    all_names = list(dict.fromkeys(must_load + production_tools))
    tools = []
    missing = []
    unknown = []
    for name in all_names:
        path = locate_skill(name)
        row = roster_match(name, roster)
        state = row.get("state") if row else None
        if not state:
            state = "UNKNOWN" if path else "MISSING"
        item = {
            "name": name,
            "role": row.get("role") if row else None,
            "registered_state": state,
            "skill_path": str(path) if path else None,
            "skill_sha256": sha256(path) if path else None,
            "evidence_path": row.get("evidence_path") if row else None,
        }
        tools.append(item)
        if state == "MISSING" or not path:
            missing.append(name)
        if state in {"UNKNOWN", "BLOCKED"}:
            unknown.append(name)
    direction = direction_audit(request, family)
    ai_roles = entry.get("ai_roles", {})
    role_tools: list[str] = []
    for value in ai_roles.values():
        role_tools.extend(value if isinstance(value, list) else [value])
    dispatch_order = list(dict.fromkeys(user_named_tools + role_tools + entry.get("production_tools", [])))
    hard_stop = bool(missing or unknown or direction["verdict"] != "DIRECTION_PASS" or inventory.get("inventory_status") != "PASS")
    return {
        "status": ("BLOCKED_PENDING_PROBES" if hard_stop else "READY_FOR_PLAN"),
        "task_family": family,
        "task_family_goal_examples": entry.get("goal_examples", []),
        "ai_roles": ai_roles,
        "user_named_tools": user_named_tools,
        "dispatch_order": dispatch_order,
        "must_load": must_load,
        "production_tools": production_tools,
        "required_outputs": entry.get("required_outputs", []),
        "acceptance": entry.get("acceptance", []),
        "forbid_unless": entry.get("forbid_unless", []),
        "cheapest_probe": entry.get("cheapest_probe"),
        "materially_different_route": entry.get("materially_different_route"),
        "direction_audit": direction,
        "tools": tools,
        "missing_tools": missing,
        "unknown_or_blocked_tools": unknown,
        "tool_gap_plan": {
            "required_when": bool(missing),
            "steps": ["browser-research-agent查官方/可信仓库", "skill-vetter审安全与许可", "CEO授权安装", "安装后最小探针", "写回roster四态"],
            "never_do": ["未授权安装", "把仓库下载当可用", "缺工具时直接付费生产"],
        },
        "capability_map_path": str(MAP_PATH),
        "capability_map_sha256": sha256(MAP_PATH),
        "personal_inventory": inventory,
        "counterargument": "外部 Demo 或长提示词不能证明本机工具和路线可用；先做最便宜的代表段并保留独立审计。",
        "stop_conditions": ["方向非 DIRECTION_PASS", "任一关键依赖 UNKNOWN/BLOCKED/MISSING", "代表段未通过", "独立审计未通过", "成本上限或权限未知"],
        "independent_auditor": entry.get("independent_auditor", "UNASSIGNED_UNLESS_SEPARATE_REVIEWER_CONFIRMED"),
        "audit_policy": entry.get("audit_policy", "未配置独立审计员时只报告自检，不声称独立审计通过。"),
        "hard_stop_before_paid_generation": hard_stop,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("request")
    parser.add_argument("--route-id")
    args = parser.parse_args()
    result = resolve(args.request, args.route_id)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result.get("status") == "READY_FOR_PLAN" else 2


if __name__ == "__main__":
    raise SystemExit(main())
