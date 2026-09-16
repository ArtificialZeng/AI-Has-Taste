# Frozen problem and triage scope

The immutable original statement is `source.md` (SHA-256
`51c5a2d559d1c8a858630d9de8afe0fb10e5b862ee0f2f5b544c8d7868fe9a75`).
No correction to the source statement is proposed.

For each integer n >= 0, let S_n be the bijections of {1,...,n}, written in
one-line notation; S_0 contains the empty permutation. A permutation contains a
classical pattern sigma in S_k if some indices i_1 < ... < i_k have the same
relative order as sigma. Avoidance means that no such indices exist, and is
vacuous when k > n. Squaring means composition: pi^2(i) = pi(pi(i)).

Define C_n = {pi in S_n: pi avoids 312 and 54321, and pi^2 avoids 132},
and a_n = |C_n|. The precise target is the conjunction of

- (a_0,...,a_5) = (1,1,2,5,11,22);
- for every integer n >= 6,
  a_n = a_(n-1) + a_(n-2) + a_(n-3) + a_(n-4) + n - 1.

This concerns squares of permutations, not entrywise squares, consecutive
patterns, or three-dimensional permutations. Finite verification is evidence,
not a substitute for the all-n assertion.

Primary source: Kassie Archer and Noel Bourne, *Pattern avoidance in
compositions and powers of permutations*, arXiv:2505.05218v3,
https://arxiv.org/html/2505.05218v3#S5, inspected live on 2026-09-12.
Section 5, paragraph 2 and its displayed equation state this exact conjecture.
Theorem 4.2 treats the adjacent 4321 restriction. Source status is
`open-supported` at publication; the dated bounded literature search is in
`literature/triage-literature.md`. No later primary resolution was verified.

Proposed delta: a complete proof or counterexample for the stated 54321 case.
The verification route is independent exact enumeration, followed by
classification of the members of C_n ending in 1. A research candidate requests
fresh mathematical review and does not authorize a manuscript.

Triage observation (separate from the frozen target): exact enumeration found
the first recurrence failure at n=11, with a_11=1265 versus RHS=1266. Two
algorithms agree on the full C_11 membership set. The admitted target is now
certification of this exact counterexample, with a complete finite classification
as the next test; no corrected recurrence is substituted for the original.
See `evidence/triage-decision.md` for the original finite observation.

Research candidate, job `newwin-00001-p06-research-8a0fdffcb5e5`, 2026-09-12:
the exact first counterexample at n=11 is now supported by the complete proof
and finite certificate in `evidence/disproof.md`. A new enumerator visited all
(n-1)! endpoint tuples for every 1<=n<=11. At n=11, a separate certificate
checker verified all 4,181 distinct classical endpoints, all 4,172 square-132
exclusion witnesses, and the nine accepted squares; the complete domain size
4,181 also follows from the proved scalar minimum-element recurrence.
The direct-sum lemma gives a_n-sum_{j=1}^4 a_(n-j)=b_n for every n>=5.
Here b_11=9, whereas the original recurrence requires 10, and b_n=n-1 for
6<=n<=10. Counts reconstructed from all endpoint lists give precisely
(a_0,...,a_11)=(1,1,2,5,11,22,45,89,174,338,655,1265).

The candidate kind is resolution-paper, with original_status=disproved as
the scope submitted for review; no independent acceptance yet exists. It
asserts this exact finite disproof and first-failure order, not a corrected
all-n enumeration. The complete decisive primary HTML is copied into
`evidence/external/archer-bourne-v3.html` and is listed in claim.json.
Its Section 5 conjecture and Theorem 4.2 were checked against live v3 HTML.
`literature/research-literature.md` records the current bounded comparison;
no equivalent disproof was verified, and priority is not asserted.
