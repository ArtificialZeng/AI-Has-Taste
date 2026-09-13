#!/usr/bin/env python3
"""Fail-closed verifier for the Q5 empty-high-pair classification.

No project or discovery module is imported.  The verifier reconstructs the
empty-chamber numerator and the symmetric critical polynomial, recomputes six
three-value resultants and eight branch ideals in Singular, and independently
performs every stated Sturm count over ``fractions.Fraction``.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from fractions import Fraction
from pathlib import Path


class CertificateError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CertificateError(message)


def reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        require(key not in result, f"duplicate JSON key: {key}")
        result[key] = value
    return result


def reject_booleans(value: object, path: str = "$") -> None:
    require(type(value) is not bool, f"boolean forbidden in certificate at {path}")
    if type(value) is dict:
        for key, child in value.items():
            reject_booleans(child, f"{path}.{key}")
    elif type(value) is list:
        for index, child in enumerate(value):
            reject_booleans(child, f"{path}[{index}]")


EXPECTED_TOP_KEYS = {
    "certificate_type",
    "format_version",
    "theorem",
    "normalization",
    "empty_chamber",
    "symmetric_system",
    "factor_polynomials",
    "three_value_cases",
    "branch_groebner_bases",
    "sturm_checks",
    "branch_inequality_certificate",
    "two_value_certificate",
    "four_value_certificate",
    "closure_coverage",
}

EXPECTED_THEOREM = {
    "claim": "The only real full-support critical direction in the positive ordered closure of the empty high-pair chamber is the diagonal direction.",
    "scope": "a0>=a1>=a2>=a3>=a4>0 and ai+aj<=T for all pairs, with T=(a0+a1+a2+a3+a4)/2",
    "conclusion": "a0=a1=a2=a3=a4",
    "excluded": "zero-coordinate strata and all sign chambers having at least one strictly high pair",
}

EXPECTED_NORMALIZATION = {
    "sum": "a0+a1+a2+a3+a4=2",
    "pair_wall": "ai+aj=1",
    "order": "a0>=a1>=a2>=a3>=a4>0",
}

EXPECTED_EMPTY = {
    "high_pairs": [],
    "low_pair_closure": "ai+aj<=1 for every 0<=i<j<=4",
    "ordered_reduction": "a0+a1<=1",
}

EXPECTED_SYSTEM = {
    "P": "3*p1^4/8-3*p1^2*p2+3*p2^2+4*p1*p3-4*p4",
    "S": "p2",
    "Pi_at_x": "C0+C1*x+12*p1*x^2-16*x^3",
    "C0": "3*p1^3/2-6*p1*p2+4*p3",
    "C1": "-6*p1^2+12*p2",
    "q": "-16*S*x^4+12*p1*S*x^3+(C1*S+P)*x^2+C0*S*x-S*P",
    "critical_root_rule": "every coordinate value is a root of q",
    "degree_bound": 4,
}

EXPECTED_FACTORS = {
    "A4": [54, -72, 32, -4, 1],
    "A5": [334, -332, 52, 44, -19, 2],
    "A8": [200, -760, 1552, -1960, 1589, -758, 148, 40, 2],
    "B4": [3, 8, -64, 48, -8],
    "B5": [501, -1338, 1376, -688, 168, -16],
    "C4": [15, -36, 32, -16, -8],
    "D8": [72, -384, 2144, -2272, 1652, -1496, 852, -216, 19],
    "E8": [4800, -13440, 20608, -20736, 14960, -7312, 2176, -256, 19],
    "F2": [9, -8, 2],
    "F4": [40, -56, 32, -8, 1],
}

EXPECTED_CASES = [
    {
        "multiplicities": [1, 1, 3], "z": "(2-x-y)/3",
        "f_scale": [27, 2], "g_scale": [81, 2],
        "resultant_constant": -881596846080000,
        "resultant_factors": [["x", 4], ["half", 8], ["seven", 1], ["A4", 1], ["A8", 1]],
        "surviving_branches": ["half"],
    },
    {
        "multiplicities": [1, 2, 2], "z": "1-x/2-y",
        "f_scale": [4, 1], "g_scale": [8, 1],
        "resultant_constant": -33554432000,
        "resultant_factors": [["x", 4], ["B4", 2], ["C4", 2], ["B5", 1]],
        "surviving_branches": ["B4", "B5"],
    },
    {
        "multiplicities": [1, 3, 1], "z": "2-x-3*y",
        "f_scale": [1, 2], "g_scale": [1, 2],
        "resultant_constant": 14929920000,
        "resultant_factors": [["x", 4], ["half", 4], ["A4", 1], ["A5", 1], ["A8", 1]],
        "surviving_branches": ["half", "A5"],
    },
    {
        "multiplicities": [2, 1, 2], "z": "1-x-y/2",
        "f_scale": [4, 1], "g_scale": [8, 1],
        "resultant_constant": -11796480000,
        "resultant_factors": [["half", 8], ["seven", 1], ["D8", 1], ["E8", 1]],
        "surviving_branches": ["half"],
    },
    {
        "multiplicities": [2, 2, 1], "z": "2-2*x-2*y",
        "f_scale": [1, 2], "g_scale": [1, 2],
        "resultant_constant": -7680000,
        "resultant_factors": [["half", 4], ["B5", 1], ["D8", 1], ["E8", 1]],
        "surviving_branches": ["half"],
    },
    {
        "multiplicities": [3, 1, 1], "z": "2-3*x-y",
        "f_scale": [1, 2], "g_scale": [1, 6],
        "resultant_constant": -32000,
        "resultant_factors": [["half", 12], ["seven", 1], ["F2", 2], ["F4", 2]],
        "surviving_branches": ["half"],
    },
]

EXPECTED_BRANCHES = {
    "113_half": ["y^2", "2*x-1"],
    "122_B4": ["88*y^2+(44*x-88)*y-3*x^3+26*x^2-40*x+24", "B4"],
    "122_B5": ["3*x+2*y-2", "B5"],
    "131_half": ["2*y-1", "2*x-1"],
    "131_A5": ["2*x+3*y-2", "A5"],
    "212_half": ["y^2", "2*x-1"],
    "221_half": ["2*y-1", "2*x-1"],
    "311_half": ["y^2*(2*y-1)", "2*x-1"],
}

EXPECTED_STURM = [
    ["A4", [2, 5], [2, 3], 0], ["A8", [2, 5], [2, 3], 0],
    ["B4", [2, 5], [2, 3], 1], ["B4", [59, 100], [3, 5], 1],
    ["C4", [2, 5], [2, 3], 0], ["B5", [2, 5], [2, 3], 1],
    ["A5", [2, 5], [2, 3], 1], ["B5", [2, 5], [1, 2], 0],
    ["D8", [2, 5], [1, 2], 0], ["E8", [2, 5], [1, 2], 0],
    ["F2", [2, 5], [1, 2], 0], ["F4", [2, 5], [1, 2], 0],
]

EXPECTED_INEQUALITY = {
    "B4_isolating_interval": [[59, 100], [3, 5]],
    "ordered_root_condition": "y>(2-x)/4",
    "empty_condition": "y<=1-x",
    "boundary_value": "R_B4(x,1-x)=-3*x^3+70*x^2-84*x+24",
    "boundary_sign": "negative on [59/100,3/5]",
    "B5_collapse": "3*x+2*y-2=0 implies z=x",
    "A5_collapse": "2*x+3*y-2=0 implies z=x",
}

EXPECTED_TWO_VALUE = [
    {"large_multiplicity": 1, "range": [[1, 1], [2, 1]],
     "divided_difference": "15*r^4*(r-3)/8", "nonzero_reason": "r>=1 and r<=2"},
    {"large_multiplicity": 2, "range": [[1, 1], [3, 2]],
     "divided_difference": "5*(16*r^5-48*r^4+40*r^3-8*r^2-9*r+3)/8", "sturm_root_count": 0},
    {"large_multiplicity": 3, "range": [[1, 1], [2, 1]],
     "divided_difference": "5*(3*r^5-9*r^4-8*r^3+40*r^2-48*r+16)/8", "sturm_root_count": 0},
    {"large_multiplicity": 4, "range": [[1, 1], None],
     "divided_difference": "15*(1-3*r)/8", "nonzero_reason": "r>=1"},
]

EXPECTED_FOUR_VALUE = {
    "duplicated_value": "1/2", "other_values_sum": "x+y+z=1",
    "u": "x*y+x*z+y*z", "w": "x*y*z",
    "vieta_e4_identity": "P/16-w/2=(4*u-1)^2/64",
    "vieta_e3_identity": "C0/16-(w+u/2)=(4*u-4*w-1)/16",
    "contradiction": "e4 gives u=1/4; e3 then gives w=0, contradicting x*y*z>0",
}

EXPECTED_CLOSURE = {
    "included": ["positive coordinate-equality faces", "all pair walls incident to the empty chamber", "their intersections"],
    "wall_justification": "the paired truncated-power numerator is C^3 and adjacent first derivatives agree when a pair form is zero",
    "not_included": ["a4=0", "lower-support strata", "nonempty high-pair chambers"],
}


def load_and_validate(path: Path) -> dict:
    try:
        cert = json.loads(
            path.read_text(encoding="utf-8"), object_pairs_hook=reject_duplicate_keys
        )
    except (OSError, UnicodeError, json.JSONDecodeError, CertificateError) as exc:
        raise CertificateError(f"cannot read certificate: {exc}") from exc
    reject_booleans(cert)
    require(type(cert) is dict, "top level must be an object")
    require(set(cert) == EXPECTED_TOP_KEYS, "unexpected or missing top-level keys")
    require(cert["certificate_type"] == "q5_empty_highpair_chamber_classification", "wrong certificate type")
    require(type(cert["format_version"]) is int and cert["format_version"] == 1,
            "unsupported format version")
    require(cert["theorem"] == EXPECTED_THEOREM, "theorem endpoint changed")
    require(cert["normalization"] == EXPECTED_NORMALIZATION, "normalization changed")
    require(cert["empty_chamber"] == EXPECTED_EMPTY, "empty chamber changed")
    require(cert["symmetric_system"] == EXPECTED_SYSTEM, "critical system changed")
    require(cert["factor_polynomials"] == EXPECTED_FACTORS, "factor polynomials changed")
    require(cert["three_value_cases"] == EXPECTED_CASES, "three-value cases changed")
    require(cert["branch_groebner_bases"] == EXPECTED_BRANCHES, "branch bases changed")
    require(cert["sturm_checks"] == EXPECTED_STURM, "Sturm checks changed")
    require(cert["branch_inequality_certificate"] == EXPECTED_INEQUALITY, "inequality proof changed")
    require(cert["two_value_certificate"] == EXPECTED_TWO_VALUE, "two-value proof changed")
    require(cert["four_value_certificate"] == EXPECTED_FOUR_VALUE, "four-value proof changed")
    require(cert["closure_coverage"] == EXPECTED_CLOSURE, "closure scope changed")
    return cert


# Polynomials below are stored low degree first for exact Fraction arithmetic.
def trim(p: list[Fraction]) -> list[Fraction]:
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def derivative(p: list[Fraction]) -> list[Fraction]:
    return trim([Fraction(i) * p[i] for i in range(1, len(p))] or [Fraction(0)])


def divrem(a: list[Fraction], b: list[Fraction]) -> tuple[list[Fraction], list[Fraction]]:
    a = trim(a[:])
    b = trim(b[:])
    require(not (len(b) == 1 and b[0] == 0), "polynomial division by zero")
    if len(a) < len(b):
        return [Fraction(0)], a
    q = [Fraction(0)] * (len(a) - len(b) + 1)
    while not (len(a) == 1 and a[0] == 0) and len(a) >= len(b):
        d = len(a) - len(b)
        c = a[-1] / b[-1]
        q[d] += c
        for i, bi in enumerate(b):
            a[i + d] -= c * bi
        trim(a)
    return trim(q), trim(a)


def sturm_chain(high_coefficients: list[int]) -> list[list[Fraction]]:
    p = trim([Fraction(c) for c in reversed(high_coefficients)])
    require(len(p) >= 2, "Sturm polynomial must be nonconstant")
    chain = [p, derivative(p)]
    while not (len(chain[-1]) == 1 and chain[-1][0] == 0):
        _, rem = divrem(chain[-2], chain[-1])
        if len(rem) == 1 and rem[0] == 0:
            break
        chain.append([-c for c in rem])
    return chain


def evaluate(p: list[Fraction], x: Fraction) -> Fraction:
    value = Fraction(0)
    for coefficient in reversed(p):
        value = value * x + coefficient
    return value


def variations(chain: list[list[Fraction]], x: Fraction) -> int:
    signs: list[int] = []
    for p in chain:
        value = evaluate(p, x)
        if value:
            signs.append(1 if value > 0 else -1)
    return sum(a != b for a, b in zip(signs, signs[1:]))


def root_count(coefficients: list[int], left: Fraction, right: Fraction) -> int:
    chain = sturm_chain(coefficients)
    require(evaluate(chain[0], left) != 0 and evaluate(chain[0], right) != 0,
            "Sturm endpoint is a root")
    return variations(chain, left) - variations(chain, right)


def verify_sturm(cert: dict) -> None:
    factors = cert["factor_polynomials"]
    for name, left_pair, right_pair, expected in cert["sturm_checks"]:
        left = Fraction(*left_pair)
        right = Fraction(*right_pair)
        require(left < right, "reversed Sturm interval")
        actual = root_count(factors[name], left, right)
        require(actual == expected, f"wrong Sturm count for {name} on {left},{right}: {actual}")

    h2 = [16, -48, 40, -8, -9, 3]
    h3 = [3, -9, -8, 40, -48, 16]
    require(root_count(h2, Fraction(1), Fraction(3, 2)) == 0, "h2 has an unexpected root")
    require(root_count(h3, Fraction(1), Fraction(2)) == 0, "h3 has an unexpected root")
    require(Fraction(0) < Fraction(2, 5), "positive-largest-value bound failed")
    require(Fraction(2, 7) < Fraction(2, 5), "7*x-2 branch was not excluded")

    # Exact sign proof used on the sole non-collapsing B4 branch.
    w = [-3, 70, -84, 24]  # high-to-low: -3*x^3+70*x^2-84*x+24
    wp = [-9, 140, -84]
    left, right = Fraction(59, 100), Fraction(3, 5)
    wp_low = [Fraction(c) for c in reversed(wp)]
    w_low = [Fraction(c) for c in reversed(w)]
    require(evaluate(w_low, left) < 0, "B4 boundary cubic is not negative at 59/100")
    require(evaluate(wp_low, right) < 0, "B4 boundary derivative is not negative at 3/5")
    # W''=140-18*x is positive here, so W' is increasing; its right endpoint
    # is its maximum and is still negative.  Hence W stays below W(left)<0.
    require(Fraction(140) - 18 * right > 0, "B4 second derivative sign failed")


def singular_poly(coefficients: list[int], variable: str = "x") -> str:
    degree = len(coefficients) - 1
    terms: list[str] = []
    for index, coefficient in enumerate(coefficients):
        power = degree - index
        if coefficient == 0:
            continue
        magnitude = abs(coefficient)
        atom = "" if magnitude == 1 and power else str(magnitude)
        if power:
            atom += ("*" if atom else "") + variable
            if power != 1:
                atom += f"^{power}"
        sign = "-" if coefficient < 0 else "+"
        if not terms:
            terms.append(("-" if coefficient < 0 else "") + atom)
        else:
            terms.append(sign + atom)
    return "".join(terms) or "0"


def pair_sum(atoms: list[str]) -> str:
    return "+".join(
        f"(1-{atoms[i]}-{atoms[j]})^4"
        for i in range(5) for j in range(i + 1, 5)
    )


def singleton_sum(atoms: list[str]) -> str:
    return "+".join(f"(1-{atom})^4" for atom in atoms)


def general_system_block() -> str:
    atoms = [f"a{i}" for i in range(5)]
    t_singletons = "+".join(f"(T-{atom})^4" for atom in atoms)
    t_pairs = "+".join(
        f"(T-{atoms[i]}-{atoms[j]})^4"
        for i in range(5) for j in range(i + 1, 5)
    )
    checks = []
    for atom in atoms:
        checks.append(
            f"if ({atom}*S*diff(P,{atom})+({atom}^2-S)*P-subst(qX,X,{atom})!=0) {{ bad=1; }}"
        )
    return f"""
