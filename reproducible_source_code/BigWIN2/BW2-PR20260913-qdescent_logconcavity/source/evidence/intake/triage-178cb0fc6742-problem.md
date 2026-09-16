# Precise interpreted problem and triage target

Immutable original: source.md. Job:
primary-20260913-qdescent-logconcavity-triage-178cb0fc6742.

## Objects, definitions, and quantifiers

Let q be an indeterminate. For every finite nonempty S subset of the positive
integers, put m=max S. Sym(n) denotes the permutations of {1,...,n}. Define
Des(pi)={h:1<=h<n and pi_h>pi_(h+1)} and
inv(pi)=#{(h,l):1<=h<l<=n and pi_h>pi_l}.
For every integer 1<=k<=m set

    a_k(S;q) = sum q^inv(pi),

over pi in Sym(m+k) with Des(pi)=S and
{m+1,...,m+k} subset of {pi_1,...,pi_m}. Set a_0=a_(m+1)=0
and extend by zero outside 1,...,m if needed. All a_k lie in Z_{>=0}[q].
Write f>=_q g when every coefficient of f-g is nonnegative.

Frozen literal original: for every such S, the polynomial sequence has no
internal zeros, and for every 1<=i<j<=m,

    a_i(S;q)a_j(S;q) >=_q a_(i-1)(S;q)a_(j+1)(S;q).

No internal zeros means a_r,a_t nonzero and r<s<t imply a_s nonzero.
The inequalities with i=1 or j=m have a zero right-hand side; m=1 has no
strict pairs. The empty set S is outside the frozen target.

The primary printed definition uses i<j while its surrounding discussion
treats i=j as included. The separate conventional strengthened target adds
every 1<=i=j<=m. A diagonal-only failure does not disprove the literal original.
Coefficientwise positivity is stronger than evaluation at positive real q;
q=1 alone is insufficient. Neither convention may silently replace the other.

## Nearest inspected prior results and source status

Gaetz–Gao, arXiv:1912.04933v2, Sections 1.1, 1.2 and 2: Theorem 5 gives the
above a_k and expansion D_S(n,q)=sum_k a_k(S;q)[n-m choose k]_q (n>m).
Theorem 6 proves the corresponding strong q-log-concavity statement for

    b_i(S;q)=sum_{pi in Sym(m+1),Des(pi)=S,pi_(m+1)=i} q^inv(pi).

Its Remark gives a_k=q^(k(k-1)) sum_i [m-i choose k-1]_q b_i.
Its counterexample for arbitrary b is already published and says nothing
directly against actual descent-derived a. Bencs, arXiv:1806.00689v2,
Corollary 4.4 (announced as Theorem 4.4), proves log-concavity at q=1.

Source status: status-uncertain as a current research problem. The inspected
source explicitly conjectures the target, and no inspected follow-up resolves
it, but bounded searches and incomplete later-source access do not establish
global openness or novelty. Details and URLs: literature/triage-screen.md.

## Proposed delta and verifier

Nearest prior result X: the b theorem and actual last-value suffix recurrence.
Proposed delta Y: prove the uniform quadratic kernel inequalities in
evidence/intake/triage-kernel-reduction.md. They imply the original and the
separately disclosed diagonal strengthening. The exact reduction is

    a_k = sum_{r=1}^m K(m;k,r) x_r,
    K(m;k,r)=q^(k^2)([m choose k]_q-[m-r choose k]_q),

where x_r enumerates inversions of size-m permutations with descent set
S without m and last value r. The reduction also shows all a_1,...,a_m
are nonzero. The kernel inequality is a stronger subsidiary statement,
not an assumed fact or accepted conjecture-note.

Verification route Z: a uniform coefficient-preserving injection or positive
q-Pascal decomposition, checked against exact polynomial arithmetic. Discovery
range m<=8 and frozen holdouts m=9..12 pass. Direct permutation enumeration
validates all 49 a_k cases with max S<=4, and 769 last-value entries of sizes
1..7. Finite checks are not a proof. Admission: advance for this precise lemma;
no mathematical acceptance, manuscript, priority claim, or release.
