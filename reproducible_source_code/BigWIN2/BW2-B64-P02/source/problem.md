# Precise reading

## Frozen source claim

The immutable statement is in `source.md`.  The following fixes notation and
quantifiers without changing its claim.

Let \(p>2\), put \(\gamma=1-2/p\), and let \(n,m\) be positive integers with
\(m\ge n\).  Let \(A\in\mathbb R^{m\times n}\) have rank \(n\), and suppose its
row-wise \(\ell_p\)-Lewis-weight vector \(w=(w_i)_{i=1}^m\) is strictly positive.
Write \(W=\operatorname{Diag}(w)\),
\[
 B=W^{\gamma/2}A,\qquad
 P=B(B^TB)^{-1}B^T,
 \qquad K=W^{-1}(P\circ P),
\]
where \(\circ\) is the Hadamard product.  The fixed-point relation is
\(w_i=P_{ii}\).  Thus \(P\) is an orthogonal projection of rank \(n\), with
positive diagonal \(w\).  Padmanabhan's Lemma 3.1 gives the log-coordinate
Jacobian \(J=\gamma(I-K)\) and
\[
 \rho(J)=\left(1-\frac2p\right)
         \bigl(1-\lambda_{\min}(K)\bigr).
\]

The two assertions to prove or disprove are:

1. For every such \(p,n,m,A\), if \(m>n(n+1)/2\), then
   \(\lambda_{\min}(K)=0\).  Consequently \(\rho(J)=1-2/p\).
2. For every real \(p>2\) and every pair of positive integers \(n,m\) with
   \(n\le m\le n(n+1)/2\), there exists an \(A\in\mathbb R^{m\times n}\) as
   above for which \(K\) is positive definite.  The matrix \(A\) may depend on
   \(p,n,m\).

"Positive definite" for the generally nonsymmetric matrix \(K\) means that
all its eigenvalues are positive, equivalently that the symmetric similar
matrix \(W^{-1/2}(P\circ P)W^{-1/2}\) is positive definite.

## Equivalent Parseval-frame formulation

Choose \(U\in\mathbb R^{m\times n}\) with \(U^TU=I_n\) and \(P=UU^T\), and
write its nonzero rows as \(u_i^T\).  Then \(w_i=\|u_i\|_2^2\), and
\[
 (P\circ P)_{ij}=\langle u_i,u_j\rangle^2
 =\langle u_i u_i^T,u_j u_j^T\rangle_F.
\]
Hence \(P\circ P\) is the Gram matrix of the \(m\) elements \(u_i u_i^T\)
of \(\operatorname{Sym}_n\), a vector space of dimension \(n(n+1)/2\).
Accordingly, \(K\) is positive definite exactly when those rank-one symmetric
matrices are linearly independent.

Conversely, every nonzero Parseval frame \((u_i)_{i=1}^m\) yields an admissible
Lewis-weight instance: set \(w_i=\|u_i\|^2\), \(W=\operatorname{Diag}(w)\),
and \(A=W^{-\gamma/2}U\).  Then \(W^{\gamma/2}A=U\), its leverage scores are
\(w_i\), and the Lewis fixed-point relation holds.  This converse is part of
the required constraint check, rather than a relaxation to an arbitrary PSD
matrix.

## Source status and nearest prior result

The cited primary source is Swati Padmanabhan, *Computing Lewis Weights to High
Precision by Fixed-Point Iteration*, arXiv:2609.04338v1, Lemma 3.1 and Section
3.2.  The supplied PDF (inspected 2026-09-07) proves the displayed Jacobian and
spectral formula, but the inspected section does not state the dimension
threshold or its sharpness.

An adjacent primary result is Dan Edidin, Ivan Gonzalez, and Itzhak Tamo,
*Pure-State Quantum Tomography with Minimal Rank-One POVMs*,
<https://arxiv.org/abs/2511.09505> (inspected 2026-09-07), especially the
whitening observation in the introduction, Definition 2.1, and Theorem 3.1 and
its sharpness construction.  It explicitly uses the real frame
\(\{e_i,e_i+e_j:i<j\}\), whitens frames to rank-one POVMs, and records the
ambient dimension \(\binom{n+1}{2}\).  These are the main ingredients of Part
2, although the inspected paper does not formulate the Lewis-weight matrix
\(K\) or the claimed local-rate consequence.  Thus the exact source claim is
**status-uncertain**, not a verified open problem; its frame-theoretic
construction is adjacent to known literature and must not be advertised as
novel without a broader search.

Nearest prior result \(X\): Lemma 3.1 gives \(0\le\lambda_i(K)\le1\) and the
local-rate formula.  Proposed delta \(Y\): determine exactly when the Gram
matrix of the constrained rank-one frame tensors must/can be nonsingular.
Verification route \(Z\): dimension counting proves the forced-singularity
direction; for sharpness, start from independent rank-one tensors spanning
\(\mathbb R^n\), whiten their frame operator, and reconstruct \(A\) by the
converse above.
