# Independent referee audit: enlarged active-block `t` layer

Date: 2026-08-23.  Verdict: **PASS as an exact seven-real-parameter partial
theorem**.

Audited snapshot:

- `tmp/research/common_metric_tilted_rankone_complex_scale_t403_enlargement.md`
  (`SHA-256 206551077ae5999cf454620aabdbbed62d648bdf84e8907a716aa7e4c19f1f6c`);
- `tmp/research/verify_common_metric_tilted_rankone_complex_scale_t403_enlargement.py`
  (`SHA-256 ae76c2868c797a5521b15d2c42fd0dfe2746ac70fbca7122b145da95b4f22a74`);
- independent verifier
  `audit/verify_common_metric_tilted_rankone_complex_scale_t403_enlargement_referee.py`
  (`SHA-256 b439d7ff59698c7eb3f5f470d322378a8497ea64cc813efb5b6484a171193575`).

The independent verifier does not import the builder or discovery code.  It
reconstructs the fully conjugated Hermitian gate and all scale-cubic
polynomials from definitions.  Before using either `t=4` centre margin, it
also reruns the immutable independent nodal referee on both stitched `r`
cells.  Thus the decisive sign table is not accepted from the builder.

The unrestricted complex Hermitian gate, the common-metric theorem, and the
fixed crossing-lens constant remain open.

## 1. Hermitian phase and rank-two boundary

With `a=3/5`, `c=4/5`, `s=sqrt(T)`, the reconstructed matrix is

\[
 Q=\begin{pmatrix}
 r&s(k+i\ell)&z+iw\\
 s(k-i\ell)&Tn/\Delta&s\\
 z-iw&s&t
 \end{pmatrix},
\]

where

\[
 \Delta=rt-z^2-w^2,
 \qquad
 n=t(k^2+\ell^2)+r-2(kz+\ell w).
\]

Direct conjugated multiplication gives the active block determinant
`Delta`, its Schur value `Tn/Delta`, and `det Q=0`.  The exact certificate
proves `Delta,n>0` on the whole closed shape box, so the active block is
positive definite and `Q` is PSD of rank exactly two for `T>0`.  At the
closure `T=0`, the active block remains positive definite and the middle row
and column vanish, so the rank is still exactly two.

The dangerous scalar is reconstructed as

\[
 \operatorname{Re}(Qp)_1=\frac35r+\frac45z<0.
\]

No conjugate or cyclic phase is deleted in these calculations.

## 2. Legal scale half-line

Replacing the middle diagonal by a free real `q` and recomputing the last
complex leakage gives

\[
 \operatorname{Im}\{c\overline{(Qp)_2}-i(Q^2)_{32}\}
   =-s(q-g),
 \qquad
 g=\frac{12}{25}\ell-zk-w\ell-t.
\]

Therefore

\[
 q_{\min}=\frac{Tn}{\Delta},\qquad q_g=g,
 \qquad q_{\min}-q_g=\frac{Tn-\Delta g}{\Delta}.
\]

The strict complementary branch is exactly

\[
 T>0\quad(g\leq0),
 \qquad
 T>\frac{\Delta g}{n}\quad(g>0).
\]

For `g>0`, the finite endpoint `T_L=Delta*g/n` is its closure.  For `g<=0`,
the closure endpoint is `T=0`.  The transition `g=0`, both finite endpoints,
and the unbounded scale tail are all covered; no scale sampling is used.

## 3. Independent original-gate cubic

Starting from the fully conjugated scalar gate, the referee first expands in
the real coupling `s`, verifies that every power is even, and substitutes
`T=s^2`.  This independently gives

\[
 4\Delta^2\mathcal G(Q)
 =P(T)=C_0+C_1T+C_2T^2+n^2T^3,
\]

with

\[
 C_2=\Delta^2(k^2+\ell^2)-2\Delta gn.
\]

A second residual-square expansion reproduces the same polynomial, so the
extraction is not relying on one symbolic path.  At
`T_L=Delta*g/n`, exact cancellation gives

\[
 P(T_L)=\frac{N_0}{15625n^2},\qquad
 P'(T_L)=\frac{N_1}{625n},\qquad
 -\operatorname{Disc}_T(P)=\frac{N_D}{244140625}.
\]

The denominator signs and the minus sign in `N_1` were reconstructed rather
than copied.  The universal cubic discriminant formula was checked
symbolically before `N_D` was formed.

## 4. Both stitched centre cells and all eight sign groups

The verifier replayed the independent rational nodal/collocation certificate
for each closed centre cell:

- `r in [99/100,101/100]`: 734,288 exact Bernstein controls;
- `r in [101/100,103/100]`: 734,288 exact Bernstein controls.

Every control was reconstructed from exact rational nodes and then mapped
back to those nodes.  Both runs returned exit code zero.  Their output
digests were respectively

```text
795888e5306edecb6f489a1fb1e174b962902e13bcfff505af6331f9cd3df360
5e95bb76e4cbea182b199561c34103e9292840f292fba2c1e9a7e455615bf16f
```

The common boundary `r=101/100` is included by both cells, so there is no
stitch gap.

Next, the referee independently differentiated the eight polynomials

```text
danger, Delta, n, C0, C1, N0, N1, ND
```

with respect to `t`.  Their exact power-term counts are

```text
1, 1, 2, 62, 67, 1851, 326, 84595.
```

