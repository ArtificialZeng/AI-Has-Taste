# Fresh mathematical referee report

## Frozen scope reviewed

The submitted `result-note` claim is exactly the partial lower bound
\[
m_2(4)\ge 18,
\]
equivalently: no width-exactly-two poset of order at most (17) has
`gap_P(C)>4` for every nonempty inclusion-maximal chain (C). This is not a
claim to determine (m_2(4)), test order (18), or classify minimizers. The
original problem therefore remains unresolved, as `claim.json` states.

The snapshot is internally valid. I recomputed the SHA-256 of every frozen
file and the canonical digest of the file-hash mapping; they agree with
snapshot digest
`773b222cd1fedf509957df57af7b795eafde6f5bb6767488e065844466c8b65b`.

## Reconstruction of the decisive mathematics

Fix a partition of a width-at-most-two poset into nonempty chains
(A_0<\cdots<A_{a-1}) and (B_0<\cdots<B_{b-1}), swapping the chains so that
(a\le b). Define
\[
L_i=|\{j:B_j<A_i\}|,
\qquad
U_i=\min(\{j:A_i<B_j\}\cup\{b\}).
\]
The two sequences are nondecreasing, and (0\le L_i\le U_i\le b). Conversely,
any coordinatewise nondecreasing sequence of pairs ((L_i,U_i)) with these
bounds defines a transitive order: (B_j<A_i) precisely for (j<L_i), and
(A_i<B_j) precisely for (j\ge U_i). Thus the recursion in
`evidence/enumerate_width2.py` covers every two-chain presentation. Dilworth's
theorem supplies such a presentation for every width-at-most-two poset, so
duplicates do not impair the nonexistence conclusion. The presented order has
width one exactly when (L_i=U_i) for every (i); otherwise an incomparable
cross-pair, together with the two-chain cover, proves width exactly two.

A linear extension of a presented order is a lattice path through states
((i,j)), where the prefix contains the first (i) elements of (A) and the
first (j) elements of (B). The next (A_i) is available iff (j\ge L_i).
The next (B_j) is available iff (i\ge K_j), where
(K_j=|\{i:U_i\le j\}|). Consequently the prefix and suffix path counts in
the program count linear extensions exactly. Each extension inserts (A_i)
at one unique state ((i,j)), which gives
\[
S(A_i)=\sum_{j=L_i}^{b}F(i,j)G(i+1,j)(i+j+1),
\]
and the analogous formula for (B_j). Hence (S(x)/e(P)) is the exact
expected rank; there is no floating-point comparison.

For a finite poset, an inclusion-maximal chain is exactly a saturated path in
the cover graph from a minimal element to a maximal element. After scaling by
the positive integer (e(P)), such a chain has gap at most (4) exactly when
its initial rank sum, every cover-edge rank-sum difference, and its final
rank-sum difference are all at most (4e(P)). The program's reachability test
therefore finds exactly the counterexample to the universal condition: a
minimal-to-maximal cover path satisfying all of those weak inequalities. It
marks a poset qualifying precisely when no such path exists. This also handles
the strict boundary correctly: gap equal to (4) makes the source condition
fail.

The unsigned arithmetic is safe in the stated range. Counts are at most
(n!); the nonnegative path products contributing to a rank sum partition the
linear extensions, and a rank is at most (n), so every rank sum and every
partial accumulated sum is at most (n\,n!). Also
((n+1)e(P)) is within range. For (n\le19), these quantities are below
(2^{64}). Labels need not be topologically ordered, but the repeated cover
relaxation is label-independent and (n) passes suffice for a path on (n)
vertices.

Orders (1)--(3) are disposed of directly in `problem.md`: order one has
width one, and each width-two type at orders two and three has a maximal chain
of gap at most (4). Orders (4)--(17) are therefore the complete remaining
domain for the asserted bound.

## Checks actually performed

1. I inspected the generator, both dynamic programs, exact rank-sum formulas,
   cover test, endpoint tests, strict inequality handling, data types, and
   iteration bounds line by line.
2. I reran the full order-(17) search in a fresh process. It returned exactly
   238,819,349 presentations, 238,753,814 width-two presentations, zero
   qualifying presentations, and no witnesses, agreeing with
   `evidence/search-order-17.json`.
3. I reran the full orders-(4)--(16) search. Every presentation and
   width-two count agreed with `evidence/search-through-16.json`, and every
   qualifying count was zero. Across both frozen runs this is 346,907,798
   presentations and 346,767,961 width-two presentations.
4. Independently of the submitted generator recursion, I counted length-(a)
   coordinatewise nondecreasing sequences in the triangular pair set
   (0\le L\le U\le b) by a finite dynamic program. The resulting aggregate
   presentation count agrees at every order (4\le n\le17). The number
   removed as width one also agrees at every order with
   \(\sum_{a=1}^{\lfloor n/2\rfloor}\binom{n}{a}\), the independent count of
   interleavings of the two chains.
5. I replayed `evidence/verify_width2.py`. Its independently generated and
   canonically deduplicated width-two domains through order (6) again equal
   the two-chain domains, with unlabeled counts (1,3,9,25,74) at orders
   (2,3,4,5,6). Its generic ideal-subset rank computation and explicit
   maximal-chain enumeration agree on every presentation in that range.
6. As a further fresh implementation check, I used a separate generic
   ideal-subset dynamic program and explicit cover-path DFS on 364
   deterministically selected non-chain presentations at orders (7)--(12).
   Extension counts, every rank sum, and the qualifying predicate all agreed
   with the submitted program.

These checks combine a full replay of the decisive enumeration, an independent
domain-count identity, exhaustive structurally independent checking at small
orders, and higher-order exact cross-checks. They support both completeness and
correctness rather than treating a successful run alone as a proof.

## Source comparison, contribution, and remaining limits

Within the authorized frozen evidence, the nearest cited result is Haqi's
Theorem 5.1, reported as giving width-two examples with arbitrarily prescribed
chain gap. That is an existence result and does not provide this first finite
threshold or the lower bound through order (17). The frozen literature screen
found no primary source computing the exact finite threshold, but this is
correctly presented only as a limited search, not as proof of priority. The
candidate makes no broader novelty claim.

The lower bound is a nontrivial, reproducible theorem directly narrowing the
original finite-threshold question. It is neither a toy restriction nor a
routine corollary of the cited existence theorem: its proof requires an exact
exhaustion of 346,767,961 width-two presentations, backed by a complete
two-chain encoding and exact rank and maximal-chain tests. Its immediate use is
to constrain every subsequent search or structural proof to orders at least
(18).

The genuine remaining gaps are outside the frozen candidate scope: no order-18
search or qualifying construction is supplied, (m_2(4)) is not determined,
and minimizers are not classified. Those omissions prevent a resolution of the
original problem but do not invalidate this `result-note` claim. The snapshot
does not include the cited primary PDF, so this review makes no priority
determination beyond the deliberately bounded source comparison above; the
mathematical lower bound itself does not depend on that paper's theorem.

## Verdict

**Accept.** The exact frozen `result-note` scope is correct, reproducible,
complete for orders at most (17), honestly distinguished from the unresolved
original problem, and mathematically substantive.
