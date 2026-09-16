# Direct-sum restriction: pass 2 working evidence

Job: primary-20260912-ray-west-j-research-db44e3159ae7.
This file records research arguments and exact tests, not referee acceptance.
Final pass status: the repair and the join argument below were completed
in evidence/sum-restriction-proof.md and checked by
evidence/verify_sum_restriction.py. The exploratory wording below records
the state when the clipping counterexample was saved; it is superseded
by that proof submission, which awaits a fresh referee.

## Exact counterexample to clipping without changing the inserted pattern

Let pi=213=21 direct-sum 1. The active pattern-(C) triples

    left:  rho=21, R=(1,1), C=(1,1)
    right: sigma=12, S=(4,4), D=(3,4)

both insert to 21435. Both triples are active, R_max<S_min and
C_max<D_min. The assigned good gap is between pi(1)=2 and pi(2)=1.
Clipping every coordinate x to min(x,3) for the prefix 21 preserves both
strict inequalities and activity. However, the two insertions become 2143
and 2134, respectively. Thus coordinate clipping with sigma unchanged is
false, already at total length 3. Changing the right inserted pattern to
21 repairs this witness. The gap-restriction assertion and sum recurrence
are not refuted by it.

## Repair being checked

For a positive-column pattern-(C) configuration assigned to an internal
prefix gap of pi=alpha direct-sum beta, the whole left triple lies within
alpha. Its common insertion is tau_A direct-sum beta. The first |alpha|
original entries in the right embedding of pi occupy positions and values
at most |alpha|+2, so yield an occurrence of alpha in tau_A. The complement
of that occurrence gives a new right triple. Its row and column multisets
are the coordinatewise clips, but its inserted permutation is determined
by these two remaining points of tau_A and may differ from sigma. All
new row and column coordinates are at least the smaller of the old
coordinate and |alpha|+1, preserving the strict separations from the
left triple. This needs a complete written boundary check and replay.

The negative-column case can instead use the source's two monotone tracks:
when both entries of the assigned gap lie in one sum component, both
tracks must remain in it, because an increasing-value, decreasing-position
track cannot cross a direct-sum cut. At the join, the tracks lie on opposite
sides and their contiguous support would force a decreasing terminal
component and a decreasing initial component. These assertions still
require explicit support and endpoint checks before being called proved.
