#!/usr/bin/env python3
"""Adversarial, no-builder audit of the exact Q5 star1 certificate.

The Bernstein calculation uses only Fraction sparse polynomials.  The
residual ideal is checked by an independently generated Singular program,
and the full tangent Hessian is rebuilt in Q(alpha).  No project module is
imported.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import platform
import random
import shutil
import subprocess
from fractions import Fraction
from pathlib import Path


def fail(message: str) -> "None":
    raise SystemExit("AUDIT FAIL: " + message)


def no_duplicate_object(pairs):
    answer = {}
    for key, value in pairs:
        if key in answer:
            fail(f"duplicate JSON key: {key}")
        answer[key] = value
    return answer


def validate_json_scalar_types(value, context="root"):
    if isinstance(value, bool) or value is None or isinstance(value, float):
        fail(f"{context}: forbidden JSON scalar type")
    if isinstance(value, dict):
        for key, child in value.items():
            validate_json_scalar_types(child, f"{context}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            validate_json_scalar_types(child, f"{context}[{index}]")
    elif not isinstance(value, (int, str)):
        fail(f"{context}: unsupported JSON value")


class Poly:
    def __init__(self, terms=None, variables=4):
        self.variables = variables
        self.terms = {
            tuple(m): Fraction(c) for m, c in (terms or {}).items() if Fraction(c)
        }

    @classmethod
    def constant(cls, value, variables=4):
        return cls({(0,) * variables: Fraction(value)}, variables)

    @classmethod
    def variable(cls, index, variables=4):
        monomial = [0] * variables
        monomial[index] = 1
        return cls({tuple(monomial): Fraction(1)}, variables)

    def coerce(self, other):
        if isinstance(other, Poly):
            if other.variables != self.variables:
                fail("polynomial dimension mismatch")
            return other
        return Poly.constant(other, self.variables)

    def __add__(self, other):
        other = self.coerce(other)
        terms = dict(self.terms)
        for monomial, coefficient in other.terms.items():
            terms[monomial] = terms.get(monomial, Fraction(0)) + coefficient
            if not terms[monomial]:
                del terms[monomial]
        return Poly(terms, self.variables)

    __radd__ = __add__

    def __neg__(self):
        return Poly({m: -c for m, c in self.terms.items()}, self.variables)

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) - self

    def __mul__(self, other):
        other = self.coerce(other)
        terms = {}
        for m1, c1 in self.terms.items():
            for m2, c2 in other.terms.items():
                monomial = tuple(a + b for a, b in zip(m1, m2))
                terms[monomial] = terms.get(monomial, Fraction(0)) + c1 * c2
                if not terms[monomial]:
                    del terms[monomial]
        return Poly(terms, self.variables)

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        scalar = Fraction(scalar)
        if not scalar:
            fail("division by zero")
        return Poly({m: c / scalar for m, c in self.terms.items()}, self.variables)

    def __pow__(self, exponent):
        if not isinstance(exponent, int) or exponent < 0:
            fail("invalid polynomial exponent")
        answer = Poly.constant(1, self.variables)
        base = self
        while exponent:
            if exponent & 1:
                answer *= base
            base *= base
            exponent //= 2
        return answer

    def derivative(self, index):
        terms = {}
        for monomial, coefficient in self.terms.items():
            exponent = monomial[index]
            if exponent:
                reduced = list(monomial)
                reduced[index] -= 1
                terms[tuple(reduced)] = coefficient * exponent
        return Poly(terms, self.variables)

    def substitute(self, replacements):
        if len(replacements) != self.variables:
            fail("wrong substitution length")
        target_variables = replacements[0].variables
        if any(item.variables != target_variables for item in replacements):
            fail("inconsistent substitution target")
        answer = Poly.constant(0, target_variables)
        for monomial, coefficient in self.terms.items():
            term = Poly.constant(coefficient, target_variables)
            for replacement, exponent in zip(replacements, monomial):
                term *= replacement**exponent
            answer += term
        return answer

    def evaluate(self, values):
        if len(values) != self.variables:
            fail("wrong evaluation dimension")
        answer = Fraction(0)
        for monomial, coefficient in self.terms.items():
            term = coefficient
            for value, exponent in zip(values, monomial):
                term *= Fraction(value) ** exponent
            answer += term
        return answer

    def evaluate_quad(self, values):
        if len(values) != self.variables:
            fail("wrong quadratic-field evaluation dimension")
        answer = Quad(0, 0)
        for monomial, coefficient in self.terms.items():
            term = Quad(coefficient, 0)
            for value, exponent in zip(values, monomial):
                term *= value**exponent
            answer += term
        return answer


class Quad:
    """c0+c1*alpha with 13*alpha^2-48*alpha+39=0."""

    def __init__(self, c0=0, c1=0):
        self.c0 = Fraction(c0)
        self.c1 = Fraction(c1)

    def coerce(self, other):
        return other if isinstance(other, Quad) else Quad(other, 0)

    def __add__(self, other):
        other = self.coerce(other)
        return Quad(self.c0 + other.c0, self.c1 + other.c1)

    __radd__ = __add__

    def __neg__(self):
        return Quad(-self.c0, -self.c1)

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) - self

    def __mul__(self, other):
        other = self.coerce(other)
        return Quad(
            self.c0 * other.c0 - Fraction(39, 13) * self.c1 * other.c1,
            self.c0 * other.c1 + self.c1 * other.c0 + Fraction(48, 13) * self.c1 * other.c1,
        )

    __rmul__ = __mul__

    def inverse(self):
        norm = self.c0 * self.c0 + Fraction(48, 13) * self.c0 * self.c1 + Fraction(39, 13) * self.c1 * self.c1
        if not norm:
            fail("zero quadratic-field denominator")
        return Quad((self.c0 + Fraction(48, 13) * self.c1) / norm, -self.c1 / norm)

    def __truediv__(self, other):
        return self * self.coerce(other).inverse()

    def __rtruediv__(self, other):
        return self.coerce(other) * self.inverse()

    def __pow__(self, exponent):
        if not isinstance(exponent, int) or exponent < 0:
            fail("invalid quadratic-field exponent")
        answer = Quad(1, 0)
        base = self
        while exponent:
            if exponent & 1:
                answer *= base
            base *= base
            exponent //= 2
        return answer

    def __eq__(self, other):
        other = self.coerce(other)
        return self.c0 == other.c0 and self.c1 == other.c1

    def pair(self):
        return [str(self.c0), str(self.c1)]


def decode_poly(rows, variables, context):
    if not isinstance(rows, list) or not rows:
        fail(context + ": expected nonempty sparse polynomial")
    terms = {}
    sequence = []
    for index, row in enumerate(rows):
        if not isinstance(row, list) or len(row) != variables + 2:
            fail(f"{context}[{index}]: malformed row")
        exponents = tuple(row[:variables])
        if any(not isinstance(e, int) or isinstance(e, bool) or e < 0 for e in exponents):
            fail(f"{context}[{index}]: invalid exponent")
        numerator, denominator = row[-2:]
        if any(not isinstance(v, int) or isinstance(v, bool) for v in (numerator, denominator)):
            fail(f"{context}[{index}]: invalid rational type")
        if denominator <= 0 or math.gcd(abs(numerator), denominator) != 1:
            fail(f"{context}[{index}]: noncanonical rational")
        if exponents in terms:
            fail(f"{context}: duplicate monomial")
        terms[exponents] = Fraction(numerator, denominator)
        sequence.append(exponents)
    if sequence != sorted(sequence, reverse=True):
        fail(context + ": noncanonical term order")
    if len(rows) == 1 and sequence[0] == (0,) * variables and rows[0][-2:] == [0, 1]:
        return Poly({}, variables)
    if any(not coefficient for coefficient in terms.values()):
        fail(context + ": embedded zero coefficient")
    return Poly(terms, variables)


def encode_poly(poly):
    if not poly.terms:
        return [[0] * poly.variables + [0, 1]]
    return [
        [*m, c.numerator, c.denominator]
        for m, c in sorted(poly.terms.items(), reverse=True)
    ]


def falling(n, k):
    answer = 1
    for value in range(n - k + 1, n + 1):
        answer *= value
    return answer


def simplex_bernstein(poly, degree=9):
    """Power-to-degree-n simplex Bernstein conversion in x,z."""
    power = {}
    for monomial, coefficient in poly.terms.items():
        p, q, eu, ew = monomial
        if p + q > degree:
            fail("polynomial exceeds advertised simplex degree")
        power.setdefault((p, q), {})[(eu, ew)] = coefficient
    rows = {}
    for i in range(degree + 1):
        for j in range(degree + 1 - i):
            terms = {}
            for (p, q), parameter_terms in power.items():
                if p <= i and q <= j:
                    factor = Fraction(falling(i, p) * falling(j, q), falling(degree, p + q))
                    for monomial, coefficient in parameter_terms.items():
                        terms[monomial] = terms.get(monomial, Fraction(0)) + factor * coefficient
                        if not terms[monomial]:
                            del terms[monomial]
            rows[i, j] = terms
    return rows


def rows_to_simplex_polynomial(rows, degree=9):
    x, z, u, w = [Poly.variable(i, 4) for i in range(4)]
    r = 1 - x - z
    answer = Poly.constant(0, 4)
    for (i, j), parameter_terms in rows.items():
        b = Poly.constant(0, 4)
        for (eu, ew), coefficient in parameter_terms.items():
            b += coefficient * u**eu * w**ew
        multinomial = math.factorial(degree) // (
            math.factorial(i) * math.factorial(j) * math.factorial(degree - i - j)
        )
        answer += multinomial * b * x**i * z**j * r ** (degree - i - j)
    return answer


def serialize_bernstein(rows, degree=9):
    output = []
    for i in range(degree + 1):
        for j in range(degree + 1 - i):
            poly = Poly(rows[i, j], 2)
            output.append({"i": i, "j": j, "terms_u_w": encode_poly(poly)})
    return output


def affine_simplex_basis(poly):
    """Return coefficients in x,z,r=1-x-z,u,w for an affine polynomial."""
    if any(sum(monomial) > 1 for monomial in poly.terms):
        fail("margin is not affine")
    zero = (0, 0, 0, 0)
    c = poly.terms.get(zero, Fraction(0))
    linear = [poly.terms.get(tuple(1 if i == j else 0 for i in range(4)), Fraction(0)) for j in range(4)]
    representation = {
        "x": c + linear[0],
        "z": c + linear[1],
        "r=1-x-z": c,
        "u": linear[2],
        "w": linear[3],
    }
    if any(value < 0 for value in representation.values()):
        fail("margin has a negative simplex-domain coefficient")
    x, z, u, w = [Poly.variable(i, 4) for i in range(4)]
    reconstructed = (
        representation["x"] * x
        + representation["z"] * z
        + representation["r=1-x-z"] * (1 - x - z)
        + representation["u"] * u
        + representation["w"] * w
    )
    if reconstructed.terms != poly.terms:
        fail("simplex-domain margin reconstruction failed")
    return {name: str(value) for name, value in representation.items() if value}


def singular_expression(poly, names):
    if not poly.terms:
        return "0"
    pieces = []
    for monomial, coefficient in sorted(poly.terms.items(), reverse=True):
        if coefficient.denominator != 1:
            fail("Singular bridge expected integer coefficients")
        magnitude = abs(coefficient.numerator)
        factors = [] if magnitude == 1 and any(monomial) else [str(magnitude)]
        for name, exponent in zip(names, monomial):
            if exponent:
                factors.append(name if exponent == 1 else f"{name}^{exponent}")
        body = "*".join(factors) if factors else "1"
        sign = "-" if coefficient < 0 else "+"
        pieces.append(sign + body)
    expression = "".join(pieces)
    return expression[1:] if expression.startswith("+") else expression


def run_singular(A, B, singular):
    a = singular_expression(A, ("u", "w"))
    b = singular_expression(B, ("u", "w"))
    program = f"""
