# Mathematical referee report

**Verdict: accept the exact frozen candidate.**

Referee job: `primary-20260914-partition-jumps-referee-3e24090a324e`.
Snapshot digest:
`fce4053e5a3907860b747c9542daeb32f9d40fbb83dae61c32423ee9941797aa`.
Review date: 2026-09-14.
Frozen kind: `result-note`. Frozen original status: `unresolved`.

This is a fresh-context mathematical review of the supplied candidate, not
external peer review or a claim of statistical independence. No agents,
other model processes, or background workers were used. I read the frozen
source, interpretation, claim, snapshot, and relevant listed evidence;
I did not consult checkpoints, scheduling state, prior review decisions,
or earlier job transcripts. The immutable source and all other frozen
files remain byte-for-byte unchanged.

## Scope decision

Acceptance covers every quantitative assertion in `claim.json`:

- For every integer n >= 2, D_delta(n) is zero at 2 and 3, one at
  4 through 10 and at 12 and 13, and two at 11 and every n >= 14.
- For every n >= 10, with T_s <= n < T_(s+1),
  4s-8 <= D_d(n) <= 4s+2. In particular the leading term is
  4 sqrt(2n) with a uniform bounded additive error.
- The stated necessary and sufficient condition for a dimension jump of
  magnitude two holds for every edge oriented toward nondecreasing support.
- The lower bounds have witnesses for every n in their claimed ranges,
  rather than only on triangular numbers or another subsequence.

The original workflow status remains `unresolved` exactly as frozen.
The quantitative growth questions are settled within this candidate;
the separate qualitative localization question is explicitly outside the
accepted conclusion. Neither a complete exact formula for D_d nor a global
or statistical description of where large jumps concentrate is accepted.
No weakening or repair of the candidate was needed in this review.

## Source comparison and hypotheses

