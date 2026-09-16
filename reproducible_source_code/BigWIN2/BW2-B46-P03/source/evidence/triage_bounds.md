# Triage evidence: literature and finite reduction

Provenance: `win-00046-p03-triage-89d6865f133e`  
Inspection/retrieval date: 2026-09-06

## Source inspection

The frozen local PDF
`/home/ailab/4math-open-problems/batches/inbox/bigWin-46-materials/2608.13599.pdf`
was hashed before use:

```text
c661b2edcda1b6d11225c5c94e8a4289ed223da6cba82702336910c38bd73d44
```

Relevant inspected locations in Yuhan Zhang, arXiv:2608.13599v1:

- Theorem 1.1 and Proposition 1.3: PDF page 2 (large-deletion-speed
  divisibility and the Goddyn--Wong gcd criterion).
- Theorem 1.6: PDF page 3 (effective bound in the middle range).
- Table 1 and Theorem 1.8: PDF page 4 (published exact census).
- Lemma 2.2: PDF page 4 (complete finite breakpoint set).
- Question 5.1: PDF page 8 (middle-range classification problem).

The current arXiv record was inspected at
<https://arxiv.org/abs/2608.13599>. It listed only v1, submitted 2026-08-01,
and supplied the same title, scope, bound, and ancillary code links. Searches
for the exact deletion-speed-12 classification and for the wording of Question
5.1 returned no separate primary result. This is a limited literature screen,
not a claim of priority or proof that no other result exists.

## Reconstruction for \(13\le n\le24\)

Put \(s=n-12\). Proposition 1.3 forces \(w=12m\). Since \(w>n-1\),
\(m\ge2\). Theorem 1.1 says equality holds exactly when
\(\gcd(12,b)>1\) for every integer \(s\le b\le ms-1\).

For \(n=14,m=2\), this interval is \(\{2,3\}\), so the criterion holds and
gives \((n,w)=(14,24)\). For \(n=13\), the interval contains the coprime
integer 1. For \(n=14,m\ge3\), it contains 5. For \(n=15,\ldots,24\),
respectively, it contains one of
\[
5,5,5,7,7,11,11,11,11,13,
\]
each coprime to 12. Thus the cited results rigorously leave exactly
\((14,24)\) in this entire regime.

## Reconstruction for \(n\ge25\)

For \(r=12\), equations (2)--(3) reduce to
\[
I(n,12)=\min\{F(1),F(5),F(7),F(11)\},
\quad
F(u)=\max\{i\le n-1:i\equiv u\pmod {12}\}.
\]
The exclusion of \(i=12\) is irrelevant for these four unit residue classes.
Theorem 1.6 requires \(25\le n\le72\) and
\[
w\le B(n):=\frac{48I(n,12)}{2(n-12)-I(n,12)}.
\]
Direct integer evaluation for \(25\le n\le45\) gives
\(\lfloor B(n)\rfloor\le74<10n\), so every candidate in that range lies
inside Theorem 1.8(i)'s exact census and is excluded by Table 1. The remaining
values are:

| \(n\) | \(F(1),F(5),F(7),F(11)\) | \(I\) | \(B(n)\) | \(\lfloor B\rfloor\) |
|---:|:---|---:|:---|---:|
| 46 | 37,41,43,35 | 35 | 560/11 | 50 |
| 47 | 37,41,43,35 | 35 | 48 | 48 |
| 48 | 37,41,43,47 | 37 | 1776/35 | 50 |
| 49 | 37,41,43,47 | 37 | 48 | 48 |
| 50 | 49,41,43,47 | 41 | 1968/35 | 56 |
| 51 | 49,41,43,47 | 41 | 1968/37 | 53 |
| 52 | 49,41,43,47 | 41 | 656/13 | 50 |
| 53 | 49,41,43,47 | 41 | 48 | 48 |
| 54 | 49,53,43,47 | 43 | 2064/41 | 50 |
| 55 | 49,53,43,47 | 43 | 48 | 48 |
| 56 | 49,53,55,47 | 47 | 2256/41 | 55 |
| 57 | 49,53,55,47 | 47 | 2256/43 | 52 |
| 58 | 49,53,55,47 | 47 | 752/15 | 50 |
| 59 | 49,53,55,47 | 47 | 48 | 48 |
| 60 | 49,53,55,59 | 49 | 2352/47 | 50 |
| 61 | 49,53,55,59 | 49 | 48 | 48 |
| 62 | 61,53,55,59 | 53 | 2544/47 | 54 |
| 63 | 61,53,55,59 | 53 | 2544/49 | 51 |
| 64 | 61,53,55,59 | 53 | 848/17 | 49 |
| 65 | 61,53,55,59 | 53 | 48 | 48 |
| 66 | 61,65,55,59 | 55 | 2640/53 | 49 |
| 67 | 61,65,55,59 | 55 | 48 | 48 |
| 68 | 61,65,67,59 | 59 | 2832/53 | 53 |
| 69 | 61,65,67,59 | 59 | 2832/55 | 51 |
| 70 | 61,65,67,59 | 59 | 944/19 | 49 |
| 71 | 61,65,67,59 | 59 | 48 | 48 |
| 72 | 61,65,67,71 | 61 | 2928/59 | 49 |

Intersecting \(n\le w\le\lfloor B(n)\rfloor\) leaves exactly the 20 pairs
\[
\begin{aligned}
 &(46,46\!:\!50),\quad (47,47\!:\!48),\quad (48,48\!:\!50),\\
 &(50,50\!:\!56),\quad (51,51\!:\!53),
\end{aligned}
\]
where \((a,b\!:\!c)\) abbreviates all \((a,w)\) with \(b\le w\le c\).
This independently reproduces the outer scouting residual list. It does not
certify any residual value of \(LR\).
