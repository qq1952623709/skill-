#!/usr/bin/env python3
"""Build the visible Skill catalog and its machine-readable registry."""

from __future__ import annotations

import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path


DESKTOP_ROOT = Path(os.environ.get("CODEX_SKILLS_LIBRARY", Path(__file__).resolve().parent))
CODEX_HOME = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))
RUNTIME_ROOT = Path(os.environ.get("CODEX_SKILLS_RUNTIME", CODEX_HOME / "skills"))
PLUGIN_ROOTS = sorted((CODEX_HOME / "plugins" / "cache").glob("*/*/skills"))
ROSTER_PATH = Path(os.environ["AI_ANIMATION_COMPANY_ROOT"]).expanduser() / "00_公司总控" / "roster.jsonl" if os.environ.get("AI_ANIMATION_COMPANY_ROOT") else None


def metadata(path: Path) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    block = text.split("---", 2)[1] if text.startswith("---") else ""
    name = re.search(r"^name:\s*['\"]?([^'\"\n]+)", block, re.MULTILINE)
    description = re.search(r"^description:\s*[\"']?(.+?)[\"']?\s*$", block, re.MULTILINE)
    return (name.group(1).strip() if name else path.parent.name,
            description.group(1).strip() if description else "")


def collect(root: Path, kind: str) -> list[dict]:
    if not root.exists():
        return []
    rows = []
    for skill_file in sorted(root.rglob("SKILL.md")):
        name, description = metadata(skill_file)
        rows.append({
            "name": name,
            "description": description,
            "path": str(skill_file),
            "source": kind,
            "folder": str(skill_file.parent),
        })
    return rows


def collect_tools() -> list[dict]:
    tools = []
    if ROSTER_PATH is None or not ROSTER_PATH.exists():
        return tools
    for line in ROSTER_PATH.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        tools.append({
            "id": row.get("id"),
            "role": row.get("role"),
            "skill_or_tool": row.get("skill_or_tool"),
            "inputs": row.get("inputs", []),
            "actions": row.get("actions", []),
            "outputs": row.get("outputs", []),
            "acceptance": row.get("acceptance", []),
            "state": row.get("state", "UNKNOWN"),
            "evidence_path": row.get("evidence_path"),
            "last_probed_at": row.get("last_probed_at"),
        })
    return tools


def main() -> None:
    desktop = collect(DESKTOP_ROOT, "desktop-library")
    runtime = collect(RUNTIME_ROOT, "codex-runtime")
    plugins = [item for root in PLUGIN_ROOTS for item in collect(root, "plugin-runtime")]
    tools = collect_tools()

    runtime_by_name = {item["name"]: item["path"] for item in runtime}
    for item in desktop + plugins:
        item["runtime_path"] = runtime_by_name.get(item["name"])
        item["callable_status"] = "RUNTIME_REGISTERED" if item["runtime_path"] else "VISIBLE_ONLY"

    catalog = {
        "schema_version": "1.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "roots": {
            "desktop_library": str(DESKTOP_ROOT),
            "codex_runtime": str(RUNTIME_ROOT),
            "plugin_runtime": [str(root) for root in PLUGIN_ROOTS],
        },
        "counts": {
            "desktop_entries": len(desktop),
            "runtime_entries": len(runtime),
            "plugin_entries": len(plugins),
            "tool_entries": len(tools),
        },
        "skills": runtime + desktop + plugins,
        "tools": tools,
    }
    (DESKTOP_ROOT / "skills-catalog.json").write_text(
        json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    lines = [
        "# 茂茂 Skill 总检索",
        "",
        f"> 自动生成时间：{catalog['generated_at']}",
        "> 机器可读正本：`skills-catalog.json`",
        "> 重建命令：`python build_skill_catalog.py`（Windows）或 `python3 build_skill_catalog.py`（macOS/Linux）",
        "",
        "## 使用规则",
        "",
        "1. 总经理开工前先读 `skills-catalog.json`，按目标语义选择 Skill，不靠用户记关键词。",
        "2. `RUNTIME_REGISTERED` 表示已有 Codex 运行入口；`VISIBLE_ONLY` 只表示桌面资料存在，不能冒充可执行。",
        "3. 同一 Skill 有多个桌面副本时，以 `runtime_path` 指向的正本为准。",
        "",
        "## 运行入口",
        "",
        "| 名称 | 调用 | 运行正本 | 状态 |",
        "|---|---|---|---|",
    ]
    for item in runtime:
        lines.append(f"| {item['name']} | `${item['name']}` | `{item['path']}` | RUNTIME_REGISTERED |")
    lines.extend(["", "## 桌面资料条目", ""])
    for item in desktop:
        lines.append(f"- `{item['name']}` — `{item['path']}` — {item['callable_status']}")
    lines.extend(["", "## 当前工具与员工能力", "", "| 员工/工具 | 职能 | 状态 | 证据 |", "|---|---|---|---|"])
    for item in tools:
        lines.append(f"| `{item['id']}` / `{item['skill_or_tool']}` | {item['role']} | `{item['state']}` | `{item.get('evidence_path')}` |")
    (DESKTOP_ROOT / "SKILL-总检索.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps(catalog["counts"], ensure_ascii=False))


if __name__ == "__main__":
    main()
