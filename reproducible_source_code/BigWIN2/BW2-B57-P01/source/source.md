# Frozen source — win-00057-p01

## Problem

For positive real numbers `r,q,t`, let

```text
P(r,q,t) =
[1 r q q r t t;
 r 1 r q q t t;
 q r 1 r q t t;
 q q r 1 r t t;
 r q q r 1 t t;
 t t t t t 1 1;
 t t t t t 1 1].
```

Let `z` be the clique-web exponent vector

```text
z = x13+x14+x24+x25+x35+x67 - sum_{i=1}^5 (x_i6+x_i7)
```

and set `alpha=z/4`, so the sum of its coordinates is `-1`. On this family,

```text
P(r,q,t)^alpha = (q^5/t^10)^(1/4).
```

Determine the exact supremum of `P(r,q,t)^alpha` over all `r,q,t>0` for which `P(r,q,t)` is Lorentzian, and decide whether the supremum is attained. Give an exact extremal sequence when it is not attained.

The published characterization to be used and independently verified is

```text
r+q-2 >= sqrt(5)*abs(r-q),
t^2 >= (1+2r+2q)/5.
```

The frozen scope is only this explicit three-parameter family. Equality with the global bounded-ratio constant `f(alpha)` must not be claimed without a separate proof.

## Primary source and contribution boundary

- Lorenzo Baldi and Mario Kummer, *A note on bounded ratios*, arXiv:2609.03934v1, equations (1)--(3) and Lemma 3.2, PDF pp.3--4: https://arxiv.org/abs/2609.03934
- The paper evaluates the admissible point `(284,701,20)` and obtains approximately `2.01638>2`; it does not state the sharp supremum of the displayed family.
- Proposed delta: replace that one witness by the exact sharp constant, an attainment classification, and exact extremal sequences. Any stronger global claim requires new evidence and a new freeze.

## Cheapest decisive test and certificate

Eliminate `t` by monotonicity, minimize admissible `r` for fixed `q` in the two branches `r<=q` and `r>=q`, then prove the resulting rational function monotonicity. A certificate consists of exact algebraic inequalities plus rational triples approaching the proposed supremum. A single admissible rational triple above the candidate constant falsifies it.

## Provenance

Primary PDF: `batches/inbox/bigWin-57-materials/2609.03934.pdf`, SHA-256 `5305355edbfa76529210e00013baa51491d63b665b302bf06d8362699bef6d6f`.
