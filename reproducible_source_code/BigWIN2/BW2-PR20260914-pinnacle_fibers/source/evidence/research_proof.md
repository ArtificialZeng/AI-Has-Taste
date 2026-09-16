# Five-permutation disproof certificate

Proposer: `primary-20260914-pinnacle-fibers-research-1f8e260fcbca`.
Research evidence for a candidate; no fresh referee acceptance is asserted.

## Exact statement

Let P be the permutations of [5] whose complete left-to-right list of
interior pinnacle values is (5). Give P the induced order in which pi <= rho
if, for every value v, the number of smaller values to the right of v in pi
is at most the corresponding number in rho. Then P is **not a distributive
lattice**. Thus the universal assertion in Liang--Sagan Question 8.6(a)
(published version), equivalently Question 8.7(a) of arXiv v1, is false,
even when restricted to nonempty fibers. Part (b) is outside the claim.

## Definitions and elementary coordinate fact

An interior position i is a peak precisely when pi_(i-1)<pi_i>pi_(i+1).
Its value pi_i is a pinnacle. Both endpoints are excluded. Write
I(pi)=(I_1,...,I_5), where I_v counts smaller values to the right of v.
Necessarily 0<=I_v<=v-1, and these coordinates determine pi uniquely:
starting with the empty word, insert v into the existing word on [v-1]
so that exactly I_v entries remain on its right. There is exactly one
such insertion position. Inserting larger values later cannot change
the number of smaller values on either side of v. This proves the
bijection with the product of the five coordinate ranges.

The order on P is the restriction of coordinate comparison. A meet or
join throughout the following proof means a greatest lower or least upper
bound among **all of P**, not just among the five displayed elements.

## Witness and proof

All entries below are permutations of [5] with precisely one peak, of value 5.

| Name | Permutation | I | Peak position |
|---|---|---|---|
| e | 12354 | (0,0,0,0,1) | 4 |
| b | 12534 | (0,0,0,0,2) | 3 |
| a | 13524 | (0,0,1,0,2) | 3 |
| c | 13452 | (0,0,1,1,1) | 4 |
| d | 13542 | (0,0,1,1,2) | 3 |

Coordinate comparison gives e<b<a<d and e<c<d, while c is incomparable
with both a and b. Comparable elements have their forced meet and join
in any induced poset. For the incomparable pairs, coordinate maxima give

    max(I(a), I(c)) = max(I(b), I(c)) = I(d).

As d belongs to P, it is the least upper bound in P for both pairs:
every upper bound has every coordinate at least that of d. Hence
a join c = b join c = d. Similarly min(I(b),I(c))=I(e) and e belongs to
P, so b meet c=e.

It remains to determine a meet c, for which the ambient coordinate minimum
(0,0,1,0,1) itself is not in P. Every common lower bound in the entire
symmetric group has a table (0,0,u,0,v) with u,v in {0,1}. By the proved
coordinate bijection, the following four possibilities exhaust them:

| I | Permutation | Complete ordered pinnacle list |
|---|---|---|
| (0,0,0,0,0) | 12345 | () |
| (0,0,0,0,1) | 12354 | (5) |
| (0,0,1,0,0) | 13245 | (3) |
| (0,0,1,0,1) | 13254 | (3,5) |

Exactly e belongs to P. Thus e is the only common lower bound of a,c
inside P and, in particular, a meet c=e. This is a certificate for the
internal meet; mere failure of closure under ambient minimum is insufficient.

All pairwise operations on the five elements have now been justified in
the whole fiber. They form the pentagon N_5 under these operations. More
directly, the distributive identity fails with every operation defined:

    a meet (b join c) = a meet d = a,
    (a meet b) join (a meet c) = b join e = b,
    a = 13524 != 12534 = b.

If P were a distributive lattice, these universally characterized internal
operations would satisfy that identity. The inequality gives the required
contradiction, whether or not other pairs in P have meets or joins. The
fiber is nonempty because it contains the five displayed permutations.
This completes the disproof of the selected universal claim.

## Dependencies, computation, and scope limits

The proof uses only the definitions, the elementary coordinate bijection
proved above, and the four-point enumeration. No lattice representation
theorem or admissibility theorem is needed. The complete primary arXiv
text, copied byte-for-byte as `evidence/external/2408.02782v1.html`, supplies
Section 6 and Question 8.7(a). Its question element is `S8.Thmthm7`.
The published question and definitions were also checked live; details and
the publication/v1 numbering distinction are in `literature/research_verified.md`.

Run `python3 evidence/research_certificate.py`. The standard-library program
cross-checks all 120 direct permutations against all 120 inversion tables,
reconstructs the full 56-element fiber, compares the retained triage fiber,
and checks universal bounds for all 3136 ordered pairs. It serializes all
common bounds for the 25 ordered pairs of named elements and the four
ambient common lower bounds of a,c. The output is
`evidence/research_certificate.json`, with exact integer data and the current
job ID. It also verifies that the entire fiber is a lattice, a supplementary
finite fact not needed for the disproof. Only the displayed distributive
triple is tested in this research run; no other n is enumerated here.

The earlier n<=4 computations remain historical evidence. Minimality in n,
larger-n classifications, a uniform description of all fibers, and counting
Question 8.6(b) are not submitted claims. No empty-fiber convention is used
to obtain this counterexample. A proof-oriented route to universal
distributivity is ruled out by the exhibited internal operations.

Known mathematical gap list for the exact statement: empty.
Pending workflow work: fresh mathematical referee and bounded novelty
assessment of this exact scope. Recalculation by the proposing worker is
not a fresh referee verdict. No manuscript has been produced.
