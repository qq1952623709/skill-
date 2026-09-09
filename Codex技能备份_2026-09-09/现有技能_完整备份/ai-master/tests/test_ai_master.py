import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "ai_master.py"
SPEC = importlib.util.spec_from_file_location("ai_master", MODULE_PATH)
ai_master = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(ai_master)


class AIMasterTests(unittest.TestCase):
    def test_marketing_is_not_core(self):
        result = ai_master.audit_source({
            "source_id": "S1", "title": "fixture", "locator": "fixture://one",
            "observed_date": "2026-09-04", "information_status": "REPORTED",
            "claim": "生产力提高1000倍", "synthetic": True,
        })
        self.assertEqual(result["decision"], "REJECTED_FOR_CORE")

    def test_duplicate_maps_to_existing(self):
        result = ai_master.audit_source({
            "source_id": "S2", "title": "fixture", "locator": "fixture://two",
            "observed_date": "2026-09-04", "information_status": "OBSERVED",
            "claim": "先测试一个样本", "synthetic": True,
        })
        self.assertEqual(result["decision"], "MAP_TO_EXISTING")

    def test_unknown_capability_creates_bounded_probe(self):
        probe = ai_master.generate_probe("Example", "支持X吗")
        self.assertEqual(probe["status"], "UNKNOWN_NEEDS_REALITY_PROBE")
        self.assertLessEqual(probe["limits"]["max_actions"], 5)
        self.assertGreater(len(probe["stop"]), 0)

    def test_proven_requires_evidence_and_date(self):
        record = json.loads((Path(__file__).parent / "fixtures" / "capability_without_evidence.json").read_text(encoding="utf-8"))
        with self.assertRaises(ai_master.ValidationError):
            ai_master.validate_capability(record)

    def test_final_artifact_can_fail_after_nodes_pass(self):
        self.assertEqual(ai_master.final_artifact_verdict(["PASS", "PASS"], False), "FAIL")

    def test_benchmarks_all_pass(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "PROJECT_STATE").mkdir(parents=True)
            (root / "PROJECT_STATE" / "MASTER_STATE.json").write_text(
                json.dumps({"status": "BUILDING"}), encoding="utf-8"
            )
            report = ai_master.run_benchmarks(root)
            self.assertEqual(report["total"], 8)
            self.assertEqual(report["failed"], 0)
            self.assertEqual(report["overall"], "PASS")


if __name__ == "__main__":
    unittest.main()
