# A derivative-certified active-block `t` layer

Date: 2026-08-23.  Status: **exact independently audited computer-assisted
partial theorem**.  The unrestricted complex Hermitian gate and the fixed
crossing-lens problem remain open.

This result depends explicitly on the two independently audited `t=4`
center theorems on the closed `r` cells `[99/100,101/100]` and
`[101/100,103/100]`.  It does not recompute or enlarge their 734,288-control
five-axis tensors.

Fix `a=3/5`, `c=4/5`, and let

\[
\begin{gathered}
8\le\ell\le10,\quad -31/100\le w\le-29/100,\\
-301/100\le k\le-299/100,\quad -101/100\le z\le-99/100,\\
99/100\le r\le103/100,\quad
1999/500\le t\le2001/500.                         \tag{0.1}
\end{gathered}
\]

The `r` interval in (0.1) is the union of the two closed center cells above.
Define

\[
\Delta=rt-z^2-w^2,quad
n=t(k^2+\ell^2)+r-2(kz+\ell w),quad
g=\frac{12}{25}\ell-zk-w\ell-t.                 \tag{0.2}
\]

For `T>0`, `s=sqrt(T)`, put

\[
Q=\begin{pmatrix}
r&s(k+i\ell)&z+iw\\
s(k-i\ell)&Tn/\Delta&s\\
z-iw&s&t
\end{pmatrix}.                                    \tag{0.3}
\]

## 1. The coordinate is normalized and nonredundant

The coupling scale `T` changes the normalized coupling column, whereas `t`
changes the active block

\[
R=\begin{pmatrix}r&z+iw\\z-iw&t\end{pmatrix}.
\]

Even after quotienting a common positive scalar on `R`, its spectral-shape
invariant `(r+t)/sqrt(Delta)` has `t`-derivative with the sign of

\[
rt-r^2-2(z^2+w^2).
\]

On the wider box `399/100<=t<=401/100` this numerator is at least
`461/625>0`.  Thus the new coordinate is not the old coupling scale or a
common active-block rescaling.  Scaling the whole datum is not an invariance
of the original gate because its fully conjugated formula contains both the
fixed term `a*c` and entries of `Q^2`.

## 2. Original gate, PSD boundary, and legal scale

The signs proved below give `Delta,n>0`.  The active block is positive
definite, its scalar Schur complement in (0.3) vanishes, and `Q` is PSD of
rank exactly two.  Reconstruction with a free middle diagonal entry gives

\[
q_{\min}=\frac{Tn}{\Delta},\qquad q_g=g,qquad
q_{\min}-q_g=\frac{Tn-\Delta g}{\Delta}.           \tag{2.1}
\]

Therefore the complete strict legal scale half-line is

\[
T>0\quad(g\le0),\qquad
T>\frac{\Delta g}{n}\quad(g>0).                   \tag{2.2}
\]

The dangerous scalar remains strictly negative:

\[
\operatorname {Re}(Qp)_1=\frac35r+\frac45z<0.     \tag{2.3}
\]

Expansion of the original fully conjugated Hermitian gate gives

\[
4\Delta^2\mathcal G(Q)
=P(T)=C_0+C_1T+C_2T^2+n^2T^3.                    \tag{2.4}
\]

At the formal positive-`g` endpoint `T_L=Delta*g/n`, define

\[
P(T_L)=\frac{N_0}{15625n^2},\qquad
P'(T_L)=\frac{N_1}{625n},\qquad
-\operatorname {Disc}_T P=\frac{N_D}{244140625}. \tag{2.5}
\]

## 3. Exact derivative bridge from the audited center

Let the eight sign polynomials be

\[
-\operatorname {Re}(Qp)_1,\ \Delta,\ n,\ C_0,\ C_1,\ N_0,\ N_1,\ N_D.
\]

