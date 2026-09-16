# Exact Hilbert-basis certificate for one closed sign chamber

## Scope

Coordinates use the fixed order

```text
004 013 022 031 040 103 112 121 130 202 211 220 301 310 400.
```

Let `L` be the balanced lattice in `Z^15`, and let `K` be the cone generated
by the 18 triangular rays from Proposition 7.4.  This audit concerns exactly

```text
S = K intersect L intersect {gamma has signs +++++--+++++-++},
```

where `+` means a weak inequality `gamma_alpha >= 0` and `-` means
`gamma_alpha <= 0`.  Thus the three weakly negative coordinates are `103`,
`112`, and `301`; all other coordinates are weakly positive.  Boundary
points are included.  No other sign chamber is claimed here.

## Reproducible exact computation

Run from the project root:

```text
PYTHONPATH=/home/ailab/4math-open-problems/tools/pynormaliz \
  python3 evidence/verify_chamber_hilbert.py \
  --output evidence/chamber-hilbert-basis.json
```

The recorded run used PyNormaliz 2.24.  The script first verifies the frozen
`source.md` hash.  It reconstructs the 18 triangular rays, the three balance
equations, and a rank-12 lattice basis.  The 12 nonzero Smith invariants of
the ray matrix are all `1`; since the rays have the full rational kernel of
the balance matrix, this proves that their group span is the saturated
balanced lattice `L`.

The script independently reconstructs the 18 facets of `K`, appends the 15
weak coordinate-sign inequalities, and performs exact double-description
cuts.  The resulting 12-dimensional pointed chamber has 48 primitive extreme
rays.  PyNormaliz is then called twice:

1. from these 48 integer rays (a V-representation), and
2. from the 33 reconstructed facet/sign inequalities (an H-representation).

Both exact calls return the same 15 irredundant support hyperplanes, the same
48 extreme rays, and the same 134-element Hilbert basis.  The serialized JSON
contains the lattice basis, all defining inequalities, irredundant support
hyperplanes, extreme rays, and every Hilbert-basis element in both rank-12
lattice coordinates and the original 15 gamma coordinates.

Of the 134 generators, 48 are extreme rays and 86 are non-ray generators.
Their positive-degree distribution is

| positive degree | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 12 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| generators | 9 | 13 | 31 | 25 | 26 | 11 | 11 | 3 | 3 | 2 |

For every returned generator, the verifier separately reconstructs `gamma`,
checks all three balance equations, recovers the same integral lattice
coordinates, checks every one of the 33 chamber inequalities, and checks the
15 coordinate signs.  These checks use exact integers and rationals.

## Exact polynomial-support test

For each of the 134 generators, the ordinary coefficient polynomials
`P_alpha` are represented by exact finite supports.  Products retain the
first two column exponents in each of the four rows.  This eight-coordinate
compression is injective here: every product of `t` coefficient polynomials
has total row degree `t`, and balance gives the same `t` for numerator and
denominator.  Hence the omitted third-column exponent is uniquely forced.

All 134 generators satisfy

```text
supp(N_gamma) subseteq supp(D_gamma).
```

There are zero missing-support failures.  The largest numerator and
denominator supports encountered have respectively 889 and 157,521 terms.
This audit does not assert that `C=1` works for the non-ray generators; only
the support containment needed for existence of some positive `C` is used.

## Certified chamber theorem

Subject to fresh audit of the exact computation, the artifacts prove the
following scoped subsidiary statement:

> For every integral `gamma` in `BR_Q(4,3)` whose coordinates satisfy the
> weak sign pattern `+++++--+++++-++` in the displayed `H(4,3)` order, there
> exists a positive constant `C(gamma)` such that
> `C(gamma) D_gamma - N_gamma` is coefficientwise nonnegative.

Indeed, the Normaliz Hilbert-basis computation says that every point of `S`
is a nonnegative integral sum of the 134 recorded generators.  All generators
are sign-compatible, so numerators and denominators multiply without
coordinate cancellation under such sums.  Support containment is preserved
under multiplication.  Thus every element of `S` has numerator support
contained in denominator support, and the finite maximum of the corresponding
coefficient ratios supplies a positive constant.

This theorem does not resolve the frozen conjecture: 4,073 other strict sign
patterns remain, and a boundary point belonging to this closed chamber does
not provide generation across incompatible signs.
