# Precise problem: Class 214

Frozen input: `source.md` (unchanged).
Research job: primary-20260913-inversion214-research-aabee08e3bf3.

For every integer n >= 0, let I_n be the set of tuples e in Z^n with
0 <= e_i < i for all i in {1,...,n}, such that for every
1 <= i < j < k <= n, at least one of e_j < e_k or e_i < e_k holds.
I_0 contains exactly the empty tuple. Write a_n = |I_n| and
F(z) = sum_{n>=0} a_n z^n in Z[[z]] subset Q[[z]].

An occurrence of a length-three pattern means an indexed subsequence with
exactly the same strict-order and equality relations as that pattern; entries
need not be adjacent. The forbidden patterns are 000, 010, 100, 110, 120, 210.
For a fixed final entry e_k, the condition is equivalently that at most one
previous entry is >= e_k. Thus a_0=a_1=1, a_2=2, and a_3=4.

The requested tasks are (i) determine F by a rigorous solved representation
beyond the already published recurrence or unsolved functional equation;
and (ii) decide the conjecture

    for all P in Q[z,w] minus {0}, P(z,F(z)) != 0 in Q[[z]].

There is no finite degree, coefficient range, or asymptotic cutoff in this
claim. Algebraic means algebraic over Q(z); its negation is transcendence
in the stated formal-power-series sense. Non-D-finiteness is a stronger
possible target and is not the frozen claim. A finite failed guess
or a polynomial recurrence alone does not settle algebraicity.

## Nearest prior result and normalization

Nathan Britt and Nicholas Beaton, *Completing the enumeration of inversion
sequences avoiding triples of relations*, arXiv:2512.21943v2, 3 August 2026,
Section 3.5, printed p.18, supplies the succession rule (3.31) and the
auxiliary equations (3.32)-(3.33). The live version and the retained PDF
agree on these statements. The authors leave the generating function
unsolved and express belief in non-algebraicity. Section 4.2, equation
(4.8), labels its asymptotics as numerical, not rigorous.
Primary links: https://arxiv.org/html/2512.21943v2#S3.SS5 and
https://arxiv.org/abs/2512.21943 (inspected 2026-09-13 Asia/Shanghai).

The enlarged class B allows forbidden 000,010,100 only when their entries
represented by 0 are literally zero. Let p,s be the lengths of the first
and second zero runs, with s=0 if the second is absent and (0,0) for the
empty tuple. Its series B(z,x,y) marks length by z and p,s by x,y.
For V(z,x)=B(z,x,0), the target is

    F(z) = [x^0]V(z,x) + [x^1]V(z,x) + [x^2]V(z,x).

The existing rule counts all auxiliary states and retains only states
(p,0), p<=2, for a_n.

Source status: open-supported by this primary version; bounded later-source
search does not establish exhaustive current open status or novelty.

Additional prior comparison: Toufik Mansour, *Inversion sequences avoiding
a set of length-3 patterns*, Integers 24 (2024), A76, Table 2 class 44
(printed p.45) and Theorem 13 (p.57), includes the exact six-pattern set
in an established Wilf-equivalence class. The inspected portions provide
equivalences and generating trees, without a solved OGF there. Primary
PDF: https://math.colgate.edu/~integers/y76/y76.pdf. This theorem is not
used as a dependency in the proposed quotient proof. See
literature/research-live-screen.md for access and coverage limits.

## Candidate scope after research pass 1

The original tasks and quantifiers above remain unchanged. The proposed
result-note addresses only the solved-representation task. Its precise
theorem in evidence/quotient-proof.md expresses F=(b-A)/(zL), with X the
small root of z(1+X)^2=X, q=X^2/(1+2X), and A,L explicit convergent formal
sums along the nonrecursive orbit
t_j=z^j q/(1-q sum_{r=1}^j z^r). Neither sum contains an unknown boundary
or counting series. Truncating both sums to m terms gives explicit
F_m in Q(z,X) with F_m-F=z^(m+3)+O(z^(m+4)) for every integer m>=0.
The boundary equation also has a unique solution in Q[x][[z]].

This goes beyond the published rule or an unsolved functional equation
by eliminating the remaining boundary coefficient and proving the
infinite tail vanishes. Evidence/quotient-check.py and .json compare
three distinct exact implementations through degree 40, including the
triage-held-out degrees 17-20. These tests corroborate, and do not replace,
the formal proof. A fresh mathematical referee has not yet reviewed it.

No proof or disproof of non-algebraicity is supplied. The original
problem therefore remains unresolved. No asymptotic or analytic
continuation conclusion is inferred from the quotient or coefficient data.
