# Fresh mathematical referee report

## Frozen scope and materials checked

I reviewed the `resolution-paper` claim frozen by snapshot
`d27f2c2e8ba7469a0c4c909674cffbefc2249b4cc2f819fc9a2879a5395d4ace`.
Before the review, the SHA-256 values of `source.md`, `problem.md`,
`claim.json`, `evidence/exact_replay.py`,
`evidence/exact_replay_output.json`, and
`evidence/external/2609.03890.pdf` all matched the snapshot. The original
statement is the universal claim for every real
\(0<\delta<1/6\), with the specified fractional point, strict size order,
half-open intervals, and job-saturating matchings. I did not reinterpret it as
a finite-sample or endpoint claim.

## Reconstruction from the definitions

Only \(q\) is big, because its size is \(1>1/2\), whereas \(h\) has size
exactly \(1/2\). The inequalities
\[
  \frac13+\delta<\frac12<\frac23,
  \qquad
  \frac23-\delta<\frac23
\]
show that neither share of \(q\) reaches the Step-2 threshold. Thus all three
jobs survive. On machine 0 the strict order is \(q,h,r\), since
\(1>1/2>1/3-\delta>0\). The total fractional masses are
\(2+\delta\), \(2/3-\delta\), and \(1/3\), so the five slots are
\[
 A=[0,1),\quad B=[1,2),\quad C=[2,2+\delta),\quad
 D=[0,2/3-\delta),\quad E=[0,1/3),
\]
where the first three belong to machine 0 and the last two to machines 1 and
2 respectively. There is no slot-count breakpoint in the open parameter
interval.

The machine-0 job intervals are
\[
 q:[0,1/3+\delta),\quad
 h:[1/3+\delta,1+\delta),\quad
 r:[1+\delta,2+\delta).
\]
The single intervals on machines 1 and 2 are \(q:D\) and \(h:E\). Applying
the exact half-open overlap test \([a,b)\cap[c,e)\ne\varnothing\) iff
\(b>c\) and \(e>a\) gives
\[
 N(q)=\{A,D\},\qquad N(h)=\{A,B,E\},\qquad
 N(r)=\{B,C\}.
\]
This adjacency pattern is uniform. In particular, the two parameter-sensitive
positive overlaps \(hB\) and \(rC\) both have length \(\delta>0\), while
the closest excluded contacts include \(qB\), with signed gap
\(-2/3+\delta<0\), and \(rA\), with signed gap \(-\delta<0\).
All relevant expressions retain their signs for \(0<\delta<1/6\).

I enumerated injective neighborhood choices independently by splitting on
\(q\). If \(q=A\), then \(h=B\) forces \(r=C\), while \(h=E\) permits
\(r=B,C\), giving three matchings. If \(q=D\), the choices
\(h=A,B,E\) permit respectively two, one, and two choices for \(r\), giving
five. Hence the complete list, in \((q,h,r)\) order, is
\[
 (A,B,C),(A,E,B),(A,E,C),(D,A,B),(D,A,C),(D,B,C),
 (D,E,B),(D,E,C).
\]
There are exactly eight, with no unused neighborhood choice capable of adding
another injective matching.

The resulting exact load and makespan calculation is

| Matching class | Multiplicity | Loads \((L_0,L_1,L_2)\) | Makespan |
|---|---:|---|---|
| \((A,B,C)\) | 1 | \((11/6-\delta,0,0)\) | \(11/6-\delta\) |
| \((A,E,B),(A,E,C)\) | 2 | \((4/3-\delta,0,1/2)\) | \(4/3-\delta\) |
| \((D,A,B),(D,A,C),(D,B,C)\) | 3 | \((5/6-\delta,1,0)\) | \(1\) |
| \((D,E,B),(D,E,C)\) | 2 | \((1/3-\delta,1,1/2)\) | \(1\) |

Because \(11/6-\delta>4/3-\delta>1\) throughout the open domain, this table
proves the multiset
\[
 \{(11/6-\delta)^1,(4/3-\delta)^2,1^5\},
\]
and therefore the asserted minimum and maximum. The unit-size job \(q\) also
gives the immediate lower bound that no makespan can be below 1.

## Certificate and source checks

I inspected the exact replay program rather than relying on its success flag.
It reconstructs the size order and intervals from the instance data, applies
the correct two-strict-inequality overlap test, checks affine signs on the
whole open domain, exhausts all 12 raw neighborhood choices, and calculates
the machine loads. Its endpoint-sign method is sound for affine expressions:
if both endpoint values are nonnegative and the expression is not identically
zero, it is strictly positive in the open interval (and similarly for negative
sign). Re-executing the program produced byte-for-byte the frozen output,
whose SHA-256 is
`1299a2be1a713f9e998dfb231eddb14ddca8872f5c4568d8a1d461783e49aee1`.
The independent enumeration above agrees with all eight certificate rows.

The allowlisted primary PDF fixes the same half-open convention and the same
definition of a valid matching on PDF pages 6--7. Its Theorem 2 on pages
10--11 proves existence of the \((A,B,C)\) matching and its
\(11/6-\delta\) load uniformly for all allowed \(\delta\). Measurement 4 on
page 11 reports eight matchings, minimum 1, and maximum
\(11/6-\delta\) only for \(\delta\in\{10^{-2},10^{-3},10^{-4}\}\), explicitly
as a measurement. Thus the candidate's precise delta is the symbolic,
full-open-interval census; it does not claim a new general rounding bound or
priority beyond the bounded source comparison. The bibliographic title in
`source.md` is inaccurate, as `problem.md` discloses, but the arXiv content
and frozen PDF hash identify the intended source and this does not alter the
mathematical claim.

## Gaps and verdict

I found no unresolved mathematical gap, missing parameter cell, endpoint
leakage, equality-convention error, or mismatch between the certificate and
the frozen statement. The optional multiset strengthening follows from the
same exhaustive table. The candidate proves the original claim in its full
stated scope, and the bounded contribution comparison is honest.

**Verdict: accept.**
