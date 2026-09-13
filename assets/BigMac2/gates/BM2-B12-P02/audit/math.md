# Fresh mathematical referee report

## Frozen scope and verdict

I reviewed the `resolution-paper` claim frozen by snapshot digest
`03c3fa4dabb4b497c7bf1c1bd4cb2f0ae986deedb09d28fad45d0ab2bde8d0bf`.
The exact scope is the stated type `D_4` equality and its Condition-A
consequence for every pair of integers `p,t>=1`; it contains no assertion for
larger type `D`, Condition B, or left-orderability.

**Verdict: accept the exact frozen scope.**  The alternating-normal-form
calculation is correct, the source theorem used for the all-powers consequence
applies with its hypotheses satisfied, and the result resolves the full frozen
original question.

## Reconstruction of the decisive calculation

Write

`a=sigma'_0`, `b=sigma_0`, `c=sigma_1`, `d=sigma_2`.

I used the standard signed-permutation realization of `W(D_4)`: `b,c,d` swap
coordinates `(1,2)`, `(2,3)`, `(3,4)`, respectively, while `a` sends
`(e_3,e_4)` to `(-e_4,-e_3)`.  Direct enumeration gives 192 elements and 12
positive roots.  In this model both words

`bacbacdcbacd` and `dbcabcdcbaca`

represent `-I_4`; their prefix lengths are `0,1,...,12`.  Thus both are reduced
words for the longest element.  Matsumoto's theorem identifies their positive
Artin lifts, so the second word is a valid representative of `Delta`.

For a simple lift `underline(w)`, the right `J`-tail is the lift of the
parabolic component `w_J`: every right divisor of a simple element is simple,
and the parabolic component is the greatest element of `W_J` below `w` in
right weak order.  I independently enumerated every parabolic suffix in each
of the four required steps.  The results were:

| step | `J` | before | residual | greatest tail | lengths | parabolic suffixes |
|---:|:---:|:---|:---|:---|:---:|---:|
| 1 | `{a,c}` | `dbcabcdcbaca` | `dbcabcdcb` | `aca` | `12=9+3` | 6 |
| 2 | `{b,c,d}` | `dbcabcdcb` | `dbca` | `bcdcb` | `9=4+5` | 12 |
| 3 | `{a,c}` | `dbca` | `db` | `ca` | `4=2+2` | 3 |
| 4 | `{b,c,d}` | `db` | `1` | `db` | `2=0+2` | 4 |

For every enumerated parabolic suffix `x`, length additivity also holds in
`tail*x^{-1}`, so each `x` right-divides the displayed tail.  This proves
greatestness rather than mere maximality.  Reading the extracted tails from
left to right gives exactly

`[Delta]=(db,ca,bcdcb,aca)`.

The Coxeter left descents of the simple element `db=bd` are exactly `{b,d}`.
Consequently

`L*(Delta,S)={sigma_0,sigma_2}`.

No atom commutes with both `a` and `c`, so `S_1^perp` is empty and
`S_2 boxminus S_1={b,d}`.  The longest element in this realization is `-I_4`,
which fixes every simple reflection by conjugation; equivalently, the standard
Garside element in even type `D_4` is central.  Hence `Phi_Delta` is the
identity and the asserted set equality follows.

## Condition A and quantifiers

I checked the actual primary source, Fromentin--Godelle,
arXiv:2609.04757v1.  Its Definition 4.1 is the depth identity used in the
frozen problem.  Its Corollary 4.7 states that for a `Delta^q`-regular covering
satisfying

`L*(Delta^q,S)=Phi_Delta^q(S_2 boxminus S_1)`,

Condition A with respect to `Delta^q` holds if and only if the covering is
`Delta^q`-fixed.  Here the ambient `D_4` monoid and both induced parabolic
graphs are irreducible, the covering is proper, and centrality of `Delta`
makes it both `Delta`-regular and `Delta`-fixed.  Applying Corollary 4.7 at
`q=1` therefore gives, for every `m>=1`,

`dpt(Delta^m)-1=m(dpt(Delta)-1)`.

Taking `m=pt` and `m=p` yields, for arbitrary `p,t>=1`,

`dpt(Delta^(pt))-1=t(dpt(Delta^p)-1)`.

This is a universal deduction from the cited theorem, not extrapolation from
finitely many powers.  The endpoint cases `p=1` and `t=1` are included, and no
division or exceptional empty domain occurs.

## Independent checks and source comparison

- `python3 evidence/verify_d4_alternating.py` completed with `PASS` and reported
  group order 192, tail-suffix counts `(6,12,3,4)`, factors
  `(db,ca,bcdcb,aca)`, and left descents `(b,d)`.
- I wrote and ran `audit/referee_d4_check.py`, a separate implementation using
  signed permutations directly rather than the candidate's root matrices.  It
  independently returned the same group order, longest length 12, suffix
  counts, factors, left descents, centrality, and empty `S_1^perp`.
- The arXiv v1 record is dated 2026-09-04.  Section 4.3 explicitly conjectures
  this equality for even `D_r`, `i=1`, and states the resulting all-power
  Condition A conclusion.  The frozen problem is exactly its smallest case
  `r=4`.  A bounded exact-term arXiv search on 2026-09-07 found no separate
  resolution.  This is an honest source comparison, not a proof of priority or
  an exhaustive literature claim.

## Gaps and contribution assessment

I found no mathematical gap in the frozen claim.  The proof establishes the
greatest tails and the complete normal form, not merely a word equality or a
finite depth check.  The contribution is small but non-routine: it supplies an
exact certificate for the first explicitly open member of the source's
exceptional family and settles every quantifier in the frozen original
problem.  The bounded literature check supports only the conservative claim
that no equivalent resolution was found in the checked arXiv material as of
the review date.
