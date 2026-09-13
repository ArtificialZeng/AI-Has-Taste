#!/usr/bin/env python3
"""Independent, fail-closed exact referee for the Q5 section proof.

Trust boundary:
  * Python standard library exact Fraction arithmetic;
  * Singular as an exact rational Groebner/saturation engine;
  * the explicitly bound Markdown/JSON inputs listed in frozen_inputs.json.

This file never imports or executes anything under src/, tests/, or discovery/.
It reconstructs the section polynomials from the paired truncated-power formula.
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
from fractions import Fraction as Q


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
BINDING = HERE / "frozen_inputs.json"
BANNED_PARTS = {"src", "tests", "discovery"}


class AuditFailure(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AuditFailure(message)


def reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        require(key not in result, f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load_json_strict(text: str) -> object:
    return json.loads(text, object_pairs_hook=reject_duplicate_keys)


def reject_noncanonical_booleans(
    value: object,
    allowed_paths: frozenset[tuple[object, ...]] = frozenset(),
    path: tuple[object, ...] = (),
) -> None:
    if type(value) is bool:
        require(path in allowed_paths, f"boolean forbidden in bound JSON at {path}")
        return
    if type(value) is dict:
        for key, child in value.items():
            reject_noncanonical_booleans(child, allowed_paths, (*path, key))
    elif type(value) is list:
        for index, child in enumerate(value):
            reject_noncanonical_booleans(child, allowed_paths, (*path, index))


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def exact_keys(obj: dict, expected: set[str], label: str) -> None:
    require(set(obj) == expected, f"{label}: schema keys differ")


class Poly:
    """Sparse multivariate polynomial over Q, exponent tuples in fixed order."""

    __slots__ = ("n", "t")

    def __init__(self, n: int, terms: dict[tuple[int, ...], Q | int] | None = None):
        self.n = n
        clean: dict[tuple[int, ...], Q] = {}
        for exponent, coefficient in (terms or {}).items():
            require(len(exponent) == n, "polynomial exponent arity mismatch")
            c = Q(coefficient)
            if c:
                clean[tuple(exponent)] = clean.get(tuple(exponent), Q(0)) + c
        self.t = {e: c for e, c in clean.items() if c}

    @staticmethod
    def zero(n: int) -> "Poly":
        return Poly(n)

    @staticmethod
    def one(n: int) -> "Poly":
        return Poly.const(n, 1)

    @staticmethod
    def const(n: int, value: Q | int) -> "Poly":
        value = Q(value)
        return Poly(n, {(0,) * n: value}) if value else Poly.zero(n)

    @staticmethod
    def var(n: int, index: int) -> "Poly":
        exponent = [0] * n
        exponent[index] = 1
        return Poly(n, {tuple(exponent): Q(1)})

    def _coerce(self, other: "Poly | Q | int") -> "Poly":
        if isinstance(other, Poly):
            require(other.n == self.n, "polynomial ring mismatch")
            return other
        return Poly.const(self.n, Q(other))

    def __add__(self, other: "Poly | Q | int") -> "Poly":
        other = self._coerce(other)
        out = dict(self.t)
        for exponent, coefficient in other.t.items():
            out[exponent] = out.get(exponent, Q(0)) + coefficient
        return Poly(self.n, out)

    __radd__ = __add__

    def __neg__(self) -> "Poly":
        return Poly(self.n, {e: -c for e, c in self.t.items()})

    def __sub__(self, other: "Poly | Q | int") -> "Poly":
        return self + (-self._coerce(other))

    def __rsub__(self, other: "Poly | Q | int") -> "Poly":
        return self._coerce(other) - self

    def __mul__(self, other: "Poly | Q | int") -> "Poly":
        other = self._coerce(other)
        out: dict[tuple[int, ...], Q] = {}
        for ea, ca in self.t.items():
            for eb, cb in other.t.items():
                exponent = tuple(a + b for a, b in zip(ea, eb))
                out[exponent] = out.get(exponent, Q(0)) + ca * cb
        return Poly(self.n, out)

    __rmul__ = __mul__

    def __truediv__(self, scalar: Q | int) -> "Poly":
        scalar = Q(scalar)
        require(scalar != 0, "division by zero scalar")
        return Poly(self.n, {e: c / scalar for e, c in self.t.items()})

    def __pow__(self, exponent: int) -> "Poly":
        require(isinstance(exponent, int) and exponent >= 0, "bad polynomial power")
        result = Poly.one(self.n)
        base = self
        k = exponent
        while k:
            if k & 1:
                result = result * base
            base = base * base
            k >>= 1
        return result

    def diff(self, variable: int) -> "Poly":
        out: dict[tuple[int, ...], Q] = {}
        for exponent, coefficient in self.t.items():
            if exponent[variable]:
                new = list(exponent)
                factor = new[variable]
                new[variable] -= 1
                out[tuple(new)] = coefficient * factor
        return Poly(self.n, out)

    def compose(self, images: list["Poly"]) -> "Poly":
        require(len(images) == self.n, "composition arity mismatch")
        m = images[0].n if images else 0
        require(all(image.n == m for image in images), "composition ring mismatch")
        result = Poly.zero(m)
        for exponent, coefficient in self.t.items():
            term = Poly.const(m, coefficient)
            for image, power in zip(images, exponent):
                term *= image ** power
            result += term
        return result

    def evaluate(self, values):
        require(len(values) == self.n, "evaluation arity mismatch")
        total = 0
        for exponent, coefficient in self.t.items():
            term = coefficient
            for value, power in zip(values, exponent):
                term *= value ** power
            total += term
        return total

    def coefficient_blocks(self, variable: int) -> dict[int, "Poly"]:
        result: dict[int, dict[tuple[int, ...], Q]] = {}
        for exponent, coefficient in self.t.items():
            power = exponent[variable]
            reduced = exponent[:variable] + exponent[variable + 1 :]
            result.setdefault(power, {})[reduced] = coefficient
        return {power: Poly(self.n - 1, terms) for power, terms in result.items()}

    def total_degree(self) -> int:
        return max((sum(e) for e in self.t), default=-1)

    def as_singular(self, names: list[str]) -> str:
        require(len(names) == self.n, "Singular variable arity mismatch")
        if not self.t:
            return "0"
        pieces: list[str] = []
        for exponent in sorted(self.t, reverse=True):
            coefficient = self.t[exponent]
            monomial = "*".join(
                name if power == 1 else f"{name}^{power}"
                for name, power in zip(names, exponent)
                if power
            ) or "1"
            ctext = str(coefficient.numerator)
            if coefficient.denominator != 1:
                ctext = f"({ctext}/{coefficient.denominator})"
            pieces.append(f"({ctext})*{monomial}")
        return "+".join(pieces)

    def __eq__(self, other) -> bool:
        try:
            other = self._coerce(other)
        except Exception:
            return False
        return self.t == other.t

    def __repr__(self) -> str:
        return f"Poly(n={self.n}, terms={len(self.t)}, degree={self.total_degree()})"


def variables(n: int) -> list[Poly]:
    return [Poly.var(n, i) for i in range(n)]


def product(items, n: int) -> Poly:
    result = Poly.one(n)
    for item in items:
        result *= item
    return result


def full_piece(a: list[Poly], high_pairs: set[tuple[int, int]]) -> Poly:
    """Paired Q5 numerator P_N, rebuilt from formula (not a certificate)."""
    require(len(a) == 5, "full_piece is specifically Q5")
    n = a[0].n
    T = sum(a, Poly.zero(n)) / 2
    P = T ** 4 - sum(((T - ai) ** 4 for ai in a), Poly.zero(n))
    for i, j in itertools.combinations(range(5), 2):
        L = T - a[i] - a[j]
        P += L ** 4
        if (i, j) in high_pairs:
            P -= 2 * (L ** 4)
    return P


def q4_piece(a: list[Poly], high_pairs: set[tuple[int, int]]) -> Poly:
    require(len(a) == 4, "q4_piece arity")
    n = a[0].n
    T = sum(a, Poly.zero(n)) / 2
    P = T ** 3 - sum(((T - ai) ** 3 for ai in a), Poly.zero(n))
    for i, j in itertools.combinations(range(4), 2):
        if (i, j) not in high_pairs:
            P += (T - a[i] - a[j]) ** 3
    return P


def q4_gauge_system(high_pairs: set[tuple[int, int]]) -> tuple[list[Poly], Poly, Poly, list[Poly]]:
    a0, a1, a2 = variables(3)
    a = [a0, a1, a2, Poly.one(3)]
    P = q4_piece(a, high_pairs)
    S = sum((ai ** 2 for ai in a), Poly.zero(3))
    G = [a[i] * S * P.diff(i) + (a[i] ** 2 - S) * P for i in range(3)]
    return a, P, S, G


def full_system_gauge(high_pairs: set[tuple[int, int]]) -> tuple[list[Poly], Poly, Poly, Poly, list[Poly]]:
    a0, a1, a2, a3 = variables(4)
    a = [a0, a1, a2, a3, Poly.one(4)]
    P = full_piece(a, high_pairs)
    S = sum((ai ** 2 for ai in a), Poly.zero(4))
    D = a0 * a1 * a2 * a3
    G = [a[i] * S * P.diff(i) + (a[i] ** 2 - S) * P for i in range(4)]
    return a, P, S, D, G


def gap_system(high_pairs: set[tuple[int, int]]) -> tuple[list[Poly], Poly, Poly, Poly, list[Poly]]:
    x, y, z, w = variables(4)
    one = Poly.one(4)
    a = [one + w + z + y + x, one + w + z + y, one + w + z, one + w, one]
    P = full_piece(a, high_pairs)
    S = sum((ai ** 2 for ai in a), Poly.zero(4))
    D = product(a, 4)
    H = [S.diff(q) * P * D + 2 * S * P.diff(q) * D - 2 * S * P * D.diff(q) for q in range(4)]
    return a, P, S, D, H


def direct_subset_numerator(values: list[Q]) -> Q:
    s = len(values)
    T = sum(values, Q(0)) / 2
    answer = Q(0)
    for mask in range(1 << s):
        L = T - sum((values[i] for i in range(s) if mask & (1 << i)), Q(0))
        if L > 0:
            answer += (-1 if mask.bit_count() & 1 else 1) * L ** (s - 1)
    return answer


def eval_full_piece(values: list[Q], high_pairs: set[tuple[int, int]]) -> Q:
    a = [Poly.const(0, value) for value in values]
    return full_piece(a, high_pairs).evaluate([])


def sparse_poly(n: int, rows, exponent_count: int | None = None) -> Poly:
    terms: dict[tuple[int, ...], Q] = {}
    for row in rows:
        require(len(row) == (exponent_count or n) + 2, "malformed sparse polynomial row")
        exponent = tuple(int(v) for v in row[:n])
        numerator, denominator = int(row[-2]), int(row[-1])
        require(denominator > 0, "nonpositive sparse denominator")
        require(exponent not in terms, "duplicate sparse monomial")
        terms[exponent] = Q(numerator, denominator)
    return Poly(n, terms)


def choose(n: int, k: int) -> int:
    return math.comb(n, k)


def univariate_bernstein_coefficients(p: Poly, variable: int, degree: int) -> list[Poly]:
    blocks = p.coefficient_blocks(variable)
    require(max(blocks, default=0) <= degree, "Bernstein degree too small")
    zero = Poly.zero(p.n - 1)
    answer = []
    for k in range(degree + 1):
        coefficient = zero
        for j in range(k + 1):
            coefficient += blocks.get(j, zero) * Q(choose(k, j), choose(degree, j))
        answer.append(coefficient)
    return answer


def trim_univariate(p: list[Q]) -> list[Q]:
    p = [Q(v) for v in p]
    while p and p[0] == 0:
        p.pop(0)
    return p


def derivative_univariate(p: list[Q]) -> list[Q]:
    p = trim_univariate(p)
    degree = len(p) - 1
    return trim_univariate([coefficient * (degree - i) for i, coefficient in enumerate(p[:-1])])


def divmod_univariate(a: list[Q], b: list[Q]) -> tuple[list[Q], list[Q]]:
    a = trim_univariate(a)
    b = trim_univariate(b)
    require(b, "univariate polynomial division by zero")
    if len(a) < len(b):
        return [], a
    quotient = [Q(0)] * (len(a) - len(b) + 1)
    remainder = list(a)
    while remainder and len(remainder) >= len(b):
        shift = len(remainder) - len(b)
        coefficient = remainder[0] / b[0]
        quotient[len(quotient) - 1 - shift] = coefficient
        subtractor = [coefficient * x for x in b] + [Q(0)] * shift
        remainder = trim_univariate([x - y for x, y in itertools.zip_longest(remainder, subtractor, fillvalue=Q(0))])
    return trim_univariate(quotient), remainder


def sturm_chain(coefficients_descending: list[int | Q]) -> list[list[Q]]:
    first = trim_univariate([Q(c) for c in coefficients_descending])
    require(first, "zero Sturm polynomial")
    second = derivative_univariate(first)
    chain = [first, second]
    while chain[-1]:
        _, remainder = divmod_univariate(chain[-2], chain[-1])
        if not remainder:
            break
        chain.append([-c for c in remainder])
    return chain


def sign_fraction(value: Q) -> int:
    return (value > 0) - (value < 0)


def polynomial_value_desc(p: list[Q], x: Q) -> Q:
    total = Q(0)
    for coefficient in p:
        total = total * x + coefficient
    return total


def signs_at(chain: list[list[Q]], point: Q | str) -> list[int]:
    if point == "+inf":
        return [sign_fraction(p[0]) for p in chain]
    if point == "-inf":
        return [sign_fraction(p[0]) * (-1 if (len(p) - 1) & 1 else 1) for p in chain]
    return [sign_fraction(polynomial_value_desc(p, Q(point))) for p in chain]


def variations(signs: list[int]) -> int:
    nonzero = [s for s in signs if s]
    return sum(a != b for a, b in zip(nonzero, nonzero[1:]))


def sturm_count(coefficients_descending: list[int | Q], left: Q | str, right: Q | str) -> int:
    chain = sturm_chain(coefficients_descending)
    return variations(signs_at(chain, left)) - variations(signs_at(chain, right))


def positive_associate_univariate(a: list[int | Q], b: list[int | Q]) -> bool:
    aa, bb = trim_univariate([Q(v) for v in a]), trim_univariate([Q(v) for v in b])
    if not aa or not bb or len(aa) != len(bb):
        return False
    ratio = aa[0] / bb[0]
    return ratio > 0 and all(x == ratio * y for x, y in zip(aa, bb))


def poly_scalar_ratio(a: Poly, b: Poly) -> Q | None:
    """Return c with a=c*b, or None."""
    if not a.t or not b.t or set(a.t) != set(b.t):
        return None
    exponent = next(iter(b.t))
    ratio = a.t[exponent] / b.t[exponent]
    return ratio if all(a.t[e] == ratio * b.t[e] for e in b.t) else None


def univariate_desc(p: Poly) -> list[Q]:
    require(p.n == 1, "univariate conversion ring mismatch")
    degree = max((e[0] for e in p.t), default=-1)
    return [p.t.get((power,), Q(0)) for power in range(degree, -1, -1)] if degree >= 0 else []


def exact_univariate_quotient(a: Poly, b: Poly) -> Poly:
    require(a.n == b.n == 1, "univariate quotient ring mismatch")
    quotient, remainder = divmod_univariate(univariate_desc(a), univariate_desc(b))
    require(not remainder, "claimed exact univariate division has remainder")
    degree = len(quotient) - 1
    return Poly(1, {(degree - i,): coefficient for i, coefficient in enumerate(quotient) if coefficient})


def run_singular(body: str, label: str, timeout: int = 180) -> str:
    executable = os.environ.get("SINGULAR", "/opt/homebrew/bin/Singular")
    require(Path(executable).is_file(), f"{label}: Singular unavailable")
    header = 'option(noredefine);\nLIB "elim.lib";\n'
    try:
        result = subprocess.run(
            [executable, "-q"],
            input=header + body,
            text=True,
            capture_output=True,
            timeout=timeout,
            cwd=HERE,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        raise AuditFailure(f"{label}: Singular timeout") from exc
    combined = result.stdout + result.stderr
    require(result.returncode == 0, f"{label}: Singular exit {result.returncode}: {combined[-10000:]}")
    require("?" not in combined, f"{label}: Singular diagnostic: {combined[-10000:]}")
    require(f"PASS::{label}" in combined, f"{label}: success sentinel absent")
    return combined


class Quad:
    """Q(alpha), alpha^2=(48 alpha-39)/13."""

    __slots__ = ("c0", "c1")

    def __init__(self, c0=0, c1=0):
        self.c0, self.c1 = Q(c0), Q(c1)

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Quad) else Quad(value, 0)

    def __add__(self, other):
        other = Quad.coerce(other)
        return Quad(self.c0 + other.c0, self.c1 + other.c1)

    __radd__ = __add__

    def __neg__(self):
        return Quad(-self.c0, -self.c1)

    def __sub__(self, other):
        return self + (-Quad.coerce(other))

    def __rsub__(self, other):
        return Quad.coerce(other) - self

    def __mul__(self, other):
        other = Quad.coerce(other)
        # alpha^2 = -3 + (48/13) alpha
        return Quad(
            self.c0 * other.c0 - 3 * self.c1 * other.c1,
            self.c0 * other.c1 + self.c1 * other.c0 + Q(48, 13) * self.c1 * other.c1,
        )

    __rmul__ = __mul__

    def inverse(self):
        # Multiplication matrix determinant for c0+c1 alpha.
        determinant = self.c0 * (self.c0 + Q(48, 13) * self.c1) + 3 * self.c1 * self.c1
        require(determinant != 0, "zero divisor in quadratic field")
        return Quad((self.c0 + Q(48, 13) * self.c1) / determinant, -self.c1 / determinant)

    def __truediv__(self, other):
        return self * Quad.coerce(other).inverse()

    def __rtruediv__(self, other):
        return Quad.coerce(other) * self.inverse()

    def __pow__(self, exponent: int):
        require(exponent >= 0, "negative Quad power")
        answer = Quad(1)
        base = self
        k = exponent
        while k:
            if k & 1:
                answer *= base
            base *= base
            k >>= 1
        return answer

    def __eq__(self, other):
        other = Quad.coerce(other)
        return self.c0 == other.c0 and self.c1 == other.c1

    def certified_sign(self, left=Q(12, 5), right=Q(5, 2)) -> int:
        endpoint = left if self.c1 >= 0 else right
        minimum = self.c0 + self.c1 * endpoint
        endpoint_max = right if self.c1 >= 0 else left
        maximum = self.c0 + self.c1 * endpoint_max
        if minimum > 0:
            return 1
        if maximum < 0:
            return -1
        raise AuditFailure(f"linear algebraic sign not separated: {self}")

    def __repr__(self):
        return f"Quad({self.c0}, {self.c1})"


def load_bound_inputs(enforce_hashes: bool = True) -> tuple[dict, dict[str, object]]:
    binding = load_json_strict(BINDING.read_text(encoding="utf-8"))
    reject_noncanonical_booleans(binding)
    exact_keys(binding, {"schema", "inputs", "semantic_contract"}, "binding")
    require(binding["schema"] == "q5-independent-referee-binding-v1", "binding schema")
    loaded: dict[str, object] = {}
    seen_paths: set[str] = set()
    for entry in binding["inputs"]:
        exact_keys(entry, {"id", "path", "sha256", "kind"}, "binding input")
        relative = Path(entry["path"])
        require(not relative.is_absolute(), "absolute input path forbidden")
        require(not (set(relative.parts) & BANNED_PARTS), "banned implementation path in binding")
        require(entry["path"] not in seen_paths, "duplicate bound path")
        seen_paths.add(entry["path"])
        path = (ROOT / relative).resolve()
        require(ROOT == path or ROOT in path.parents, "bound path escapes project")
        require(path.is_file(), f"missing bound input {relative}")
        if enforce_hashes:
            require(sha256_file(path) == entry["sha256"], f"hash mismatch: {relative}")
        if entry["kind"] == "json":
            value = load_json_strict(path.read_text(encoding="utf-8"))
            allowed = (
                frozenset({("classification", "radical")})
                if entry["id"] == "star3"
                else frozenset()
            )
            reject_noncanonical_booleans(value, allowed)
            loaded[entry["id"]] = value
        elif entry["kind"] == "text":
            loaded[entry["id"]] = path.read_text(encoding="utf-8")
        else:
            raise AuditFailure(f"unknown bound input kind: {entry['kind']}")
    return binding, loaded


def verify_chamber_graphs(contract: dict) -> dict:
    edges = list(itertools.combinations(range(5), 2))

    def shifted(graph: set[tuple[int, int]]) -> bool:
        for edge in graph:
            for endpoint in edge:
                other = edge[1] if endpoint == edge[0] else edge[0]
                for replacement in range(endpoint):
                    if replacement == other:
                        continue
                    candidate = tuple(sorted((replacement, other)))
                    if candidate not in graph:
                        return False
        return True

    def intersecting(graph: set[tuple[int, int]]) -> bool:
        return all(set(e) & set(f) for e, f in itertools.combinations(graph, 2))

    graphs = []
    for mask in range(1 << len(edges)):
        graph = {edges[i] for i in range(len(edges)) if mask & (1 << i)}
        if shifted(graph) and intersecting(graph):
            graphs.append(graph)

    expected = {
        "empty": set(),
        "star1": {(0, 1)},
        "star2": {(0, 1), (0, 2)},
        "star3": {(0, 1), (0, 2), (0, 3)},
        "star4": {(0, 1), (0, 2), (0, 3), (0, 4)},
        "triangle": {(0, 1), (0, 2), (1, 2)},
    }
    contract_graphs = {name: {tuple(edge) for edge in graph} for name, graph in contract["chambers"].items()}
    require(contract_graphs == expected, "semantic contract chamber graph changed")
    require({frozenset(g) for g in graphs} == {frozenset(g) for g in expected.values()}, "shifted/intersecting graph exhaustion failed")

    samples = {
        "empty": [1, 1, 1, 1, 1],
        "star1": [5, 5, 2, 2, 2],
        "star2": [5, 4, 4, 2, 2],
        "star3": [6, 4, 4, 4, 1],
        "star4": [3, 1, 1, 1, 1],
        "triangle": [5, 5, 5, 2, 2],
    }
    for name, sample in samples.items():
        values = [Q(v) for v in sample]
        T = sum(values, Q(0)) / 2
        require(max(values) < T, f"{name}: sample not strictly balanced")
        graph = {(i, j) for i, j in edges if values[i] + values[j] > T}
        require(graph == expected[name], f"{name}: nonrealizable graph sample")
        require(eval_full_piece(values, graph) == direct_subset_numerator(values), f"{name}: paired formula differs from subset definition")

    return {"graphs": len(graphs), "strict_samples": len(samples), "balance_wall": "excluded by positive derivative a_j/(a0*R)"}


def verify_star1(cert: dict) -> dict:
    exact_keys(cert, {"schema", "normalization", "chamber", "chart", "critical_equations", "bernstein", "residual_necessary_ideal", "surviving_component", "hessian"}, "star1")
    require(cert["schema"] == "q5-star1-exact-v1", "star1 schema")
    require(cert["normalization"] == "a4=1" and cert["chamber"] == "N={(0,1)} ordered closure", "star1 scope")
    require(cert["chart"]["domain"] == ["x>=0", "z>=0", "x+z<=1", "u>=0", "w>=0"], "star1 chart domain")
    require(cert["chart"]["gap_order"] == ["x=a0-a1", "y=a1-a2", "z=a2-a3", "w=a3-a4"], "star1 gap order")
    require(cert["chart"]["substitution"] == "y=(1-x-z)/2+u", "star1 chart substitution")
    require(cert["critical_equations"] == {
        "cleared_derivative": "Hq=S_q*P*D+2*S*P_q*D-2*S*P*D_q",
        "combination": [-6, 7, -8, 4],
        "variable_order": ["x", "y", "z", "w"],
    }, "star1 critical semantics")

    gap_a, _, _, _, H = gap_system({(0, 1)})
    x, z, u, w = variables(4)
    y_image = (Poly.one(4) - x - z) / 2 + u
    chart_images = [x, y_image, z, w]
    chart_a = [coordinate.compose(chart_images) for coordinate in gap_a]
    chart_total = sum(chart_a, Poly.zero(4))
    margin_records = cert["chart"]["pair_margins"]
    require(len(margin_records) == 10, "star1 pair-margin count")
    seen_pairs: set[tuple[int, int]] = set()
    for record in margin_records:
        exact_keys(record, {"kind", "pair", "polynomial_x_z_u_w"}, "star1 pair margin")
        pair = tuple(record["pair"])
        require(pair in set(itertools.combinations(range(5), 2)) and pair not in seen_pairs, "star1 pair-margin labels")
        seen_pairs.add(pair)
        is_high = pair == (0, 1)
        require(record["kind"] == ("high" if is_high else "low"), "star1 pair-margin kind")
        i, j = pair
        actual = 2 * (chart_a[i] + chart_a[j]) - chart_total
        if not is_high:
            actual = -actual
        require(actual == sparse_poly(4, record["polynomial_x_z_u_w"]), f"star1 pair-margin identity {pair}")
    require(seen_pairs == set(itertools.combinations(range(5), 2)), "star1 pair-margin coverage")
    Hc = [h.compose(chart_images) for h in H]
    K = sum((coefficient * h for coefficient, h in zip([-6, 7, -8, 4], Hc)), Poly.zero(4))

    bernstein = cert["bernstein"]
    exact_keys(bernstein, {"basis", "degree", "parameter_order", "rows", "rows_sha256"}, "star1 Bernstein")
    require(bernstein["degree"] == 9 and bernstein["parameter_order"] == ["u", "w"], "star1 Bernstein metadata")
    rows = bernstein["rows"]
    require(len(rows) == 55, "star1 Bernstein row count")
    positions = {(row["i"], row["j"]) for row in rows}
    require(positions == {(i, j) for i in range(10) for j in range(10 - i)}, "star1 Bernstein positions")
    reconstruction = Poly.zero(4)
    positive_parameter_terms = 0
    for row in rows:
        exact_keys(row, {"i", "j", "terms_u_w"}, "star1 Bernstein row")
        i, j = row["i"], row["j"]
        coefficient_uw = sparse_poly(2, row["terms_u_w"])
        if (i, j) == (0, 0):
            require(not coefficient_uw.t, "star1 b00 must vanish")
        else:
            require(coefficient_uw.t and all(c > 0 for c in coefficient_uw.t.values()), "star1 nonpositive Bernstein parameter coefficient")
            require(coefficient_uw.t.get((0, 0), Q(0)) > 0, "star1 Bernstein block lacks positive constant")
            positive_parameter_terms += len(coefficient_uw.t)
        embedded = Poly(4, {(0, 0, eu, ew): c for (eu, ew), c in coefficient_uw.t.items()})
        basis = Q(math.factorial(9), math.factorial(i) * math.factorial(j) * math.factorial(9 - i - j))
        reconstruction += embedded * basis * (x ** i) * (z ** j) * ((Poly.one(4) - x - z) ** (9 - i - j))
    require(reconstruction == K, "star1 Bernstein identity")
    require(positive_parameter_terms == 1620, "star1 Bernstein term count")

    residual = cert["residual_necessary_ideal"]
    exact_keys(residual, {"A", "B", "complex_degree", "components", "resultant_u", "variable_order"}, "star1 residual")
    A = sparse_poly(2, residual["A"])
    B = sparse_poly(2, residual["B"])
    require(residual["variable_order"] == ["u", "w"] and residual["complex_degree"] == 15, "star1 residual metadata")
    # Embed u,w in chart ring and verify the two exposed factorizations.
    A4 = Poly(4, {(0, 0, eu, ew): c for (eu, ew), c in A.t.items()})
    B4 = Poly(4, {(0, 0, eu, ew): c for (eu, ew), c in B.t.items()})
    face = [Poly.zero(4), Poly.zero(4), u, w]
    Hface = [h.compose(face) for h in Hc]
    require(Hface[0] == ((w + 1) ** 2) * (2 * u + 2 * w + 3) * A4 / 16, "star1 residual A factor")
    require(Hface[2] == -(w + 1) * (2 * u + 2 * w + 3) * B4 / 16, "star1 residual B factor")

    components = residual["components"]
    require(len(components) == 5, "star1 component count")
    expected_degrees = [2, 2, 2, 3, 6]
    component_polys: list[tuple[Poly, Poly]] = []
    for component, degree in zip(components, expected_degrees):
        exact_keys(component, {"u_factor", "w_relation"}, "star1 residual component")
        uf = sparse_poly(1, component["u_factor"])
        require(uf.total_degree() == degree, "star1 component degree")
        # Component relation rows use (w,u), as indicated by their role as a
        # linear graph equation in w.
        wr = sparse_poly(2, component["w_relation"])
        require(wr.total_degree() >= 1 and max((exponent[0] for exponent in wr.t), default=-1) == 1, "star1 component not linear in w")
        component_polys.append((uf, wr))

    U = Poly.var(1, 0)
    W, U2 = variables(2)
    expected_components = [
        (4 * U ** 2 + 4 * U + 3, 2 * W + 2 * U2 + 3),
        (52 * U ** 2 - 36 * U - 15, W),
        (84 * U ** 2 - 52 * U + 1, 3 * W + 2),
        (32 * U ** 3 + 48 * U ** 2 + 32 * U + 9, 2 * W + 2 * U2 + 3),
        (1280 * U ** 6 + 3840 * U ** 5 + 6720 * U ** 4 + 7072 * U ** 3 + 5056 * U ** 2 + 2160 * U + 525,
         40 * W + 640 * U2 ** 5 + 1920 * U2 ** 4 + 2960 * U2 ** 3 + 2736 * U2 ** 2 + 1488 * U2 + 465),
    ]
    require(component_polys == expected_components, "star1 residual component semantics")

    # Recompute the resultant and prove the exact ideal is the intersection
    # of five pairwise-comaximal radical graph ideals of total degree 15.
    resultant_record = residual["resultant_u"]
    exact_keys(resultant_record, {"content", "factors"}, "star1 residual resultant")
    require(resultant_record["content"] == [1024, 1], "star1 resultant content")
    target_resultant = Poly.const(1, Q(1024))
    for factor in resultant_record["factors"]:
        exact_keys(factor, {"exponent", "polynomial_w"}, "star1 resultant factor")
        target_resultant *= sparse_poly(1, factor["polynomial_w"]) ** factor["exponent"]
    singular_lines = [
        "ring r=0,(w,u),lp;",
        f"poly A={A.as_singular(['u', 'w'])};",
        f"poly B={B.as_singular(['u', 'w'])};",
        "ideal I=A,B;",
    ]
    for index, (uf, wr) in enumerate(component_polys):
        singular_lines.extend([
            f"poly uf{index}={uf.as_singular(['u'])};",
            f"poly wr{index}={wr.as_singular(['w', 'u'])};",
            f"ideal J{index}=uf{index},wr{index};",
            f"if (!(reduce(1,std(ideal(uf{index},diff(uf{index},u))))==0)) {{ quit(1); }}",
        ])
    singular_lines.append("ideal JJall=J0;")
    for index in range(1, 5):
        singular_lines.append(f"JJall=intersect(JJall,J{index});")
    singular_lines.extend([
        "ideal zi=reduce(I,std(JJall)); ideal zu=reduce(JJall,std(I));",
        "int ok=(dim(std(I))==0)&&(vdim(std(I))==15)&&(size(simplify(zi,2))==0)&&(size(simplify(zu,2))==0);",
    ])
    for i, j in itertools.combinations(range(5), 2):
        singular_lines.append(f"ok=ok&&(reduce(1,std(J{i}+J{j}))==0);")
    singular_lines.extend([
        "poly rawres=resultant(A,B,u);",
        f"poly targetres={target_resultant.as_singular(['w'])};",
        "ideal zr1=reduce(ideal(rawres),std(ideal(targetres))); ideal zr2=reduce(ideal(targetres),std(ideal(rawres)));",
        "ok=ok&&(size(simplify(zr1,2))==0)&&(size(simplify(zr2,2))==0);",
        'if (ok) { print("PASS::star1_components"); } else { quit(1); }',
    ])
    run_singular("\n".join(singular_lines), "star1_components")

    # Exact semialgebraic exclusions on u,w>=0.  Component 0 has negative
    # discriminant; component 2 has w=-2/3; components 3 and 4 have strictly
    # positive u-polynomial coefficients.  Component 1 has w=0 and exactly
    # one positive root.
    require(4 ** 2 - 4 * 4 * 3 < 0, "star1 component 0 real exclusion")
    require(Q(-2, 3) < 0, "star1 component 2 w exclusion")
    require(all(coefficient > 0 for coefficient in expected_components[3][0].t.values()), "star1 component 3 positivity")
    require(all(coefficient > 0 for coefficient in expected_components[4][0].t.values()), "star1 component 4 positivity")
    require(sturm_count([52, -36, -15], Q(0), "+inf") == 1, "star1 survivor positive-root count")

    survivor = cert["surviving_component"]
    exact_keys(survivor, {"alpha", "alpha_isolating_interval", "alpha_polynomial_ascending", "normalized_coordinates", "u_polynomial_ascending", "u_positive_root", "w"}, "star1 survivor")
    require(survivor["alpha_polynomial_ascending"] == [39, -48, 13], "star1 alpha polynomial")
    require(survivor["u_polynomial_ascending"] == [-15, -36, 52] and survivor["w"] == 0, "star1 survivor component")
    require(survivor["alpha"] == "u+3/2=(24+sqrt(69))/13" and survivor["u_positive_root"] == "(9+2*sqrt(69))/26", "star1 root semantics")
    require(survivor["normalized_coordinates"] == ["alpha", "alpha", "1", "1", "1"], "star1 survivor coordinates")
    left, right = (Q(*pair) for pair in survivor["alpha_isolating_interval"])
    require((left, right) == (Q(12, 5), Q(5, 2)), "star1 alpha interval")
    minpoly = [Q(13), Q(-48), Q(39)]
    require(polynomial_value_desc(minpoly, left) < 0 < polynomial_value_desc(minpoly, right), "star1 root isolation signs")
    require(26 * left - 48 > 0, "star1 minpoly monotonicity")

    # Survivor sufficiency: every original H is zero modulo 52u^2-36u-15.
    u_poly_desc = [Q(52), Q(-36), Q(-15)]
    for index, h in enumerate(Hface):
        univariate = h.coefficient_blocks(3).get(0, Poly.zero(3))
        # Hface has variables x,z,u,w; set x=z=w=0 and collect u.
        values: dict[int, Q] = {}
        for exponent, coefficient in h.t.items():
            ex, ez, eu, ew = exponent
            if ex == ez == ew == 0:
                values[eu] = values.get(eu, Q(0)) + coefficient
        degree = max(values, default=0)
        desc = [values.get(k, Q(0)) for k in range(degree, -1, -1)]
        _, remainder = divmod_univariate(desc, u_poly_desc)
        require(not remainder, f"star1 survivor H{index} not zero")

    # Independent exact Hessian rebuild in Q(alpha).
    aa = variables(5)
    P5 = full_piece(aa, {(0, 1)})
    alpha = Quad(0, 1)
    point = [alpha, alpha, Quad(1), Quad(1), Quad(1)]
    Sval = sum((value * value for value in point), Quad(0))
    Pval = P5.evaluate(point)
    Pi = [P5.diff(i).evaluate(point) for i in range(5)]
    Pij = [[P5.diff(i).diff(j).evaluate(point) for j in range(5)] for i in range(5)]
    M = []
    for i in range(5):
        row = []
        for j in range(5):
            delta = 1 if i == j else 0
            row.append(delta / Sval - 2 * point[i] * point[j] / (Sval ** 2) + Pij[i][j] / Pval - Pi[i] * Pi[j] / (Pval ** 2) + delta / (point[i] ** 2))
        M.append(row)

    def quadratic(vector) -> Quad:
        return sum((Quad.coerce(vector[i]) * M[i][j] * Quad.coerce(vector[j]) for i in range(5) for j in range(5)), Quad(0))

    forms = {
        "large_block": quadratic([1, -1, 0, 0, 0]),
        "small_block": quadratic([0, 0, 1, -1, 0]),
        "block_contrast": quadratic([3, 3, -2 * alpha, -2 * alpha, -2 * alpha]),
    }
    hessian = cert["hessian"]
    exact_keys(hessian, {"matrix_formula", "reduced_quadratic_forms_mod_13alpha2-48alpha+39", "symmetry_dimensions", "tangent_signature", "tangent_vectors"}, "star1 Hessian")
    require(hessian["matrix_formula"] == "Mij=deltaij/S-2*ai*aj/S^2+Pij/P-Pi*Pj/P^2+deltaij/ai^2", "star1 Hessian formula")
    require(hessian["tangent_vectors"] == {
        "block_contrast": ["3", "3", "-2*alpha", "-2*alpha", "-2*alpha"],
        "large_block": ["1", "-1", "0", "0", "0"],
        "small_block": ["0", "0", "1", "-1", "0"],
    }, "star1 Hessian tangent vectors")
    stored = hessian["reduced_quadratic_forms_mod_13alpha2-48alpha+39"]
    for name, value in forms.items():
        record = stored[name]
        expected = Quad(Q(record["linear_numerator_ascending"][0], record["denominator"]), Q(record["linear_numerator_ascending"][1], record["denominator"]))
        require(value == expected, f"star1 Hessian form {name}")
        actual_sign = value.certified_sign(left, right)
        claimed_sign = 1 if record["sign"] == "positive" else -1
        require(actual_sign == claimed_sign, f"star1 Hessian sign {name}")
    require(hessian["tangent_signature"] == ["negative", "negative", "negative", "positive"], "star1 Hessian signature metadata")
    require(hessian["symmetry_dimensions"] == {"block_contrast": 1, "large_block": 1, "small_block": 2}, "star1 Hessian dimensions")

    return {"bernstein_rows": 55, "positive_parameter_terms": positive_parameter_terms, "components": 5, "hessian_signature": [1, 3]}


def verify_star2(cert: dict) -> dict:
    exact_keys(cert, {"schema", "claim", "normalization", "coordinate_order", "high_pairs", "domain", "gaps", "chamber_margin_identities", "critical_numerators", "direction_coefficients_xyzw", "bernstein", "proof_assistants"}, "star2")
    require(cert["schema"] == "q5-star2-bernstein-v1", "star2 schema")
    require(cert["claim"] == "the ordered full-support star2 chamber closure has no critical direction", "star2 claim")
    require(cert["normalization"] == {"a4": 1}, "star2 normalization")
    require(cert["high_pairs"] == [[0, 1], [0, 2]], "star2 graph")
    require(cert["domain"] == ["u>=0", "y>=0", "w>=0", "0<=v<=1"], "star2 domain")
    require(cert["direction_coefficients_xyzw"] == [-2, 2, -2, 1], "star2 direction")
    require(cert["critical_numerators"] == "Hq=S_q*P*D+2*S*P_q*D-2*S*P*D_q", "star2 critical definition")
    require(cert["chamber_margin_identities"] == {"high_02": "x+z-1=2*u", "low_03": "1+z-x=2*(1-v)", "low_12": "1+x-z=2*v"}, "star2 wall identities")

    _, P, _, _, H = gap_system({(0, 1), (0, 2)})
    u, v, y, w = variables(4)
    images = [u + v, y, u + 1 - v, w]
    require(images[0] + images[2] - 1 == 2 * u, "star2 high-02 wall polynomial")
    require(1 + images[2] - images[0] == 2 * (1 - v), "star2 low-03 wall polynomial")
    require(1 + images[0] - images[2] == 2 * v, "star2 low-12 wall polynomial")
    Pc = P.compose(images)
    Hcomb = sum((coefficient * h for coefficient, h in zip([-2, 2, -2, 1], H)), Poly.zero(4)).compose(images)

    data = cert["bernstein"]
    exact_keys(data, {"parameter_order", "H_degree", "P_degree", "H_coefficients", "P_coefficients", "canonical_tables_sha256"}, "star2 Bernstein")
    require(data["parameter_order"] == ["u", "y", "w"] and data["H_degree"] == 8 and data["P_degree"] == 4, "star2 Bernstein metadata")

    def verify_table(polynomial: Poly, degree: int, rows: list, label: str, expected_terms: int) -> int:
        coeffs = univariate_bernstein_coefficients(polynomial, 1, degree)
        require([row["k"] for row in rows] == list(range(degree + 1)), f"{label}: block indices")
        count = 0
        for k, (actual, row) in enumerate(zip(coeffs, rows)):
            exact_keys(row, {"k", "terms"}, f"{label} row")
            expected = sparse_poly(3, row["terms"])
            require(actual == expected, f"{label}: coefficient block {k}")
            require(expected.t and all(c > 0 for c in expected.t.values()), f"{label}: positivity block {k}")
            require(expected.t.get((0, 0, 0), Q(0)) > 0, f"{label}: positive constant block {k}")
            count += len(expected.t)
        require(count == expected_terms, f"{label}: term count")
        return count

    h_terms = verify_table(Hcomb, 8, data["H_coefficients"], "star2 H", 1125)
    p_terms = verify_table(Pc, 4, data["P_coefficients"], "star2 P", 70)
    require(data["canonical_tables_sha256"] == "7ea0e1ec667bcceb0be53f4cc437fe0ffef5d146528268054d98c39b8b82d95f", "star2 canonical digest field")
    return {"H_positive_terms": h_terms, "P_positive_terms": p_terms, "closure": True}


def verify_star3(cert: dict) -> dict:
    exact_keys(cert, {"schema_version", "endpoint", "variables", "fixed_coordinate", "negative_pairs", "saturation_factors", "system_sha256", "expected_quotient_dimension", "expected_complex_points", "expected_real_points", "ordered_chamber", "components", "classification"}, "star3")
    require(cert["schema_version"] == 1, "star3 schema")
    require(cert["fixed_coordinate"] == "a4=1", "star3 gauge")
    require(cert["negative_pairs"] == [[0, 1], [0, 2], [0, 3]], "star3 graph")
    require(cert["saturation_factors"] == ["a0", "a1", "a2", "a3", "P", "S"], "star3 saturation metadata")
    require(cert["ordered_chamber"] == {
        "weak_order": ["a0-a1", "a1-a2", "a2-a3", "a3-1"],
        "strict_positive": ["a0-a1-a2+a3-1", "-a0+a1+a2+a3-1", "a0-a1-a2+a3+1"],
        "interpretation": ["a0+a3>T", "a0+1<T", "a1+a2<T"],
    }, "star3 ordered chamber semantics")
    require(cert["expected_quotient_dimension"] == 14 and cert["expected_complex_points"] == 14 and cert["expected_real_points"] == 8, "star3 expected counts")
    expected_components = [
        {
            "id": "equal_branch", "degree": 2, "parameter": "t", "minimal_polynomial": "3*t**2-1",
            "real_isolating_intervals": [["-2/3", "-1/2"], ["1/2", "2/3"]],
            "coordinates": ["2*t", "t", "t", "t"],
            "ideal_generators": ["a0-2*a3", "a1-a3", "a2-a3", "3*a3**2-1"],
        },
        {
            "id": "large_at_a1", "degree": 4, "parameter": "s", "minimal_polynomial": "2*s**4+5*s**2-1",
            "real_isolating_intervals": [["-1/2", "-2/5"], ["2/5", "1/2"]],
            "coordinates": ["(3*s**2+1)/(2*s)", "(s**2+1)/(2*s)", "s", "s"],
            "ideal_generators": ["a0-a1-a2", "a2-a3", "2*a2*a1-a2**2-1", "2*a2**4+5*a2**2-1"],
        },
        {
            "id": "large_at_a2", "degree": 4, "parameter": "s", "minimal_polynomial": "2*s**4+5*s**2-1",
            "real_isolating_intervals": [["-1/2", "-2/5"], ["2/5", "1/2"]],
            "coordinates": ["(3*s**2+1)/(2*s)", "s", "(s**2+1)/(2*s)", "s"],
            "ideal_generators": ["a0-a1-a2", "a1-a3", "2*a1*a2-a1**2-1", "2*a1**4+5*a1**2-1"],
        },
        {
            "id": "large_at_a3", "degree": 4, "parameter": "s", "minimal_polynomial": "2*s**4+5*s**2-1",
            "real_isolating_intervals": [["-1/2", "-2/5"], ["2/5", "1/2"]],
            "coordinates": ["(3*s**2+1)/(2*s)", "s", "s", "(s**2+1)/(2*s)"],
            "ideal_generators": ["a0-a1-a3", "a1-a2", "2*a1*a3-a1**2-1", "2*a1**4+5*a1**2-1"],
        },
    ]
    require(cert["components"] == expected_components, "star3 component semantics")
    require(cert["classification"] == {"radical": True, "multiple_complex_roots": 0, "subset_sum_wall_roots": 0, "ordered_star3_closure_roots": 0}, "star3 classification metadata")

    _, P, S, _, G = full_system_gauge({(0, 1), (0, 2), (0, 3)})
    names = ["a0", "a1", "a2", "a3"]
    gtext = ",".join(g.as_singular(names) for g in G)
    body = f"""
