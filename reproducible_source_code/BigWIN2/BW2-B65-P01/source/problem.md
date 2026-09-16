# Precise problem statement

## Frozen source and correction

The statement to be tested is exactly the claim in `source.md`; that file is not
modified. Its bibliographic attribution is incorrect: arXiv:2609.05358v1 is
Hikaru Manabe's *Purely Periodic Three-move Subtraction Games*, not a paper by
Grossman. This correction does not change the mathematical reading because the
arXiv identifier uniquely specifies the conventions used below.

## Definitions and quantifiers

Let \(\mathbb N_0=\{0,1,2,\ldots\}\). For each integer \(K\geq 1\), define
\[
 c_K=10K+1,\qquad S_K=\{4,6,c_K\}.
\]
The Sprague--Grundy sequence is the unique function
\(G_K:\mathbb N_0\to\mathbb N_0\) satisfying
\[
 G_K(n)=\operatorname{mex}\{G_K(n-s):s\in S_K,\ s\leq n\}
 \quad(n\in\mathbb N_0),
\]
where `mex` is the least nonnegative integer omitted by the displayed finite set.
Thus the game is normal play on one nonnegative heap, a legal move subtracts one
member of \(S_K\), and a position with no legal move has value \(0\).

Define the least eventual period by
\[
 p_K=\min\{p\geq1:\exists q\geq0\ \forall n\geq q,
                   G_K(n+p)=G_K(n)\},
\]
and, after fixing this least \(p_K\), define the least preperiod by
\[
 q_K=\min\{q\geq0:\forall n\geq q,
                   G_K(n+p_K)=G_K(n)\}.
\]
This is the "period first, then pre-period" convention on pp. 1--2 of the cited
preprint.

The universal claim is
\[
 \boxed{\ \forall K\in\mathbb Z_{\geq1},\quad
          (q_K,p_K)=(20K+7,5)=(2c_K+5,5).\ }
\]
Both equalities are part of the target: proving eventual 5-periodicity without
showing that 5 is the least eventual period, or without showing that
\(2c_K+5\) is the least starting index for that period, is insufficient.
A disproof consists of one integer \(K\geq1\) for which either equality fails,
with an exact recurrence-replayable certificate.

For every allowed \(K\), \(4<6<c_K\), \(c_K\neq4+6\), and
\(\gcd(4,6,c_K)=1\). Moreover \(a+b=10\),
\(\rho=c_K\bmod10=1\), and \(\delta=b-a=2\), so this is precisely the single
angle \(1\leq\rho\leq\delta-1\) in the first row's conjectural positive-preperiod
cell of Manabe's Table 1.

## Literature position and proposed delta

- Primary source inspected: H. Manabe, *Purely Periodic Three-move Subtraction
  Games*, arXiv:2609.05358v1 (4 September 2026), local PDF SHA-256
  `39457676064479f1ff52fded8697695c1ddd598f63665996b2eb889ec6fa66ca`,
  retrieved 7 September 2026. Theorem 32 and Table 1 (PDF pp. 21--23) prove the
  admissible pure-periodic zones. Conjecture 50 (PDF p. 33) conjectures only
  that the complementary angle here has positive preperiod; it gives neither
  the claimed exact preperiod nor the eventual period in this cell.
- Nearest cited result inspected: S. Zhang, *On the linearity of the periods of
  subtraction games*, Theoretical Computer Science 985 (2024), 114350,
  <https://doi.org/10.1016/j.tcs.2023.114350>, retrieved 7 September 2026.
  Its Theorem 6.3 covers \(\{a,a+2,(2a+2)t+1\}\) only for odd \(a\geq3\), so it
  does not cover the present even boundary \(a=4\).

Accordingly the source status is **new-question**: the exact assertion was not
located as a theorem or explicit open problem in the inspected primary sources.
This is not a priority or novelty claim. The proposed contribution is the exact
even-boundary formula above; the nearest prior result predicts positive
preperiod in the containing angle cell and proves the analogous ultimately
bipartite family for odd \(a\); the verification route is a uniform SG-word or
finite-state recurrence argument proving the eventual word and both minimality
claims.
