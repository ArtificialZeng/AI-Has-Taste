# Polynomial reduction of the full complex Schur-boundary gate

Date: 2026-08-18.  Status: **exact reduction; the resulting polynomial
positivity remains open**.

Let \(a,c>0\), \(a^2+c^2=1\), \(p=(a,0,c)^T\), and, after fixing the
middle-coordinate phase, write

\[
 Q=\begin{pmatrix}
 r&u+iv&z+iw\\
 u-iv&q&s\\
 z-iw&s&t
 \end{pmatrix},\qquad s>0,                         \tag{0.1}
\]

with all scalar parameters real.  Assume the strict active Schur chart

\[
 r>0,\qquad
 \Delta:=rt-z^2-w^2>0,                             \tag{0.2}
\]

and the dangerous sign

\[
 x:=ar+cz<0.                                       \tag{0.3}
\]

The scalar gate \(\mathcal G(Q)\) is the left side minus the right side of

\[
\begin{aligned}
 a^2|\xi_2|^2
 &+\frac14\left|c\overline{\xi_1}+a\xi_3+
 i\{ac-(Q^2)_{31}\}\right|^2\\
 &+\frac14\left|c\overline{\xi_2}-i(Q^2)_{32}\right|^2
 \geq8a^2(\operatorname {Re}\xi_1)^2,\qquad \xi=Qp.
                                                               \tag{0.4}
\end{aligned}
\]

## 1. Exact Schur boundary and branch condition

In the active order \(\{1,3\}\mid\{2\}\), the active block and coupling are

\[
 R=\begin{pmatrix}r&z+iw\\z-iw&t\end{pmatrix},
 \qquad h=(u+iv,s)^T.
\]

Put

\[
 N=t(u^2+v^2)+rs^2-2s(uz+vw).                     \tag{1.1}
\]

Then

\[
 q_{\min}=h^*R^{-1}h=\frac N\Delta,                \tag{1.2}
\]

and \(Q(q_{\min})\succeq0\) has rank two.  The unconstrained scalar-gate
minimizer is

\[
 q_0=\frac{acv-zu-wv-ts}{s}.                       \tag{1.3}
\]

Define

\[
 H_0=acv-zu-wv-ts,\qquad
 J=sN-\Delta H_0.                                  \tag{1.4}
\]

Since \(s,\Delta>0\),

\[
 \boxed{\quad q_{\min}>q_0\quad\Longleftrightarrow\quad J>0.\quad}
                                                               \tag{1.5}
\]

Thus \(J>0\) is the exact polynomial description of the complementary
Schur-boundary branch.

## 2. Cleared gate polynomial

Introduce the real residuals

\[
\begin{aligned}
 L&=au+cs,\\
 R_1&=ac(r+t)+z-w(r+t)-sv,\\
 I_1&=ac-w-z(r+t)-su,\\
 R_2&=cL+zv-wu.                                    \tag{2.1}
\end{aligned}
\]

Direct multiplication at \(q=q_{\min}\) gives

\[
\begin{aligned}
 |\xi_2|^2&=L^2+a^2v^2,\\
 \left|c\overline{\xi_1}+a\xi_3+
 i\{ac-(Q^2)_{31}\}\right|^2&=R_1^2+I_1^2,\\
 \left|c\overline{\xi_2}-i(Q^2)_{32}\right|^2
 &=R_2^2+\frac{J^2}{\Delta^2}.                    \tag{2.2}
\end{aligned}
\]

Consequently the full two-phase boundary gate is exactly

\[
\boxed{
\begin{aligned}
 4\Delta^2\mathcal G(Q(q_{\min}))
 ={}&\Delta^2\Bigl[
 4a^2(L^2+a^2v^2)+R_1^2+I_1^2+R_2^2-32a^2x^2
 \Bigr]+J^2.
                                                               \tag{2.3}
\end{aligned}}
\]

No phase, \(Q^2\) term, or Schur-boundary penalty has been discarded.
Therefore the open branch \(q_0<q_{\min}\) on the strict active chart is
equivalent to nonnegativity of the polynomial on the right of (2.3) under

\[
 a,c,r,s,\Delta>0,\quad a^2+c^2=1,\quad x<0,\quad J>0.          \tag{2.4}
\]

The final \(J^2\) is precisely the cost of forcing the scalar completion
from its unconstrained gate minimizer to the PSD boundary.  The bracket in
(2.3) is not asserted to be nonnegative termwise.

## 3. Exact two-phase calibration

For

\[
\begin{gathered}
 a=\frac35,\quad c=\frac45,\quad
 r=1,\quad t=4,\quad z=-1,\quad w=-\frac3{10},\\
 u=-\frac3{10},\quad v=\frac9{10},\quad s=\frac1{10},
\end{gathered}
\]

one obtains

\[
\Delta=\frac{291}{100},\quad
N=\frac{901}{250},\quad
q_{\min}=\frac{1802}{1455},\quad
q_0=\frac1{50},\quad
J=\frac{17729}{50000}>0.                           \tag{3.1}
\]

The original-order matrix \(Q(q_{\min})\) is positive semidefinite with
leading principal minors

\[
 1,\qquad \frac{197}{582},\qquad0,
\]

and \(x=-1/5\).  Direct evaluation gives

\[
 \mathcal G(Q(q_{\min}))
 =\frac{226444674193}{21170250000}>0.              \tag{3.2}
\]

This datum checks the simultaneous nonzero phases and the branch direction;
it is not evidence sufficient to prove (2.3) nonnegative in general.

## 4. Scope

Equation (2.3) is a bounded exact target for the full two-complex-phase
Schur-boundary branch.  It neither proves nor disproves the scalar gate.
The singular active-block boundary \(\Delta=0\), the feasible-interior
branch, the common-metric theorem, and the fixed crossing-lens constant are
outside this note.

