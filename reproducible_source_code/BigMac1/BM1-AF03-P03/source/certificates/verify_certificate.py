#!/usr/bin/env python3
"""Fail-closed verifier for the finite Lentfer basis certificate.

The verifier is deliberately standalone: it imports no discovery module and
reconstructs both Definition 3.1 and the 4n polarized-power-sum input from the
serialized JSON.  Singular performs exact standard-basis and matrix-rank
arithmetic over QQ; no floating-point or modular inference is used.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import tempfile


ALLOWED_TOP_KEYS = {
    "schema_version",
    "field",
    "n",
    "count",
    "term_order",
    "invariant_generators",
    "monomials",
    "block_counts",
}


class VerificationError(RuntimeError):
    pass


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def expected_candidates(n: int):
    if not 1 <= n <= 5:
        raise VerificationError("this finite verifier is restricted to 1 <= n <= 5")
    result = []
    for theta_mask in range(1 << n):
        if theta_mask & 1:
            continue
        for xi_mask in range(1 << n):
            if xi_mask & 1:
                continue
            height = 0
            alpha = [0]
            valid = True
            for i in range(n):
                in_theta = bool(theta_mask & (1 << i))
                in_xi = bool(xi_mask & (1 << i))
                if not in_theta and not in_xi:
                    height += 1
                elif in_theta and in_xi:
                    height -= 1
                if i == 0:
                    valid = not in_theta and not in_xi and height == 1
                elif height < 1:
                    valid = False
                if not valid:
                    break
                if i >= 1:
                    alpha.append(alpha[-1] - 1 + int(not in_theta) + int(not in_xi))
            if not valid:
                continue
            if len(alpha) != n or min(alpha) < 0:
                raise VerificationError("internal Motzkin/alpha reconstruction failed")
            for exponents in itertools.product(*(range(bound + 1) for bound in alpha)):
                result.append((tuple(exponents), theta_mask, xi_mask))
    return result


def expected_generators(n: int):
    result = []
    for r in range(1, n + 1):
        terms = []
        for i in range(n):
            x = [0] * n
            x[i] = r
            terms.append((1, tuple(x), 0, 0))
        result.append((f"p_{r},1", tuple(terms)))
    for species, has_theta, has_xi in (
        ("theta", True, False),
        ("xi", False, True),
        ("theta_xi", True, True),
    ):
        for r in range(n):
            terms = []
            for i in range(n):
                x = [0] * n
                x[i] = r
                terms.append(
                    (
                        1,
                        tuple(x),
                        (1 << i) if has_theta else 0,
                        (1 << i) if has_xi else 0,
                    )
                )
            result.append((f"p_{r},{species}", tuple(terms)))
    return result


def parse_monomial(raw, n: int):
    if not isinstance(raw, dict) or set(raw) != {"x", "theta_mask", "xi_mask"}:
        raise VerificationError("malformed candidate monomial")
    x = raw["x"]
    t = raw["theta_mask"]
    z = raw["xi_mask"]
    if (
        not isinstance(x, list)
        or len(x) != n
        or any(type(value) is not int or value < 0 for value in x)
        or type(t) is not int
        or type(z) is not int
        or not 0 <= t < (1 << n)
        or not 0 <= z < (1 << n)
    ):
        raise VerificationError("candidate exponent or mask is out of range")
    return tuple(x), t, z


def parse_generator(raw, n: int):
    if not isinstance(raw, dict) or set(raw) != {"name", "terms"}:
        raise VerificationError("malformed invariant generator")
    if not isinstance(raw["name"], str) or not isinstance(raw["terms"], list):
        raise VerificationError("malformed generator name/terms")
    terms = []
    for term in raw["terms"]:
        if not isinstance(term, dict) or set(term) != {"coefficient", "x", "theta_mask", "xi_mask"}:
            raise VerificationError("malformed generator term")
        coefficient = term["coefficient"]
        if type(coefficient) is not int:
            raise VerificationError("nonintegral generator coefficient")
        monomial = parse_monomial(
            {"x": term["x"], "theta_mask": term["theta_mask"], "xi_mask": term["xi_mask"]},
            n,
        )
        terms.append((coefficient, *monomial))
    return raw["name"], tuple(terms)


def block_counts(monomials):
    counts = {}
    for x, t, z in monomials:
        key = f"{sum(x)},{t.bit_count()},{z.bit_count()}"
        counts[key] = counts.get(key, 0) + 1
    return dict(sorted(counts.items(), key=lambda item: tuple(map(int, item[0].split(",")))))


def factor_string(n: int, monomial) -> str:
    x, theta_mask, xi_mask = monomial
    factors = []
    for i, exponent in enumerate(x, 1):
        if exponent == 1:
            factors.append(f"x{i}")
        elif exponent > 1:
            factors.append(f"x{i}^{exponent}")
    factors.extend(f"t{i + 1}" for i in range(n) if theta_mask & (1 << i))
    factors.extend(f"z{i + 1}" for i in range(n) if xi_mask & (1 << i))
    return "*".join(factors) if factors else "1"


def polynomial_string(n: int, terms) -> str:
    pieces = []
    for coefficient, x, theta_mask, xi_mask in terms:
        if coefficient == 0:
            continue
        monomial = factor_string(n, (x, theta_mask, xi_mask))
        if not pieces:
            prefix = "-" if coefficient < 0 else ""
        else:
            prefix = "+" if coefficient > 0 else "-"
        magnitude = abs(coefficient)
        scalar = "" if magnitude == 1 and monomial != "1" else str(magnitude)
        multiplication = "*" if scalar and monomial != "1" else ""
        pieces.append(prefix + scalar + multiplication + monomial)
    if not pieces:
        raise VerificationError("zero generator is forbidden")
    return "".join(pieces)


def singular_program(n: int, generators, candidates, term_order: str) -> str:
    variables = (
        [f"x{i}" for i in range(1, n + 1)]
        + [f"t{i}" for i in range(1, n + 1)]
        + [f"z{i}" for i in range(1, n + 1)]
    )
    generator_strings = [polynomial_string(n, terms) for _, terms in generators]
    candidate_strings = [factor_string(n, monomial) for monomial in candidates]
    return "\n".join(
        [
            'LIB "nctools.lib";',
            f"ring R=0,({','.join(variables)}),{term_order};",
            f"def A=superCommutative({n + 1},{3 * n}); setring A;",
            "ideal I=" + ",\n".join(generator_strings) + ";",
            "ideal G=twostd(I);",
            "ideal RI=reduce(I,G); int j;",
            "for(j=1;j<=size(RI);j++){if(RI[j]!=0){print(\"FAIL generator reduction\"); exit;};};",
            "ideal C=" + ",\n".join(candidate_strings) + ";",
            "ideal N=reduce(C,G); ideal K=kbase(G);",
            "matrix M=coeffs(N,K);",
            "if(matrix(K)*M!=matrix(N)){print(\"FAIL coordinate reconstruction\"); exit(18);};",
            "int r=rank(M); int d=vdim(G);",
            'print("CERT n=' + str(n) + ' generators="+string(size(I))+" candidates="+string(size(C))+" vdim="+string(d)+" rank="+string(r)+" std-size="+string(size(G)));',
            "exit;",
        ]
    ) + "\n"


def load_and_validate(path: Path):
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise VerificationError(f"cannot parse certificate: {error}") from error
    if not isinstance(raw, dict) or set(raw) != ALLOWED_TOP_KEYS:
        raise VerificationError("unexpected or missing top-level certificate keys")
    if raw["schema_version"] != 1 or raw["field"] != "QQ" or raw["term_order"] != "dp":
        raise VerificationError("unsupported schema, field, or term order")
    n = raw["n"]
    if type(n) is not int or not 1 <= n <= 5:
        raise VerificationError("invalid finite n")
    candidates = [parse_monomial(item, n) for item in raw["monomials"]]
    if len(candidates) != len(set(candidates)):
        raise VerificationError("duplicate candidate monomial")
    expected = expected_candidates(n)
    if candidates != expected:
        raise VerificationError("serialized candidate list differs from Definition 3.1 reconstruction")
    expected_count = (2 ** (n - 1)) * math.factorial(n)
    if raw["count"] != expected_count or len(candidates) != expected_count:
        raise VerificationError("candidate cardinality mismatch")
    if raw["block_counts"] != block_counts(candidates):
        raise VerificationError("multidegree block count mismatch")
    generators = [parse_generator(item, n) for item in raw["invariant_generators"]]
    if generators != expected_generators(n):
        raise VerificationError("serialized generators differ from the 4n structural reduction")
    return n, generators, candidates, raw["term_order"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--singular", default="/opt/homebrew/bin/Singular")
    args = parser.parse_args()
    certificate = args.certificate.resolve()
    try:
        n, generators, candidates, term_order = load_and_validate(certificate)
        if not os.path.isfile(args.singular) or not os.access(args.singular, os.X_OK):
            raise VerificationError("Singular executable is unavailable")
        program = singular_program(n, generators, candidates, term_order)
        with tempfile.TemporaryDirectory(prefix="lentfer-cert-") as directory:
            script = Path(directory) / "verify.sing"
            script.write_text(program, encoding="utf-8")
            completed = subprocess.run(
                [args.singular, "-q", str(script)],
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                timeout=300,
                check=False,
            )
        output = completed.stdout.strip()
        if completed.returncode != 0 or "?" in output or "FAIL" in output:
            raise VerificationError(f"Singular failed closed (code {completed.returncode}): {output}")
        expected_line = (
            f"CERT n={n} generators={4 * n} candidates={len(candidates)} "
            f"vdim={len(candidates)} rank={len(candidates)}"
        )
        if not any(line.startswith(expected_line) for line in output.splitlines()):
            raise VerificationError(f"unexpected exact result: {output}")
        version = subprocess.run(
            [args.singular, "-v"], text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=30
        ).stdout.splitlines()[0]
        print(
            "VERIFIED",
            f"n={n}",
            f"dimension={len(candidates)}",
            f"candidate_rank={len(candidates)}",
            f"input_sha256={sha256(certificate)}",
            f"verifier_sha256={sha256(Path(__file__).resolve())}",
            f"engine={version}",
        )
        return 0
    except (VerificationError, subprocess.SubprocessError) as error:
        print(f"REJECTED: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
