# Lorentzian partition functions characterize connected cliques

Source mode: authorized primary-literature fallback, not a browser-generated batch.
Frozen on 2026-09-14, Asia/Shanghai. No 大WIN batch number is consumed.

## Original proposal and explicit scope clarification

Lee, Oh and Seo, *Counting homomorphisms in antiferromagnetic graphs via Lorentzian polynomials*, arXiv:2506.13659v2, Conjecture 7.1:
> The $G$-chromatic function $h_H(\mathbf{x};G)$ is Lorentzian for all antiferromagnetic graphs $G$ if and only if $H$ is a complete graph.

Original source: https://arxiv.org/html/2506.13659v2#S7

The displayed conjecture does not explicitly include connectedness. We do NOT silently interpret its literal disconnected version as the research target: products of clique partition functions give disconnected examples. The authors' later paper explicitly states the connected version in Section 6:
Joonkyung Lee and Jaehyeon Seo, *Antiferromagnetic models are clique-minimizing*, arXiv:2608.17920v1, concluding paragraph on the Lorentzian characterization.
https://arxiv.org/html/2608.17920v1#S6

The frozen original research target is that later CONNECTED version, stated precisely below. This explicit restriction is source-supported, not an original solution or a newly invented weakened conjecture.

## Exact target in fixed notation

For every finite connected simple source graph F on n >= 1 vertices, the following are equivalent:

1. F is the complete graph K_n.
2. For every finite nonempty spin set I and every real symmetric entrywise-nonnegative matrix A indexed by I with at most one positive eigenvalue, counting multiplicities, the homogeneous polynomial
   Z_(F,A)(x) = sum_(sigma: V(F) -> I) [product_(uv in E(F)) A_(sigma(u),sigma(v))] [product_(v in V(F)) x_(sigma(v))]
   is Lorentzian.

The variables x_i are common to all source vertices. A may have diagonal entries and zero weights; the source F has neither loops nor parallel edges. Degree-one nonnegative polynomials and the zero polynomial are included in the standard closed Lorentzian convention. For n >= 2, use the M-convex-support and iterated-quadratic-Hessian definition in the original paper Section 2; do not replace Lorentzian by ordinary or normalized coefficient log-concavity without proof.

Equivalently, the open direction asks: for each connected noncomplete F, construct some finite A as above for which Z_(F,A) is not Lorentzian, or refute this universal assertion with a nonclique F whose partition function is Lorentzian for every such A. A bad A for one F supports the conjecture; it does not refute it.

## Nearest known results and non-contributions

- arXiv:2506.13659v2 Theorem 3.1 proves the complete-source direction for all antiferromagnetic targets. Reproving it alone is not a new contribution.
- Section 7 already gives a P3 witness A=((0,0,1),(0,0,2),(1,2,0)) and reports K_(3,3) fails with target K_3. These are calibration examples, not new results.
- Target-specific Lorentzian chromatic symmetric functions do not establish the universal-target statement. Nor does target blow-up/induced-subgraph closure imply closure under deleting source vertices.
- arXiv:2608.17920v1 Theorem 1.2 settles the semiproper-coloring lower-bound conjecture from arXiv:2602.02450v1, Conjecture 4.2. That different known result is not this characterization.
- Current primary Section 6 still proposes the connected characterization. Bounded searches on 2026-09-14 located no inspected later resolution; global priority and completeness are not guaranteed.

## Bounded next test and admissible outcome

First verify definitions and reproduce the known P3 witness exactly. Then perform a bounded exact probe on small connected noncliques (start with P4, C4, and the paw/diamond, not an unbounded enumeration), using small rational antiferromagnetic targets such as nonnegative diagonal congruences of complete or singly-looped complete targets. Record target inertia and a failed M-exchange or an order n-2 derivative with a Hessian having at least two positive eigenvalues. Floating-point screening may suggest a candidate but is not a certificate.

The purpose is to decide whether a witness propagates to a meaningful structural infinite class or a general source-localization lemma. A small-graph table alone, the known P3/K_(3,3) examples, a disconnected-scope correction, or an arbitrarily selected finite order is not a publication. If no concrete new structural delta or discriminating next test is found, park promptly. Do not spend three research blocks automatically.

No accepted mathematics, proof, candidate manuscript or release exists at intake.
See the outer source/dedup record:
 /home/ailab/4math-open-problems/supervisor/primary-intake-20260914/lorentzian-cliques/screen.md
and its local primary captures. Comparison covers the bound 2883-row Excel corpus and current local registry; live target-conversation history is unavailable and its deduplication is not claimed.

