# Precise original target

Provenance: `newwin-00001-p05-triage-39e6415a55b0`, triage, 2026-09-12.
The verbatim Chinese statement is frozen in `source.md`, SHA256
`dc2bdde5fef1bc7a1651940c02b76b65125ee7ad49eb26c921ac7664c0579a26`.
No correction or weakening of that statement is proposed.

For each integer k >= 3, consider every word w of length 2k+2 with exactly k
distinct letters. Two words are equivalent precisely when a bijection of their
used alphabets carries one to the other, position by position. Positions are
ordered: reversal and cyclic rotation are not additional equivalences. Each
equivalence class has one restricted growth representative with w_1=0 and
0 <= w_i <= 1+max(w_1,...,w_{i-1}), using all symbols 0,...,k-1.

Define phi on any finite word by starting with empty stack and output, reading
the input from left to right. If pushing the next letter would create stack
positions i<j<l with letters a,b,a and a != b, pop the top letter to the output
and retry the same input letter. Otherwise push it and advance the input.
When the input is exhausted, pop the entire stack to the output. Read the stack
from top to bottom; the forbidden pattern is a subsequence, not necessarily
consecutive (its reversal is the same pattern). Each iteration starts with a
fresh empty stack. Set phi^0(w)=w and phi^{t+1}(w)=phi(phi^t(w)).

A word is sorted if the positions occupied by each used letter form a single
integer interval. No ordering of the distinct letter blocks is required.
Let H_k={ [w] : |w|=2k+2, w uses exactly k letters, and phi^{k-1}(w) is
not sorted }, and let M_k=|H_k|. The requested result is a complete, uniform,
non-overlapping structural classification of H_k, with a closed expression or
a proved recurrence and sufficient initial conditions for M_k, for every k>=3.
A fixed-k census, fitted formula, or reformulation of the original simulator
does not establish this all-k classification.

## Nearest prior results and scope

Choi, Gan, Li, Zhu, *Set Partitions that Require a Maximum Number of Sorts
Through the aba-avoiding Stack*, ECA 5:1 (2025), S2R1,
[journal PDF](https://ecajournal.haifa.ac.il/Volume2025/ECA2025_S2A1.pdf),
DOI 10.54550/ECA2025V5S1R1; cached PDF/text in `literature/`.
Theorem 1.1 (p.2) gives the unique class (01...(k-1))^2 at lengths <=2k.
Theorem 1.2 (p.2) gives binom(k+1,2)+2 binom(k,2) at length 2k+1.
Lemma 3.5 (pp.4-5) already gives binom(2k+1,3)-4 binom(k+1,3)
for the length-2k+2 subclass whose first letter occurs four times and every
other letter twice. This subclass is known, not a proposed new contribution.

Journal Corollary 2.2 (p.3) implies no letter of a maximally slow input is
initially clumped, hence each letter occurs at least twice. Thus the possible
multiplicities here are (4,2,...,2) and (3,3,2,...,2); adjacent repetitions
within an otherwise unclumped letter remain allowed. Lemma 2.1 (p.3) gives
first-letter segmentation, and Proposition 3.1 (p.3) gives compatibility with
truncation, which replaces each maximal constant run by a single letter.
The arXiv v1 labels the journal's Corollary 2.2 as Corollary 2.3.

Source status: new-question, motivated by an explicitly posed broader problem.
The inspected primary sources support the neighboring results and broader
question; they do not explicitly single out this next layer as a numbered open
problem. No equivalent all-k solution was found in the bounded search; this
is not a priority guarantee. See `literature/triage-20260912.md` for the
retrieval scope and historical-registry limitations.

Proposed delta: classify and count the remaining length-2k+2 classes, including
non-first-letter quadruples and two triples. Verification route: prove a
complete first-letter inverse decomposition with truncation, then compare it
against the exact k=3,4 witnesses. All boundary reductions reaching two letters
require a separate base case; Theorems 1.1-1.2 assume at least three letters.

## Research pass 1 update (2026-09-12)

The original target above is unchanged. Exact counts now extend through k=8:
M_3,...,M_8 = 81, 272, 672, 1403, 2612, 4475. A complete forward census
through k=6 and a complete inverse census through k=8 agree on their shared
full witness sets. The inverse census retains the terminal clumped letter
and therefore does not assume the disputed deletion bridge. It is a finite
calculation, not the requested all-k structural classification.

The bridge is established computationally for k=4,...,8 but has no all-k
proof here. A sufficient stronger assertion is now isolated: for a run-free
word q on r>=3 letters, each occurring at least twice and at least two
occurring exactly twice, appending a new terminal letter cannot raise the
sorting time from r-1 to r. This assertion is unproved. The unrestricted
assertion without multiplicity/length restrictions fails already for
q=01201202, whose sorting time is two while that of q3 is three. Elementary
deletion commutation, a one-pass delay bound, an exact marker-gap recurrence,
the inverse construction, and all computation scopes are recorded in
`evidence/research-pass1-notes.md`. No candidate or novelty claim is made.

## Research pass 2 update (2026-09-12; supersedes the preceding bridge status)

B2 is false: q=01231230213421431 has five letters of multiplicities
(2,5,4,4,2), is run-free, and satisfies T(q)=4 but T(q5)=5. The complete
length-17 search found 12 such words. Full independently recomputed orbits
are in `evidence/b2-validation.json`. These words exceed the original bridge
length bound, so they do not disprove the original problem or its bridge.

A different partial theorem is now proposed for fresh review: for r>=3,
if q has multiplicities (2,...,2) or (3,2,...,2), and W is obtained by inserting
new letters each occurring in a single contiguous block, then T(W)=r if and
only if T(q)=r. Arbitrarily many new letters and arbitrary positive block
multiplicities are allowed; q need not be run-free. The complete argument in
`evidence/clumped-marker-theorem.md` uses an induction on r and an explicitly
computer-assisted base of 28,800 marked three-letter inputs, exhaustively
checked by three exact implementations. This proves the original terminal
deletion bridge for all k>=4, subject to independent verification of the
submitted argument. Boundary and held-out tests are saved separately.

The requested uniform inverse-fiber classification and count M_k are still
unfinished. The candidate scope is therefore result-note, original_status
unresolved, not a resolution of the immutable original question. The finite
M_3,...,M_8 values above have not changed. No mathematical acceptance is claimed.
