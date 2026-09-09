#!/usr/bin/env python3
"""Deterministic startup router for animation tasks.

This is a preflight/checker, not a claim that every downstream tool is callable.
It returns the route, must-load skills, file hashes, and missing runtime entries.
"""
from __future__ import annotations

import hashlib
import json
import sys
import re
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from inventory_check import check_inventory
from capability_map import resolve as resolve_capabilities

ROOTS = [
    Path("/Users/xingxuan/.codex/skills"),
    Path("/Users/xingxuan/.codex/plugins/cache/chatcut-inc/chatcut/0.2.26/skills"),
]
ANIMATION = ("动画", "漫剧", "短剧", "视频", "片", "镜头", "成片", "动作片")
COMBAT = ("打斗", "打架", "对打", "打戏", "干架", "互殴", "打一架", "武器", "挥刀", "刀砍", "持刀", "挥拳", "碰撞", "击退", "重心", "打击感", "闪避", "追击", "死斗", "动作片")
SPORTS = ("踢球", "足球", "篮球", "排球", "运动比赛")
ANCHOR = ("角色", "人物", "定妆", "四视图", "三视图", "一致", "皮肤")
EDIT = ("删除", "删掉", "删", "剪", "口播", "已有素材", "剪掉", "裁掉", "裁一下", "切掉", "去掉", "只剪", "修一下", "保留结尾", "保留片尾", "替换片段")
CONSULT = ("哪个", "比较", "适合", "怎么收费", "多少钱", "是否支持", "推荐", "只咨询", "咨询路线")
CONSULT_PAUSE = ("先别开工", "先别生成", "只问问", "只是问问", "先咨询")
RESUME = ("继续", "恢复", "上次做到", "原任务状态", "接着做")
KNOWLEDGE = ("观点讲解", "资讯短片", "知识卡", "知识讲解")
REFERENCE = ("复刻参考", "复刻参考片", "参考片节奏", "还原动作", "逐帧重建", "逐帧还原")
WRONG_METHOD = ("直接整段", "直接丢进", "别做分镜", "跳过分镜", "不做分镜", "直接用提示词", "直接用一个提示词")


def skill_path(name: str) -> Path | None:
    for root in ROOTS:
        direct = root / name / "SKILL.md"
        if direct.exists():
            return direct
        if ":" in name:
            plugin_name = name.split(":", 1)[1]
            candidate = root / plugin_name / "SKILL.md"
            if candidate.exists():
                return candidate
    return None


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def has_any(text: str, needles: tuple[str, ...]) -> bool:
    return any(n in text for n in needles)


def probe_runtime(name: str, path: Path) -> tuple[str, str]:
    """Return a conservative state; never call paid or browser actions here."""
    if ":" in name:
        return "UNKNOWN", "hosted plugin requires current MCP/host probe"
    if not (path / "SKILL.md").exists():
        return "MISSING", "SKILL.md missing"
    scripts = path / "scripts"
    if scripts.exists() and any(scripts.iterdir()):
        node = shutil.which("node") or "/Applications/ChatGPT.app/Contents/Resources/cua_node/bin/node"
        if Path(node).exists():
            return "UNKNOWN", "script entry exists; only runtime binary presence probed"
        return "BLOCKED", "script skill requires Node.js but no runtime was found"
    return "UNKNOWN", "skill file read; no execution probe requested"


def _reference_evidence(reference_path: str | None) -> dict:
    if not reference_path:
        return {"reference_provider_status": "REFERENCE_PROVIDER_UNKNOWN", "evidence": [], "reason": "no reference path supplied"}
    path = Path(reference_path)
    if not path.exists():
        return {"reference_provider_status": "REFERENCE_PROVIDER_UNKNOWN", "evidence": [{"type": "path", "path": str(path), "exists": False}], "reason": "reference path missing"}
    evidence = [{"type": "sha256", "path": str(path), "sha256": sha(path)}]
    ffprobe = shutil.which("ffprobe")
    if ffprobe:
        proc = subprocess.run(
            [ffprobe, "-v", "error", "-show_entries", "format=format_name,duration,size:stream=codec_name,width,height,r_frame_rate,sample_rate,channels", "-of", "json", str(path)],
            capture_output=True, text=True, check=False,
        )
        if proc.returncode == 0:
            try:
                evidence.append({"type": "ffprobe", "path": str(path), "metadata": json.loads(proc.stdout)})
            except json.JSONDecodeError:
                evidence.append({"type": "ffprobe", "path": str(path), "raw_available": True})
    return {"reference_provider_status": "REFERENCE_PROVIDER_UNKNOWN", "evidence": evidence, "reason": "container evidence cannot identify upstream generator"}


