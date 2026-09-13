# A seven-sign active-block `t` layer of radius `1/19`

Date: 2026-08-24. Status: **exact source-verified computer-assisted partial
theorem; independent referee audit still required**. The unrestricted complex
Hermitian gate, the common-metric theorem, and the fixed crossing-lens problem
remain open.

This theorem strictly enlarges the independently audited radius `1/20` layer.
It uses only the seven sign groups in the terminal proof DAG. The cubic
discriminant and `N_D` are neither formed nor assumed.

Fix

\[
 a=\frac35,\qquad c=\frac45,
\]

and let

\[
\begin{gathered}
 8\leq\ell\leq10,\qquad -\frac{31}{100}\leq w\leq-\frac{29}{100},\\
 -\frac{301}{100}\leq k\leq-\frac{299}{100},\qquad
 -\frac{101}{100}\leq z\leq-\frac{99}{100},\\
 \frac{99}{100}\leq r\leq\frac{103}{100},\qquad
 \boxed{\frac{75}{19}\leq t\leq\frac{77}{19}}.
                                                               \tag{0.1}
\end{gathered}
\]

Thus `|t-4|<=1/19`, an exact enlargement of the radius `1/20` layer by
the factor `20/19`.

For `T>0`, put `s=sqrt(T)` and define

\[
\begin{aligned}
 \Delta&=rt-z^2-w^2,\\
 n&=t(k^2+\ell^2)+r-2(kz+\ell w),\\
 g&=\frac{12}{25}\ell-zk-w\ell-t,
\end{aligned}
\]

and

\[
 Q=\begin{pmatrix}
 r&s(k+i\ell)&z+iw\\
 s(k-i\ell)&Tn/\Delta&s\\
 z-iw&s&t
 \end{pmatrix}.                                      \tag{0.2}
\]

## 1. Exact legality and complete scale branch

The certificate gives `Delta,n>0` throughout the closed box. Since
`r>=99/100`, the active block indexed by `(1,3)` is positive definite. Its
scalar Schur complement vanishes exactly, so `Q` is Hermitian PSD of rank two.
With a free middle diagonal entry,

\[
 q_{\min}=\frac{Tn}{\Delta},\qquad q_g=g,
 \qquad q_{\min}-q_g=\frac{Tn-\Delta g}{\Delta}.       \tag{1.1}
\]

Therefore the complete strict complementary branch is

\[
 T>0\quad(g\leq0),\qquad
 T>\frac{\Delta g}{n}\quad(g>0).                     \tag{1.2}
\]

The proof includes the closure endpoint `T=0` when `g<=0` and the finite
endpoint `T_L=Delta*g/n` when `g>0`. The dangerous scalar is uniformly strict:

\[
 \operatorname{Re}(Qp)_1=\frac35r+\frac45z<0.         \tag{1.3}
\]

The phase domain remains genuinely complex and opposite-phase:

\[
 -\frac{31}{10}\leq \ell w\leq-\frac{58}{25}<0.       \tag{1.4}
\]

For every positive coupling scale the product of the two imaginary matrix
coordinates is therefore `s*ell*w<0`.

The coordinate `t` is not spectrally redundant. On the full enlarged box,
`t-2r>=1793/950>0`; the exact shape-separation lower bound used by the
verifier is `1057/1520>0`.

## 2. Original-gate scale cubic and terminal DAG

The fail-closed verifier starts from the fully conjugated original gate, forms
`Q^2`, and independently reproduces the same polynomial from the two real
residual squares. It obtains

\[
 4\Delta^2\mathcal G(Q)
 =P(T)=C_0+C_1T+C_2T^2+n^2T^3,                       \tag{2.1}
\]

where

\[
 C_2=\Delta^2(k^2+\ell^2)-2\Delta gn.                \tag{2.2}
\]

At the formal positive-`g` endpoint `T_L=Delta*g/n`, define

\[
 P(T_L)=\frac{N_0}{15625n^2},\qquad
 P'(T_L)=\frac{N_1}{625n}.                           \tag{2.3}
\]

The curvature identity is

\[
 C_2+3n^2T_L
 =\Delta^2(k^2+\ell^2)+\Delta gn>0\qquad(g>0).       \tag{2.4}
\]

The terminal proof uses exactly

```text
danger, Delta, n                         -> legality
Delta, n, C0, C1 and (2.2)              -> g<=0
Delta, n, N0, N1                        -> g>0 endpoint
Delta, n and (2.4)                       -> g>0 curvature
```

If `g<=0`, every coefficient of `P` is positive. If `g>0`, `P(T_L)` and
`P'(T_L)` are positive, while `P''(T)` is positive and strictly increasing on
`T>=T_L`. Thus `P` increases from a positive endpoint. This exhausts all legal
scales and closure endpoints. No additional cubic branch remains.

