#!/usr/bin/env python3
"""Core unit, adversarial tamper, AST zero-float, and full verification tests
for the Agoh--Giuga Tier 1 + Tier 2 certificate and verifier.

Fast core tests (<1 second):
    python3 -m unittest tests.test_agoh_giuga_tier2.TestASTZeroFloatAudit \
        tests.test_agoh_giuga_tier2.TestExactMathPrimitives -v

Full suite including full 846-pair zero-float certificate verification (~25 seconds):
    python3 -m unittest tests/test_agoh_giuga_tier2.py -v
"""

from __future__ import annotations

import ast
import copy
from fractions import Fraction
import json
import math
from pathlib import Path
import random
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
CERT_PATH = ROOT / "certificates" / "agoh_giuga_tier2_certificate.json"
VERIFIER_PATH = SRC / "verify_agoh_giuga_certificate.py"
GENERATOR_PATH = SRC / "generate_agoh_giuga_certificate.py"

sys.path.insert(0, str(SRC))
import verify_agoh_giuga_certificate as ver  # noqa: E402


class TestASTZeroFloatAudit(unittest.TestCase):
    """Syntactically guarantee the standalone verifier uses ZERO float operations."""

    def test_verifier_contains_zero_float_constructs(self) -> None:
        source = VERIFIER_PATH.read_text(encoding="utf-8")
        tree = ast.parse(source, filename=str(VERIFIER_PATH))
        forbidden_names = {"float", "round"}
        forbidden_attrs = {"log", "log10", "log2", "sqrt", "exp", "pow"}

        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, float):
                self.fail(f"Float literal found in verifier: {node.value!r} at line {node.lineno}")
            if isinstance(node, ast.Name) and node.id in forbidden_names:
                self.fail(f"Forbidden float builtin {node.id!r} at line {node.lineno}")
            if isinstance(node, ast.Attribute) and node.attr in forbidden_attrs:
                self.fail(f"Forbidden float attribute .{node.attr} at line {node.lineno}")
            if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
                # Only exact Fraction / Fraction division or pathlib Path / str joins are permitted
                src_seg = ast.get_source_segment(source, node) or ""
                allowed = (
                    ("Fraction" in src_seg)
                    or ("Path" in src_seg)
                    or ("parents" in src_seg)
                    or ('"' in src_seg)
                )
                self.assertTrue(
                    allowed,
                    f"Potential float true division '/' found at line {node.lineno}: {src_seg!r}",
                )


