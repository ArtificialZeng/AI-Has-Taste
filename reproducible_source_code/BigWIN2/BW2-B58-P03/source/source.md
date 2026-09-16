# Frozen source — win-00058-p03

## Problem

Audit and repair Section 4 of S. Bera, arXiv:2609.03512v1, without changing the paper's definitions.

1. Decide whether a finite simple connected graph can simultaneously have a pendant vertex, diameter two, and domination number two. If the hypotheses of Theorem 4.2 are inconsistent, give the shortest rigorous proof and locate each invalid or unnecessary step in Lemma 4.1/Theorem 4.2.
2. Move to the first nonempty neighboring class: finite simple connected graphs with a pendant vertex, diameter three, and domination number two. Decide whether all such graphs have total domination number two. If false, find the least order, give an exact counterexample, and classify all counterexamples at that least order up to isomorphism. If true, prove it.
3. Independently repair the proof of Theorem 4.6. The family `H` is generated from `C5`, `G0`, and the Petersen graph by repeated degree-2 vertex duplication; Lemma 3.3 claims total domination is invariant under vertex multiplication. Preserve the base values 3, 3, and 6 and determine whether the printed `{3,6}` conclusion is correct. Do not turn a variable-name typo alone into a paper.

## Primary source and contribution boundary

- S. Bera, *On graphs with equal domination and total domination numbers*, arXiv:2609.03512v1, Definition 1.1, Lemma 3.3, Lemma 4.1, Theorems 4.2 and 4.6, PDF pp.3,6,9--11: https://arxiv.org/abs/2609.03512
- The source presents the diameter-two pendant case as a structural extreme and concludes that such a graph has `gamma_t=2` whenever `gamma=2`. It also prints a final Theorem 4.6 line setting all descendants to 3 despite the Petersen base value 6.
- Proposed delta: a coherent correction consisting of the exact vacuity diagnosis, a meaningful first nonempty replacement theorem or smallest counterexample atlas, and the repaired extremal-family proof. A mere typographical note is not sufficient.

## Cheapest decisive test and certificate

Let `a` be pendant with unique neighbor `u`; use `diam(G)=2` directly on the distances from `a`. For the diameter-three boundary, enumerate connected unlabeled graphs in increasing order, filter exactly by pendant vertex, diameter and domination number, then compute total domination by subset enumeration. Save graph6 strings, adjacency lists, witnesses, and exhaustive counts. For Theorem 4.6, verify Lemma 3.3 from the printed blow-up definition and apply it separately to the three ancestor classes.

## Provenance

Primary PDF: `batches/inbox/bigWin-58-materials/2609.03512.pdf`, SHA-256 `785df29b61d399150418f5796aa43f0d8029e0755097b2830266f64ee1309824`.