## 3. Exact seven-sign radius test

The `r` interval is stitched from the two independently audited `t=4` center
cells

\[
 [99/100,101/100]\quad\text{and}\quad[101/100,103/100].
\]

For each of

\[
 -\operatorname{Re}(Qp)_1,\ \Delta,\ n,\ C_0,\ C_1,\ N_0,\ N_1,           \tag{3.1}
\]

the verifier reconstructs every exact nodal Bernstein control at `t=4`,
40,595 controls per cell, and recovers the independently audited minima. It
then recomputes from the original six-variable polynomials the exact absolute
power-monomial bounds `|partial_t p|<=M` on the full target box
`75/19<=t<=77/19`:

| sign | exact new `M` |
|---|---:|
| danger | `0` |
| `Delta` | `103/100` |
| `n` | `1090601/10000` |
| `C0` | `100691127533136076513/85737500000000000` |
| `C1` | `558534110200039372331/85737500000000000` |
| `N0` | `63308252758924753067073580824757643386661/7923516800000000000000000000` |
| `N1` | `19839330969499660813210417263/10974400000000000000` |

Among all finite ratios from the fourteen cell/sign pairs, the unique minimum
is lower-cell `N0`:

\[
 \rho_*=\min_{M>0}\frac mM
 =\frac{86248707481421051963533451880821625580096}
 {1582706318973118826676839520618941084666525},       \tag{3.2}
\]

and exactly

\[
                  \frac1{19}<\rho_*<\frac1{18}.       \tag{3.3}
\]

Thus the requested radius lies strictly below the newly recomputed reserve
ceiling, and the mean-value estimate

\[
                         p(t)\geq m-\frac M{19}        \tag{3.4}
\]

is strictly positive for every sign and both cells. The exact reserves are:

| cell | sign | exact reserve |
|---|---|---:|
| low | danger | `93/500` |
| low | `Delta` | `265011/95000` |
| low | `n` | `54266013/190000` |
| low | `C0` | `44732897241033386591509/162901250000000000000` |
| low | `C1` | `99958292687474521598453/162901250000000000000` |
| low | `N0` | `56019123173881160630296065116669801355299/3763670480000000000000000000000` |
| low | `N1` | `402767836285811446192677185819/5212840000000000000000` |
| high | danger | `87/500` |
| high | `Delta` | `272611/95000` |
| high | `n` | `54269813/190000` |
| high | `C0` | `48379942051354404148421/162901250000000000000` |
| high | `C1` | `108530687604876305004253/162901250000000000000` |
| high | `N0` | `164564931073235573503759030399341098721499/3763670480000000000000000000000` |
| high | `N1` | `452053742961002955504366146819/5212840000000000000000` |

No derivative-majorant tightening or rational subdivision is needed at this
endpoint. The ratio (3.2) may not be extrapolated beyond the derivative box on
which its `M` values were proved.

## 4. Endpoint phase integrity

At the new upper endpoint, take

\[
 \ell=9,\quad w=-31/100,\quad k=-301/100,\quad z=-101/100,
 \quad r=103/100,\quad t=77/19,\quad T=1.
\]

Then

\[
 \Delta=\frac{290511}{95000},\qquad
 n=\frac{69446939}{190000},\qquad
 g=\frac{3281}{190000},
\]

and

\[
 q_{\min}-g=\frac{6596506038409}{55197090000}>0.
\]

Thus the datum lies strictly inside the legal scale branch. Direct
original-gate evaluation gives

\[
 \mathcal G(Q)=
 \frac{11088710761166761635176131}{3046718744468100000000}>0,             \tag{4.1}
\]

whereas

\[
 4\{\mathcal G(Q)-\mathcal G(\operatorname{Re}Q)\}
 =-\frac{180854568847307917}{116527190000000}<0.                           \tag{4.2}
\]

The determinant is exactly zero and the two imaginary coordinates have
product `-279/100`. Hence both complex phases remain live at the new endpoint;
discarding them would change the gate in the wrong direction.

## 5. Verification and scope

Run

```text
.venv/bin/python -B \
  tmp/research/verify_common_metric_tilted_rankone_complex_scale_t19_monotonicity_enlargement.py
```

The verifier uses exact rational symbolic arithmetic, imports no discovery
code, reconstructs both center tensors, binds every center and reduction
dependency by SHA-256, and fails closed under optimized Python, a malformed
dependency, or a missing terminal sign group.

This is a seven-real-parameter island: six bounded shape coordinates and every
legal coupling scale. It does not cover arbitrary active blocks, arbitrary
phase directions, the feasible-center branch, unbalanced densities, higher
rank or dimension, arbitrary nodes, the common-metric theorem, or the fixed
crossing-lens constant.
