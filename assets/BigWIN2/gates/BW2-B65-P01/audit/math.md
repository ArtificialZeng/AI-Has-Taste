# Fresh mathematical referee report

- Job: `win-00065-p01-referee-2caf9816d3e3`
- Frozen snapshot: `6948a0141286c660f4aaa3b14befe9feeac385f4fd97e453a4340e8893cd81b1`
- Candidate: `resolution-paper`
- Frozen original status: `proved`
- Verdict: **accept**

## Scope and integrity

I reviewed the exact universal claim in `claim.json`: for every integer
\(K\geq 1\), with \(c=10K+1\) and moves \(\{4,6,c\}\), the least eventual
period is 5 and its period-first least preperiod is \(2c+5\). I did not weaken
the quantifier, replace the nim sequence by the outcome sequence, or reinterpret
the preperiod convention.

All files named by `audit/snapshot.json` matched their recorded SHA-256 hashes.
In particular, the proof and checker hashes were respectively
`3dbe7b6734829189439f2bce30e106bc90c6982080a476de4a068e7e055b704f`
and `18f3c4f5c80e4a9d7b5920d98a0852748a6b7a1d6e43ed9dfaba95532c729a8b`.
The external PDF matched
`39457676064479f1ff52fded8697695c1ddd598f63665996b2eb889ec6fa66ca`.

## Reconstruction of the proof

Write

```text
A = 0000111122,  B = 2331020010,  D = 1121020010,
F = 112102,      W = 02101.
```

The proposed exact word is

```text
A^K 0 B D^(K-1) F W^infinity.
```

Its finite part has length
\(10K+1+10+10(K-1)+6=20K+7=2c+5\). I checked the
recurrence region by region as follows.

1. Before index \(c\), only moves 4 and 6 occur. Direct mex calculation gives
   `A` at indices 0 through 9. The ten circular predecessor pairs at offsets 4
   and 6 have mex word `A`, so this propagates through `A^K` and gives the
   separate final zero at index \(c-1\).
2. At indices \(c+t\), \(0\leq t<10\), subtraction by \(c\) reads `A[t]`.
   Accounting separately for short moves that cross the left seam gives option
   triples
   `110 210 210 020 221 301 321 131 032 212`, whose mex word is exactly `B`.
3. In each `D` block, the short predecessors are the circular entries of `D`
   at residues \(j-4,j-6\), while the \(c\)-predecessor is `A[j]`. The first
   seam is valid because `B[4:10]=D[4:10]`; all later seams are `D|D`. The ten
   option triples are
   `000 020 100 000 111 101 211 111 022 212`, with mex word `D`.
   This region is empty when \(K=1\), as the formula requires.
4. The block `F` occupies indices \([2c-1,2c+5)\). For both the `B|F` seam at
   \(K=1\) and the `D|F` seam at \(K\geq2\), its option triples are
   `000 022 103 003 111 100`, with mex word `F`.
5. For the tail beginning at \(q=2c+5\), the first six option triples are
   `212 110 020 211 000 221`, giving `021010`, including every short-move
   interaction with `F`. For later tail offset \(u\geq6\), let
   \(r=u\bmod5\) and \(h_u=G(c+5+u)\). The short options are
   \(W[r+1]\) and \(W[r-1]\), and a direct five-row mex check shows that the
   proposed value is \(W[r]\) exactly when \(h_u\ne W[r]\). This inequality
   holds on every possible source region: `D` differs pointwise from the
   aligned `WW`; `F` differs pointwise from aligned `021010`, with alignment
   valid because \(c-6\equiv0\pmod5\); and once the \(c\)-predecessor is itself
   in the tail it equals \(W[r-1]\), which differs from \(W[r]\) at all five
   cyclic positions. These ranges meet without a gap, including the empty-`D`
   case \(K=1\).

Thus the displayed word satisfies every mex recurrence for every \(K\geq1\),
not merely the sampled values of \(K\). Since the recurrence determines the
sequence successively, this proves the exact word and eventual 5-periodicity.

For minimality, the comparison immediately before the proposed start fails:
\(G(q-1)=F[5]=2\), whereas \(G(q+4)=W[4]=1\). Hence period 5 cannot start
earlier. If an eventual period \(p<5\) existed, it and period 5 would imply
eventual period \(\gcd(p,5)=1\) by the standard difference-of-periods
argument. But `W^infinity` is nonconstant. Therefore 5 is the least eventual
period, and the failed comparison proves that \(q=2c+5\) is its least
preperiod.

## Checks actually performed

- Recomputed the four finite mex tables and the seam indexing by hand from the
  block definitions, including the exceptional \(K=1\) geometry.
- Ran `evidence/verify_uniform_blocks.py`; all symbolic local identities passed,
  as did its redundant recurrence replays for \(K=1,\ldots,50,100,1000\).
- Ran `evidence/triage_check.py`; its exact recurrence checks passed for
  \(1\leq K\leq25\), always with tail block `02101` and boundary mismatch
  `2!=1`.
- Ran a separate direct integer-recurrence implementation, written independently
  of the supplied scripts, for \(K=1,2,3,7,25,100,1000\). It matched the full
  block formula through the finite prefix, verified more than one propagation
  window of 5-periodicity, reproduced the boundary mismatch, and found repeated
  tail mismatches for each candidate period 1 through 4. These finite runs are
  corroboration only; the universal quantifier is established by the local
  block proof above.

## Source comparison and contribution

The supplied PDF metadata identifies arXiv:2609.05358v1 as Hikaru Manabe's
*Purely Periodic Three-move Subtraction Games*, confirming the correction in
`problem.md`. Its pp. 1--2 use the same mex recurrence and the same convention
of minimizing the eventual period first and then the preperiod. Table 1 on
PDF p. 22 places \(a<b<2a\) and \(1\leq\rho\leq\delta-1\) in a daggered
positive-preperiod cell left conjectural by Conjecture 50. Here
\((a,b,\delta,\rho)=(4,6,2,1)\), exactly that cell. PDF p. 35 describes the
nearby \(b=a+2,\rho=1\) ultimately-bipartite result only for odd \(a\geq3\),
so it does not contain the even boundary \(a=4\). The frozen candidate proves
the substantially sharper exact nim word, least period, and least preperiod;
it is not presented as a priority claim.

The snapshot does not include Zhang's paper itself, so I did not independently
audit its theorem statement beyond Manabe's explicit summary on p. 35. No step
of the self-contained proof depends on Zhang, and the candidate makes no
publication-priority assertion, so this is not a gap in the frozen mathematical
resolution.

## Gaps and verdict

I found no unresolved mathematical gap, hidden exceptional parameter, or scope
mismatch. The proof is uniform, self-contained, treats \(K=1\), and establishes
both required minimality statements. The exact frozen candidate is accepted.
