# Exact singular-value asymptotics for the four frozen matrices

All variables below are real and (0<d=\delta\leq1).  Singular values are
ordered decreasingly.  The exact computation in `verify_asymptotics.py`
independently checks every displayed characteristic coefficient and limiting
polynomial.

## Exact characteristic polynomials

Write
\[
 \det(zI-X_i(d)^TX_i(d))=z^3-S_{1,i}(d)z^2+S_{2,i}(d)z-S_{3,i}(d).
\]
Exact rational expansion gives the following coefficients.

For (i=1),
\[
S_{1,1}=\frac{250d^4+1500d^3+29628d^2+82134d+123201}
 {13689d^2(d+3)^2},
\]
\[
S_{2,1}=\frac{d^4+6d^3+340d^2+486d+729}
 {13689d^2(d+3)^2},\qquad
S_{3,1}=\frac1{13689(d+3)^2}.
\]

For (i=2),
\[
S_{1,2}=\frac{207256033d^6+3730608594d^5+28044203733d^4
 +112693929156d^3+272094339780d^2+409886770176d+409886770176}
 {1265082624d^2(d+3)^2(d+6)^2},
\]
\[
S_{2,2}=\frac{93925d^6+1690650d^5+62315146d^4+1179452736d^3
 +8611859475d^2+24691257378d+30477601890}
 {632541312d^2(d+3)^2(d+6)^2},
\]
\[
S_{3,2}=\frac{25(d+9)^2(d+19)^2}
 {35141184d^2(d+3)^2(d+6)^2}.
\]

For (i=3),
\[
S_{1,3}=\frac{207256033d^4+3730608594d^3+26779121109d^2
 +89922441924d+124079672772}
 {1265082624(d+3)^2(d+6)^2},
\]
\[
S_{2,3}=\frac{187850d^4+3381300d^3+95628179d^2
 +1047613518d+3862824273}
 {1265082624(d+3)^2(d+6)^2},
\]
\[
S_{3,3}=\frac{25(17d+115)^2}{140564736(d+3)^2(d+6)^2}.
\]

For (i=4),
\[
S_{1,4}=\frac{250d^2+1500d+15939}{13689(d+3)^2},\quad
S_{2,4}=\frac{d^2+6d+259}{13689(d+3)^2},\quad
S_{3,4}=\frac1{13689(d+3)^2}.
\]

## Case 1: exact constant (27) and a full-interval error bound

Put (a=-1/9), (b=1/(3+d)), (t=1/d), and let
(lambda_+\geq\lambda_->0) be the squared singular values of
\(\begin{pmatrix}a&t\\0&b\end{pmatrix}\).  The third squared singular value
of (X_1) is (1/169).  We have
\[
t^2\leq\lambda_+\leq t^2+a^2+b^2\leq d^{-2}+10/81,
\]
and, because (lambda_+\lambda_-=a^2b^2),
\[
 \lambda_-\leq \frac{d^2}{81(3+d)^2}\leq\frac1{1296}<\frac1{169}.
\]
Thus the extreme singular values of the full matrix come from this (2\times2)
block and
\[
 \kappa_2(X_1)=\frac{\lambda_+}{|ab|}=9(3+d)\lambda_+.
\]
Consequently, throughout (0<d\leq1),
\[
1+\frac d3\leq\frac{\kappa_2(X_1)}{27d^{-2}}
\leq\left(1+\frac d3\right)\left(1+\frac{10d^2}{81}\right),
\]
and hence
\[
 \left|\frac{\kappa_2(X_1)}{27d^{-2}}-1\right|
 \leq\frac{121}{243}d.
\]
In particular (p_1=2) and (K_1=27).

## Case 2: exact algebraic constant and an explicit linear remainder

Permuting the columns of (X_2) in the order (2,1,3), which preserves its
singular values, gives
\[
M(d)=\begin{pmatrix}t&u^T\\v&D\end{pmatrix},\quad t=d^{-1},\quad
u=\binom{-1/9}{-1/19},\quad
v=\binom{1/(3+d)}{1/(6+d)},
\]
\[
D=\begin{pmatrix}-1/6&-1/16\\-1/3&-1/13\end{pmatrix}.
\]
The exact factorization
\[
M(d)=
\begin{pmatrix}1&0\\dv&I_2\end{pmatrix}
\begin{pmatrix}t&0\\0&D-dvu^T\end{pmatrix}
\begin{pmatrix}1&du^T\\0&I_2\end{pmatrix}
\tag{1}
\]
controls all three singular values.  Define
\[
U=\|u\|=\frac{\sqrt{442}}{171},\quad
V=\frac{\sqrt5}{6},\quad a=UV=\frac{\sqrt{2210}}{1026}.
\]
Then (|v|\leq V).  Also
\[
\det(zI-D^TD)=z^2-\frac{57905}{389376}z+\frac{25}{389376},
\]
so, on putting
\[
\mu_-:=\frac{57905-5\sqrt{132562057}}{778752},\qquad s:=\sqrt{\mu_-},
\]
we have (s=\sigma_{\min}(D)>0).