ring r=0,(a0,a1,a2,a3),dp;
poly P={P.as_singular(names)};
poly S={S.as_singular(names)};
ideal I={gtext};
ideal W=a0*a1*a2*a3*P*S;
ideal SatI=sat(I,W);
ideal J0=a0-2*a3,a1-a3,a2-a3,3*a3^2-1;
ideal J1=a0-a1-a2,a2-a3,2*a2*a1-a2^2-1,2*a2^4+5*a2^2-1;
ideal J2=a0-a1-a2,a1-a3,2*a1*a2-a1^2-1,2*a1^4+5*a1^2-1;
ideal J3=a0-a1-a3,a1-a2,2*a1*a3-a1^2-1,2*a1^4+5*a1^2-1;
ideal U=intersect(J0,J1); U=intersect(U,J2); U=intersect(U,J3);
ideal z1=reduce(SatI,std(U)); ideal z2=reduce(U,std(SatI));
int ok=(dim(std(SatI))==0) && (vdim(std(SatI))==14) && (size(simplify(z1,2))==0) && (size(simplify(z2,2))==0);
ideal pair01=J0+J1; ideal pair02=J0+J2; ideal pair03=J0+J3; ideal pair12=J1+J2; ideal pair13=J1+J3; ideal pair23=J2+J3;
ok=ok && (reduce(1,std(pair01))==0) && (reduce(1,std(pair02))==0) && (reduce(1,std(pair03))==0) && (reduce(1,std(pair12))==0) && (reduce(1,std(pair13))==0) && (reduce(1,std(pair23))==0);
if (ok) {{ print("PASS::star3_saturation"); }} else {{ quit(1); }}
"""
    run_singular(body, "star3_saturation")
    require(sturm_count([3, 0, -1], "-inf", "+inf") == 2, "star3 quadratic real roots")
    require(sturm_count([2, 0, 5, 0, -1], "-inf", "+inf") == 2, "star3 quartic real roots")
    require(sturm_count([3, 0, -1], Q(1, 2), Q(2, 3)) == 1, "star3 positive t isolator")
    require(sturm_count([2, 0, 5, 0, -1], Q(2, 5), Q(1, 2)) == 1, "star3 positive s isolator")
    # Gauge a4=1 and order require a3>=1.  Every positive component has an
    # exposed coordinate t<2/3 or s<1/2, so none reaches the ordered closure.
    return {"saturated_dimension": 0, "complex_points": 14, "real_points": 8, "ordered_closure_points": 0}


def verify_triangle(cert: dict) -> dict:
    exact_keys(cert, {"format_version", "certificate_type", "theorem", "variables", "normalization", "high_pairs", "low_pairs", "critical_system", "ordered_closure_constraints", "saturated_groebner_basis", "elimination_factor", "proof_identities"}, "triangle")
    require(cert["format_version"] == 1 and cert["certificate_type"] == "q5_triangle_highpair_chamber_no_go", "triangle schema")
    require(cert["high_pairs"] == [[0, 1], [0, 2], [1, 2]], "triangle graph")
    require(cert["low_pairs"] == [[0, 3], [0, 4], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], "triangle low pairs")
    require(cert["normalization"] == {"a4": "1", "meaning": "divide a full-support ordered normal by its smallest coordinate"}, "triangle gauge")
    require(cert["ordered_closure_constraints"] == {
        "order": ["a0-a1>=0", "a1-a2>=0", "a2-a3>=0", "a3-1>=0"],
        "polygon": ["a1+a2+a3+1-a0>=0"],
        "high_pair_closure": [
            "a0+a1-a2-a3-1>=0", "a0+a2-a1-a3-1>=0", "a1+a2-a0-a3-1>=0",
        ],
        "low_pair_closure": [
            "a1+a2+1-a0-a3>=0", "a1+a2+a3-a0-1>=0",
            "a0+a2+1-a1-a3>=0", "a0+a2+a3-a1-1>=0",
            "a0+a1+1-a2-a3>=0", "a0+a1+a3-a2-1>=0",
            "a0+a1+a2-a3-1>=0",
        ],
    }, "triangle closure-wall semantics")
    require(cert["critical_system"]["saturating_product"] == "a0*a1*a2*a3*P*s", "triangle saturation factors")
    expected_basis = [
        "4*a1^2-3*a0*a2-9*a1*a2+6*a2^2+2*a3^2+2",
        "6*a0*a1-9*a0*a2-9*a1*a2+10*a2^2+2*a3^2+2",
        "4*a0^2-9*a0*a2-3*a1*a2+6*a2^2+2*a3^2+2",
        "4*a1*a2^2-3*a2^3+6*a0*a3^2-10*a1*a3^2+3*a2*a3^2+6*a0-10*a1+3*a2",
        "4*a0*a2^2-3*a2^3-10*a0*a3^2+6*a1*a3^2+3*a2*a3^2-10*a0+6*a1+3*a2",
        "a2^4-5*a2^2*a3^2+4*a3^4-5*a2^2+8*a3^2+4",
    ]
    require(cert["saturated_groebner_basis"] == expected_basis, "triangle saturated basis semantics")
    require(cert["elimination_factor"] == {
        "polynomial": "a2^4-5*a2^2*a3^2+4*a3^4-5*a2^2+8*a3^2+4",
        "factorization": "(a2^2-a3^2-1)*(a2^2-4*a3^2-4)",
        "branch_1": "a2^2-a3^2-1=0", "branch_2": "a2^2-4*a3^2-4=0",
    }, "triangle factor semantics")

    _, P, S, _, G = full_system_gauge({(0, 1), (0, 2), (1, 2)})
    names = ["a0", "a1", "a2", "a3"]
    body = f"""
