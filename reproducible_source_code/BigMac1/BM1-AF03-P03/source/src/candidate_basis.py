#!/usr/bin/env python3
"""Enumerate Lentfer's candidate monomials from Definition 3.1.

This module uses only the Python standard library.  A monomial is represented
by ``(x_exponents, theta_mask, xi_mask)`` with one-based variable indices in
the mathematical description and zero-based bits internally.
"""

from __future__ import annotations

import argparse
import itertools
import json
from collections import Counter
from pathlib import Path


def popcount(mask: int) -> int:
    return mask.bit_count()


def valid_motzkin_masks(n: int):
    """Yield the pairs (T,S) defining modified Motzkin paths of length n."""
    if n < 1:
        return
    # The first step is forced to be up, hence neither first bit can occur.
    for theta_mask in range(1 << n):
        if theta_mask & 1:
            continue
        for xi_mask in range(1 << n):
            if xi_mask & 1:
                continue
            height = 0
            valid = True
            for i in range(n):
                in_t = bool(theta_mask & (1 << i))
                in_s = bool(xi_mask & (1 << i))
                if not in_t and not in_s:
                    height += 1
                elif in_t and in_s:
                    height -= 1
                # Exactly one membership is a decorated horizontal step.
                if i == 0:
                    valid = not in_t and not in_s and height == 1
                elif height < 1:
                    valid = False
                if not valid:
                    break
            if valid:
                yield theta_mask, xi_mask


def alpha_sequence(n: int, theta_mask: int, xi_mask: int) -> tuple[int, ...]:
    alpha = [0]
    for i in range(1, n):
        value = (
            alpha[-1]
            - 1
            + int(not bool(theta_mask & (1 << i)))
            + int(not bool(xi_mask & (1 << i)))
        )
        alpha.append(value)
    return tuple(alpha)


def candidate_monomials(n: int):
    for theta_mask, xi_mask in valid_motzkin_masks(n):
        bounds = alpha_sequence(n, theta_mask, xi_mask)
        assert min(bounds) >= 0
        for exponents in itertools.product(*(range(a + 1) for a in bounds)):
            yield tuple(exponents), theta_mask, xi_mask


def singular_monomial(n: int, monomial) -> str:
    exponents, theta_mask, xi_mask = monomial
    factors: list[str] = []
    for i, exponent in enumerate(exponents, 1):
        if exponent == 1:
            factors.append(f"x{i}")
        elif exponent > 1:
            factors.append(f"x{i}^{exponent}")
    factors.extend(f"t{i + 1}" for i in range(n) if theta_mask & (1 << i))
    factors.extend(f"z{i + 1}" for i in range(n) if xi_mask & (1 << i))
    return "*".join(factors) if factors else "1"


def polarized_power_sum_generators(n: int):
    """Return the 4n finite generators as sparse monomial sums."""
    generators = []
    for r in range(1, n + 1):
        terms = []
        for i in range(n):
            exponents = [0] * n
            exponents[i] = r
            terms.append({"coefficient": 1, "x": exponents, "theta_mask": 0, "xi_mask": 0})
        generators.append({"name": f"p_{r},1", "terms": terms})
    for species, theta_bit, xi_bit in (("theta", True, False), ("xi", False, True), ("theta_xi", True, True)):
        for r in range(n):
            terms = []
            for i in range(n):
                exponents = [0] * n
                exponents[i] = r
                terms.append(
                    {
                        "coefficient": 1,
                        "x": exponents,
                        "theta_mask": (1 << i) if theta_bit else 0,
                        "xi_mask": (1 << i) if xi_bit else 0,
                    }
                )
            generators.append({"name": f"p_{r},{species}", "terms": terms})
    return generators


