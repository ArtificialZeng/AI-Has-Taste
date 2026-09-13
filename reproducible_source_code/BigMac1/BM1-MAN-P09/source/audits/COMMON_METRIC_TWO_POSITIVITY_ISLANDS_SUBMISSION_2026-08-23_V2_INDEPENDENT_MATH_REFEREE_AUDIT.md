# Independent mathematical referee audit: revised two-island manuscript

Date: 2026-08-23  
Verdict: **PASS with no fatal or major mathematical issue.**

Audited manuscript:

```text
tmp/release/common_metric_two_positivity_islands_submission_2026-08-23-v2/main.tex
SHA-256 cc57547a6b1c3e3547f5a82f858bfb08e6dcbf8e311ccabb4498943c4b906098
```

This verdict is limited to the mathematical consistency of the two revised
partial theorems, their exact data, and their stated logical scope.  It is not
peer review of the unrestricted common-metric problem and does not imply
journal acceptance.

## 1. Trust boundary and independent checks

I did not reuse the old manuscript referee verdict and did not run the long
`t403` tensor verifier.  I checked the revised text against the new source and
isolated-referee snapshots:

```text
tmp/research/common_metric_tilted_rankone_complex_scale_t403_enlargement.md
  206551077ae5999cf454620aabdbbed62d648bdf84e8907a716aa7e4c19f1f6c
tmp/research/verify_common_metric_tilted_rankone_complex_scale_t403_enlargement.py
  ae76c2868c797a5521b15d2c42fd0dfe2746ac70fbca7122b145da95b4f22a74
audit/verify_common_metric_tilted_rankone_complex_scale_t403_enlargement_referee.py
  b439d7ff59698c7eb3f5f470d322378a8497ea64cc813efb5b6484a171193575

tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_adjacent_x_layer.md
  95028dc46a177a8e856200eaba3f954086d6b4335aef34efac6be09783e39e92
tmp/research/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_adjacent_x_layer.py
  1095e6811abaac380b3650e162bf9e061c7e3ab547b07f92772601993f5c6e0c
audit/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_adjacent_x_layer_independent.py
  e793ae55e0ed30f862ca20101aa8c2b54080f78219ad97ecbd97fbfcc751a6a5
```

The six packaged copies in `certificates/scale_cubic/` and
`certificates/moving_sheet/` are byte-identical to these workspace files.

As a separate lightweight reconstruction, I started from the fully
conjugated Hermitian matrix

\[
Q=\begin{pmatrix}
r&s(k+i\ell)&z+iw\\
s(k-i\ell)&s^2n/\Delta&s\\
z-iw&s&t
\end{pmatrix}
\]

and the original scalar gate.  Exact symbolic arithmetic independently
confirmed:

1. Hermiticity, `det Q=0`, the Schur value `s^2 n/Delta`, and the danger
   scalar `(3/5)r+(4/5)z`;
2. the free-middle-entry center
   `g=(12/25)ell-zk-w ell-t` and
   `q_min-q_g=(Tn-Delta g)/Delta`;
3. the identity
   `4 Delta^2 gate=P(T)` with no odd coupling powers;
4. `C2=Delta^2(k^2+ell^2)-2 Delta g n`; and
5. the endpoint curvature identity
   `C2+3n^2 T_L=Delta^2(k^2+ell^2)+Delta g n`.

I also independently recomputed the rational interval extrema used in the
moving-sheet legality proof and checked every wrapped integer string in the
appendix against the audited values.

## 2. Theorem A: enlarged all-scale island

The manuscript uses exactly the audited closed shape box

\[
8\le\ell\le10,\quad -31/100\le w\le-29/100,\quad
-301/100\le k\le-299/100,
\]
\[
-101/100\le z\le-99/100,\quad 99/100\le r\le103/100,
\quad 1611/403\le t\le1613/403.
\]

The endpoints equal `4-1/403` and `4+1/403`, and this interval strictly
contains the former radius `1/500`.  The two closed `r` cells meet at
`r=101/100`, so the text introduces no stitch gap.

The legal strict scale branch is stated correctly:

\[
T>0\quad(g\le0),\qquad T>\Delta g/n\quad(g>0).
\]

