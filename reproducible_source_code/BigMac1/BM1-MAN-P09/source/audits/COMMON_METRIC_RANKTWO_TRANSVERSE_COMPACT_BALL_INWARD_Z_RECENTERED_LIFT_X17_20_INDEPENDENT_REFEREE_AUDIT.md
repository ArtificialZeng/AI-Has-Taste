# Independent referee audit: recentered inward-Z lift to X=17/20

Date: 2026-08-25  
Verdict: **PASS**  
Classification: **fatal 0 / major 0 / minor 0**

## Audited claim

The audited cell is

```text
0<S<=1/10000, 83059/100000<=X<=17/20,
|M|<=1/1000, |omega|,|nu|<=1/100,
Z=9/13-X^2+S*b-S^2*y0^2+2(X-83059/100000).
```

The claim is only that the original fully conjugated Hermitian scalar gate
is strictly positive on this legal rank-two compact-ball family, for both
signed lifts of `z`. It is not a full compact-ball theorem, unrestricted
common-metric result, arbitrary-node/dimension theorem, raw-gate
counterexample, chart-maximality result, or fixed crossing-lens theorem.

## Independence boundary

The frozen candidate source
`tmp/research/compact_ball_inward_z_recentered_lift_x17_20_exact_gate.py`
was treated as opaque bytes and used only for its SHA-256 digest. It was not
opened for coefficients, parsed, imported, executed, or consulted for
helpers or Bernstein controls. Its digest is
`9875a6d365c0ed8a52deccd85415b7e1e3288778e420ef5415d7f6ce2c827e4d`.
The source-freeze manifest digest is
`d32d987a7ed49e3be0b68742e994fb6810b8e164022040bbafab0a305ad75a87`.

The referee started from the audited compact-ball definitions. It ordered
the signed Gram columns as `(z-column, mixed-column)`, formed each of the
nine entries of `Q^2` as its own three-term scalar product, eliminated the
relations in the order `h`, `q`, signed `z`, substituted the sheet densely,
and transformed the bivariate tensor with the `tau` axis first. This is
definition-level work and not the source's sparse pre-map or saved control
table.

## Exact mathematical reconstruction

The referee verified all of the following exactly.

1. The frame vectors are orthonormal modulo `h^2=S`, `q^2=1-S`; the
   compression is Hermitian, even in signed `z`, and has determinant
   `(5/9)SZ`.
2. All `9/9` entries of `Q^2` agree with explicit matrix multiplication and
   form a Hermitian matrix.
3. The literal four-term fully conjugated raw gate equals the independent
   cyclic Gram-vector expression. Frame radicals cancel, the result is real,
   and its exact degree in `Z` is four.
4. Multiplication of `36*Gate` by the strictly positive factor
   `25^8(1+M)^8 S^3` is exactly reversible. After removing only the displayed
   nonnegative layer, the structural counts are `34/34/1659` and the
   `(S,X)` bidegree is `(7,4)`.
5. Fresh dense Bernstein conversion on the lossless cell yields `40/40`
   strict centered rational lower controls. The unique weakest index is
   `(7,0)` and its exact reserve is

```text
4989868253428042904100458867373768732890103155600729500817292846407383462088295685657449907
/37458715500011520000000000000000000000000000000000000000000000000000000000000000.
```

   The complete weakest-control polynomial was independently reconstructed
   and its centered coefficient-l1 lower bound was recomputed to be exactly
   this reserve. Thus nonnegative Bernstein weights, not samples, prove the
   continuum statement.
6. At `X=83059/100000` every raw-gate input and the cleared gate splice
   parameter by parameter to the audited predecessor.
7. Exact monotonicity gives

```text
dZ/dX >= 814199/2750000 > 0,
Z >= 160243869095653/15857127000000000000 > 0,
Z < 701/81250 < 1,
T_max = -8425838367/357500000 < 0,
D >= 135767/650000 > 0,
det(C) >= [160243869095653/28542828600000000000] S > 0.
```

   Consequently `lambda>0`, strict danger, rank two, and both signed lifts
   are legal on the complete cell.
8. All 72 exact rational endpoint/midpoint/corner diagnostics are legal and
   raw-gate positive. Their smallest raw-gate value was

```text
2300246806628869221146172981442144843035125440470830199752746439
/2613510006250000000000000000000000000000000000000000
```

   at `(S,X,M,omega,nu)=(1/10000,83059/100000,-1/1000,-1/100,-1/100)`.
   These nodes were used only as falsification diagnostics.

## Adversarial review

- **Numerical evidence promoted to proof:** rejected. Every sign decision is
  rational/algebraic; the 72 nodes are explicitly downstream diagnostics.
- **Old chart obstruction promoted to a gate counterexample or maximality:**
  rejected. The recentered formula changes `Z` beyond the exact splice, and
  the theorem is stated only for this new legal chart.
- **CE-046:** no real-part monotonicity or deletion of complex interference
  is used; the full conjugated `Q^2` terms are retained.
- **CE-048:** no feasible-center absorption implication is used.
- **CE-059:** no fixed copositivity allocation such as `s=-2` is used.
- **CE-060:** no quadratic remainder anchored at `Z=0` is used.
- **Partial theorem promoted to an unrestricted solution:** rejected by the
  explicit scope and open-problem statements.

Fail-closed tests rejected optimized Python, a bad source hash, a changed
recentered-Z normalization, deletion of a `Q^2` contribution, a flipped
danger sign, and deletion of one core coefficient. The last attack reached
the structural check and failed because the core had 33 rather than 34
nonzero `(S,X)` coefficients.

## Findings and conclusion

No fatal, major, or minor mathematical, certificate, dependency, or scope
finding was identified. The candidate passes as an **exact independently
audited partial theorem on the displayed recentered cell only**. This audit
does not authorize any broader claim and did not modify the project ledgers,
manuscripts, PDF/ZIP artifacts, or candidate source.

Replay from the project root:

```sh
.venv/bin/python -B tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_inward_z_recentered_lift_x17_20_independent_referee.py
```
