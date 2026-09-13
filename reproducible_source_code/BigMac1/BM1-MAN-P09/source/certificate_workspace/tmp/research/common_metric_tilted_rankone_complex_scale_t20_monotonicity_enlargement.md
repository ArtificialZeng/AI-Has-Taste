# A seven-sign active-block `t` layer of radius `1/20`

Date: 2026-08-24.  Status: **exact source-verified computer-assisted partial
theorem; independent referee audit still required**.  The unrestricted
complex Hermitian gate, the common-metric theorem, and the fixed
crossing-lens problem remain open.

This theorem strictly enlarges the independently audited radius `1/100`
layer.  It uses only the seven sign groups in the terminal proof DAG.  The
cubic discriminant and `N_D` are neither formed nor assumed.

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
 \boxed{\frac{79}{20}\leq t\leq\frac{81}{20}}.
                                                               \tag{0.1}
\end{gathered}
\]

Thus `|t-4|<=1/20`.  It enlarges the audited `1/100` radius by the exact
factor `5`.

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

The certificate gives `Delta,n>0` throughout the closed box.  Since
`r>=99/100`, the active block indexed by `(1,3)` is positive definite.
Its scalar Schur complement vanishes exactly, so `Q` is Hermitian PSD of
rank two.  With a free middle diagonal entry,

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
endpoint `T_L=Delta*g/n` when `g>0`.  The dangerous scalar is uniformly
strict:

\[
 \operatorname{Re}(Qp)_1=\frac35r+\frac45z<0.         \tag{1.3}
\]

The phase domain also stays genuinely complex and opposite-phase:

\[
 -\frac{31}{10}\leq \ell w\leq-\frac{58}{25}<0.       \tag{1.4}
\]

For every positive coupling scale, the product of the two imaginary matrix
coordinates is therefore `s*ell*w<0`.

## 2. Original-gate scale cubic and terminal DAG

The fail-closed verifier starts from the fully conjugated original gate,
forms `Q^2`, and independently reproduces the same polynomial from the two
real residual squares.  It obtains

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

If `g<=0`, every coefficient of `P` is positive.  If `g>0`, `P(T_L)` and
`P'(T_L)` are positive, while `P''(T)` is positive and strictly increasing
on `T>=T_L`.  Thus `P` increases from a positive endpoint.  This exhausts
all legal scales and closure endpoints.  No discriminant branch remains.

## 3. Exact seven-sign radius test

The `r` interval is stitched from the two independently audited `t=4`
center cells

\[
 [99/100,101/100]\quad\text{and}\quad[101/100,103/100].
\]

For each of

\[
 -\operatorname{Re}(Qp)_1,\ \Delta,\ n,\ C_0,\ C_1,\ N_0,\ N_1,           \tag{3.1}
\]

the center certificate supplies `p(4)>=m`.  The verifier recomputes from the
six-variable power coefficients—without extrapolating the radius `1/100`
majorants—the exact absolute power-monomial bounds `|partial_t p|<=M` on
the full target box `79/20<=t<=81/20`:

| sign | exact new `M` |
|---|---:|
| danger | `0` |
| `Delta` | `103/100` |
| `n` | `1090601/10000` |
| `C0` | `7330309783059851/6250000000000` |
| `C1` | `162718802887612103/25000000000000` |
| `N0` | `102031510952390678261878426882374421/12800000000000000000000` |
| `N1` | `11554426319351381788185663/6400000000000000` |

Among all finite ratios from the fourteen cell/sign pairs, the unique
minimum is lower-cell `N0`:

\[
 \rho_*=\min_{M>0}\frac mM
 =\frac{
 139329982333373668764509741946217216
 }{
 2550787773809766956546960672059360525
 },                                                     \tag{3.2}
\]

and exactly

\[
                  \frac1{19}<\rho_*<\frac1{18}.         \tag{3.3}
\]

Thus the requested radius `1/20` is strictly below the newly recomputed
necessary-reserve ceiling.  Since `1/20<rho_*`, the mean-value estimate

\[
                         p(t)\geq m-\frac M{20}         \tag{3.4}
\]

is strictly positive for every sign and both cells.

The exact radius-`1/20` reserves are:

| cell | sign | exact reserve |
|---|---|---:|
| low | danger | `93/500` |
| low | `Delta` | `27923/10000` |
| low | `n` | `57179519/200000` |
| low | `C0` | `347212475210945019/1250000000000000` |
| low | `C1` | `1577604698086835071/2500000000000000` |
| low | `N0` | `47162374571541283748646833372996759/1280000000000000000000000` |
| low | `N1` | `52570927222411509536270309/640000000000000000` |
| high | danger | `87/500` |
| high | `Delta` | `28723/10000` |
| high | `n` | `57183519/200000` |
| high | `C0` | `375197564416222891/1250000000000000` |
| high | `C1` | `1709162849380974671/2500000000000000` |
| high | `N0` | `84078102143731304081678909964839959/1280000000000000000000000` |
| high | `N1` | `58621943611198152893726309/640000000000000000` |

No derivative-majorant tightening or one-dimensional `t` subdivision is
needed to reach this endpoint.  Any continuation past radius `1/20` must
first certify derivatives on a larger `t` domain; equation (3.2) alone may
not be extrapolated beyond the box on which `M` was proved.

## 4. Endpoint phase integrity

At the new upper endpoint, take

\[
 \ell=9,\quad w=-31/100,\quad k=-301/100,\quad z=-101/100,
 \quad r=103/100,\quad t=81/20,\quad T=1.
\]

Then

\[
 \Delta=\frac{30553}{10000},\qquad
 n=\frac{73054641}{200000},\qquad
 g=\frac{199}{10000},
\]

and the datum lies strictly inside the legal scale branch.  Direct
original-gate evaluation gives

\[
 \mathcal G(Q)=\frac{679782423179948045013}{186697161800000000}>0,          \tag{4.1}
\]

whereas

\[
 4\{\mathcal G(Q)-\mathcal G(\operatorname{Re}Q)\}
 =-\frac{948596098430067}{611060000000}<0.                                \tag{4.2}
\]

The two imaginary coordinates have product `-279/100`.  Hence both complex
phases remain live at the new endpoint.  The proof uses neither CE-046/048
absorption nor the CE-059 fixed allocation.

## 5. Verification and scope

Run

```text
.venv/bin/python -B \
  tmp/research/verify_common_metric_tilted_rankone_complex_scale_t20_monotonicity_enlargement.py
```

The verifier uses exact rational symbolic arithmetic, imports no discovery
code, binds every center and reduction dependency by SHA-256, and fails
closed under optimized Python, a malformed dependency, or a missing terminal
sign group.

This is a seven-real-parameter island: six bounded shape coordinates and
every legal coupling scale.  It does not cover arbitrary active blocks,
arbitrary phase directions, the feasible-center branch, unbalanced
densities, higher rank or dimension, arbitrary nodes, the common-metric
theorem, or the fixed crossing-lens constant.