For `T>0`, the certified strict signs `Delta,n>0` make the active block
positive definite and the Schur-boundary matrix positive semidefinite of rank
exactly two.  For `g<=0`, positivity of `C0,C1` and `C2` makes every cubic
coefficient positive.  For `g>0`, positive `N0,N1` and positive endpoint
curvature make the cubic increase strictly from a positive finite endpoint.
Thus the complete unbounded legal half-line, `g=0`, and both closure endpoint
types are handled without scale sampling.  The theorem itself retains the
strict branch; the closure statement is correctly made only for the cleared
polynomial.

All eight appendix reserves `danger, Delta, n, C0, C1, N0, N1, ND` match the
isolated referee audit digit for digit.  In particular, the wrapped `ND`
numerator concatenates to

```text
211896779612896328421389008272777422300367253543677239239053722934418999
```

with the correct positive denominator.

The manuscript's method-ceiling statement is also correctly limited.  It
says that `1/403` is maximal only for the fixed reciprocal-integer derivative
method and explicitly says that the negative sufficient reserve at `1/402`
is not a negative original-gate value.  It therefore does not promote the
`1/402` method failure to a counterexample.

## 3. Theorem B: merged positive-Z moving sheet

The merged theorem retains every required quantifier:

```text
0<S<=1/10000,
0<=X<=1/31,
|M|<=1/1000,
|omega|,|nu|<=1/100.
```

The moving map, including `lambda=(1+M)/S`, `y0`, `wc`, `Y`, `W_sh`, `Z`,
`x`, and `y`, agrees exactly with the source and referee artifacts.  Exact
independent interval arithmetic reproduced

```text
46999/100100 <= y0 <= 16333/33300,
wc+omega >= 79093/114700,
Z >= 3X-X^2 + S*(237033451226441/343755900000000) > 0,
Z <= 3005268611/31031000000 < 1/8,
1-x^2-y^2-Z >= 8886607262249/17222205000000 > 1/2.
```

Here the displayed upper bound on `Z` is a valid deliberately coarse bound:
it drops both negative squares and uses `3X<=3/31`.  The compression has
leading entry `S>0` and determinant `(5/9)SZ>0`; with `lambda>0`, the
constructed Hermitian matrix is PSD of rank exactly two.  The ball identity
then gives strict danger.  The gate depends on the signed coordinate through
`Z=z^2`, so both signs of `z` are legitimately included.

The projective divisions are legal and cover every endpoint:

- `X=0` is handled only by predecessor chart C0, which divides by `S^2`;
- the predecessor and adjacent closed cells both contain `X=3/10000`;
- on the adjacent cell, `0<S<=1/10000<3/10000<=X`, so division by `X^2`
  and `S=X sigma` are lossless;
- `X=1/31` is included by the strict exact margin; and
- `S=0` is explicitly excluded because `lambda=(1+M)/S` is undefined.

The appendix copies all five `B_d` values and the predecessor C0, predecessor
C1, and adjacent-C1 exact margins correctly.  In particular, the adjacent
margin concatenates to

```text
42950357876463827039627477692165648038556445276911579
/984800872161607680000000000000000000000000 > 0.
```

The manuscript makes no gate claim at `X=1/30`; consequently it does not
mislabel the audited negative inherited remainder bound there.  The source
and referee artifacts correctly classify that number only as failure of a
sufficient absolute-remainder certificate, not as a gate counterexample.

## 4. Normalizations and scope

The manuscript consistently distinguishes

```text
gate = mathcal G,
Gamma = 4 gate,
Delta^2 Gamma = 4 Delta^2 gate = P,
36 Gamma = 144 gate.
```

No denominator-clearing sign is lost: `Delta>0` on the scale branch and
`D=25^8(1+M)^8>0`, `S>0` on the moving sheet.  The abstract, theorem
statements, logical-scope remark, unresolved-problem section, and disclosure
all retain the status **partial theorem**.  They explicitly do not claim the
unrestricted Hermitian gate, the common-metric assertion, arbitrary-node
bridges, or the fixed crossing-lens constant.  Numerical diagnostics are not
used as proofs, and no proof-assistant claim is made.

## 5. Clean lightweight build

A clean temporary-directory `latexmk` build from only `main.tex` and
`references.bib` succeeded.  Final output:

```text
15 pages
442711 bytes
no undefined references or citations
no overfull boxes
one non-substantive underfull-vbox notice on page 12
PDF title and author metadata correct
```

## Final classification

**PASS: exact computer-assisted partial theorem manuscript.**  No fatal or
major mathematical correction is required for the revised `t403` and
adjacent-`X` statements.
