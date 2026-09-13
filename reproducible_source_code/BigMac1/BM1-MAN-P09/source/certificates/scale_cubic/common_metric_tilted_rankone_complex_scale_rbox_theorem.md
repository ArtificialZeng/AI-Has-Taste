# A rational active-block `r` layer for the complex scale cubic

Date: 2026-08-23.  Status: **exact independently audited computer-assisted
partial theorem**.  The unrestricted complex Hermitian gate and fixed
crossing-lens problem remain open.

Fix (a=3/5,c=4/5,t=4), and let

\[
\begin{gathered}
8\le\ell\le10,\quad -31/100\le w\le-29/100,\\
-301/100\le k\le-299/100,\quad -101/100\le z\le-99/100,\\
99/100\le r\le101/100.
\end{gathered}                                      \tag{0.1}
\]

Define

\[
\Delta=4r-z^2-w^2,\quad
n=4(k^2+\ell^2)+r-2(kz+\ell w),\quad
g=\frac{12}{25}\ell-zk-w\ell-4.                  \tag{0.2}
\]

For (T>0,s=\sqrt T), put

\[
Q=\begin{pmatrix}
r&s(k+i\ell)&z+iw\\
s(k-i\ell)&Tn/\Delta&s\\
z-iw&s&4
\end{pmatrix}.                                     \tag{0.3}
\]

## Exact legal half-line and scale cubic

The certificate below proves (\Delta,n>0), so the active block is positive
definite.  Direct inversion gives zero scalar Schur complement, hence (Q)
is positive semidefinite of rank exactly two.  Moreover

\[
\operatorname {Re}(Qp)_1=\frac35r+\frac45z<0.     \tag{1.1}
\]

Reconstruction at an arbitrary scalar completion gives (q_g=g), while

\[
q_{\min}=\frac{Tn}{\Delta},\qquad
q_{\min}-q_g=\frac{Tn-\Delta g}{\Delta}.           \tag{1.2}
\]

Thus the complete strict branch is

\[
T>T_L,\qquad T_L=0\ (g\le0),\qquad
T_L=\Delta g/n\ (g>0).                            \tag{1.3}
\]

Starting from the original fully conjugated gate gives

\[
4\Delta^2\mathcal G(Q)=P(T)=C_0+C_1T+C_2T^2+n^2T^3.              \tag{1.4}
\]

For the formal positive-(g) endpoint define

\[
P(T_L)=\frac{N_0}{15625n^2},\quad
P'(T_L)=\frac{N_1}{625n},\quad
-\operatorname {Disc}_T P=\frac{N_D}{244140625}.  \tag{1.5}
\]

All of (-\operatorname {Re}(Qp)_1,\Delta,n,C_0,C_1,N_0,N_1,N_D)
are strictly positive on (0.1).  If (g\le0), all cubic coefficients are
positive because

\[
C_2=\Delta^2(k^2+\ell^2)-2\Delta gn>0.             \tag{1.6}
\]

If (g>0), the shifted endpoint and derivative are positive, and

\[
C_2+3n^2T_L=\Delta^2(k^2+\ell^2)+\Delta gn>0.      \tag{1.7}
\]

Hence the shifted cubic increases strictly from a positive endpoint; its
negative discriminant also excludes tangency.  The original gate is strictly
positive at every legal scale and at the closed endpoint, with no equality.

## Exact five-axis certificate

All 734,288 exact tensor Bernstein controls are strictly positive:

| polynomial | five-degree | controls | least control |
|---|---:|---:|---:|
| danger margin | `(0,0,0,1,1)` | 4 | `93/500` |
| `Delta` | `(0,2,0,2,1)` | 18 | `14219/5000` |
| `n` | `(2,1,2,1,1)` | 72 | `1456753/5000` |
| `C0` | `(0,6,0,6,4)` | 245 | `420515573041543529/1250000000000000` |
| `C1` | `(2,6,2,6,3)` | 1764 | `1195599356262447793/1250000000000000` |
| `N0` | `(5,10,5,10,6)` | 30492 | `544257743489740893611366179477411/1250000000000000000000` |
| `N1` | `(4,7,4,7,4)` | 8000 | `3448220588099013077412457/20000000000000000` |
| `ND` | `(10,20,10,20,12)` | 693693 | `16659627721252625696244381239255705449827376815068142600603001925331/3200000000000000000000000000000000000000000` |

The source verifier uses direct exact interval-to-Bernstein conversion from
the original power coefficients.  The isolated referee extracts the cubic
from the original gate, recovers the five-axis controls from exact rational
nodes by collocation inversion, and reconstructs all nodes.

## Phase witness and scope

At

\[
\ell=9,\ w=-31/100,\ k=-301/100,\ z=-101/100,
\ r=99/100,\ T=1,
\]

one has

\[
\Delta=\frac{14219}{5000},\quad n=\frac{1803651}{5000},\quad
g=\frac{699}{10000},\quad q=\frac{1803651}{14219}>g.
\]

Exact evaluation gives

\[
\mathcal G(Q)=\frac{82629943031775348959}{20217996100000000}>0,
\]

but

\[
4\{\mathcal G(Q)-\mathcal G(\operatorname {Re}Q)\}
=-\frac{1176241596854997}{710950000000}<0.         \tag{3.1}
\]

The imaginary coordinates have opposite signs.  Thus CE-046, CE-048, and
the old phase cone are not used.

This is a five-dimensional shape box plus every legal scale.  It does not
cover arbitrary active blocks or directions, the feasible-center branch,
unbalanced densities, higher rank or dimension, arbitrary nodes, or the
fixed crossing-lens constant.  No manuscript or PDF package is claimed.
