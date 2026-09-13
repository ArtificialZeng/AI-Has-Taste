# Independent mathematical transcription audit: v3 submission after t20 promotion

Date: 2026-08-24.

Target:

```text
tmp/release/common_metric_two_positivity_islands_submission_2026-08-24-v3
```

## Verdict

**PASS as an exact transcription of two computer-assisted partial theorems.**

No fatal, major, or minor discrepancy was found in the updated `main.tex` or
`README.md`.  The t20 all-scale theorem, its exact rational data, the unchanged
five-cell moving-sheet theorem, all displayed normalization factors, and all
replay filenames agree with their independently audited authorities.

This verdict does not prove the unrestricted complex Hermitian gate, the
common-metric assertion, the full compact-ball theorem, or the optimal fixed
crossing-lens constant.  Those problems remain open.  Per the audit remit,
the temporarily stale `RELEASE_MANIFEST.sha256` was not used as a failure
criterion; it must be regenerated after the release files and this report are
frozen.

The exact files reviewed in this pass have SHA-256 values

```text
main.tex
  0a3119fbd1ecca3ef6bb08951b8df11b4e6174ea7d2b62831c4132365782cbbc
README.md
  3a0948f05b0d966a4e9171b23dd458df852e2548be402272cd9272f4db4a359d
common_metric_tilted_rankone_complex_scale_t20_monotonicity_enlargement.md
  bfd4ffb334a57a3bd73d6694c4ff267d9c1a5d8a0bb6d1bcb5b18b6fd2794b57
COMMON_METRIC_TILTED_RANKONE_COMPLEX_SCALE_T20_MONOTONICITY_REFEREE_AUDIT.md
  b6a0ad44759fdc8462d2cdd57e5a8a89fcc4f96744f4eb6b733f6c51469d625a
```

## 1. Trust boundary and method

Theorem A was compared line by line with

```text
tmp/research/common_metric_tilted_rankone_complex_scale_t20_monotonicity_enlargement.md
audit/COMMON_METRIC_TILTED_RANKONE_COMPLEX_SCALE_T20_MONOTONICITY_REFEREE_AUDIT.md
```

Theorem B was rechecked against the predecessor, adjacent, next-sigma,
reciprocal-endpoint, and cross-cap source statements and their independent
audits.  These five closed cells cover

```text
[0,3/10000], [3/10000,1/31], [1/31,1/30],
[1/30,1/24], [1/24,1/23].
```

The t20 and moving-sheet statement/audit copies in `certificate_workspace/`
are byte-identical to the workspace authorities.  The individual manifests
named by the README all pass.  This was an adversarial transcription audit:
the source/referee programs remain the authorities for the large exact tensor
computations, while their decisive outputs and every manuscript integer were
independently compared here.

## 2. Theorem A: t20 transcription

### 2.1 Quantifiers, branch, rank, and danger

The manuscript has exactly the audited bounded shape box

```text
a=3/5, c=4/5,
8 <= ell <= 10,
-31/100 <= w <= -29/100,
-301/100 <= k <= -299/100,
-101/100 <= z <= -99/100,
99/100 <= r <= 103/100,
79/20 <= t <= 81/20.
```

It therefore states `|t-4|<=1/20`, not the superseded radius `1/100`.
The complete strict complementary branch is copied without loss:

```text
T>0                    if g<=0,
T>Delta*g/n            if g>0.
```

The matrix `Q_A(T)`, `Delta`, `n`, and `g` agree with the source.  The
positive active block and its zero Schur complement give Hermitian PSD rank
two for every stated `T>0`, and

```text
Re(Q_A p_A)_1=(3/5)r+(4/5)z<0
```

is the exact strict-danger condition.  The text correctly distinguishes the
strict geometric family from positivity of the cleared polynomial at the
closure endpoint `T=T_L`.

### 2.2 Normalization and terminal proof graph

The global convention is consistent everywhere:

```text
Gamma=4*mathcal G,
Delta^2*Gamma=4*Delta^2*mathcal G=P(T),
36*Gamma=144*mathcal G.
```

The endpoint numerators retain the audited factors

```text
N0=15625*n^2*P(T_L),
N1=625*n*P'(T_L).
```

The terminal DAG uses exactly the seven essential sign groups

```text
danger, Delta, n, C0, C1, N0, N1.
```

No discriminant numerator is used in Theorem A.  The two terminal branches
are complete: coefficient positivity closes `g<=0`; endpoint value,
endpoint derivative, and the displayed curvature identity close `g>0` on
the whole legal half-line.

### 2.3 Counts, derivative bridge, and reserves

The two `r` cells are

```text
[99/100,101/100], [101/100,103/100].
```

The displayed control counts satisfy

```text
4+18+72+245+1764+30492+8000=40595
```

per cell.  The text uses derivative majorants certified on the full new box
`79/20<=t<=81/20` and the exact mean-value loss

```text
m_f-M_f/20.
```

The t20 source and isolated referee both reproduce all fourteen cell/sign
reserves as strictly positive.  The appendix correctly prints the smaller
reserve across the two cells for each sign:

