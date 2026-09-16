"""A second, differently organized rigorous sign computation.

Run: python3 evidence/crosscheck_n5_arb.py
Requires python-flint. Uses endpoint derivative signs and Taylor subdivision,
not the Bernstein certificate. This is a same-worker cross-check, not a
fresh referee audit. It does not claim the stronger normalized lower bound.
"""
from flint import arb, ctx
import flint
from math import factorial
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
ctx.prec = 192
terms = json.loads((ROOT / "evidence/n5-certificate.json").read_text())["P_exponential_terms_base_coefficient"]
logs = {b: arb(b).log() for b, _ in terms}
S = sum(abs(c)*b*b for b, c in terms)
assert S == 212096
assert all(logs[b] < 5 for b, _ in terms)


def taylor(center, h, radius_bound, derivative=0, order=18):
    """Bound P^(derivative)(center+h), where |h|<=radius_bound.

    Terms through h^(order-1). For every segment used, 1<=center+h<=2,
    so the order-th remainder is at most
    S*5^(order+derivative)*radius_bound^order/order!.
    """
    weights = [(c*(logs[b]*center).exp(), logs[b]) for b, c in terms]
    coefficients = [sum((w*l**(k+derivative) for w, l in weights), arb(0))/factorial(k)
                    for k in range(order)]
    out = coefficients[-1]
    for coefficient in reversed(coefficients[:-1]):
        out = out*h + coefficient
    remainder = arb(S)*5**(order+derivative)*radius_bound**order/factorial(order)
    return out + arb(0, remainder)


def main():
    left = taylor(arb(1), arb(1, 1)/32, arb(1)/16, derivative=1)
    right = taylor(arb(2), arb(-1, 1)/32, arb(1)/16, derivative=3)
    assert left > 0, left
    assert right < 0, right
    cells = []
    for j in range(136, 248):
        c = arb(2*j+1)/256
        enclosure = taylor(c, arb(0, arb(1)/256), arb(1)/256)
        assert enclosure > 0, (j, enclosure)
        cells.append({"left": f"{j}/128", "right": f"{j+1}/128",
                      "P_enclosure": str(enclosure)})
    # Direct Cramer determinants and direct P evaluations at held-out dyadic
    # points, including extremely near both excluded H endpoints. These
    # finite checks supplement, rather than establish, the interval proof.
    determinant_checks = []
    from flint import arb_mat
    for t in [arb(1)+arb(1)/2**30, arb(9)/8, arb(5)/4,
              arb(3)/2, arb(7)/4, arb(15)/8, arb(2)-arb(1)/2**30]:
        rhos = [arb(1)]
        for j in range(1, 5):
            rhos.append(((arb(j+1).log()*t).exp()
                         - 2*(arb(j).log()*t).exp()
                         + (arb(0) if j == 1 else (arb(j-1).log()*t).exp()))/2)
        matrix = [[rhos[abs(i-j)] for j in range(4)] for i in range(4)]
        denominator = arb_mat(matrix).det()
        assert denominator > 0
        coefficient_enclosures = []
        for column in range(4):
            replaced = [row[:] for row in matrix]
            for i in range(4):
                replaced[i][column] = rhos[i+1]
            numerator = arb_mat(replaced).det()
            assert numerator > 0
            if column == 2:
                direct_sum = sum((c*(logs[b]*t).exp() for b, c in terms), arb(0))
                assert (16*numerator).overlaps(direct_sum)
            coefficient_enclosures.append(str(numerator/denominator))
        determinant_checks.append({"t": str(t), "Gamma_5_2_through_5": coefficient_enclosures})
    output = {
        "job_id": "primary-20260913-fgn-positivity-research-1f1ccfebc1c5",
        "evidence_type": "same-worker rigorous ball arithmetic cross-check, not fresh referee review",
        "python_flint_version": flint.__version__,
        "precision_bits": ctx.prec,
        "input_certificate_sha256": hashlib.sha256((ROOT / "evidence/n5-certificate.json").read_bytes()).hexdigest(),
        "Taylor_order": 18,
        "left_endpoint_interval": "[1,17/16]",
        "P_prime_enclosure_on_left": str(left),
        "right_endpoint_interval": "[31/16,2]",
        "P_third_derivative_enclosure_on_right": str(right),
        "endpoint_zero_dependencies": "P(1)=P(2)=P'(2)=P''(2)=0, checked exactly in certify_n5.py",
        "interior_cells": cells,
        "all_interior_P_enclosures_positive": True,
        "held_out_direct_determinant_checks": determinant_checks,
        "conclusion": "P(t)>0 for every 1<t<2; no claim about n>=6"
    }
    (ROOT / "evidence/n5-arb-crosscheck.json").write_text(json.dumps(output, indent=2)+"\n")
    print(json.dumps({"positive_interior_cells": len(cells),
                      "left_P_prime": str(left), "right_P_third": str(right),
                      "positive_direct_determinant_rows": len(determinant_checks),
                      "output": "evidence/n5-arb-crosscheck.json"}))


if __name__ == "__main__":
    main()
