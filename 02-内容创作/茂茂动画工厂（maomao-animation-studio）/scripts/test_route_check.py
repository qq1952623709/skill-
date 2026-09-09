#!/usr/bin/env python3
"""Free regression cases for the semantic startup router."""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from route_check import route  # noqa: E402


CASES = [
    ("T-combat-打架", "桥上两个人打架，做成紧张的短片", "animation_combat_oneshot"),
    ("T-combat-对打", "复刻参考片的两人对打节奏，约五十秒", "animation_combat_oneshot"),
    ("T-combat-刀踢", "两个角色用刀和踢击死斗，要有重心和击退", "animation_combat_oneshot"),
    ("T-edit-删两秒", "帮我把这个视频结尾删两秒", "edit_only"),
    ("T-consult-选模型", "只咨询：即梦和 MiniMax 哪个适合打斗", "consult_only"),
    ("T-wrong-直冲", "直接整段丢进 ChatCut，别做分镜", "animation_combat_oneshot"),
    ("T-knowledge-观点", "把这个观点做成资讯短片讲解", "knowledge_short"),
    ("P1-干架", "帮我做一段桥上两个人干架的短动画，要有重量", "animation_combat_oneshot"),
    ("P2-裁片尾", "这个成片尾巴多了两秒，帮我裁一下就行", "edit_only"),
    ("P3-先问问", "先别开工，我想问问 Seedance 跟即梦打戏谁更稳", "consult_only"),
    ("P4-参考别猜", "参考片我想逐帧还原动作，别猜是哪个平台做的", "animation_combat_oneshot"),
    ("P5-错误手段", "直接用提示词整段生成，跳过分镜省事", "animation_combat_oneshot"),
    ("P6-十五秒完整提示词", "15秒，16:9，两名少年在都市街道高速对打。左侧黑发红格纹外套，力量型近身硬打；右侧银蓝短发科技外套，高速突进与蓝色能量。第一秒立即开打，动作清楚可读，镜头高速跟随，冲击波、水花、碎石和车辆震动都要有反馈；无字幕、无Logo，结尾双方对峙。", "animation_single_prompt"),
    ("R2-小孩踢球", "帮我做一个30秒小孩踢球的动画，要有声音", "animation_dialogue_oneshot"),
    ("R2-家庭动画", "温馨家庭吃晚饭的动画短片", "animation_dialogue_oneshot"),
    ("R2-口播剪辑", "帮我剪一个已有素材的口播", "edit_only"),
    ("R2-厨房刀", "厨房里有一把刀的温馨动画短片", "animation_dialogue_oneshot"),
    ("R2-直接提示词", "直接用一个提示词生成50秒打戏", "animation_combat_oneshot"),
]


def main() -> int:
    failures = []
    for name, text, expected in CASES:
        got = route(text)
        if got["route_id"] != expected:
            failures.append({"case": name, "expected": expected, "observed": got["route_id"]})
        if expected == "edit_only" and any(x["skill"] == "novel-storyboard" for x in got["must_load"]):
            failures.append({"case": name, "error": "edit route loaded storyboard"})
        if expected == "consult_only" and got["signals"]["consult_only"] is not True:
            failures.append({"case": name, "error": "consult signal missing"})
        if expected == "animation_combat_oneshot" and not got["signals"]["combat"]:
            failures.append({"case": name, "error": "combat signal missing"})
        if expected == "animation_single_prompt":
            if not got["signals"]["single_prompt_ready"]:
                failures.append({"case": name, "error": "single prompt signal missing"})
            if len(got["must_load"]) != 3:
                failures.append({"case": name, "error": "fast route should load exactly three skills"})
        if name == "P5-错误手段" and not got["signals"]["wrong_method_claim"]:
            failures.append({"case": name, "error": "wrong method not flagged"})
        if name == "P5-错误手段" and got.get("capability_plan", {}).get("direction_audit", {}).get("verdict") != "WRONG_PROBLEM":
            failures.append({"case": name, "error": "direction audit did not hard-stop wrong method"})
        if expected == "animation_combat_oneshot":
            if got.get("capability_plan", {}).get("task_family") != expected:
                failures.append({"case": name, "error": "capability map family mismatch"})
            if got.get("capability_plan", {}).get("hard_stop_before_paid_generation") is not True:
                failures.append({"case": name, "error": "unknown dependencies did not stop paid generation"})
        if name == "R2-小孩踢球":
            if got["signals"]["combat"]:
                failures.append({"case": name, "error": "sports action falsely routed as combat"})
            if "chatcut:voice" not in got.get("capability_plan", {}).get("production_tools", []):
                failures.append({"case": name, "error": "voice dependency missing"})
            if got.get("capability_plan", {}).get("direction_audit", {}).get("verdict") == "DIRECTION_PASS":
                failures.append({"case": name, "error": "heuristic direction falsely passed"})
        if name == "R2-口播剪辑" and any(x["skill"] == "novel-storyboard" for x in got["must_load"]):
            failures.append({"case": name, "error": "edit route loaded storyboard"})
        if name == "R2-厨房刀" and got["signals"]["combat"]:
            failures.append({"case": name, "error": "incidental knife falsely routed as combat"})
        if name == "R2-直接提示词":
            if not got["signals"]["wrong_method_claim"]:
                failures.append({"case": name, "error": "wrong method not flagged"})
            if got.get("capability_plan", {}).get("direction_audit", {}).get("verdict") != "WRONG_PROBLEM":
                failures.append({"case": name, "error": "wrong method did not hard-stop"})
    report = {"total": len(CASES), "passed": len(CASES) - len(failures), "failed": len(failures), "failures": failures}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
