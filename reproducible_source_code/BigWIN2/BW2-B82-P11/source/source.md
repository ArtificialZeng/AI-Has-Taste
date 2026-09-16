# Source statement: the first uncovered rank-one mass layer

Source id: ARXIV-2609.08915-B82-RANK1-Q3

Primary source: Enkai Zhang, *Sharp Ordered Integer Models for Short
Additive Equalities*, arXiv:2609.08915v1, Definition 2.1, Proposition 6.5,
Corollary 9.2, Remark 10.1, and Question 12.3 (PDF pp. 3, 11, 19, 21,
and 24).

Local source PDF:
`batches/inbox/bigWin-82-materials/2609.08915.pdf`, SHA-256
`d3b9baeaadbab54b75975d304cfe4985af2ccaaef2a7cdd21414b823c85ffb82`.

## Frozen question

For an increasing real five-letter alphabet
\(T=(t_0<t_1<t_2<t_3<t_4)\), let \(Z_3(T)\) be its balanced integer
relations of mass at most three, and let \(M_3(T)\) be the least diameter of
an increasing integer alphabet with exactly the same vanishing relations in
that range. Suppose the rational span of \(Z_3(T)\) has rank one and its
primitive balanced generator has mass three.

Prove or disprove
\[
                         M_3(T)\le 33
\]
for every such \(T\). Equivalently, determine whether the maximum of
\(M_3\) on this rank-one, primitive-mass-three layer is exactly 33, since
the cluster profile in Corollary 9.2 attains 33. Equality classification is
a strengthening and must not replace the frozen universal bound.

## Verified source boundary

Proposition 6.5 gives only \(M_3(T)\le 3\cdot3\cdot4=36\). Remark 10.1
does not cover this high-mass layer, and Question 12.3 explicitly asks for
the per-mass maxima. Corollary 9.2 and \(L_4(3)=11\) give the exact cluster
value 33 and the integer model \(\{0,22,23,29,33\}\). The case
\((q,\mu)=(2,2)\) is already closed by the source bounds, making
\((3,3)\) the first uncovered finite layer. This is an open boundary
relative to the inspected source; global novelty still requires a fresh
primary-literature check, including the nearby work of Shin.

## Required verification route

Give a complete derivation of all feasible primitive mass-three relation
directions, not a sampled search. A candidate finite certificate may use the
tail sums of the relation coefficients to prove feasibility or infeasibility,
then supply an integer model of diameter at most 33 for every feasible
profile. An independent checker must verify that each model preserves
exactly the prescribed mass-at-most-three relation space. The cluster lower
bound must be proved from the relation-free four-letter core. Any claim that
only the cluster profile and its reflection attain 33 needs its own complete
certificate and referee check.
