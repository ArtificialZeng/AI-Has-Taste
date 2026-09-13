# Independent referee audit: complex-scale radius `1/100`

Date: 2026-08-24.  Verdict: **PASS as an exact computer-assisted partial
theorem on the stated seven-real-parameter island**.  This audit does not
prove the unrestricted complex Hermitian gate, the common-metric theorem, or
the fixed crossing-lens constant.

Audited candidate:

- `tmp/research/common_metric_tilted_rankone_complex_scale_t100_monotonicity_enlargement.md`
- `tmp/research/verify_common_metric_tilted_rankone_complex_scale_t100_monotonicity_enlargement.py`
- `tmp/research/common_metric_tilted_rankone_complex_scale_t100_monotonicity_enlargement_manifest.sha256`

Independent referee:

- `audit/verify_common_metric_tilted_rankone_complex_scale_t100_monotonicity_referee.py`

## 1. Quantified endpoint audited

The audit proves the candidate exactly for

```text
a=3/5, c=4/5,
8 <= ell <= 10,
-31/100 <= w <= -29/100,
-301/100 <= k <= -299/100,
-101/100 <= z <= -99/100,
99/100 <= r <= 103/100,
399/100 <= t <= 401/100,
```

and every coupling scale `T` on the complete strict complementary legal
half-line

```text
T>0                         if g<=0,
T>Delta*g/n                 if g>0.
```

The closure endpoint is also positive in the coefficient or endpoint sense
used in the candidate proof.  The result is a local rank-two boundary chart;
it does not quantify over arbitrary active blocks, phases, ranks, dimensions,
or nodes.

## 2. Reconstruction independent of the candidate verifier

The referee imports no candidate code, old referee, discovery output, or
cached tensor.  It rebuilds from the fully conjugated original Hermitian gate:

1. Hermiticity, the active determinant `Delta`, the zero Schur complement,
   and rank-two determinant;
2. the strict danger scalar and the free-middle-diagonal center `q_g=g`;
3. the cubic `P(T)=4 Delta^2 G(Q)` by even coupling-power extraction;
4. the same cubic by an independent real-residual square decomposition;
5. the endpoint numerators `N0,N1` and the curvature identity.

Only the seven terminal sign groups

```text
danger, Delta, n, C0, C1, N0, N1
```

are formed.  No cubic-discriminant reserve is required.  The exact terminal
DAG covers legality, the `g<=0` coefficient branch, the `g>0` endpoint, and
the `g>0` curvature branch, hence the whole legal `T` half-line.

## 3. Independent center and derivative certificates

For each of the two stitched `r` cells

```text
[99/100,101/100], [101/100,103/100],
```

the referee converts every center polynomial at `t=4` directly from affine
power coefficients to its full tensor Bernstein basis.  It then inverts the
entire tensor back to the original power polynomial exactly.  This reconstructs
40,595 controls per cell, proves every control strictly positive, and matches
all seven claimed exact minima.

The wider six-variable derivative polynomials are independently expanded on
`399/100<=t<=401/100`.  The referee matches the seven exact term counts and
absolute monomial majorants, and verifies all fourteen reserves
`m-M/100>0`.  The unique finite-radius bottleneck is lower-cell `N0`:

\[
\rho_*=\frac{
139329982333373668764509741946217216
}{
2461207401365957174292955503842740925
},
\qquad \frac1{18}<\rho_*<\frac1{17}.
\]

Thus `1/100<rho_*`; the derivative certificate closes the claimed interval.
The earlier radius `1/402` is strictly contained.

## 4. Legality, nonredundancy, and complex phase

The exact center signs give `Delta,n>0`, while `r,t>0`; the Schur identity
therefore makes `Q` Hermitian PSD of rank two.  The sign of
`T*n-Delta*g` gives exactly the claimed legal scale branch.

Varying `t` is not hidden coupling rescaling or common active-block scaling.
For the scale-free active-block invariant `(r+t)/sqrt(Delta)`, the derivative
numerator has the exact box lower bound

\[
rt-r^2-2(z^2+w^2)\geq \frac{461}{625}>0.
\]

At the stated endpoint witness the audit independently obtains

```text
Delta=30141/10000,
n=361670801/1000000,
g=599/10000,
G(Q)=2304143350537886621/628705800000000 > 0,
4(G(Q)-G(Re Q))=-30685556925187/19700000000 < 0,
Im(Q12)*Im(Q13)=-279/100.
```

Hence both complex phases remain live; the proof does not replace the gate by
its real part or invoke any of the previously rejected absorption/allocation
routes.

## 5. Fail-closed execution

Environment used: Python 3.13.5, SymPy 1.13.3, Darwin arm64.

Normal exact run:

```text
/opt/anaconda3/bin/python3 -B \
  audit/verify_common_metric_tilted_rankone_complex_scale_t100_monotonicity_referee.py
```

returned, in part:

```text
PASS original fully conjugated gate, Schur boundary, and legal T half-line
PASS independent affine/Bernstein/inverse reconstruction: 40595 controls per cell
PASS seven derivative groups and all fourteen radius-1/100 reserves
PASS unique lower-r N0 bottleneck and 1/18 < rho_star < 1/17
PASS strict old-interval inclusion, spectral nonredundancy, and phase integrity
```

The following adversarial runs each failed closed with nonzero exit status:

```text
python -O                         -> rejected before verification
T100_REFEREE_TEST_BAD_DEPENDENCY=1 -> dependency hash mismatch
T100_REFEREE_TEST_DROP_SIGN=1      -> seven-sign DAG rejected
```

The ordinary verifier SHA-256 is

```text
11e65029b4a56b1a626e47f69c6f065cb9d366c01fb9c27387d37912fd27db29
```

No proof assistant was used.  The status is an exact source-and-referee
verified **partial theorem**, not a resolution of the unrestricted problem.
