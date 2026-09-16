# A uniform top-degree coefficient for complete-raw inversion

This note proves a matching lower bound for the algebraic degree in the
frozen problem.  It does not settle the joint-ANF-leap equality.

## Statement

Let \(n\geq 3\), let \(p\in\mathbb F _2[t]\) be any irreducible polynomial
of degree \(n\), and use the polynomial basis
\(E=(e_0,\ldots,e_{n-1})=(1,\alpha,\ldots,\alpha^{n-1})\).  For the full
Boolean map
\[
 f_{\rm raw}(P,u)=\operatorname{adj}(P)J_n(Pu)
\]
of `problem.md`, including singular \(P\), one has
\[
 \deg f_{\rm raw}=3(n-1).
\]

More explicitly, put
\[
 G_{ij}=\operatorname{Tr}_{F/\mathbb F _2}(e_i e_j),\qquad B=G^{-1}.
\]
There are distinct indices \(r,a\) with \(B_{ar}=1\).  Fix distinct column
indices \(s,k\).  List the columns other than \(s\) as
\(c_0=k,c_1,\ldots,c_{n-2}\), and list the rows other than \(r\) as
\(\rho_0,\ldots,\rho_{n-2}=a\).  Define
\[
 Q=\{(\rho_i,c_i):0\leq i\leq n-2\}
   \mathbin\cup\{(r,s)\}
   \mathbin\cup\{(\rho_i,c_{i+1}):0\leq i<n-2\}.
\]
Then the coefficient of
\[
 \left(\prod_{(i,j)\in Q}p_{ij}\right)
 \left(\prod_{j\ne s}u_j\right)                                      \tag{1}
\]
in output coordinate \(k\) of \(f_{\rm raw}\) is exactly \(B_{ar}=1\).
The monomial (1) has degree \(2(n-1)+(n-1)=3(n-1)\).

## Proof

Let \((\lambda_0,\ldots,\lambda_{n-1})\) be the trace-dual basis, so
\(\operatorname{Tr}(\lambda_r e_i)=\delta_{ri}\).  Its coordinate matrix
has columns \(B_{\bullet r}\):
\[
 \lambda_r=\sum_a B_{ar}e_a.                                         \tag{2}
\]

First determine the degree-\((n-1)\) layer of the inversion map.  The ANF
coefficient of \(\prod_{i\ne r}x_i\) is the vector corresponding to
\[
 \sum_{x\in H_r}x^{-1},\qquad
 H_r=\operatorname{span}_{\mathbb F _2}\{e_i:i\ne r\}
     =\ker\bigl(x\mapsto\operatorname{Tr}(\lambda_r x)\bigr),         \tag{3}
\]
where \(0^{-1}=0\).  If \(H_0=\ker\operatorname{Tr}\), its subspace
polynomial is
\[
 \prod_{h\in H_0}(z+h)=\operatorname{Tr}(z)
   =z+z^2+z^4+\cdots+z^{2^{n-1}}.
\]
After division by \(z\), comparison of the constant and linear
coefficients gives
\(\sum_{h\in H_0\setminus\{0\}}h^{-1}=1\).  Since
\(H_r=\lambda_r^{-1}H_0\), (3) is \(\lambda_r\).  Also the coefficient of
the product of all \(n\) input bits is
\(\sum_{x\in F}x^{-1}=\sum_{x\in F}x=0\) for \(n\geq2\).  Consequently
the whole top layer is
\[
 J_n(x)_{[n-1]}=
 \sum_{r=0}^{n-1}[\lambda_r]_E\prod_{i\ne r}x_i.                     \tag{4}
\]

The matrix \(B\) has a nonzero off-diagonal entry.  Indeed, if not, then
its nonsingularity over \(\mathbb F _2\) would give \(B=I\), hence
\(G=I\).  If \(M\) is the matrix of multiplication by \(\alpha\) in
the polynomial basis, invariance of the trace pairing gives
\(M^T G=GM\).  Thus \(G=I\) would make \(M\) symmetric.  But
\(Me_0=e_1\), so \(M_{1,0}=1\), while \(Me_1=e_2\) for \(n\geq3\), so
\(M_{0,1}=0\), a contradiction.  Choose \(r\ne a\) with \(B_{ar}=1\).

The target below has the maximum possible degree \(3(n-1)\), so no ANF
layer of \(J_n\) below (4) can contribute: a degree-\(d\) input monomial
has degree at most \(2d\) after \(x=Pu\), and multiplication by the
adjugate adds at most \(n-1\).  Substitute \(x=Pu\) in (4).  A term of
degree \(n-1\) in the \(u\)'s
which omits \(u_s\) selects a perfect matching from the rows other than
some \(r'\) to the columns other than \(s\).  In output coordinate \(k\),
the determinant expansion of \(\operatorname{adj}(P)_{k a'}\) selects a
perfect matching from the rows other than \(a'\) to the columns other
than \(k\).  To produce all \(2(n-1)\) distinct \(P\)-variables in (1),
the two matchings must be edge-disjoint and have union \(Q\).

Regard \(Q\) as a bipartite graph.  It is the disjoint union of the edge
\(s-r\) and the path
\[
 k=c_0-\rho_0-c_1-\rho_1-\cdots-c_{n-2}-\rho_{n-2}=a.                \tag{5}
\]
The first matching must omit column \(s\), forcing the edge \(s-r\) into
the adjugate matching.  The adjugate matching must omit column \(k\),
forcing the first edge of (5) into the first matching.  Alternation along
the path then forces every edge.  Hence the decomposition is unique: the
first matching is \(\{(\rho_i,c_i)\}\), omitting row \(r\), and the
adjugate matching is
\(\{(r,s)\}\cup\{(\rho_i,c_{i+1}):i<n-2\}\), omitting row \(a\).
By (2), the resulting coefficient is \(B_{ar}=1\).

Finally, \(\operatorname{adj}(P)\) has degree \(n-1\); inversion has
degree at most \(n-1\); and substitution of the bilinear coordinates of
\(Pu\) at most doubles the latter degree.  Thus
\(\deg f_{\rm raw}\leq(n-1)+2(n-1)\).  The coefficient above gives the
reverse inequality and proves the statement.

## Reference-polynomial change

If a second allowed polynomial basis is expressed in the first by an
invertible matrix \(T\), its trace Gram matrix and inverse transform as
\[
 G'=T^TGT,\qquad B'=T^{-1}BT^{-T}.                                   \tag{6}
\]
Thus a particular pair \((r,a)\), and hence the displayed monomial, need
not be preserved.  Nevertheless every polynomial basis of length
\(n\geq3\) has a nonzero off-diagonal entry in its own \(B'\) by the
multiplication-matrix argument above.  Re-selecting that pair gives a
coefficient of the same degree for every permitted irreducible \(p\).
The certificate is therefore reference-dependent in location but uniform
in existence and value.

## Scope

This proves only the algebraic-degree equality from the original
conjunction.  No upper bound \(L_{\rm ANF}^{\rm joint}\leq n\) is proved
here, so the original problem remains unresolved.
