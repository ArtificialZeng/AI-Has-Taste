# Independent mathematical transcription audit: v4 submission at t19/X22

Date: 2026-08-24.

Target manuscript:

```text
tmp/release/common_metric_two_positivity_islands_submission_2026-08-24-v4/main.tex
```

## Verdict

**PASS as an exact manuscript transcription of the frozen t19 and X22
partial theorems.**

No fatal, major, or minor mathematical transcription discrepancy was found.
The theorem quantifiers, legal branches, normalization factors, displayed
endpoint witness, exact reserve data, X22 legality bounds, all seven
moving-sheet margins, and the scope disclaimers agree with the frozen source
and independent-referee authorities.

This is a manuscript-transcription verdict only.  It does not promote either
island to the unrestricted complex Hermitian gate, a common-metric theorem,
the full compact-ball theorem, an arbitrary-node theorem, or an optimal fixed
crossing-lens constant.  Those problems remain open.

There is one separate release-packaging blocker: the current
`RELEASE_MANIFEST.sha256` is stale.  In the release directory, `shasum -a 256
-c RELEASE_MANIFEST.sha256` fails on exactly `README.md`,
`audits/BIB_AUDIT.md`, `main.tex`, and `main.pdf`.  This did not change the
manuscript-transcription verdict, but the manifest must be regenerated after
the release and this audit are frozen before the directory is called a
verified release package.

The exact manuscript snapshot audited here has SHA-256

```text
fb318fb80a6e25e8735d8e9015de35c7f795dd46476ac1445bf75219157e5852  main.tex
```

## 1. Trust boundary and frozen authorities

The t19 statement was checked line by line against

```text
tmp/research/common_metric_tilted_rankone_complex_scale_t19_monotonicity_enlargement.md
audit/COMMON_METRIC_TILTED_RANKONE_COMPLEX_SCALE_T19_MONOTONICITY_REFEREE_AUDIT.md
audit/verify_common_metric_tilted_rankone_complex_scale_t19_monotonicity_referee.py
```

Their decisive hashes are

```text
211976602dbeaef10f0a49eb07c788957bf6f31b4c9673a53e0b28abf9a90195  source note
206d87cdf33b84fc5e84d1a17466c0919571ba9e16f999f19b3b2714b9796073  referee report
98e74e87f3b34711afdd2b3fab5951bf7ecd8a732340afc4baa3f8ec8a08fd3b  referee verifier
```

The X22 statement was checked line by line against

```text
tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x22_extension.md
audit/COMMON_METRIC_RANKTWO_TRANSVERSE_COMPACT_BALL_POSITIVE_Z_MOVING_SHEET_X22_EXTENSION_INDEPENDENT_REFEREE_AUDIT.md
audit/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x22_extension_independent_referee.py
```

Their decisive hashes are

```text
5189571fc3913b3ff41dde268d2ce47cd89b18568748d76378007a1e0667d06d  source note
e905d17eb05b6d135b81e281c19d3b6488e8bb53606a15c983923dbcf7fc1d25  referee report
12873ef0577c6576febe4e7703c90dacdef7533b03b177deae5bd0c78b5a1568  referee verifier
```

All four source/referee manifests pass from the workspace root.  The packaged
t19 and X22 source notes and referee verifiers are byte-identical to these
authorities.  No discovery program, cached tensor, or numerical sample was
used to decide this audit.

## 2. Theorem A: t19 transcription

### 2.1 Quantifiers, legal branch, rank, and danger

The manuscript states exactly the frozen box

```text
a=3/5, c=4/5,
8 <= ell <= 10,
-31/100 <= w <= -29/100,
-301/100 <= k <= -299/100,
-101/100 <= z <= -99/100,
99/100 <= r <= 103/100,
75/19 <= t <= 77/19.
```

The complete strict legal half-line is copied without change:

```text
T>0                    if g<=0,
T>Delta*g/n            if g>0.
```

The matrix `Q_A(T)`, the definitions of `Delta`, `n`, `g`, and the exact Schur
entry `T*n/Delta` agree with the frozen theorem.  The text correctly states
PSD rank two, strict danger, strict gate positivity on the legal half-line,
and positivity of the cleared polynomial at the closure endpoint.  It does
not include that closure point in the strict geometric branch.