ring rgeneral=0,(X,a0,a1,a2,a3,a4),dp;
int bad=0;
poly p1=a0+a1+a2+a3+a4;
poly S=a0^2+a1^2+a2^2+a3^2+a4^2;
poly C3=a0^3+a1^3+a2^3+a3^3+a4^3;
poly C4=a0^4+a1^4+a2^4+a3^4+a4^4;
poly T=p1/2;
poly Praw=T^4-({t_singletons})+({t_pairs});
poly P=3*(p1^4)/8-3*p1^2*S+3*S^2+4*p1*C3-4*C4;
if (Praw-P!=0) {{ bad=1; }}
poly C0=3*(p1^3)/2-6*p1*S+4*C3;
poly C1=-6*p1^2+12*S;
poly qX=-16*S*X^4+12*p1*S*X^3+(C1*S+P)*X^2+C0*S*X-S*P;
{chr(10).join(checks)}
poly qdiag=subst(qX,X,1);
qdiag=subst(qdiag,a0,1); qdiag=subst(qdiag,a1,1); qdiag=subst(qdiag,a2,1);
qdiag=subst(qdiag,a3,1); qdiag=subst(qdiag,a4,1);
if (qdiag!=0) {{ bad=1; }}
if (bad==0) {{ print("__EMPTY_GENERAL_OK__"); }}
if (bad!=0) {{ print("__EMPTY_GENERAL_FAIL__"); }}
"""


def factor_expression(case: dict, factors: dict[str, list[int]]) -> str:
    atoms = {"x": "x", "half": "(2*x-1)", "seven": "(7*x-2)"}
    pieces: list[str] = []
    for name, exponent in case["resultant_factors"]:
        base = atoms[name] if name in atoms else f"({singular_poly(factors[name])})"
        pieces.append(base if exponent == 1 else f"({base})^{exponent}")
    return "*".join(pieces)


def branch_candidate(key: str, factors: dict[str, list[int]]) -> tuple[str, list[str]]:
    branch = key.split("_", 1)[1]
    branch_poly = {
        "half": "2*x-1", "B4": singular_poly(factors["B4"]),
        "B5": singular_poly(factors["B5"]), "A5": singular_poly(factors["A5"]),
    }[branch]
    candidates = {
        "113_half": ["y^2", "2*x-1"],
        "122_B4": ["88*y^2+(44*x-88)*y-3*x^3+26*x^2-40*x+24", singular_poly(factors["B4"])],
        "122_B5": ["3*x+2*y-2", singular_poly(factors["B5"])],
        "131_half": ["2*y-1", "2*x-1"],
        "131_A5": ["2*x+3*y-2", singular_poly(factors["A5"])],
        "212_half": ["y^2", "2*x-1"],
        "221_half": ["2*y-1", "2*x-1"],
        "311_half": ["y^2*(2*y-1)", "2*x-1"],
    }
    return branch_poly, candidates[key]


def three_value_block(index: int, case: dict, factors: dict[str, list[int]]) -> str:
    m, n, k = case["multiplicities"]
    atoms = ["x"] * m + ["y"] * n + ["z"] * k
    fsn, fsd = case["f_scale"]
    gsn, gsd = case["g_scale"]
    expected_resultant = f"({case['resultant_constant']})*({factor_expression(case, factors)})"
    case_tag = f"{m}{n}{k}"
    branches: list[str] = []
    for branch in case["surviving_branches"]:
        key = f"{case_tag}_{branch}"
        branch_poly, candidates = branch_candidate(key, factors)
        candidate_csv = ",".join(candidates)
        branches.append(f"""