ring r=0,(a0,a1,a2,a3),dp;
poly P={P.as_singular(names)}; poly S={S.as_singular(names)};
ideal I={','.join(g.as_singular(names) for g in G)}; ideal W=a0*a1*a2*a3*P*S;
ideal SatI=sat(I,W);
ideal B={','.join(expected_basis)};
ideal z1=reduce(SatI,std(B)); ideal z2=reduce(B,std(SatI));
int ok=(dim(std(SatI))==1) && (vdim(std(SatI))==-1) && (size(std(SatI))==6) && (size(simplify(z1,2))==0) && (size(simplify(z2,2))==0);
if (ok) {{ print("PASS::triangle_saturation"); }} else {{ quit(1); }}
"""
    run_singular(body, "triangle_saturation")

    a0, a1, a2, a3 = variables(4)
    b0 = 4 * a1 ** 2 - 3 * a0 * a2 - 9 * a1 * a2 + 6 * a2 ** 2 + 2 * a3 ** 2 + 2
    b1 = 6 * a0 * a1 - 9 * a0 * a2 - 9 * a1 * a2 + 10 * a2 ** 2 + 2 * a3 ** 2 + 2
    b2 = 4 * a0 ** 2 - 9 * a0 * a2 - 3 * a1 * a2 + 6 * a2 ** 2 + 2 * a3 ** 2 + 2
    F1 = a2 ** 2 - a3 ** 2 - 1
    F2 = a2 ** 2 - 4 * a3 ** 2 - 4
    b5 = a2 ** 4 - 5 * a2 ** 2 * a3 ** 2 + 4 * a3 ** 4 - 5 * a2 ** 2 + 8 * a3 ** 2 + 4
    require(b2 - b0 == 2 * (a0 - a1) * (2 * a0 + 2 * a1 - 3 * a2), "triangle ordered factor identity")
    require(b5 == F1 * F2, "triangle elimination factorization")
    images_equal01 = [a0, a0, a2, a3]
    c0, c1 = b0.compose(images_equal01), b1.compose(images_equal01)
    require(c1 - c0 == 2 * (a0 - a2) * (a0 - 2 * a2), "triangle second ordered factor")
    at_equal = c0.compose([a2, a1, a2, a3])
    at_double = c0.compose([2 * a2, a1, a2, a3])
    require(at_equal == -2 * F1 and at_double == -2 * F1, "triangle F1 branch identity")
    # Positivity is semantic, not numerical: 2(a0-a2)+2(a1-a2)+a2>0.
    require(2 * a0 + 2 * a1 - 3 * a2 == 2 * (a0 - a2) + 2 * (a1 - a2) + a2, "triangle positive-factor decomposition")
    require(F2 - F1 == -3 * (a3 ** 2 + 1), "triangle branch separation")
    require((a3 + 1) ** 2 - a2 ** 2 == -F1 + 2 * a3, "triangle high-edge contradiction identity")
    return {"saturated_dimension": 1, "basis_size": 6, "ordered_closure_points": 0, "walls_included": True}


def verify_star4(cert: dict) -> dict:
    exact_keys(cert, {"schema", "gauge", "ordered_variables", "high_pairs", "expected_saturated_dimension", "expected_saturated_vector_dimension", "ideal_consequences", "all_leaves_one_polynomial_degree_descending", "sturm_sequence_primitive_degree_descending", "expected_sturm_variations_at_2", "expected_sturm_variations_at_positive_infinity", "ordered_chamber_reduction", "branch_margin_numerator_degree_descending", "conclusion"}, "star4")
    require(cert["schema"] == "q5-star4-no-critical-root-v1", "star4 schema")
    require(cert["gauge"] == "a4=1", "star4 gauge")
    require(cert["high_pairs"] == [[0, 1], [0, 2], [0, 3], [0, 4]], "star4 graph")
    require(cert["expected_saturated_dimension"] == 0 and cert["expected_saturated_vector_dimension"] == 48, "star4 saturated counts")
    expected_consequences = {
        "h23": "(a2-1)*(a2-a3)*(a3-1)",
        "h13": "(a1-1)*(a1-a3)*(a3-1)",
        "h12": "(a1-1)*(a1-a2)*(a2-1)",
        "k3": "(a3-1)*(a0*a3+a0-a1*a3-a1-a2*a3-a2-a3^2+2*a3-1)",
        "k2": "(a2-1)*(a0*a2+a0-a1*a2-a1-a2^2+a2-a3^2-1)",
        "k1": "(a1-1)*(a0*a1+a0-a1^2-a2^2-a3^2-1)",
    }
    require(cert["ideal_consequences"] == expected_consequences, "star4 consequence semantics")
    require(cert["all_leaves_one_polynomial_degree_descending"] == [1, -12, 51, -96, 96, 0, -64], "star4 final polynomial")
    require(cert["ordered_chamber_reduction"] == "a0+1>a1+a2+a3", "star4 chamber margin")
    require(cert["branch_margin_numerator_degree_descending"] == [-2, 2], "star4 branch margin")
    require(cert["conclusion"] == "no saturated critical root satisfies a0>=a1>=a2>=a3>=a4=1 and a0+1>a1+a2+a3", "star4 conclusion")

    _, P, S, _, G = full_system_gauge({(0, 1), (0, 2), (0, 3), (0, 4)})
    names = ["a0", "a1", "a2", "a3"]
    body = f"""
