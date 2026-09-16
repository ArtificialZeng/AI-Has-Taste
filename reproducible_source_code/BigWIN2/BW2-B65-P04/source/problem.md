# Precise problem statement

## Frozen claim and interpretation

For every pair of integers \(s,t\ge 0\) such that
\[
n=3s+4t\ge 4,
\]
let \(F=sC_3\sqcup tC_4\) be the finite simple graph consisting of \(s\)
vertex-disjoint triangles and \(t\) vertex-disjoint four-cycles, and let
\(G=\overline F\) be its simple-graph complement on the same \(n\) vertices.
The frozen assertion to prove or disprove is
\[
\forall s,t\in\mathbb Z_{\ge0}\quad
(3s+4t\ge4\Longrightarrow \operatorname{rig}(\overline{sC_3\sqcup
tC_4})=M(\overline{sC_3\sqcup tC_4})).
\]
The assertion is invariant under relabelling the components and their vertices.
It is only about this pure \(C_3/C_4\) family.

The phrase “Guler–Jackson conventions” in `source.md` is a bibliographic
misattribution, not a change to the mathematics. As recorded before triage in
`source-correction.md`, the intended definitions are those in John Haslegrave,
Peleg Michaeli and Anthony Nixon, *Rigidity of complements of bounded-degree
graphs*, arXiv:2609.05058v1 (2026).

## Definitions

For an integer \(d\) with \(0\le d\le n-1\), a realisation is a map
\(p:V(G)\to\mathbb R^d\). It is generic when all \(dn\) coordinates are
algebraically independent over \(\mathbb Q\). The graph \(G\) is *generically
\(d\)-rigid* when one (equivalently every) generic realisation is rigid, meaning
that every sufficiently small continuous motion preserving the lengths of all
edges also preserves all pairwise distances. Equivalently, for \(n\ge d+1\),
the generic \(d\)-dimensional rigidity matrix has rank
\[
dn-\binom{d+1}{2}.
\]
Every graph is generically \(0\)-rigid by convention, and generic rigidity is
monotone downward in \(d\). Thus
\[
\operatorname{rig}(G)=\max\{d\in\mathbb Z:0\le d\le n-1,
\ G\text{ is generically }d\text{-rigid}\}.
\]

The Maxwell dimension is
\[
M(G)=\max\left\{d\in\mathbb Z:0\le d\le n-1,
\ dn-\binom{d+1}{2}\le |E(G)|\right\}.
\]
Maxwell's necessary edge count gives \(\operatorname{rig}(G)\le M(G)\), so
the frozen equality is equivalent to generic \(M(G)\)-rigidity for every
allowed pair \((s,t)\).

## Normalisation and boundary cases

Every vertex of \(F\) has degree two. Consequently \(G\) is
\((n-3)\)-regular and
\[
|E(G)|=\binom n2-n=\frac{n(n-3)}2.
\]
If
\[
a_n=\min\{a\in\mathbb Z_{\ge0}:a(a+1)\ge2n\}
=\left\lceil\frac{\sqrt{8n+1}-1}{2}\right\rceil,
\]
then direct substitution in the Maxwell inequality gives the exact target
\[
M(G)=n-1-a_n.
\]
In particular, the target dimension depends only on \(n\), although the
generic rigidity could depend on the decomposition \(n=3s+4t\).

The least allowed pair is \((s,t)=(0,1)\): here \(G=2K_2\), \(M(G)=0\), and
the equality holds by the zero-dimensional convention. The next two feasible
cases also pass exact structural checks. For \((2,0)\), \(G=K_{3,3}\) and
\(M(G)=2\); \(K_{3,3}\) is a Laman graph. For \((1,1)\), \(M(G)=2\); a
spanning \(K_{3,3}\) is obtained from the triangle component and any three
vertices of the four-cycle component, and the last vertex has three neighbours
in that subgraph, so a 0-extension proves generic 2-rigidity.

## Nearest prior result and exact gap

The primary paper was checked in its hash-fixed local copy
`batches/inbox/bigWin-65-materials/2609.05058.pdf` (SHA-256
`e5a603ed64fc286ceb56f1a009d559bb4a27ac2f5bc63ac02977a2800cd842be`)
and at <https://arxiv.org/abs/2609.05058> on 2026-09-07.
Its Theorem 1.4 (PDF page 2) proves Maxwell-sharpness when the complement has
maximum degree at most two and has no component isomorphic to \(C_3\) or
\(C_4\). The following limitation paragraph says the authors believe those
exclusions are limitations of their argument, inherited from a non-twin
hypothesis, rather than genuine obstructions. Thus Theorem 1.4 does not cover
any nonempty graph in the frozen family.

Its Corollary 1.5 (PDF page 3) gives
\[
\operatorname{rig}(G)\ge M(G)-\left\lceil\sigma(F)/2\right\rceil,
\]
where \(\sigma(F)\) is the minimum number of vertices whose deletion leaves no
\(C_3\)- or \(C_4\)-component (and still has maximum degree at most two).
Here exactly one deletion per component is necessary and sufficient, so
\(\sigma(F)=s+t\). The nearest prior quantitative bound is therefore
\[
M(G)-\operatorname{rig}(G)\le\left\lceil\frac{s+t}{2}\right\rceil.
\]

The exact universal pure-component assertion was not located as a proved
theorem or as a separately numbered conjecture in the primary-source searches
performed on 2026-09-07. It is a precise new question carved out of an
explicitly identified proof gap. This limited search finding is not a priority
or novelty claim. A repository-wide normalized-text check found no overlapping
project claim.

## Triage target

Nearest prior result: Theorem 1.4 and Corollary 1.5 above. Proposed delta:
prove Maxwell-sharpness for all pure \(C_3/C_4\) complement components, or give
one exact counterexample with its generic-rank obstruction. Verification route:
first compute exact small-instance rigidity ranks at \(d=n-1-a_n\), retaining
checkable nonzero maximal minors for positive instances; then seek a uniform
rigidity-matroid/join argument or a structural obstruction suggested by any
deficient case. A rank deficiency at one special coordinate placement is not
a counterexample.