Here is a completely explicit remainder.  Set
\[
c=U+V+a,\qquad F=2c+c^2,\qquad b=a/s,
\]
\[
M_2=F+2b+2Fb,\qquad d_2=\min\{1,s/(2a)\}.
\]
For (0<d\leq d_2), Weyl's inequality gives
\[
s-ad\leq\sigma_{\min}(D-dvu^T)\leq s+ad.
\tag{2}
\]
Each shear in (1), and its inverse, has norm at most (1+dV) or
(1+dU), respectively.  Thus, with (f=(1+dU)(1+dV)), every singular
value of (M(d)) differs multiplicatively from the corresponding singular
value of \(\operatorname{diag}(t,D-dvu^T)\) by a factor in
([f^{-1},f]).  The ordering used here is valid since
(|D-dvu^T|\leq\|D\|_F+a<1\leq t).
Moreover (f^2\leq1+Fd).  Combining these facts with (2) gives
\[
\frac1{f^2}\frac{s}{s+ad}
\leq \frac{\kappa_2(X_2)}{s^{-1}d^{-1}}
\leq f^2\frac{s}{s-ad}.
\]
Since (bd\leq1/2), elementary expansion of the last bounds yields
\[
 \left|\frac{\kappa_2(X_2)}{K_2d^{-1}}-1\right|\leq M_2d,
 \qquad
 K_2=\frac1s=
 \sqrt{\frac{778752}{57905-5\sqrt{132562057}}}.
\]
Thus (p_2=1).  (Numerically (K_2\approx48.0567994164), only as a
cross-check.)

## Case 3: exact limiting algebraic condition number

Let (X_{3,0}=X_3(0)) and (H=X_{3,0}^TX_{3,0}).  Its characteristic
polynomial is
\[
\det(zI-H)=\frac{P(z)}{45542974464},
\]
\[
P(z)=45542974464z^3-13786630308z^2+429202697z-330625.
\]
Let (0<\rho_1<\rho_2<\rho_3) be the three roots of (P).  This designation
is exact: Sturm counts give exactly one root in each of
\[
(1/1300,1/1200),\qquad(1/30,1/29),\qquad(1/4,1/3).
\]
(The exact positive discriminant also proves that the roots are distinct.)
It follows that
\[
K_3=\kappa_2(X_{3,0})=\sqrt{\rho_3/\rho_1},\qquad p_3=0.
\]

For a rigorous remainder, put (m=\sqrt{\rho_1}), (A=\sqrt{\rho_3}),
(e=\sqrt{17}/36), (alpha=e/A), (eta=e/m), and
\[
M_3=\alpha+2\beta+2\alpha\beta.
\]
Only two entries vary, and direct subtraction shows
\[
\|X_3(d)-X_{3,0}\|_2\leq\|X_3(d)-X_{3,0}\|_F\leq ed.
\]
Weyl's singular-value inequality therefore gives
\[
A-ed\leq\sigma_1(X_3(d))\leq A+ed,
\quad m-ed\leq\sigma_3(X_3(d))\leq m+ed.
\]
The isolating bound (ho_1>1/1300) implies (eta d<1/2) for
(0<d\leq1/10).  Hence
\[
\left|\frac{\kappa_2(X_3(d))}{K_3}-1\right|\leq M_3d
\qquad(0<d\leq1/10).
\]
For orientation only, (K_3\approx18.4008717040).

## Case 4: exact formula on the full interval

For (0<d\leq1), the largest diagonal magnitude of (X_4) is
(1/(3+d)) and the smallest is (1/13).  Therefore
\[
\kappa_2(X_4(d))=\frac{13}{3+d},\qquad
K_4=\frac{13}{3},\qquad p_4=0,
\]
and on the full interval
\[
\left|\frac{\kappa_2(X_4(d))}{13/3}-1\right|
=\frac d{3+d}\leq\frac d3.
\]

Thus the four exact pairs are
\[
(p_1,K_1)=(2,27),\quad
(p_2,K_2)=\left(1,\sqrt{\frac{778752}{57905-5\sqrt{132562057}}}\right),
\quad
(p_3,K_3)=\left(0,\sqrt{\rho_3/\rho_1}\right),\quad
(p_4,K_4)=(0,13/3).
\]
