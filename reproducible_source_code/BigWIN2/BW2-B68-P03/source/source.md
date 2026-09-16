# win-00068-p03 — Two modulo-16 congruences for 18-colored generalized Frobenius partitions

## Immutable primary-source record

- Primary source: H. Das, H. Nath, and A. Sarma, *Proof of a Conjecture of Cui, Gu and Tang on 18-Colored Generalized Frobenius Partitions*, arXiv:2609.05302v1, <https://arxiv.org/abs/2609.05302>.
- Definition location: PDF page 1, Introduction.
- Frozen conjecture location: PDF page 21, Conjecture 5.1.
- Source status: the authors state that the two congruences below are based on numerical evidence and leave their proofs for future investigation.

## Definitions

A generalized Frobenius partition of an integer \(N\ge0\) is a two-row array
\[
\begin{pmatrix}
a_1&a_2&\cdots&a_r\\
b_1&b_2&\cdots&b_r
\end{pmatrix},
\]
where the entries are nonnegative integers in weakly decreasing order along each row and
\[
N=r+\sum_{j=1}^r(a_j+b_j).
\]
In a \(k\)-colored generalized Frobenius partition, the parts carry one of \(k\) colors, with the ordering and counting convention of Andrews used by the primary source. Let \(c\phi_k(N)\) denote their number. Before doing coefficient computations, the worker must audit the precise colored-part ordering against the source or its cited generating function; an ordinary partition count or an independently invented coloring convention is not interchangeable with \(c\phi_k\).

## Frozen problem

Prove or disprove both assertions of Conjecture 5.1:
\[
c\phi_{18}(30n+19)\equiv0\pmod {16}
\qquad\text{for every integer }n\ge0,
\]
and
\[
c\phi_{18}(30n+25)\equiv0\pmod {16}
\qquad\text{for every integer }n\ge0.
\]

The two progressions form one frozen source conjecture. A proof or counterexample for only one progression is a precisely scoped partial result, not a resolution of both. A disproof must give the least failing \(n\) within the exactly reproduced coefficient sequence whenever feasible, together with an exact coefficient certificate.

## Nearest results in the primary source

The paper proves, for every \(n\ge0\):

- Theorem 1.2: \(c\phi_{18}(6n+5)\equiv0\pmod 8\);
- Theorem 1.3: \(c\phi_{18}(3n+1)\equiv0\pmod {81}\) and \(c\phi_{18}(3n+2)\equiv0\pmod {2187}\).

It also proves two high-power congruences for \(c\phi_{16}\). Its methods use exact generating functions, \(q\)-series dissections, and a \((p,k)\)-parametrization. The proposed delta is specifically the additional factor of \(2\) on the two residue classes \(19,25\pmod {30}\); it is not supplied by merely restating the source's established modulus-8 result.

## Cheapest decisive tests

1. Reproduce the source-compatible generating series for \(c\phi_{18}(N)\) and compute coefficients exactly modulo \(16\), not with floating-point arithmetic.
2. Check both progressions over a substantial prefix, recording the recurrence or truncated-product algorithm, coefficient range, software versions, and hashes of any certificate files.
3. In parallel, reduce the source's exact generating function modulo \(16\) and perform the relevant \(2\)- and \(3\)- or \(5\)-dissections needed to isolate exponents \(30n+19\) and \(30n+25\). Audit whether the proven \(6n+5\pmod8\) identity has a lift modulo \(16\) on precisely these two subprogressions.
4. If a modular-form reinterpretation is used, state the form, level, character, integral coefficient ring, and a rigorously justified finite bound before invoking a finite coefficient check.

The fastest disproof is an exact coefficient not divisible by \(16\) in either progression. Any discrepancy must first be checked against the colored Frobenius convention and an independently implemented coefficient generator.

## What does not count as a proof

- No finite enumeration, however long, proves either all-\(n\) congruence without a theorem reducing the universal statement to a justified finite bound.
- Numerical agreement from one implementation is evidence only; it must be replayed independently before being used even as a computational claim.
- Formal power-series manipulations truncated at \(q^M\) are not identities in \((\mathbb Z/16\mathbb Z)[[q]]\) unless the omitted tail is rigorously controlled for the claimed coefficient range or the argument is genuinely formal.
- The source's modulus-8 theorem on \(6n+5\) does not imply either modulus-16 statement without an additional argument.
- A proof of one residue class must not be described as proving Conjecture 5.1 in full.

## Required evidence for acceptance

An accepted proof must provide an exact generating-function derivation or a valid modular-form/Sturm-type reduction, cover all \(n\ge0\), and receive a fresh referee audit of every dissection and divisibility step. An accepted disproof must provide the exact counterexample coefficient, two independent reproductions, and the corrected mathematical scope. Until one of those gates passes, finite checks are recorded only as observations supporting or attacking the conjecture.
