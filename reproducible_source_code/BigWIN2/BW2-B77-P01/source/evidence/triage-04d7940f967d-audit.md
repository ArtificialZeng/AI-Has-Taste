# Triage audit (2026-09-09)

Job: `win-00077-p01-triage-04d7940f967d`.

## Inputs and source integrity

- `source.md` was read with SHA-256
  `8dac979afd6c6ebb67e2f1b23bdb42cd5c37198b8c119d9f47d4f27a0e5be1d5`;
  it was not edited.
- `checkpoint.md` and every project file matching
  `literature/*handoff*.md` were enumerated.  No such handoff file (and no
  `literature` directory) was present.
- The official arXiv v1 HTML,
  <https://arxiv.org/html/2609.05268v1>, was re-inspected on 2026-09-09.
  Definition 1 (HTML lines 48--50) gives the frozen
  eventual quantifier; Section 1.2 defines the fork and disjoint union;
  Theorem 12 (lines 400--437) gives the connected-fork value 9; and Problem 2
  (lines 456--459) asks for the disconnected diagonal classification.  The
  exact disconnected graph is not separately settled in the inspected text.
- Bounded web/arXiv searches for `"S_{2,1,1}" "K_2" Ramsey maximal planar`,
  `"fork graph" "disjoint union" edge "maximal planar" Ramsey`, and
  `"spider" "S_{2,1,1}" disconnected Ramsey planar` found no primary paper
  settling this exact case.  This is only a status-uncertain search result,
  not a novelty claim.

## Direct symbolic check of the proposed family

For each integer `m >= 3`, let `B_m` have rim
`v_0,...,v_{m-1}` forming `C_m`, two nonadjacent apices `a,b`, and every
apex--rim edge.  Colour the `2m` apex--rim edges red and the `m` rim edges
blue.

Embed the rim as a Jordan cycle on the sphere, put `a` in one complementary
disc and `b` in the other, and cone each disc to its apex.  The resulting
`2m` faces are precisely `a v_i v_{i+1}` and `b v_i v_{i+1}` (indices modulo
`m`), all triangular.  Thus `B_m` is a simple plane triangulation and hence
maximal planar.  This includes `m=3`: the graph is the triangular bipyramid
`K_5-ab`, with six triangular faces.  Also `|E(B_m)|=3m=3(m+2)-6`.

The red graph is `K_{2,m}` with bipartition `{a,b}` and the rim.  A red fork
centre has red degree at least three, so it is an apex.  The internal vertex
of the length-two arm is then a rim vertex, and its only possible distal
neighbour is the other apex.  Consequently every red fork uses both apices.
Every red edge meets an apex, so no red edge is vertex-disjoint from that
fork.  Hence there is no red `S_{2,1,1} union K_2`.  The blue graph is `C_m`,
which has maximum degree two and therefore no fork, hence no blue target.

Since `|V(B_m)|=m+2` covers every order at least five, this family has
unbounded order and satisfies the exact negation recorded in `problem.md`.
This is strong triage evidence for a disproof target, not a refereed result.

## Reproducible finite checks

The dependency-free checker `evidence/bipyramid_check.py` was rerun and passed
for every `m=3,...,40`.  A second implementation,
`evidence/triage_independent_check.py`, uses NetworkX 3.4.2 planarity and VF2
subgraph-monomorphism routines and passed for every `m=3,...,12`; its transcript
is `evidence/triage_independent_check.txt`.  These checks test the encoding and
boundary cases only; the preceding uniform argument is the evidence for all
`m`.
