#!/usr/bin/env python3
"""Independent exact verifier for the 2x2 binary64 SM-IR counterexample."""

from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json
import sys


def fail(message):
    raise SystemExit("FAIL: " + message)


def rat(value):
    if not isinstance(value, str):
        fail("exact numbers must be JSON strings")
    try:
        return Fraction(value)
    except (ValueError, ZeroDivisionError) as exc:
        fail(f"invalid rational {value!r}: {exc}")


def floor_log2_positive(x):
    if x <= 0:
        fail("internal log2 domain")
    exponent = x.numerator.bit_length() - x.denominator.bit_length()
    boundary = (Fraction(1 << exponent) if exponent >= 0
                else Fraction(1, 1 << -exponent))
    return exponent - 1 if x < boundary else exponent


def nearest_integer_ties_even(x):
    quotient, remainder = divmod(x.numerator, x.denominator)
    sign = 2 * remainder - x.denominator
    if sign < 0:
        return quotient
    if sign > 0:
        return quotient + 1
    return quotient if quotient % 2 == 0 else quotient + 1


def round_binary(x, precision):
    if x == 0:
        return x
    output_sign = -1 if x < 0 else 1
    magnitude = abs(x)
    exponent = floor_log2_positive(magnitude)
    shift = precision - 1 - exponent
    scaled = (magnitude * (1 << shift) if shift >= 0
              else magnitude / (1 << -shift))
    significand = nearest_integer_ties_even(scaled)
    if significand == 1 << precision:
        significand //= 2
        exponent += 1
    shift = precision - 1 - exponent
    return (Fraction(output_sign * significand, 1 << shift) if shift >= 0
            else Fraction(output_sign * significand * (1 << -shift)))


def assert_equal(label, actual, expected):
    if actual != expected:
        fail(f"{label}: got {actual}, expected {expected}")


def vector(values):
    return [rat(value) for value in values]


def matrix(values):
    return [vector(row) for row in values]


