# Mathematical referee report

Verdict: **accept**.

Job: `primary-20260914-grid-narayana-referee-da7ad25dee1f`.
Snapshot: `61d25cfd4ce813d80b62073019af758dfaded6085829355302c8ad232f8e69ee`.
Review date: 2026-09-14 Asia/Shanghai (2026-09-13 UTC).
Frozen kind: `resolution-paper`. Frozen original status: `proved`.

The argument in `evidence/research-proof.md` proves the entire statement in
`source.md` and `claim.json`: for every integer n>=1, the support enumerator
of the specified maximum-deleted grid polytope is A_(n-1)(t) B_n(t).
There is no restriction on supports or n and no substitution of an Ehrhart
numerator for the support statistic. Scope, mathematical correctness, and
the contribution relative to the inspected sources pass this review.

This was a fresh referee context. Only the prescribed statement, interpretation,
claim, snapshot, listed evidence, and primary-source checks were used as research
inputs. Owner confidence was not used as evidence. No earlier audit, checkpoint,
state file, job transcript, or progress summary was read. No other agent or
background worker was launched. No frozen input was changed. This is a separate
model review pass, not a claim of statistical independence or external peer review.

## Reconstructed argument

### Original inequalities and the transfer

Every lower ideal consists of prefixes of the two rows with lengths (i,j),
where 0<=i<=n and 0<=j<=min(i,n-1). Necessity follows from downward closure
along each row and from (j,1)<=(j,2); these same conditions prove sufficiency.
Consequently the inequalities are exactly U_i+V_j>=0 with
U_i=i-sum_(k<=i)a_k and V_j=j-sum_(k<=j)b_k.

After m complete columns set M=min(V_0,...,V_m), z=U_m+M, s=V_m-M.
For a legal prefix, z,s>=0. Appending a=a_(m+1) introduces the constraints
U_(m+1)+V_j>=0 for old j, equivalent to 0<=a<=z+1. Appending b=b_(m+1)
adds only the new permissible pair of prefixes, giving
0<=b<=z+s+2-a. With delta=max(0,b-s-1), the next state is
(z+1-a-delta, max(0,s+1-b)). These formulas depend only on the recorded state;
the actual value of M is unnecessary for future feasibility.

The half-step alpha records a=0 with weight 1 and every positive a with
weight t. For beta, b=0 increases s; 1<=b<=s+1 lowers s without changing
the horizontal slack; and s+2<=b<=s+1+r gives each horizontal state
0,...,r-1 once, with vertical state zero. This gives exactly the two monomial
operators in the candidate, including the empty last sum when r=0.
After n-1 columns, only a_n remains, and its bound is 0<=a_n<=z+1.
Evaluation of the final state polynomial at x=y=1 therefore gives H_n.

Under x=1+u and y=1+v the operators become, at c=1+t,

    A=U_1+c+tD_1,
    B=U_2+c+tD_2+tD_1 E_2.

For example, the alpha summation is
(1+u)f+t((1+u)f-f(0,v))/u, which is Af. The beta calculation has the
additional term t(f(u,0)-f(0,0))/u, exactly tD_1 E_2 f.
Thus, with e=1, epsilon=[u^0 v^0], and T=BA,

    H_n = epsilon A T^(n-1)e |_(c=1+t).

### Finite trace and its boundary sign

The only noncommuting summands of B and A are tD_1 E_2 and U_1.
Since [D_1,U_1]=E_1,

    [B,A]=tE_1 E_2=t e epsilon,
    [A,T]=-t E A.

All these operators have bounded displacement on the two nonnegative indices.
A finite product with E=e epsilon has finitely many nonzero matrix entries:
both its input and output indices must lie within a bounded distance of the
origin. Traces and cyclic permutations of these terms are consequently finite
algebraic sums. Expanding [A,T^n] gives

    tr[A,T^n]=-nt h_n,   h_n=epsilon A T^(n-1)e.

This does not permit taking the trace of A T^n or T^n A separately.
I checked the boundary cancellation directly. For any fixed vertical index j,
writing K=T^n and summing horizontal diagonal entries through N gives

    sum_(i=0)^N [A,K]_((i,j),(i,j))
       = t K_((N+1,j),(N,j)) - K_((N,j),(N+1,j)).

