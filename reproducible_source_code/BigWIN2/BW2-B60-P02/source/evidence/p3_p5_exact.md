# Exact global certificate for degrees three through five

Put $k=\kappa$, $D=5p(p+1)$, and

\[
 g_*={1\over D-p^2}={1\over p(4p+5)}.
\]

Write the nonconstant coefficient vectors of $u,q$ as

\[
 \alpha=(a_1,\ldots,a_p)^T,\qquad
 \beta=(b_1,\ldots,b_p)^T,
\]

and replace the constant coefficient of $q$ by $y=q(k)$. Define

\[
 U_{ij}={ij(-1)^{i+j-2}\over i+j-1},\quad
 K_{ij}(k)={ij\,k^{i+j-1}\over i+j-1},\quad
 v_i(k)=i k^{i-1}.
\]

Direct integration and completion of the boundary square give the exact
identity

\[
\begin{split}
 a^{(2)}_{k,g}(u,q)
={}&D\left(y-{v^T\beta\over D}\right)^2
 +\alpha^TU\alpha+g\|\beta-\alpha\|^2\\
 &+\beta^T\left(K-{vv^T\over D}\right)\beta .
\end{split} \tag{1}
\]

The unused coefficient $u_0$ is the sole factored constant null direction.
Since $U$ is the Gram matrix of the basis $i x^{i-1}$ in
$L^2(-1,0)$, $P:=U+g_*I$ is positive definite. A second completion of
squares changes the last two terms in (1) into

\[
 (\alpha-g_*P^{-1}\beta)^TP(\alpha-g_*P^{-1}\beta)
 +\beta^TS_p(k)\beta,
\]

where

\[
 S_p(k)=K(k)-{v(k)v(k)^T\over D}+g_*I-g_*^2P^{-1}. \tag{2}
\]

Thus it remains only to certify $S_p(k)\succeq0$. Let
$\Delta_{p,j}(k)$ be its leading $j$ by $j$ principal minor. The
following is an exact coefficient certificate. Every line means

\[
 \Delta_{p,j}(k)={1\over d_{p,j}}\sum_{r=0}^{j^2}c_r k^r,
\]

with the displayed coefficient list ordered from $c_0$ upward (trailing
zeros are omitted). All denominators are positive. For $j<p$, every
coefficient is strictly positive. For $j=p$, the constant coefficient is
zero and every other coefficient is strictly positive.

## Degree 3

\[
\begin{array}{c|r|l}
j&d_{3,j}&[c_0,c_1,\ldots]\\ \hline
1&288030&[307,288030]\\
2&5184540&[25,61422,23211,7368,1728180]\\
3&34563600&[0,5880,2840,2120,181635,143000,310954,46422,5526,576060]
\end{array}
\]

## Degree 4

\[
\begin{array}{c|r|l}
j&d_{4,j}&[c_0,c_1,\ldots]\\ \hline
1&48007300&[51771,48007300]\\
2&3600547500&[24375,27996320,7713468,5177100,1200182500]\\
3&72010950000&[875,1739100,975540,1337000,114382590,258434400,436320220,46280808,11648475,1200182500]\\
4&630095812500&[0,61000,62400,94500,6815025,23373000,48129900,42105980,24482475,103345560,146389600,175877940,193087755,135333240,7713468,1035420,60009125]
\end{array}
\]

## Degree 5

\[
\begin{array}{c|r|l}
j&d_{5,j}&[c_0,c_1,\ldots]\\ \hline
1&6916071394725&[6278291156,6916071394725]\\
2&20748214184175&[84567189,106874255547,28461576147,25113164624,6916071394725]\\
3&414964283683500&[2668344,4810393332,2672153712,4198766224,474811709205,1020581506614,1660048955862,170769456882,56504620404,6916071394725]\\
4&72618749644612500&[333396,832077540,684736080,1293181680,122210625915,462292088538,1214092038530,1612891692510,1347981905385,3856221165605,10764841802388,17921277398340,15187050676180,10287912491580,569231522940,100452658496,6916071394725]\\
5&5123978974923858000&[0,32450544,55714176,139878144,12001478076,85474806984,315059491656,646065363384,811064107476,1531206650484,4815423196416,10864703913504,16644420401196,19355277131064,17235330280896,12474909886544,10263697225341,9027379754694,9240770097776,11347738287144,8917299321651,4238179481074,1640073302706,56923152294,6278291156,276642855789]
\end{array}
\]

It follows that for every $p=3,4,5$, the fraction-free leading pivots
$\Delta_{p,j}/\Delta_{p,j-1}$ are positive for $j<p$, while the last
pivot is nonnegative on $k\ge0$, vanishing exactly at $k=0$. Hence
$S_p(k)\succeq0$ for $k\ge0$, and $S_p(k)\succ0$ for $k>0$.
Equations (1)--(2) therefore prove the global upper bound
$\tau_p(k)\le g_*$ on the whole required interval and positive definiteness
on the effective coordinates for every $k>0$.

For a self-contained necessity certificate at the vanishing cut, put
$e_1=(1,0,\ldots,0)^T$. At $k=0$, (2) for arbitrary $g>0$ is

\[
 S_{p,g}(0)=A_g-{e_1e_1^T\over D},\qquad
 A_g=gI-g^2(U+gI)^{-1}=gU(U+gI)^{-1}\succ0.
\]

The rank-one downdate is PSD exactly when
$e_1^TA_g^{-1}e_1\le D$. Now

\[
 A_g^{-1}=g^{-1}I+U^{-1},\qquad
 (U^{-1})_{11}=p^2.
\]

The last identity is also exact: its left side is the squared norm of endpoint
evaluation on $\mathbb P_{p-1}$ in $L^2(-1,0)$. Shifted Legendre
polynomials give the reproducing-kernel value
$\sum_{m=0}^{p-1}(2m+1)=p^2$. Consequently

\[
 S_{p,g}(0)\succeq0
 \quad\Longleftrightarrow\quad {1\over g}+p^2\le D
 \quad\Longleftrightarrow\quad g\ge g_* . \tag{3}
\]

For every $g<g_*$, put $\beta=A_g^{-1}e_1$,
$\alpha=g(U+gI)^{-1}\beta$, and $y=e_1^T\beta/D$. The two completed
squares vanish, while, for $t=e_1^TA_g^{-1}e_1>D$, the remaining value is
$t-t^2/D<0$. This is an exact negative direction at $k=0$, and it persists
for all sufficiently small positive $k$. Together with the global upper
certificate this proves

\[
 \Gamma_p=g_*={1\over p(4p+5)}
 \quad(p=3,4,5).
\]

At every fixed $k>0$, the effective matrix at $g_*$ is positive definite,
so continuity permits a strictly smaller $g$; hence no interior point is a
maximizer. Positive definiteness also holds uniformly near $k=1$, so that
endpoint is not a limiting maximizer. Equation (3) and continuity show
$\tau_p(k)\to g_*$ as $k\to0^+$. Thus the unique limiting maximizer is
$k\to0^+$.

The script `evidence/verify_p3_p5.py` reconstructs (1)--(2), checks the matrix
congruence and $(U^{-1})_{11}=p^2$ in exact rational arithmetic for all five
degrees, and reproduces every coefficient and denominator displayed above.
