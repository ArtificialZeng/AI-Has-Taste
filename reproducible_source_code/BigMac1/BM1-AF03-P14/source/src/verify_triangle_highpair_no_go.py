#!/usr/bin/env python3
"""Fail-closed verifier for the Q5 triangle high-pair chamber certificate.

This verifier deliberately does not import any discovery or project module.  It
loads a small JSON statement, reconstructs the exact critical ideal directly in
Singular, saturates it afresh, and checks the claimed Groebner basis and the
algebraic identities used by the ordered-cone contradiction.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path


EXPECTED_KEYS = {
    "certificate_type",
    "format_version",
    "theorem",
    "variables",
    "normalization",
    "high_pairs",
    "low_pairs",
    "critical_system",
    "ordered_closure_constraints",
    "saturated_groebner_basis",
    "elimination_factor",
    "proof_identities",
}

EXPECTED_BASIS = [
    "4*a1^2-3*a0*a2-9*a1*a2+6*a2^2+2*a3^2+2",
    "6*a0*a1-9*a0*a2-9*a1*a2+10*a2^2+2*a3^2+2",
    "4*a0^2-9*a0*a2-3*a1*a2+6*a2^2+2*a3^2+2",
    "4*a1*a2^2-3*a2^3+6*a0*a3^2-10*a1*a3^2+3*a2*a3^2+6*a0-10*a1+3*a2",
    "4*a0*a2^2-3*a2^3-10*a0*a3^2+6*a1*a3^2+3*a2*a3^2-10*a0+6*a1+3*a2",
    "a2^4-5*a2^2*a3^2+4*a3^4-5*a2^2+8*a3^2+4",
]

EXPECTED_CONSTRAINTS = {
    "order": ["a0-a1>=0", "a1-a2>=0", "a2-a3>=0", "a3-1>=0"],
    "polygon": ["a1+a2+a3+1-a0>=0"],
    "high_pair_closure": [
        "a0+a1-a2-a3-1>=0",
        "a0+a2-a1-a3-1>=0",
        "a1+a2-a0-a3-1>=0",
    ],
    "low_pair_closure": [
        "a1+a2+1-a0-a3>=0",
        "a1+a2+a3-a0-1>=0",
        "a0+a2+1-a1-a3>=0",
        "a0+a2+a3-a1-1>=0",
        "a0+a1+1-a2-a3>=0",
        "a0+a1+a3-a2-1>=0",
        "a0+a1+a2-a3-1>=0",
    ],
}

EXPECTED_SYSTEM = {
    "t": "(a0+a1+a2+a3+1)/2",
    "s": "a0^2+a1^2+a2^2+a3^2+1",
    "p_rule": "t^4-sum_i(t-ai)^4+sum_pairs(t-ai-aj)^4-2*sum_high_pairs(t-ai-aj)^4",
    "g_rule": "gi=ai*s*dP/dai+(ai^2-s)*P for i=0,1,2,3",
    "saturating_product": "a0*a1*a2*a3*P*s",
}

EXPECTED_IDENTITIES = {
    "basis_difference": "b2-b0=2*(a0-a1)*(2*a0+2*a1-3*a2)",
    "positive_factor_decomposition": "2*a0+2*a1-3*a2=2*(a0-a2)+2*(a1-a2)+a2",
    "after_a1_equals_a0": "c1-c0=2*(a0-a2)*(a0-2*a2)",
    "c0_at_a0_equals_a2": "c0=-2*(a2^2-a3^2-1)",
    "c0_at_a0_equals_2a2": "c0=-2*(a2^2-a3^2-1)",
    "factor_gap": "F2-F1=-3*(a3^2+1)",
    "triangle_gap": "(a3+1)^2-a2^2=-(a2^2-a3^2-1)+2*a3",
}


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


def load_and_validate(path: Path) -> dict:
    try:
        raw = path.read_text(encoding="utf-8")
        cert = json.loads(raw, object_pairs_hook=reject_duplicate_keys)
    except (OSError, UnicodeError, json.JSONDecodeError, CertificateError) as exc:
        raise CertificateError(f"cannot read certificate: {exc}") from exc

    reject_booleans(cert)
    require(type(cert) is dict, "top level must be an object")
    require(set(cert) == EXPECTED_KEYS, "unexpected or missing top-level keys")
    require(cert["certificate_type"] == "q5_triangle_highpair_chamber_no_go", "wrong certificate type")
    require(type(cert["format_version"]) is int and cert["format_version"] == 1,
            "unsupported format version")
    require(cert["variables"] == ["a0", "a1", "a2", "a3"], "wrong variables")
    require(
        cert["normalization"]
        == {"a4": "1", "meaning": "divide a full-support ordered normal by its smallest coordinate"},
        "wrong normalization",
    )
    require(cert["high_pairs"] == [[0, 1], [0, 2], [1, 2]], "wrong high-pair triangle")
    require(
        cert["low_pairs"] == [[0, 3], [0, 4], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]],
        "wrong low-pair complement",
    )
    require(cert["critical_system"] == EXPECTED_SYSTEM, "critical-system recipe changed")
    require(cert["ordered_closure_constraints"] == EXPECTED_CONSTRAINTS, "ordered chamber constraints changed")
    require(cert["saturated_groebner_basis"] == EXPECTED_BASIS, "claimed basis changed")
    require(
        cert["elimination_factor"]
        == {
            "polynomial": EXPECTED_BASIS[-1],
            "factorization": "(a2^2-a3^2-1)*(a2^2-4*a3^2-4)",
            "branch_1": "a2^2-a3^2-1=0",
            "branch_2": "a2^2-4*a3^2-4=0",
        },
        "elimination factor changed",
    )
    require(cert["proof_identities"] == EXPECTED_IDENTITIES, "proof identities changed")

    theorem = cert["theorem"]
    require(type(theorem) is dict and set(theorem) == {"claim", "scope", "excluded"}, "malformed theorem")
    require(
        theorem["claim"]
        == "No real full-support critical point lies in the ordered closure of the triangle high-pair chamber.",
        "claim changed",
    )
    require(
        theorem["scope"]
        == "a0>=a1>=a2>=a3>=a4=1, polygon closure, triangle high-pair closure, complementary low-pair closure, P!=0",
        "scope changed",
    )
    require(
        theorem["excluded"]
        == "zero-coordinate strata and sign chambers outside this closure",
        "excluded scope changed",
    )

    safe = re.compile(r"^[a-zA-Z0-9_+*^()\-]+$")
    for expr in cert["saturated_groebner_basis"]:
        require(type(expr) is str and safe.fullmatch(expr) is not None, "unsafe basis expression")
    return cert


def singular_program(cert: dict) -> str:
    a = ["a0", "a1", "a2", "a3", "1"]
    pairs = [(i, j) for i in range(5) for j in range(i + 1, 5)]
    high = [tuple(pair) for pair in cert["high_pairs"]]
    single_sum = "+".join(f"(T-{x})^4" for x in a)
    pair_sum = "+".join(f"(T-{a[i]}-{a[j]})^4" for i, j in pairs)
    high_sum = "+".join(f"(T-{a[i]}-{a[j]})^4" for i, j in high)
    basis_defs = "\n".join(f"poly b{i}={expr};" for i, expr in enumerate(cert["saturated_groebner_basis"]))

    return f"""
