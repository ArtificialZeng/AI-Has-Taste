# Precise problem reading

## Objects and conventions

- A **rooted tree** \((H,\rho)\) is a finite simple connected acyclic graph
  with distinguished vertex \(\rho\).  A rooted isomorphism is a graph
  isomorphism carrying root to root.
- Its **root height** is \(\max_{v\in V(H)}d_H(\rho,v)\).  Thus “height at
  most two” includes the one-vertex tree and trees of height zero or one.
- For \(J\subseteq E(H)\), \(c(J)\) is the set of vertex sets of the
  connected components of the spanning forest \((V(H),J)\), and \(R_J\)
  is the unique member containing \(\rho\).
- The variables \(z_1,z_2,\ldots\) are commuting algebraically independent
  variables, and equality of the displayed polynomials means coefficientwise
  equality in \(\mathbb Z[z_1,z_2,\ldots]\).

For an integer \(g\geq 3\), define
\[
\Psi_{H,g}(\mathbf z)=\sum_{J\subseteq E(H)}
 z_{g-1+|V(R_J)|}
 \prod_{\substack{D\in c(J)\\D\ne R_J}}z_{|V(D)|}.
\]

## Exact quantified claim

For every fixed integer \(g\geq3\), every integer \(N\geq1\), and every
pair of rooted trees \((H,\rho)\), \((H',\rho')\) with
\(|V(H)|=|V(H')|=N\) and root height at most two,
\[
 \Psi_{H,g}=\Psi_{H',g}\quad\Longrightarrow\quad
 (H,\rho)\cong(H',\rho').
\]
The same value of \(g\) is used on both sides.  The problem makes no claim
for \(g=2\), for comparisons across different \(g\), or for rooted trees of
height greater than two.  For \(N=1\) there is only one rooted tree.

## Height-two normal form

Let the components of \(H-\rho\) be \(B_1,\ldots,B_r\), where
\(r=\deg_H(\rho)\).  Because the root height is at most two, each \(B_i\)
is a star rooted at the unique neighbor of \(\rho\).  Put
\[
 b_i=|V(B_i)|\geq1,\qquad d_i=b_i-1,\qquad
 \sum_{i=1}^r b_i=N-1.
\]
Here \(d_i\) is the number of depth-two leaves in branch \(i\).  Conversely,
the multiset \(\{b_1,\ldots,b_r\}\) determines the rooted isomorphism type,
including height-one branches through \(b_i=1\).  The case \(N=1\) has
\(r=0\) and the empty multiset.

## Source status and nearest prior results

The mathematical source boundary was checked on 2026-09-09 against
[arXiv:2609.07728v1](https://arxiv.org/abs/2609.07728) and the supplied local
PDF (SHA-256
`f3d4ae846384717ecce1c31261f021f172dad47443c7dd635d1d15b64ddd8f12`).
The official v1 title is *The Loopy Polynomial: from Tutte's Universal
V-Function to Bizonotopal Geometry*, not the different title recorded in
`source.md`; this is a bibliographic correction only and does not alter the
frozen claim.

- Conjecture 9.10 (printed p. 52) asserts injectivity of \(H\mapsto
  \Psi_{H,g}\) on all rooted trees of fixed order for every \(g\geq3\).
- Remark 9.12 records exhaustive verification through order 13, automatic
  reconstruction for \(g\geq N\), and counterexamples when \(g=2\).
- The proof of Theorem 9.14 covers the regime in which every component of
  \(H-\rho\) has fewer than \(g\) vertices: the root-component factor is then
  identifiable, so the fully pointed polynomial is recovered.  This does not
  cover arbitrary height-two branches.
- The fully pointed rooted \(U\)-polynomial is known to reconstruct every
  rooted tree by Aliste-Prieto, de Mier, and Zamora,
  [arXiv:2002.08186, Theorem 9](https://arxiv.org/abs/2002.08186)
  (published in *Discrete Mathematics* 344 (2021), 112255).  It retains the
  root-component size separately, whereas \(\Psi_{H,g}\) merges that marker
  into the ordinary \(z\)-variables.

The exact height-two specialization was not stated in either inspected
primary paper, and targeted arXiv searches on 2026-09-09 found no separate
source settling it.  This supports treating it as a new special-case question,
not as a claim of novelty or proof of open status.

## Proposed contribution and verification route

Nearest prior result \(X\): injectivity of the fully pointed rooted
\(U\)-polynomial for all rooted trees, and injectivity of this specialization
when the root marker is unambiguous (in particular \(b_i<g\)).

Proposed delta \(Y\): remove every restriction on \(b_i\) for all rooted
trees of height at most two and all \(g\geq3\).

For \(0\leq k\leq\lfloor(N-1)/2\rfloor\), the cheapest candidate invariant is
\[
 a_k=[z_gz_2^kz_1^{N-1-2k}]\Psi_{H,g}.
\]
Direct inspection of the defining forest sum suggests the exact identity
\[
 a_k=e_k(d_1,\ldots,d_r),\qquad
 \sum_{k=0}^{\lfloor(N-1)/2\rfloor}a_kt^k
   =\prod_{i=1}^r(1+d_it).
\]
Indeed, because \(g\geq3\), a monomial using only \(z_g,z_2,z_1\) forces
the root component to be the singleton root; its size-two components then
come from choosing one leaf edge in each of \(k\) distinct branches.  Also
\([z_{g+1}z_1^{N-2}]\Psi_{H,g}=r\) for \(N\geq2\).  A research pass should
prove these statements without hidden monomial-collision assumptions, use
the resulting product and the known value of \(r\) to recover the zeros and
positive entries of the multiset \(\{d_i\}\), and then recover \(\{b_i\}\).
An exact integer-partition enumerator is suitable only as an independent
audit of that symbolic proof.
