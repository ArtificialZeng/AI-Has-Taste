# Exact five-permutation obstruction (triage evidence)

Job: `primary-20260914-pinnacle-fibers-triage-1b1fd3a827dc`.
This is a mathematical evidence note, not a manuscript or referee acceptance.

Use the definitions frozen in `problem.md`. In the nonempty fiber P_5((5)),
consider the following permutations and value-indexed inversion tables:

| Name | Permutation | iota |
|---|---|---|
| e | 12354 | (0,0,0,0,1) |
| b | 12534 | (0,0,0,0,2) |
| a | 13524 | (0,0,1,0,2) |
| c | 13452 | (0,0,1,1,1) |
| d | 13542 | (0,0,1,1,2) |

Each has exactly one interior peak, with value 5. Their induced comparisons
are e<b<a<d and e<c<d, with c incomparable to a and b.

All joins and meets of comparable pairs are forced by comparability.
For the remaining two pairs, the ambient coordinate maxima give
a join c = b join c = d: d is in the fiber and is the least ambient
upper bound, hence also the least upper bound within the fiber.
The coordinate minimum of b and c is e, which belongs to the fiber,
so b meet c = e.

For a and c, the coordinate minimum is (0,0,1,0,1), whose permutation
13254 has two pinnacles, 3 and 5. Mere nonmembership does not settle
the internal meet. Every common lower bound must have inversion table
(0,0,u,0,v) with u,v in {0,1}. These are ALL four possibilities:

| Table | Permutation | Complete pinnacle list |
|---|---|---|
| (0,0,0,0,0) | 12345 | () |
| (0,0,0,0,1) | 12354 | (5) |
| (0,0,1,0,0) | 13245 | (3) |
| (0,0,1,0,1) | 13254 | (3,5) |

Thus the only common lower bound in P_5((5)) is e, proving a meet c=e.
Consequently these five elements have all pairwise operations within the
fiber and form the pentagon N_5. In particular the required distributive
identity fails, with all operations certified in the entire fiber:

    a meet (b join c) = a meet d = a,
    (a meet b) join (a meet c) = b join e = b,
    a != b.

This gives a direct obstruction to the assertion that every nonempty
fiber is a distributive lattice. It does not rely on assuming beforehand
that this particular fiber is a lattice. A finite computation additionally
checks that P_5((5)) is a lattice with 56 elements, but that extra fact
is not needed for the obstruction. No conclusion about source part (b)
is made. A new resolution-paper candidate still requires a later research
freeze, fresh mathematical referee, and novelty review.

## Reproducibility and coverage

Run `python3 evidence/triage_exact.py`, then
`python3 evidence/verify_triage.py` from the project directory.
The first program enumerates permutations directly and computes every
internal bound. It checks all nonempty fibers for 0<=n<=4 and stops at
the first failure at n=5, sigma=(5), the sixth fiber tested at n=5.
It does not claim coverage at n=6 or n=7. Set/list admissibility agrees
with the Rusu--Tenner criterion for all lists at every enumerated n<=5.

The separate verifier does not import the discovery program. It enumerates
inversion vectors and inserts successive values to decode permutations,
recomputes all bounds from their universal properties, and directly
checks every distributive triple for all nonempty fibers at 0<=n<=4.
It reconstructs the complete 56-element fiber independently and verifies
the displayed failure without using the join-irreducible shortcut of
the discovery program. Thus n=5 is the smallest n at which a failure
can occur, within these explicitly tested definitions and boundary scope.

`triage_obstruction.json` retains the full fiber. `triage_verification.json`
retains all common upper/lower bounds for every pair of the five named
elements, and the four-point ambient lower box. Two implementations run
by one worker are not a fresh mathematical referee.