ring r=0,(a0,a1,a2,a3),dp;
poly T=(a0+a1+a2+a3+1)/2;
poly S=a0^2+a1^2+a2^2+a3^2+1;
poly P=T^4-({single_sum})+({pair_sum})-2*({high_sum});
poly g0=a0*S*diff(P,a0)+(a0^2-S)*P;
poly g1=a1*S*diff(P,a1)+(a1^2-S)*P;
poly g2=a2*S*diff(P,a2)+(a2^2-S)*P;
poly g3=a3*S*diff(P,a3)+(a3^2-S)*P;
ideal I=g0,g1,g2,g3;
LIB "elim.lib";
ideal Nonzero=a0*a1*a2*a3*P*S;
ideal Q=sat(I,Nonzero);
ideal J=std(Q);
{basis_defs}
ideal E=b0,b1,b2,b3,b4,b5;
E=std(E);
int bad=0;
if (dim(J)!=1) {{ bad=1; }}
if (vdim(J)!=-1) {{ bad=1; }}
if (size(J)!=6) {{ bad=1; }}
if (size(reduce(J,E))!=0) {{ bad=1; }}
if (size(reduce(E,J))!=0) {{ bad=1; }}
poly F1=a2^2-a3^2-1;
poly F2=a2^2-4*a3^2-4;
if (b5-F1*F2!=0) {{ bad=1; }}
if (b2-b0-2*(a0-a1)*(2*a0+2*a1-3*a2)!=0) {{ bad=1; }}
if (2*a0+2*a1-3*a2-(2*(a0-a2)+2*(a1-a2)+a2)!=0) {{ bad=1; }}
poly c0=subst(b0,a1,a0);
poly c1=subst(b1,a1,a0);
if (c1-c0-2*(a0-a2)*(a0-2*a2)!=0) {{ bad=1; }}
if (subst(c0,a0,a2)+2*F1!=0) {{ bad=1; }}
if (subst(c0,a0,2*a2)+2*F1!=0) {{ bad=1; }}
if (F2-F1+3*(a3^2+1)!=0) {{ bad=1; }}
if ((a3+1)^2-a2^2+F1-2*a3!=0) {{ bad=1; }}
if (bad==0) {{ print("__TRIANGLE_CERT_OK__"); }}
if (bad!=0) {{ print("__TRIANGLE_CERT_FAIL__"); }}
quit;
"""


def verify(cert_path: Path, singular: str) -> None:
    cert = load_and_validate(cert_path)
    executable = shutil.which(singular)
    require(executable is not None, f"Singular executable not found: {singular}")
    program = singular_program(cert)
    try:
        proc = subprocess.run(
            [executable, "-q"],
            input=program,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=120,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise CertificateError(f"Singular failed to run: {exc}") from exc
    combined = proc.stdout + "\n" + proc.stderr
    require(proc.returncode == 0, f"Singular returned {proc.returncode}")
    require("?" not in combined, "Singular reported an error")
    require("__TRIANGLE_CERT_FAIL__" not in combined, "an exact check failed")
    require(combined.count("__TRIANGLE_CERT_OK__") == 1, "missing or duplicate success sentinel")


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
    print("PASS: exact saturated ideal, factorization, and proof identities verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
