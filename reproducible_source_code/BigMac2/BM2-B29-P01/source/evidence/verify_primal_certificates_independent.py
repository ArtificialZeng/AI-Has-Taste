#!/Users/mac/4prove-or-disprove-math/.research-venv/bin/python
"""Independent exact replay of both positive claims in source.md."""

from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path

from verify_d7_farkas_independent import (
    SCALE, exact_rows, independent_hadamard_matrix,
)


MIXED = Path("evidence/mixed_d6_rational_point.json")
GAUSS = Path("evidence/gauss_d7_rational_point.json")
REPORT = Path("evidence/primal_certificates_verification.json")


def read_sparse(path: Path, count: int, expected_format: str):
    raw = path.read_bytes()
    payload = json.loads(raw)
    if payload["format"] != expected_format or payload["counts"]["variables_total"] != count:
        raise AssertionError("wrong point format or dimension")
    values = [Fraction(0)] * count
    seen = set()
    for item in payload["nonzero_values"]:
        j = item["variable"]
        if not isinstance(j, int) or not 0 <= j < count or j in seen:
            raise AssertionError("invalid or duplicate point coordinate")
        seen.add(j)
        q = Fraction(*item["value"])
        if q == 0:
            raise AssertionError("listed sparse coordinate is zero")
        values[j] = q
    if len(seen) != payload["counts"]["nonzero_values"]:
        raise AssertionError("wrong sparse count")
    return payload, values, hashlib.sha256(raw).hexdigest()


def kraw(j: int, w: int) -> int:
    return sum((-1)**ell * math.comb(w, ell) * math.comb(20-w, j-ell)
               for ell in range(max(0, j-(20-w)), min(j, w)+1))


def verify_mixed():
    payload, point, digest = read_sparse(MIXED, 1813, "mixed-d6-rational-point-v1")
    if payload["parameters"] != {"n": 20, "k": 8, "d": 6}:
        raise AssertionError("wrong mixed parameters")
    index, transform = independent_hadamard_matrix()
    rows, m0 = exact_rows(index, distance=6)
    common = 1
    for q in point:
        common = math.lcm(common, q.denominator)
    scaled = [q.numerator * (common // q.denominator) for q in point]
    for name, sparse, rhs, target in rows:
        if sparse is not None:
            lhs = sum(value * scaled[j] for j, value in sparse.items())
        else:
            lhs = SCALE * scaled[m0 + target]
            lhs -= sum(int(value) * scaled[m0 + si]
                       for si, value in enumerate(transform[target]) if value)
        if lhs != rhs * common:
            raise AssertionError(f"mixed equality failed: {name}")
    if min(scaled) < 0:
        raise AssertionError("mixed point has a negative coordinate")
    for w in range(1, 21):
        if scaled[w] + scaled[21+w] > math.comb(20, w) * common:
            raise AssertionError(f"mixed packing row {w} failed")
    return {
        "point_sha256": digest, "variables": 1813, "nonzero": sum(q != 0 for q in point),
        "equalities_replayed": len(rows), "packing_rows_replayed": 20,
        "joint_coefficients_generated": int(transform.size),
        "common_denominator_bits": common.bit_length(), "all_rows_pass": True,
    }


def verify_gauss():
    payload, x, digest = read_sparse(GAUSS, 42, "gauss-d7-rational-point-v1")
    expected_branch = {"tau": "O", "beta": 0, "eta": 0, "dual_tau": "O"}
    if payload["parameters"] != {"n": 20, "k": 8, "d": 7} or payload["branch"] != expected_branch:
        raise AssertionError("wrong Gauss parameters or branch")
    if min(x) < 0 or x[0] != 1 or x[21] != 1:
        raise AssertionError("Gauss normalization/nonnegativity failed")
    for w in range(1, 7):
        if x[w] != 0:
            raise AssertionError("Gauss distance zero failed")
    for j in range(21):
        if 256*x[21+j] != sum(x[w]*kraw(j, w) for w in range(21)):
            raise AssertionError(f"Gauss MacWilliams row {j} failed")
    for w in range(1, 21):
        if x[w] + x[21+w] > math.comb(20, w):
            raise AssertionError(f"Gauss packing row {w} failed")
    if x[20] != 0:
        raise AssertionError("Gauss eta row failed")
    targets = {0: 72, 1: 64, 2: 56}
    for residue, rhs in targets.items():
        if sum(x[w] for w in range(residue, 21, 4)) != rhs:
            raise AssertionError(f"Gauss phase row {residue} failed")
    # (O,O) is allowed and (20-beta) mod 8 = 4 lies in B_O(12).
    return {
        "point_sha256": digest, "branch": expected_branch,
        "branch_admissible": True, "variables": 42,
        "nonzero": sum(q != 0 for q in x), "normalization_rows": 2,
        "distance_rows": 6, "MacWilliams_rows": 21,
        "packing_rows": 20, "eta_rows": 1, "phase_rows": 3,
        "all_rows_pass": True,
    }


def main() -> None:
    report = {
        "format": "primal-certificates-independent-verification-v1",
        "verdict": "pass",
        "generator": "standalone exact generator, with no import from mixed_lp_search.py",
        "mixed_d6": verify_mixed(),
        "gauss_d7": verify_gauss(),
        "conclusion": "M_2(20,8,6) and the (O,0,0) branch of G_2(20,8,7) are nonempty over the rationals.",
    }
    REPORT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