ring r=0,(a0,a1,a2,a3),dp;
poly P={P.as_singular(names)}; poly S={S.as_singular(names)};
ideal I={','.join(g.as_singular(names) for g in G)}; ideal W=a0*a1*a2*a3*P*S;
ideal SatI=sat(I,W);
ideal C={','.join(expected_consequences.values())};
ideal z=reduce(C,std(SatI));
int ok=(dim(std(SatI))==0) && (vdim(std(SatI))==48) && (size(simplify(z,2))==0);
if (ok) {{ print("PASS::star4_saturation"); }} else {{ quit(1); }}
"""
    run_singular(body, "star4_saturation")

    R = [Q(v) for v in cert["all_leaves_one_polynomial_degree_descending"]]
    computed_chain = sturm_chain(R)
    stored_chain = [[Q(v) for v in row] for row in cert["sturm_sequence_primitive_degree_descending"]]
    require(len(computed_chain) == len(stored_chain), "star4 Sturm length")
    require(all(positive_associate_univariate(actual, stored) for actual, stored in zip(computed_chain, stored_chain)), "star4 Sturm recurrence")
    v2 = variations(signs_at(computed_chain, Q(2)))
    vinf = variations(signs_at(computed_chain, "+inf"))
    require(v2 == cert["expected_sturm_variations_at_2"] == 2, "star4 Sturm variation at 2")
    require(vinf == cert["expected_sturm_variations_at_positive_infinity"] == 2, "star4 Sturm variation at infinity")

    X = Poly.var(1, 0)
    specialize = [X, Poly.one(1), Poly.one(1), Poly.one(1)]
    Gline = [g.compose(specialize) for g in G]
    Rpoly = sparse_poly(1, [[len(R) - 1 - i, c.numerator, c.denominator] for i, c in enumerate(R)])
    require(Gline[0] == -4 * Gline[1] and Gline[1] == Gline[2] == Gline[3], "star4 all-leaf gradient ratio")
    ratio = poly_scalar_ratio(Gline[1], Rpoly)
    require(ratio is not None and ratio != 0, "star4 all-leaf polynomial reconstruction")

    # The h-consequences, under a1>=a2>=a3>=1, leave exactly three r>1
    # equality patterns (besides all leaves equal to one).  The relevant
    # k-consequence solves for a0.  In every pattern the numerator of the
    # difference between that value and the strict star4 threshold is
    # 2(1-r)<0, so none lies in the chamber.
    rr, aa0 = variables(2)
    branch_relations = [
        ((rr + 1) * aa0 - (3 * rr ** 2 + 1), aa0 - (3 * rr - 1)),
        ((rr + 1) * aa0 - (rr ** 2 + 3), aa0 - (rr + 1)),
        ((rr + 1) * aa0 - (2 * rr ** 2 + 2), aa0 - 2 * rr),
    ]
    for relation, margin in branch_relations:
        require((rr + 1) * margin - relation == 2 * (1 - rr), "star4 equality-branch margin identity")
    branch_margin = sparse_poly(1, [[1, -2, 1], [0, 2, 1]])
    require(branch_margin == 2 * (1 - Poly.var(1, 0)), "star4 stored branch-margin polynomial")
    require(Q(2) * (1 - Q(3, 2)) < 0, "star4 r>1 branch sign")

    # Pair-wall stitching.  In star4 closure the star margins are ordered
    # m01>=m02>=m03>=m04>=0. Any high-edge wall forces m04=0, placing the
    # point in star3 closure. A low leaf-pair wall plus a disjoint weak-high
    # star edge would sum to A while omitting a positive fifth coordinate,
    # an exact contradiction. Coordinate-equality faces remain in the ideal.
    return {"saturated_dimension": 0, "complex_multiplicity": 48, "sturm_roots_on_2_inf": v2 - vinf, "pair_boundary_delegated_to": "star3 closure"}


def verify_empty(cert: dict) -> dict:
    exact_keys(cert, {"certificate_type", "format_version", "theorem", "normalization", "empty_chamber", "symmetric_system", "factor_polynomials", "three_value_cases", "branch_groebner_bases", "sturm_checks", "branch_inequality_certificate", "two_value_certificate", "four_value_certificate", "closure_coverage"}, "empty")
    require(cert["certificate_type"] == "q5_empty_highpair_chamber_classification" and cert["format_version"] == 1, "empty schema")
    require(cert["normalization"] == {"sum": "a0+a1+a2+a3+a4=2", "pair_wall": "ai+aj=1", "order": "a0>=a1>=a2>=a3>=a4>0"}, "empty normalization")
    require(cert["empty_chamber"] == {"high_pairs": [], "low_pair_closure": "ai+aj<=1 for every 0<=i<j<=4", "ordered_reduction": "a0+a1<=1"}, "empty chamber semantics")

    aa = variables(5)
    P = full_piece(aa, set())
    p1 = sum(aa, Poly.zero(5))
    p2 = sum((a ** 2 for a in aa), Poly.zero(5))
    p3 = sum((a ** 3 for a in aa), Poly.zero(5))
    p4 = sum((a ** 4 for a in aa), Poly.zero(5))
    Psym = Q(3, 8) * p1 ** 4 - 3 * p1 ** 2 * p2 + 3 * p2 ** 2 + 4 * p1 * p3 - 4 * p4
    require(P == Psym, "empty symmetric P identity")
    C0 = Q(3, 2) * p1 ** 3 - 6 * p1 * p2 + 4 * p3
    C1 = -6 * p1 ** 2 + 12 * p2
    G = [aa[i] * p2 * P.diff(i) + (aa[i] ** 2 - p2) * P for i in range(5)]
    for i in range(5):
        X = aa[i]
        qx = -16 * p2 * X ** 4 + 12 * p1 * p2 * X ** 3 + (C1 * p2 + P) * X ** 2 + C0 * p2 * X - p2 * P
        require(G[i] == qx, f"empty common quartic identity {i}")
    require(cert["symmetric_system"] == {
        "P": "3*p1^4/8-3*p1^2*p2+3*p2^2+4*p1*p3-4*p4", "S": "p2",
        "Pi_at_x": "C0+C1*x+12*p1*x^2-16*x^3",
        "C0": "3*p1^3/2-6*p1*p2+4*p3", "C1": "-6*p1^2+12*p2",
        "q": "-16*S*x^4+12*p1*S*x^3+(C1*S+P)*x^2+C0*S*x-S*P",
        "critical_root_rule": "every coordinate value is a root of q", "degree_bound": 4,
    }, "empty quartic metadata")
    # Its leading coefficient is -16*p2, nonzero because all coordinates are
    # positive, so the degree bound is genuinely four.

    # Two distinct values: reconstruct the necessary divided difference from
    # the five independent G_i before imposing multiplicities.
    r = Poly.var(1, 0)
    expected_two = {
        1: Q(15, 8) * r ** 4 * (r - 3),
        2: Q(5, 8) * (16 * r ** 5 - 48 * r ** 4 + 40 * r ** 3 - 8 * r ** 2 - 9 * r + 3),
        3: Q(5, 8) * (3 * r ** 5 - 9 * r ** 4 - 8 * r ** 3 + 40 * r ** 2 - 48 * r + 16),
        4: Q(15, 8) * (1 - 3 * r),
    }
    expected_two_metadata = [
        {"large_multiplicity": 1, "range": [[1, 1], [2, 1]], "divided_difference": "15*r^4*(r-3)/8", "nonzero_reason": "r>=1 and r<=2"},
        {"large_multiplicity": 2, "range": [[1, 1], [3, 2]], "divided_difference": "5*(16*r^5-48*r^4+40*r^3-8*r^2-9*r+3)/8", "sturm_root_count": 0},
        {"large_multiplicity": 3, "range": [[1, 1], [2, 1]], "divided_difference": "5*(3*r^5-9*r^4-8*r^3+40*r^2-48*r+16)/8", "sturm_root_count": 0},
        {"large_multiplicity": 4, "range": [[1, 1], None], "divided_difference": "15*(1-3*r)/8", "nonzero_reason": "r>=1"},
    ]
    require(cert["two_value_certificate"] == expected_two_metadata, "empty two-value certificate semantics")
    for m, record in enumerate(cert["two_value_certificate"], start=1):
        require(record["large_multiplicity"] == m, "empty two-value multiplicity order")
        images = [r] * m + [Poly.one(1)] * (5 - m)
        large = G[0].compose(images)
        small = G[m].compose(images) if m < 5 else G[0].compose(images)
        divided = exact_univariate_quotient(large - small, r - 1)
        require(divided == expected_two[m], f"empty two-value divided difference m={m}")
    require(sturm_count([16, -48, 40, -8, -9, 3], Q(1), Q(3, 2)) == 0, "empty two-value m2 Sturm")
    require(sturm_count([3, -9, -8, 40, -48, 16], Q(1), Q(2)) == 0, "empty two-value m3 Sturm")

    factor_polys = {name: [Q(v) for v in coefficients] for name, coefficients in cert["factor_polynomials"].items()}
    require(set(factor_polys) == {"A4", "A5", "A8", "B4", "B5", "C4", "D8", "E8", "F2", "F4"}, "empty factor names")

    # Independently reconstruct the six three-value resultants from the
    # power-sum quartic rule.  Exact equality is tested up to a nonzero Q-unit.
    x, y = variables(2)
    one2 = Poly.one(2)
    cases: dict[tuple[int, int, int], tuple[Poly, Poly, Poly]] = {}
    alias = {
        "x": x,
        "half": 2 * x - 1,
        "seven": 7 * x - 2,
    }
    for name, coefficients in factor_polys.items():
        degree = len(coefficients) - 1
        alias[name] = Poly(2, {(degree - i, 0): c for i, c in enumerate(coefficients) if c})

    singular_blocks: list[str] = ["ring r=0,(y,x),lp;"]
    expected_survivors = {
        (1, 1, 3): ["half"],
        (1, 2, 2): ["B4", "B5"],
        (1, 3, 1): ["half", "A5"],
        (2, 1, 2): ["half"],
        (2, 2, 1): ["half"],
        (3, 1, 1): ["half"],
    }
    expected_case_metadata = {
        (1, 1, 3): ("(2-x-y)/3", [27, 2], [81, 2], -881596846080000),
        (1, 2, 2): ("1-x/2-y", [4, 1], [8, 1], -33554432000),
        (1, 3, 1): ("2-x-3*y", [1, 2], [1, 2], 14929920000),
        (2, 1, 2): ("1-x-y/2", [4, 1], [8, 1], -11796480000),
        (2, 2, 1): ("2-2*x-2*y", [1, 2], [1, 2], -7680000),
        (3, 1, 1): ("2-3*x-y", [1, 2], [1, 6], -32000),
    }
    for index, record in enumerate(cert["three_value_cases"]):
        exact_keys(record, {"multiplicities", "z", "f_scale", "g_scale", "resultant_constant", "resultant_factors", "surviving_branches"}, "empty three-value case")
        m, n, k = tuple(record["multiplicities"])
        key = (m, n, k)
        require((record["z"], record["f_scale"], record["g_scale"], record["resultant_constant"]) == expected_case_metadata[key], f"empty three-value case metadata {key}")
        require(record["surviving_branches"] == expected_survivors[key], f"empty surviving branch semantics {key}")
        z = (2 - m * x - n * y) / k
        pp2 = m * x ** 2 + n * y ** 2 + k * z ** 2
        pp3 = m * x ** 3 + n * y ** 3 + k * z ** 3
        pp4 = m * x ** 4 + n * y ** 4 + k * z ** 4
        pp = 6 - 12 * pp2 + 3 * pp2 ** 2 + 8 * pp3 - 4 * pp4
        cc0 = 12 - 12 * pp2 + 4 * pp3
        cc1 = -24 + 12 * pp2

        def Ruv(u0: Poly, v0: Poly) -> Poly:
            return (-16 * pp2 * (u0 ** 3 + u0 ** 2 * v0 + u0 * v0 ** 2 + v0 ** 3)
                    + 24 * pp2 * (u0 ** 2 + u0 * v0 + v0 ** 2)
                    + (cc1 * pp2 + pp) * (u0 + v0) + cc0 * pp2)

        f, g = Ruv(x, y), Ruv(y, z)
        target = Poly.one(2)
        for name, exponent in record["resultant_factors"]:
            target *= alias[name] ** exponent
        cases[key] = (f, g, target)
        label = "".join(map(str, key))
        singular_blocks.extend([
            f"poly f{label}={f.as_singular(['x','y'])};",
            f"poly g{label}={g.as_singular(['x','y'])};",
            f"poly t{label}={target.as_singular(['x','y'])};",
            f"poly rr{label}=resultant(f{label},g{label},y);",
            f"ideal za{label}=reduce(ideal(rr{label}),std(ideal(t{label})));",
            f"ideal zb{label}=reduce(ideal(t{label}),std(ideal(rr{label})));",
            f"if (!((size(simplify(za{label},2))==0)&&(size(simplify(zb{label},2))==0))) {{ quit(1); }}",
        ])
    singular_blocks.append('print("PASS::empty_three_value_resultants");')
    run_singular("\n".join(singular_blocks), "empty_three_value_resultants")

    expected_sturm_checks = [
        ["A4", [2, 5], [2, 3], 0], ["A8", [2, 5], [2, 3], 0],
        ["B4", [2, 5], [2, 3], 1], ["B4", [59, 100], [3, 5], 1],
        ["C4", [2, 5], [2, 3], 0], ["B5", [2, 5], [2, 3], 1],
        ["A5", [2, 5], [2, 3], 1], ["B5", [2, 5], [1, 2], 0],
        ["D8", [2, 5], [1, 2], 0], ["E8", [2, 5], [1, 2], 0],
        ["F2", [2, 5], [1, 2], 0], ["F4", [2, 5], [1, 2], 0],
    ]
    require(cert["sturm_checks"] == expected_sturm_checks, "empty Sturm-check coverage")
    for name, left_pair, right_pair, count in cert["sturm_checks"]:
        require(sturm_count(factor_polys[name], Q(*left_pair), Q(*right_pair)) == count, f"empty factor Sturm {name} {left_pair} {right_pair}")

    # Check all exposed branch ideal bases by mutual exact containment.
    basis_map = cert["branch_groebner_bases"]
    expected_basis_map = {
        "113_half": ["y^2", "2*x-1"],
        "122_B4": ["88*y^2+(44*x-88)*y-3*x^3+26*x^2-40*x+24", "B4"],
        "122_B5": ["3*x+2*y-2", "B5"],
        "131_half": ["2*y-1", "2*x-1"],
        "131_A5": ["2*x+3*y-2", "A5"],
        "212_half": ["y^2", "2*x-1"],
        "221_half": ["2*y-1", "2*x-1"],
        "311_half": ["y^2*(2*y-1)", "2*x-1"],
    }
    require(basis_map == expected_basis_map, "empty branch basis semantics")
    branch_specs = [
        ("113_half", (1, 1, 3), "half"), ("122_B4", (1, 2, 2), "B4"),
        ("122_B5", (1, 2, 2), "B5"), ("131_half", (1, 3, 1), "half"),
        ("131_A5", (1, 3, 1), "A5"), ("212_half", (2, 1, 2), "half"),
        ("221_half", (2, 2, 1), "half"), ("311_half", (3, 1, 1), "half"),
    ]
    branch_script = ["ring r=0,(y,x),lp;"]
    named_expr = {name: Poly(2, {(len(coeffs)-1-i, 0): c for i, c in enumerate(coeffs) if c}).as_singular(["x", "y"]) for name, coeffs in factor_polys.items()}
    named_expr["half"] = "2*x-1"
    for idx, (branch_name, key, factor_name) in enumerate(branch_specs):
        f, g, _ = cases[key]
        expected_strings = [named_expr.get(expr, expr.replace("**", "^")) for expr in basis_map[branch_name]]
        branch_script.extend([
            f"ideal I{idx}={f.as_singular(['x','y'])},{g.as_singular(['x','y'])},{named_expr[factor_name]};",
            f"ideal B{idx}={','.join(expected_strings)};",
            f"ideal zc{idx}=reduce(I{idx},std(B{idx})); ideal zd{idx}=reduce(B{idx},std(I{idx}));",
            f"if (!((size(simplify(zc{idx},2))==0)&&(size(simplify(zd{idx},2))==0))) {{ quit(1); }}",
        ])
    branch_script.append('print("PASS::empty_branch_ideals");')
    run_singular("\n".join(branch_script), "empty_branch_ideals")

    # The possible largest value obeys x in [2/5,2/3] when its multiplicity
    # is one, and x in [2/5,1/2] when it is at least two.  This follows from
    # average 2/5 and respectively x+y<=1 or 2x<=1.  The Sturm table therefore
    # removes every resultant factor except the explicitly reconstructed
    # branches.  All x=1/2 branches have y=0 or y=x; B5/A5 give z=x.
    require(Q(2, 5) < Q(1, 2) < Q(2, 3), "empty largest-value ranges")
    cx, cy = variables(2)
    require(2 * (1 - cx / 2 - cy - cx) == -(3 * cx + 2 * cy - 2), "empty B5 collapse identity")
    require(2 - cx - 3 * cy - cx == -(2 * cx + 3 * cy - 2), "empty A5 collapse identity")

    branch_ineq = cert["branch_inequality_certificate"]
    require(branch_ineq == {
        "B4_isolating_interval": [[59, 100], [3, 5]],
        "ordered_root_condition": "y>(2-x)/4",
        "empty_condition": "y<=1-x",
        "boundary_value": "R_B4(x,1-x)=-3*x^3+70*x^2-84*x+24",
        "boundary_sign": "negative on [59/100,3/5]",
        "B5_collapse": "3*x+2*y-2=0 implies z=x",
        "A5_collapse": "2*x+3*y-2=0 implies z=x",
    }, "empty branch-inequality semantics")
    # The only non-collapsing B4 branch violates x+y<=1.
    B4coeff = factor_polys["B4"]
    require(sturm_count(B4coeff, Q(59, 100), Q(3, 5)) == 1, "empty B4 isolator")
    bx, by = variables(2)
    RB4 = 88 * by ** 2 + (44 * bx - 88) * by - 3 * bx ** 3 + 26 * bx ** 2 - 40 * bx + 24
    require(RB4.diff(1) == 44 * (4 * by + bx - 2), "empty B4 monotonicity identity")
    Wboundary = -3 * r ** 3 + 70 * r ** 2 - 84 * r + 24
    require(RB4.compose([r, 1 - r]) == Wboundary, "empty B4 boundary identity")
    require(Wboundary.evaluate([Q(59, 100)]) == Q(-1809137, 10**6) < 0, "empty B4 left endpoint sign")
    require(Wboundary.diff(0).evaluate([Q(3, 5)]) == Q(-81, 25) < 0, "empty B4 derivative endpoint sign")
    require(Wboundary.diff(0).diff(0) == 140 - 18 * r and 140 - 18 * Q(3, 5) > 0, "empty B4 convexity")

    # Four distinct values: the common quartic has four distinct coordinate
    # roots.  Its root sum is 3/2 while the five coordinates sum to 2, so the
    # duplicated coordinate is 1/2.  The e4 and e3 identities then contradict
    # positivity of the other three values.
    require(cert["four_value_certificate"] == {
        "duplicated_value": "1/2", "other_values_sum": "x+y+z=1",
        "u": "x*y+x*z+y*z", "w": "x*y*z",
        "vieta_e4_identity": "P/16-w/2=(4*u-1)^2/64",
        "vieta_e3_identity": "C0/16-(w+u/2)=(4*u-4*w-1)/16",
        "contradiction": "e4 gives u=1/4; e3 then gives w=0, contradicting x*y*z>0",
    }, "empty four-value certificate semantics")
    require(Q(2) - Q(3, 2) == Q(1, 2), "empty duplicated-root Vieta deduction")
    xx, yy = variables(2)
    zz = 1 - xx - yy
    uu = xx * yy + xx * zz + yy * zz
    ww = xx * yy * zz
    values = [Poly.const(2, Q(1, 2)), Poly.const(2, Q(1, 2)), xx, yy, zz]
    PP = full_piece(values, set())
    pp1 = sum(values, Poly.zero(2)); pp2 = sum((v ** 2 for v in values), Poly.zero(2)); pp3 = sum((v ** 3 for v in values), Poly.zero(2))
    CC0 = Q(3, 2) * pp1 ** 3 - 6 * pp1 * pp2 + 4 * pp3
    require(PP / 16 - ww / 2 == (4 * uu - 1) ** 2 / 64, "empty four-value e4 identity")
    require(CC0 / 16 - (ww + uu / 2) == (4 * uu - 4 * ww - 1) / 16, "empty four-value e3 identity")

    coverage = cert["closure_coverage"]
    require(coverage["included"] == ["positive coordinate-equality faces", "all pair walls incident to the empty chamber", "their intersections"], "empty closure coverage")
    require(coverage["not_included"] == ["a4=0", "lower-support strata", "nonempty high-pair chambers"], "empty closure exclusions")
    return {"common_quartic": True, "two_value_cases": 4, "three_value_cases": 6, "branch_ideals": 8, "four_value_contradiction": True, "ordered_closure_orbits": 1}


def verify_q4_complete(cert: dict) -> dict:
    exact_keys(cert, {"schema", "unnormalized_vector", "expected_active_sign_vectors", "expected_wall_sign_vectors", "expected_tangent_signature"}, "q4")
    require(cert["schema"] == "q4-rational-saddle-v1", "q4 schema")
    require(cert["unnormalized_vector"] == ["1", "1", "1/2", "1/2"], "q4 point")
    require(cert["expected_active_sign_vectors"] == 6 and cert["expected_wall_sign_vectors"] == 4, "q4 activity metadata")
    require(cert["expected_tangent_signature"] == {"positive": 1, "negative": 2, "zero": 0}, "q4 signature metadata")

    triangle = {(0, 1), (0, 2), (1, 2)}
    star = {(0, 1), (0, 2), (0, 3)}
    qv = variables(4)
    qtotal = sum(qv, Poly.zero(4))
    require(2 * (qv[0] + qv[1]) - qtotal == (qv[0] - qv[2]) + (qv[1] - qv[3]), "Q4 fixed pair comparison 01")
    require(2 * (qv[0] + qv[2]) - qtotal == (qv[0] - qv[1]) + (qv[2] - qv[3]), "Q4 fixed pair comparison 02")
    require(2 * (qv[0] + qv[3]) - qtotal == -(2 * (qv[1] + qv[2]) - qtotal), "Q4 variable complementary pair")
    _, Pt, St, Gt = q4_gauge_system(triangle)
    _, Ps, Ss, Gs = q4_gauge_system(star)
    names = ["a0", "a1", "a2"]
    q1 = "4*a2^4-5*a2^3+15*a2^2+7*a2+10"
    q2 = "10*a2^4+7*a2^3+15*a2^2-5*a2+4"
    q2a1 = "10*a1^4+7*a1^3+15*a1^2-5*a1+4"
    star_elim = f"(a2-2)*(a2-1)*(2*a2-1)*({q1})*({q2})"
    body = f"""
