# Fresh mathematical referee report

## Verdict

**Accept.** The frozen `resolution-paper` claim is correct at its exact scope:

\[
ZF(44)=\{(1^{44})\},\qquad D(44)=1.
\]

This report is bound to snapshot
`2869c743f3ebcab8dc20f7aeb8dc095911d1ebb0ac80bd793ddf25eb83bc45a8`
and referee job `win-00046-p04-referee-e698f297f482`.

## Reconstruction of the decisive argument

The reduction recorded in the frozen source and precise problem applies for
`n=44 >= 3`. It says that a zero-free type must be
`(3^a,2^b,1^c)`, with `b` even, `b <= s_2(44)`, and
`a <= s_3(44)`. The numerical bounds in the submission check directly:

- `44`, `42`, `40`, and `38` are not triangular, whereas
  `44-2*4=36=8*9/2`; hence `s_2(44)=4`.
- `3*44+1=133=9^2+9*4+4^2`, so the stated 3-core criterion gives
  `s_3(44)=0`.

Thus `a=0` and the even integer `b` is one of `0,2,4`. The reduction is
therefore exhaustive and leaves exactly

\[
(1^{44}),\quad (2^2,1^{40}),\quad (2^4,1^{36}).
\]

For every partition `lambda` of 44, the value at the identity is the positive
Specht dimension, so `(1^44)` is zero-free. The two displayed witness rows in
the claim are nonincreasing positive integer sequences and both sum to 44.
Exact recomputation gives

\[
\chi^{(14,7,6,5,3,3,2,2,2)}(2^2,1^{40})=0
\]

and

\[
\chi^{(14,11,4,3,3,1,1,1,1,1,1,1,1,1)}(2^4,1^{36})=0.
\]

Each nonidentity candidate is consequently excluded by one valid row, while
the sole survivor satisfies the universal quantifier. This proves the exact
set and cardinality claimed.

## Checks performed

I checked the code and reran all three frozen computations. The beta-number
Murnaghan--Nakayama scan regenerated all 75,175 partitions of 44 and reproduced
the frozen zero counts (18 and 2), first witnesses, value ranges, and ordered
column digests. Its partition generator is exhaustive by recursive choice of
the first part with a nonincreasing upper bound. Its hook move `x -> x-k`,
height sign, conversion back to a partition, and terminal hook-length
dimension implement the standard recurrence using exact integers.

The Jacobi--Trudi verifier is structurally different. Under
`p_1=1`, `p_2=y`, and all higher power sums zero, homogeneity ensures that the
coefficient of `y^b` in `s_lambda` contains only cycle type
`(2^b,1^(44-2b))`. Multiplication by
`(44-2b)! 2^b b!` therefore recovers the desired character. I checked its
determinant signs and coefficient formula; exact rational arithmetic returned
coefficient and character zero for both witnesses.

As a further fresh check, I wrote and ran a direct diagrammatic
Murnaghan--Nakayama recurrence which enumerates subpartitions whose two-cell
skew difference is connected and contains no `2 x 2` block. This calculation
uses neither beta numbers nor Jacobi--Trudi. It passed the standard `S_3` and
`S_4` test columns and independently returned zero for both witnesses.

Finally, the frozen historical-regression program reran successfully: all 43
values for `1 <= n <= 43` matched its recorded published vector, and its seven
survivors for `n=43` matched the recorded list. This regression supports the
implementation but is not needed to turn either witness into a proof.

The canonical snapshot digest recomputed from its file mapping. Hashes of all
authorized decisive files inspected in this review matched the snapshot.
Consistent with the referee brief, I did not read `checkpoint.md` even though
the snapshot mapping contains its digest. `source.md` retained SHA-256
`a751a6ae80f49eff99139fd5df89f77b7449e572d1e55a3443a8bc6f2b4b83b9`.

## Quantifier, scope, and contribution audit

There is no empty-domain, parity, sign, division, limiting, or numerical
precision issue. Only exact integer/rational operations enter the decisive
checks. No full-column computation is needed for a rejected type, and the
positive identity degree establishes nonvanishing for every row of the only
surviving type.

The frozen source/problem record the nearest prior paper as proving the
reduction and publishing data only through `n=43`; the candidate supplies the
adjacent exact `n=44` layer requested by the original problem. It does not
silently weaken the problem, address only a toy subcase, claim an asymptotic
result, or assert priority. Under this job's instruction to use only the frozen
evidence, no broader novelty conclusion is made.

No unresolved mathematical gap remains in the frozen claim. The limited
literature search recorded in `problem.md` is not evidence of priority, but
priority is expressly outside the claim and is not needed for the exact
resolution audited here.