ideal JB{index}{branch}=f,g,{branch_poly};
JB{index}{branch}=std(JB{index}{branch});
ideal EB{index}{branch}={candidate_csv};
EB{index}{branch}=std(EB{index}{branch});
if (size(reduce(JB{index}{branch},EB{index}{branch}))!=0) {{ bad=1; }}
if (size(reduce(EB{index}{branch},JB{index}{branch}))!=0) {{ bad=1; }}
""")
    special = ""
    if case_tag == "122":
        special = """
poly RB4=88*y^2+(44*x-88)*y-3*x^3+26*x^2-40*x+24;
poly W=-3*x^3+70*x^2-84*x+24;
if (subst(RB4,y,1-x)-W!=0) { bad=1; }
if (subst(diff(RB4,y),y,(2-x)/4)!=0) { bad=1; }
if (y-z-2*(y-(2-x)/4)!=0) { bad=1; }
if (z-x+(3*x+2*y-2)/2!=0) { bad=1; }
"""
    elif case_tag == "131":
        special = """
if (z-x+(2*x+3*y-2)!=0) { bad=1; }
"""
    return f"""
ring r{index}=0,(y,x),lp;
int bad=0;
poly z=(2-{m}*x-{n}*y)/{k};
poly S={m}*x^2+{n}*y^2+{k}*z^2;
poly C3={m}*x^3+{n}*y^3+{k}*z^3;
poly C4={m}*x^4+{n}*y^4+{k}*z^4;
poly P=6-12*S+3*S^2+8*C3-4*C4;
poly Praw=1-({singleton_sum(atoms)})+({pair_sum(atoms)});
if ({m}*x+{n}*y+{k}*z-2!=0) {{ bad=1; }}
if (Praw-P!=0) {{ bad=1; }}
poly C0=4*(3-3*S+C3);
poly C1=12*(S-2);
proc RR{index}(poly u,poly v)
{{ return(-16*S*(u^3+u^2*v+u*v^2+v^3)+24*S*(u^2+u*v+v^2)+(C1*S+P)*(u+v)+C0*S); }}
poly f={fsn}/{fsd}*RR{index}(x,y);
poly g={gsn}/{gsd}*RR{index}(y,z);
poly resultant_actual=resultant(f,g,y);
poly resultant_expected={expected_resultant};
if (resultant_actual-resultant_expected!=0) {{ bad=1; }}
{''.join(branches)}
{special}
if (bad==0) {{ print("__EMPTY_CASE_{case_tag}_OK__"); }}
if (bad!=0) {{ print("__EMPTY_CASE_{case_tag}_FAIL__"); }}
"""


def two_value_blocks() -> str:
    expected = {
        1: "15*r^4*(r-3)/8",
        2: "5*(16*r^5-48*r^4+40*r^3-8*r^2-9*r+3)/8",
        3: "5*(3*r^5-9*r^4-8*r^3+40*r^2-48*r+16)/8",
        4: "15*(1-3*r)/8",
    }
    blocks: list[str] = []
    for m in range(1, 5):
        k = 5 - m
        atoms = ["r"] * m + ["1"] * k
        blocks.append(f"""
