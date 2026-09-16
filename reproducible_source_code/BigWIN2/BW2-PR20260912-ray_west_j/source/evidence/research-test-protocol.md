# Research pass 1: declarations before new computations

Job: primary-20260912-ray-west-j-research-6795cc8901c9.
Recorded 2026-09-12, before producing or inspecting any length-8 counts.

Frozen subsidiary statements from triage (no revisions):

- (E) For every m>=1 and beta in S_m, j(beta)=m-1 if and only if beta
  is layered or colayered, with the definitions in problem.md.
- (D) For every m>=2, beta in S_m and deletion position i, writing
  gamma=std(beta with entry i removed), j(beta)<=j(gamma)+1.

All already accessible m<=7 data are treated as exploratory. The inherited
claim that length 7 was a holdout is not relied on: the present file cannot
verify the original event ordering. This follows the caution in
literature/outer-holdout-handoff.md, independently checked against the fact
that evidence/statistics-test.json already contains the length-7 histogram.

Chosen new attack: enumerate all 10! ambient permutations, deduplicating all
45 deletions of two positions. This gives exact g2 for all 8! patterns.
Test E and all 322,560 single deletions for D. Independently recompute any
violating pair using the existing insertion oracle. Also use that oracle
on every length-8 extremizer and 64 fixed-seed randomly chosen patterns.
Validate the new implementation against all existing m<=7 counts first.
No symmetry reduction or floating point arithmetic is used.

Proof direction: inspect the active pattern-(C) classification of Ray–West
to seek a structural proof of D or of E directly. Failure of D would reject
that proposed sufficient route only. Neither finite success nor a failure
of D resolves the original Problem 3.7.
