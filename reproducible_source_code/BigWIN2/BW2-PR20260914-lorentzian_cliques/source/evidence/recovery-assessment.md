# Recovery triage assessment

Job: primary-20260914-lorentzian-cliques-triage-06c34b78afa0.
Inspected 2026-09-14 Asia/Shanghai. Recommendation: advance to bounded research;
candidate kind none, original status unresolved. This is not referee acceptance.

The interrupted first worker's opening checkpoint assertion of completed triage
was a draft assessment. The recovery handoff reports that its final result was
not accepted by the runner. This worker does not alter that history or scheduler
state. Exactly one handoff was present and read:
`literature/triage-recovery-handoff.md`.

## Verification of the preserved structural argument

The original `evidence/even-cycle-argument.md` was read and is retained unchanged
as historical evidence, SHA256
`50389639aaba8520ef35886870792b29d397506e2610216cb2835eca984bb55b`.
Its cycle calculation survives this triage check, with a correction to the
separate continuation paragraph below.

For the fixed target A=[[0,1,1],[1,0,1],[1,1,1]], admissibility follows from
the characteristic polynomial (z+1)(z^2-2z-1): exactly one root is positive.
Each valid assignment is an ordered pair of disjoint independent sets assigned
spins 1 and 2; the remaining vertices receive the unrestricted spin 3.

For C_(2k), k>=2, the only size-k independent sets are its two alternating
parts: equality in the cyclic spacing bound forces each gap to be one vertex.
Thus the ordinary coefficients used by the derivative are 0, 2, and 2k as
stated in the saved argument. For the two vertices of spin 3, the three
disjoint cases contribute

    adjacent:                         (2k)*2,
    nonadjacent, opposite parity:     (k^2-2k)*4,
    same parity:                      k(k-1)*2.

Deleting adjacent vertices leaves one even path; the second case leaves two
even paths; the third leaves two odd paths, whose two imbalances must cancel.
These cases exhaust unordered pairs, including k=2. Their sum is 6k(k-1).

For beta=(k-1,k-1,0), each Hessian entry is
c_(beta+e_i+e_j) times the factorial product of beta+e_i+e_j.
Consequently H=2(k!)^2 M, where

    M = [[0,1,1],[1,0,1],[1,1,6(k-1)/k]].

The eigenvalue on (1,-1,0) is -1. The other two real eigenvalues have
product -det(M)>0 and sum trace(M)+1>0, since det(M)=-4+6/k<0.
Both are positive. This is a quadratic derivative obstruction for every k>=2;
no support-exchange assertion is needed for this negative test.

`recovery-check.py` separately reconstructs all Hessian entries by exact
independent-set-pair enumeration for k=2..7. Its output `recovery-check.json`
agrees with the older labeled-assignment Hessians for k=2..5. The readonly
outer verifier and its saved JSON named by the handoff were inspected; their
k=2..7 coefficient values agree with this new local run. These are distinct
implementations of finite checks, not statistical independence or an all-k
proof. The all-k evidence is the combinatorial argument above.

## Correction to the previous next test

The unqualified claim that K_(k,k) has c_(k-1,k-1,2)=2k^2 is false at k=2.
In K_(2,2), the two proper colors each occur once, so any ordered pair of
distinct vertices works: c_(1,1,2)=4*3=12, not 8. This agrees with C4.

For k>=3, a nonempty independent color class of K_(k,k) lies in one part.
Two disjoint classes of size k-1 cannot lie in the same part because
2(k-1)>k. There are two choices of orientation and k choices of the omitted
vertex in each part; hence c=2k^2. The corrected range is therefore k>=3.
Exact boundary values for k=2..7 are 12,18,32,50,72,98. The correction concerns
only the continuation example and does not change the even-cycle certificate.

## Decision and contribution limits

Nearest prior result: clique sufficiency and known isolated nonclique witnesses.
Proposed delta: one explicit admissible three-spin target excludes every even
cycle, a natural infinite family. Verification route: the above coefficient
count, factorial normalization, and exact inertia. This is concrete enough
for a bounded research pass. Novelty and whether the result has sufficient
mathematical value remain unverified; no paper or candidate is authorized by
this recommendation. The connected characterization remains unresolved.

One next test: for k>=3 and connected bipartite F on 2k vertices whose only
maximum independent sets are its two size-k parts, express c_(k-1,k-1,2)
using the component bipartitions after deleting two vertices, and test a
natural separator condition forcing c>2k^2. Require K_(k,k) to give equality
for k>=3 and retain K_(2,2)=C4 as the strict k=2 boundary exception. Keep the
even-cycle argument as the fallback scope; do not expand to an unbounded
enumeration. No general separator theorem is claimed here.
