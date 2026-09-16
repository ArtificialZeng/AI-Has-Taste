# Mathematical referee report

**Verdict: accept the exact frozen claim.**

Referee job: `primary-20260914-pinnacle-fibers-referee-e4cd1693ee54`.
Review date: 2026-09-14.
Snapshot digest: `577ba5aee5bfe25eb8771ec71cc2a49f173bee70d1fb42e36bfe63f900e56a82`.
Frozen kind: `resolution-paper`. Frozen original status: `disproved`.

The five specified permutations give a valid negative answer to the selected
universal distributive-lattice question. The operations are established among
all permutations of the required fiber. No substantive change of statement or
proof was needed during review.

## Frozen scope and integrity

I read `source.md`, `problem.md`, `claim.json`, `audit/snapshot.json`, and the
listed proof, checker, two numerical certificates, source-comparison note, and
relevant passages of the two frozen primary HTML files. No unlisted project
research files, checkpoint, scheduling state, owner verdict, or job transcript
were consulted. The proposing checker was inspected but not imported or run.
No other agent or worker was used.

All ten file hashes in the snapshot match the current files. Its digest was
recomputed from the sorted-key compact JSON file mapping. The evidence list
agrees exactly with that mapping after adding `claim.json`. The frozen files
and snapshot were checked again after the independent calculation. In
particular, `source.md` retains SHA-256
`1df3a7b5d04986a7f3a816b6fd50b53b6a27d5b95b005273f1d100fe5f5bcba7`.

The accepted assertion concerns the nonempty fiber with n=5 and ordered
pinnacle list (5). A single admissible failure refutes both the unqualified
universal assertion and the explicitly disclosed nonempty-fiber reading.
No use is made of the convention for empty lattices. Cases n=0,1,2 and empty
sigma cause no gap in a disproof by n=5. Minimality in n, any classification of
other fibers, and counting/log-concavity part (b) are outside the frozen claim.
Historical small-n observations in `problem.md` are not additional accepted
theorems.

## Reconstruction from definitions

Write I_v(pi) for the number of values below v lying to its right. For each v,
0 <= I_v <= v-1. An inversion table determines a unique permutation: insert
v into the already constructed word on [v-1] with I_v letters to its right.
There is exactly one such slot. Later insertions are larger than v and do not
alter I_v. This proves the required bijection without invoking an external
theorem.

Direct inspection gives the following table. The peak positions are counted
from 1, and endpoints are excluded.

| Name | Permutation | (I_1,I_2,I_3,I_4,I_5) | Only peak position |
| --- | --- | --- | --- |
| e | 12354 | (0,0,0,0,1) | 4 |
| b | 12534 | (0,0,0,0,2) | 3 |
| a | 13524 | (0,0,1,0,2) | 3 |
| c | 13452 | (0,0,1,1,1) | 4 |
| d | 13542 | (0,0,1,1,2) | 3 |

Every peak has value 5, so all five elements belong to the entire fiber P.
Coordinate comparison gives e < b < a < d and e < c < d, with c incomparable
to a and b. Meets and joins of comparable elements have the usual forced
values, even without assuming that every pair of P has bounds.

For b,c and for a,c, the coordinate maximum is I(d). Since d belongs to P,
every upper bound in P lies above d. Thus b join c = a join c = d. The
coordinate minimum of b,c is I(e), giving b meet c = e.

The crucial meet a meet c is not inferred from ambient closure. Every ambient
common lower bound has table (0,0,u,0,v), with u,v in {0,1}. The coordinate
bijection proves that exactly these four permutations need to be considered:

| Table | Permutation | Complete ordered pinnacle list |
| --- | --- | --- |
| (0,0,0,0,0) | 12345 | () |
| (0,0,0,0,1) | 12354 | (5) |
| (0,0,1,0,0) | 13245 | (3) |
| (0,0,1,0,1) | 13254 | (3,5) |

Consequently e is the only common lower bound of a,c in P; in particular,
a meet c = e. This argument excludes hidden lower bounds anywhere in the
fiber, not just among the five named elements.

All operations on the five elements are now determined in P. They give the
pentagon operations. More directly, all terms in the following identity exist:

    a meet (b join c) = a meet d = a = 13524,
    (a meet b) join (a meet c) = b join e = b = 12534.

These are distinct. If P were a distributive lattice, its uniquely
characterized operations would satisfy this identity. The contradiction
settles the claim without assuming or needing a proof that the rest of P
is a lattice. It is stronger than merely displaying a pentagon as an induced
order subset: the necessary internal operations have been certified.

## Independent exact checks actually performed

I wrote and executed `audit/referee_verifier.py`, using only Python's standard
library. Its output is `audit/referee_verification.json`. It uses a different
enumeration and coordinate calculation from the submitted program:

- All 3125 words in {1,...,5}^5 were tested for five distinct entries, yielding
  exactly the 120 permutations. Inversion coordinates were computed from
  inverse positions; peaks were detected from successive sign changes.
