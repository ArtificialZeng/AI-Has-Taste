# Advance to counterexample certification

Job `newwin-00001-p06-triage-aaf5e6140737`, 2026-09-12.
Workflow outcome: advance; candidate_kind: none; original_status: unresolved.

Exact finite counts from the first enumerator, n=0,...,12:

    1, 1, 2, 5, 11, 22, 45, 89, 174, 338, 655, 1265, 2442.

The first failure of the proposed recurrence occurs at n=11:

    655 + 338 + 174 + 89 + (11-1) = 1266 != 1265.

The recurrence agrees for every n in 6,...,10. A second independently coded
enumeration agrees through 11, including the full set of 1265 members at n=11.
These are deterministic integer computations by two algorithms in the same
worker, not a fresh mathematical referee. No final resolution candidate is
being submitted in this triage role.

## Reproduce

From PROJECT_DIR:

    python3 evidence/triage_count.py
    python3 evidence/insertion_verify.py
    python3 evidence/compare_enumerations.py

Outputs are `triage_counts.json`, `insertion_counts.json`,
`insertion_members_n11.json`, and `enumeration_comparison.json`, all in evidence/.
There are no numerical tolerances, random seeds, or recurrence-based generation.

## Completeness arguments for review

First algorithm: if 1 occupies position k+1 in a 312-avoider, every entry before
1 is smaller than every entry after it, since otherwise those two entries and
1 form 312. Thus the permutation is uniquely

    (alpha+1), 1, (beta+k+1),

where alpha and beta avoid 312, of sizes k and n-k-1. Conversely this construction
avoids 312. Its longest decreasing subsequence has length
max(LDS(alpha)+1, LDS(beta)), taking LDS(empty)=0. Consequently the recursive
height parameter 4 generates exactly the permutations avoiding 312 and 54321.
Their squares are filtered directly for 132. Set equality against all n!
permutations was checked for n=0,...,7 using generic rank-based pattern tests.

Second algorithm: deleting the maximum preserves both classical avoidance
conditions. Insert the new maximum in every gap of every valid previous
classical avoider, then test 312 and 54321 by explicit index loops. Induction
gives completeness; deleting the maximum also proves uniqueness. Only after
constructing this class is square avoidance tested. In particular the algorithm
does not assume square avoidance survives deletion. It runs through n=11.

## Structural route available for the next phase

Let b_k count C_k members ending in 1. The first block rho of any nonempty
312-avoider ends in 1, and pi=rho direct-sum tau. Squaring preserves this sum.
An inversion in tau^2, together with any entry of rho^2, would form 132;
hence tau is an involution. Conversely rho^2 avoiding 132 and tau^2 increasing
are sufficient. A 312-avoiding involution is layered: it also avoids 231 by
inversion, and avoiding both forces decreasing direct-sum blocks. One elementary
proof is to locate 1: the preceding entries must decrease (else 231 with 1),
and the preceding block is below the suffix by 312 avoidance; repeat on the
suffix. Avoiding 54321 limits every decreasing block to size at most 4.

If t_m counts compositions of m with parts 1,2,3,4 (t_0=1), then

    a_n = sum_{k=1}^n b_k t_(n-k),  n>=1.

Writing T(x)=1/(1-x-x^2-x^3-x^4) yields A(x)=1+B(x)T(x).
For n>=5, a_n-a_(n-1)-a_(n-2)-a_(n-3)-a_(n-4)=b_n.
Thus the source recurrence would require b_n=n-1 for n>=6. Computation gives
b_11=9, with all nine tuples in `triage_counts.json`; this reduces a possible
human-checkable disproof to a short complete finite classification.
The reduction adapts the nearest paper's method; no novelty is claimed for it.

## Scope and operational limits

`python` was unavailable; `python3` worked. No C++ compiler was found, so the
draft `bruteforce.cpp` was not executed. The planned all-11! C++ verification
was replaced by the independent maximum-insertion verifier. Neither missing
compiler nor unexecuted code is mathematical evidence. The all-permutation
check covers only n<=7, while maximum insertion covers n<=11.

Next test: prepare and audit a complete classification of the nine members of
C_11 ending in 1, checking it against both enumerators; use this with the
direct-sum reduction to freeze the smallest exact n=11 disproof certificate.
Do not continue trying to prove the contradicted all-n recurrence. Literature
priority and independent mathematical review remain required before release.
