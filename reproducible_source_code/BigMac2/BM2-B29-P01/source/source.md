# bigMac-00029-p01 — exact reverse LCD-LP comparison at `(20,8)`

Using exactly the binary Gauss-phase relaxation `G_2(n,k,d)` of Definition
4.4 and the mixed joint-weight-enumerator relaxation `M_2(n,k,d)` of
Definition 5.1 in Kang--Xiong, arXiv:2609.08662v1, prove or disprove all three
claims

`G_2(20,8,7) != empty`, `M_2(20,8,7) = empty`, and
`M_2(20,8,6) != empty`.

Certification requires rational feasible points for the two positive claims
and a rational or integer Farkas certificate for mixed infeasibility at
`d=7`, each checked row by row against an independently generated exact
constraint matrix.  This is a statement only about LP relaxations; it does
not assert the existence or nonexistence of a binary LCD code.

Primary source: `batches/literature/bigMac-29/2609.08662v1.pdf`, pages
10--13.  The source explicitly calls `(20,8):7->6` a screening observation
and excludes it from its exact endpoint claims.

