# Immutable source: win-00061-p03

## Frozen problem

Let `S` be the fixed triangulated torus encoded by Figure 1 of arXiv:2609.02701v1. Its 18 unordered triangles are the cyclic consecutive triples in the following three displayed 2-circuits:

`105374(10)`, `216587(21)`, and `023648(02)`.

Equivalently, the facets are

`105,053,537,374,741,410, 216,165,658,587,872,721, 023,236,364,648,480,802`,

with each three-digit word interpreted as an unordered triple.

Determine exactly the minimum number `c(S)` of 2-circuits in any 2-circuit decomposition of `S`, where every facet must occur exactly once. The source gives `c(S)<=3` and states without proof that `c(S)!=1`; the unresolved local boundary here is whether `c(S)=2` or `3`. Supply an explicit minimum decomposition and an independently replayable exact exclusion certificate for every smaller number. Also report the number of minimum decompositions modulo cyclic rotation, reversal when valid, and automorphisms of `S`, if that enumeration can be certified without weakening the main target.

## Primary source

- Robert W. Bell, *Circuit Decomposition for Triangulations of Surfaces*, arXiv:2609.02701v1, Definition 1, Figure 1, and Theorem 1 (PDF pp.1–2).
- URL: https://arxiv.org/abs/2609.02701
- Local evidence: `batches/inbox/bigWin-61-materials/2609.02701.pdf`
- PDF SHA-256: `903f9946c9919a6ced917bcd768f7caeaac992d8e63907b79d1c606539eafbee`.

This problem does not relabel a prior registry item. The source's no-Euler assertion must be rechecked rather than assumed.

