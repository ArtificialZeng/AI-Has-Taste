# Exact result at n=44

## Theorem

For the ordinary irreducible character table of the symmetric group `S_44`,

\[
ZF(44)=\{(1^{44})\},\qquad D(44)=1.
\]

## Proof and exhaustive scope

Defant--Hariharan--Lau--Ono Proposition 3.1 and Corollaries 4.1--4.2, applied
as detailed in `problem.md`, imply that every zero-free cycle type at `n=44`
belongs to

\[
\mathcal C_{44}=\{(1^{44}),(2^2,1^{40}),(2^4,1^{36})\}.
\]

Indeed, a zero-free type has form `(3^a,2^b,1^c)` with even `b`.  Here
`s_2(44)=4`, while `s_3(44)=0` because
`133=3*44+1=9^2+9*4+4^2`.  Thus `a=0` and `b` is one of `0,2,4`.

The identity column survives because
`chi^lambda(1^44)=dim(S^lambda)>0` for every `lambda |- 44`.

The other two candidates have the following exact zero witnesses:

| cycle type `mu` | partition `lambda` | exact value |
| --- | --- | --- |
| `(2^2,1^40)` | `(14,7,6,5,3,3,2,2,2)` | `0` |
| `(2^4,1^36)` | `(14,11,4,3,3,1,1,1,1,1,1,1,1,1)` | `0` |

Both displayed row labels sum to 44.  The exact beta-number
Murnaghan--Nakayama program `mn_scan.py` recursively generates every integer
partition by choosing each possible first part and then a partition bounded
by it.  Consequently it generates every partition exactly once; at `n=44` it
counts `p(44)=75175`.  It scanned both columns on all 75,175 rows, finding 18
and 2 zero rows respectively.  All arithmetic is integral: a rim hook of
length `k` replaces beta number `x` by `x-k`; the sign is determined by the
number of beta numbers strictly between them; the terminal value is the exact
hook-length dimension.  Low-rank tests reproduce the relevant standard `S_3`
and `S_4` columns.

The displayed witnesses were then checked by the structurally independent
program `independent_verify.py`.  This program uses no beta numbers or rim-hook
enumeration.  It specializes the Frobenius/Jacobi--Trudi identity at
`p_1=1`, `p_2=y`, and `p_k=0` for `k>2`.  Since

\[
\sum_{k\geq0}h_k t^k=\exp(t+yt^2/2),
\]

it computes the coefficient of `y^b` in
`det(h_{lambda_i-i+j})` using exact rational arithmetic and multiplies by
`(44-2b)! 2^b b!`.  For each displayed witness that coefficient, and hence
the character, is exactly zero.  Its own standard `S_3` and `S_4` tests pass.

Finally, `reproduce_table.py` reruns the reduced exact beta-number search for
every `3 <= n <= 43`, adjoining the immediate identity case at `n=1` and the
explicit exceptional two-column case at `n=2`.  Its 43-value vector agrees
entry-by-entry with Table 1 of the cited paper, and its seven survivors at
`n=43` agree with the seven types listed there.  This is a historical
implementation check, not a second proof of the two new witness values.

The reduction is exhaustive, the sole claimed survivor is proved nonzero on
every row, and each rejected candidate has an independently checked exact
zero.  Therefore the theorem follows.

## Gap list

No mathematical gap is presently known.  The claim still requires the
mandated fresh referee audit; the limited literature search recorded in
`problem.md` does not establish priority.
