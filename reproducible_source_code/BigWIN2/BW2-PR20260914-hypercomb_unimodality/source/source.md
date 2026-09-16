# Unimodality of uniform linear hypercombs

Primary: David Galvin and Courtney Sharpe, Independent set sequence of some linear hypertrees, arXiv:2409.15555v5 (2026-01-30); journal version Australasian Journal of Combinatorics 94(1) (2026), 93--121.
https://arxiv.org/pdf/2409.15555v5
https://academicweb.nd.edu/~dgalvin1/pdf/journal/linear-hyperpaths_J.pdf

Original Question 1.10(4), with its mathematical symbol transliterated:
> Can the gap of length O(sqrt(n)) in Corollary 1.8 be shortened or eliminated?

The selected target is elimination of this gap, i.e. full unimodality for the specified hypercomb family, not the larger question about all linear hypertrees. The definitions precede Theorem1.7. In arXiv v5 they are printed pp6--7, with Note1.9 and Question1.10 on p8. In the journal copy they are pp99--100. The old v3 assertion of log-concavity is explicitly withdrawn as a proof error in Note1.9; do not treat it as a known theorem or as a counterexample.

Fix integers n>=1 and ell>=3. Start with the linear ell-uniform hyperpath P_(n,ell): n ell-element edges in a chain, consecutive edges intersect in exactly one vertex, and nonconsecutive edges are disjoint. Attach a new ell-element edge at each of the n-1 consecutive-edge intersection vertices and at one chosen private vertex of each endpoint edge. Each attached edge otherwise has ell-1 distinct new vertices. For n=1 choose TWO DISTINCT vertices of the sole spine edge as the attachment points. This gives C_(n,ell). All vertices are the union of these edges.

A strong independent set S satisfies |S intersect e|<=1 for every hyperedge e. Let c_(n,ell,k) be the number of k-element strong independent sets. For every n>=1 and ell>=3, does there exist m in {0,...,2n+1} such that
c_(n,ell,0)<=...<=c_(n,ell,m)>=...>=c_(n,ell,2n+1)?
There is no fixed n or ell cutoff. Weak independence is not the definition. The ell=2 graph-comb case is known and excluded from the research delta.

For exact arithmetic the same primary Theorem1.7 gives
C_(0,ell)(x)=1+ell*x,
C_(1,ell)(x)=1+(3ell-2)x+
 [2(ell-1)(ell-2)+(ell-1)^2+2(ell-1)]x^2+
 (ell-1)^2(ell-2)x^3,
and for n>=2,
C_(n,ell)(x)=(1+(ell-1)x)*[(1+(ell-2)x)C_(n-1,ell)(x)+x*C_(n-2,ell)(x)].
The n=0 initial polynomial is auxiliary, not a silent redefinition of the n>=1 combinatorial objects.

Known current boundary: Theorem1.7 provides the exact recurrence; Corollary1.8 leaves a possible O(sqrt(n)) central band for each fixed ell. The authors report unimodality for n<=500 and ell<=12 as finite experiments. Full all-parameter log-concavity would imply the target but is stronger; its failure alone is not a disproof of unimodality. A smaller unresolved band or an eventual theorem is partial relative to the frozen full target.

Selected 2026-09-14 via authorized primary-literature fallback, not browser generation; no 大WIN number consumed. The v5/history, current author-hosted journal copy, and bounded subsequent queries support an open investigation. No worldwide priority guarantee or completed unavailable live-conversation comparison is claimed. Raw primary PDFs/HTML are preserved in literature; source.md must remain immutable.
