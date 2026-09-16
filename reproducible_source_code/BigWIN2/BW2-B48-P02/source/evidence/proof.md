# Certificate argument for the four truth values

The claim proved by the attached finite certificates is exactly
\[
  (E_3,C_3,E_7,C_7)=(0,0,1,1)
\]
under the definitions frozen in `source.md` and made precise in `problem.md`.

## The negative values at r=3

Balance assigns one of the steps 1, 2, 3 to each tail in `Z_12`.  In any one
tail residue class `j mod 4`, the three tails are `j,j+4,j+8`, and their steps
must be a permutation of `(1,2,3)`.  Consequently the four independent layer
permutations give all and only the `(3!)^4=1296` balanced assignments.

For every such assignment the certificate forms the successor function
`f(x)=x+s[x] mod 12`.  A directed Hamilton cycle would make `f` a permutation
with cycle type `(12)`.  Exhaustive enumeration finds only 15 assignments for
which `f` is even a permutation: 12 have cycle type `(6,6)` and 3 have cycle
type `(4,8)`.  None is Hamilton.  Hence `E_3=0`; the implication
`C_3 => E_3` gives `C_3=0`.  `evidence/r3_enumeration.py` generates the domain
in two ways and serializes all 15 bijective assignments and all 112
translation-orbit representatives.  `evidence/verify_tuple.py` independently
regenerates the unsymmetrized 1296-element domain without using the orbit
reduction.

## The positive values at r=7

Let the step at tails `0,1,...,27` be

```
(1,6,4,2,5,5,7,1,4,7,1,3,7,2,3,6,6,1,2,5,3,4,5,7,2,3,6,4).
```

Its successor cycle, including the return to the start, is

```
0,1,7,8,12,19,24,26,4,9,16,22,27,3,5,10,11,14,17,18,20,23,2,6,13,15,21,25,0.
```

Thus all 28 vertices occur once.  The tails using steps 1 through 7 are,
respectively,

```
1: 0,7,10,17       2: 3,13,18,24      3: 11,14,20,25
4: 2,8,21,27       5: 4,5,19,22       6: 1,15,16,26
7: 6,9,12,23.
```

Each displayed row contains one tail from every residue class modulo 4, so the
cycle is balanced and proves `E_7=1`.

For chain compatibility, take the simple path with vertices

```
0,1,2,3,4,5,6,12
```

and steps `(1,1,1,1,1,1,6)`.  From the balanced starter the beta rows (rows
`j=0,1,2,3`, columns `s=1,...,7`) are

```
(0,6,5,2,1,4,3)
(4,3,6,5,1,0,2)
(2,4,3,0,5,6,1)
(1,0,2,6,4,3,5).
```

For a tail `x=j+4t`, calculating `t-beta_j(s) mod 7` along the path gives

```
0,3,5,6,1,4,2,
```

which are all seven development colours.  The path therefore selects exactly
one arc from every developed cycle and proves `C_7=1`.  The complete integer
checks, including the corresponding selected arc indexed by each colour, are
serialized in `evidence/r7_witness.json` and replayed without a solver by
`evidence/verify_tuple.py`.

No assertion is made here about any other value of r or about uniqueness.