def singular_check_script(n: int, order: str = "dp", determinant: bool = False) -> str:
    variables = (
        [f"x{i}" for i in range(1, n + 1)]
        + [f"t{i}" for i in range(1, n + 1)]
        + [f"z{i}" for i in range(1, n + 1)]
    )
    gens: list[str] = []
    gens.extend("+".join(f"x{i}^{r}" for i in range(1, n + 1)) for r in range(1, n + 1))
    for odd in ("t", "z"):
        gens.extend(
            "+".join((f"x{i}^{r}*" if r else "") + f"{odd}{i}" for i in range(1, n + 1))
            for r in range(n)
        )
    gens.extend(
        "+".join((f"x{i}^{r}*" if r else "") + f"t{i}*z{i}" for i in range(1, n + 1))
        for r in range(n)
    )
    candidates = [singular_monomial(n, monomial) for monomial in candidate_monomials(n)]
    lines = [
            'LIB "nctools.lib";',
            f"ring R=0,({','.join(variables)}),{order};",
            f"def A=superCommutative({n + 1},{3 * n}); setring A;",
            "ideal I=" + ",\n".join(gens) + ";",
            "ideal G=twostd(I);",
            "ideal C=" + ",\n".join(candidates) + ";",
            "ideal N=reduce(C,G); ideal K=kbase(G);",
            "matrix M=coeffs(N,K); int candidateRank=rank(M);",
            "int unchanged=0; int vanished=0; int i; poly r;",
            "for(i=1;i<=size(C);i++){r=reduce(C[i],G); if(r==C[i]){unchanged++;}; if(r==0){vanished++;};};",
            'print("n=' + str(n) + ' candidates="+string(size(C))+" vdim="+string(vdim(G))+" std-size="+string(size(G))+" candidate-rank="+string(candidateRank)+" unchanged="+string(unchanged)+" vanished="+string(vanished));',
            "exit;",
        ]
    if determinant:
        lines.insert(-2, 'number candidateDeterminant=det(M); print("candidate-determinant="+string(candidateDeterminant));')
    return "\n".join(lines) + "\n"


def singular_dimension_script(n: int, order: str = "dp") -> str:
    """Emit an exact quotient-dimension exploration without candidate ranks."""
    variables = (
        [f"x{i}" for i in range(1, n + 1)]
        + [f"t{i}" for i in range(1, n + 1)]
        + [f"z{i}" for i in range(1, n + 1)]
    )
    gens: list[str] = []
    gens.extend("+".join(f"x{i}^{r}" for i in range(1, n + 1)) for r in range(1, n + 1))
    for odd in ("t", "z"):
        gens.extend(
            "+".join((f"x{i}^{r}*" if r else "") + f"{odd}{i}" for i in range(1, n + 1))
            for r in range(n)
        )
    gens.extend(
        "+".join((f"x{i}^{r}*" if r else "") + f"t{i}*z{i}" for i in range(1, n + 1))
        for r in range(n)
    )
    return "\n".join(
        [
            'LIB "nctools.lib";',
            f"ring R=0,({','.join(variables)}),{order};",
            f"def A=superCommutative({n + 1},{3 * n}); setring A;",
            "ideal I=" + ",\n".join(gens) + ";",
            "ideal G=twostd(I);",
            'print("n=' + str(n) + ' generators="+string(size(I))+" vdim="+string(vdim(G))+" std-size="+string(size(G)));',
            "exit;",
        ]
    ) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--singular", action="store_true")
    parser.add_argument("--dimension-only", action="store_true")
    parser.add_argument("--order", default="dp")
    parser.add_argument("--determinant", action="store_true")
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    if args.dimension_only:
        print(singular_dimension_script(args.n, args.order), end="")
        return 0
    mons = list(candidate_monomials(args.n))
    expected = (2 ** (args.n - 1)) * __import__("math").factorial(args.n)
    if len(mons) != expected:
        raise SystemExit(f"candidate count {len(mons)} != expected {expected}")
    if args.singular:
        print(singular_check_script(args.n, args.order, args.determinant), end="")
        return 0
    blocks = Counter((sum(exp), popcount(t), popcount(s)) for exp, t, s in mons)
    payload = {
        "schema_version": 1,
        "field": "QQ",
        "n": args.n,
        "count": len(mons),
        "term_order": "dp",
        "invariant_generators": polarized_power_sum_generators(args.n),
        "monomials": [
            {"x": list(exp), "theta_mask": t, "xi_mask": s}
            for exp, t, s in mons
        ],
        "block_counts": {",".join(map(str, key)): value for key, value in sorted(blocks.items())},
    }
    text = json.dumps(payload, sort_keys=True, indent=2) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
