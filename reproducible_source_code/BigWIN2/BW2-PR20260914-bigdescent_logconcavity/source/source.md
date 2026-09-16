# Big-descent log-concavity for length-three pattern avoidance

Frozen source-defined mathematical target, taken from Elizalde–Rivera–Zhuang,
Counting Pattern-Avoiding Permutations by Big Descents, Annals of Combinatorics
(2026), Conjecture 4.6. DOI: 10.1007/s00026-026-00805-1.
Primary URL: https://link.springer.com/article/10.1007/s00026-026-00805-1
Accessed 2026-09-14, Asia/Shanghai. This is primary-literature fallback intake,
not a browser-generated batch.

Verbatim Conjecture 4.6 (mathematical notation rendered in Markdown):

> Let $\Pi\subseteq\mathfrak S_3$ with $|\Pi|=1$ or $|\Pi|=2$. The sequence $\{b_{n,k}(\Pi)\}_{0\le k\le n}$ is log-concave for all $n\ge0$.

The following explicit definitions reproduce the notation of Sections 1.1–1.2.
A permutation pi of [n] avoids a pattern sigma of length three when no triple
of indices i<j<l has the same relative order as sigma. It avoids Pi when it
avoids every sigma in Pi. The unique permutation of [0] is the empty word.
A big descent is an index i in {1,...,n-1} with pi_i > pi_(i+1)+1.
Let b_(n,k)(Pi) count Pi-avoiding permutations with exactly k big descents,
and use zero outside the attainable statistic range.

Prove or disprove the entire source assertion: for every n>=0, each of the
21 singleton or doubleton subsets Pi of S3, and each 1<=k<=n-1,
b_(n,k)(Pi)^2 >= b_(n,k-1)(Pi) b_(n,k+1)(Pi).
The all-zero rows (for instance Pi={123,321}, n>=5) are included.
The n=0,1 inequalities are vacuous.

Do not replace the full source target with real-rootedness or a selected
pattern family. A theorem covering only some families must be identified as
a partial result, with original_status unresolved. The known source results
and any proposed refinement belong in problem.md rather than edits here.
No assertion of global current openness or priority is part of this source.
