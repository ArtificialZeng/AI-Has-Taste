#!/usr/bin/env python3
"""Independent exact finite model for R_n^(1,2).

This module deliberately does not import any discovery code from the project.
It implements

    C_n = Q[x_1,...,x_n]/(e_1,...,e_n) tensor Exterior(theta,xi)

in the Artin monomial basis, the diagonal S_n action, Reynolds images, and
the Lentfer candidate monomials.  A prime-field mode is included only for
discovery/performance measurements; rational mode is the certification mode.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations, product
from math import factorial
from typing import Dict, Iterable, Iterator, List, Mapping, MutableMapping, Sequence, Tuple

try:
    from gmpy2 import mpq as _Rational
except ImportError:  # correctness-preserving fallback
    _Rational = Fraction

Exponent = Tuple[int, ...]
Monomial = Tuple[Exponent, int, int]  # polynomial exponent, theta mask, xi mask
SparseVector = Dict[int, object]
Block = Tuple[int, int, int]


def weak_compositions(total: int, length: int) -> Iterator[Tuple[int, ...]]:
    if length == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in weak_compositions(total - first, length - 1):
            yield (first,) + tail


def inversion_parity(values: Sequence[int]) -> int:
    return sum(values[i] > values[j] for i in range(len(values)) for j in range(i + 1, len(values))) & 1


def masks_of_weight(n: int, weight: int) -> List[int]:
    ans: List[int] = []
    for subset in combinations(range(n), weight):
        mask = 0
        for i in subset:
            mask |= 1 << i
        ans.append(mask)
    return ans


@dataclass(frozen=True)
class Field:
    prime: int | None = None

    def normalize(self, value: object) -> object:
        if self.prime is None:
            return value if isinstance(value, _Rational) else _Rational(value)
        return int(value) % self.prime

    def inv(self, value: object) -> object:
        if self.prime is None:
            return 1 / self.normalize(value)
        return pow(int(value) % self.prime, -1, self.prime)

    def is_zero(self, value: object) -> bool:
        return self.normalize(value) == 0

    def add(self, left: object, right: object) -> object:
        return self.normalize(self.normalize(left) + self.normalize(right))

    def mul(self, left: object, right: object) -> object:
        return self.normalize(self.normalize(left) * self.normalize(right))


class SparseReducer:
    """Incremental reduced row echelon basis over Q or F_p."""

    def __init__(self, field: Field):
        self.field = field
        self.rows: Dict[int, SparseVector] = {}

    def _clean(self, vec: MutableMapping[int, object]) -> SparseVector:
        return {i: self.field.normalize(c) for i, c in vec.items() if not self.field.is_zero(c)}

    def reduce(self, vector: Mapping[int, object]) -> SparseVector:
        vec: SparseVector = self._clean(dict(vector))
        while vec:
            pivot = min(vec)
            row = self.rows.get(pivot)
            if row is None:
                break
            scale = vec[pivot]  # stored pivot is one
            for col, coeff in row.items():
                value = self.field.add(vec.get(col, 0), -self.field.mul(scale, coeff))
                if self.field.is_zero(value):
                    vec.pop(col, None)
                else:
                    vec[col] = value
        return vec

    def add(self, vector: Mapping[int, object]) -> bool:
        vec = self.reduce(vector)
        if not vec:
            return False
        pivot = min(vec)
        inv = self.field.inv(vec[pivot])
        vec = self._clean({i: self.field.mul(c, inv) for i, c in vec.items()})
        # Clear the new pivot from old rows, retaining RREF.  This makes the
        # stored rows deterministic and reduces multiplication fill-in.
        for old_pivot, row in list(self.rows.items()):
            if pivot not in row:
                continue
            scale = row[pivot]
            updated = dict(row)
            for col, coeff in vec.items():
                value = self.field.add(updated.get(col, 0), -self.field.mul(scale, coeff))
                if self.field.is_zero(value):
                    updated.pop(col, None)
                else:
                    updated[col] = value
            self.rows[old_pivot] = updated
        self.rows[pivot] = vec
        return True

    @property
    def rank(self) -> int:
        return len(self.rows)

    def basis(self) -> List[SparseVector]:
        return [self.rows[p] for p in sorted(self.rows)]


class CoinvariantModel:
    def __init__(self, n: int):
        if n < 1:
            raise ValueError("n must be positive")
        self.n = n
        self.top_x_degree = n * (n - 1) // 2
        self.perms = list(permutations(range(n)))
        self.poly_basis = list(product(*(range(i + 1) for i in range(n))))
        self.poly_by_degree: Dict[int, List[Exponent]] = {
            d: [] for d in range(self.top_x_degree + 1)
        }
        for exponent in self.poly_basis:
            self.poly_by_degree[sum(exponent)].append(exponent)
        self.masks_by_weight = {w: masks_of_weight(n, w) for w in range(n + 1)}
        self._replacement = self._make_replacements()
        self._blocks: Dict[Block, List[Monomial]] = {}
        self._indices: Dict[Block, Dict[Monomial, int]] = {}

    def _make_replacements(self) -> Dict[int, List[Exponent]]:
        """Tail terms in h_{i+1}(x_{i+1},...,x_n), zero-based i.

        Under lex x_1 > ... > x_n these form the monic Groebner basis with
        leading monomials x_{i+1}^{i+1}.  Entries returned include their full
        n-variable exponent tuples and exclude the leading monomial.
        """
        ans: Dict[int, List[Exponent]] = {}
        for i in range(self.n):
            degree = i + 1
            terms: List[Exponent] = []
            for comp in weak_compositions(degree, self.n - i):
                if comp[0] == degree:
                    continue
                terms.append((0,) * i + comp)
            ans[i] = terms
        return ans

    @lru_cache(maxsize=None)
    def reduce_polynomial_monomial(self, exponent: Exponent) -> Dict[Exponent, int]:
        """Normal form modulo (e_1,...,e_n), in the Artin basis."""
        for i, value in enumerate(exponent):
            degree = i + 1
            if value < degree:
                continue
            base = list(exponent)
            base[i] -= degree
            out: Dict[Exponent, int] = {}
            for tail in self._replacement[i]:
                child = tuple(base[j] + tail[j] for j in range(self.n))
                for term, coeff in self.reduce_polynomial_monomial(child).items():
                    out[term] = out.get(term, 0) - coeff
                    if out[term] == 0:
                        del out[term]
            return out
        return {exponent: 1}

    def block_basis(self, block: Block) -> List[Monomial]:
        if block not in self._blocks:
            d, t, s = block
            mons = [
                (exponent, theta, xi)
                for exponent in self.poly_by_degree.get(d, [])
                for theta in self.masks_by_weight.get(t, [])
                for xi in self.masks_by_weight.get(s, [])
            ]
            self._blocks[block] = mons
            self._indices[block] = {mon: i for i, mon in enumerate(mons)}
        return self._blocks[block]

    def block_index(self, block: Block) -> Dict[Monomial, int]:
        self.block_basis(block)
        return self._indices[block]

    def all_blocks(self) -> Iterator[Block]:
        for total in range(self.top_x_degree + 2 * self.n + 1):
            for d in range(self.top_x_degree + 1):
                for t in range(self.n + 1):
                    s = total - d - t
                    if 0 <= s <= self.n:
                        yield (d, t, s)

    @staticmethod
    def exterior_product(theta_a: int, xi_a: int, theta_b: int, xi_b: int) -> Tuple[int, int, int] | None:
        if theta_a & theta_b or xi_a & xi_b:
            return None
        # theta_a xi_a theta_b xi_b -> theta_(a union b) xi_(a union b)
        crossings = xi_a.bit_count() * theta_b.bit_count()
        crossings += sum(
            1
            for i in range(max(theta_a.bit_length(), theta_b.bit_length()))
            if (theta_a >> i) & 1
            for j in range(i)
            if (theta_b >> j) & 1
        )
        crossings += sum(
            1
            for i in range(max(xi_a.bit_length(), xi_b.bit_length()))
            if (xi_a >> i) & 1
            for j in range(i)
            if (xi_b >> j) & 1
        )
        return (-1 if crossings & 1 else 1, theta_a | theta_b, xi_a | xi_b)

    def multiply_monomials(self, left: Monomial, right: Monomial) -> Dict[Monomial, int]:
        exterior = self.exterior_product(left[1], left[2], right[1], right[2])
        if exterior is None:
            return {}
        sign, theta, xi = exterior
        exponent = tuple(a + b for a, b in zip(left[0], right[0]))
        return {(term, theta, xi): sign * coeff for term, coeff in self.reduce_polynomial_monomial(exponent).items()}

    @lru_cache(maxsize=None)
    def permute_polynomial(self, exponent: Exponent, perm: Tuple[int, ...]) -> Dict[Exponent, int]:
        image = [0] * self.n
        for i, power in enumerate(exponent):
            image[perm[i]] = power
        return self.reduce_polynomial_monomial(tuple(image))

    def permute_mask(self, mask: int, perm: Tuple[int, ...]) -> Tuple[int, int]:
        selected = [i for i in range(self.n) if (mask >> i) & 1]
        images = [perm[i] for i in selected]
        sign = -1 if inversion_parity(images) else 1
        out = 0
        for i in images:
            out |= 1 << i
        return sign, out

    def reynolds(self, monomial: Monomial, block: Block, field: Field) -> SparseVector:
        index = self.block_index(block)
        out: SparseVector = {}
        for perm in self.perms:
            sign_t, theta = self.permute_mask(monomial[1], perm)
            sign_s, xi = self.permute_mask(monomial[2], perm)
            for exponent, coeff in self.permute_polynomial(monomial[0], perm).items():
                col = index[(exponent, theta, xi)]
                out[col] = field.add(out.get(col, 0), sign_t * sign_s * coeff)
                if field.is_zero(out[col]):
                    del out[col]
        return out

    def invariant_basis(self, block: Block, field: Field) -> List[SparseVector]:
        reducer = SparseReducer(field)
        for monomial in self.block_basis(block):
            reducer.add(self.reynolds(monomial, block, field))
        return reducer.basis()

    def multiply_vector_by_monomial(
        self,
        vector: Mapping[int, object],
        source_block: Block,
        multiplier: Monomial,
        target_block: Block,
        field: Field,
    ) -> SparseVector:
        source = self.block_basis(source_block)
        target_index = self.block_index(target_block)
        out: SparseVector = {}
        for col, scalar in vector.items():
            for product_monomial, coeff in self.multiply_monomials(multiplier, source[col]).items():
                target_col = target_index[product_monomial]
                out[target_col] = field.add(out.get(target_col, 0), field.mul(scalar, coeff))
                if field.is_zero(out[target_col]):
                    del out[target_col]
        return out

    def candidate_monomials(self) -> List[Monomial]:
        out: List[Monomial] = []
        # The first step is forced up, hence bit zero is absent from T and S.
        for theta in range(1 << self.n):
            if theta & 1:
                continue
            for xi in range(1 << self.n):
                if xi & 1:
                    continue
                alpha = [0]
                valid = True
                for i in range(1, self.n):
                    value = alpha[-1] + 1 - ((theta >> i) & 1) - ((xi >> i) & 1)
                    alpha.append(value)
                    if value < 0:
                        valid = False
                        break
                if not valid:
                    continue
                for exponent in product(*(range(value + 1) for value in alpha)):
                    out.append((tuple(exponent), theta, xi))
        return out

    def candidates_by_block(self) -> Dict[Block, List[Monomial]]:
        out: Dict[Block, List[Monomial]] = {}
        for monomial in self.candidate_monomials():
            block = (sum(monomial[0]), monomial[1].bit_count(), monomial[2].bit_count())
            out.setdefault(block, []).append(monomial)
        return out


def expected_ambient_dimension(n: int) -> int:
    return factorial(n) * (1 << (2 * n))
