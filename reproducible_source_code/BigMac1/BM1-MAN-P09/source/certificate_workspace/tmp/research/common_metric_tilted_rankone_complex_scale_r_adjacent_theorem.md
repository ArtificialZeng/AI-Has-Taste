# The adjacent rational active-block `r` layer

Date: 2026-08-23.  Status: **exact independently audited computer-assisted
partial theorem**.  The unrestricted complex Hermitian gate and fixed
crossing-lens problem remain open.

Fix `a=3/5`, `c=4/5`, `t=4`, and let

\[
\begin{gathered}
8\le\ell\le10,\quad -31/100\le w\le-29/100,\\
-301/100\le k\le-299/100,\quad -101/100\le z\le-99/100,\\
101/100\le r\le103/100.
\end{gathered}                                      \tag{0.1}
\]

Define

\[
\Delta=4r-z^2-w^2,\qquad
n=4(k^2+\ell^2)+r-2(kz+\ell w),\qquad
g=\frac{12}{25}\ell-zk-w\ell-4.                  \tag{0.2}
\]

For `T>0` and `s=sqrt(T)`, put

\[
Q=\begin{pmatrix}
r&s(k+i\ell)&z+iw\\
s(k-i\ell)&Tn/\Delta&s\\
z-iw&s&4
\end{pmatrix}.                                     \tag{0.3}
\]

## Original gate, PSD boundary, and legal scales

The exact certificate below proves `Delta>0` and `n>0`.  Therefore the
active block indexed by `(1,3)` is positive definite.  Direct inversion
gives

\[
q_{\min}=\frac{Tn}{\Delta},
\]

and the scalar Schur complement vanishes, so `Q` is positive semidefinite of
rank exactly two.  The dangerous scalar is strictly negative:

\[
\operatorname {Re}(Qp)_1=\frac35r+\frac45z<0.     \tag{1.1}
\]

Reconstruction with a free middle diagonal entry gives `q_g=g`, and

\[
q_{\min}-q_g=\frac{Tn-\Delta g}{\Delta}.           \tag{1.2}
\]

Consequently the complete strict legal scale half-line is

\[
T>0\quad(g\le0),\qquad
T>\frac{\Delta g}{n}\quad(g>0).                   \tag{1.3}
\]

Expanding the original fully conjugated Hermitian gate—not a real-part
surrogate—gives the exact cubic

\[
4\Delta^2\mathcal G(Q)=P(T)=C_0+C_1T+C_2T^2+n^2T^3.              \tag{1.4}
\]

At the formal positive-`g` endpoint `T_L=Delta*g/n`, write

\[
P(T_L)=\frac{N_0}{15625n^2},\qquad
P'(T_L)=\frac{N_1}{625n},\qquad
-\operatorname {Disc}_T P=\frac{N_D}{244140625}.  \tag{1.5}
\]

All of `-Re(Qp)_1`, `Delta`, `n`, `C0`, `C1`, `N0`, `N1`, and `ND`
have strictly positive Bernstein controls on (0.1).  For `g<=0`,

\[
C_2=\Delta^2(k^2+\ell^2)-2\Delta gn>0,             \tag{1.6}
\]

so every coefficient of `P` is positive.  For `g>0`, the value and first
derivative at `T_L` are positive, while

\[
C_2+3n^2T_L=\Delta^2(k^2+\ell^2)+\Delta gn>0.      \tag{1.7}
\]

Thus `P''(T)>0` on `T>=T_L`; `P'` remains positive and `P` increases
strictly from a positive closed endpoint.  The separately certified
negative discriminant excludes an unrecorded tangency.  Hence the original
gate is strictly positive at the endpoint and on the complete legal
half-line, with no equality.

## Exact five-axis certificate

The direct exact power-to-Bernstein computation gives 734,288 strictly
positive rational controls:

| polynomial | five-degree | controls | least control |
|---|---:|---:|---:|
| danger margin | `(0,0,0,1,1)` | 4 | `87/500` |
| `Delta` | `(0,2,0,2,1)` | 18 | `14619/5000` |
| `n` | `(2,1,2,1,1)` | 72 | `1456853/5000` |
| `C0` | `(0,6,0,6,4)` | 245 | `448500662246821401/1250000000000000` |
| `C1` | `(2,6,2,6,3)` | 1764 | `1261378431909517593/1250000000000000` |
| `N0` | `(5,10,5,10,6)` | 30492 | `4642466069575661682742742534193063/10000000000000000000000` |
| `N1` | `(4,7,4,7,4)` | 8000 | `3637314850248595682332957/20000000000000000` |
| `ND` | `(10,20,10,20,12)` | 693693 | `18942501765434648654554516142706963646914690725542726020966050250291/3200000000000000000000000000000000000000000` |

The source verifier recomputes these controls directly from the original
power coefficients.  The isolated referee independently extracts `P` anew
from the original gate, evaluates all exact rational tensor nodes, inverts all
five Bernstein collocation axes, and reconstructs every node without
importing the source or discovery scripts.  Both exact runs exit with code
zero and print all four required PASS lines.

## Genuine adjacent-layer phase witness

At

\[
\ell=9,\quad w=-31/100,\quad k=-301/100,\quad z=-101/100,
\quad r=103/100,\quad T=1,
\]

one has

\[
\Delta=\frac{15019}{5000},\quad
n=\frac{1803851}{5000},\quad
g=\frac{699}{10000},\quad
q=\frac{1803851}{15019}>g,
\]

and `Re(Qp)_1=-19/100`.  Exact evaluation gives

\[
\mathcal G(Q)=\frac{82806323094723125611}{22557036100000000}>0,
\]

but

\[
4\{\mathcal G(Q)-\mathcal G(\operatorname {Re}Q)\}
=-\frac{234143982116037}{150190000000}<0.          \tag{3.1}
\]

The two imaginary coordinates have product `-279/100`.  Thus the proof does
not use CE-046, CE-048, CE-059, or the old same-sign phase cone.

This is only the adjacent five-dimensional shape box plus every legal scale.
It does not cover arbitrary active blocks, arbitrary complex directions,
unbalanced densities, higher rank or dimension, arbitrary nodes, or the
fixed crossing-lens constant.  No manuscript or PDF package is claimed.
