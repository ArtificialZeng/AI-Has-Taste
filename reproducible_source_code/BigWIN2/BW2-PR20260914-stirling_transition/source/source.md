# Fixed-column sign transition for signless Stirling numbers

Primary-source mathematical transcription frozen on 2026-09-14; this is an authorized primary-literature fallback, not a browser-generated batch.

## Original assertion and scope

Let c(n,k) count permutations of n elements with k cycles. For each integer k>=1, ask whether there is an integer N_k such that, with
D_k(n)=c(n,k)^2-c(n-1,k)c(n+1,k),
one has D_k(n)>=0 for every integer 1<=n<N_k and D_k(n)<=0 for every integer n>=max(1,N_k).
Use c(0,0)=1 and c(n,k)=0 outside 0<=k<=n. Equality is allowed; no unique numerical threshold is asserted. The k=0 boundary can be recorded separately. Do not replace the all-k, all-n assertion by eventual convexity, a finite table, or fixed small k and then claim the original solved.

## Provenance

Jinting Liang and Bruce E. Sagan, Log-Concavity and Log-Convexity via Distributive Lattices, Order 43, article21 (2026), DOI10.1007/s11083-026-09735-2.
The published Section8.2, Conjecture8.8, printedp31, states this change of log-shape. The arXiv2408.02782v1 version labels the same assertion Conjecture8.9. Authors report testing 1<=k<=n<=100; that is prior finite evidence, not a proof.
Primary published PDF: https://users.math.msu.edu/users/bsagan/Papers/Old/lclc%20-%20pub.pdf
Primary old full HTML: https://arxiv.org/html/2408.02782v1
Current version history: https://arxiv.org/abs/2408.02782
Published metadata: https://doi.org/10.1007/s11083-026-09735-2

## Nearby result and proposed contribution

The source's Theorem7.2 concerns second-kind fixed columns, not this first-kind transition. Salas arXiv2607.04217v1 Theorems1.4/1.5 concern fixed rows and row-generating polynomials. Those displayed statements are not this assertion; further transformations must be checked, not dismissed by title.
Recent primary text: https://arxiv.org/html/2607.04217v1

Target: a complete proof or exact contrary sign reversal; a nontrivial uniform partial theorem may qualify only with its own frozen narrower scope and original_status=unresolved. A known corollary or isolated small-k calculation without material new value must be parked.

## First bounded test and access limits

Start with exact recurrence c(n,k)=(n-1)c(n-1,k)+c(n-1,k-1), cross-check small rows independently, inspect the sign words with zero coefficients and equality treated correctly, and seek a sign-persistence lemma or exact violation. No outer experiment is claimed.

Outer screen compared complete2883 Excel records and687 registry entries; the five query matches are unrelated semantic neighbors, not this object. Conversation-side comparison is unavailable and not claimed. Bounded current primary searches found no inspected resolution; open-supported is not a worldwide guarantee. Detailed source/version/dedup receipts and local captures are in literature/outer-intake-handoff.md when copied. The author-hosted PDF was readable through web extraction, but a direct download returned a212-byte HTML challenge, not a PDF. A genuine1051126-byte arXiv HTML capture is available.
