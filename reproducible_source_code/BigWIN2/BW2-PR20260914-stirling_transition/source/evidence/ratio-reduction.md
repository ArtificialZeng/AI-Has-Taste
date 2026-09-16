# A sufficient ratio inequality, not an established theorem

Job: `primary-20260914-stirling-transition-triage-fc44a4f8547e`.
Date: 2026-09-14. This is a triage reduction and finite evidence dossier.

For k>=1 and n>=k set q_k(n)=c(n,k-1)/c(n,k). The denominator
is strictly positive. The proposed stronger lemma is

    q_k(n) - 2 q_k(n+1) + q_k(n+2) >= 0   (k>=1, n>=k).       (L)

Its universal truth and novelty have not been established. For k=1 it is an
identity. The integer screen tested 138525 instances, exactly
1<=k<=150 and k<=n<=998, with no negative numerator. This is finite evidence.

## Why (L) would settle the original assertion

The recurrence gives c(n+1,k)/c(n,k)=n+q_k(n) for n>=k.
Consequently, for n>=k+1,

    D_k(n) / (c(n-1,k)c(n,k)) = q_k(n-1)-q_k(n)-1.            (1)

Let d_n=q_k(n)-q_k(n+1) for n>=k. Under (L), d_n is
nonincreasing. There must be an index j>=k with d_j<1: otherwise
q_k(k+t)=q_k(k)-sum_{i=k}^{k+t-1}d_i <= q_k(k)-t would become
negative, contradicting q_k>=0. Once d_j<1 it stays below 1.
Equation (1) therefore makes the signs of D_k(n), n>=k+1, pass
from nonnegative to nonpositive at most once and guarantees a negative tail.
Together with D_k(k)=1 and the leading zeros this proves the frozen assertion
**conditional on (L)**. No asymptotic differentiation or unproved tail estimate
is needed for this implication.

The original conjecture does not imply (L); falsifying (L) would only defeat
this stronger proof route. In contrast, an exact pair n<m with
D_k(n)<0<D_k(m) would disprove the original.

## A concrete algebraic test

Fix n>=k>=1 and write

    A=c(n,k), B=c(n,k-1), C=c(n,k-2), E=c(n,k-3),
    Q1=n*A+B,
    Q2=n*(n+1)*A+(2*n+1)*B+C.

The convention for negative k makes C or E zero at the boundary; A,Q1,Q2>0.
Two recurrence steps give

    q_k(n)=B/A,
    q_k(n+1)=(n*B+C)/Q1,
    q_k(n+2)=(n*(n+1)*B+(2*n+1)*C+E)/Q2.

After multiplying (L) by A*Q1*Q2, its numerator is

    (n*A+B)*(B*B-A*C)
      + n*(2*B**3-3*A*B*C+A*A*E)
      + B*B*C-2*A*C*C+A*B*E.                                (2)

This expansion was checked by exact symbolic algebra, and can be checked
directly from the three displayed fractions. Usual row log-concavity controls
B*B-A*C, but the other cubic expressions require justification; their signs
are not assumed. A bounded research pass should test whether Newton/Toeplitz
inequalities for the real-rooted polynomial product_{j=0}^{n-1}(x+j) control
(2), or find an exact counterexample to (L). The requested result is the
whole numerator's sign, not an unsupported assertion that each summand is
nonnegative.

## Reproduction and limitations

Run `python3 evidence/triage_exact.py` from the project directory.
`evidence/triage_exact.json` stores every sign word, coverage, first-negative
indices, and script/source hashes. All 150000 D tests use integer arithmetic;
all 46234 permutations of sizes 0 through 8 were independently enumerated to
check the recurrence's small rows. The first-negative indices for k=1,...,10
are 2,3,5,6,8,10,11,13,15,17; for k=150 it is 257. No zero D on
the positive support was observed in the tested rectangle. These indices
are finite observations, not certified infinite thresholds.

This reduction has not passed a fresh referee; no candidate, manuscript,
novelty claim, or resolution is being asserted in triage.