The coefficient t multiplies the transition from N to N+1 in K, and the
transition from N+1 to N has a minus sign. No lower-boundary term remains,
because the unilateral operators kill the missing negative-index terms.

For N>=2n+2, every path contributing to the two displayed entries stays away
from horizontal index zero. Their symbols are therefore legitimately bilateral:
S(u)=u+c+t/u for A, B_u=J+(t/u)E_v for B, and S(u)^n B_u^n for K,
where J=U+c+tD on the vertical index. The displayed boundary equals
-CT_u (u-t/u)S(u)^n times the relevant vertical diagonal entry of B_u^n.

First sum over 0<=j<=L with L>=n+2. This contains the diagonal support of
[A,T^n]. Subtracting the corresponding diagonal of J^n changes nothing,
since CT_u (u-t/u)S(u)^n=0 by formal differentiation. Every word in
B_u^n-J^n contains E_v, and its diagonal vanishes at j>n. The subtraction
therefore leaves a genuinely finite vertical trace, independent of L. Hence

    nt h_n = CT_u (u-t/u)S(u)^n R_n(t/u),
    R_n(y)=tr((J+yE_v)^n-J^n).

This verifies both the finiteness and the sign of the candidate's decisive
boundary identity. No infinite-matrix cyclic-trace assertion is required.

### Rank-one perturbation, formal extraction, and telescoping

The series M(q)=epsilon_v (I-qJ)^(-1)1 enumerates excursions of nonnegative
Motzkin walks. The empty walk, an initial level step, and an initial up step
with its first matching return give M=1+cqM+tq^2 M^2.
Thus V=tqM is the unique zero-constant-term solution of
V=q(V^2+cV+t).

Differentiating sum_(n>=1) R_n(y)q^n/n with respect to y uses only finite
rank-one terms and gives q epsilon_v(I-q(J+yE_v))^(-1)1.
Expanding in rank-one insertions yields qM/(1-yqM). The series vanishes
at y=0, so coefficientwise integration proves

    sum_(n>=1) R_n(y)q^n/n = -log(1-yqM).

Substitution y=t/u in the boundary identity and formal constant-term
integration by parts give

    t h_n = [q^n] CT_u S(u)^(n+1) V/(u-V)/(n+1).

The sign is positive here: u d/du log(1-V/u)=V/(u-V).
All exchanged extractions are finite at each fixed q coefficient, because
V has zero constant term. Lagrange inversion applies over Q(c,t), where t
is invertible; the resulting polynomial identities extend to all c,t.
Writing C_(m,k)=[u^k]S(u)^m, it gives

    [q^n] V^k = (k/n) C_(n,-k) = (k/n)t^k C_(n,k)

for 1<=k<=n, with zero coefficients for k>n. This is precisely formula (9)
of the candidate. An equivalent check is R_n(y)=sum_(k=1)^n C_(n,k)y^k,
which follows from the same logarithm and inversion and was independently
tested by marked closed-walk enumeration.

Finally, differentiating S^(n+1) yields

    k C_(n+1,k)=(n+1)(C_(n,k-1)-t C_(n,k+1)).

The sum in formula (9) telescopes, leaving
(n+1)t C_(n,0)C_(n,1). Consequently h_n=C_(n,0)C_(n,1)/n.
At c=1+t, S(u)=(1+u)(1+t/u). Ordinary binomial expansion gives
C_(n,0)=B_n(t) and C_(n,1)/n=A_(n-1)(t), with exactly the frozen
normalizations.

### Quantifiers and exceptional cases

The full ideal bounds the total by 2n-1, so the original count is finite.
The empty ideal imposes nothing. For n=1 the poset has one coordinate,
Q_1=[0,1], and both sides are 1+t; the operator argument also gives h_1=c.
All denominators n and n+1 are nonzero because n>=1. Division by t occurs
only in an intermediate identity over a rational-function field. Both final
sides are polynomials, so cancellation proves the identity also at t=0
(where H_n=1). There is no analytic limit, positivity assumption, asymptotic
argument, or numerical interpolation in the uniform proof.

