# Frozen problem and precise reading

Job: `newwin-00001-p19-triage-624bca8c0b20`; triage, 2026-09-12.

The original Chinese statement remains verbatim in `source.md`, SHA256
`06bb18541ed5c313de4681fcc61eebb42d73353add1b3dc546c441aa8a9015b6`.
No correction or weakening is proposed.

For every integer n >= 1 define

    S_0(n) = {k in Z : 1 <= k <= floor(n/2)},
    S_(j+1)(n) = {n mod k : k in S_j(n), k > 0}  (j >= 0),
    s_j(n) = |S_j(n)|.

Here n mod k = n - k floor(n/k) belongs to {0,...,k-1}; the braces denote
sets, so repeated values count once. Zero is retained as a value and excluded
as a modulus at the next step. For n=1 all these sets are empty.

The target is: the real sequence a_n = s_2(n)/n has no limit as n tends to
infinity through all positive integers. Equivalently, there is no real L such
that for every epsilon>0 there is N with |a_n-L|<epsilon for every n>=N.
Since 0<=a_n<=1/2, divergence to an infinite extended-real limit is excluded.
A sufficient certificate is two increasing positive-integer sequences n_t,m_t
tending to infinity and real alpha<beta with

    limsup_t a_(n_t) <= alpha < beta <= liminf_t a_(m_t).

Only the fixed iterate j=2 is in scope. Higher iterates and exact global
liminf/limsup are separate questions.

## Prior result and source status

Baraskar and Vukusic, *Bounds for Sets of Remainders*, Journal of Integer
Sequences 29 (2026), Article 26.1.4, published January 26, 2026:
[publisher PDF](https://cs.uwaterloo.ca/journals/JIS/VOL29/Vukusic/vukusic2.pdf),
[publisher record](https://cs.uwaterloo.ca/journals/JIS/VOL29/Vukusic/vukusic2.html),
[arXiv record](https://arxiv.org/abs/2508.20853). Retrieved live 2026-09-12;
the supplied local PDF and text were also inspected.

Theorem 1 (p.3) proves s_1(n)/n -> c, with an explicit prime sum for c.
Theorem 3 (p.4) gives, for fixed j>=0,
1/(j+2)! <= liminf s_j(n)/n <= limsup s_j(n)/n <= 1/(j+2).
Thus at j=2 the known general bounds are 1/24 and 1/4. Section 7,
Problem 2 (p.16), asks nonconvergence for every j>=2; the present claim is
exactly its j=2 case. Source status: `open-supported`, subject to the bounded
current-literature search recorded in the triage evidence; no priority claim.

## Research candidate and relation to the original

Research job `newwin-00001-p19-research-c7978facb398`, 2026-09-12.
Nearest prior result: the above general bounds and the explicit open problem.
The proposed delta is a strict pair of subsequence bounds for exactly j=2.
It settles the full frozen original if the proposed proof passes fresh review.
It does not settle the source article's larger all-j>=2 problem.

Let M=691374732709966591241323368000 and L=75600. The proposed
complete proof in `evidence/research-proof.md` establishes, for every t>=1,

    s_2(M*t)/(M*t) <= alpha+(M+3)/(M*t),
    s_2(L*t+1)/(L*t+1) >= beta-(L+2)/(L*t+1),

where

    alpha=30093341768093808664597/276977102566985955634500,
    beta=1182869/9979200,
    beta-alpha=131410063319607383019139/13294900923215325870456000>0.

The bounds separate uniformly for every t>=203, with all floor, counting,
and zero corrections included. Taking subsequence limits proves the requested
nonconvergence. The exact constants and finite threshold are recomputed by
`evidence/research_verify.py`, with output in
`evidence/research-verification.json`. Finite tests supplement the written
universal argument; this is a candidate for review, not an accepted result.

The unreviewed handoff `literature/p19-intake-handoff.md` supplied the initial
route; its assertions were checked rather than assumed. The primary PDF/text
decisive for the interpretation and source-status comparison are copied in
`evidence/external/baraskar-vukusic-2026.pdf` and
`evidence/external/baraskar-vukusic-2026.txt`. The research literature screen
and its limits are in `literature/research-literature.md`. No change has been
made to the original statement or its interpretation above.
