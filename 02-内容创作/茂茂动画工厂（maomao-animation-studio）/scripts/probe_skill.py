#!/usr/bin/env python3
"""Conservative, no-cost capability probe for one employee/skill/tool."""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOTS = [
    Path("/Users/xingxuan/.codex/skills"),
    Path("/Users/xingxuan/.codex/plugins/cache/chatcut-inc/chatcut/0.2.26/skills"),
]


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def find_skill(name: str) -> Path | None:
    for root in ROOTS:
        candidates = [root / name / "SKILL.md"]
        if ":" in name:
            candidates.append(root / name.split(":", 1)[1] / "SKILL.md")
        for candidate in candidates:
            if candidate.exists():
                return candidate
    return None


def probe(name: str) -> dict:
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    if name == "Blender" or name.lower() == "blender":
        binary = Path("/Applications/Blender.app/Contents/MacOS/Blender")
        if not binary.exists():
            return {"name": name, "state": "MISSING", "reason": "Blender binary not found", "checked_at": now}
        proc = subprocess.run([str(binary), "--version"], capture_output=True, text=True, check=False)
        return {"name": name, "state": "CALLABLE" if proc.returncode == 0 else "BLOCKED", "probe": [str(binary), "--version"], "returncode": proc.returncode, "stdout": proc.stdout.strip(), "checked_at": now}
    path = find_skill(name)
    if not path:
        return {"name": name, "state": "MISSING", "reason": "SKILL.md not found in configured roots", "checked_at": now}
    if ":" in name:
        state = "UNKNOWN"
        reason = "hosted plugin is present on disk; current MCP/host invocation was not attempted"
    else:
        state = "UNKNOWN"
        reason = "SKILL.md was read and hashed; no execution adapter was invoked by this no-cost probe"
    return {"name": name, "state": state, "skill_path": str(path), "skill_sha256": digest(path), "reason": reason, "checked_at": now}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("name")
    args = parser.parse_args()
    result = probe(args.name)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["state"] == "CALLABLE" else 2


if __name__ == "__main__":
    raise SystemExit(main())
