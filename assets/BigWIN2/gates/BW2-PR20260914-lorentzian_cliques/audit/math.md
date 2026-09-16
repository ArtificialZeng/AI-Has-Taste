# Mathematical referee report

Verdict: **accept** the exact frozen `result-note` in `claim.json`.
The frozen original status is **unresolved**. The accepted theorem is a
subsidiary result about bistable bipartite sources and one specified target
and derivative; it does not resolve the connected-clique characterization.

Referee job: `primary-20260914-lorentzian-cliques-referee-9a05707292b2`.
Review date: 2026-09-14, Asia/Shanghai.
Snapshot digest:
`433d775ecce23495c57cb0b57f8bf311721ff57d30a9c8a2b19e2d8bf4270d2d`.

This fresh review used `source.md`, `problem.md`, `claim.json`,
`audit/snapshot.json`, its listed evidence, and the actual cited primary
results accessed online. No checkpoint, scheduling state, prior review,
job transcript, or owner verdict was used. No agents or additional model
processes were spawned. All ten snapshot file hashes and the canonical
mapping digest matched before and after the independent computation.
The immutable source hash remains
`42cb787665ee3c401f92b773101e4d4daa27d30c0430cb71bae2e410a2393400`.

## Scope and reconstruction

Write $F=(L\cup R,E)$, with $|L|=|R|=k\ge2$, and assume that its only
maximum independent sets are $L,R$. In particular $\alpha(F)=k$.
The proof works for every graph satisfying these hypotheses, with no
restriction on planarity, regularity, degree, or order beyond those stated.
The matrix $A$, the labeled-assignment convention, the coefficient $c$,
and $\beta=(k-1,k-1,0)$ agree across the frozen statement and argument.

**Expansion and connectivity.** If $\varnothing\ne S\subsetneq L$
and $|N(S)|\le |S|$, then $S\cup(R\setminus N(S))$ is independent
of size at least $k$. A larger size contradicts $\alpha(F)=k$; equality
gives a maximum independent set different from both parts. Thus

\[
 |N(S)|\ge |S|+1
\]

for every nonempty proper subset of either part. Since $k\ge2$, this
applies to singletons and gives minimum degree at least two.
If deleting $u\in L$ produced several components, each component would
contain a nonempty proper subset $R_i\subset R$, and

\[
 |R_i|+1\le |N_F(R_i)|\le |L_i|+1.
\]

Summing contradicts $k=|R|>|L\setminus\{u\}|=k-1$.
Deleting a vertex of $R$ is symmetric. Therefore $F$ is 2-connected.
This is correctly attributed as known background, not a new graph theorem.

**The coefficient after two deletions.** An assignment has weight one
exactly when its spin-1 and spin-2 classes are independent; spin 3 is
unrestricted because every entry involving spin 3 equals one. Choose its
two-vertex class $D$ as an unordered subset. The remaining task is to
properly two-color $F-D$ with $k-1$ vertices of each color. Choosing an
unordered subset introduces no extra factor of two.

For $D=\{u,v\}$ with $u\in L,v\in R$, minimum degree two ensures
that every remaining vertex has a neighbor. For each component with parts
$L_i,R_i$, strict expansion gives

\[
 |L_i|+1\le |R_i|+1,\qquad |R_i|+1\le |L_i|+1.
\]

Both part subsets are proper because one vertex of each original part was
deleted. Hence every component is balanced. Its two possible orientations
are independent of the other components and preserve the required color
totals. This pair contributes exactly $2^{q(u,v)}$.

For $D\subset L$, a connected remainder has parts of sizes $k-2,k$
and contributes zero. In a disconnected remainder each component has
nonempty proper $R_i\subset R$. Expansion at $R_i$ gives
$|R_i|\le |L_i|+1$. When $L_i\ne\varnothing$, expansion at $L_i$
gives the reverse bound. When $L_i=\varnothing$, the component is a
single isolated vertex of $R$, so the same equality still holds.
Thus every component has imbalance $|R_i|-|L_i|=1$. Their total
imbalance is two, forcing exactly two components. Precisely two of their
four color orientations balance the totals. The case $D\subset R$
is symmetric. This proves the full identity

\[
 c=\sum_{u\in L,v\in R}2^{q(u,v)}+2s.
\]