def main():
    cert_path = Path(sys.argv[1] if len(sys.argv) > 1
                     else "breaker_main_counterexample.json")
    cert_bytes = cert_path.read_bytes()
    cert = json.loads(cert_bytes)
    fmt = cert.get("format", {})
    if (fmt.get("radix"), fmt.get("precision"), fmt.get("rounding")) != (
            2, 53, "roundTiesToEven"):
        fail("certificate is not the required binary64 arithmetic")
    precision = 53
    unit = rat(fmt.get("unit_roundoff"))
    assert_equal("unit roundoff", unit, Fraction(1, 1 << precision))

    data = cert.get("inputs", {})
    A = matrix(data.get("A"))
    update_u = vector(data.get("u"))
    update_v = vector(data.get("v"))
    b = vector(data.get("b"))
    if len(A) != 2 or any(len(row) != 2 for row in A):
        fail("A must be 2x2")
    if any(round_binary(value, precision) != value
           for row in A for value in row):
        fail("A contains a non-binary64 input")
    if any(round_binary(value, precision) != value
           for value in update_u + update_v + b):
        fail("vector contains a non-binary64 input")
    if A[0][1] != 0 or A[1][0] != 0 or A[0][0] == 0 or A[1][1] == 0:
        fail("verifier only accepts the serialized nonsingular diagonal A")

    fl = lambda x: round_binary(x, precision)
    fadd = lambda x, y: fl(x + y)
    fsub = lambda x, y: fl(x - y)
    fmul = lambda x, y: fl(x * y)
    fdiv = lambda x, y: fl(x / y)

    def vadd(x, y):
        return [fadd(x[i], y[i]) for i in range(2)]

    def vsub(x, y):
        return [fsub(x[i], y[i]) for i in range(2)]

    def scale(alpha, x):
        return [fmul(alpha, x[i]) for i in range(2)]

    def dot(x, y):
        # Sequential two-term dot product.  The second term is exactly zero.
        return fadd(fmul(x[0], y[0]), fmul(x[1], y[1]))

    def matvec(M, x):
        return [fadd(fmul(M[i][0], x[0]), fmul(M[i][1], x[1]))
                for i in range(2)]

    def solve_A(rhs):
        # Correctly rounded diagonal solve, exact on every RHS in this trace.
        return [fdiv(rhs[0], A[0][0]), fdiv(rhs[1], A[1][1])]

    # Exact real target B=A+u*v^T.
    B = [[A[i][j] + update_u[i] * update_v[j] for j in range(2)]
         for i in range(2)]
    expected = cert.get("expected", {})
    assert_equal("target B", B, matrix(expected.get("B")))

    y = solve_A(b)
    z = solve_A(update_u)
    alpha = dot(update_v, y)
    beta = fadd(Fraction(1), dot(update_v, z))
    if beta == 0:
        fail("SM denominator unexpectedly zero")
    theta = fdiv(alpha, beta)
    x = vsub(y, scale(theta, z))
    assert_equal("beta", beta, rat(expected.get("beta")))
    assert_equal("theta", theta, rat(expected.get("theta")))
    assert_equal("initial x", x, vector(expected.get("x_fixed")))

    def separated_residual(xk):
        # fl(fl(b-A*x)-fl((v^T*x)u)), as in the source residual lemma.
        first = vsub(b, matvec(A, xk))
        second = scale(dot(update_v, xk), update_u)
        return vsub(first, second)

    expected_r = vector(expected.get("computed_residual"))
    for iteration in range(8):
        rhat = separated_residual(x)
        assert_equal(f"computed residual {iteration}", rhat, expected_r)
        yr = solve_A(rhat)
        theta_r = fdiv(dot(update_v, yr), beta)
        # Literal left association from x+y_r-theta_r*z.
        x_next = vsub(vadd(x, yr), scale(theta_r, z))
        # Alternative association gives the same result, so no parsing issue.
        x_alt = vadd(x, vsub(yr, scale(theta_r, z)))
        assert_equal(f"association check {iteration}", x_alt, x_next)
        assert_equal(f"fixed point {iteration}", x_next, x)
        x = x_next

    # Exact spectral condition numbers for positive diagonal 2x2 matrices.
    kappa_A = max(A[0][0], A[1][1]) / min(A[0][0], A[1][1])
    kappa_B = max(B[0][0], B[1][1]) / min(B[0][0], B[1][1])
    assert_equal("kappa_2(A)", kappa_A, rat(expected.get("kappa_A")))
    assert_equal("kappa_2(B)", kappa_B, rat(expected.get("kappa_B")))
    if not kappa_A < (1 / unit) / (1 << 25):
        fail("kappa_A is not safely below epsilon^-1 by certified factor")
    if not kappa_B < (1 / unit) / (1 << 25):
        fail("kappa_B is not safely below epsilon^-1 by certified factor")

    # Rigal--Gaches eta=||b-Bx||/(||B|| ||x||+||b||); x=0 makes
    # every vector norm and every induced matrix norm give eta=1.
    exact_residual = [b[i] - sum(B[i][j] * x[j] for j in range(2))
                      for i in range(2)]
    if x != [0, 0] or exact_residual != b:
        fail("unexpected exact residual at fixed point")
    backward_error = Fraction(1)
    assert_equal("true backward error", backward_error,
                 rat(expected.get("true_backward_error")))

    print("PASS 2x2 binary64 SM-IR fixed-point counterexample")
    print(f"kappa_A={kappa_A} kappa_B={kappa_B}")
    print(f"beta={beta} x_fixed={x} computed_residual={expected_r} true_eta=1")
    print(f"certificate_sha256={sha256(cert_bytes).hexdigest()}")
    print(f"verifier_sha256={sha256(Path(__file__).read_bytes()).hexdigest()}")


if __name__ == "__main__":
    main()