def route(request: str, reference_path: str | None = None) -> dict:
    inventory = check_inventory()
    text = request.casefold()
    has_edit = has_any(text, EDIT) and has_any(text, ("视频", "片尾", "结尾", "秒", "素材", "片段"))
    has_reference = has_any(text, REFERENCE)
    explicit_pause = has_any(text, CONSULT_PAUSE)
    has_consult = has_any(text, CONSULT) and not has_any(text, ("帮我做", "生成", "制作", "出片", "提交"))
    if explicit_pause:
        has_consult = True
    has_resume = has_any(text, RESUME)
    has_knowledge = has_any(text, KNOWLEDGE) and not has_any(text, ("角色动画", "做动画", "打斗片", "生成视频"))
    has_animation = has_any(text, ANIMATION) or has_any(text, ("复刻", "参考片", "成片"))
    wrong_method = has_any(text, WRONG_METHOD)
    durations = [int(x) for x in re.findall(r"(?<!\d)(\d{1,3})\s*(?:秒|s\b)", text)]
    single_prompt_ready = bool(durations) and max(durations) <= 15 and len(request) >= 120 and not wrong_method
    has_combat = (not has_any(text, SPORTS)) and (has_any(text, COMBAT) or has_reference or wrong_method or (
        "两个人" in text and has_any(text, ("打", "战", "冲突"))
    ))
    has_anchor = has_any(text, ANCHOR)
    if has_edit:
        route_id = "edit_only"
    elif has_consult and (explicit_pause or not has_reference):
        route_id = "consult_only"
    elif has_resume:
        route_id = "resume"
    elif has_knowledge:
        route_id = "knowledge_short"
    elif single_prompt_ready:
        route_id = "animation_single_prompt"
    elif has_combat or wrong_method:
        route_id = "animation_combat_oneshot"
    elif has_animation:
        route_id = "animation_dialogue_oneshot"
    else:
        route_id = "RESEARCH_REQUIRED"

    route_file = Path(__file__).resolve().parents[1] / "references" / "task-router.json"
    spec = json.loads(route_file.read_text(encoding="utf-8"))
    selected = next((r for r in spec["routes"] if r["id"] == route_id), None)
    must_load = selected["must_load"] if selected else []
    loaded = []
    missing = []
    for name in must_load:
        path = skill_path(name)
        item = {"skill": name, "state": "UNKNOWN", "read_path": None, "read_path_hash": None}
        if path:
            # Reading the full SKILL.md is intentional: route discovery is not a name-only lookup.
            raw = path.read_bytes()
            digest = hashlib.sha256(raw).hexdigest()
            state, reason = probe_runtime(name, path.parent)
            item.update({"path": str(path), "read_path": str(path), "read_path_hash": digest, "state": state, "probe_reason": reason})
            loaded.append(item)
        else:
            item["state"] = "MISSING"
            item["probe_reason"] = "skill path not found in configured roots"
            missing.append(item)
    spec_hash = sha(route_file)
    ref_evidence = _reference_evidence(reference_path) if has_reference else {
        "reference_provider_status": "NOT_APPLICABLE",
        "evidence": [],
    }
    capability_plan = resolve_capabilities(request, route_id)
    return {
        "route_id": route_id,
        "observed_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "route_spec_path": str(route_file),
        "route_spec_sha256": spec_hash,
        "signals": {
            "animation": has_animation,
            "combat": has_combat,
            "anchor_language_present": has_anchor,
            "edit_only": has_edit,
            "consult_only": has_consult,
            "resume": has_resume,
            "knowledge_short": has_knowledge,
            "wrong_method_claim": wrong_method,
            "reference_reconstruction": has_reference,
            "single_prompt_ready": single_prompt_ready,
            "duration_seconds_detected": durations,
        },
        **ref_evidence,
        "must_load": loaded,
        "missing": missing,
        "capability_plan": capability_plan,
        "company_inventory": inventory,
        "hard_stop_before_paid_generation": inventory["inventory_status"] != "PASS" or bool(missing) or route_id == "RESEARCH_REQUIRED" or any(
            item["state"] != "CALLABLE" for item in loaded
        ) or capability_plan.get("hard_stop_before_paid_generation", False),
        "note": "本探针会读取并哈希 must_load 的 SKILL.md；目录存在仍不等于插件或模型可调用。",
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("usage: route_check.py '用户原话' [--reference /path/to/file]")
    request = sys.argv[1]
    reference = None
    if len(sys.argv) == 4 and sys.argv[2] == "--reference":
        reference = sys.argv[3]
    elif len(sys.argv) != 2:
        raise SystemExit("usage: route_check.py '用户原话' [--reference /path/to/file]")
    print(json.dumps(route(request, reference), ensure_ascii=False, indent=2))
