# Exact verification accompanying Theorems A--C

Job: newwin-00001-p10-research-b1ee08dba39b.

Run from the project root:

    python3 evidence/check-research-moments.py

The script uses only the Python standard library and imports no older
experiment implementation. It writes `evidence/research-moment-check.json`
atomically and records source, script, and statement hashes. This is a
separate implementation by the same proposer, not an independent referee.
No numerical logarithms, numerical root solver, or random sampling is used.

## Executed coverage

- Every nondecreasing integer log-base-2 list with entries in
  {-2,-1,0,1,2}, lengths 2 through 8: 1281 lists, representing positive
  dyadic rational multisets. Direct tableaux and content-type multisets
  agree exactly. All moments through the input length agree with the
  generating-function formula. Distinct equal-output lists occur only
  at lengths 2 and 4 and always have different sums in this finite domain.
- Sixty structured samples selected after statement v1: four families
  at each length 9,10,11,12,13,14,15,16,20,22,26,34,46,60,61. They include
  constant lists, repeated clusters separated by 1000 in log coordinates,
  translated progressions, and irregular rational log coordinates with
  denominator 1009. The JSON records every input. Actual positive values
  may be interpreted as 2 raised to those rational coordinates.
- In all 1341 samples the direct output moments agree with the formal
  character expression. Complete triangular and Newton reconstruction
  succeeds in 1252. The other 89 stop at the predicted zero: 15 length-2,
  70 length-4, and four length-14 cases. A stopped reconstruction is not
  a detected collision. All 85 small length-2/4 samples are separately
  recovered exactly from S22 and their prescribed positive sum.
- The Mobius set-partition coefficient formula agrees with c_j(n) for
  every 2<=n<=64 and 1<=j<=n: 2079 exact checks. Tableaux cardinalities
  are independently counted at all these lengths. The CRT residue set
  is exactly {14,26,34,46}; the modular arithmetic identities are also
  checked for 4<=j<=2048. The infinite modular proof is in the dossier.

## Finite coefficient certificate, not an unbounded classification

For A_j=1+3^j-3*2^(j-1), one has

    A_(j+1)-A_j = 2*3^j - 3*2^(j-1) > 0  (j>=1).

The JSON lists every A_j and floor(sqrt(A_j)) for 1<=j<=26. Squaring
these integers certifies that the only square values in this range have
(j,sqrt(A_j))=(1,1),(2,2),(3,4),(5,14). Moreover

    A_26 = 2541765165034 > (10^6)^2.

Strict increase therefore proves that the complete set of coefficient
zeros for 2<=n<=10^6, at any order j>=1, is
(n,j)=(2,2),(4,3),(14,5). This is a finite length statement with a valid
stopping argument; a fixed-length cutoff on j alone would not suffice.
Together with the mathematical proof and the boundary cases, it certifies
the frozen injectivity assertion for lengths at most one million other
than 14. This computational corollary is ancillary to Theorems A--C;
neither a theorem for every length nor failure at length 14 follows.

## Negative boundary controls

The script serializes these exact unequal-sum witnesses:

    (4,1) and (2,2): both outputs are {16}, sums 5 and 4.

    (8,2,2,2) and (4,4,4,1): both outputs are
    {16 repeated 6 times, 64 repeated 8 times, 256 repeated 6 times},
    sums 14 and 13.

These verify that omitting the fixed-sum condition at the exceptional
boundary lengths would produce a false overstatement. They do not
disprove any instance of the frozen same-N problem.

## Research audit boundary

The tests corroborate the implementations and provide the stated finite
certificate. The infinite theorem rests on the symbolic argument. No
fresh referee review, formal proof assistant check, accepted novelty
claim, manuscript, or PDF was produced by this research job.
