# Fresh mathematical referee report

Job: `win-00064-p02-referee-a6cd8b8cde33`  
Frozen snapshot: `4522d8fc638ddac56d9e97fe87c4452226e6fd9833077c02eb6de40229ea021a`

## Scope and source checks

I reviewed the exact two-part statement in `source.md`, its interpretation in
`problem.md`, the frozen `claim.json`, and every file listed in
`audit/snapshot.json`.  All listed SHA-256 hashes agree with the snapshot.  In
particular, the supplied Padmanabhan PDF has the recorded digest
`caaccb291c1fd425141c79cc77835a253908cb2b62ade72903c705f5e4a1d9a1`.

Definition 1.1 of that PDF defines the row-wise Lewis weights as the unique
positive fixed point of the leverage-score equation.  Lemma 3.1 and Section
3.2 give, with \(\gamma=1-2/p\),
\[
J=\gamma(I-K),\qquad K=W^{-1}(P\circ P),
\]
show that the eigenvalues of \(K\) lie in \([0,1]\), and derive
\(\rho(J)=\gamma(1-\lambda_{\min}(K))\).  Thus the source formulas used by the
candidate match their actual cited statements.  The inspected source section
does not itself state the dimension threshold or its sharpness.  The candidate
makes no claim of priority or verified open status.

## Reconstruction of the decisive argument

At a fixed point let \(B=W^{\gamma/2}A\) and factor its rank-\(n\) orthogonal
projection as \(P=UU^T\), where \(U^TU=I_n\).  If \(u_i^T\) is row \(i\) of
\(U\), then positivity of the weights gives \(u_i\ne0\), and
\[
(P\circ P)_{ij}=\langle u_i,u_j\rangle^2
=\langle u_i u_i^T,u_j u_j^T\rangle_F.
\]
Therefore \(P\circ P\) is exactly the Gram matrix of the \(m\) tensors
\(u_i u_i^T\) in the \(d=n(n+1)/2\) dimensional space
\(\operatorname{Sym}_n\).  Also
\[
K\sim W^{-1/2}(P\circ P)W^{-1/2}.
\]
Consequently, if \(m>d\), this Gram matrix is singular and the least
eigenvalue of \(K\) is zero.  The cited spectral formula then gives exactly
\(\rho(J)=1-2/p\).  This proves Part 1 without assuming an arbitrary PSD
matrix in place of a frame Gram matrix.

For Part 2, fix \(n\le m\le d\) and take
\(v_1,\ldots,v_m\) to be all \(e_i\), together with any \(m-n\) distinct
vectors \(e_i+e_j\).  In a linear relation among the tensors \(v_av_a^T\),
the \((i,j)\) coordinate belonging to a selected pair occurs in exactly one
pair tensor.  Hence every pair coefficient is zero, after which the diagonal
coordinates force every coefficient of \(e_ie_i^T\) to be zero.  The tensors
are thus linearly independent for every allowed intermediate \(m\).

Let \(S=\sum_a v_av_a^T\).  Since the first \(n\) terms sum to \(I_n\),
\(S\succ0\).  With \(R=S^{-1/2}\) and \(u_a=Rv_a\), one has
\(\sum_a u_au_a^T=I_n\).  Congruence \(X\mapsto RXR\) is invertible on
\(\operatorname{Sym}_n\), so the whitened tensors remain independent.  The
rows \(u_a^T\) therefore form a nonzero Parseval frame whose
\(P\circ P\) is positive definite.

The converse Lewis constraint is also satisfied, rather than assumed.  Put
\(w_a=\lVert u_a\rVert^2>0\), \(W=\operatorname{Diag}(w)\), and
\(A=W^{-\gamma/2}U\).  Positive row scaling preserves rank, while
\(W^{\gamma/2}A=U\) and \(A^TW^\gamma A=I_n\).  Hence the leverage score of
row \(a\) is exactly \(\lVert u_a\rVert^2=w_a\), so \(w\) is the unique
Lewis fixed point from Definition 1.1.  Its associated projection is the
constructed \(UU^T\), and the similar symmetric matrix above is positive
definite.  This establishes Part 2 for every real \(p>2\).

## Independent attacks and boundary checks

- Empty choices cause no gap: when \(m=n\), no pair vector is used and the
  construction is \(U=I_n\).  When \(n=1\), necessarily \(m=1\).
- At \(m=d\), every pair is used and the same unique off-diagonal-coordinate
  argument gives a basis of \(\operatorname{Sym}_n\).
- There is no division by zero: all whitened vectors are nonzero, hence every
  \(w_a\) is positive and every power of \(W\) used in the reconstruction is
  finite.
- No uniformity or limiting exchange is present.  The construction is valid
  separately for every real \(p>2\), as required; only the final positive row
  rescaling depends on \(p\).
- As a supplementary exact check, I independently formed the tensor-coordinate
  matrices over the rationals for every \(n=1,\ldots,7\) and every
  \(m=n,\ldots,n(n+1)/2\).  All had column rank \(m\), and all leading
  principal minors of the corresponding rational frame operators were
  positive.  This check corroborates, but is not used in place of, the proof.
- The failed attempt to invoke an unavailable `python` executable was purely
  operational; rerunning the exact check with `python3` succeeded and has no
  bearing on the verdict.

## Contribution and verdict

The frozen candidate is a `resolution-paper`, and its proof settles both parts
of the original claim at the full stated quantifier scope, including the
Parseval-frame and Lewis-weight constraints explicitly demanded by the
problem.  The sharpness construction works for every intermediate \(m\), not
only at the endpoint.  A short proof is sufficient here, and the claimed
contribution is limited honestly to resolving the frozen problem rather than
asserting literature priority.

I found no mathematical or scope gap requiring revision.  **Verdict: accept.**