The graph convention was checked against Sections 2.1–2.2 and 3.1 of
[Jump and Gradient Invariants](https://arxiv.org/html/2605.28981v1).
The zero recipient creates a new row, equal-size donors and recipients
require distinct rows, and identity moves are excluded. Its local dimension
is the largest clique through the vertex minus one, as in the candidate.
Section 8.6 asks the two growth questions and separately asks about
localization. Sections 3.2 and 4 provide the support bound and transition
framework, without either sharp quantitative conclusion under review.

[Degree theory, Theorem 2.2](https://arxiv.org/html/2603.27248v1)
gives d=r(r-1)+A+B, where A counts nonunit gaps including the gap to zero,
and B counts repeated sizes. The convention agrees with the dossier.
That paper's maximum-degree results concern a vertex maximum, not the
maximum difference over adjacent pairs.

[Local Morphology, Theorem 7.1](https://arxiv.org/html/2603.18696v1)
gives the two capacity families used in the proof. The singleton and unit-gap
indicators, including a_(r+1)=b_0=0, agree exactly. Its Section 2 explicitly
identifies the corner-transfer graph with the row-transfer convention here.
[Local Complexity, Background Proposition 3.1](https://arxiv.org/html/2606.20773v1)
reproduces the same formula. I checked the relevant statements in both live
primary text and the frozen captures where available; the original local
morphology paper was inspected live. No restriction on support, multiplicity,
or minimum n has been omitted from the imported formula.

[Support and Support Jumps, Theorem 3.4 and Sections 2–4](https://arxiv.org/html/2604.11837v1)
already supply exact support birth/death accounting, the triangular support
maximum, and the quadratic degree baseline. These are prior inputs. The
inspected results do not state the sharp dimension-jump attainment set,
the submitted equality-edge criterion, or the degree-jump leading coefficient.

## Reconstruction of the dimension argument

Let e(v)=delta(v)-r(v). A row capacity is r+1-a_i-b_i, and a column
capacity is at most r. Thus e=1 precisely when some repeated size x has
x-1 absent, which necessarily means x >= 2: this is H. If H fails, every
row has capacity at most r. All rows have capacity r-1 precisely when
every size is single and every augmented gap is one, namely the staircase
S_r=(r,...,1). Its boundary columns have capacity r-1. Otherwise at least
one row has capacity r. Hence e=-1 for S_r, e=1 for H, and e=0 otherwise.
This includes r=1. The reformulation is a consequence of the attributed
formula, not a separate novelty claim.

I checked the two support restrictions directly from a legal transfer.
At a staircase, an existing recipient has a different size from the donor;
the excluded identity case is the only way an output could restore one of
those original sizes. Both sizes therefore disappear, while only the new
maximum r+1 can be born. With a new recipient, a donor p >= 2 disappears
and both positive outputs were already present. Every staircase neighbor
has smaller support. S_1 has no edge and lies outside n >= 2.

A support increase of two needs two distinct positive births and no death.
In particular p-1 is absent initially, p > 1, and p survives the removal
of the donor. Therefore p was repeated, giving H at the starting endpoint.
If donor and recipient have the same size, survival requires at least three
copies; this strengthens, rather than invalidates, the conclusion. A unit
donor or coincident outputs cannot yield two distinct positive births.

For the support-oriented edge, write k=r(mu)-r(lambda), e=e(lambda),
and f=e(mu). The difference is k+f-e. The complete relevant case split is:

| k | Restrictions | Range of k+f-e | Equality at magnitude two |
|---|---|---|---|
| 0 | e,f in {0,1} | [-1,1] | Impossible |
| 1 | e in {0,1}; f in {-1,0,1} | [-1,2] | e=0, f=1 |
| 2 | e=1; f in {-1,0,1} | [0,2] | f=1 |

These restrictions follow from the two lemmas, so no unproved independence
of endpoint types is being assumed. The equality conditions are sufficient
by substitution and necessary because these ranges have no value -2.
They are exactly the conditions in `claim.json`. Equal-support orientation
ties are harmless because no such edge has magnitude two.

The exceptional edges at n=11 and n=14 have dimensions 2 and 4 by the
three-case formula. For n >= 15, k=n-11 >= 4 in the displayed witness
(k,4,4,3) to (k,4,4,2,1). At k=4, the support changes from two to three;
at k >= 5 it changes from three to four. In both cases the lower endpoint
is neither H nor a staircase and the upper endpoint is H. Coincidence of
the added part with size 4 is thus covered explicitly. The antenna edge
(n) to (n-1,1) supplies a jump of one for every n >= 4. The two small
graphs at n=2,3 have constant local dimension one.

The remaining finite exclusions were verified independently as described
below. These exclusions and the all-n witnesses prove the complete
attainment set, including the isolated value n=11 and the gaps at 12,13.

## Reconstruction of the degree argument

Inserting a size between consecutive augmented support values splits one
gap into two positive integer gaps. Its contribution to A changes by at
most one. Insertion above the maximum adds at most one; deletion reverses
these operations. This includes the bottom gap to zero and empty support
as an intermediate set operation. A transfer changes support membership
at at most four positive sizes, so |Delta A| <= 4. It changes the indicator
of multiplicity at least two at at most four sizes, so |Delta B| <= 4,
including equal donors and recipients and coincident outputs.

Consequently the degree difference differs from the difference of r(r-1)
by at most eight. A partition of n has r <= s because its distinct positive
sizes alone sum to at least T_r. For s >= 4 and supports differing by at
most two, the largest quadratic difference is
s(s-1)-(s-2)(s-3)=4s-6. This proves the stated upper bound 4s+2.

Write n=T_s+q, 0 <= q <= s. The two witness partitions are
(s+q,s-1,...,1) and (s+q,s-1,...,4,3,3). Combining the unit row with
the row of size two is a legal move. Their supports are s and s-2;
their (A,B) pairs are (1[q>0],0) and (1+1[q>0],1).
The degree difference is exactly 4s-8. For s=4 the middle range in the
second partition is empty, and all these statements still hold.

There is no limiting exchange or nonuniform parameter here. In particular
s < sqrt(2n) < s+3/2 follows from the triangular inequalities and directly
makes the claimed additive error absolute (an error bound of 14 suffices
for n >= 10).

## Independent exact verification

I wrote `audit/referee_check.py` without importing or executing the proposer
program. It expands the partition generating product coefficient by
coefficient, generates transfers using literal donor and recipient row
indices, and deduplicates resulting partitions. It computes every local
dimension by an exact maximum-clique search on the resulting neighborhood
graph. The clique search enumerates choices in index order; its only pruning
rule discards a branch when the chosen clique plus all remaining candidates
cannot improve the incumbent. Thus its upper bounds do not assume either
published invariant formula or the proposed dimension-jump theorem.

Command actually run: `python3 audit/referee_check.py`.
It exited successfully and wrote `audit/referee_check.json` with:

- Every partition for 2 <= n <= 24: 7,336 vertices and 42,903 undirected edges.
- Direct local clique searches totaling 105,701 recursive nodes. Both vertex
  formulas, the claimed dimension maxima, the degree bounds where applicable,
  and the complete equality criterion agree throughout this range.
- All 371 serialized vertex records for 2 <= n <= 13 checked individually,
  including every listed clique witness's membership, cardinality, and edges.
- All 522 dimension-jump-two edges in the expanded range classified correctly.
- 315 degree-family checks, covering every q for each 4 <= s <= 24, with
  direct neighbor counts giving exactly 4s-8.
- Direct dimensions for the two exceptional witnesses and nine further
  family parameters, including 4, 5, and 10^30.
- 28,672 exact support-insertion checks.

These computations use integer and finite-set operations only. They are
finite verification, not an extrapolation to the infinite theorem. Only
the finite exceptional dimension exclusions depend on exhaustive computation
in the submitted proof; the infinite claims have the arguments above.
The proposer program's larger formula-based coverage beyond n=24 was not
independently recomputed in this pass and is not needed for acceptance.

The verifier also recomputed the canonical snapshot digest and all 16 file
hashes before and after execution. They match. In particular `source.md`
still has SHA-256
`f7b5d436d50606d2679b25bc5f17c2a79e098c16343a41802e06cae98cb393c1`.

## Contribution assessment and limits

The contribution passes as one modest, coherent result-note. The input
formulas alone give only a coarse dimension bound of four. The compatibility
restrictions on adjacent endpoint types improve that to the sharp constant
two, identify every equality edge, and combine with exact exclusions and
uniform witnesses to determine every value of D_delta. For degree jumps,
the uniform perturbation control and explicit edges determine the leading
coefficient with bounded error. This addresses the stated edgewise questions
on the full partition graph, rather than an arbitrary restricted family.
It is more than a restatement of a vertex formula. Its techniques are
elementary; no new general method or broad priority claim is warranted.

A credible use is to bound dimension changes in any transfer atlas and
classify maximal dimension transitions from endpoint multiplicity data,
while providing the correct degree-jump scale and test witnesses. The
overlapping dimension and degree conclusions should remain in one note.

The frozen bounded literature screen was assessed against the primary
locations above. I also searched live for `"partition graph" "dimension
jumps" bound`, `"partition graph" "degree-jump" growth`, `"partition graph"
"D_delta" OR "4sqrt" OR "4√"`, `site:arxiv.org "partition graph" "jump"
"dimension"`, `site:arxiv.org "partition graph" "degree jumps"`,
`site:arxiv.org Lyudogovskiy "Lipschitz"`, and `"integer partitions"
"unit transfer" "degree" bound`. The relevant primary result returned was
the original jump paper; other results included secondary summaries and
unrelated topics, which were not used as mathematical evidence.

No equivalent sharp statement was found in these inspected sources on
2026-09-14. This does not exhaust terminology from partition Gray codes,
dominance lattices, or induced Johnson graphs, or nonindexed and later work.
The intake deduplication records do not independently prove priority, and
this pass did not rerun the supervisor's external corpus search. Those
limitations are compatible with the candidate's expressly bounded novelty
language; they must be retained in any manuscript.

No unresolved mathematical gap remains in the frozen candidate. No claim
is made about formal proof-assistant certification, journal acceptance,
or the unresolved qualitative localization question. The runner should
validate `check-math` against this unchanged snapshot before dispatching
the writing phase. This referee job did not create a manuscript or PDF.
