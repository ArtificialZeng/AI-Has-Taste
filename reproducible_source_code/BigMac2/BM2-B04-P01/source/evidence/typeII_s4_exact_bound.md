# Exact type-II bound on the \(S_4\)-invariant family

Provenance: `bigMac-00004-p01-research-499edf789275`  
Scope: only matrices invariant under permutations of indices \(3,4,5,6\).

Let \(s=1+3d\).  On the orthogonal sum of the three-dimensional space
supported on \(\{3,4,5,6\}\) with coordinate sum zero and its complement,
the matrix in `checkpoint.md` acts respectively as \((1-d)I_3\) and
\[
 Q=\begin{pmatrix}1&a&2b\\a&1&2c\\2b&2c&s\end{pmatrix}.
\]
Moreover
\[
 \det Q=(1-a^2)(s-4b^2)-4(c-ab)^2.
\]
Consequently the matrix has at most one positive eigenvalue if and only if
\[
 d\ge1,\qquad a\ge1,\qquad 4b^2\ge s,\qquad
 (1-a^2)(s-4b^2)\ge4(c-ab)^2. \tag{1}
\]
Necessity follows from the displayed decomposition, interlacing applied to the
\((1,2)\) and \((1,3)\) principal submatrices, and \(\det Q\ge0\).
For sufficiency, if \(a>1\), the leading \(2\times2\) block has one positive
and one negative eigenvalue; interlacing and \(\det Q\ge0\) exclude a second
positive eigenvalue.  If \(a=1\), (1) forces \(c=b\); then \((1,-1,0)\) is a
zero vector for \(Q\), while the remaining \(2\times2\) block has determinant
\(2(s-4b^2)\le0\).  This also proves sufficiency in the singular cases.

For \(h=(-2,-1,1,1,1,1)\), the normalized monomial is
\[
 F(P)=\frac{\sqrt a\,d^{3/2}}{b^2c}. \tag{2}
\]
Write, uniquely with \(x,y\ge0\),
\[
 a=\cosh x,\qquad \frac{2b}{\sqrt s}=\cosh y.
\]
Condition (1) gives
\[
 c\ge ab-\frac12\sqrt{(a^2-1)(4b^2-s)}
   =\frac{\sqrt s}{2}\cosh(x-y). \tag{3}
\]
Substitution into (2) yields
\[
 F(P)\le 8\left(\frac d{s}\right)^{3/2}
 \frac{\sqrt{\cosh x}}{\cosh^2y\,\cosh(x-y)}. \tag{4}
\]
The last factor is at most one.  Indeed, put \(z=x-y\),
\(p=\tanh y\ge0\), and \(q=\tanh z\).  After squaring, the required
inequality is
\[
 1+pq\le \cosh^3y\cosh z,
\]
because \(\cosh x=\cosh y\cosh z(1+pq)\).  If \(q\le0\), the left side is
at most one.  If \(q\ge0\), Cauchy--Schwarz gives
\[
 \sqrt{(1-p^2)(1-q^2)}+pq\le1,
\]
and hence
\(\sqrt{(1-p^2)(1-q^2)}(1+pq)\le1\), i.e.
\(1+pq\le\cosh y\cosh z\le\cosh^3y\cosh z\).

It follows exactly that
\[
 F(P)\le8\left(\frac d{1+3d}\right)^{3/2}
 <\frac8{3\sqrt3}<2. \tag{5}
\]
The family bound is sharp as a supremum: for every \(d\ge1\), take
\(a=1\) and \(b=c=\sqrt{1+3d}/2\).  These matrices satisfy (1) and attain
the first quantity in (5); letting \(d\to\infty\) gives
\[
 \sup_{P\ \text{in this }S_4\text{-invariant family}}F(P)
 =\frac8{3\sqrt3}.
\]
Thus the proposed strict feasibility condition
\(a^2d^6>16b^8c^4\) has no real solution under (1), and in particular no
rational solution.  This does **not** bound nonsymmetric type-II matrices.
