# Fresh mathematical referee report

## Frozen scope and checks performed

I reviewed the exact `resolution-paper` claim frozen by snapshot digest
`9321a384fea2f8a429ec15c60513abbd0d01bcac9930a376dfb34109fc0ae600`.
All hashes in `audit/snapshot.json`, including the hash of `source.md`, were
recomputed and match the snapshot.  I read the original statement, its precise
interpretation, the submitted proof and certificate, the literature screen,
and the cited statements in the frozen Manabe v1 PDF.  I did not use an owner
verdict or confidence assessment.

The audit included (i) a reconstruction of the source-based positive cases,
(ii) an independent recurrence/signature implementation that did not import
the submitted Python module, (iii) a check of the parameter endpoints and word
lengths, and (iv) a direct examination of the transfer argument excluding every
possible pure period in the two negative residue classes.  I also ran the
submitted exact certificate through `k=1000`; it checked 1,999 parameter
instances and agreed with the independent implementation.  Those finite runs
are sanity checks only; the all-parameter conclusion rests on the block-local
argument below.

## Reconstruction of the positive cases

For `a=2`, `b=5`, the modulus is 7, `delta=3=1*2+1`, so `eta=1` and
`epsilon=1`; the shape is primitive and non-harmonic.  Direct substitution in
Lemma 14, the odd-`eta` case of Theorem 28, and Theorem 57 of the frozen source
gives

```
Theta_7     = {2,5},
Theta_{c+2} = {1,5},
C_{2,5}     = {3,6},
Theta_{c+5} = C_{2,5} union {2} = {2,3,6}.
```

For every `c>5`, `c!=7`, the hypotheses of Theorem 32 hold:
`gcd(2,5,c)=1`, `c>5`, and the sole additive value is excluded.  The theorem
therefore proves full nim-value pure periodicity for residues
`{1,2,3,5,6}`.  Taking the least admissible candidate gives `c+2` for residue
1, 7 for residues 2 and 5, and `c+5` for residues 3 and 6.  The minimality
statement in Theorem 32/Proposition 46 applies, so none of these periods may be
replaced by a proper divisor.  This also covers the smallest positive case
`c=6`; no hypothesis silently assumes `c>=7` or `c>=14`.

## Reconstruction of the two negative families

Let the blocks be those displayed in `evidence/fixed_shape_proof.md`.  For
`c=7k+4`, `k>=1`, the proposed prefix and tail word have lengths

```
|B^k E| = 7k+7 = c+3,
|A C^(k-1) D| = 7k+6 = c+2.
```

For `c=7k`, the domain forces `k>=2`, and the corresponding lengths are

```
|B^k F| = 7k+8 = c+8,
|H^(k-1) I J| = 7k+2 = c+2.
```

Thus both displayed words are well-defined at their endpoint values `c=11`
and `c=14`.

For either candidate word `x=U W^omega`, put `q=|U|` and `p=|W|=c+2`.
Once `n>=q+c`, the current entry and all three predecessors are in the
periodic tail.  Their ordered recurrence signature is then `p`-periodic, and
the `c`-predecessor has cyclic offset `-c = +2 (mod p)`.  It is consequently
sufficient to inspect `0<=n<q+c+p`.

I checked the claimed all-`k` reduction rather than treating a large finite
run as its substitute.  Split this finite interval at `c`, `q`, and `q+c`.
Before `q`, only a repeated `B` block and a fixed `E` or `F` endpoint occur;
the interval `[c,q)` has respectively 3 or 8 fixed positions.  On
`[q,q+c)`, the current word and its aligned `c`-predecessor word are exactly

```
rho=4:  A C^(k-1) D[0:4]   paired with   B[3:7] B^(k-1) E,
rho=0:  H^(k-1) I          paired with   B[1:7] B^(k-2) F.
```

The other offsets are only -2 and -5.  Hence a signature sees at most one
seven-symbol repeated block and its two adjacent boundaries.  Inserting an
additional aligned `C/B` or `H/B` pair adds only an already present interior
factor; it does not create a new boundary type.  In the last interval the
cyclic offsets are `-2,-5,+2`, so the same local-factor observation applies to
the cyclic words `A C^(k-1) D` and `H^(k-1) I J`.  The zero-copy boundary cases
(`k=1` in the first family and `k=2` in the second) are separate fixed cases.
This exhausts every `k`, rather than merely sampled values.

A fresh enumeration of precisely these wall, interior, and boundary types
produced 20 ordered signatures for residue 4 and 25 for residue 0.  After
forgetting predecessor order, their complete option-set/mex table is

```
{}          -> 0       {0}         -> 1
{0,2}       -> 1       {1}         -> 0
{1,2}       -> 0       {1,3}       -> 0
{0,1}       -> 2       {0,1,3}     -> 2
{0,1,2}     -> 3
{0,3}       -> 1       {0,2,3}     -> 1
{1,2,3}     -> 0
```

The last three rows occur only in the residue-0 family.  Every asserted value
is the mex of its option set.  The wall recurrence determines the sequence
uniquely by induction, so the two infinite word identities are established at
the full nim-value level.  Independent direct recurrence comparisons included
the endpoint cases and large representatives and found exact agreement; these
checks also reproduced the 20/25 signature counts.

Finally, the tail period `p=c+2` is not a period from zero:
`G(0)=0` whereas `G(c+2)=3` for residue 4 and `G(c+2)=2` for residue 0.
If a sequence had any pure period `d` and eventual period `p`, then for each
`n` one could choose `m` with `n+md>=q` and obtain

```
x(n+p)=x(n+p+md)=x(n+md)=x(n).
```

Thus an eventual period of a purely periodic sequence is already a period
from zero.  The displayed mismatch rules out every possible pure period, not
only the candidate periods, in residues 0 and 4.

## Source comparison and contribution

The frozen Manabe v1 source explicitly presents admissibility as sufficient
and the converse as Conjecture 50 outside its proved slices; the fixed shape
here is not resolved there.  The frozen literature screen records an informal
2009 statement of the same preperiod classification without proof and with a
period-table discrepancy.  That external note is not itself among the frozen
evidence files, so I do not treat its priority or wording as independently
verified in this audit.  This limitation does not support a novelty claim, and
the candidate makes none: it expressly credits the earlier statement.  The
audited contribution is instead the complete all-`c` proof and the exact
full-nim word formulae.  Those are nontrivial, reproducible, and directly
resolve the frozen original problem.

## Verdict

**Accept.**  The exact frozen scope is proved.  Correctness/evidence,
full-scope equivalence (including least periods), and contribution all pass.
The original status is `proved`, and the appropriate candidate kind is
`resolution-paper`.
