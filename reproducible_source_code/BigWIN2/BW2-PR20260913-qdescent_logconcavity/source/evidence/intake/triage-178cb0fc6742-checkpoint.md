# Checkpoint

Job: primary-20260913-qdescent-logconcavity-triage-178cb0fc6742 (triage).
Decision: advance. Original status: unresolved; candidate kind: none.

Source SHA256 remains 09b28e35bf37a42405472803e963d8cd37dce27edee55c075e7689eab2781fcb.
Read source, previous problem/checkpoint, AGENTS.md, outer intake screen,
installed skill and triage reference. Enumerated literature/*handoff*.md: none.
Independently inspected cached primary Sections 1.1, 1.2 and 2, including
Theorems 5/6, Conjecture 7 and Remark. Literal i<j and conventional i=j remain
separate. Live source version record still lists v2 dated 8 January 2020.

New exact algebraic reduction: a_k = sum_r K(m;k,r) x_r, where x_r is the
last-value inversion enumerator of size m with descent set S without m, and
K(m;k,r)=q^(k^2)([m choose k]_q-[m-r choose k]_q). See
evidence/intake/triage-kernel-reduction.md for the derivation and frozen
sufficient quadratic positivity target. Discovery checks m<=8 and frozen
holdouts m=9..12 passed: 15,015 strict-pair and 3,367 diagonal kernel quadratic
coefficients checked, no failures. These count polynomial expressions, not
scalar coefficients or arbitrary descent sets. No uniform inequality proof.

evidence/intake/triage-kernel-check.py and .json record 46,233 directly
enumerated permutations, 769 verified prefix last-value entries (all patterns
of sizes 1..7), all 49 direct a-definition cases with max S<=4, and 45 Gaussian
subset-enumeration checks (n<=8). Kernel closed forms also matched the positive
suffix sums for all m<=12. Exact integer arithmetic; 11.22 seconds. Arithmetic
helpers are shared with the intake script, while direct enumeration is a
separate calculation; this is not a fresh referee pass.

Admission is justified by the exact structural reduction and a frozen uniform
sufficient lemma with a concrete verifier, not just larger a-sequence tables.
All a_1,...,a_m have nonzero support by the positive h=1 kernel summand and
existence of a permutation with any prescribed prefix descent pattern.

Literature obstacles: full Liu–Xiao transformation source remains inaccessible;
publisher search preview supplies only partial statements. No current-open or
priority claim. Outer historical-registry comparison is supervisor evidence,
not independently replayed here; no registry payload exists in this project.
See literature/triage-screen.md for inspected primary claims, positions, URLs,
search coverage and the q-Kaplansky injection lead. q=1 and the b theorem are
known; neither is a new contribution. No manuscript was created.

One next test: prove or falsify the frozen mixed kernel inequalities by a
weight-preserving injection or positive q-Pascal decomposition.
