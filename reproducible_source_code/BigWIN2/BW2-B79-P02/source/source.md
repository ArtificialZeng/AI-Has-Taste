# win-00079-p02 — necessity of cut--pad stability for finite-corner reconstruction

## Immutable primary-source record

- Mohsen Kian and Fuad Kittaneh, *Finite-Corner Reconstruction and Separation
  for Cones of Normal Maps*, arXiv:2609.04889v1.
- Official HTML: <https://arxiv.org/html/2609.04889v1>
- Official PDF: <https://arxiv.org/pdf/2609.04889v1>
- Local full text: `bigWin-79-materials/2609.04889.pdf`, SHA-256
  `5b22fea96a72de6c107ab8eccebfdbd3002f670d093038ff5ff1465986b93421`.
- Locators: Definition 3.3, Theorems 3.9 and 4.1, and Proposition 5.5 (PDF
  pp.5, 7, 13--15, 21--23).

## Frozen assertion

Let `H` be an infinite-dimensional complex Hilbert space and let `CP^sigma`
be the cone of normal completely positive maps `B(H)->B(H)`. Disprove:

> Every point-ultraweakly closed convex cone `K` contained in `CP^sigma` is
> determined by its finite corner cones even without assuming cut--pad
> stability.

More precisely, construct a point-ultraweakly closed proper convex cone
`K proper-subset CP^sigma` for which

```
K_(Q,P) = CP_(Q,P)
```

for every pair of finite-rank projections `P,Q`. Corner notation and the
point-ultraweak topology are exactly those of the source.

## Nearest result and exact delta

Theorems 3.9 and 4.1 prove reconstruction and corner-bipolar separation under
both point-ultraweak closedness and cut--pad stability. Proposition 5.5 keeps
cut--pad stability but drops closedness, showing the closedness assumption is
essential. The target asks for the complementary sharpness example: keep
closedness and complete positivity but drop cut--pad stability.

This is not asserted by the source to be open. It is a precise, source-adjacent
hypothesis audit. A narrow later-literature search is mandatory before any
priority language.

## Cheapest decisive attack and certificate

Fix a unit vector `e`, put `E=|e><e|`, `A=2E-I`, and test

```
K={Phi in CP^sigma : <e,Phi(A)e> <= 0}.
```

For every finite `P,Q` and every `psi in CP_(Q,P)`, check the zero extension
and the rank-one normal CP perturbation

```
Theta_v(T)=<v,Tv>E,
```

where `v` is a unit vector perpendicular to `ran(P)+C e`. A complete proof
must show that a nonnegative multiple of `Theta_v` makes the extension satisfy
the half-space inequality without changing its `(Q,P)` corner. It must also
prove point-ultraweak closedness, convexity, properness, and failure of
cut--pad stability by an explicit map and projections. Every sign, domain,
normality, and complete-positivity claim must be checked directly.

If any step fails, search symmetrically for another exact cone or prove an
obstruction to this half-space construction; do not weaken equality of all
finite corner cones to equality along one projection sequence.