## Independent computational checks actually performed

The fresh executable `audit/referee-check.py` imports no candidate code and
does not execute the submitted verifiers. Its complete exact output is
`audit/referee-check.json`. It passed with Python integer arithmetic.

- All 12 frozen file hashes and the canonical snapshot digest were checked
  before and after the computation. In particular, source.md retains SHA-256
  `3475114886a7af30aad77d1c99dcf080b0b048690f814c3d5ac22f6b4e87b801`.
- For n=1,...,6, every subset was tested for downward closure using the
  coordinatewise relation itself. The resulting ideals, including empty,
  agreed with the prefix characterization. A stars-and-bars enumeration
  then tested every ambient vector of total at most 2n-1 against all those
  ideals. The respective ambient counts were 2, 20, 252, 3432, 48620,
  and 705432, totaling 757758. Every full support polynomial matched the
  frozen factorization.
- The commutator was tested on the 64 monomials with both exponents in
  0,...,7, at each of seven exact pairs (c,t): (0,0), (2,3), (0,1),
  (-3,2), (4,-3), (1,0), and (-2,-2), totaling 448 cases.
- For n=1,...,16 at those seven pairs, direct operator-word enumeration
  matched both the product formula and the extraction numerator, totaling
  112 cases. Laurent coefficients were evaluated independently by a
  multinomial factorial formula.
- For n=1,...,8 at the same pairs, marked closed walks computed R_n(y)
  without taking either divergent trace separately. Its coefficients
  matched C_(n,k). The resulting constant term and the far-horizontal
  boundary flux matched nt h_n with the prescribed sign, totaling 56 cases.

The submitted research verifier and its output were inspected as supporting
evidence. The older triage script references intake files outside the frozen
input list; it was therefore not rerun, and those inputs were not opened.
The independent direct enumeration above covers its stated n<=6 counting
range without those dependencies. These finite computations calibrate the
argument; acceptance rests on the uniform proof reconstructed above.

## Source comparison and contribution

The primary [Athanasiadis--Chapoton paper](https://arxiv.org/html/2605.26916v1#S9.SS3)
was checked through the frozen HTML and the live arXiv page. Its Section 3
uses the same ideal inequalities, Section 5 defines the same support statistic,
and Section 9 defines the same type A and B Narayana factors. The final paragraph
of Section 9.3 proposes exactly this maximum-deleted-grid factorization. Its
displayed examples are n=1,...,4. The accepted delta is a proof for every n>=1.

The nearest inspected established comparison is
[Athanasiadis, Lattice point enumeration of polytopes associated to integer compositions](https://arxiv.org/html/2510.23903):
Examples 2.3 and 2.4 separately evaluate the total-bounded and chain-prefix
families, giving B_r and A_r respectively. Theorem 3.1 and Remark 3.2 concern
composition polytopes and their Eulerian descriptions. These results do not
themselves evaluate the coupled grid inequalities. The rank-one transfer and
boundary calculation supply the missing uniform evaluation. The contribution
has a clear use: an exact support distribution for the stated polytope family.

Independent live searches included the paper identifier with `proof`, `grid`,
and `commutator`; its title with `Narayana proof`; `Narayana rank-one commutator`;
and truncated/grid/Narayana factorization queries restricted to arXiv.
No equivalent resolution was found among the results inspected. Search results
and secondary summaries were used only as leads, not as mathematical sources.
This is bounded literature screening, not proof of global priority. The served
arXiv metadata identifies v1; no extra revision is inferred from the HTML's
internal date. The proof itself uses no unproved auxiliary statement from
either comparison paper.

## Gaps, limits, and disposition

No substantive mathematical gap remains in the frozen scope. No claim revision
or change to decisive evidence is requested. The acceptance concerns the exact
support identity and the proof supplied for it; it does not certify broader
preorder conjectures, global priority, or future journal acceptance.

The next workflow step is the runner's structural `check-math` gate, followed
by manuscript preparation at this unchanged scope. Preserve the explicit finite
boundary-trace justification and the removable t=0 specialization in that draft.
No manuscript or publication artifact was created in this referee job.
