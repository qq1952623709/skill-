#!/usr/bin/env python3
"""Create a no-side-effect remediation contract for missing capabilities.

It intentionally does not install anything. Installation is a separate,
explicitly authorized action after research and security/licence review.
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("tools", nargs="+")
    args = parser.parse_args()
    result = {
        "status": "MISSING_TOOL_RESEARCH_REQUIRED",
        "created_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "tools": args.tools,
        "steps": [
            {"step": 1, "action": "本机与当前运行时复查", "owner": "ai-master", "side_effect": "read_only"},
            {"step": 2, "action": "查官方文档、官方仓库和许可", "owner": "browser-research-agent", "side_effect": "read_only"},
            {"step": 3, "action": "安全审查、依赖和权限审查", "owner": "skill-vetter", "side_effect": "read_only"},
            {"step": 4, "action": "由CEO授权安装或登录", "owner": "CEO", "side_effect": "approval_required"},
            {"step": 5, "action": "最小无费用探针并写回roster四态", "owner": "ai-master", "side_effect": "reversible_probe"},
        ],
        "hard_stops": [
            "未授权不得安装、登录或付款",
            "下载仓库不等于工具可用",
            "探针失败不得进入付费生产",
            "同一根因连续失败三次必须复核路线而不是继续重试",
        ],
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