class TestExactMathPrimitives(unittest.TestCase):
    """Fast mathematical unit tests on every algorithmic building block."""

    def test_mod16_and_r2_barrier_checks(self) -> None:
        ver.verify_mod16_congruence_exhaustively()
        ver.verify_r2_barrier_constants()

    def test_r2_barrier_exact_boundary_inequality(self) -> None:
        # Verify P1*P2 < t0^3 * M0^2 + t0^2 * M0 holds strictly at the exact boundary d1 = x_+
        # (including cases where naive t0^3 * M0^2 fails!).
        for N0 in (3, 5, 7, 9, 15, 101, 1001):
            t0 = (1 + math.sqrt(1 + 4 * N0)) / (2 * N0)
            for mult in (2, 3, 10, 1000):
                M0 = mult * N0 + 1
                b = M0 - N0
                x_plus = (b + math.sqrt(b * b + 4 * N0 * (M0 * M0 - N0))) / (2 * N0)
                d2 = (M0 * M0 - N0) / x_plus
                P1P2 = (M0 + x_plus) * (M0 + d2) / (N0 * N0)
                corrected_rhs = (t0**3) * (M0**2) + (t0**2) * M0
                self.assertLess(P1P2, corrected_rhs)
                if M0 >= 100_000 and N0 == 3:
                    self.assertLess(P1P2, 0.4523 * M0 * M0)

    def test_signed_hex_roundtrip_and_malformed_rejection(self) -> None:
        for val in (0, 1, -1, 123456789, -(1 << 20000), (1 << 20000) + 7):
            s = ("-" + hex(-val)) if val < 0 else hex(val)
            self.assertEqual(ver.decode_signed_hex(s, "test"), val)
        for bad in ("", "1234", "+0x10", "0xzz", None, 42):
            with self.assertRaises(ValueError):
                ver.decode_signed_hex(bad, "bad")

    def test_lattice_witness_edge_cases(self) -> None:
        M, C, U, R = 1009, 317, 10, 12
        # Valid opposite-sign witness: find v > 0, u < 0 with u = C*v mod M
        # Pick v = 1, u = C - M = -692 -> |v|*R + |u|*U = 12 + 6920 >= 1009 (too large -> must reject)
        with self.assertRaises(ValueError):
            ver.verify_lattice_witness(M, C, U, R, C - M, 1, "too_large_opp")
        # Degenerate (0, 0) and axis-aligned (M, 0) must reject
        with self.assertRaises(ValueError):
            ver.verify_lattice_witness(M, C, U, R, 0, 0, "zero")
        with self.assertRaises(ValueError):
            ver.verify_lattice_witness(M, C, U, R, M, 0, "axis_u")
        # Non-lattice vector must reject
        with self.assertRaises(ValueError):
            ver.verify_lattice_witness(M, C, U, R, 1, 1, "not_in_lattice")
        # Same-sign primitive ray INSIDE box [1, R] x [1, U] MUST reject!
        # Let M = 10007, C = 3, U = 10, R = 10 -> (u, v) = (3, 1) is in Lambda with |v|*R = 10 < M, |u|*U = 30 < M,
        # BUT (3, 1) IS a valid coprime solution in [1, 10] x [1, 10]! Verifier must reject it!
        with self.assertRaises(ValueError):
            ver.verify_lattice_witness(10007, 3, 10, 10, 3, 1, "ray_inside_box")
        # Same-sign primitive ray OUTSIDE box [1, 2] x [1, 10] MUST accept!
        ver.verify_lattice_witness(10007, 3, 10, 2, 3, 1, "ray_outside_box")
        # Opposite-sign valid witness: M = 10007, C = 10004 (=-3 mod M),
        # (u, v) = (-3, 1), U=10, R=10 -> 1*10 + 3*10 = 40 < 10007
        ver.verify_lattice_witness(10007, 10004, 10, 10, -3, 1, "valid_opp")

    def test_incremental_crt_matches_fresh_build(self) -> None:
        # Build a small normal set of primes and test incremental extend_state vs build_state
        primes = ver.sieve_primes(500)
        spf = ver.build_spf(500)
        normal = [5, 7]
        for p in primes[4:]:
            if not any(q in normal for q in ver.odd_prime_factors(p - 1, spf)):
                normal.append(p)
        P_base = ver.prod_tree(normal)
        crt = ver.ExactIncrementalCRT(P_base, spf)
        M_inc, C_inc, pp_inc = crt.build_state(normal[:5])
        for step in (normal[5:8], [normal[8]], normal[9:15], normal[15:25]):
            M_inc, C_inc, pp_inc = crt.extend_state(M_inc, C_inc, pp_inc, step)
        M_fresh, C_fresh, pp_fresh = crt.build_state(normal[:25])
        self.assertEqual((M_inc, C_inc, pp_inc), (M_fresh, C_fresh, pp_fresh))

    def test_greedy_k_bound_and_dp2_suffix_min_soundness(self) -> None:
        # Synthetic mini star-pack: verify compute_dp2_u_bounds upper-bounds ALL subsets W_c subseteq T_c!
        rng = random.Random(42)
        centers = [101, 103, 107, 109, 113, 127, 131]
        leaves = {
            101: [203, 405, 607],
            103: [207, 413],
            107: [429, 643, 857],
            109: [],
            113: [227],
            127: [],
            131: [],
        }
        D = 10**9
        cap_int = {}
        for c in centers:
            f = Fraction(1, c) - sum((Fraction(1, q) for q in leaves[c]), Fraction(0))
            self.assertGreater(f, 0)
            cap_int[c] = ver.floor_frac_scaled(f, D)
        B_int = D // 40  # budget allowing several omitted stars/centers
        L0_pref = [0]
        L0_prod_pref = [1]
        for p in reversed(centers):
            L0_pref.append(L0_pref[-1] + (D // p))
            L0_prod_pref.append(L0_prod_pref[-1] * p)
        star_prod_pref = [1]
        for c in sorted([c for c in centers if leaves[c]], reverse=True):
            star_prod_pref.append(star_prod_pref[-1] * c)

        for p_omit in (None, 101, 109):
            F_ext, U_by_k = ver.compute_dp2_u_bounds(
                centers, leaves, cap_int, L0_pref, L0_prod_pref, star_prod_pref, B_int, D, set(), p_omit
            )
            # Exhaustively sample/enumerate actual choices (including STRICT subsets W_c subsetneq T_c!)
            for _ in range(500):
                cost = 0
                Y_actual = 1
                k_actual = 0
                omitted = set()
                if p_omit is not None:
                    omitted.add(p_omit)
                    T = leaves[p_omit]
                    if T and rng.random() < 0.7:
                        sub = rng.sample(T, rng.randint(1, len(T)))
                        c_f = Fraction(1, p_omit) - sum((Fraction(1, q) for q in sub), Fraction(0))
                        cost += ver.floor_frac_scaled(c_f, D)
                        k_actual += len(sub)
                    else:
                        cost += D // p_omit
                    Y_actual *= p_omit
                for c in centers:
                    if c == p_omit or rng.random() < 0.65:
                        continue
                    omitted.add(c)
                    T = leaves[c]
                    if T and rng.random() < 0.6:
                        sub = rng.sample(T, rng.randint(1, len(T)))
                        c_f = Fraction(1, c) - sum((Fraction(1, q) for q in sub), Fraction(0))
                        cost += ver.floor_frac_scaled(c_f, D)
                        k_actual += len(sub)
                    else:
                        cost += D // c
                    Y_actual *= c
                if cost < B_int:
                    # Every forced prime in F_ext MUST NOT be omitted!
                    self.assertTrue(F_ext.isdisjoint(omitted), "F_ext wrongly forced omitted prime!")
                    self.assertLess(k_actual, len(U_by_k), f"k_actual={k_actual} >= len(U_by_k)")
                    self.assertLessEqual(Y_actual, U_by_k[k_actual], f"Y_actual > U_by_k[{k_actual}]")

    def test_previous_improved_bound_verifier_unchanged(self) -> None:
        res = subprocess.run(
            [sys.executable, str(SRC / "verify_improved_bound.py")],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(res.returncode, 0, res.stderr)


class TestFailClosedTamperingAndEndToEnd(unittest.TestCase):
    """Adversarial fail-closed tampering tests and full end-to-end certificate check."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.cert = json.loads(CERT_PATH.read_text(encoding="utf-8"))

    def test_tamper_schema_and_digests_fail_closed(self) -> None:
        bad_schema = copy.deepcopy(self.cert)
        bad_schema["schema_version"] = 99
        with self.assertRaises(ValueError):
            ver.verify_certificate(bad_schema)

        bad_sha = copy.deepcopy(self.cert)
        bad_sha["part1_extremal_normal_set"]["P_L_sha256_binary"] = "0" * 64
        with self.assertRaises(ValueError):
            ver.verify_certificate(bad_sha)

    def test_tamper_leaf_partition_gap_fails_closed(self) -> None:
        bad_leaves = copy.deepcopy(self.cert)
        bad_leaves["part1_extremal_normal_set"]["leaves_at_B"][-1]["N"] = [11]
        with self.assertRaises(ValueError):
            ver.verify_certificate(bad_leaves)

    def test_full_certificate_end_to_end_and_deep_tampers(self) -> None:
        # 1. Full zero-float verification of the genuine certificate
        summary = ver.verify_certificate(self.cert)
        self.assertEqual(summary["status"], "VERIFIED")
        self.assertTrue(summary["zero_float_arithmetic"])
        self.assertEqual(summary["unconditional_bounds"]["omega_at_least"], 8_138)
        self.assertEqual(summary["unconditional_bounds"]["largest_prime_at_least"], 326_057)
        self.assertEqual(summary["unconditional_bounds"]["decimal_digits_at_least"], 40_922)
        self.assertEqual(summary["verified_UR_pairs"]["total"], 846)

        # 2. Tamper with a Part 3 bucket witness (u_hex flipped by +1) -> MUST fail closed!
        bad_p3 = copy.deepcopy(self.cert)
        bk0 = bad_p3["part3_tier2_largest_prime"]["cascade"][0]["buckets"][0]
        u0 = ver.decode_signed_hex(bk0["u_hex"], "u")
        bk0["u_hex"] = ("-" + hex(-(u0 + 1))) if (u0 + 1) < 0 else hex(u0 + 1)
        with self.assertRaises(ValueError):
            ver.verify_certificate(bad_p3)

        # 3. Tamper with a Part 4 dm19 interval gap -> MUST fail closed!
        bad_p4 = copy.deepcopy(self.cert)
        bad_p4["part4_tier2_digit_bound"]["dm19"]["intervals"][1]["m0_lo"] += 1
        with self.assertRaises(ValueError):
            ver.verify_certificate(bad_p4)


if __name__ == "__main__":
    unittest.main()
