# Complete proof of the sharp threshold

This proves exactly the two-part claim frozen in `source.md`, under the precise
reading in `problem.md`. Put
\(\gamma=1-2/p\) and \(d=n(n+1)/2=\dim\operatorname{Sym}_n\).
The formulas for \(J\), \(K\), their spectral relation, and the predicted local
rate are those of Lemma 3.1 of the copied primary source
`evidence/external/2609.04338.pdf`.

## Reduction to rank-one symmetric tensors

At the Lewis fixed point, set \(B=W^{\gamma/2}A\). The matrix
\[
 P=B(B^TB)^{-1}B^T
\]
is an orthogonal projection of rank \(n\), and its diagonal is the Lewis-weight
vector: \(P_{ii}=w_i>0\). Choose an \(m\times n\) matrix \(U\) with
\(U^TU=I_n\) and \(P=UU^T\), and denote the transpose of row \(i\) by
\(u_i\in\mathbb R^n\). Then
\[
 w_i=\|u_i\|_2^2,
 \qquad
 (P\circ P)_{ij}=\langle u_i,u_j\rangle^2
 =\langle u_i u_i^T,u_j u_j^T\rangle_F.                 \tag{1}
\]
Thus \(P\circ P\) is the Gram matrix of the \(m\) vectors
\(u_i u_i^T\) in the \(d\)-dimensional real inner-product space
\(\operatorname{Sym}_n\).

Since \(W\) is positive diagonal,
\[
 K=W^{-1}(P\circ P)
 \sim W^{-1/2}(P\circ P)W^{-1/2}.                       \tag{2}
\]
The matrix on the right is positive semidefinite. In particular, the
eigenvalues of \(K\) are real and nonnegative; \(K\) is positive definite in
the sense of the problem exactly when \(P\circ P\) is nonsingular, equivalently
when the tensors in (1) are linearly independent.

## Part 1

If \(m>d\), the \(m\) tensors \(u_i u_i^T\in\operatorname{Sym}_n\) are
linearly dependent. Their Gram matrix \(P\circ P\) is therefore singular.
By (2), \(K\) is similar to a singular positive-semidefinite matrix, so
\(\lambda_{\min}(K)=0\). Lemma 3.1 then gives
\[
 \rho(J)=\left(1-\frac2p\right)
          \bigl(1-\lambda_{\min}(K)\bigr)
        =1-\frac2p.
\]
This is exactly the global factor, proving Part 1 and its rate consequence.

## Part 2: construction at every dimension up to the threshold

Fix \(n\le m\le d\), and put \(r=m-n\). Choose any \(r\) distinct unordered
pairs from \(\{\{i,j\}:1\le i<j\le n\}\). This is possible because
\(0\le r\le n(n-1)/2\). Form a list of \(m\) vectors consisting of
\[
 e_1,\ldots,e_n,
 \quad\text{and}\quad e_i+e_j
 \quad\text{for the chosen pairs }\{i,j\}.              \tag{3}
\]
Call these vectors \(v_1,\ldots,v_m\).

Their rank-one tensors are linearly independent. Indeed, in a relation
\[
 \sum_{i=1}^n a_i e_i e_i^T+
 \sum_{\{i,j\}}b_{ij}(e_i+e_j)(e_i+e_j)^T=0,
\]
the \((i,j)\) off-diagonal entry is \(b_{ij}\) for each chosen pair, because
no other displayed tensor contributes to that coordinate. Hence every
\(b_{ij}=0\), after which the diagonal entries give every \(a_i=0\).

Let
\[
 S=\sum_{a=1}^m v_a v_a^T.
\]
The first \(n\) summands add to \(I_n\), so \(S\succ0\). Put
\(R=S^{-1/2}\) (the positive-definite inverse square root) and
\(u_a=Rv_a\). Then every \(u_a\ne0\) and
\[
 \sum_{a=1}^m u_a u_a^T=RSR=I_n.                       \tag{4}
\]
Consequently the matrix \(U\) with rows \(u_a^T\) is Parseval:
\(U^TU=I_n\). Moreover, congruence by the invertible matrix \(R\) is an
invertible linear map on \(\operatorname{Sym}_n\), and
\[
 u_a u_a^T=R(v_a v_a^T)R.
\]
It therefore preserves the tensor independence just proved. By (1), for
\(P=UU^T\) the matrix \(P\circ P\) is positive definite.

It remains to verify that this constrained Parseval example really is a Lewis
instance, rather than merely an arbitrary Gram construction. Define
\[
 w_a=\|u_a\|_2^2>0,\qquad W=\operatorname{Diag}(w),
 \qquad A=W^{-\gamma/2}U.                               \tag{5}
\]
The positive row scaling in (5) preserves column rank, so \(A\) has rank
\(n\) and has no zero row. Furthermore
\[
 W^{\gamma/2}A=U,
 \qquad A^TW^\gamma A=U^TU=I_n.
\]
Thus the leverage score of row \(a\) of \(W^{\gamma/2}A\) is
\(u_a^T(U^TU)^{-1}u_a=\|u_a\|^2=w_a\). Hence \(w\) satisfies the defining
Lewis fixed-point equation (Definition 1.1 of the copied primary source); by
the uniqueness in that definition it is the row Lewis-weight vector of
\(A\). Its associated projection is exactly \(P=UU^T\). Since
\(P\circ P\succ0\) and \(W\succ0\), (2) shows that the resulting \(K\) is
positive definite. This proves Part 2 for every real \(p>2\).

## Boundary and dependency audit

- If \(n=1\), then \(d=m=1\); (3) is just \(v_1=e_1\), and (4)--(5) apply.
- If \(m=n\), no pair vectors are chosen, \(S=I_n\), and \(U=I_n\).
- If \(m=d\), all \(n(n-1)/2\) pair vectors are chosen; the off-diagonal
  coordinate argument proves independence of all \(d\) tensors.
- The only use of \(p>2\) is the prescribed exponent \(\gamma\) and the scope
  of the source's Lewis fixed-point dynamics; all row scalings in (5) remain
  finite and positive.
- The converse construction checks nonzero rows, full column rank, the
  fixed-point equation, the exact projection, and positive weights explicitly.
- Research-pass gap list: empty. This is a proposer proof, not a substitute
  for the required fresh-referee audit.