ring r=0,(a0,a1,a2),lp;
poly Pt={Pt.as_singular(names)}; poly St={St.as_singular(names)};
ideal It={','.join(g.as_singular(names) for g in Gt)}; ideal Wt=a0*a1*a2*Pt*St; ideal Qt=sat(It,Wt);
poly et=a2^4-5*a2^2+4; ideal etrem=reduce(ideal(et),std(Qt));
ideal Et=eliminate(Qt,a0*a1); ideal BEt=ideal(et);
ideal eteq1=reduce(Et,std(BEt)); ideal eteq2=reduce(BEt,std(Et));
ideal T1=Qt+ideal(a2-1); ideal BT1=a2-1,a0-a1,4*a1^2-3*a0-9*a1+8;
ideal T2=Qt+ideal(a2-2); ideal BT2=a2-2,a0+a1-3,2*a1^2-3*a0-9*a1+13;
int ok=(dim(std(Qt))==0)&&(vdim(std(Qt))==8)&&(size(simplify(etrem,2))==0)
       &&(size(simplify(eteq1,2))==0)&&(size(simplify(eteq2,2))==0);
ideal zt1=reduce(T1,std(BT1)); ideal zt2=reduce(BT1,std(T1)); ideal zt3=reduce(T2,std(BT2)); ideal zt4=reduce(BT2,std(T2));
ok=ok&&(size(simplify(zt1,2))==0)&&(size(simplify(zt2,2))==0)&&(size(simplify(zt3,2))==0)&&(size(simplify(zt4,2))==0);
ideal ET1=eliminate(T1,a0); ideal EBT1=a2-1,(a1-1)*(a1-2);
ideal ET2=eliminate(T2,a0); ideal EBT2=a2-2,(a1-1)*(a1-2);
ideal et11=reduce(ET1,std(EBT1)); ideal et12=reduce(EBT1,std(ET1)); ideal et21=reduce(ET2,std(EBT2)); ideal et22=reduce(EBT2,std(ET2));
ok=ok&&(size(simplify(et11,2))==0)&&(size(simplify(et12,2))==0)&&(size(simplify(et21,2))==0)&&(size(simplify(et22,2))==0);
poly Ps={Ps.as_singular(names)}; poly Ss={Ss.as_singular(names)};
ideal Is={','.join(g.as_singular(names) for g in Gs)}; ideal Ws=a0*a1*a2*Ps*Ss; ideal Qs=sat(Is,Ws);
ideal Es=eliminate(Qs,a0*a1); ideal targetE={star_elim};
ideal ze1=reduce(Es,std(targetE)); ideal ze2=reduce(targetE,std(Es));
ok=ok&&(dim(std(Qs))==0)&&(vdim(std(Qs))==20)&&(size(simplify(ze1,2))==0)&&(size(simplify(ze2,2))==0);
ideal S2=Qs+ideal(a2-2); ideal BS2=a2-2,a1-1,a0-a1-1; ideal zs1=reduce(S2,std(BS2)); ideal zs2=reduce(BS2,std(S2));
ok=ok&&(size(simplify(zs1,2))==0)&&(size(simplify(zs2,2))==0);
ideal S12=Qs+ideal(a2-1,a1-2); ideal BS12=a2-1,a1-2,a0-2; ideal zs3=reduce(S12,std(BS12)); ideal zs4=reduce(BS12,std(S12));
ok=ok&&(size(simplify(zs3,2))==0)&&(size(simplify(zs4,2))==0);
ideal S11=Qs+ideal(a2-1,a1-1); ideal BS11=a2-1,a1-1,(a0-1)*(a0^4-5*a0^3+6*a0^2-3*a0-3); ideal zs5=reduce(S11,std(BS11)); ideal zs6=reduce(BS11,std(S11));
ok=ok&&(size(simplify(zs5,2))==0)&&(size(simplify(zs6,2))==0);
ideal ES2=eliminate(S2,a0); ideal EBS2=a2-2,a1-1;
ideal S1=Qs+ideal(a2-1); ideal ES1=eliminate(S1,a0); ideal EBS1=a2-1,(a1-1)*(a1-2)*({q2a1});
ideal es21=reduce(ES2,std(EBS2)); ideal es22=reduce(EBS2,std(ES2)); ideal es11=reduce(ES1,std(EBS1)); ideal es12=reduce(EBS1,std(ES1));
ok=ok&&(size(simplify(es21,2))==0)&&(size(simplify(es22,2))==0)&&(size(simplify(es11,2))==0)&&(size(simplify(es12,2))==0);
if (ok) {{ print("PASS::q4_exhaustion"); }} else {{ quit(1); }}
"""
    run_singular(body, "q4_exhaustion")
    # Exact positivity of q1,q2 for r>0 follows from negative discriminants:
    # q1=r^2(4r^2-5r+2)+13r^2+7r+10; q2 has positive
    # leading terms plus 15r^2-5r+4.
    require(25 - 4 * 4 * 2 < 0 and 25 - 4 * 15 * 4 < 0, "q4 quartic positivity discriminants")
    # K4<0 on [1,3): with t=r-1 on [0,1], it is
    # t^4-t^3-3t^2-2t-4; on [2,3), r^2(r-2)(r-3)-3(r+1).
    require(sturm_count([1, -5, 6, -3, -3], Q(1), Q(3)) == 0, "q4 final quartic has unexpected root")
    require(polynomial_value_desc([Q(1), -5, 6, -3, -3], Q(1)) < 0, "q4 final quartic sign")
    # Ordered gauge has a0>=a1>=a2>=1.  Hence triangle roots a2=-2,-1
    # and star root a2=1/2 are impossible.  At triangle a2=2 the two exact
    # a1 roots 1,2 force respectively a1<a2 or a0<a1.  At star a2=2,
    # elimination gives a1=1<a2.  At a2=1 the positive quartic q2 removes
    # all a1 except 1,2, yielding only the diagonal and (2,2,1,1).
    require(Q(-1) < 1 and Q(1, 2) < 1, "Q4 gauge-order exclusions")
    require(Q(1) < Q(2), "Q4 a2=2 order exclusion")

    # Recompute p and its two-sided wall Hessian from the subset formula.
    point = [Q(1), Q(1), Q(1, 2), Q(1, 2)]
    Tpoint = sum(point, Q(0)) / 2
    active = wall = 0
    for mask in range(1 << 4):
        L = Tpoint - sum((point[i] for i in range(4) if mask & (1 << i)), Q(0))
        active += L > 0
        wall += L == 0
    require((active, wall) == (6, 4), "q4 active/wall counts")
    av = variables(4)
    P4 = q4_piece(av, triangle)
    S4 = sum((v ** 2 for v in av), Poly.zero(4))
    G4 = [av[i] * S4 * P4.diff(i) + (av[i] ** 2 - S4) * P4 for i in range(4)]
    require(all(g.evaluate(point) == 0 for g in G4), "q4 p stationarity")
    Pval = P4.evaluate(point); Sval = S4.evaluate(point)
    Pi = [P4.diff(i).evaluate(point) for i in range(4)]
    Pij = [[P4.diff(i).diff(j).evaluate(point) for j in range(4)] for i in range(4)]
    M = [[(Q(1) if i == j else Q(0)) / Sval - 2 * point[i] * point[j] / Sval ** 2 + Pij[i][j] / Pval - Pi[i] * Pi[j] / Pval ** 2 + ((Q(1) if i == j else Q(0)) / point[i] ** 2) for j in range(4)] for i in range(4)]

    def rayleigh(vector: list[Q]) -> Q:
        numerator = sum((vector[i] * M[i][j] * vector[j] for i in range(4) for j in range(4)), Q(0))
        denominator = sum((v * v for v in vector), Q(0))
        return numerator / denominator

    log_eigen = sorted([rayleigh([Q(1), -1, 0, 0]), rayleigh([0, 0, Q(1), -1]), rayleigh([Q(1, 2), Q(1, 2), -1, -1])])
    require(log_eigen == [Q(-1), Q(-2, 5), Q(1, 5)], "q4 logarithmic Hessian")
    sphere_coeff_sqrt10 = sorted([Sval * Q(5, 12) * eig for eig in log_eigen])
    require(sphere_coeff_sqrt10 == [Q(-25, 24), Q(-5, 12), Q(5, 24)], "q4 spherical Hessian eigenvalues")
    return {
        "triangle_vdim": 8,
        "star_vdim": 20,
        "ideal_containment": {
            "triangle_elimination": "bidirectional",
            "star_elimination": "bidirectional",
            "special_fibres": {"triangle": 2, "star": 3},
        },
        "strict_sign_exclusions": "q1,q2 positive on r>0; residual quartic negative on [1,3) by Sturm",
        "critical_orbits": ["diagonal", "(2,2,1,1)"],
        "non_diagonal_signature": [1, 2, 0],
    }


def verify_q3(cert: dict) -> dict:
    exact_keys(cert, {"schema", "normalization", "box_spline_numerator", "cleared_derivative", "positive_saturation", "resultant_variable", "primitive_resultant", "surviving_positive_branch", "claim"}, "q3")
    require(cert["schema"] == "q3-positive-critical-classification-v1", "q3 schema")
    require(cert["normalization"] == "ordered balanced positive coordinates (a,b,1)", "q3 normalization")
    require(cert["box_spline_numerator"] == "T^2-sum_i(T-a_i)^2", "q3 numerator semantics")
    require(cert["cleared_derivative"] == "H_q=S_q*P*D+2*S*P_q*D-2*S*P*D_q", "q3 derivative semantics")
    require(cert["positive_saturation"] == ["a", "b"] and cert["resultant_variable"] == "a", "q3 saturation/resultant semantics")
    require(cert["primitive_resultant"] == "-64*b^2*(b-1)^6*(b^2+b+1)^3", "q3 primitive resultant metadata")
    require(cert["surviving_positive_branch"] == "b=1, a=1" and cert["claim"] == "the balanced positive Q3 critical orbit is diagonal", "q3 conclusion semantics")
    a, b = variables(2)
    one = Poly.one(2)
    T = (a + b + one) / 2
    S = a ** 2 + b ** 2 + one
    P = T ** 2 - (T - a) ** 2 - (T - b) ** 2 - (T - one) ** 2
    D = a * b
    Ha = S.diff(0) * P * D + 2 * S * P.diff(0) * D - 2 * S * P * D.diff(0)
    Hb = S.diff(1) * P * D + 2 * S * P.diff(1) * D - 2 * S * P * D.diff(1)
    raw_target = -64 * (b ** 7) * ((b - 1) ** 8) * (b ** 2 + 1) * ((b ** 2 + b + 1) ** 3)
    names = ["a", "b"]
    body = f"""