- The resulting tables are exactly the product of the five coordinate ranges.
  The complete fiber has 56 elements. Every serialized fiber row in both
  supplied numerical certificates agrees with this census.
- Common lower and upper sets were computed in the full fiber. Universality
  was checked by containment of each complete bound set in the proposed
  principal ideal or filter. All 3136 ordered pairs have unique meet and join.
  This last fact is supplementary finite evidence, not needed for the disproof.
- Every saved lower-bound list, upper-bound list, meet and join for all 25
  ordered named pairs agrees exactly with the independent result. The four
  ambient lower bounds of a,c and the selected distributive failure also
  agree. The triage certificate's indexed triple and outcomes were checked.

Only n=5, sigma=(5), and the one specified distributive triple were tested in
this referee calculation. There is no floating-point computation, sampled
search, symmetry reduction, or formal-proof-assistant claim. The mathematical
justification is the elementary argument above; program success corroborates
it. This is a fresh review context, not external peer review or a claim of
statistically independent mathematical discovery.

## Primary-source and contribution assessment

The frozen Liang--Sagan v1 HTML was inspected at Section 6 and Section 8.2,
including question element `S8.Thmthm7`. I also opened the live published PDF:
printed pp.15--16 use inversion tops indexed by value; printed p.30 poses
Question 8.6(a) on the ordered pinnacle fiber. The v1 question is 8.7(a).
The v1 pinnacle display has a malformed right-neighbor subscript; its
description as peak values and the adjacent-entry definition in Section 6.2
support the precise reading already frozen in `source.md`.
[Published primary source](https://users.math.msu.edu/users/bsagan/Papers/Old/lclc%20-%20pub.pdf),
[arXiv v1](https://arxiv.org/html/2408.02782v1).
The publisher record confirms Order 43 (2026), article 21, published 2 May
2026. [Publisher record](https://doi.org/10.1007/s11083-026-09735-2).

The nearest prior results do not supply this disproof:

- Rusu--Tenner, Theorems 3.4 and 3.6, characterize admissible pinnacle sets and
  their orderings. I checked the frozen theorem statements and the live
  interruption formula k_x = x-2|S_x|-1 and accompanying proof. These are
  existence criteria, not assertions about internal lattice operations.
  [Primary source](https://arxiv.org/html/2001.08185v3).
- Bouvel--Ferrari--Tenner, Proposition 1.3 and its proof, identify the ambient
  middle order with a product of chains. This does not confer distributivity
  on arbitrary induced fibers. A search within the live HTML found no
  occurrence of "pinnacle".
  [Primary source](https://arxiv.org/html/2405.08943v2).
- Schwob's June 2026 paper describes and classifies ambient middle orders.
  I checked the abstract and searched the live HTML for "pinnacle", with no
  match. This is a bounded comparison, not an audit of all consequences of
  the classification. [Primary source](https://arxiv.org/html/2606.12129v1).
- The publisher-indexed abstract and introduction of Falque--Novelli--Thibon
  concern, in part, a lower ideal of left weak order on selected orbit
  representatives. The subset and order differ from the whole fixed fiber
  here. I did not inspect that paper's full theorem proofs.
  [Primary record](https://www.sciencedirect.com/science/article/abs/pii/S0012365X23005204).
- The inspected abstract of Bozeman et al. concerns attainable pinnacle sets
  of graph labelings. Its objects differ from individual permutations of a
  fixed ordered fiber. [Primary abstract](https://arxiv.org/abs/2406.19562).

Focused searches on 2026-09-14 included combinations of "pinnacle", "middle
order", "counterexample", "distributive lattice", "Liang", "Sagan", the
two question numbers, the paper title with "correction", and the witness
13524. Searches returned the source question and the comparisons above,
along with irrelevant results. No equivalent resolution was found in the
inspected primary passages or focused results. This is not proof of priority,
an exhaustive survey, or a guarantee against unindexed or unpublished work.

The precise delta is the explicit nonempty-fiber obstruction with correct
internal operations. It resolves the selected published question rather than
merely observing failure of coordinatewise closure. Its use is to show that
fixing a pinnacle ordering is insufficient for the proposed distributive
lattice approach. Neither ambient distributivity nor the admissibility
criterion gives this conclusion alone. Its short elementary proof is
appropriate to the scope; no additional theorem or minimum length is required
to justify acceptance.

## Gaps, limitations, and disposition

No mathematical gap was found in the exact frozen statement. Correctness,
relationship to the original question, and contribution pass at this scope.
The bounded literature qualification must remain explicit. There is no
acceptance of minimality, a general lattice classification, or source part
(b), and no authorization to describe this as journal peer review.

The next workflow check is for the runner to execute `release_gate.py
check-math` on this project, including its own role-provenance checks, before
dispatching the manuscript phase. I did not read or manufacture runner role
metadata or create a manuscript. The frozen claim and decisive evidence
remain unchanged.
