# Minimum lag among 2-by-2 shift equivalences

Let
\[
A=\begin{pmatrix}1&12\\11&1\end{pmatrix},\qquad
B=\begin{pmatrix}1&132\\1&1\end{pmatrix}.
\]
The exact claim proved here is:

> If nonnegative integer matrices \(R,S\in M_2(\mathbb N_0)\) satisfy
> \(AR=RB\), \(SA=BS\), \(RS=A^L\), and \(SR=B^L\), then \(L\geq22\).
> Equality occurs, so 22 is the minimum lag in this precisely delimited class.

Consequently, every SSE chain from \(A\) to \(B\), if one exists, has at least
22 elementary steps. Indeed, composing the rectangular factors along an
\(m\)-step SSE chain gives 2-by-2 endpoint matrices \(R,S\) forming a shift
equivalence at lag \(m\).

This does not decide strong shift equivalence: an SSE chain may use many steps
and larger intermediate matrices.

## Scalar reduction

Write
\[
A^L=\begin{pmatrix}a&12b\\11b&a\end{pmatrix},
\qquad a+b\sqrt{132}=(1+\sqrt{132})^L.
\]
Solving the two intertwining equations entry by entry shows, conversely as well
as necessarily, that
\[
R=\begin{pmatrix}x&12z\\z&11x\end{pmatrix},\qquad
S=\begin{pmatrix}11u&12v\\v&u\end{pmatrix}
\]
for \(x,z,u,v\in\mathbb N_0\). Put
\((p,q,r,s)=(xu,zv,xv,zu)\). Then \(RS=A^L\) is equivalent to
\[
11p+12q=a,\qquad r+s=b,
\]
and automatically \(pq=rs\). Conversely, every nonnegative integral
quadruple satisfying these three scalar conditions lifts to \(x,z,u,v\): the
rank-one integer matrix
\(\left(\begin{smallmatrix}p&r\\s&q\end{smallmatrix}\right)\) has a
nonnegative integral outer factorization. For example, if its first row is
nonzero, divide that row by its gcd; coprimality and determinant zero force the
second row to be an integral multiple of the resulting primitive row. The
zero-row cases are immediate.

For a scalar solution set \(Y=|r-s|\) and \(X=24q-a\). Completing the square
and using \(a^2-132b^2=(-131)^L\) gives
\[
X^2-132Y^2=(-131)^L. \tag{1}
\]
The reverse reconstruction is exact after checking
\[
q=(X+a)/24,\quad p=(a-12q)/11,\quad
r=(b+Y)/2,\quad s=(b-Y)/2
\]
are nonnegative integers.

## Complete Pell-orbit parametrization

Work in \(K=\mathbb Q(\sqrt{33})\), whose integer ring is
\(\mathcal O_K=\mathbb Z[(1+\sqrt{33})/2]\) and whose discriminant is 33.
Minkowski's bound is \(\sqrt{33}/2<3\), so every ideal class has an integral
representative of norm 1 or 2. Since
\(N((5+\sqrt{33})/2)=-2\), both conjugate primes above 2 are principal.
Hence \(\mathcal O_K\) has class number one.

Set
\[
\lambda=1+2\sqrt{33},\qquad \bar\lambda=1-2\sqrt{33},
\qquad \epsilon=23+4\sqrt{33}.
\]
Here \(N(\lambda)=-131\), the two conjugates generate the two distinct primes
above 131, and \(\epsilon\) is the least unit greater than one. For the last
statement, a unit \((u+v\sqrt{33})/2\) obeys
\(u^2-33v^2=\mathord\pm4\); direct checking of \(1\leq v<8\) gives no
solution, and at \(v=8\) there is no norm-minus-one solution while
\((u,v)=(46,8)\) gives \(\epsilon\). The standard cyclicity of the unit group
of a real quadratic field then gives all norm-one units as
\(\mathord\pm\epsilon^n\).

Unique ideal factorization now shows that every solution of (1), regarded as
\(X+2Y\sqrt{33}\), is
\[
\mathord\pm\lambda^j\bar\lambda^{L-j}\epsilon^n,
\qquad 0\leq j\leq L,\quad n\in\mathbb Z. \tag{2}
\]
This also proves completeness; it is not a prefix search in \(X\) or \(Y\).

Only finitely many unit exponents in (2) can meet the reconstruction bounds.
Indeed a scalar solution has \(|X|\leq a\), \(0\leq Y\leq b\), hence both
real embeddings have absolute value at most
\(a+b\sqrt{132}=(1+\sqrt{132})^L\). Since
\(\epsilon=23+2\sqrt{132}>1+\sqrt{132}\), while every absolute embedding of
\(\lambda^j\bar\lambda^{L-j}\) is greater than one, \(n\geq L+1\) violates
the first embedding bound and \(n\leq-L-1\) violates the second. Thus the
finite ranges \(0\leq j\leq L\), \(-L\leq n\leq L\), and the two signs are
exhaustive.

## Exact result

`lag1_22_2x2_minimality.py` evaluates those finite orbits using integer-pair
arithmetic only. The numbers of reconstructed scalar solutions for lags
\(1,2,\ldots,22\) are
\[
(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1).
\]
As an independent computational cross-check, the script directly enumerates
all admissible \(q\) for \(1\leq L\leq8\) and obtains the same empty sets.

At lag 22 the unique scalar quadruple is
\[
(p,q,r,s)=(330834707029117152443,
56286015521267519916875,
56286015521267519916875,
330834707029117152443).
\]
It lifts to
\[
R=\begin{pmatrix}1&12\\1&11\end{pmatrix},\quad
S=\begin{pmatrix}
3639181777320288676873&675432186255210239002500\\
56286015521267519916875&330834707029117152443
\end{pmatrix}.
\]
The script checks nonnegativity and all four identities exactly. Therefore lag
22 is minimal among 2-by-2 nonnegative integer shift equivalences from \(A\) to
\(B\). The standard composition of an SSE chain into an SE then gives the
unconditional subsidiary bound of 22 elementary steps for any possible SSE
chain. The unrestricted SSE existence question remains unresolved.