ring r=0,(w,u),lp;
poly A={a};
poly B={b};
ideal SI=std(A,B);
poly q1=4*u^2+4*u+3;
poly q2=52*u^2-36*u-15;
poly q3=84*u^2-52*u+1;
poly q4=32*u^3+48*u^2+32*u+9;
poly q5=1280*u^6+3840*u^5+6720*u^4+7072*u^3+5056*u^2+2160*u+525;
ideal C1=q1,2*w+2*u+3;
ideal C2=q2,w;
ideal C3=q3,3*w+2;
ideal C4=q4,2*w+2*u+3;
ideal C5=q5,40*w+640*u^5+1920*u^4+2960*u^3+2736*u^2+1488*u+465;
ideal SJ=std(intersect(C1,C2,C3,C4,C5));
int forward=1; int reverse=1; int i;
for(i=1;i<=size(SI);i++){{if(NF(SI[i],SJ)!=0){{forward=0;}}}}
for(i=1;i<=size(SJ);i++){{if(NF(SJ[i],SI)!=0){{reverse=0;}}}}
poly expectedR=1024*w^2*(3*w+2)^2*(2*w^2+4*w+3)*(32*w^3+96*w^2+104*w+39)*(10240*w^6+61440*w^5+158720*w^4+225216*w^3+184192*w^2+81840*w+15345);
int resultant_ok=(resultant(A,B,u)-expectedR==0);
int irreducible=1;
list f1=factorize(q1); if(size(f1[1])!=2){{irreducible=0;}}
list f2=factorize(q2); if(size(f2[1])!=2){{irreducible=0;}}
list f3=factorize(q3); if(size(f3[1])!=2){{irreducible=0;}}
list f4=factorize(q4); if(size(f4[1])!=2){{irreducible=0;}}
list f5=factorize(q5); if(size(f5[1])!=2){{irreducible=0;}}
print("STAR1_VDIM="+string(vdim(SI)));
print("STAR1_FORWARD="+string(forward));
print("STAR1_REVERSE="+string(reverse));
print("STAR1_RESULTANT="+string(resultant_ok));
print("STAR1_IRREDUCIBLE="+string(irreducible));
"""
    process = subprocess.run([singular, "--quiet"], input=program, text=True, capture_output=True, check=False)
    if process.returncode != 0:
        fail("Singular failed: " + (process.stderr or process.stdout)[-500:])
    markers = {}
    for line in process.stdout.splitlines():
        if line.startswith("STAR1_") and "=" in line:
            key, value = line.strip().split("=", 1)
            markers[key] = value
    expected = {
        "STAR1_VDIM": "15",
        "STAR1_FORWARD": "1",
        "STAR1_REVERSE": "1",
        "STAR1_RESULTANT": "1",
        "STAR1_IRREDUCIBLE": "1",
    }
    if markers != expected:
        fail(f"Singular residual audit failed: {markers}")
    return markers


def univariate_remainder(poly, modulus_ascending):
    if poly.variables != 1:
        fail("univariate remainder received multivariate polynomial")
    coefficients = {m[0]: c for m, c in poly.terms.items()}
    modulus = [Fraction(c) for c in modulus_ascending]
    degree = len(modulus) - 1
    leading = modulus[-1]
    while coefficients and max(coefficients) >= degree:
        top_degree = max(coefficients)
        scale = coefficients[top_degree] / leading
        shift = top_degree - degree
        for index, coefficient in enumerate(modulus):
            exponent = shift + index
            coefficients[exponent] = coefficients.get(exponent, Fraction(0)) - scale * coefficient
            if not coefficients[exponent]:
                del coefficients[exponent]
    return coefficients


def qform(vector, matrix, other=None):
    other = vector if other is None else other
    answer = Quad(0, 0)
    for i in range(len(vector)):
        for j in range(len(other)):
            answer += vector[i] * matrix[i][j] * other[j]
    return answer


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--seed", type=int, default=140120260829)
    parser.add_argument("--random-checks", type=int, default=64)
    parser.add_argument("--singular", default=shutil.which("Singular"))
    args = parser.parse_args()
    if not args.singular:
        fail("Singular executable not found")

    raw = args.certificate.read_bytes()
    data = json.loads(raw, object_pairs_hook=no_duplicate_object)
    validate_json_scalar_types(data)
    expected_top = {
        "schema", "normalization", "chamber", "chart", "critical_equations",
        "bernstein", "residual_necessary_ideal", "surviving_component", "hessian",
    }
    if not isinstance(data, dict) or set(data) != expected_top:
        fail("wrong top-level schema")
    if data["schema"] != "q5-star1-exact-v1" or data["normalization"] != "a4=1":
        fail("wrong schema or normalization")
    if data["chamber"] != "N={(0,1)} ordered closure":
        fail("wrong chamber claim")

    # Original gap variables (x,y,z,w), independent 32-subset reconstruction.
    x0, y0, z0, w0 = [Poly.variable(i, 4) for i in range(4)]
    one = Poly.constant(1, 4)
    a = [one+w0+z0+y0+x0, one+w0+z0+y0, one+w0+z0, one+w0, one]
    total = sum(a, Poly.constant(0, 4))
    T = total / 2
    sample = [Fraction(1, 4), Fraction(3, 4), Fraction(1, 4), Fraction(1, 3)]
    direct_P = Poly.constant(0, 4)
    active_subsets = 0
    for bits in itertools.product((0, 1), repeat=5):
        linear = T - sum((a[i] for i, bit in enumerate(bits) if bit), Poly.constant(0, 4))
        value = linear.evaluate(sample)
        if value == 0:
            fail("strict reconstruction sample is on a subset-sum wall")
        if value > 0:
            active_subsets += 1
            direct_P += (-1 if sum(bits) % 2 else 1) * linear**4
    paired_P = T**4 - sum(((T-ai)**4 for ai in a), Poly.constant(0, 4))
    for i, j in itertools.combinations(range(5), 2):
        paired_P += (-1 if (i, j) == (0, 1) else 1) * (T-a[i]-a[j])**4
    if direct_P.terms != paired_P.terms:
        fail("32-subset and paired star1 numerators disagree")

    S = sum((ai*ai for ai in a), Poly.constant(0, 4))
    D = a[0]*a[1]*a[2]*a[3]*a[4]
    H = []
    numerator_squared = S*direct_P**2
    for index in range(4):
        h = S.derivative(index)*direct_P*D + 2*S*direct_P.derivative(index)*D - 2*S*direct_P*D.derivative(index)
        if (D*numerator_squared.derivative(index)-2*numerator_squared*D.derivative(index)-direct_P*h).terms:
            fail("F-squared quotient-rule identity failed")
        H.append(h)

    critical = data["critical_equations"]
    expected_critical = {
        "variable_order": ["x", "y", "z", "w"],
        "cleared_derivative": "Hq=S_q*P*D+2*S*P_q*D-2*S*P*D_q",
        "combination": [-6, 7, -8, 4],
    }
    if critical != expected_critical:
        fail("altered critical-equation metadata")

    # Chart variables are (x,z,u,w).
    x, z, u, w = [Poly.variable(i, 4) for i in range(4)]
    chart_substitution = [x, (1-x-z)/2+u, z, w]
    ac = [ai.substitute(chart_substitution) for ai in a]
    Hc = [h.substitute(chart_substitution) for h in H]
    K = -6*Hc[0]+7*Hc[1]-8*Hc[2]+4*Hc[3]

    chart = data["chart"]
    if set(chart) != {"gap_order", "substitution", "domain", "pair_margins"}:
        fail("wrong chart schema")
    if chart["gap_order"] != ["x=a0-a1", "y=a1-a2", "z=a2-a3", "w=a3-a4"]:
        fail("wrong gap order")
    if chart["substitution"] != "y=(1-x-z)/2+u":
        fail("wrong chart substitution")
    if chart["domain"] != ["x>=0", "z>=0", "x+z<=1", "u>=0", "w>=0"]:
        fail("wrong chart domain")

    chart_total = sum(ac, Poly.constant(0, 4))
    margin_chart = {}
    certificate_margins = chart["pair_margins"]
    pairs = list(itertools.combinations(range(5), 2))
    if not isinstance(certificate_margins, list) or len(certificate_margins) != 10:
        fail("wrong margin count")
    for row, pair in zip(certificate_margins, pairs):
        if set(row) != {"pair", "kind", "polynomial_x_z_u_w"} or row["pair"] != list(pair):
            fail("malformed or reordered pair margin")
        kind = "high" if pair == (0, 1) else "low"
        if row["kind"] != kind:
            fail("wrong pair sign")
        expected_margin = 2*(ac[pair[0]]+ac[pair[1]])-chart_total if kind == "high" else chart_total-2*(ac[pair[0]]+ac[pair[1]])
        observed_margin = decode_poly(row["polynomial_x_z_u_w"], 4, f"margin {pair}")
        if observed_margin.terms != expected_margin.terms:
            fail("serialized margin identity mismatch")
        margin_chart[f"pair_{pair[0]}{pair[1]}_{kind}"] = affine_simplex_basis(expected_margin)
    for index in range(4):
        margin_chart[f"order_{index}{index+1}"] = affine_simplex_basis(ac[index]-ac[index+1])
    for index in range(5):
        margin_chart[f"polygon_{index}"] = affine_simplex_basis(chart_total-2*ac[index])

    bernstein = data["bernstein"]
    if set(bernstein) != {"degree", "basis", "parameter_order", "rows", "rows_sha256"}:
        fail("wrong Bernstein schema")
    if bernstein["degree"] != 9 or bernstein["parameter_order"] != ["u", "w"]:
        fail("wrong Bernstein degree or parameters")
    if bernstein["basis"] != "multinomial(9;i,j,9-i-j)*x^i*z^j*(1-x-z)^(9-i-j)":
        fail("wrong Bernstein basis declaration")
    recomputed_rows = simplex_bernstein(K, 9)
    if rows_to_simplex_polynomial(recomputed_rows, 9).terms != K.terms:
        fail("independent Bernstein reconstruction failed")
    canonical_rows = serialize_bernstein(recomputed_rows, 9)
    if bernstein["rows"] != canonical_rows:
        fail("certificate Bernstein rows differ or are noncanonical")
    digest = hashlib.sha256(json.dumps(canonical_rows, separators=(",", ":"), sort_keys=True).encode()).hexdigest()
    if bernstein["rows_sha256"] != digest:
        fail("Bernstein digest mismatch")
    all_coefficients = [c for terms in recomputed_rows.values() for c in terms.values()]
    if recomputed_rows[0, 0]:
        fail("b00 is not exactly zero")
    if len(all_coefficients) != 1620 or any(c <= 0 for c in all_coefficients):
        fail("Bernstein positivity/count claim failed")
    for pair, terms in recomputed_rows.items():
        if pair != (0, 0) and terms.get((0, 0), Fraction(0)) <= 0:
            fail("nonzero Bernstein coefficient lacks positive constant")
    if not recomputed_rows[9, 0] or not recomputed_rows[0, 9]:
        fail("endpoint positivity witnesses are missing")

    # Exact random and boundary checks challenge the K=0 iff x=z=0 inference.
    rng = random.Random(args.seed)
    points = [
        (0, 0, 0, 0), (0, 0, 3, 4), (1, 0, 0, 0), (0, 1, 0, 0),
        (Fraction(1, 2), Fraction(1, 2), 2, 0),
    ]
    for _ in range(args.random_checks):
        denominator = rng.randint(1, 12)
        ix = rng.randint(0, denominator)
        iz = rng.randint(0, denominator-ix)
        points.append((Fraction(ix, denominator), Fraction(iz, denominator), Fraction(rng.randint(0, 30), rng.randint(1, 9)), Fraction(rng.randint(0, 30), rng.randint(1, 9))))
    for point in points:
        value = K.evaluate(point)
        if (point[0] == 0 and point[1] == 0 and value != 0) or ((point[0] > 0 or point[1] > 0) and value <= 0):
            fail("exact point challenge contradicts Bernstein zero set")

    residual = data["residual_necessary_ideal"]
    if set(residual) != {"variable_order", "A", "B", "complex_degree", "components", "resultant_u"}:
        fail("wrong residual schema")
    if residual["variable_order"] != ["u", "w"] or residual["complex_degree"] != 15:
        fail("wrong residual metadata")
    A = decode_poly(residual["A"], 2, "A")
    B = decode_poly(residual["B"], 2, "B")
    u2, w2 = [Poly.variable(i, 2) for i in range(2)]
    face_substitution = [Poly.constant(0, 2), Poly.constant(0, 2), u2, w2]
    face_H = [h.substitute(face_substitution) for h in Hc]
    positive_factor = 2*u2+2*w2+3
    if (16*face_H[0]-(w2+1)**2*positive_factor*A).terms:
        fail("A residual factor identity failed")
    if (-16*face_H[2]-(w2+1)*positive_factor*B).terms:
        fail("B residual factor identity failed")

    expected_components = [
        ([[2,4,1],[1,4,1],[0,3,1]], [[1,0,2,1],[0,1,2,1],[0,0,3,1]]),
        ([[2,52,1],[1,-36,1],[0,-15,1]], [[1,0,1,1]]),
        ([[2,84,1],[1,-52,1],[0,1,1]], [[1,0,3,1],[0,0,2,1]]),
        ([[3,32,1],[2,48,1],[1,32,1],[0,9,1]], [[1,0,2,1],[0,1,2,1],[0,0,3,1]]),
        ([[6,1280,1],[5,3840,1],[4,6720,1],[3,7072,1],[2,5056,1],[1,2160,1],[0,525,1]], [[1,0,40,1],[0,5,640,1],[0,4,1920,1],[0,3,2960,1],[0,2,2736,1],[0,1,1488,1],[0,0,465,1]]),
    ]
    if not isinstance(residual["components"], list) or len(residual["components"]) != 5:
        fail("wrong residual component count")
    for row, (q, relation) in zip(residual["components"], expected_components):
        if set(row) != {"u_factor", "w_relation"} or row["u_factor"] != q or row["w_relation"] != relation:
            fail("altered or noncanonical residual component")

    expected_resultant = {
        "content": [1024, 1],
        "factors": [
            {"polynomial_w": [[1,1,1]], "exponent": 2},
            {"polynomial_w": [[1,3,1],[0,2,1]], "exponent": 2},
            {"polynomial_w": [[2,2,1],[1,4,1],[0,3,1]], "exponent": 1},
            {"polynomial_w": [[3,32,1],[2,96,1],[1,104,1],[0,39,1]], "exponent": 1},
            {"polynomial_w": [[6,10240,1],[5,61440,1],[4,158720,1],[3,225216,1],[2,184192,1],[1,81840,1],[0,15345,1]], "exponent": 1},
        ],
    }
    if residual["resultant_u"] != expected_resultant:
        fail("altered or noncanonical resultant factorization")
    singular_markers = run_singular(A, B, args.singular)

    # Independent semialgebraic branch audit on u,w >= 0.
    if 4*4-4*4*3 >= 0:
        fail("first residual quadratic unexpectedly has a real root")
    if not (-15 < 0 and 52 > 0):
        fail("survivor quadratic does not have roots of opposite signs")
    if not all(value > 0 for value in [1280,3840,6720,7072,5056,2160,525]):
        fail("sixth-degree rejected component lost coefficient positivity")
    # Component 3 gives 3w+2=0; component 4 gives 2w+2u+3=0.
    # Both are incompatible with u,w >= 0 by their positive constants and
    # nonnegative variable coefficients.
    semialgebraic_rejections = {
        "component_1": "discriminant(4u^2+4u+3)=-32<0",
        "component_3": "3w+2=0 forces w=-2/3<0",
        "component_4": "2w+2u+3>0 on u,w>=0",
        "component_5": "all seven u-polynomial coefficients are positive",
        "component_2": "w=0 and 52u^2-36u-15 has exactly one positive root",
    }

    survivor = data["surviving_component"]
    expected_survivor = {
        "w": 0,
        "u_polynomial_ascending": [-15,-36,52],
        "u_positive_root": "(9+2*sqrt(69))/26",
        "alpha": "u+3/2=(24+sqrt(69))/13",
        "alpha_polynomial_ascending": [39,-48,13],
        "alpha_isolating_interval": [[12,5],[5,2]],
        "normalized_coordinates": ["alpha","alpha","1","1","1"],
    }
    if not isinstance(survivor.get("w"), int) or isinstance(survivor.get("w"), bool):
        fail("surviving w has non-integer JSON type")
    if survivor != expected_survivor:
        fail("altered survivor certificate")
    one_variable_u = Poly.variable(0, 1)
    for index, h in enumerate(face_H):
        h_w0 = h.substitute([one_variable_u, Poly.constant(0, 1)])
        if univariate_remainder(h_w0, [-15, -36, 52]):
            fail(f"survivor fails full critical equation {index}")

    # Full ambient Hessian rebuilt over Q(alpha), including all cross terms.
    av = [Poly.variable(i, 5) for i in range(5)]
    T5 = sum(av, Poly.constant(0, 5))/2
    P5 = T5**4-sum(((T5-ai)**4 for ai in av), Poly.constant(0, 5))
    for i, j in itertools.combinations(range(5), 2):
        P5 += (-1 if (i,j)==(0,1) else 1)*(T5-av[i]-av[j])**4
    S5 = sum((ai*ai for ai in av), Poly.constant(0, 5))
    alpha = Quad(0, 1)
    point = [alpha, alpha, Quad(1), Quad(1), Quad(1)]
    pvalue, svalue = P5.evaluate_quad(point), S5.evaluate_quad(point)
    pi = [P5.derivative(i).evaluate_quad(point) for i in range(5)]
    pij = [[P5.derivative(i).derivative(j).evaluate_quad(point) for j in range(5)] for i in range(5)]
    M = []
    for i in range(5):
        row = []
        for j in range(5):
            delta = Quad(1 if i==j else 0)
            row.append(delta/svalue-2*point[i]*point[j]/(svalue*svalue)+pij[i][j]/pvalue-pi[i]*pi[j]/(pvalue*pvalue)+delta/(point[i]*point[i]))
        M.append(row)
    zero, oneq = Quad(0), Quad(1)
    L = [oneq,-oneq,zero,zero,zero]
    S1 = [zero,zero,oneq,-oneq,zero]
    S2 = [zero,zero,oneq,oneq,Quad(-2)]
    C = [Quad(3),Quad(3),-2*alpha,-2*alpha,-2*alpha]
    basis = [L,S1,S2,C]
    for vector in basis:
        if sum((vector[i]*point[i] for i in range(5)), Quad(0)) != zero:
            fail("purported Hessian vector is not tangent")
    gram = [[qform(left,M,right) for right in basis] for left in basis]
    for i in range(4):
        for j in range(4):
            if i != j and gram[i][j] != zero:
                fail("tangent Hessian Gram matrix is not block diagonal")
    expected_forms = [
        Quad(Fraction(-54388,864435),Fraction(-71136,864435)),
        Quad(Fraction(-5468,66495),Fraction(1664,66495)),
        Quad(Fraction(-16404,66495),Fraction(4992,66495)),
        Quad(Fraction(-2580,169),Fraction(1248,169)),
    ]
    if [gram[i][i] for i in range(4)] != expected_forms:
        fail("independent full Hessian Gram matrix disagrees")
    left, right = Fraction(12,5), Fraction(5,2)
    modulus = lambda value: 13*value*value-48*value+39
    if not (modulus(left)<0<modulus(right) and 26*left-48>0):
        fail("alpha isolating interval is invalid")
    if not (expected_forms[0].c0+expected_forms[0].c1*left<0):
        fail("large-block sign failed")
    if not (expected_forms[1].c0+expected_forms[1].c1*right<0):
        fail("small-block sign failed")
    if not (expected_forms[3].c0+expected_forms[3].c1*left>0):
        fail("contrast sign failed")
    if pvalue != Quad(Fraction(-39,4),24):
        fail("candidate P value identity failed")

    expected_hessian = {
        "matrix_formula": "Mij=deltaij/S-2*ai*aj/S^2+Pij/P-Pi*Pj/P^2+deltaij/ai^2",
        "tangent_vectors": {"large_block":["1","-1","0","0","0"],"small_block":["0","0","1","-1","0"],"block_contrast":["3","3","-2*alpha","-2*alpha","-2*alpha"]},
        "reduced_quadratic_forms_mod_13alpha2-48alpha+39": {
            "large_block":{"linear_numerator_ascending":[-54388,-71136],"denominator":864435,"sign":"negative"},
            "small_block":{"linear_numerator_ascending":[-5468,1664],"denominator":66495,"sign":"negative"},
            "block_contrast":{"linear_numerator_ascending":[-2580,1248],"denominator":169,"sign":"positive"},
        },
        "symmetry_dimensions":{"large_block":1,"small_block":2,"block_contrast":1},
        "tangent_signature":["negative","negative","negative","positive"],
    }
    dimensions = data.get("hessian", {}).get("symmetry_dimensions", {})
    if not isinstance(dimensions, dict) or any(
        not isinstance(value, int) or isinstance(value, bool) for value in dimensions.values()
    ):
        fail("Hessian symmetry dimensions have non-integer JSON types")
    if data["hessian"] != expected_hessian:
        fail("altered or noncanonical Hessian certificate")

    result = {
        "status": "PASS",
        "method": "Fraction sparse polynomials + independently generated Singular ideal audit + Q(alpha) Hessian; no builder imports",
        "python": platform.python_version(),
        "singular": subprocess.run([args.singular, "--version"], text=True, capture_output=True).stdout.splitlines()[0],
        "seed": args.seed,
        "random_exact_checks": args.random_checks,
        "active_subsets_at_strict_sample": active_subsets,
        "paired_equals_32_subset": True,
        "critical_numerator_F_squared_identities": 4,
        "bernstein_degree": 9,
        "bernstein_rows": len(recomputed_rows),
        "bernstein_positive_parameter_monomials": len(all_coefficients),
        "bernstein_minimum_positive_coefficient": str(min(all_coefficients)),
        "bernstein_rows_sha256": digest,
        "zero_set_endpoint_witnesses": [[9,0],[0,9]],
        "margin_chart": margin_chart,
        "singular_residual_checks": singular_markers,
        "semialgebraic_component_audit": semialgebraic_rejections,
        "survivor_all_H_remainders_zero": True,
        "full_tangent_gram_diagonal": [entry.pair() for entry in expected_forms],
        "tangent_signature": ["negative","negative","negative","positive"],
        "certificate_sha256": hashlib.sha256(raw).hexdigest(),
        "audit_script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    print(json.dumps({k:v for k,v in result.items() if k != "margin_chart"}, indent=2))


if __name__ == "__main__":
    main()
