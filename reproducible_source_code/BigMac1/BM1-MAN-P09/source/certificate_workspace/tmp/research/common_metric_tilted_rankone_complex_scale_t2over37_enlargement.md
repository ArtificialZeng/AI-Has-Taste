# A seven-sign active-block `t` layer of radius `2/37`

Date: 2026-08-24. Status: **exact source-verified computer-assisted partial
theorem; independent referee audit accompanies this note**. The unrestricted
complex Hermitian gate, the common-metric theorem, and the fixed
crossing-lens problem remain open.

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
 \boxed{\frac{146}{37}\leq t\leq\frac{150}{37}}.
                                                               \tag{0.1}
\end{gathered}
\]

Thus `|t-4|<=2/37`, strictly enlarging the frozen independently audited
radius `1/19` theorem.

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

## 1. Exact statement and legal scales

Throughout the closed box, `Delta,n>0` and

\[
 \operatorname{Re}(Qp)_1=\frac35r+\frac45z<0,
 \qquad p=(3/5,0,4/5)^{\mathsf T}.                    \tag{1.1}
\]

The active `(1,3)` block is positive definite and the scalar Schur
complement of (0.2) vanishes. Hence `Q` is Hermitian PSD of rank two. With a
free middle diagonal entry, the exact complementary strict branch is

\[
 T>0\quad(g\leq0),\qquad
 T>\frac{\Delta g}{n}\quad(g>0).                     \tag{1.2}
\]

For every datum (0.1) and every `T` in (1.2), the original complex Hermitian
scalar gate satisfies

\[
                         \mathcal G(Q)>0.             \tag{1.3}
\]

The proof also establishes positivity at the closure endpoint `T=0` when
`g<=0` and at `T_L=Delta*g/n` when `g>0`.

## 2. Original-gate cubic and complete terminal DAG

Starting from the fully conjugated original gate and independently checking a
real-residual square decomposition gives

\[
 4\Delta^2\mathcal G(Q)
 =P(T)=C_0+C_1T+C_2T^2+n^2T^3,                       \tag{2.1}
\]

where

\[
 C_2=\Delta^2(k^2+\ell^2)-2\Delta gn.                \tag{2.2}
\]

At `T_L=Delta*g/n`, define

\[
 P(T_L)=\frac{N_0}{15625n^2},\qquad
 P'(T_L)=\frac{N_1}{625n}.                           \tag{2.3}
\]

The proof uses exactly the following seven terminal sign groups:

```text
danger, Delta, n                         -> legality
Delta, n, C0, C1 and (2.2)              -> g<=0
Delta, n, N0, N1                        -> g>0 endpoint
Delta, n and curvature identity         -> g>0 curvature
```

For `g<=0`, every coefficient in (2.1) is positive. For `g>0`, `P(T_L)`
and `P'(T_L)` are positive, while

\[
 C_2+3n^2T_L=\Delta^2(k^2+\ell^2)+\Delta gn>0.       \tag{2.4}
\]

Thus `P''(T)>0` on `T>=T_L` and `P` increases from a positive endpoint.
This closes every legal scale and uses neither a discriminant nor `N_D`.

## 3. New-box derivative certificate

The `r` interval is stitched exactly from

\[
 [99/100,101/100]\quad\text{and}\quad[101/100,103/100],
\]

including their common seam. The exact `t=4` minima of all seven signs in
both cells are supplied by the frozen independently audited center theorem.
From the original six-variable sign polynomials, the verifier recomputes the
absolute power-monomial bounds `|partial_t p|<=M` on the full new box
`146/37<=t<=150/37`:

| sign | exact new `M` |
|---|---:|
| danger | `0` |
| `Delta` | `103/100` |
| `n` | `1090601/10000` |
| `C0` | `744128529196165565221/633162500000000000` |
| `C1` | `4126672805275222029427/633162500000000000` |
| `N0` | `1775215308784565826159975640142805255396523/221900662400000000000000000000` |
| `N1` | `146616757232077940451518475621/81044800000000000000` |

