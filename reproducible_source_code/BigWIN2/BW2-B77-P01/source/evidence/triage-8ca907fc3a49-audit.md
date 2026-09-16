# Triage verification

Job: `win-00077-p01-triage-8ca907fc3a49` (2026-09-09).

## Inputs and source status

`source.md` was read at SHA-256
`8dac979afd6c6ebb67e2f1b23bdb42cd5c37198b8c119d9f47d4f27a0e5be1d5`.
The sole `literature/*handoff*.md` file,
`literature/triage-recovery-handoff.md`, was enumerated and read as a lead,
not accepted as a conclusion.

The official arXiv HTML for 2609.05268v1,
<https://arxiv.org/html/2609.05268v1>, was inspected live on 2026-09-09.
Definition 1 (HTML lines 48--50) states the eventual-unavoidability
quantifiers; Section 1.2 (lines 87--95) defines `S_{2,1,1}` and disjoint
union; Proposition 4 (lines 340--342) gives only necessary conditions for
disconnected graphs; Theorem 12 (lines 400--437) proves the connected-fork
value 9; and Problem 2 (lines 456--459) asks for the disconnected diagonal
classification.  The inspected v1 text does not separately state the present
exact case.  Bounded arXiv-focused searches for the exact symbols and
equivalent fork/disconnected language returned no other primary-paper match.
This supports only `status-uncertain`, not priority or an exhaustive novelty
claim.

## Independent symbolic verification of the lead

For an integer `m >= 3`, let the rim vertices form `C_m`, add nonadjacent
apices `a,b`, join each apex to every rim vertex, colour all `2m` spokes red,
and colour all `m` rim edges blue.

Draw the rim as a Jordan cycle on the sphere, with one apex in each
complementary disc.  Coning each disc gives exactly the `2m` triangular faces
`a v_i v_{i+1}` and `b v_i v_{i+1}`.  Hence the graph is a simple plane
triangulation and therefore maximal planar.  This reasoning includes `m=3`,
where the graph is `K_5-ab`; it has `3m=3(m+2)-6` edges and six triangular
faces.

The red graph is `K_{2,m}`.  In any injective, ordinary non-induced red copy
of `S_{2,1,1}`, the degree-three centre must be an apex because each rim
vertex has red degree two.  The internal vertex on the length-two arm is then
a rim vertex, whose only red neighbour other than the centre is the other
apex.  Thus every red fork uses both apices.  Every red edge meets an apex, so
no red edge is vertex-disjoint from such a fork.  Therefore there is no red
`S_{2,1,1} union K_2`.  The blue graph is `C_m`, has maximum degree two, and
contains no fork, hence no blue target.  Extra host edges are irrelevant to
this non-induced-copy argument.

The orders are `m+2`, covering every integer at least five, so the family
satisfies the exact negation in `problem.md`, not merely a finite lower bound.
The two existing implementations were inspected and rerun; their new
transcript is `evidence/triage-8ca907fc3a49-checks.txt`.  Their finite ranges
are sanity checks only; the uniform argument above carries the quantifier.

## Triage decision

Advance this exact disproof target to a fresh research audit.  No manuscript
or mathematical acceptance is authorized at triage.
