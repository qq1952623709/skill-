#!/usr/bin/env python3
"""Read-only company roster and inventory gate.

Presence is not availability.  This module validates the machine-readable
roster, hashes the authoritative files, and returns a conservative status for
startup_adapter/generation_gate.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path

COMPANY_ROOT = Path(os.environ.get("AI_ANIMATION_COMPANY_ROOT", Path.home() / "Documents" / "AI动画公司")).expanduser()
CONTROL_ROOT = COMPANY_ROOT / "00_公司总控"
ROSTER = CONTROL_ROOT / "roster.jsonl"
CAPABILITY_MAP = CONTROL_ROOT / "capability_map.json"
CAPABILITY_GRAPH = CONTROL_ROOT / "总经理能力导图_20260906.md"
AUTHORITATIVE = [
    COMPANY_ROOT / "README.md",
    COMPANY_ROOT / "STATE.md",
    CONTROL_ROOT / "OWNER.md",
    CONTROL_ROOT / "公司级禁令.md",
    CONTROL_ROOT / "能力等级与成长路线.md",
    ROSTER,
    CAPABILITY_MAP,
    CAPABILITY_GRAPH,
]
ALLOWED_STATES = {"CALLABLE", "BLOCKED", "MISSING", "UNKNOWN"}
REQUIRED = {"id", "role", "skill_or_tool", "inputs", "actions", "outputs", "acceptance", "state", "evidence_path", "last_probed_at"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def check_inventory() -> dict:
    missing_files = [str(path) for path in AUTHORITATIVE if not path.exists()]
    records = []
    errors = []
    if ROSTER.exists():
        for line_no, raw in enumerate(ROSTER.read_text(encoding="utf-8").splitlines(), 1):
            if not raw.strip():
                continue
            try:
                record = json.loads(raw)
            except json.JSONDecodeError as exc:
                errors.append(f"roster line {line_no}: {exc}")
                continue
            if not isinstance(record, dict):
                errors.append(f"roster line {line_no}: record is not object")
                continue
            missing = sorted(REQUIRED - set(record))
            if missing:
                errors.append(f"roster line {line_no}: missing {missing}")
            if record.get("state") not in ALLOWED_STATES:
                errors.append(f"roster line {line_no}: invalid state {record.get('state')}")
            if not isinstance(record.get("inputs"), list) or not isinstance(record.get("actions"), list) or not isinstance(record.get("outputs"), list) or not isinstance(record.get("acceptance"), list):
                errors.append(f"roster line {line_no}: inputs/actions/outputs/acceptance must be arrays")
            records.append(record)
    else:
        errors.append("roster.jsonl missing")
    duplicate_ids = sorted({record.get("id") for record in records if record.get("id") and sum(1 for x in records if x.get("id") == record.get("id")) > 1})
    if duplicate_ids:
        errors.append(f"duplicate ids: {duplicate_ids}")
    if CAPABILITY_MAP.exists():
        try:
            capability_map = json.loads(CAPABILITY_MAP.read_text(encoding="utf-8"))
            if not isinstance(capability_map, dict) or not isinstance(capability_map.get("task_families"), list) or not capability_map.get("task_families"):
                errors.append("capability_map.json: task_families must be a non-empty array")
            else:
                family_ids = [x.get("id") for x in capability_map["task_families"] if isinstance(x, dict)]
                if len(family_ids) != len(set(family_ids)):
                    errors.append("capability_map.json: duplicate task family ids")
        except json.JSONDecodeError as exc:
            errors.append(f"capability_map.json: invalid JSON: {exc}")
    file_hashes = {str(path): sha256(path) for path in AUTHORITATIVE if path.exists()}
    material = "\n".join(f"{path}:{file_hashes.get(str(path), 'MISSING')}" for path in AUTHORITATIVE)
    inventory_sha256 = hashlib.sha256(material.encode("utf-8")).hexdigest()
    status = "PASS" if not missing_files and not errors and records else "BLOCKED"
    return {
        "inventory_status": status,
        "inventory_path": str(CONTROL_ROOT),
        "roster_path": str(ROSTER),
        "roster_count": len(records),
        "roster_sha256": sha256(ROSTER) if ROSTER.exists() else None,
        "inventory_sha256": inventory_sha256,
        "authoritative_file_hashes": file_hashes,
        "missing_files": missing_files,
        "validation_errors": errors,
        "checked_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "evidence_level": "OBSERVED" if status == "PASS" else "BLOCKED",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = check_inventory()
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["inventory_status"] == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
