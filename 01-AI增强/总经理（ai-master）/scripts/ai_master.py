#!/usr/bin/env python3
"""Deterministic local control plane for AI Master V1.1."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List


SOURCE_FIELDS = (
    "source_id", "title", "locator", "observed_date", "information_status", "claim"
)
RUN_FIELDS = (
    "run_id", "problem", "environment", "method", "input", "action", "artifact",
    "evidence", "failures", "corrections", "time", "cost", "human_intervention",
    "result", "would_run_again",
)
FAILURE_FIELDS = (
    "failure_id", "task", "environment", "symptom", "root_cause", "wrong_assumption",
    "fix", "permanent_constraint", "regression_test", "affected_method", "status",
)

MARKETING_PATTERNS = (
    "1000倍", "一千倍", "永久免费", "免费claude code", "一周赚几千",
    "一个人替代几十人", "3–5天变40分钟", "3-5天变40分钟",
)
DUPLICATE_SAMPLE_PATTERNS = (
    "先测试一个样本", "先测一个样本", "先做一个样本", "golden unit",
    "minimum proof before scale",
)
HIGH_RISK_PATTERNS = (
    "付款", "支付", "群发", "发布", "删除", "生产环境", "密钥", "权限变更", "credential",
)


class ValidationError(ValueError):
    pass


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def stable_id(prefix: str, text: str) -> str:
    return f"{prefix}-{hashlib.sha256(text.encode('utf-8')).hexdigest()[:12].upper()}"


def load_json(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValidationError(f"{path} must contain one JSON object")
    return value


def require_fields(record: Dict[str, Any], fields: Iterable[str], label: str) -> None:
    missing = [field for field in fields if field not in record]
    empty = [
        field for field in fields
        if field in record and record[field] is None
        or field in record and isinstance(record[field], str) and not record[field].strip()
    ]
    if missing or empty:
        raise ValidationError(f"{label}: missing={missing}, empty={empty}")


def append_jsonl(path: Path, record: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")


def read_jsonl(path: Path) -> List[Dict[str, Any]]:
    if not path.exists():
        return []
    records: List[Dict[str, Any]] = []
    for line_no, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        try:
            value = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise ValidationError(f"{path}:{line_no}: {exc}") from exc
        if not isinstance(value, dict):
            raise ValidationError(f"{path}:{line_no}: expected JSON object")
        records.append(value)
    return records


def validate_capability(record: Dict[str, Any]) -> None:
    required = (
        "capability_id", "capability_name", "problem_solved", "model_or_tool", "input",
        "output", "can_do", "cannot_guarantee", "required_permission",
        "required_environment", "minimum_probe", "pass_condition", "fail_condition",
        "evidence_level", "applicable_scope", "failure_boundary", "version", "source",
        "last_verified", "status", "evidence",
    )
    require_fields(record, required[:-3] + ("status",), "capability")
    allowed = {"CLAIMED", "OBSERVED", "PROVEN", "PARTIAL", "UNSUPPORTED", "BLOCKED"}
    if record["status"] not in allowed:
        raise ValidationError(f"capability: invalid status {record['status']}")
    if record["status"] == "PROVEN":
        if not str(record.get("evidence", "")).strip():
            raise ValidationError("capability: PROVEN requires non-empty evidence")
        if not str(record.get("last_verified", "")).strip():
            raise ValidationError("capability: PROVEN requires last_verified")


def audit_source(record: Dict[str, Any]) -> Dict[str, Any]:
    require_fields(record, SOURCE_FIELDS, "source")
    status = record["information_status"]
    if status not in {"OBSERVED", "REPORTED", "INFERRED", "UNKNOWN"}:
        raise ValidationError(f"source: invalid information_status {status}")
    claim = str(record["claim"])
    folded = claim.casefold()
    result = dict(record)
    result.setdefault("synthetic", False)
    result["audited_at"] = utc_now()
    if any(pattern.casefold() in folded for pattern in MARKETING_PATTERNS):
        result.update({
            "decision": "REJECTED_FOR_CORE",
            "evidence_level": "MARKETING_OR_ANECDOTAL_CLAIM",
            "reason": "量化或绝对化宣传缺少可复算对照证据",
        })
    elif any(pattern.casefold() in folded for pattern in DUPLICATE_SAMPLE_PATTERNS):
        result.update({
            "decision": "MAP_TO_EXISTING",
            "mapped_to": "CORE-03/MINIMUM_PROOF_BEFORE_SCALE",
            "evidence_level": "DUPLICATE_METHOD_CLAIM",
            "reason": "与既有Golden Unit/最小验证规则同义",
        })
    elif status in {"REPORTED", "UNKNOWN"} and any(
        word in folded for word in ("支持", "可以", "能够", "capability")
    ):
        result.update({
            "decision": "NEEDS_REALITY_PROBE",
            "evidence_level": status,
            "reason": "产品能力主张缺少当前环境的直接观察",
        })
    else:
        result.update({
            "decision": "CANDIDATE",
            "evidence_level": status,
            "reason": "通过基础过滤，但尚未获得真实运行证据",
        })
    return result


def generate_probe(product: str, claim: str, environment: str = "UNVERIFIED") -> Dict[str, Any]:
    if not product.strip() or not claim.strip():
        raise ValidationError("probe: product and claim are required")
    seed = f"{product}|{claim}|{environment}"
    return {
        "probe_id": stable_id("PROBE", seed),
        "status": "UNKNOWN_NEEDS_REALITY_PROBE",
        "product": product,
        "claim": claim,
        "environment": environment,
        "action": f"在{product}的真实可用环境中，只执行一个足以证明或证伪该主张的最小动作",
        "success": "产生与主张直接对应、可重复观察的结果及证据地址",
        "failure": "明确失败、功能不存在、权限不足，或结果不能直接支持主张",
        "evidence": "保存环境、动作、可观察行为、制品、截图/日志、错误和限制",
        "limits": {
            "max_actions": 5,
            "max_runtime_minutes": 10,
            "max_retries": 2,
            "max_files": 3,
            "max_spend": 0,
        },
        "stop": [
            "登录或权限不可用",
            "需要付款、发布、删除、生产修改或凭据变更",
            "同一根因连续失败3次",
            "超过任一探针上限",
        ],
    }


def choose_complexity(request: str) -> str:
    folded = request.casefold()
    simple = ("润色", "改一句", "翻译", "摘要", "改写一封", "写一封邮件")
    if len(request) < 160 and any(token in folded for token in simple):
        return "DIRECT_REQUEST"
    if any(token in folded for token in ("长期", "批量", "多系统", "恢复", "多agent", "多 agent")):
        return "HARNESS_REVIEW_REQUIRED"
    return "STRUCTURED_INSTRUCTION"


def permission_decision(request: str) -> Dict[str, Any]:
    matches = [token for token in HIGH_RISK_PATTERNS if token.casefold() in request.casefold()]
    return {
        "human_approval_required": bool(matches),
        "risk_signals": matches,
        "autonomous_preparation_allowed": True,
    }


def validate_run(record: Dict[str, Any]) -> None:
    require_fields(record, RUN_FIELDS, "verified_run")
    if record["result"] not in {"PASS", "FAIL", "PARTIAL"}:
        raise ValidationError("verified_run: result must be PASS, FAIL or PARTIAL")
    if not isinstance(record["would_run_again"], bool):
        raise ValidationError("verified_run: would_run_again must be boolean")


def validate_failure(record: Dict[str, Any]) -> None:
    require_fields(record, FAILURE_FIELDS, "failure")
    if record["status"] not in {"OPEN", "MITIGATED", "VERIFIED_FIXED", "DEFERRED"}:
        raise ValidationError("failure: invalid status")


def final_artifact_verdict(node_results: List[str], final_artifact_ok: bool) -> str:
    return "PASS" if node_results and all(x == "PASS" for x in node_results) and final_artifact_ok else "FAIL"


def method_competition(methods: List[str], real_metrics_available: bool) -> str:
    if len(methods) < 2:
        return "NO_COMPETITION"
    return "SELECT_BY_EVIDENCE" if real_metrics_available else "BENCHMARK_REQUIRED"


def run_benchmarks(root: Path) -> Dict[str, Any]:
    cases: List[Dict[str, Any]] = []

    def check(name: str, observed: Any, expected: Any) -> None:
        cases.append({"name": name, "passed": observed == expected, "observed": observed, "expected": expected})

    marketing = audit_source({
        "source_id": "SYN-001", "title": "synthetic marketing fixture", "locator": "fixture://marketing",
        "observed_date": "2026-09-04", "information_status": "REPORTED",
        "claim": "一款AI工具让生产力提高1000倍。", "synthetic": True,
    })
    check("1_marketing_filter", marketing["decision"], "REJECTED_FOR_CORE")

    duplicate = audit_source({
        "source_id": "SYN-002", "title": "synthetic duplicate fixture", "locator": "fixture://duplicate",
        "observed_date": "2026-09-04", "information_status": "OBSERVED",
        "claim": "新文章说先测试一个样本。", "synthetic": True,
    })
    check("2_duplicate_mapping", duplicate["decision"], "MAP_TO_EXISTING")

    probe = generate_probe("Grok Bot", "是否支持X？")
    check("3_unknown_capability", probe["status"], "UNKNOWN_NEEDS_REALITY_PROBE")

    check("4_complexity_control", choose_complexity("帮我润色一封邮件。"), "DIRECT_REQUEST")

    gate = permission_decision("自动给客户群发并付款。")
    check("5_high_risk_permission", gate["human_approval_required"], True)

    failure_fixture = {
        "failure_id": "FAIL-SYN-001", "task": "synthetic", "environment": "fixture",
        "symptom": "输出错误", "root_cause": "边界未校验", "wrong_assumption": "节点通过等于最终通过",
        "fix": "增加最终制品复验", "permanent_constraint": "最终制品必须独立验收",
        "regression_test": "最终制品错误时整体必须FAIL", "affected_method": "M-19", "status": "MITIGATED",
    }
    try:
        validate_failure(failure_fixture)
        failure_result = all(bool(failure_fixture[key]) for key in ("root_cause", "permanent_constraint", "regression_test"))
    except ValidationError:
        failure_result = False
    check("6_failure_changes_system", failure_result, True)

    check("7_final_artifact_reverification", final_artifact_verdict(["PASS", "PASS"], False), "FAIL")

    check("8_method_competition", method_competition(["A", "B"], False), "BENCHMARK_REQUIRED")

    negative = {"name": "invariant_proven_requires_evidence", "passed": False}
    cap = {
        "capability_id": "CAP-SYN", "capability_name": "synthetic", "problem_solved": "test",
        "model_or_tool": "fixture", "input": "x", "output": "y", "can_do": "x",
        "cannot_guarantee": "y", "required_permission": "none", "required_environment": "fixture",
        "minimum_probe": "one", "pass_condition": "pass", "fail_condition": "fail",
        "evidence_level": "NONE", "applicable_scope": "fixture", "failure_boundary": "fixture",
        "version": "1", "source": "fixture", "last_verified": "", "status": "PROVEN", "evidence": "",
    }
    try:
        validate_capability(cap)
    except ValidationError:
        negative["passed"] = True
    negative["observed"] = "REJECTED" if negative["passed"] else "ACCEPTED"
    negative["expected"] = "REJECTED"

    passed = sum(1 for case in cases if case["passed"])
    report = {
        "system": "ai-master",
        "version": "2.1.0",
        "generated_at": utc_now(),
        "fixture_policy": "All synthetic inputs are explicitly marked and are not real-world evidence.",
        "passed": passed,
        "failed": len(cases) - passed,
        "total": len(cases),
        "cases": cases,
        "invariants": [negative],
        "overall": "PASS" if passed == len(cases) and negative["passed"] else "FAIL",
    }
    report_path = root / "BENCHMARKS" / "benchmark_report.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    state_path = root / "PROJECT_STATE" / "MASTER_STATE.json"
    if state_path.exists():
        state = load_json(state_path)
        state["status"] = "READY" if report["overall"] == "PASS" else "BENCHMARK_FAILED"
        state["updated_at"] = utc_now()
        state["last_benchmark_report"] = str(report_path.relative_to(root))
        state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return report


def status(root: Path) -> Dict[str, Any]:
    registry_paths = {
        "methods": root / "METHOD_REGISTRY" / "methods.jsonl",
        "capabilities": root / "CAPABILITY_REGISTRY" / "capabilities.jsonl",
        "sources": root / "SOURCE_LIBRARY" / "source_index.jsonl",
        "products": root / "PRODUCT_RADAR" / "products.jsonl",
        "verified_runs": root / "VERIFIED_RUNS" / "runs.jsonl",
        "failures": root / "FAILURE_LIBRARY" / "failures.jsonl",
    }
    counts = {name: len(read_jsonl(path)) for name, path in registry_paths.items()}
    state_path = root / "PROJECT_STATE" / "MASTER_STATE.json"
    return {"root": str(root), "state": load_json(state_path) if state_path.exists() else {}, "counts": counts}


def auto_route(root: Path, request: str) -> Dict[str, Any]:
    configured_root = os.environ.get("AI_MANAGER_ROOT") or os.environ.get("AI_COMPANY_ROOT")
    default_root = "D:/Codex/AI总经理个人总控" if os.name == "nt" else str(Path.home() / "AI总经理个人总控")
    route_path = Path(configured_root or default_root) / "CAPABILITY_REGISTRY" / "skill_routes.json"
    if not route_path.exists():
        route_path = root / "CAPABILITY_REGISTRY" / "skill_routes.json"
    routes = load_json(route_path).get("routes", []) if route_path.exists() else []
    folded = unicodedata.normalize("NFKC", request).casefold()
    selected = []
    for route in routes:
        score = sum(1 for term in route.get("when", [])
                    if unicodedata.normalize("NFKC", term).casefold() in folded)
        if score:
            selected.append((score, route))
    selected.sort(key=lambda item: (-item[0], item[1].get("id", "")))
    skills, seen = [], set()
    for _, route in selected:
        for name in [route.get("skill", ""), *route.get("load_with", [])]:
            if name and name not in seen:
                skills.append(name); seen.add(name)
    return {"request": request, "registry": str(route_path),
            "route_ids": [r.get("id") for _, r in selected],
            "selected_skills": skills,
            "matched": [{"id": r.get("id"), "skill": r.get("skill"), "score": s} for s, r in selected],
            "status": "ROUTED" if skills else "NO_MATCH_REQUIRES_GENERAL_REASONING"}


def animation_script(name: str) -> Path:
    codex_home = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex")).expanduser()
    candidates = [
        Path(__file__).resolve().parents[2] / "maomao-animation-studio" / "scripts" / name,
        codex_home / "skills" / "personal" / "maomao-animation-studio" / "scripts" / name,
    ]
    return next((path for path in candidates if path.exists()), candidates[0])


def inventory_check() -> Dict[str, Any]:
    script = animation_script("inventory_check.py")
    if not script.exists():
        raise ValidationError(f"personal inventory checker missing: {script}")
    proc = subprocess.run([sys.executable, str(script), "--json"], capture_output=True, text=True, encoding="utf-8", env={**os.environ, "PYTHONIOENCODING": "utf-8"}, check=False)
    try:
        output = json.loads(proc.stdout)
    except json.JSONDecodeError as exc:
        raise ValidationError(f"personal inventory checker returned invalid JSON: {proc.stdout[-500:]}") from exc
    output["control_plane_exit_code"] = proc.returncode
    return output


def capability_preflight(request: str, route_id: str | None = None) -> Dict[str, Any]:
    script = animation_script("capability_map.py")
    if not script.exists():
        raise ValidationError(f"capability map resolver missing: {script}")
    command = [sys.executable, str(script), request]
    if route_id:
        command.extend(["--route-id", route_id])
    proc = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", env={**os.environ, "PYTHONIOENCODING": "utf-8"}, check=False)
    try:
        output = json.loads(proc.stdout)
    except json.JSONDecodeError as exc:
        detail = (proc.stderr or proc.stdout)[-500:]
        raise ValidationError(f"capability resolver failed (exit {proc.returncode}): {detail}") from exc
    output["control_plane_exit_code"] = proc.returncode
    return output


def tool_gap_contract(tools: List[str]) -> Dict[str, Any]:
    script = Path(__file__).resolve().parent / "tool_gap.py"
    proc = subprocess.run([sys.executable, str(script), *tools], capture_output=True, text=True, encoding="utf-8", env={**os.environ, "PYTHONIOENCODING": "utf-8"}, check=False)
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError as exc:
        raise ValidationError(f"tool gap contract returned invalid JSON: {proc.stdout[-500:]}") from exc


def write_json(path: Path, value: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="AI Master V1.1 deterministic local CLI")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    commands = parser.add_subparsers(dest="command", required=True)

    commands.add_parser("benchmark")
    commands.add_parser("status")
    commands.add_parser("inventory-check")
    route = commands.add_parser("auto-route")
    route.add_argument("--request", required=True)

    preflight = commands.add_parser("preflight")
    preflight.add_argument("--request", required=True)
    preflight.add_argument("--route-id")

    gap = commands.add_parser("tool-gap")
    gap.add_argument("tools", nargs="+")

    audit = commands.add_parser("audit-source")
    audit.add_argument("--input", type=Path, required=True)
    audit.add_argument("--commit", action="store_true")

    probe = commands.add_parser("probe-contract")
    probe.add_argument("--product", required=True)
    probe.add_argument("--claim", required=True)
    probe.add_argument("--environment", default="UNVERIFIED")
    probe.add_argument("--output", type=Path)

    run = commands.add_parser("record-run")
    run.add_argument("--input", type=Path, required=True)
    run.add_argument("--commit", action="store_true")

    failure = commands.add_parser("record-failure")
    failure.add_argument("--input", type=Path, required=True)
    failure.add_argument("--commit", action="store_true")
    return parser


def main(argv: List[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = args.root.resolve()
    try:
        if args.command == "benchmark":
            output = run_benchmarks(root)
        elif args.command == "status":
            output = status(root)
        elif args.command == "inventory-check":
            output = inventory_check()
        elif args.command == "auto-route":
            output = auto_route(root, args.request)
        elif args.command == "preflight":
            output = capability_preflight(args.request, args.route_id)
        elif args.command == "tool-gap":
            output = tool_gap_contract(args.tools)
        elif args.command == "audit-source":
            output = audit_source(load_json(args.input))
            if args.commit:
                append_jsonl(root / "SOURCE_LIBRARY" / "source_index.jsonl", output)
        elif args.command == "probe-contract":
            output = generate_probe(args.product, args.claim, args.environment)
            destination = args.output or root / "BENCHMARKS" / "capability_probes" / f"{output['probe_id']}.json"
            write_json(destination, output)
            output = dict(output, output_path=str(destination))
        elif args.command == "record-run":
            output = load_json(args.input)
            validate_run(output)
            if args.commit:
                append_jsonl(root / "VERIFIED_RUNS" / "runs.jsonl", output)
        elif args.command == "record-failure":
            output = load_json(args.input)
            validate_failure(output)
            if args.commit:
                append_jsonl(root / "FAILURE_LIBRARY" / "failures.jsonl", output)
        else:
            raise ValidationError(f"unknown command {args.command}")
    except (OSError, json.JSONDecodeError, ValidationError) as exc:
        print(json.dumps({"status": "ERROR", "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2
    print(json.dumps(output, ensure_ascii=False, indent=2))
    if args.command == "inventory-check" and output.get("inventory_status") != "PASS":
        return 2
    if args.command == "preflight" and output.get("status") != "READY_FOR_PLAN":
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
