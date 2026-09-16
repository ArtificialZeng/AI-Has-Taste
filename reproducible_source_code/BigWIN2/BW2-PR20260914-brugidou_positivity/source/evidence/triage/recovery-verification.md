# Recovery triage verification

Job: primary-20260914-brugidou-positivity-triage-af8134cc889c.
Date: 2026-09-14 Asia/Shanghai (2026-09-13 UTC).
Decision: advance to one bounded research pass. This is a triage examination,
not mathematical referee acceptance or a novelty certificate.

The only literature handoff found and read was
`literature/operational-recovery-handoff.md`. Its recommendation was treated
as a lead. The source, precise problem, actual derivation, checker, and
relevant primary statements were inspected directly.

## Mathematical checks

For a>=3, p_(a-1)e_(b+1)=m_(a,1^b)+m_(a-1,1^(b+1)) has multiplicity
one in both terms: the distinguished variable either is or is not in the
elementary monomial. The condition a-1>=2 matters; applying this argument
at a=2 without changing multiplicities would be wrong. The separately
known base K_(2,b)=[b+1]_q covers this boundary.

For K_(a,b)=J_(a,1^b)/b!, the specialization is exactly
phi_q(m_(a,1^b))=(1-q)^(a-1)q^(b(b+1)/2)K_(a,b)/(a+b-1)!.
Substitution gives recurrence (H1), including its binomial multiplier and
q^(b+1) shift. Corollary 3.5 justifies cancellation in Q(q); evaluation at
q=1 is used only after forming a polynomial identity. Integral coefficient
prefixes prove integrality of K; divisibility by b! is not assumed from J.

Put D=binom(a-2,2), s=b+1, A=binom(a+b-1,a-2)J_(a-1),
B=K_(a-1,b+1). The threshold b>=max(0,D-1) implies s>=D and the
induction hypothesis for B. The identity (1-q)K=A-q^s B gives A(1)=B(1).
For k<s, the coefficient prefix contains the positive constant of A and
no subtraction. For k>=s, the complete A sum has been reached, leaving
the remaining tail sum of B. Finally
s+deg(B)-1=binom(a-1,2)+(a-1)b=deg(K), so this tail is nonempty for
every required k. This checks strictness, endpoints, b=0, and s=D.
No defect was found in this bounded reading. A fresh referee is still required.

The saved deterministic checker was reexecuted successfully with python3:
45 direct-specialization checks (size<=10), 66 prior-calibration comparisons
(size<=12), 31 explicit a=3 cases (0<=b<=30), and 28 cutoff/neighbor checks
(3<=a<=12). These are the original ranges, with no new finite coverage.
This was the same code, not an independent implementation. The current-job
receipt is `recovery-verification.json`; code/output remain `hook_check.py`
and `hook_check.json`.

## Scope and suitability

Nearest prior result X: positive rows, columns, (2,1^b), integer-polynomial
normalization, and the positive final n-1 coefficients. Proposed delta Y:
parameter-uniform positivity for hooks a>=3,
b>=max(0,binom(a-2,2)-1), potentially strengthened for short legs.
Verification Z: the identity and coefficient-prefix induction, then targeted
source comparison and fresh mathematical review. The symmetric-function
multiplication identity itself is not advertised as novel.

For example, (4,1^40) has n=44 and degree 123. It is beyond the source's
size<=43 computations and listed row/column/(2,1^b) families. Its final
43 coefficients occupy degrees 81..123; the hook argument covers 0..123.
This distinguishes scope from the explicitly inspected prior results, without
certifying literature novelty.

For s<D the unresolved part of this method is the difference of prefixes
for s<=k<D. The next research test is the symbolic a=5 short-leg overlap,
beginning b=1, seeking a coefficient bound extending to general a. Merely
checking that numerical polynomial would add nothing to prior finite coverage.
If no uniform mechanism emerges from this one test, retain the threshold
argument for targeted novelty/referee work instead of increasing finite ranges.