For `q=2/37`, every exact reserve `m-qM` is strictly positive:

| cell | sign | exact reserve |
|---|---|---:|
| low | danger | `93/500` |
| low | `Delta` | `515803/185000` |
| low | `n` | `2640463/9250` |
| low | `C0` | `639288181047879148809969/2342701250000000000000` |
| low | `C1` | `1415411124077141012291273/2342701250000000000000` |
| low | `N0` | `304944185165887347790739852577939707794093/102629056360000000000000000000000` |
| low | `N1` | `699275403702571484222111483263/9370805000000000000000` |
| high | danger | `87/500` |
| high | `Delta` | `530603/185000` |
| high | `n` | `1320324/4625` |
| high | `C0` | `691736743817931930675361/2342701250000000000000` |
| high | `C1` | `1538691702270928995729073/2342701250000000000000` |
| high | `N0` | `3264808470772680758250345288696777589889993/102629056360000000000000000000000` |
| high | `N1` | `196968419140925613831803445847/2342701250000000000000` |

The unique finite bottleneck for these recomputed new-box majorants is the
low-cell `N0` ratio

\[
 \rho_{\rm new}=
 \frac{2415423075934055837934601667899895734740928}
 {44380382719614145653999391003570131384913075},     \tag{3.1}
\]

with `2/37<rho_new<1/18`. More importantly, direct exact comparison with the
frozen radius ceiling gives

\[
 \frac1{19}<\frac2{37}<
 \frac{86248707481421051963533451880821625580096}
 {1582706318973118826676839520618941084666525}.       \tag{3.2}
\]

The frozen ceiling in (3.2) is used only for the requested comparison. It is
not extrapolated beyond its original derivative box; all derivative
majorants used for (0.1) were recomputed on the wider box.

## 4. Complex-phase and nonredundancy checks

The phase product remains uniformly opposite and nonzero:

\[
 -\frac{31}{10}\leq\ell w\leq-\frac{58}{25}<0.       \tag{4.1}
\]

At the new upper endpoint take

\[
 \ell=9,\ w=-31/100,\ k=-301/100,\ z=-101/100,
 \ r=103/100,\ t=150/37,\ T=1.
\]

Then

\[
 \Delta=\frac{566003}{185000},\quad
 n=\frac{8455386}{23125},\quad g=\frac{5863}{370000},
\]

and `q_min-g=25024624084411/209421110000>0`. Direct evaluation gives

\[
 \mathcal G(Q)=
 \frac{159584437542119281978612371}
 {43857201313632100000000}>0,                         \tag{4.2}
\]

but

\[
 4\{\mathcal G(Q)-\mathcal G(\operatorname{Re}Q)\}
 =-\frac{12024664566834413421}{7748581070000000}<0.  \tag{4.3}
\]

Thus both complex phases remain live and real-part monotonicity is not used.
The scale-free active-block shape derivative has exact lower margin
`10271/14800>0`, so changing `t` is not a hidden common rescaling.

## 5. Falsification and scope

The independent verifier attacks all 96 endpoint combinations of
`ell,w,k,z,t` and the three stitched `r` values. It checks the legal branch,
the relevant endpoint gate and slope, and a direct original-gate evaluation
at `T=1`. This finite attack is diagnostic; the fourteen reserve inequalities
prove the continuum theorem.

Run

```text
.venv/bin/python -B \
  tmp/research/verify_common_metric_tilted_rankone_complex_scale_t2over37_enlargement.py
```

The verifier uses exact rational symbolic arithmetic, imports no discovery
code, starts from the original Hermitian gate, and fails closed under
optimized Python, a bad dependency, or a dropped terminal sign.

This is a seven-real-parameter partial theorem: six bounded shape coordinates
and every legal coupling scale. It does not cover arbitrary active blocks,
arbitrary phase directions, the feasible-center branch, unbalanced
densities, higher rank or dimension, arbitrary nodes, the common-metric
theorem, or the fixed crossing-lens constant.
