#!/usr/bin/env python3
"""Consume a startup route receipt before any self-built generation adapter.

This gate only controls callers that use this adapter. It does not claim to
block native Codex/MCP/browser entry points; those remain HOST_UNKNOWN until
tested separately.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def decide(receipt: dict, action: str) -> dict:
    reasons = []
    inventory = receipt.get("company_inventory", {})
    if inventory.get("inventory_status") != "PASS":
        reasons.append(f"company inventory status={inventory.get('inventory_status', 'MISSING')}")
    if not inventory.get("inventory_sha256") or not inventory.get("roster_sha256"):
        reasons.append("company inventory hash/roster hash missing")
    if action == "video-gen" and receipt.get("route_id") in {"edit_only", "consult_only", "knowledge_short", "RESEARCH_REQUIRED"}:
        reasons.append(f"route {receipt.get('route_id')} does not authorize video generation")
    if action == "video-gen" and receipt.get("signals", {}).get("wrong_method_claim"):
        reasons.append("wrong_method_claim=true: must complete route correction artifacts before generation")
    direction = receipt.get("capability_plan", {}).get("direction_audit", {})
    if action == "video-gen" and direction.get("verdict") in {"WRONG_PROBLEM", "NEEDS_RESEARCH", "NEEDS_CEO_DECISION", "DIRECTION_CANDIDATE", "DIRECTION_REVIEW_REQUIRED"}:
        reasons.append(f"direction audit verdict={direction.get('verdict')}")
    if action == "video-gen" and receipt.get("capability_plan", {}).get("missing_tools"):
        reasons.append("capability map reports missing tools; research/vet/install/probe required before production")
    if action == "video-gen" and receipt.get("hard_stop_before_paid_generation"):
        reasons.append("startup route is hard-stopped: missing/unknown/unprobed dependency or evidence")
    if not receipt.get("route_spec_sha256"):
        reasons.append("route specification hash missing")
    if action == "video-gen":
        for item in receipt.get("must_load", []):
            if item.get("state") != "CALLABLE":
                reasons.append(f"{item.get('skill')}: state={item.get('state')}")
    return {
        "action": action,
        "decision": "BLOCKED" if reasons else "ALLOW_ADAPTER_ONLY",
        "reasons": reasons,
        "host_native_entrypoints": "UNKNOWN",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--receipt", required=True)
    parser.add_argument("--action", choices=["plan", "video-gen"], required=True)
    args = parser.parse_args()
    path = Path(args.receipt)
    if not path.exists():
        result = {"action": args.action, "decision": "BLOCKED", "reasons": ["startup receipt missing"], "host_native_entrypoints": "UNKNOWN"}
    else:
        result = decide(json.loads(path.read_text(encoding="utf-8")), args.action)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["decision"] != "BLOCKED" else 2


if __name__ == "__main__":
    raise SystemExit(main())
