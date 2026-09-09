#!/usr/bin/env python3
"""Run the startup route and persist the receipt for downstream gates."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from route_check import route  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("request")
    parser.add_argument("--receipt", required=True)
    parser.add_argument("--reference")
    args = parser.parse_args()
    result = route(args.request, args.reference)
    path = Path(args.receipt)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    inventory = result.get("company_inventory", {})
    plan = result.get("capability_plan", {})
    direction = plan.get("direction_audit", {})
    print(json.dumps({"receipt": str(path), "route_id": result["route_id"], "task_family": plan.get("task_family"), "inventory_status": inventory.get("inventory_status"), "inventory_sha256": inventory.get("inventory_sha256"), "capability_map_sha256": plan.get("capability_map_sha256"), "direction_verdict": direction.get("verdict"), "hard_stop_before_paid_generation": result["hard_stop_before_paid_generation"]}, ensure_ascii=False))
    return 0 if inventory.get("inventory_status") == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