### 2.2 Normalization and terminal proof graph

The global normalization is consistent throughout:

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

The terminal proof uses exactly the seven necessary sign groups

```text
danger, Delta, n, C0, C1, N0, N1.
```

The discriminant numerator from an older eight-sign route is explicitly
excluded from the terminal proof.  The two `r` cells are exactly
`[99/100,101/100]` and `[101/100,103/100]`.  The displayed control counts are

```text
4, 18, 72, 245, 1764, 30492, 8000,
```

which sum to `40595` theorem-relevant controls per cell, as in both frozen
authorities.

### 2.3 Derivative bridge, all fourteen reserves, and bottleneck

The derivative interval and loss are correctly transcribed as

```text
75/19 <= t <= 77/19,       f(t)>=m_f-M_f/19.
```

The frozen source has fourteen cell/sign reserves.  They are:

```text
low  danger  93/500
low  Delta   265011/95000
low  n       54266013/190000
low  C0      44732897241033386591509/162901250000000000000
low  C1      99958292687474521598453/162901250000000000000
low  N0      56019123173881160630296065116669801355299
              /3763670480000000000000000000000
low  N1      402767836285811446192677185819
              /5212840000000000000000

high danger  87/500
high Delta   272611/95000
high n       54269813/190000
high C0      48379942051354404148421/162901250000000000000
high C1      108530687604876305004253/162901250000000000000
high N0      164564931073235573503759030399341098721499
              /3763670480000000000000000000000
high N1      452053742961002955504366146819
              /5212840000000000000000
```

The appendix intentionally prints seven values: for each sign group it prints
the smaller of its two cell reserves.  Every one of those seven minima is the
correct minimum of the fourteen values above.  Thus the compressed appendix
is exact and does not omit a negative cell reserve.

The unique finite ratio bottleneck is correctly copied as the lower-cell
`N0` ratio

```text
rho_*=
86248707481421051963533451880821625580096
/1582706318973118826676839520618941084666525,

1/19 < rho_* < 1/18.
```

The manuscript correctly refuses to extrapolate this ratio to `1/18` or
beyond the derivative box on which its majorants were certified.

### 2.4 Exact endpoint witness

The displayed witness is exactly

```text
(ell,w,k,z,r,t,T)
=(9,-31/100,-301/100,-101/100,103/100,77/19,1).
```

Both displayed values match the frozen source and referee digit for digit:

```text
mathcal G(Q)=
11088710761166761635176131
/3046718744468100000000 > 0,

4*(mathcal G(Q)-mathcal G(Re Q))=
-180854568847307917/116527190000000 < 0.
```

The factor four is intentional under the manuscript normalization.  The
witness supports genuine complex-phase nonredundancy; it is not used as the
continuum proof.

## 3. Theorem B: X22 transcription

### 3.1 Quantified domain and map

The merged theorem domain is exactly

```text
0<S<=1/10000,
0<=X<=1/22,
|M|<=1/1000,
|omega|,|nu|<=1/100,
lambda*S=1+M in [999/1000,1001/1000].
```

Every term of the moving-sheet map (`lambda`, `y0`, `w_c`, `Y`, `W_sh`,
`Z`, `x`, and `y`) agrees with the frozen source.  The theorem correctly
allows either sign of `z` with `z^2=Z`, fixes `h=sqrt(S)`, and obtains rank
exactly two from the positive compression determinant `(5/9)SZ`.  It excludes
`S=0` because the scale is undefined there.

### 3.2 Exact legality bounds

The manuscript gives the audited bounds

```text
46999/100100 <= y0 <= 16333/33300,
0<Y<=16333/333000000,
w_c+omega >= 27743/40700,
w_c+omega-S*y0^2 >= 83142836564221/121977900000000,
Z <= 1479554991/11011000000 < 1/7,
1-x^2-y^2-Z >= 267603185879/555555000000,
det(compression)=(5/9)SZ>0.
```

These are the frozen theorem bounds.  The independent referee also found a
slightly sharper upper bound for `Z`, but explicitly validated the source's
displayed looser rational; using that audited looser value in the manuscript
is correct.

