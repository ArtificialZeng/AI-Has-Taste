# Independent referee audit: recentered inward-Z adjacent cell to X=7/8

Date: 2026-08-25  
Verdict: **PASS**  
Classification: **fatal 0 / major 0 / minor 0**

## Claim and independence boundary

The audited cell is

```text
0<S<=1/10000, 17/20<=X<=7/8,
|M|<=1/1000, |omega|,|nu|<=1/100,
Z=9/13-X^2+S*b-S^2*y0^2+2(X-83059/100000).
```

The frozen candidate source was treated as opaque bytes and used only for
SHA-256. It was not opened for its coefficient data, parsed, imported,
executed, or consulted for controls or helper functions. Its digest is
`33bad020143d4e4143b0742526b4fb0ba4d0089d1e12e8365ceca878577e0d2e`;
the source-freeze manifest digest is
`bf68bd1522118abb2d04fff5aeb70443b766250ade53702a9259eaeb88aa384b`.

The audit also binds the previous independently audited cell by the exact
source/referee/report/referee-manifest hashes supplied in the dispatch. No
previous coefficient or control table was imported. The new referee starts
from the raw compact-ball definitions, checks a direct compression against a
separately ordered signed-z Gram sum, forms every `Q^2` entry explicitly,
eliminates signed `z`, then `h`, then `q`, and uses a fresh dense tau-first
Bernstein transform.

## Exact results

The following gates passed.

1. The frame is orthonormal modulo `h^2=S`, `q^2=1-S`; the compression is
   Hermitian, even in signed `z`, and has determinant `(5/9)SZ`.
2. All `9/9` entries of `Q^2` agree with direct matrix multiplication and
   satisfy Hermitian symmetry.
3. The literal fully conjugated raw gate equals the independently assembled
   cyclic vector gate. All frame radicals cancel, the result is real, and
   its exact degree in `Z` is four.
4. Clearing `36*Gate` by the positive factor `25^8(1+M)^8S^3` is exactly
   reversible. Removing only the displayed nonnegative layer gives
   `34/34/1659` and bidegree `(7,4)`.
5. The new cell has `40/40` strict centered rational Bernstein lower
   controls. The unique weakest index is `(7,0)`, with exact reserve

```text
36396400755316082608953526916356109068914066995807402520780718071668303870073911227
/239735779200073728000000000000000000000000000000000000000000000000000000.
```

   The complete weakest-control polynomial was independently reconstructed,
   and its centered coefficient-l1 lower bound is exactly the displayed
   reserve. The nonnegative Bernstein partition, not node samples, proves
   positivity on the continuum.
6. At `X=17/20`, the parameters, cleared raw gate, and cleared core splice
   exactly to a separately reconstructed copy of the previous cell.
7. Exact monotonicity establishes

```text
dZ/dX >= 676699/2750000 > 0,
Z >= 97261562093134873/15857127000000000000 > 0,
Z < 40307/2600000 < 1,
T_max = -434919/17875 < 0,
D >= 109767/650000 > 0,
det(C) >= [97261562093134873/28542828600000000000] S > 0.
```

   Hence `lambda>0`, strict danger, rank two, and both signed-z lifts are
   legal throughout the complete cell.
8. All 72 exact endpoint/midpoint/corner diagnostics are legal and raw-gate
   positive. The smallest was

```text
16778139227521596145974491304128605159669900943351380079
/16726464040000000000000000000000000000000000
```

   at `(S,X,M,omega,nu)=(1/10000,17/20,-1/1000,-1/100,-1/100)`. These
   evaluations are explicitly diagnostics, not the continuum proof.

## Adversarial review

- Optimized Python, bad source and predecessor hashes, bad sparse-Z
  normalization, deletion of a `Q^2` contribution, a flipped danger sign,
  and deletion of a core coefficient all failed closed.
- No floating or sampled sign was promoted to a theorem.
- A chart obstruction was not described as a raw-gate counterexample or
  maximality statement.
- The proof retains the complex interference, uses no feasible-center
  absorption, no fixed `s=-2` allocation, and no `Z=0` anchored quadratic
  remainder. Thus CE-046, CE-048, CE-059, and CE-060 are not reused.
- The statement remains one adjacent local chart. It is not expanded to the
  full compact ball, unrestricted common metric, arbitrary nodes/dimension,
  or a fixed crossing-lens optimal constant.

## Conclusion

No fatal, major, or minor finding was identified. The candidate passes as an
**exact independently audited adjacent local theorem only**. This audit did
not modify the five ledgers, research state, v13/v14/v15 artifacts, any
PDF/ZIP, or the candidate source.

Replay from the project root:

```sh
.venv/bin/python -B tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_inward_z_recentered_lift_x7_8_independent_referee.py
```