On the wider box `399/100 <= t <= 401/100`, direct absolute monomial bounds
give `|partial_t p| <= M`.  Applying the exact mean-value bound
`p(t)>=m-M/403` separately to both centre cells yields the following smaller
reserve across the stitch:

| group | exact least reserve at radius `1/403` |
|---|---:|
| danger | `87/500` |
| `Delta` | `5725107/2015000` |
| `n` | `1173052317/4030000` |
| `C0` | `168031168212372292987/503750000000000000` |
| `C1` | `473798761153505578829/503750000000000000` |
| `N0` | `53688775478983631337804470500482797123/128960000000000000000000000` |
| `N1` | `10834008694368493232491091993/64480000000000000000` |
| `ND` | `211896779612896328421389008272777422300367253543677239239053722934418999/20633600000000000000000000000000000000000000000000` |

All eight reserves are strictly positive on both closed `r` cells and at both
closed `t` endpoints.

## 5. Cubic sign and degeneracies

If `g<=0`, the certified `C0,C1,Delta,n>0` and

\[
 C_2=\Delta^2(k^2+\ell^2)-2\Delta gn>0
\]

make every coefficient of `P` positive.  This proves strict positivity for
all `T>=0`, including the closure `T=0`.

If `g>0`, the certified `N0,N1>0` give a positive value and positive first
derivative at `T_L`.  Moreover

\[
 C_2+3n^2T_L
 =\Delta^2(k^2+\ell^2)+\Delta gn>0.
\]

Since the curvature increases with `T`, the cubic increases strictly from a
positive endpoint on the entire unbounded half-line.  The additional
`N_D>0` check excludes a tangent cubic but is logically redundant once the
positive endpoint derivative has been proved.  Hence all scale, branch,
endpoint, and `g=0` degeneracies in the stated family are covered.

## 6. Strict enlargement and nonredundancy

Exact comparison gives

\[
 \frac1{403}>\frac1{500},
\]

so `[1999/500,2001/500]` is strictly contained in
`[1611/403,1613/403]`; the half-width grows by `500/403`.

For the scale-free active-block invariant `(r+t)/sqrt(Delta)`, the sign of
its `t` derivative is the sign of

\[
 rt-r^2-2(z^2+w^2).
\]

This numerator is increasing in `r` on the wider box and has exact lower
bound `461/625>0`.  Thus varying `t` is not the coupling scale `T` and is not
a common active-block rescaling.  The original gate itself also contains the
fixed `ac` term together with `Q^2`, so common scaling is not a gate
invariance.

## 7. Phase integrity

The exact interior witness at `t=2001/500` was reevaluated directly in the
original gate.  It is rank-two PSD, strictly dangerous, and satisfies the
strict legal scale inequality.  Its gate is

\[
 \mathcal G(Q)=
 \frac{414461983319631411704949}{112939929245000000000}>0,
\]

but

\[
 4\{\mathcal G(Q)-\mathcal G(\operatorname{Re}Q)\}
 =-\frac{585660171418319979}{375732500000000}<0,
\]

and the product of the two retained imaginary coordinates is `-279/100`.
The proof therefore does not discard the cyclic phase or use the rejected
real-part monotonicity, absorption, or universal-allocation routes.

## 8. Exact method ceiling and the `1/402` failure

The referee computed every centre-margin/absolute-derivative ratio for both
cells and all eight groups.  The unique finite minimum is the lower-cell
`N_D` ratio

\[
 \rho_*=
 \frac{
 2445449940734330377430367888331112726580165404046699831281174594544000
 }{
 983572318963523249183141112132550562552170261009318405958248648546787789
 },
\]

and exact cross multiplication proves

\[
 \frac1{403}<\rho_*<\frac1{402}.
\]

Thus `1/403` is the largest reciprocal-integer radius for which this fixed
**eight-sign package** proves all eight signs.  At `1/402`, the lower-cell
`N_D` derivative reserve is exactly

\[
 -\frac{
 54657263927145682718521091555313864896870775497413042370594307870877001
 }{
 20582400000000000000000000000000000000000000000000
 }<0.
\]

All other cell/group derivative reserves remain strictly positive at
`1/402`.  The displayed negative rational is `m-M/402`, an absolute-bound
certificate reserve; it is not a Bernstein control at a realizable parameter
point and is not an evaluation of `mathcal G`.  No exact negative original
gate is produced.  Moreover `N_D` is a consistency check, not needed after
`N0,N1` and convexity have established monotone positivity.  Therefore the
source is correct to classify the `1/402` number only as a certificate
failure.  For editorial precision, “method ceiling” should continue to mean
the ceiling of this eight-sign package, not a proved ceiling for the gate's
positive region.

## 9. Execution and trust boundary

The full normal run exited `0` after independently reconstructing the two
centre tensors and the new derivative layer.  It printed all six required
`PASS` lines.  Separate executed regressions gave nonzero exit status for:

- `python -O` (immediate fail-closed `RuntimeError`);
- a deliberately injected bad dependency hash.

The verifier uses exact `sympy.Rational` arithmetic.  No numerical optimizer,
floating-point sign, or cached builder sign table enters an acceptance
decision.  No proof assistant was used.

Final scope classification: **exact computer-assisted partial theorem** on
the displayed seven-real-parameter family and every legal scale.  It does
not settle arbitrary active blocks, the unrestricted complex Hermitian gate,
the common-metric theorem, or the fixed crossing-lens problem.
