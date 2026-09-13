# Recentered inward-Z lift beyond the old chart root: exact source candidate

Date: 2026-08-25. Status: **exact source-level partial-theorem candidate,
pending a genuinely independent definition-level referee**.

## 1. Precise cell and scope

Let

```text
0<S<=1/10000,             83059/100000<=X<=17/20,
|M|<=1/1000,             |omega|,|nu|<=1/100,
A=1+M,                   lambda=A/S,
y0=12/(25A)+nu,
b=(45M+18)/(25A)-(3/5)X+omega-(10636/275)(X-1/5),
x=-1/5+X,                y=3/5+S y0,
Z_old=9/13-X^2+S b-S^2 y0^2,
Z=Z_old+2(X-83059/100000).
```

For both signed lifts `z=+-sqrt(Z)`, the source candidate proves that these
are legal, strictly dangerous rank-two compact-ball data and that the
original fully conjugated Hermitian scalar gate is strictly positive.  At
the left endpoint the added lift vanishes exactly, so this cell splices
termwise to the independently audited predecessor.

This is one local cell.  It does not prove the full compact-ball quartic, the
general complex common-metric theorem, arbitrary nodes or dimension, or a
fixed crossing-lens optimal constant.

## 2. Definition-level gate and sparse exact clearing

The source constructs the signed compact-ball frame, the Hermitian matrix
`Q`, every entry of `Q^2`, and the original conjugated leakage gate from the
definitions.  Eliminating only

```text
q^2=1-S,          h^2=S,          z^2=Z
```

gives a scale quartic with constant coefficient five.  Its exact degree in
`Z` is four.  No stored quartic or coefficient table is imported.

To avoid an irrelevant monolithic SymPy expansion, the source forms the
audited 134-term pre-map in `(S,Z,X,Yaux)`, composes it by exact sparse
dictionary multiplication with the displayed `y` and new `Z`, and clears
only the positive factor

```text
25^8 A^8 S^3.
```

After removing the manifestly nonnegative layer

```text
S^3 25^8 M^2 A^8 (5M^2+14M+14),
```

the exact structure is

```text
cleared (S,X) coefficients: 34
core (S,X) coefficients:    34
centered monomials:          1659
bidegree (S,X):              (7,4).
```

## 3. Continuum positivity certificate

On the lossless cell map

```text
X=83059/100000+(17/20-83059/100000)u,
S=tau/10000,                 0<=u,tau<=1,
```

a fresh bidegree-`(7,4)` Bernstein tensor has 40 controls.  All 40 centered
rational L1 lower controls are strictly positive.  A weakest index is
`(7,0)`, with reserve

```text
4989868253428042904100458867373768732890103155600729500817292846407383462088295685657449907
/37458715500011520000000000000000000000000000000000000000000000000000000000000000.
```

The complete weakest-control polynomial is printed by the source log.  Since
the tensor Bernstein weights are nonnegative and sum to one, this is a
continuum proof for the displayed cell.  The 72 endpoint/midpoint nodes are
breaker diagnostics only.

## 4. Full-cell legality

The new lift obeys

```text
dZ/dX=2-2X-(10801/275)S
     >=814199/2750000>0.
```

Exact monotonicity in all centered parameters and in `S` gives

```text
Z >= 160243869095653/15857127000000000000 > 0,
Z < 701/81250 < 1.
```

Writing `T=(6/5)y0+b`, its exact full-cell maximum is

```text
T_max=-8425838367/357500000<0.
```

The literal danger identity is

```text
D=1-x^2-y^2-Z
 =(2/5)(X-3/13)-2(X-83059/100000)-S T,
```

and therefore

```text
D >= 135767/650000 > 0,
det(C)=(5/9)SZ
      >= [160243869095653/28542828600000000000] S > 0.
```

Thus both signs of `z` are legal and rank two everywhere on the cell.

## 5. Breaker and fail-closed tests

The source evaluates the literal original raw gate on three exact positive
scales, the left/middle/right `X` values, and all eight centered corners.
All 72 points are legal, strictly dangerous, and gate-positive.

The final frozen bytes reject:

- optimized Python (`python -O`);
- a corrupted frozen dependency hash;
- a deliberately changed sparse `Z` normalization;
- deletion of one exact core coefficient.

Two earlier monolithic four-endpoint and one-endpoint attempts were stopped
for resource growth before a sign decision.  They are implementation/resource
failures, not mathematical counterexamples.  Two later assertions initially
used unsimplified rational expressions (`expand` instead of `cancel`) and an
obsolete predecessor value for `T_max`; both were exposed before freezing,
corrected by exact identities, and followed by a complete from-scratch PASS.

No sampled SDP, floating sign decision, real-part monotonicity, feasible-
center absorption, fixed copositivity allocation, or CE-046/048/059/060 route
is used.  No proof assistant is used.

## 6. Replay and next gate

Run from the project root:

```text
.venv/bin/python tmp/research/compact_ball_inward_z_recentered_lift_x17_20_exact_gate.py
```

The next mandatory gate is a separate no-import referee that reconstructs
the Hermitian `Q,Q^2` gate and all 40 controls without importing this source
or its coefficient objects; it must also reprove the splice, every legality
bound, both signed lifts, the 72 raw-gate diagnostics, and all negative tests.
Until that audit passes, this remains a source candidate and must not be
promoted to the five project ledgers or a manuscript.
