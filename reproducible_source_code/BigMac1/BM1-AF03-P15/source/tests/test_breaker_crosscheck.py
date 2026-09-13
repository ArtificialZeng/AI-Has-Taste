#!/usr/bin/env python3
"""Regression tests binding formula-level and element-level breaker audits."""

from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, relative: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


ELEMENT = load_module("breaker_element_verifier", "tests/verify_breaker_element_certificate.py")
ORBIT = load_module("breaker_orbit_verifier", "tests/verify_breaker_orbit_candidate.py")


class BreakerCrossCheck(unittest.TestCase):
    def test_element_certificates(self) -> None:
        for n in (4, 5, 6):
            data = json.loads((ROOT / f"discovery/breaker_d{n}_element_audit.json").read_text())
            self.assertEqual(ELEMENT.verify(data)["status"], "ACCEPT")

    def test_generic_cell_degrees_match_complete_enumeration(self) -> None:
        for n in (4, 5, 6):
            data = json.loads((ROOT / f"discovery/breaker_d{n}_element_audit.json").read_text())
            observed = {}
            for rank_pair in data["rank_pairs"]:
                for edge in rank_pair["support"]:
                    observed[(edge["lower"], edge["upper"])] = (
                        edge["edge_count"],
                        edge["out_degree"],
                        edge["in_degree"],
                    )
            expected = {}
            for lower in ORBIT.all_types(n):
                for upper, out_degree in ORBIT.generic_upper_degrees(lower).items():
                    edge_count = ORBIT.class_size(n, lower) * out_degree
                    in_degree = edge_count // ORBIT.class_size(n, upper)
                    expected[(ORBIT.key(lower), ORBIT.key(upper))] = (
                        edge_count,
                        out_degree,
                        in_degree,
                    )
            self.assertEqual(observed, expected)

    def test_d4_through_d9_orbit_candidates(self) -> None:
        for n in range(4, 10):
            data = json.loads((ROOT / f"discovery/d{n}_orbit_flow_candidate.json").read_text())
            self.assertEqual(ORBIT.verify(data)["status"], "ACCEPT")

    def test_independently_accepted_flows_equal_release_certificates(self) -> None:
        def release_key(value: str) -> str:
            positive, negative = value.split("|")
            return f"P[{positive}]N[{negative}]"

        for n in range(4, 10):
            audited = json.loads((ROOT / f"discovery/d{n}_orbit_flow_candidate.json").read_text())
            if n == 4:
                release_path = ROOT / "certificates/d4_baseline_flow.json"
            elif n == 8:
                release_path = ROOT / "experiments/d8_baseline_flow.json"
            elif n == 9:
                release_path = ROOT / "certificates/d9_normalized_flow.json"
            else:
                release_path = ROOT / f"experiments/d{n}_orbit_flow.json"
            release = json.loads(release_path.read_text())
            audited_flows = {
                (flow["lower"], flow["upper"]): (flow["numerator"], flow["denominator"])
                for pair in audited["rank_pairs"]
                for flow in pair["flows"]
            }
            release_flows = {
                (release_key(flow["from"]), release_key(flow["to"])):
                (flow["numerator"], flow["denominator"])
                for layer in release["layers"]
                for flow in layer["flows"]
            }
            self.assertEqual(audited_flows, release_flows, f"D_{n} flow mismatch")


if __name__ == "__main__":
    unittest.main()
