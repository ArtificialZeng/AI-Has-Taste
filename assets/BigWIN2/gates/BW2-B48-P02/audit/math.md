# Fresh mathematical referee report

## Scope reviewed

I reviewed the exact frozen claim in `claim.json`, bound to snapshot digest
`ae3e8516573c1519063c1ab93ddf7beabf28b00839d6717f413b3623c54801a3`.
The claim is the full four-value statement
\[
  (E_3,C_3,E_7,C_7)=(0,0,1,1)
\]
under the definitions in `source.md` and `problem.md`.  It makes no assertion
for other values of (r), and makes no uniqueness claim.  Every file hash in
`audit/snapshot.json` was recomputed and matched the frozen value before the
mathematical checks below.

## Reconstruction and check for (r=3)

A Hamilton cycle chooses exactly one outgoing allowed arc at every tail
(x\in\mathbb Z_{12}).  For a fixed residue (j\pmod 4), balance requires the
three tails (j,j+4,j+8) to use steps (1,2,3) exactly once.  Hence the four
layer permutations give all possible balanced outgoing-step functions, with
no omitted Hamilton candidates, and their number is
\((3!)^4=1296\).

For each such function (s(x)), its selected arcs have successor map
(f(x)=x+s(x)\pmod {12}).  It can be a Hamilton cycle only if (f) is a
permutation consisting of one 12-cycle.  I independently scanned all
(3^{12}) step functions and retained those satisfying the four balance
predicates, rather than using the certificate's translation quotient.  This
reproduced exactly 1296 balanced functions.  Exactly 15 had bijective successor
maps: 12 had cycle type ((6,6)) and 3 had cycle type ((4,8)).  None had cycle
type ((12)).  These counts agree with `evidence/r3_enumeration.json` and with a
fresh replay of `evidence/verify_tuple.py` from a temporary copy.

This enumeration is exhaustive for (E_3), not merely symmetry sampled:
balance supplies the four independent permutations, and every Hamilton cycle
would occur as one of the corresponding successor functions.  Thus (E_3=0).
The definition of (C_3) existentially includes a starter witnessing (E_3),
so (C_3\Rightarrow E_3) and consequently (C_3=0).  No separate negative
chain enumeration is needed in this case.

## Reconstruction and check for (r=7)

From `evidence/r7_witness.json`, the step-at-tail tuple is

```
(1,6,4,2,5,5,7,1,4,7,1,3,7,2,3,6,6,1,2,5,3,4,5,7,2,3,6,4).
```

Direct modular addition gives the orbit from zero

```
0,1,7,8,12,19,24,26,4,9,16,22,27,3,5,10,11,14,
17,18,20,23,2,6,13,15,21,25,0.
```

The 28 entries before the return are distinct, so this is a directed Hamilton
cycle in the allowed-step circulant.  Independently sorting the seven steps at
tails (j,j+4,\ldots,j+24), for each (j=0,1,2,3), gives (1,\ldots,7).
Equivalently, for every step its four listed tails have all four residues
modulo 4.  The cycle is therefore balanced and proves (E_7=1).

For chain compatibility, I reconstructed the unique table
(\beta_j(s)) from the step-at-tail tuple and checked the proposed path

```
0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 12
```

with steps ((1,1,1,1,1,1,6)).  Its eight vertices are distinct.  Applying

\[
  \chi(x,s)=\lfloor x/4\rfloor-\beta_{x\bmod4}(s)\pmod 7
\]

to its seven arcs gives

```
0,3,5,6,1,4,2,
```

which is exactly every development colour once.  I also checked the serialized
arcs indexed by colours (k=0,\ldots,6): for each arc tail (x), if (b) is
the corresponding base tail in (H), then (b+4k\equiv x\pmod {28}), and the
head is (x+s\pmod {28}).  Thus the seven path arcs select exactly one arc
from each (H_k), proving (C_7=1).  This verification uses only the explicit
integers; CP-SAT feasibility is not used as proof.

## Source comparison and limitations

The frozen PDF's Definition 2.1, Proposition 2.2, and Lemma 2.3 agree with the
balance/orbit/development interpretation used above.  Definition 5.1 and
Lemma 5.2 give the same existential chain condition and the same colour formula
used in the (r=7) check.  Theorem 4.7 and Lemma 5.4 cover the different range
(r\equiv1\pmod4, r\ge9).  Section 9 says that failure of the ABAB mechanism
for (r\equiv3\pmod4) is not an obstruction to other starters, so the
candidate does not misuse that failure in proving (E_3=0).

The broader (r\equiv3\pmod4) family remains outside the frozen scope.  The
provided literature screening does not establish global priority for these
small cases, but the candidate makes no such priority claim; the cited primary
source does not contain these two determinations.  I found no mathematical gap
within the exact frozen four-Boolean scope.

## Verdict

**Accept.**  The exhaustive exact (r=3) argument and the directly checkable
(r=7) starter and rainbow path establish all four values at precisely the
scope claimed.  The contribution settles the full original statement rather
than a weakened subsidiary claim.
