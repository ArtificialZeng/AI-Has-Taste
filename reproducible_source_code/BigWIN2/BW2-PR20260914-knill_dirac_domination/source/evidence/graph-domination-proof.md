# Candidate theorem: the sharp additive-one comparison for graph complexes

Research job: `primary-20260914-knill-dirac-domination-research-6e957123a5e9`.
Statement frozen for the tests in `graph_proof_checks.py` on 2026-09-14.
This is a proposed partial theorem awaiting a fresh referee, not an accepted
resolution of the original arbitrary-dimensional problem.

**Theorem.** Let G be a nonempty finite abstract simplicial complex all of
whose faces have cardinality at most two. With the unaugmented, unweighted
connection and signed Dirac matrices specified in `problem.md`,

\[
 S_k(L_G)\ge S_k(D_G)+1\qquad(1\le k\le |G|).
\]

The constant 1 is best possible, even among complexes with an edge.
There is no connectedness or bipartiteness assumption. An abstract graph
with a triangle is included as its vertices and edges, without a filled
two-dimensional face. No assertion for dimension at least two follows.

## Linear-algebra preliminaries and full proof

Write v for the number of vertices, e for the number of edges, c for the
number of connected components (including isolated vertices), and n=v+e.
Nonemptiness implies v>=c>=1. Put all vertices before all edges in the face
basis. Let B be the v-by-e unsigned incidence matrix and C the v-by-e signed
incidence matrix, with one +1 and one -1 in every column. Let A be the graph
adjacency matrix and let Delta be the diagonal matrix of vertex degrees.
Define

\[
 Q=BB^{\mathsf T}=\Delta+A,\qquad
 H=CC^{\mathsf T}=\Delta-A.
\]

List their v eigenvalues as q_1>=...>=q_v>=0 and h_1>=...>=h_v>=0, and list
the vertex degrees as delta_1>=...>=delta_v>=0. The elementary identities

\[
 L=\begin{pmatrix}I_v&B\\B^{\mathsf T}&B^{\mathsf T}B-I_e\end{pmatrix},
 \qquad D=\begin{pmatrix}0&C\\C^{\mathsf T}&0\end{pmatrix}                 \tag{1}
\]

follow directly from face intersection and incidence. In particular, distinct
edges share at most one vertex; the diagonal of B^T B is 2. These observations
justify the lower-right block of L without an imported spectral theorem.

Define

\[
 f(t)=\frac{t+\sqrt{t^2+4}}2,\qquad
 R(t)=\frac{\sqrt{t^2+4}-2}2 \quad(t\ge0).                              \tag{2}
\]

For every positive singular value s of B, an orthogonal singular-value
decomposition reduces L to a block

\[
 \begin{pmatrix}1&s\\s&s^2-1\end{pmatrix},
\]

whose characteristic polynomial is z^2-s^2 z-1. Its eigenvalues are f(s^2)
and -1/f(s^2). On ker(B^T) the remaining eigenvalues are +1, and on ker(B)
they are -1. Thus L has exactly v positive and e negative eigenvalues; its
positive eigenvalues, in decreasing order, are f(q_1),...,f(q_v), because
f is increasing and f(0)=1. Consequently

\[
 S_k(L)=\sum_{i=1}^k f(q_i)\quad(1\le k\le v),\qquad
 S_k(L)\ge\operatorname{tr}L=n\quad(v\le k\le n).                     \tag{3}
\]

The second inequality holds because all eigenvalues omitted from that sum
are negative. Empty B and C (e=0) cause no exception to these statements.

The signed incidence SVD similarly gives the nonzero Dirac eigenvalues
as the pairs +/-sqrt(h_i), for h_i>0. Write r=rank(C). There are n-2r zero
Dirac eigenvalues and r<=e, so n-r>=v. There are therefore enough nonnegative
Dirac eigenvalues that

\[
 S_k(D)=\sum_{i=1}^k\sqrt{h_i}\quad(1\le k\le v).                     \tag{4}
\]

Zeros among the h_i are included in this identity. For all k, the Dirac
partial sum is at most the sum of its positive eigenvalues.

We need two standard variational inequalities, recalled here to specify their
directions. For symmetric M, S_k(M) is the maximum of tr(PM) over rank-k
orthogonal projections P. Choosing a coordinate projection onto k largest
diagonal entries of Q gives

\[
 \sum_{i=1}^k q_i\ge\sum_{i=1}^k\delta_i.                            \tag{5}
\]

Also H<=2 Delta in positive-semidefinite order, since 2 Delta-H=Q>=0.
The eigenvalue min-max principle therefore gives

\[
 h_i\le 2\delta_i\quad(1\le i\le v).                                \tag{6}
\]

