#!/usr/bin/env python3
"""Independent exact verifier for breaker_counterexample.json.

Trust base: Python integer/Fraction arithmetic and this small RNE routine.
The discovery search is neither imported nor read.
"""

from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json
import sys


def die(message):
    raise SystemExit("FAIL: " + message)


def parse_fraction(value):
    if not isinstance(value, str):
        die("all exact numeric fields must be strings")
    try:
        return Fraction(value)
    except (ValueError, ZeroDivisionError) as exc:
        die(f"bad rational {value!r}: {exc}")


def floor_log2_positive(x):
    if x <= 0:
        die("internal log2 domain error")
    e = x.numerator.bit_length() - x.denominator.bit_length()
    power = Fraction(1 << e) if e >= 0 else Fraction(1, 1 << -e)
    if x < power:
        e -= 1
    return e


def nearest_integer_ties_even(x):
    q, r = divmod(x.numerator, x.denominator)
    comparison = 2 * r - x.denominator
    if comparison < 0:
        return q
    if comparison > 0:
        return q + 1
    return q if q % 2 == 0 else q + 1


def round_binary(x, precision):
    """RNE to a normalized precision-bit binary float, unbounded exponent."""
    if x == 0:
        return x
    sign = -1 if x < 0 else 1
    magnitude = abs(x)
    exponent = floor_log2_positive(magnitude)
    shift = precision - 1 - exponent
    scaled = (magnitude * (1 << shift) if shift >= 0
              else magnitude / (1 << -shift))
    significand = nearest_integer_ties_even(scaled)
    if significand == 1 << precision:
        significand //= 2
        exponent += 1
    output_shift = precision - 1 - exponent
    result = (Fraction(sign * significand, 1 << output_shift)
              if output_shift >= 0
              else Fraction(sign * significand * (1 << -output_shift)))
    return result


def require_equal(label, actual, expected):
    if actual != expected:
        die(f"{label}: got {actual}, expected {expected}")


def is_precision_float(x, precision):
    return round_binary(x, precision) == x


def main():
    certificate_path = Path(sys.argv[1] if len(sys.argv) > 1
                            else "breaker_counterexample.json")
    raw = certificate_path.read_bytes()
    cert = json.loads(raw)
    fmt = cert.get("format", {})
    if fmt.get("radix") != 2 or fmt.get("rounding") != "roundTiesToEven":
        die("unsupported floating-point format")
    precision = fmt.get("precision")
    if precision != 53:
        die("this certificate must bind IEEE binary64 precision p=53")
    unit = parse_fraction(fmt.get("unit_roundoff"))
    require_equal("unit roundoff", unit, Fraction(1, 1 << precision))

    inputs = cert.get("inputs", {})
    A, u, v, b = [parse_fraction(inputs.get(key))
                   for key in ("A", "u", "v", "b")]
    for key, value in zip(("A", "u", "v", "b"), (A, u, v, b)):
        if not is_precision_float(value, precision):
            die(f"input {key} is not exactly representable")
    if A == 0 or A + u * v == 0 or b == 0:
        die("certificate requires nonzero A, B, and b")

    fl = lambda x: round_binary(x, precision)
    fadd = lambda x, y: fl(x + y)
    fsub = lambda x, y: fl(x - y)
    fmul = lambda x, y: fl(x * y)
    fdiv = lambda x, y: fl(x / y)

    # Algorithm SM, with a correctly rounded scalar division as the A-solver.
    y = fdiv(b, A)
    z = fdiv(u, A)
    alpha = fmul(v, y)
    vz = fmul(v, z)
    beta = fadd(Fraction(1), vz)
    if beta == 0:
        die("SM denominator is zero")
    theta = fdiv(alpha, beta)
    theta_z = fmul(theta, z)
    x = fsub(y, theta_z)

    expected = cert.get("expected", {})
    require_equal("fl(v*z)", vz, parse_fraction(expected.get("fl_v_times_z")))
    require_equal("beta", beta, parse_fraction(expected.get("beta")))
    require_equal("theta", theta, parse_fraction(expected.get("theta")))
    require_equal("initial x", x, parse_fraction(expected.get("x_fixed")))

    def computed_residual(xk):
        # Literal association from Algorithm SM-IR / the source residual lemma:
        # p=fl(b-A*x), q=fl(fl(v*x)*u), r=fl(p-q).
        pterm = fsub(b, fmul(A, xk))
        qterm = fmul(fmul(v, xk), u)
        return fsub(pterm, qterm)

    def refine_once(xk):
        rhat = computed_residual(xk)
        yr = fdiv(rhat, A)
        alpha_r = fmul(v, yr)
        theta_r = fdiv(alpha_r, beta)
        # Both natural associations give the same exact zero correction here.
        return fsub(fadd(xk, yr), fmul(theta_r, z)), rhat

    for iteration in range(8):
        x_next, rhat = refine_once(x)
        require_equal(f"computed residual at iteration {iteration}", rhat,
                      parse_fraction(expected.get("computed_residual")))
        require_equal(f"fixed point at iteration {iteration}", x_next, x)
        x = x_next

    # Exact target is B=A+u*v over the reals, not fl(A+fl(u*v)).
    B = A + u * v
    require_equal("true B", B, parse_fraction(expected.get("true_B")))
    kappa_A = abs(A) * abs(1 / A)
    kappa_B = abs(B) * abs(1 / B)
    require_equal("kappa_2(A)", kappa_A, Fraction(1))
    require_equal("kappa_2(B)", kappa_B, Fraction(1))
    true_residual = b - B * x
    backward_error = abs(true_residual) / (abs(B) * abs(x) + abs(b))
    require_equal("true backward error", backward_error,
                  parse_fraction(expected.get("true_backward_error")))
    if not backward_error > Fraction(1, 6):
        die("strict separator eta > 1/6 failed")
    if not kappa_A < 1 / unit or not kappa_B < 1 / unit:
        die("condition-number hypotheses failed")

    code_hash = sha256(Path(__file__).read_bytes()).hexdigest()
    cert_hash = sha256(raw).hexdigest()
    print("PASS scalar binary64 SM-IR fixed-point counterexample")
    print(f"kappa_A={kappa_A} kappa_B={kappa_B} beta={beta}")
    print(f"x_fixed={x} computed_residual=0 true_eta={backward_error} > 1/6")
    print(f"certificate_sha256={cert_hash}")
    print(f"verifier_sha256={code_hash}")


if __name__ == "__main__":
    main()
