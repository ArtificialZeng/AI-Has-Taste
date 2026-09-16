# Fresh mathematical audit

- Referee job: `win-00085-p11-referee-a991a849a655`
- Frozen snapshot: `3f585e2e84218726bd0caecaf55bef5c679d457727b8f8667ce25aaef3397afa`
- Candidate: `resolution-paper`, with frozen original status `proved`
- Verdict: **accept**

## Scope and integrity

The candidate claims the full frozen exact value, not an extremizer
classification.  This is exactly the success scope in `source.md` and
`problem.md`.  I recomputed every file hash in `audit/snapshot.json`; all six
frozen-input hashes agree, and I independently recomputed the snapshot digest.
In particular, `source.md` still has SHA-256
`c3d26bd50db550877a991b263ebec998946948438739646d7f9a07f5a3647350`.

Write

\[
 P(U)=256U^7+256U^6-96U^5-80U^4+40U^3+30U^2-15U-5
\]

and let $u\in[533/1000,267/500]$ be as in the claim.  As a check independent
of the submitted derivative estimate, I used an exact rational Sturm count.
It gives exactly one root of $P$ in this interval.  Thus the algebraic branch
in the statement is unambiguous.  The relevant denominators below do not
vanish: $u>1/2$, $32u^4+8u^2+1>0$, and the primal normalizer is positive.

## Reconstructed primal certificate

Set

\[
 q(X)=X^3+uX^2+(2u^2-5/4)X-2u^3,
 \qquad
 A_0={128u^6-20u^2+5\over32}.
\]

I reconstructed the Chebyshev expansion from the monomial coefficients by an
exact basis change, rather than importing the submitted checker.  It is

\[
q(X)^2=A_0T_0
-{u(64u^4-40u^2+5)\over8}T_1
+{5u^2-1\over8}T_4+{u\over8}T_5+{1\over32}T_6.
\]

In particular, the $T_2$ and $T_3$ coefficients vanish identically.  Also
$A_0>0$; alternatively, $A_0$ is the positive constant Chebyshev
coefficient of the nonzero square $q^2$.  Therefore
$p(X)=q(X)^2/A_0$ has normalized constant coefficient one, only the allowed
frequencies $1,4,5,6$, and is nonnegative for every $X\in[-1,1]$.  This is
a global square certificate, not sampled-grid evidence.  Exact simplification
gives

\[
 {p(1)\over2}=
 { (2u+1)^2(4u^2-6u+1)^2\over128u^6-20u^2+5}.
\]

Hence the claimed number is a rigorous lower bound for the frozen Turán
constant through the stated finite reduction.

## Reconstructed dual certificate

I reconstructed the moment functional $L$ from the displayed $m_0,m_1,m_2$
in `evidence/exact_solution.md` and the recurrence

\[
 m_{n+3}=-u m_{n+2}-(2u^2-5/4)m_{n+1}+2u^3m_n
 \quad(0\le n\le3).
\]

Direct symbolic reduction in $\mathbb Q[U]/(P)$ gives

\[
 L(T_1)=L(T_4)=L(T_5)=L(T_6)=-1,
 \qquad L(qX^n)=0\quad(0\le n\le3).
\]

I separately checked the support and positivity rather than inferring them
from these identities.  Exact Sturm sign-constancy checks in the isolating
interval for $u$ give the signs of $q$ at

\[
 -23/25,-91/100,-21/50,-41/100,79/100,4/5
\]

as $-,+,+,-,-,+$, respectively.  Thus $q$ has three distinct real roots,
one in each of

\[
(-23/25,-91/100),\quad(-21/50,-41/100),\quad(79/100,4/5),
\]

all strictly inside $(-1,1)$.  I formed the moment matrix
$H=(m_{i+j})_{0\le i,j\le2}$ directly.  Exact Sturm sign checks on its three
leading principal minors give $+,+,+$, so $H$ is positive definite.

For clarity, these facts really do produce a positive atomic functional.
The recurrence gives $L(qs)=0$ for every polynomial $s$ of degree at most
three.  Reducing modulo the cubic and interpolating at its three distinct roots
$r_i$ therefore yields

\[
 L(f)=\sum_{i=1}^3w_i f(r_i)\qquad(\deg f\le6).
\]

If $h_i$ is the degree-two Lagrange polynomial for $r_i$, then
$h_i^2-h_i$ is divisible by $q$.  Hence
$w_i=L(h_i)=L(h_i^2)>0$ by positive definiteness of $H$.  This closes the
possible gap between a formal truncated moment vector and an actual positive
measure on the feasible interval.

Now let

\[
 f=1+2\sum_{k\in\{1,4,5,6\}}c_kT_k
\]

be any feasible polynomial.  Positivity of the atomic functional gives

\[
 0\le L(f)=m_0-2\sum_kc_k,
 \qquad f(1)\le1+m_0.
\]

For the primal square, the recurrence gives $L(q^2)=0$, hence $L(p)=0$.
Therefore it attains the dual bound: $p(1)=1+m_0$.  The finite optimum is
exactly $M=p(1)$, and the frozen identity
$T_{\mathbb R}(\Omega_{5/2})=M/2$ proves precisely the formula in
`claim.json`.

## Source comparison, attacks, and limits

The frozen source comparison reports only

\[
 {559+80\sqrt{42}\over506}\le T_{\mathbb R}(\Omega_{5/2})\le{9\over4}.
\]

The new exact value is approximately $2.1353071788763974$, consistently
between the reported endpoints (the lower endpoint is approximately
$2.1293661183253534$).  The page-level source account in
`evidence/triage.md` identifies the reduction theorem and verifies that
substitution of $(p,q)=(5,2)$ gives the frozen frequency set.  The immutable
problem itself includes that reduction as part of the setup, so this audit
tests the new finite optimization certificate rather than reproving the cited
general theorem.  No primary-source PDF was among the snapshot-listed files,
and, following the assigned evidence boundary, I used no unlisted source.

I specifically checked uniqueness of the algebraic parameter, zero
denominators, the forbidden-frequency coefficients, nonnegativity for the
entire continuum, interior and distinct dual support, strict positivity of all
three weights, the signs in the dual inequality, the factor $1/2$ in the
continuous reduction, and primal-dual complementarity.  No empty-domain,
endpoint, limiting, or equality-case gap remains.  Extremizer classification
is outside the frozen success condition.

The literature screen is explicitly bounded and labels priority/open status
uncertain.  The candidate makes no priority or formal-open-problem claim, so
that limitation does not overstate the mathematical contribution.  The exact
primal-dual certificate is a nontrivial full resolution of the frozen value
problem.

The independent executable checks are recorded in
`audit/referee_recheck.py`; they complete successfully using exact arithmetic
and Sturm tests.  The submitted verifier also completed with all exact
assertions passing.  I find no unresolved mathematical gap in the frozen
candidate and therefore accept it at its exact submitted scope.
