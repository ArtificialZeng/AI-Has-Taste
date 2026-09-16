# Exact sign-chamber and small-sum audit

Run from the project root with

```text
python3 evidence/verify_sign_chamber.py
```

The verifier uses only exact integer/rational operations (including exact
linear rational arithmetic in Z3).  Its coordinate order is

```text
004 013 022 031 040 103 112 121 130 202 211 220 301 310 400.
```

## Balanced lattice and chamber count

The 18 recorded triangular rays have rank 12.  Their 12 nonzero Smith
invariants are all 1, so their group span is the full saturated balanced
lattice, not a proper finite-index sublattice.  An exact enumeration of all
11-subsets finds 18 facets of their real cone.

There are exactly 4,074 strict coordinate-sign patterns meeting the relative
interior of this cone.  The enumeration solves
`lambda_j >= 1` and `s_i (R lambda)_i >= 1` and blocks each discovered Boolean
sign pattern; homogeneity makes this equivalent to strict realizability.
Exactly 256 of these full-dimensional chambers have the primitive ray
`rho_(002;1)` in their closure.  Thus the phrase "the chamber containing the
ray" is not unique unless an adjacent orthant is specified.

## One specified adjacent chamber

The audit selects the closed chamber with sign pattern

```text
+++++--+++++-++
```

in the displayed coordinate order.  (There are five initial plus signs.)  A
strict relative-interior certificate is the positive coefficient vector

```text
(7,1,6,2,2,1,1,1,1,1,7,11,1,2,1,1,2,3)
```

in ray order
`(002;1),(002;2),(002;3),(011;1),...,(200;3)`.  Its image is

```text
(6,1,1,1,1,-1,-19,1,1,5,1,1,-1,1,1).
```

Exact double-description cuts give 48 primitive extreme rays for this closed
12-dimensional chamber.  Their positive degrees are distributed as follows:

| positive degree | 2 | 3 | 4 | 5 | 6 | 8 | 9 | 12 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| number of rays | 8 | 8 | 14 | 5 | 6 | 3 | 2 | 2 |

Every one of the 48 rays passes exact support containment.  Sparse supports
are represented by eight row/column exponents; this compression is injective
because the omitted third-column exponent is forced by the common row degree.
The full gamma vectors and support cardinalities are printed by the verifier.

## Independent small-sum falsification screen

The same verifier tests every distinct exponent vector obtained from a
multiset of two or three of the original 18 triangular rays.  There are 162
distinct two-ray sums and 984 additional distinct three-ray sums, for 1,146
vectors total.  All satisfy exact numerator-support containment in the
denominator support.

These are finite observations, not a resolution.  In particular, the 48
primitive real-cone rays are not asserted to be the balanced-lattice Hilbert
basis of the selected chamber.  Interior indecomposable lattice points remain
the decisive gap.
