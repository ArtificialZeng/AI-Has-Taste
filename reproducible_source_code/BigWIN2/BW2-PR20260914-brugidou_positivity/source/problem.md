# Precise problem and partial-result scope

The verbatim source is frozen in `source.md` (SHA256
41514463fec1850514a2d7e769680ea0403b78bc8ec786ce51eef70271847b1d).
No correction or weakening of its statement is proposed.

Let Lambda_Q=Q[e_1,e_2,...] be the ring of symmetric functions, with e_0=1.
For the indeterminate q, let phi_q:Lambda_Q -> Q[q] be the unique unital
Q-algebra homomorphism with phi_q(e_j)=q^(j(j-1)/2)/j! for every integer j>=1.
A nonempty partition of n is a tuple lambda=(lambda_1>=...>=lambda_r>=1)
with sum n; n>=1, r>=1. Put nu(lambda)=sum_(i=1)^r (i-1)lambda_i and
 a_j(lambda)=#{i:lambda_i=j}. The monomial symmetric function m_lambda is the
sum of the distinct monomials having nonzero exponent multiset lambda.

Define J_lambda by the polynomial identity

phi_q(m_lambda) = (1-q)^(n-r) q^nu(lambda) J_lambda(q)
                  / ((n-1)! product_(j>=1) a_j(lambda)!).

Brugidou, Corollary 3.5, establishes that J_lambda belongs to Z[q], has
nonzero constant term, and has degree
 d(lambda)=binom(n-1,2)+r-1-nu(lambda).
The frozen target is

For every n>=1, every lambda partitioning n, and every integer
0<=k<=d(lambda), [q^k]J_lambda(q)>0.

Only coefficients from constant through leading degree are quantified; those
outside the support are not required to be positive. The empty partition is
excluded. One-row, one-column, and constant polynomials are included; J_(1)=1
and J_(1^n)=(n-1)!. Evaluation at q=0 or q=1 is not division in the defining
identity. There are no upper bounds on n, r, or the largest part. Positivity
of values at real q, nonnegativity alone, log-concavity (Conjecture 4.2), and
positivity of a sum over partitions are distinct assertions.

Primary source: [Brugidou v7](https://arxiv.org/html/2306.15300v7), equations
(3.16)-(3.17) and Conjecture 4.1. Live record checked 2026-09-14 Asia/Shanghai:
v7 remains the latest listed version. Source status is **open-supported** by
this primary conjecture and the bounded searches in `literature/triage-screen.md`
and `literature/recovery-triage-screen.md`, with the research-stage comparison
in `literature/research-pass1-screen.md`;
this is not exhaustive certification of current openness or priority.

Nearest prior results: integer polynomial/degree/valuation; the positive
one-row tree polynomials; formulas (3.21)-(3.22) for columns and (2,1^b);
positive aggregate J_n^(r) in Proposition 4.4; and the final n-1 coefficients
in Corollary 5.2. The source reports all-partition checks through n=43.

Research pass 1 proposes a **result-note candidate**, original status
**unresolved**. For a>=2,b>=0 write K_(a,b)=J_(a,1^b)/b! and put

 d_(a,b)=binom(a-1,2)+(a-1)b,
 D_a=binom(a-2,2), F(a)=max(0,ceil((D_a-4)/2)).

The exact subsidiary theorem submitted for review asserts that K_(a,b)
belongs to Z[q]; that [q^k]K_(a,b)>0 for
0<=k<=min(d_(a,b),2b+3); and that all coefficients through d_(a,b)
are positive whenever b>=F(a). Together with the established rows b=0,
this includes every hook with 2<=a<=6. F is a sufficient bound, not an
asserted optimal bound. The full all-partition target above is unchanged;
non-hooks and general hooks outside the specified region remain untouched.
No coefficient log-concavity theorem is submitted.

The complete argument is `evidence/research/hook-prefix-proof.md`.
The source's established positive row recurrence yields
R_m=J_m-(m-1)J_(m-1) in N[q] and [q]R_m=(m-1)!/2 for m>=3.
Two coefficient prefixes in the hook recurrence, including the next
constant correction, prove the initial range. Tail induction then yields
F(a). This improves the unreviewed triage bound max(0,D_a-1), preserved
in `evidence/triage/hook-route.md`. The assigned a=5,b=1 overlap is
positive with coefficient 130; the uniform proof, not that finite check,
is the proposed contribution.

Primary inputs decisive to this scope have been preserved as full text:
`evidence/external/2306.15300v7.html` and its complete copied extraction
`evidence/external/2306.15300v7.txt`. Corollary 3.5 supplies polynomiality
and degree, the introduction and Corollary 3.4 supply the positive aggregate
recurrence and constants, and equation (3.22) supplies the base case.
These established facts and the elementary symmetric-function identity
are not advertised as new. The primary-source comparison found no matching
hook theorem in the inspected content; this is not a priority certificate.

The new exact checker imports no previous checker or calibration output.
It compares 66 direct defining specializations through size 12, enumerates
labeled trees through seven vertices, and verifies 177 hook cases and
2,377 prefix identities. Ranges and limitations are recorded in
`evidence/research/hook_prefix_check.json`. These computations validate the
formulas; the infinite assertion rests on the mathematical proof.

Proposer: primary-20260914-brugidou-positivity-research-cd617853de0e.
A fresh referee must check the exact scope, proof, and source overlap.
No mathematical acceptance, manuscript, or generated PDF is asserted.
One next test: independently audit the endpoint at k=2b+3 and the tail
induction at D_a=2b+4, against the preserved primary recurrence.
