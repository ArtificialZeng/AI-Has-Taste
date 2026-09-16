# Frozen source problem: projective equivalence without CCZ equivalence over F_11

Canonical id: win-00086-p03
Frozen on: 2026-09-10 (Asia/Shanghai)
Primary source:
- Huczynska--Klawuhn--Paterson, *The Intersection Distribution: New Results
  and Perspectives*, arXiv:2510.04675v2; published in *Finite Fields and
  Their Applications* 114 (2026), article 102828,
  DOI 10.1016/j.ffa.2026.102828.  See Theorem 2.9, Corollary 2.10, and
  Example 2.11 on PDF p.9; Definition 2.14 on PDF p.13; Open Problem 4 on
  PDF p.34.

## Definitions

For a function `h:F_11->F_11`, put

```
Gamma_h = {(x,h(x)): x in F_11},
S_h = {(x:h(x):1): x in F_11} union {(0:1:0)}.
```

Functions `f,g` are projectively equivalent here when an element of
`PGL(3,11)` maps `S_f` onto `S_g`.  They are CCZ-equivalent when an affine
permutation of the 121-point affine plane maps `Gamma_f` onto `Gamma_g`.

Fix

```
f(x)=x^4,  g(x)=x^8  over F_11.
```

## Statement

Prove that `f` and `g` are projectively equivalent but not CCZ-equivalent,
or give an exact counterexample to either part.  The projective equivalence
and the non-CCZ obstruction must both be certified.

For a graph `Gamma`, the proposed finite invariant is

```
Delta_Gamma(w) = |{(P,Q) in Gamma^2 : P-Q=w}|,  w != 0.
```

The full multiset over the 120 nonzero vectors may be used only after proving
that affine graph equivalence preserves it.

## Scope and contribution boundary

The primary source already proves in Example 2.11 that `x^4` and `x^8` are
projectively equivalent and observes that they are not EA-equivalent.  Open
Problem 4 asks whether any projectively equivalent pair can fail to be
CCZ-equivalent.  Thus only a rigorous non-CCZ separation of this pair can
resolve the open problem; repeating projective or EA inequivalence is not a
new result.

Difference distributions, differential spectra, CCZ invariants, and affine
graph equivalence have an existing literature.  A manuscript must locate and
credit the appropriate prior form of this invariant and must not claim to
invent it.  It must also search for any post-v2 resolution of Open Problem 4.

The exact certificate must give the projective transformation including its
action on the zero and infinite points, both 120-entry integer difference
tables (or a symmetry-reduced table with a complete reconstruction proof),
and a checker using arithmetic modulo 11.  Floating point computation is not
relevant.

The bibliography must normally cover the primary paper and the relevant
foundational CCZ/differential-spectrum literature, plus one or two genuinely
relevant papers from the user's Excel library when available.  That minimum
does not cap references and cannot be satisfied by padding.

This file is immutable.  Changing the field, polynomials, or equivalence
notions creates a different problem.