For completeness, the variational formula follows by diagonalizing M: the
diagonal entries of the conjugated projection lie in [0,1] and sum to k, so
their weighted eigenvalue sum is maximized by putting weight 1 on the k
largest eigenvalues. The min-max inequality follows by applying the
quadratic-form inequality H<=2 Delta on every subspace in that principle.

Combining (2)--(6), for 1<=k<=v we obtain the useful universal estimate

\[
\begin{aligned}
 S_k(L)-S_k(D)
 &\ge \sum_{i=1}^k R(q_i)
       +k+\frac12\sum_{i=1}^k q_i-\sum_{i=1}^k\sqrt{2\delta_i}\\
 &\ge R(q_1)+\frac12\sum_{i=1}^k(\sqrt{\delta_i}-\sqrt2)^2
 \ge R(q_1).                                                        \tag{7}
\end{aligned}
\]

Here f(t)=1+t/2+R(t), every R(t)>=0, and (5) was used before completing
the squares. No comparison between the complete spectra of Q and H has
been assumed.

**Initial sums when the graph is not bipartite.** Such a finite graph has an
odd cycle. One elementary justification is to color vertices of each component
by the parity of their distance from a root; a monochromatic edge gives an
odd closed walk, which contains an odd cycle after deleting repeated-vertex
subwalks. Let ell be the length of an odd cycle and let x equal 1/sqrt(ell)
on its vertices and zero elsewhere. Then ||x||=1 and

\[
 q_1\ge x^{\mathsf T}Qx
      =\sum_{uv\in E}(x_u+x_v)^2\ge 4.
\]

Indeed, the ell cycle edges alone contribute 4; all other terms are
nonnegative. Formula (7) therefore proves, for every 1<=k<=v,

\[
 S_k(L)-S_k(D)\ge R(4)=\sqrt5-1>1.                                  \tag{8}
\]

**Initial sums when the graph is bipartite.** Choose a diagonal matrix J
whose signs are the two vertex colors (choose either sign on isolates).
Then JHJ=Q, so h_i=q_i, including zero multiplicities. For every t>=0,

\[
 f(t)\ge1+t/2\ge\sqrt t+1/2,
\]

where the second difference is (sqrt(t)-1)^2/2. Equations (3) and (4) give

\[
 S_k(L)-S_k(D)\ge k/2\ge1\quad(2\le k\le v).                         \tag{9}
\]

For k=1, the endpoint estimate works for every complex: entrywise
|D|+I<=L. If u is a real unit vector and w=|u|, then

\[
 u^{\mathsf T}Du\le w^{\mathsf T}|D|w
 \le w^{\mathsf T}(L-I)w\le\lambda_1(L)-1.
\]

Maximizing over u proves S_1(L)>=S_1(D)+1. This also handles v=1.

**The remaining sums.** The identity
x^T Hx=sum_{uv in E}(x_u-x_v)^2 shows ker(H) consists precisely of
vectors constant on each connected component. Hence r=v-c. Since tr(H)=2e
and sqrt(t)<=(t+1)/2 for t>=0, the sum of positive Dirac eigenvalues satisfies

\[
 \sum_{h_i>0}\sqrt{h_i}
 \le\frac{\sum_{h_i>0}h_i+r}{2}=e+\frac r2.
\]

For v<=k<=n, (3) now yields

\[
 S_k(L)-S_k(D)\ge n-e-r/2=(v+c)/2\ge1.                              \tag{10}
\]

Together, (8)--(10) and the endpoint prove every asserted k.

**Sharpness.** For the complex consisting of one edge and its two vertices,

\[
 \operatorname{spec}(L)=(1+\sqrt2,1,1-\sqrt2),\qquad
 \operatorname{spec}(D)=(\sqrt2,0,-\sqrt2).
\]

Thus S_1(L)-S_1(D)=1, and the uniform additive constant cannot be increased.

## Dependencies, scope, and gaps

The argument uses real symmetric diagonalization, rectangular singular-value
decomposition, the eigenvalue min-max principle, and elementary graph
incidence identities. The signed and unsigned spectra are equated **only in
the bipartite case**, via the displayed conjugation. Every special spectral
formula needed for L is derived from (1). Knill's hydrogen identity and its
spectral transform are prior context, not an unproved premise here.

Known mathematical gaps in this stated graph theorem: none identified in the
proposer's checking. Fresh mathematical review remains required. The original
claim in dimensions at least two is unresolved. The five-vertex certificates
are finite supporting evidence, not steps in this uniform proof.

The additive-one conjecture itself is already in Knill's August 2025 post.
The proposed contribution is its proof for all graph complexes, including
non-bipartite ones. The current literature comparison and its search limits
are in `literature/research-verification.md`; no absolute priority or journal
acceptance is asserted.