The singleton case is essential and is valid, including $k=2$.
Every remainder has at least two vertices, so $q\ge1$.
Consequently $c\ge2k^2$, with strict inequality exactly when some pair
disconnects $F$. Together with 2-connectivity and $2k\ge4$, this is
exactly the claimed distinction between 3-connected sources and the
remaining sources in the class.

**Hessian and signs.** The six relevant coefficients, in the exponent
order shown, are

\[
\begin{array}{c|rrrrrr}
\alpha &(k+1,k-1,0)&(k-1,k+1,0)&(k,k,0)&(k,k-1,1)&(k-1,k,1)&(k-1,k-1,2)\\
[x^\alpha]f&0&0&2&2k&2k&c.
\end{array}
\]

The zeros use $\alpha(F)=k$. The coefficient 2 uses connectedness and
the two orientations of its bipartition. For a color class of size $k$,
the bistability hypothesis forces that class to be a whole part; the one
spin-3 vertex can then be chosen in $k$ ways in the other part. This
justifies both coefficients $2k$.

Since $|\beta|=2k-2$, the $(i,j)$ Hessian entry is exactly
$[x^{\beta+e_i+e_j}]f\prod_a(\beta+e_i+e_j)_a!$. In particular the
$(3,3)$ entry includes $2!$, while the off-diagonal entries do not.
This yields, without any coefficient normalization change,

\[
 H=2(k!)^2 M,\qquad
 M=\begin{pmatrix}0&1&1\\1&0&1\\1&1&c/k^2\end{pmatrix}.
\]

Set $t=c/k^2\ge2$. The vector $(1,-1,0)$ has eigenvalue $-1$.
On its orthogonal complement $M$ is represented by

\[
 \begin{pmatrix}1&\sqrt2\\\sqrt2&t\end{pmatrix}.
\]

Its determinant is $t-2$, and its trace is $1+t>0$. It is positive
definite for $t>2$, and has eigenvalues $3,0$ for $t=2$.
Thus the claimed inertias are exactly $(2,1,0)$ and $(1,1,1)$, in
positive/negative/zero order. The target itself has characteristic
polynomial $\lambda^3-\lambda^2-3\lambda-1
=(\lambda+1)(\lambda^2-2\lambda-1)$, giving the stated spectrum and
exactly one positive eigenvalue. It is entrywise nonnegative.

The necessary quadratic-derivative condition for Lorentzianity therefore
fails whenever $F$ has a two-vertex cut. No support assumption, numerical
eigenvalue test, limiting step, or source-deletion closure theorem is being
substituted for that condition. Conversely, the zero eigenvalue at equality
only describes this derivative. It establishes no Lorentzianity of $f$.

**Corollaries and boundary cases.** A maximum independent set in $C_{2k}$
has $k$ cyclic gaps each at least two; their sum is $2k$, so every gap
is two. Thus its only maximum independent sets are its two parts. There
are $2k$ adjacent cross-part pairs and $k^2-2k$ other cross-part pairs;
every same-part pair is a cut. The formula gives $6k(k-1)$, also for
$C_4$. In $K_{k,k}$, every independent set lies in one part. For
$k\ge3$, every two-vertex deletion leaves a nonempty connected complete
bipartite graph, giving $c=2k^2$. For $K_{2,2}$, deleting one whole
part leaves two isolated vertices and the formula instead gives $c=12$.
The serialized cube example was also checked exactly and has $c=32$,
showing that equality is not confined to complete bipartite graphs.

## Independent finite checks

`audit/referee-check.py` is a fresh verifier and imports no proposer code.
It enumerates vertex spin assignments directly using the entries of $A$,
rather than counting disjoint pairs of precomputed independent sets as the
proposer does. A separate set-based breadth-first search computes all
deletion components. Its independent-set hypothesis test examines every
$k$-subset; any independent set larger than $k$ necessarily contains
a $k$-subset different from the two parts, so this also rules out larger
maximum independent sets. Minimum degree two is used only as the proved
necessary prefilter.

The command `python3 audit/referee-check.py` completed successfully.
Its durable output is `audit/referee-check.json`. Exact results were:

| $k$ | All fixed-part graphs | Qualifying graphs | Strict cases | Equality cases |
|---|---:|---:|---:|---:|
| 2 | 16 | 1 | 1 | 0 |
| 3 | 512 | 34 | 33 | 1 |
| 4 | 65536 | 6785 | 6576 | 209 |