At `X=0`, strict `Z>0` is supplied by the predecessor chart, exactly as the
text says.  No division by `X`, `z`, `Z`, or `Z-1/8` is silently introduced.

### 3.3 Quadratic core, cells, and exact margins

The cleared expression, positive denominator, `S^2` divisibility, twenty
`(S,X)` monomials, bidegree `(5,4)`, and first layer

```text
25^8*M^2*S*(1+M)^8*(5*M^2+14*M+14)
```

all agree with the frozen sources.  The common quadratic reserve is

```text
c_*=
2564950982194530478444050838857341987999
/1274019840000000000000000000 > 0.
```

The predecessor source gives exact lower bounds for `a_2` and `b_2` larger
than this same `c_*`, while `c_2>=c_*`; hence the manuscript's compact
statement `a_2,b_2,c_2>=c_*` is valid.

The six stitched closed cells and their lossless projective data are correct:

```text
predecessor: 0<=X<=3/10000, with C0 and C1 charts;
adjacent:    3/10000<=X<=1/31;
next:        1/31<=X<=1/30, sigma<=31/10000;
reciprocal:  1/30<=X<=1/24, sigma<=3/1000;
cross-cap:   1/24<=X<=1/23, sigma<=3/1250;
X22:         1/23<=X<=1/22, sigma<=23/10000.
```

They meet at every displayed seam.  The occurrences of `1/23` in the
manuscript are therefore required X22 stitch data, not a stale theorem
endpoint.

All five `B_d` values and all seven exact projective margins in Appendix B
match their independently audited authorities digit for digit, including

```text
m_adj numerator =
42950357876463827039627477692165648038556445276911579

m_next numerator =
34580339142052196913279468445031671587443896471169689550375704523100547

m_rec numerator =
19666826464450448575286154539314661657460944445647100238594863919

m_cross numerator =
83854846318555455131346013627095055256473934297852585381468177735953

m_22 numerator =
33473277839430772291616341971402441279238321762300948743627232727876747.
```

The line-wrapped numerators and denominators concatenate to the exact frozen
integers.  The `m_22` denominator is

```text
16648891269120000000000000000000000000000000000000000000000.
```

The proof consistently identifies negative absolute-remainder bounds as a
method issue rather than an original-gate counterexample; no numerical grid
is promoted to a continuum theorem.

## 4. Stale-claim and scope audit

The current `main.tex` contains no `v3`, `t20`, `X23`, `79/20`, or `81/20`
promotion.  It does not state `X<=1/23` as the final moving-sheet domain.
The legitimate `1/23` occurrences are only the cross-cap/X22 seam and the
corresponding sigma bound.

The abstract calls the results partial scalar-gate theorems.  The logical
scope remark correctly separates scalar-gate positivity from selection of a
single metric.  The final scope section explicitly leaves open arbitrary
complex Hermitian `Q`, the complementary branch, the full positive-`Z`
collar and compact ball, arbitrary normalized scale, higher ranks and
dimension, the common metric, arbitrary-node bridges, and the fixed-lens
constant.  It also states that no sharpness conclusion is made.

The manuscript explicitly rejects floating-point signs, sampled minima, and
cached discovery polynomials as proof.  It does not claim a Lean or other
proof-assistant formalization of either complex theorem.  Diagnostic complex
endpoint values and cross-cap witnesses are kept separate from the exact
continuum certificates.

## 5. LaTeX and reference structure

A clean isolated build from only `main.tex` and `references.bib` completed
with

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

and produced a 15-page PDF.  The final log contains no undefined control
sequence, unresolved reference, unresolved citation, overfull box, or LaTeX
warning.  The separate source audit reported

```text
cited=5  bib=5  missing=0  unused=0.
```

The title, author, subject, and page metadata are present.  Text extracted
from the clean build is byte-identical to text extracted from the packaged
PDF.  The different PDF hashes are attributable to build metadata and are
not a content discrepancy.

## 6. Final determination

The v4 `main.tex` is an exact and appropriately scoped transcription of the
frozen t19 and X22 results.  The manuscript audit therefore passes.  The
release directory itself must not be called manifest-verified until its
stale four-entry release manifest is regenerated and rechecked.