ring rt{m}=0,(r),dp;
int bad=0;
poly p1={m}*r+{k};
poly S={m}*r^2+{k};
poly C3={m}*r^3+{k};
poly C4={m}*r^4+{k};
poly P=3*(p1^4)/8-3*p1^2*S+3*S^2+4*p1*C3-4*C4;
poly T=p1/2;
poly Praw=T^4-({'+'.join(f'(T-{a})^4' for a in atoms)})+({'+'.join(f'(T-{atoms[i]}-{atoms[j]})^4' for i in range(5) for j in range(i+1,5))});
if (Praw-P!=0) {{ bad=1; }}
poly C0=3*(p1^3)/2-6*p1*S+4*C3;
poly C1=-6*p1^2+12*S;
poly R=-16*S*(r^3+r^2+r+1)+12*p1*S*(r^2+r+1)+(C1*S+P)*(r+1)+C0*S;
if (R-({expected[m]})!=0) {{ bad=1; }}
if (bad==0) {{ print("__EMPTY_TWO_{m}_OK__"); }}
if (bad!=0) {{ print("__EMPTY_TWO_{m}_FAIL__"); }}
""")
    return "".join(blocks)


def four_value_block() -> str:
    return r"""
ring rfour=0,(y,x),dp;
int bad=0;
poly z=1-x-y;
poly u=x*y+x*z+y*z;
poly w=x*y*z;
poly S=1/2+x^2+y^2+z^2;
poly C3=1/4+x^3+y^3+z^3;
poly C4=1/8+x^4+y^4+z^4;
poly P=6-12*S+3*S^2+8*C3-4*C4;
poly C0=4*(3-3*S+C3);
if (P/16-w/2-((4*u-1)^2)/64!=0) { bad=1; }
if (C0/16-(w+u/2)-(4*u-4*w-1)/16!=0) { bad=1; }
if (bad==0) { print("__EMPTY_FOUR_OK__"); }
if (bad!=0) { print("__EMPTY_FOUR_FAIL__"); }
"""


def singular_program(cert: dict) -> str:
    pieces = [general_system_block()]
    pieces += [three_value_block(i, case, cert["factor_polynomials"])
              for i, case in enumerate(cert["three_value_cases"])]
    pieces.append(two_value_blocks())
    pieces.append(four_value_block())
    pieces.append("quit;\n")
    return "\n".join(pieces)


def verify_singular(cert: dict, singular: str) -> None:
    executable = shutil.which(singular)
    require(executable is not None, f"Singular executable not found: {singular}")
    try:
        proc = subprocess.run(
            [executable, "-q"], input=singular_program(cert), text=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=120, check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise CertificateError(f"Singular failed to run: {exc}") from exc
    combined = proc.stdout + "\n" + proc.stderr
    require(proc.returncode == 0, f"Singular returned {proc.returncode}")
    require("?" not in combined, "Singular reported an error")
    require("_FAIL__" not in combined, "an exact Singular check failed")
    markers = ["__EMPTY_GENERAL_OK__"]
    markers += [f"__EMPTY_CASE_{''.join(map(str, case['multiplicities']))}_OK__"
               for case in cert["three_value_cases"]]
    markers += [f"__EMPTY_TWO_{m}_OK__" for m in range(1, 5)]
    markers.append("__EMPTY_FOUR_OK__")
    for marker in markers:
        require(combined.count(marker) == 1, f"missing or duplicate success marker: {marker}")


def verify(path: Path, singular: str) -> None:
    cert = load_and_validate(path)
    verify_sturm(cert)
    verify_singular(cert, singular)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--singular", default="Singular")
    args = parser.parse_args()
    try:
        verify(args.certificate, args.singular)
    except CertificateError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    print("PASS: empty-chamber classification, exact resultants, branches, and Sturm counts verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
