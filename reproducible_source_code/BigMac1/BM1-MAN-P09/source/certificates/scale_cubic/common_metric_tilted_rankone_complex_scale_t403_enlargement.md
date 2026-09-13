# An enlarged derivative-certified active-block `t` layer

Date: 2026-08-23.  Status: **exact source-verified computer-assisted partial
theorem; independent referee audit still required**.  The unrestricted
complex Hermitian gate and the fixed crossing-lens problem remain open.

This theorem strictly enlarges the audited interval in
`common_metric_tilted_rankone_complex_scale_tthinbox_theorem.md`.  It uses
the same two independently audited `t=4` center cells, but it recomputes the
entire original Hermitian gate, all eight derivative majorants, and every new
reserve in exact rational arithmetic.

Fix

\[
 a=\frac35,\qquad c=\frac45,
\]

and let

\[
\begin{gathered}
8\le\ell\le10,\qquad -\frac{31}{100}\le w\le-\frac{29}{100},\\
-\frac{301}{100}\le k\le-\frac{299}{100},\qquad
-\frac{101}{100}\le z\le-\frac{99}{100},\\
\frac{99}{100}\le r\le\frac{103}{100},\qquad
\boxed{\frac{1611}{403}\le t\le\frac{1613}{403}}.
                                                               \tag{0.1}
\end{gathered}
\]

The new `t` interval is exactly

\[
                 4-\frac1{403}\le t\le4+\frac1{403}.
\]

Because `1/403>1/500`, it strictly contains the former certified interval
`[1999/500,2001/500]`; its half-width is larger by the exact factor
`500/403`.

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

## 1. Exact legality and the full scale half-line

The eight strict signs certified below include `Delta>0` and `n>0`.
Consequently the active `2 x 2` block is positive definite and the scalar
Schur complement in (0.2) vanishes.  Thus `Q` is Hermitian PSD of rank two.
Reconstruction with a free middle diagonal entry gives

\[
 q_{\min}=\frac{Tn}{\Delta},\qquad q_g=g.
\]

The complete strict branch is therefore

\[
 T>0\quad(g\le0),\qquad
 T>\frac{\Delta g}{n}\quad(g>0).                   \tag{1.1}
\]

No scale is sampled or truncated.  The result below holds at the finite
closed endpoint and at every point of the entire legal positive half-line.
The danger scalar is also strictly negative:

\[
 \operatorname{Re}(Qp)_1=\frac35r+\frac45z<0.
\]

## 2. Original-gate scale cubic

The fail-closed verifier starts from the fully conjugated Hermitian scalar
gate, forms `Q^2`, and proves symbolically that

\[
        4\Delta^2\mathcal G(Q)
        =P(T)=C_0+C_1T+C_2T^2+n^2T^3.             \tag{2.1}
\]

When `g>0`, let `T_L=Delta*g/n`.  The endpoint, derivative, and discriminant
normalizations are

\[
 P(T_L)=\frac{N_0}{15625n^2},\qquad
 P'(T_L)=\frac{N_1}{625n},\qquad
 -\operatorname{Disc}_T P=\frac{N_D}{244140625}. \tag{2.2}
\]

The eight controlling polynomials are

\[
 -\operatorname{Re}(Qp)_1,\quad\Delta,\quad n,\quad C_0,\quad C_1,
 \quad N_0,\quad N_1,\quad N_D.                  \tag{2.3}
\]

For `g<=0`, positivity of `C0,C1` and

\[
 C_2=\Delta^2(k^2+\ell^2)-2\Delta gn>0
\]

makes every coefficient of (2.1) positive.  For `g>0`, (2.2), (2.3), and

\[
 C_2+3n^2T_L=\Delta^2(k^2+\ell^2)+\Delta gn>0
\]

show that the strictly convex cubic increases from a positive endpoint.
The separately certified `N_D>0` excludes tangency and is a consistency
check.

## 3. Exact derivative certificate on the enlarged interval

The `r` range is the union of the already audited closed center cells

\[
 [99/100,101/100]\quad\text{and}\quad[101/100,103/100].
\]

For every polynomial `p` in (2.3), those center theorems give an exact
five-axis lower bound `p(4)>=m`.  On the wider box `399/100<=t<=401/100`,
the verifier expands `partial_t p` in powers of all six shape variables and
proves the exact monomial majorant `|partial_t p|<=M`.  Hence

\[
 p(t)\ge m-\frac{M}{403}.                         \tag{3.1}
\]

For each sign group, the least new reserve across both stitched `r` cells is:

| sign | exact least reserve at half-width `1/403` |
|---|---:|
| danger | `87/500` |
| `Delta` | `5725107/2015000` |
| `n` | `1173052317/4030000` |
| `C0` | `168031168212372292987/503750000000000000` |
| `C1` | `473798761153505578829/503750000000000000` |
| `N0` | `53688775478983631337804470500482797123/128960000000000000000000000` |
| `N1` | `10834008694368493232491091993/64480000000000000000` |
| `ND` | `211896779612896328421389008272777422300367253543677239239053722934418999/20633600000000000000000000000000000000000000000000` |

Every entry is strictly positive.  Thus the original gate is strictly
positive for every shape in (0.1) and every legal scale in (1.1).

## 4. Exact ceiling of this derivative method

Among all sixteen center-margin/derivative ratios, the unique limiting one
is `ND` on the lower `r` cell.  Its exact safe radius is

\[
\rho_*=
\frac{
2445449940734330377430367888331112726580165404046699831281174594544000
}{
983572318963523249183141112132550562552170261009318405958248648546787789
}.
\]

Exact cross multiplication gives

\[
                    \boxed{\frac1{403}<\rho_*<\frac1{402}}.   \tag{4.1}
\]

Therefore `1/403` is the largest half-width of the reciprocal-integer family
`1/d` certified by this fixed center-margin/absolute-derivative method.  At
`1/402`, its lower-cell `ND` reserve equals

\[
-\frac{
54657263927145682718521091555313864896870775497413042370594307870877001
}{
20582400000000000000000000000000000000000000000000
}<0.
\]

This last negative number is only a failure of the derivative certificate.
It is not a negative Bernstein control of a full tensor and, crucially, not
a negative value of the original Hermitian gate.

## 5. Phase integrity and scope

The previously audited exact witness at `t=2001/500`, which lies strictly
inside the enlarged interval, has

\[
4\{\mathcal G(Q)-\mathcal G(\operatorname{Re}Q)\}
=-\frac{585660171418319979}{375732500000000}<0,
\]

while `mathcal G(Q)>0`, and its two imaginary coordinates have product
`-279/100`.  Hence the proof neither discards the cyclic complex phase nor
uses real-part monotonicity, automatic phase absorption, or the universal
`s=-2` allocation rejected by CE-046, CE-048, and CE-059.

This is a strict enlargement of one local seven-real-parameter island.  It
does not prove arbitrary active blocks, the unrestricted complex Hermitian
gate, the common-metric theorem, or the fixed crossing-lens constant.  The
source verifier found no exact legal negative of the original gate in this
class.

