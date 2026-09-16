# Precise interpretation of Chen's ULC failure conjecture

The original `source.md` is frozen verbatim. Its SHA256 is
`35bf7999e659653cddadf84048b691931a7e0d0d3064a2f0020c7603c780731b`.

For every integer m >= 4, work in Z[s] with

    f_m(s) = ((s+1)^m - (-1)^m)/(s+2),
    h_m(s) = ((s+1)^m + (-1)^m(s+1))/(s+2).

The quotients are polynomials, each monic of degree d=m-1. For either
p=f_m or p=h_m let a_j=[s^j]p for 0<=j<=d. These coefficients are
nonnegative. Ordinary ultra-log-concavity means log-concavity of
b_j=a_j/binom(d,j): b_j^2 >= b_{j-1}b_{j+1} at every integer 1<=j<=d-1.
Equivalently, define

    D_m,j(p)=j(m-1-j)a_j^2-(j+1)(m-j)a_{j-1}a_{j+1}.

The frozen original is the conjunction of:

1. For every integer m>=4 and each p in {f_m,h_m}, there exists an
   integer j in [1,m-2] for which D_m,j(p)<0.
2. For every integer m>=4, every integer j in [4,m-2], and each of the
   two polynomials p, D_m,j(p)<0.

The second range is empty for m=4,5; the first assertion still applies.
The degree and normalization do not change if the constant coefficient
is zero. Equality at a target index would refute assertion 2. This is
ULC of order m-1, not ULC(m) and not ordinary coefficient log-concavity.

## Nearest prior result and proposed contribution

Stephanie Chen, arXiv:2503.16296v2, Definition 2.4 and equations
(2.14)-(2.15), printed pp.8-9, specify this normalization. Equations
(3.1),(3.3), p.10, define the polynomials. Proposition 3.8 and its proof,
p.16, already establish assertion 1 and the low-index sign pattern;
Conjecture 3.9 on the same page asks for assertion 2 and repeats assertion
1. The author reports computation through m=100. Proposition 3.10,
pp.18-19, concerns the distinct ULC(m) normalization.

The identity h_m=f_m+(-1)^m gives identical D_m,j for j>=2, so the
proposed delta is one uniform strict-negative-minor theorem for f_m at
4<=j<=m-2, or one exact nonnegative minor in that range. It is not a
new non-ULC existence result or two separate theorems for f and h.

The even-h_m sentence of Proposition 3.8 contains a contradictory
degree-2 phrase; this does not affect the precise original above.
No correction to source.md is proposed.

Source status: the higher-index clause is conjectural in the inspected
arXiv v2. Live research-pass searches again located no later primary
resolution, but the journal body at DOI 10.1016/j.geomphys.2025.105666
remains uninspected. The publisher's indexed introduction confirms the
known non-ULC result, with changed numbering. Present global priority is
uncertain. The precise evidence and limits are in
literature/research-screen.md; a bounded search is not a priority certificate.

Verification route: exact integer coefficients from
2a_j+a_{j-1}=binom(m,j), plus a uniform sign identity or rigorously
bounded integral representation. A counterexample certificate consists
of m,j, the three exact coefficients, and D_m,j>=0. Finite scans alone
cannot establish the proposed theorem.

Research pass 1 reconstructed a complete proof route in
evidence/research-proof.md: set p=j-1,k=m-j-2 and reduce the sign to
H(p,k)=M_0 M_2-M_1^2 for
M_r=integral_(-1)^1 x^(k+r)(1+x)^p dx. The target is exactly H(p,k)>0
for all integers p>=3,k>=0; the inverse map is j=p+1,m=p+k+3.
Even k follows from a positive measure. Odd k has an explicit positive
base at p=3 and a recurrence with strictly positive coefficients and a
strictly positive auxiliary determinant. The endpoint D_m,m-2=-m treats
the existence clause for every m>=4, including m=4,5.

The complete argument has no known mathematical gap in the proposer's
reconstruction and is submitted as a full-scope proof candidate, pending
a fresh referee. Symbolic identities and exact finite regression are in
evidence/research-verify.py and evidence/research-verify.json. These do
not replace the infinite proof or constitute independent acceptance.
The decisive arXiv primary is retained unchanged in
evidence/external/chen-2503.16296v2.pdf and is bound with source.md and
this precise interpretation in claim.json. No original quantifier,
normalization, or endpoint convention has been altered.