```text
danger  87/500
Delta   27923/10000
n       57179519/200000
C0      347212475210945019/1250000000000000
C1      1577604698086835071/2500000000000000
N0      47162374571541283748646833372996759
        /1280000000000000000000000
N1      52570927222411509536270309
        /640000000000000000
```

The unique finite-radius bottleneck is exactly lower-cell `N0`:

```text
rho_*=
139329982333373668764509741946217216
/2550787773809766956546960672059360525,

1/19 < rho_* < 1/18.
```

Thus `1/20<rho_*`.  The manuscript correctly refuses to extrapolate this
ratio beyond the box on which the t20 derivative bounds were proved.

### 2.4 Endpoint witness

The manuscript uses the audited upper-endpoint datum

```text
(ell,w,k,z,r,t,T)
=(9,-31/100,-301/100,-101/100,103/100,81/20,1).
```

Its displayed original-gate values match both source and referee exactly:

```text
mathcal G(Q)=
679782423179948045013/186697161800000000 > 0,

4*(mathcal G(Q)-mathcal G(Re Q))=
-948596098430067/611060000000 < 0.
```

The authority additionally verifies `Delta=30553/10000`,
`n=73054641/200000`, `g=199/10000`, and the imaginary-coordinate product
`-279/100`.  Hence the example is legal, genuinely complex, and not a
real-part-monotonicity proof.  The factor four in the second displayed value
is intentional and consistent with the manuscript normalization.

## 3. Theorem B: unchanged moving-sheet transcription

The merged quantified domain remains exactly

```text
0<S<=1/10000,
0<=X<=1/23,
|M|<=1/1000,
|omega|,|nu|<=1/100,
lambda*S=1+M in [999/1000,1001/1000].
```

The moving map and legality reserves agree with the independently audited
cross-cap source.  They imply

```text
lambda>0, 0<Z<1/7, x^2+y^2+Z<1,
det(compression)=(5/9)SZ>0,
```

so the datum is strictly dangerous and `Q_B` is PSD of rank exactly two for
either sign of `z` with `z^2=Z`.  `S=0` is correctly excluded because the
scale is then undefined; `X=0` is supplied by the predecessor C0 chart and
does not require division by `X`.

The five cells and their projective bounds are transcribed correctly:

```text
next cell        sigma<=31/10000,
reciprocal cell  sigma<=3/1000,
cross-cap cell   sigma<=3/1250.
```

On the last full interval `1/24<=X<=1/23`, `T=Z-1/8` is only a recentered
coordinate and is never divided out.  The source/referee exact witnesses on
opposite sides of `Z=1/8` therefore lie in one proved continuous band, not
in two pointwise patches.  The outer-box obstruction is also stated with the
correct strict attribution:

```text
y-1/2=1/10+S*y0>1/10,
```

which is a coordinate-coverage gap rather than a gate counterexample.

The cleared quotient normalization and sparse counts remain exact:

```text
N=S^3*(36*Gamma(Q_B)),
D=25^8*(1+M)^8,
Qhat=D*N/S^2,

20 (S,X) monomials,
16 higher terms,
947 centered parameter monomials.
```

All eleven moving-sheet appendix groups match their authorities digit for
digit: `B1,...,B5` and
`m_C0,m_C1,m_adj,m_next,m_rec,m_cross`.  Together with the seven t20 minima,
all eighteen displayed appendix data groups have the correct sign,
numerator, denominator, and wrapped-digit concatenation.

## 4. README and replay audit

No t100 verifier, note, or manifest name remains in `README.md`.  The README
uses the exact promoted t20 names

```text
verify_common_metric_tilted_rankone_complex_scale_t20_monotonicity_enlargement.py
verify_common_metric_tilted_rankone_complex_scale_t20_monotonicity_referee.py
common_metric_tilted_rankone_complex_scale_t20_monotonicity_enlargement_manifest.sha256
common_metric_tilted_rankone_complex_scale_t20_monotonicity_referee_manifest.sha256
```

and the correct next-sigma, reciprocal-endpoint, and cross-cap source/referee
names.  Every listed file exists at the stated repository-relative path in
`certificate_workspace/`.

All eight listed ordinary Python replay commands completed with exit status
zero from `certificate_workspace/`.  The t20 source and referee respectively
reported the full fourteen reserves and the independent `40595`-control
reconstruction; the moving-sheet programs reproduced the stated `20/16/947`
counts and exact strict margins.  All eight listed individual manifest
commands also passed.

Adversarial t20 checks were repeated on the distributed copies.  Both source
and referee reject `python -O` with nonzero status, and the referee rejects a
deliberately corrupted dependency hash.  The independent audit additionally
records fail-closed rejection when a terminal sign group is removed.

The README's prose accurately says that the promoted scale radius is `1/20`,
the moving sheet ends at `X=1/23`, the last cell crosses `Z=1/8` without
division, and neither theorem resolves the open global problems.

## 5. Final classification

```text
PASS -- exact computer-assisted partial-theorem transcription.
```

No manuscript or README edit is required by this mathematical audit.  No
proof assistant was used for either complex theorem.  This report makes no
claim about visual PDF layout and, by instruction, does not adjudicate the
pre-freeze release manifest.
