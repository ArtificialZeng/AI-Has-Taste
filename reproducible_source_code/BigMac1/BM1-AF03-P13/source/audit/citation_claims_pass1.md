# Citation-check pass 1: frozen claim extraction

Frozen from `paper/main.tex` before online verification on 2026-08-29. This
pass extracts claims only; it does not treat a plausible citation as verified.

## Cited claims

1. Lee--Vindas-Meléndez--Wang study Ehrhart polynomials of order polytopes of
   generalized snake posets (`LeeVindasWang2026`).
2. Their Conjecture 5.1 has an \(h^*\)-real-rootedness part and an Ehrhart-root
   disk part (`LeeVindasWang2026`).
3. Their Definition 2.1 defines the length of
   \(\varepsilon w_1\cdots w_m\) to be \(m\), while Conjecture 5.1 says
   “length \(n+1\)” (`LeeVindasWang2026`).
4. The displayed disk in Conjecture 5.1 has a positive center while the same
   sentence states a negative symmetry axis (`LeeVindasWang2026`).
5. Their Theorem 2.9 proves the fixed factor
   \(\prod_{j=1}^{m+3}(t+j)\) and the functional equation
   \(L(t)=L(-m-4-t)\) (`LeeVindasWang2026`).
6. The original paper reports verification for words of length at most 9
   (`LeeVindasWang2026`).
7. Braun--Jal prove the \(h^*\)-real-rootedness part for generalized snake
   posets and do not claim the Ehrhart disk result (`BraunJal2026`).
8. For a naturally labelled poset, the \(h^*\)-polynomial of its order
   polytope is the descent enumerator of its linear extensions
   (`Stanley1986`).
9. The source's Theorem 4.8 gives the regular-snake formula
   \(h^*(\mathbf w;z)=\sum_iD(n-i,i)z^i\) for actual length \(n-1\),
   providing a source-level cross-check of both witness vectors
   (`LeeVindasWang2026`).

## Uncited external or frontier claims requiring evidence

10. No source code or exact certificate accompanies the original paper's
    “length up to 9” sentence.
11. Through 2026-08-29, the recorded public-source search located no earlier
    proof, counterexample, or public certificate for the corrected disk
    statement.
12. The current arXiv v2 and journal/repository text retain the defective
    Conjecture 5.1 rather than silently correcting it.

## Internal claims excluded from web citation checking

13. All displayed \(h^*\)-vectors, exact factorizations, Taylor coefficients,
    rational inequalities, Routh entries, hashes, mutation-test counts, and
    counterexample conclusions are new project outputs. They require proof
    and certificate audit, not external citation matching.

