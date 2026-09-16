# win-00078-p02 — finite classical-mass-action sensitivity-zero census

## Immutable primary-source record

- Arne Kuhrs, Máté L. Telek, and Nicola Vassena, *Layered mixed matrices and
  reaction networks*, arXiv:2609.05100v1.
- Official HTML: <https://arxiv.org/html/2609.05100v1>
- Official PDF: <https://arxiv.org/pdf/2609.05100v1>
- Local full text: `bigWin-78-materials/2609.05100.pdf`, SHA-256
  `948965eb5b52a0229289fb7ac885ad02fdd2860d07b55724ee717f7bb2585bdf`.
- Locators: equations (22)--(25) and Remark 3.6 (PDF p.17);
  Theorem 3.23 (PDF p.27).

## Frozen assertion

Let the ordered complex set be

```
C = (0, X, Y, 2X, X+Y, 2Y).
```

Use the induced lexicographic order on directed reactions `(source,target)`. Among
all simple directed networks `E subset C times C` with no loops or repeated
reactions and `3<=|E|<=4`, retain exactly those for which

1. the integer stoichiometric matrix `S` has rank two;
2. `ker(S)` contains a strictly positive real vector;
3. the source's independent-symbol determinant `det(SR)` is not identically zero.

For every retained network, reaction `rho`, and species `m`, compare the generic
entry `(A_gen^{-1})_(m,rho)` with its classical-mass-action specialization, where

```
A_gen = [R | C_Gale],
R_MA = diag(v) (S^-)^T diag(x)^(-1),
S v = 0,
```

using the source's row/column conventions. Decide whether there exists a pair for
which the generic entry is nonzero but the mass-action entry is identically zero
on the positive steady-state parameter variety. If yes, return the lexicographically
smallest canonical network and pair; otherwise certify absence throughout this
finite class.

## Nearest result and exact delta

Theorem 3.23 characterizes sensitivities in the independent-symbol model through
reachability in the influence graph. Remark 3.6 states that classical mass action
is not parameter-rich and imposes additional algebraic constraints that require
further analysis. The exact six-complex census above is a newly frozen finite test
of that distinction; the paper does not assert that this particular census is open.

## Cheapest decisive attack and certificate

Before isomorphism reduction the search has
`binom(30,3)+binom(30,4)=31,465` labelled edge sets. Canonicalize under the species
permutations induced by swapping `X,Y`. Use exact integer/rational arithmetic.
Parameterize steady fluxes by a rational Gale basis `v=C_Gale z`. The normalization
`x=(1,1)` is legitimate for testing existence because any positive steady flux is
realized by positive mass-action constants `k_rho=v_rho` there.

For a positive result preserve: canonical reaction list; integer `S` and `S^-`;
rational Gale basis; the nonzero generic inverse cofactor; an exact ideal-membership
identity proving its mass-action specialization vanishes modulo `<Sv>`; a positive
rational flux; and a nonzero specialized determinant. Independently replay all
identities.

For a negative result preserve: a complete canonical-orbit manifest with hashes,
exact positivity/rank/determinant filters, and reduced exact normal forms for every
surviving cofactor. Sampling or floating-point evaluation cannot certify absence.

One research pass is the intended initial cap. Park promptly if the formulation
collides with known literature or exact elimination is not bounded in practice.
