# Triage evidence

Provenance: `win-00050-p03-triage-a451ec619de0`

Date inspected: 2026-09-07.

## Primary source inspection

- Mou, Sun, Zhang, *The game chromatic number of generalized Mycielski graphs
  of paths and cycles*, arXiv:2609.02283v1,
  https://arxiv.org/abs/2609.02283v1.
- The supplied 16-page PDF was inspected directly. Its SHA-256 is
  `42a09d9f05b1ab5b3fe51662cab09cb61e3d5e7660703fc9840b4a8e3bc67504`,
  matching `source.md`.
- Definition 2.1 (PDF page 4) gives layers `V^0,...,V^k` and the root. For
  `k=n=3`, this yields `4*3+1=13` vertices and the edge formula in
  `problem.md`.
- Theorem 3.1 (PDF pages 6--7) supplies the five-color upper bound.
- Theorem 5.1(1) (PDF page 14) states only
  `4 <= chi_g(M_k(C_3)) <= 5` for `k>=2`; its proof uses
  `chi(M_k(C_3))=4` and `Delta(M_k(C_3))=4`.
- Proposition 2.1 (PDF page 4) concerns the ordinary, one-layer Mycielski
  construction and does not decide `k=3`.

## Literature screen

Searches performed on 2026-09-07 included the exact strings `M_3(C_3)` and
`M_2(C_3)`, variants `M_k(C_3)` and `Mk(C3)`, and combinations with `game
chromatic number`, `coloring game`, and `generalized Mycielski`. Searches also
covered the exact cited title and the broader phrase `game chromatic number
Mycielski graph`.

The only directly relevant current primary work found for generalized layers
was arXiv:2609.02283v1. Earlier primary works found concern the classical
one-layer Mycielskian, notably:

- R. Alagammai and V. Vijayalakshmi, *Game Chromatic Number and Game Chromatic
  Index of the Mycielski Graphs of Some Families of Graphs*, Applied
  Mathematics & Information Sciences 13(S1) (2019), 261--265,
  https://doi.org/10.18576/amis/13S128.
- C. Chamberlin et al., *On game chromatic number analogues of Mycielsians and
  Brooks' Theorem*, North Carolina Journal of Mathematics and Statistics 5
  (2019), 17--27,
  https://janeway.uncpress.org/ncjms/article/id/980/.

Neither is an exact result about the generalized `k=3` graph. Search snippets
were treated only as leads; the negative search result does not establish
novelty. The source's note that a prior internal project treated `k=2` was not
used as evidence for the `k=3` outcome, and no historical-registry artifact
was supplied to this job.

## Cheapest structural test

Running `python3 evidence/validate_graph.py` constructs the graph from the
formula independently. It reports 13 vertices, 24 edges, degree multiset
`[3,3,3,3,4,4,4,4,4,4,4,4,4]`, connectedness, clique number 3, and exactly
six graph automorphisms. This validates the fixed finite target and makes
automorphism-aware exhaustive minimax a bounded, replayable next test. It does
not decide the game.

## Triage decision

Advance. Nearest prior result: the 4--5 bound above. Proposed delta: the exact
`k=3` value. Verification route: a complete four-color minimax strategy DAG
and independent replay checker using both color and graph symmetries.
