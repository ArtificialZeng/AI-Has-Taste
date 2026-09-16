# Exact verification of the proposed proof steps

2026-09-14. Job:
`primary-20260914-arbor-ehrhart-words-research-9e9070b093b6`.

The symbolic argument in `research-proof.md` establishes the infinite
statement. This note records finite attempts to expose indexing, truncation,
or convention errors. The code was written in this pass and imports no
triage enumeration routines. This is a separate implementation, not a fresh
model-context referee report or formal proof.

Command from the project root: `python3 evidence/research_checks.py`.
The first execution succeeded and atomically saved `research_checks.json`.
All arithmetic is exact integer arithmetic, with no random sampling.

| Check | Complete domain within this test | Outcome |
| --- | --- | --- |
| Local identity (L) | b=1,...,8 and K=0,...,32; all polynomial coefficients | 264 identities; 5,676 coefficients agree |
| Operator identity (O) | b=1,...,5; N-b=0,...,8; m=0,...,4; one full-degree alternating-sign R for each triple | 225 identities; 4,950 coefficients agree |
| Box/word map and inverse | All subsets of n letter/box slots among n(m+1) slots, for n=1,...,5 and m=0,...,4; all words on [n] of length n | 80,011 subset objects; 17,065 word/dilation checks pass |
| Direct lattice/content/word enumeration | Three specified n=6 arbors; m=0,...,3 | All 12 count triples agree |

The direct cases cover a single block of size six, nested branching with
interleaved labels and a nonsingleton leaf, and two nonsingleton leaves.
Their descendant sets, blocks, and parents are serialized in the JSON.
The lattice enumeration visits all weak compositions of mn into n+1 parts,
using the last coordinate as slack; this gives each nonnegative vector of
sum at most mn exactly once. It checks the explicit descendant inequalities,
without subtree recursion. Contents are all weak compositions of n into n
parts satisfying the lower inequalities. Word enumeration visits all n^n
words. No isomorphism reduction, inferred census, or floating interpolation
is used.

For the nested branching case, the three definitions all give counts
1, 270, 4,365, 28,784 at m=0,1,2,3. Its directly enumerated non-descent
polynomial has coefficients (1,263,2496,3864,1137,39).

The complete polynomial identities and general bijection have been checked
on paper in `research-proof.md`, including m=0, K=0, empty child products,
nonempty large blocks, ties, leading/trailing bars, and adjacent bars.
No counterexample to a named proof step was found. No method-class
impossibility result is claimed. Fresh referee checking remains the next
decisive test.