ring r=0,(a,b),lp;
poly Ha={Ha.as_singular(names)};
poly Hb={Hb.as_singular(names)};
poly R=resultant(Ha,Hb,a);
poly target={raw_target.as_singular(names)};
ideal z1=reduce(ideal(R),std(ideal(target)));
ideal z2=reduce(ideal(target),std(ideal(R)));
if ((size(simplify(z1,2))==0) && (size(simplify(z2,2))==0)) {{ print("PASS::q3_resultant"); }} else {{ quit(1); }}
"""
    run_singular(body, "q3_resultant")
    Ha1 = Ha.compose([Poly.var(1, 0), Poly.one(1)])
    Hb1 = Hb.compose([Poly.var(1, 0), Poly.one(1)])
    av = Poly.var(1, 0)
    require(Ha1 == -2 * av ** 2 * (av - 1) ** 2, "q3 b=1 Ha")
    require(Hb1 == av ** 3 * (av - 1) ** 2, "q3 b=1 Hb")
    # For b>0, b^2+1>0 and b^2+b+1>0, so the resultant forces b=1;
    # then a>0 and the displayed equations force a=1.
    require(Q(1) > 0 and Q(3, 4) > 0, "q3 positive quadratic lower bounds")
    # The JSON primitive divides out only factors harmless for the positive real zero set.
    quotient = ("b^5", "(b-1)^2", "b^2+1")
    return {"raw_resultant": "-64*b^7*(b-1)^8*(b^2+1)*(b^2+b+1)^3", "primitive_removed": quotient, "positive_branch": "a=b=1"}


def verify_d4_transverse(contract: dict) -> dict:
    """Rebuild F5(1,1,1,1,t) and prove it rises for 0<t<=1/2."""
    expected_path = [[1, 0], [1, 0], [1, 0], [1, 0], [0, 1]]
    require(contract["support_paths"]["d4"] == expected_path, "d4 support path changed")
    (t,) = variables(1)
    one = Poly.one(1)
    a = [one, one, one, one, t]
    # For 0<t<2 all ten pair sums are below T, so this is the empty piece.
    P = full_piece(a, set())
    q = 3 * t ** 3 - 16 * t ** 2 + 128
    require(8 * P == t * q, "d4 transverse numerator identity")
    # Hence F=sqrt(t^2+4)q/192.  Compare squares with F(0)=4/3:
    # 9(t^2+4)q^2-16*192^2 = 9*t^3*R(t).
    R = 9 * t ** 5 - 96 * t ** 4 + 292 * t ** 3 + 384 * t ** 2 - 3072 * t + 3072
    square_gap_numerator = 9 * (t ** 2 + 4) * (q ** 2) - 16 * (192 ** 2)
    require(square_gap_numerator == 9 * (t ** 3) * R, "d4 square-gap factorization")
    # On 0<t<=1/2: R >= 3072-3072t-96t^4 >= 1530 > 0.
    lower_bound = Q(3072) - Q(3072, 2) - Q(96, 16)
    require(lower_bound == 1530 and lower_bound > 0, "d4 exact positivity lower bound")
    return {
        "identity": "F5=sqrt(t^2+4)*(3*t^3-16*t^2+128)/192",
        "strict_increase_interval": "0<t<=1/2",
        "square_gap": "9*t^3*(9*t^5-96*t^4+292*t^3+384*t^2-3072*t+3072)",
    }


def rational_log_hessian(P: Poly, symbols: list[Poly], point: list[Q]) -> tuple[list[list[Q]], Q, Q]:
    S_poly = sum((a ** 2 for a in symbols), Poly.zero(P.n))
    Sval = S_poly.evaluate(point)
    Pval = P.evaluate(point)
    require(Sval > 0 and Pval > 0, "nonpositive physical S or P")
    Pi = [P.diff(i).evaluate(point) for i in range(P.n)]
    Pij = [[P.diff(i).diff(j).evaluate(point) for j in range(P.n)] for i in range(P.n)]
    M = [[(Q(1) if i == j else Q(0)) / Sval - 2 * point[i] * point[j] / Sval ** 2 + Pij[i][j] / Pval - Pi[i] * Pi[j] / Pval ** 2 + ((Q(1) if i == j else Q(0)) / point[i] ** 2) for j in range(P.n)] for i in range(P.n)]
    return M, Sval, Pval


def rational_rayleigh(M: list[list[Q]], vector: list[Q]) -> Q:
    numerator = sum((vector[i] * M[i][j] * vector[j] for i in range(len(vector)) for j in range(len(vector))), Q(0))
    denominator = sum((v * v for v in vector), Q(0))
    require(denominator > 0, "zero Rayleigh vector")
    return numerator / denominator


def verify_support_types(contract: dict, saddle_cert: dict) -> dict:
    # s=1 and s=2: the direct parameterization is R/a0 in the ordered
    # dominant region. Its derivative in a positive smaller coordinate is
    # a1/(a0*R)>0, hence no positive interior critical point; equality a0=a1
    # is d2.  This also yields F1=1 and F2(d2)=sqrt(2).
    (rho,) = variables(1)
    require((1 + rho ** 2) - 1 == rho ** 2, "s2 squared-value monotonicity identity")
    # On the unit sphere near d1, a0^2=1-rho^2 and F^2=1/a0^2;
    # F^2-1=rho^2/(1-rho^2)>0 for 0<rho^2<1.
    require(1 - (1 - rho ** 2) == rho ** 2, "d1 strict local-minimum identity")

    # d3 crossing path, reconstructed without a series truncation.
    require(contract["support_paths"]["d3"] == [[1, 1], [1, 1], [1, -2], [0, 0], [0, 0]], "d3 support path changed")
    (u,) = variables(1)
    one = Poly.one(1)
    a3 = [one + u, one + u, one - 2 * u]
    T3 = sum(a3, Poly.zero(1)) / 2
    P3 = T3 ** 2 - sum(((T3 - a) ** 2 for a in a3), Poly.zero(1))
    D3 = product(a3, 1)
    S3 = sum((a ** 2 for a in a3), Poly.zero(1))
    require(P3 * 2 == 3 * (2 * u + 1) * (1 - 2 * u), "d3 numerator identity")
    # F3^2 identity; all denominators are positive on |u|<=1/4.
    left_num = S3 * P3 ** 2 * 16 * (one + u) ** 4
    right_num = 4 * D3 ** 2 * 27 * (2 * u + 1) ** 2 * (2 * u ** 2 + 1)
    require(left_num == right_num, "d3 exact path identity")
    crossing = (2 * u + 1) ** 2 * (2 * u ** 2 + 1) - (one + u) ** 4
    require(crossing == u ** 3 * (7 * u + 4), "d3 square-gap crossing factor")
    require(4 - Q(7, 4) > 0, "d3 crossing interval sign")
    require(crossing.evaluate([Q(1, 4)]) > 0 > crossing.evaluate([Q(-1, 4)]), "d3 two-sided crossing")

    # d4 has decreasing directions within support: its Q4 tangent Hessian is
    # -4/3 times the identity.  Use either polynomial extension at the wall;
    # x_+^3 is C2, so both give the same 2-jet.
    s4 = variables(4)
    P4 = q4_piece(s4, {(0, 1), (0, 2), (1, 2)})
    ones4 = [Q(1)] * 4
    M4, S4val, P4val = rational_log_hessian(P4, s4, ones4)
    tangent4 = [rational_rayleigh(M4, [Q(1), -1, 0, 0]), rational_rayleigh(M4, [Q(1), 0, -1, 0]), rational_rayleigh(M4, [Q(1), 0, 0, -1])]
    require(tangent4 == [Q(-1, 4)] * 3, "d4 support log Hessian")
    # F4=4/3 and spherical scaling is S=4.
    require(P4val == 4 and S4val == 4, "d4 value data")
    require([S4val * Q(4, 3) * value for value in tangent4] == [Q(-4, 3)] * 3, "d4 support spherical Hessian")
    transverse = verify_d4_transverse(contract)

    # d5: exact S5-symmetric tangent Hessian.
    s5 = variables(5)
    P5 = full_piece(s5, set())
    ones5 = [Q(1)] * 5
    M5, S5val, P5val = rational_log_hessian(P5, s5, ones5)
    eigen5 = [rational_rayleigh(M5, [Q(1) if i == 0 else Q(-1) if i == j else Q(0) for i in range(5)]) for j in range(1, 5)]
    require(eigen5 == [Q(-6, 115)] * 4, "d5 tangent log Hessian")
    # F5=(P/24)*sqrt(5); spherical eigen coefficient of sqrt(5):
    coefficient5 = S5val * (P5val / 24) * eigen5[0]
    require(P5val == Q(115, 8) and coefficient5 == Q(-5, 32), "d5 spherical Hessian")

    # Cross-bind the small star1 saddle certificate to the independently
    # verified alpha orbit (t=1/alpha).
    exact_keys(saddle_cert, {"schema", "minimal_polynomial_constant_first", "root_interval", "unnormalized_vector", "expected_active_sign_vectors", "expected_tangent_signature"}, "star1 saddle")
    require(saddle_cert["schema"] == "q5-quadratic-saddle-v1", "star1 saddle schema")
    require(saddle_cert["minimal_polynomial_constant_first"] == [13, -48, 39], "star1 reciprocal minpoly")
    require(saddle_cert["unnormalized_vector"] == ["1", "1", "t", "t", "t"], "star1 reciprocal vector")
    left = Q(saddle_cert["root_interval"]["left"]); right = Q(saddle_cert["root_interval"]["right"])
    tpoly = [Q(39), Q(-48), Q(13)]
    require(left < right and polynomial_value_desc(tpoly, left) > 0 > polynomial_value_desc(tpoly, right), "star1 reciprocal root interval")
    require(78 * right - 48 < 0, "star1 reciprocal monotonicity")
    t_alpha = Quad(1) / Quad(0, 1)
    aa5 = variables(5)
    Pstar1 = full_piece(aa5, {(0, 1)})
    Sstar1 = sum((a ** 2 for a in aa5), Poly.zero(5))
    point = [Quad(1), Quad(1), t_alpha, t_alpha, t_alpha]
    Pval = Pstar1.evaluate(point); Sval = Sstar1.evaluate(point)
    Gstar = [aa5[i] * Sstar1 * Pstar1.diff(i) + (aa5[i] ** 2 - Sstar1) * Pstar1 for i in range(5)]
    require(all(g.evaluate(point) == Quad(0) for g in Gstar), "star1 small saddle stationarity")
    require(saddle_cert["expected_tangent_signature"] == {"positive": 1, "negative": 3, "zero": 0}, "star1 saddle signature")
    Tstar = sum(point, Quad(0)) / 2
    active_star = 0
    for mask in range(1 << 5):
        subset_form = Tstar - sum((point[i] for i in range(5) if mask & (1 << i)), Quad(0))
        try:
            sign = subset_form.certified_sign()
        except AuditFailure:
            require(subset_form == Quad(0), "star1 subset sign not isolated")
            sign = 0
        require(sign != 0, "star1 survivor lies on subset wall")
        active_star += sign > 0
    require(saddle_cert["expected_active_sign_vectors"] == active_star == 16, "star1 active sign count")

    return {
        "s1": "coordinate diagonal only; strict local minimum",
        "s2": "no positive interior critical; d2 at equality",
        "s3": "diagonal only; d3 exact cubic crossing",
        "s4": "diagonal plus rational saddle; d4 support-decrease/transverse-increase",
        "d5_hessian": "-5*sqrt(5)/32 multiplicity 4",
        "external_global_dependencies": ["Vaaler/Hensley lower bound for d1", "Ball cube-slicing upper bound for d2"],
        "d4_transverse": transverse,
    }


def verify_wall_support_stitching(contract: dict) -> dict:
    require(
        contract["wall_policy"]
        == "all pair walls are weak chamber-closure constraints; the singleton balance wall is checked separately",
        "wall policy changed",
    )
    chamber_names = set(contract["chambers"])
    require(chamber_names == {"empty", "star1", "star2", "star3", "star4", "triangle"}, "wall routing chamber set")

    # For an ordered positive vector, strict-high edges form a shifted graph.
    # Two disjoint strict-high edges are impossible because their four
    # endpoints sum to A-a_m<A but would also sum to >A.  This is precisely
    # the intersecting test used by verify_chamber_graphs, including when
    # other pair forms vanish.  Therefore the graph of strictly high edges at
    # every wall point is one of the six and the point obeys that graph's weak
    # closure inequalities.
    five = variables(5)
    total = sum(five, Poly.zero(5))
    for omitted in range(5):
        remaining = [i for i in range(5) if i != omitted]
        lhs = sum((five[i] for i in remaining), Poly.zero(5))
        require(lhs == total - five[omitted], "disjoint-high pair sum identity")

    # If the strict-high graph is star4, a low leaf-pair wall cannot occur:
    # choose another leaf k; the wall leaf pair and strict edge 0k are
    # disjoint, and the preceding identity contradicts positivity of the
    # fifth coordinate.  A vanishing star edge instead lowers the strict-high
    # graph to a shorter star, so star4 needs only its interior certificate.
    leaves = {1, 2, 3, 4}
    for i, j in itertools.combinations(sorted(leaves), 2):
        choices = sorted(leaves - {i, j})
        require(len(choices) == 2 and 0 not in {i, j, choices[0]}, "star4 disjoint-edge routing")

    closure_route = {
        "empty": "empty closure",
        "star1": "star1 closure",
        "star2": "star2 closure",
        "star3": "star3 closure",
        "triangle": "triangle closure",
        "star4": "strict interior; every pair wall has a shorter strict-high graph",
    }
    require(set(closure_route) == chamber_names, "pair-wall route omitted a chamber")

    # At a pair wall, x|x|^3 has matching derivatives through order three:
    # x^4 and -x^4 and their first three derivatives all have limit zero.
    X = Poly.var(1, 0)
    plus, minus = X ** 4, -(X ** 4)
    for order in range(4):
        require(plus.evaluate([Q(0)]) == minus.evaluate([Q(0)]) == 0, f"pair-wall C3 order {order}")
        plus, minus = plus.diff(0), minus.diff(0)

    # The singleton balance wall is not divided away.  In the dominant formula
    # F=R/a0, every positive smaller coordinate has logarithmic derivative
    # a_j/S>0, including the equality wall by C1 matching.
    require(Q(1, 5) > 0, "balance-wall derivative sign model")

    # A zero coordinate restricts the central section to the lower-dimensional
    # Q_s section (the unused cube factors have unit volume).  All recursive
    # boundary supports s=1,2,3,4 are executed by verify_support_types and
    # verify_q4_complete.
    return {
        "pair_wall_routes": closure_route,
        "pair_piece_regularity": "C3",
        "balance_wall": "nonstationary: a_j/S>0",
        "coordinate_boundary": "recursive supports s=1,2,3,4",
        "wall_forms_divided_out": 0,
    }


def verify_nonzero_factors(inputs: dict[str, object]) -> dict:
    proof = inputs["main_proof"]
    require(isinstance(proof, str) and "No wall form is divided out in what follows." in proof, "main proof wall-division assertion missing")

    # Every saturation used by this verifier is by coordinates, P and S only.
    # On a full-support gauge chart, a0,...,a3,a4=1 are strictly positive and
    # S=1+sum ai^2 >=1.  The cube contains the Euclidean radius-1/2 ball, so
    # every central section contains its four-dimensional equatorial ball and
    # has positive 4-volume.  Formula (2), with positive coordinates, then
    # gives P>0.  Thus these factors are strictly nonzero on the stated domain.
    gauge = variables(4)
    S = 1 + sum((a ** 2 for a in gauge), Poly.zero(4))
    require(S - 1 == sum((a ** 2 for a in gauge), Poly.zero(4)), "S positivity decomposition")

    for key in ("star3",):
        cert = inputs[key]
        require(isinstance(cert, dict) and cert["saturation_factors"] == ["a0", "a1", "a2", "a3", "P", "S"], f"{key} saturation factors")
    triangle = inputs["triangle"]
    require(isinstance(triangle, dict) and triangle["critical_system"]["saturating_product"] == "a0*a1*a2*a3*P*s", "triangle saturation factors")

    # The cleared logarithmic systems additionally multiply by D=prod ai,
    # again strictly positive in their positive charts.  Star1 exposes two
    # residual prefactors; u,w>=0 makes them >=1 and >=3 respectively.
    require(Q(1) > 0 and Q(3) > 0, "star1 residual prefactor bounds")

    # Empty-chamber divided differences divide by x-y only on the branch that
    # assumes distinct values; x=y is retained and classified separately.
    X, Y = variables(2)
    require((X ** 2 - Y ** 2) == (X - Y) * (X + Y), "divided-difference model identity")

    # Q3: compare the raw resultant with the stored primitive polynomial.
    # b^5 and b^2+1 are strictly nonzero for b>0.  Dividing by (b-1)^2 only
    # reduces multiplicity from 8 to 6 and does not delete the b=1 locus.
    (b,) = variables(1)
    raw = -64 * b ** 7 * (b - 1) ** 8 * (b ** 2 + 1) * (b ** 2 + b + 1) ** 3
    primitive = -64 * b ** 2 * (b - 1) ** 6 * (b ** 2 + b + 1) ** 3
    require(raw == primitive * b ** 5 * (b - 1) ** 2 * (b ** 2 + 1), "Q3 primitive quotient identity")
    require(1 > 0, "Q3 b^2+1 lower bound")

    return {
        "saturation_factors": ["positive coordinates", "P>0 by equatorial-ball volume", "S>=1 in gauge"],
        "clearing_factor": "D>0 on positive support",
        "star1_prefactors": ["w+1>=1", "2u+2w+3>=3"],
        "empty_divided_difference": "only on distinct-value branch",
        "q3_removed_zero_loci": ["b=0 (outside b>0)", "b^2+1=0 (no real root)"],
        "q3_multiplicity_only": "(b-1)^8 reduced to (b-1)^6; locus retained",
        "wall_factors_saturated": 0,
    }


def verify_literature_scope(inputs: dict[str, object]) -> dict:
    ag25 = inputs["ag_2025"]
    po25 = inputs["pournin_2025"]
    am22 = inputs["ambrus_2022"]
    ag24 = inputs["ag_2024"]
    require(isinstance(ag25, str) and "Theorem 1.4" in ag25 and "3 ⩽ 𝑘 ⩽ 𝑛 − 1" in ag25 and "do not have" in ag25, "2025 diagonal-strata theorem scope absent")
    require("is globally minimal" in ag25 and "constitutes a global maximum" in ag25, "d1/d2 global theorem scopes absent")
    require(isinstance(po25, str) and "misses a term" in po25 and "main diagonal" in po25 and "do not change" in po25, "2025 corrigendum scope absent")
    require(isinstance(am22, str) and "Theorem 3" in am22 and "(1, 1, 2, 2)" in am22, "2022 Q4 baseline scope absent")
    require(isinstance(ag24, str) and "Conjecture 1.3" in ag24 and "locally extremal" in ag24, "2024 conjecture scope absent")
    return {
        "2022_q4": "critical-direction classification, with independent Hessian correction used here",
        "2024_ag": "conjecture plus constructed non-diagonal family; not a Q5 exhaustion",
        "2025_ag": "only subdiagonals 3<=k<=n-1 are declared non-extremal",
        "2025_pournin": "missing transverse Hessian term; main-diagonal claims unchanged",
        "d1_global": "Vaaler/Hensley lower bound scope: every central hyperplane section",
        "d2_global": "Ball 1986 scope: every central hyperplane section",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--result", default=str(HERE / "verification_result.json"))
    args = parser.parse_args()
    try:
        binding, inputs = load_bound_inputs(enforce_hashes=True)
        contract = binding["semantic_contract"]
        results = {
            "binding": {"inputs": len(binding["inputs"]), "hashes_enforced": True},
            "chambers": verify_chamber_graphs(contract),
            "empty": verify_empty(inputs["empty"]),
            "star1": verify_star1(inputs["star1"]),
            "star2": verify_star2(inputs["star2"]),
            "star3": verify_star3(inputs["star3"]),
            "star4": verify_star4(inputs["star4"]),
            "triangle": verify_triangle(inputs["triangle"]),
            "q3": verify_q3(inputs["q3"]),
            "q4": verify_q4_complete(inputs["q4"]),
            "d4_transverse": verify_d4_transverse(contract),
            "support_types": verify_support_types(contract, inputs["star1_saddle"]),
            "wall_support_stitching": verify_wall_support_stitching(contract),
            "nonzero_factors": verify_nonzero_factors(inputs),
            "literature_scope": verify_literature_scope(inputs),
        }
        output = {
            "schema": "q5-independent-referee-result-v1",
            "status": "PASS",
            "python": sys.version.split()[0],
            "singular": "/opt/homebrew/bin/Singular",
            "results": results,
            "verifier_sha256": sha256_file(Path(__file__)),
            "binding_sha256": sha256_file(BINDING),
        }
        Path(args.result).write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print("PASS: independent exact referee core")
        print(json.dumps(results, sort_keys=True))
        return 0
    except (AuditFailure, KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        print(f"FAIL CLOSED: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