All six Hessian coefficients, the separator formula, the component balance
claims, 2-connectivity, the equality criterion, and the Hessian determinant
were checked for all 6820 qualifying graphs. All three excess histograms
match the frozen output. Additionally, all 15 serialized representatives
and 22 serialized structured cases through $k=7$ were read as explicit
edge lists and independently checked, including their component histograms
and Hessians. These 37 records are not claimed to be distinct graphs or
an exhaustive larger-order domain. The target characteristic polynomial
was independently computed with integer determinants. The eigenvalue sign
argument is the exact analytic reduction above, not a floating-point test.
This finite computation corroborates the proof; it does not replace its
unbounded quantifiers.

## Primary-source comparison and contribution

The relevant sections of both frozen primary HTML captures were inspected
locally, preserving mathematical `alttext`. Live primary pages independently
confirmed the decisive statements. The current arXiv version histories
display v2 for 2506.13659 and v1 for 2608.17920 on the review date.

- [Lee–Oh–Seo, 2506.13659v2](https://arxiv.org/html/2506.13659v2):
  Section 2 uses the same assignment polynomial and spectral convention;
  Theorem 3.1 proves clique sufficiency. Proposition 3.3 concerns support
  M-convexity, not the present Hessian calculation. Section 7 gives the
  earlier characterization conjecture and the known $P_3,K_{3,3}$
  examples. The source's even-cycle swapping result is a different
  property. None of these inspected statements gives this separator
  coefficient or the asserted fixed-target obstruction for bistable graphs.
- [Lee–Seo, 2608.17920v1, Section 6](https://arxiv.org/html/2608.17920v1#S6):
  the connected-source universal-target characterization is explicitly
  presented as a conjecture. Its clique-minimizing inequalities do not
  establish the coefficient identity reviewed here.
- [de Berg–Jansen–Mukherjee, 1610.03766v1](https://pure.tue.nl/ws/files/39529266/1610.03766v1):
  Definition 2, Lemma 6, and Definition 3/Observation 1 were inspected in
  the institutional primary PDF. They confirm the name and exact
  bistability hypothesis, the known biconnectivity fact, and the pumpkin
  examples. Their independent-set reconfiguration results are background;
  they do not state the semiproper-coloring coefficient or Lorentzian
  obstruction. The accepted contribution excludes those background facts.
- [Matherne–Morales–Selover, 2201.07333v4](https://arxiv.org/html/2201.07333v4):
  the proper-coloring definition and Theorem 1.5 were inspected. Its
  Lorentzian theorem concerns abelian Dyck-path indifference graphs with
  all colors proper, unlike the unrestricted third spin here.
- [Bendjeddou–Hardiman, DOI 10.1112/blms.70031](https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/blms.70031):
  the publisher abstract was inspected. It treats transformed multivariate
  independence polynomials after edge replacement. This remains an
  abstract-level comparison, not an exclusion of every full-text result.

Fresh searches combined Lorentzian polynomials with bistable graphs,
semiproper colorings, vertex cuts, separators, chromatic polynomials, and
two independent sets. Most cut/bistability hits concerned unrelated
physics, so their negative evidential value is small. No equivalent result
was found in the inspected primary statements. This is a bounded source
comparison, not a proof of global priority or a guarantee of open status
outside the inspected literature.

The precise delta is the sharp separator expression for this coefficient,
its conversion to an explicit common antiferromagnetic witness for every
bistable source of vertex connectivity two, and the exact equality
limitation on 3-connected bistable sources. This is a modest but coherent
nontrivial partial result. The source class is established in graph theory
and contains infinite families of varying size and degree; it is not a
finite table or an arbitrarily chosen order restriction. The credible use
is to settle this structural class in the unresolved characterization and
to identify exactly where this natural derivative ceases to be a witness.
The result does not follow merely by specializing the inspected clique
sufficiency, swapping, or biconnectivity theorems. The even-cycle case
belongs in the same note as a corollary, not in a separate contribution.

## Decision and remaining limits

The full frozen scope passes correctness, evidence, and contribution review.
No substantive correction or scope downgrade is required. Acceptance does
not claim that the target witnesses every bistable graph, that the
3-connected equality case proves Lorentzianity, or that the original
characterization is settled. Novelty language must retain the bounded
primary-source qualification above. No formal proof-assistant check or
journal peer review is claimed.

The next workflow test is the runner's integrity/provenance `check-math`
gate, followed by a manuscript restricted to this accepted scope. This
referee has not written a manuscript or performed publication audits.