For any one of them, call it `p`, and either closed `r` cell, the audited
`t=4` theorem supplies a pointwise lower bound `p(4)>=m`, where `m` is its
least five-axis Bernstein control.  On the wider derivative box
`399/100<=t<=401/100`, write the power expansion of `partial_t p` in the six
variables.  Replacing each monomial by the product of the coordinate absolute
bounds gives an exact rational majorant `M` for `|partial_t p|`.  Since the
target box is contained in the wider box, the mean value theorem gives

\[
p(t)\ge p(4)-|t-4|\sup|\partial_t p|
\ge m-\frac1{500}M.                              \tag{3.1}
\]

The exact derivative term counts, majorants, and smaller reserve across the
two `r` cells are:

| `p` | derivative terms | exact `M` | minimum reserve `m-M/500` |
|---|---:|---:|---:|
| danger margin | 1 | `0` | `87/500` |
| `Delta` | 1 | `103/100` | `142087/50000` |
| `n` | 2 | `1090601/10000` | `1455662399/5000000` |
| `C0` | 62 | `3591519308424373/3125000000000` | `2088211787974020153/6250000000000000` |
| `C1` | 67 | `32111117681043527/5000000000000` | `2359087594843852059/2500000000000000` |
| `N0` | 1851 | `98448296054638286971718220153709637/12800000000000000000000` | `2688151350612835088318476618770634683/6400000000000000000000000` |
| `N1` | 326 | `452887170660359886538671/256000000000000` | `108078622965866619044505269/640000000000000000` |
| `ND` | 84595 | `107209382767024034160962381222448011318186558450015706249449102691599869001/51200000000000000000000000000000000000000000000` | `26067639002996971408992668691597632280432456070529434555374912711048130999/25600000000000000000000000000000000000000000000000` |

All eight reserves are strictly positive.  This avoids the forbidden direct
six-axis tensor: its `ND` degree would be `(10,20,10,20,12,13)`, requiring
9,711,702 controls by itself and 9,975,375 controls in total.

## 4. Cubic sign partition

If `g<=0`, `C0,C1>0` and

\[
C_2=\Delta^2(k^2+\ell^2)-2\Delta gn>0,             \tag{4.1}
\]

so every coefficient of `P` is positive.  If `g>0`, (2.5) and the eight
reserves give a positive endpoint and endpoint derivative, while

\[
C_2+3n^2T_L=\Delta^2(k^2+\ell^2)+\Delta gn>0.      \tag{4.2}
\]

Thus `P''(T)>0` for `T>=T_L`, `P'` remains positive, and `P` increases from
a positive closed endpoint.  The certified negative discriminant is a
separate exact consistency check excluding tangency.  Hence the original
gate is strictly positive at the finite endpoint and on every legal scale,
with no equality.

## 5. Phase witness and scope

At

\[
\ell=9,\ w=-31/100,\ k=-301/100,\ z=-101/100,
\ r=103/100,\ t=2001/500,\ T=1,
\]

one has

\[
\Delta=\frac{150293}{50000},\quad
n=\frac{1804751601}{5000000},\quad
g=\frac{679}{10000},\quad
q=\frac{1804751601}{15029300}>g,
\]

and the danger scalar is `-19/100`.  Exact evaluation gives

\[
\mathcal G(Q)=
\frac{414461983319631411704949}{112939929245000000000}>0,
\]

whereas

\[
4\{\mathcal G(Q)-\mathcal G(\operatorname {Re}Q)\}
=-\frac{585660171418319979}{375732500000000}<0.
\]

The two imaginary coordinates have product `-279/100`.  The proof therefore
does not use CE-046, CE-048, CE-059, or the old same-sign phase cone.

This is only a thin `t` extension of the displayed six-real-parameter chart,
with every legal scale.  It does not cover arbitrary active blocks, arbitrary
complex directions, unbalanced densities, higher rank or dimension,
arbitrary nodes, or the fixed crossing-lens constant.  No manuscript or PDF
package is claimed.
