# Exact recurrence and method diagnostics

Job: `primary-20260913-binary-subsum-shape-triage-b98ea643b894`.
Reproduce from the project root with `python3 evidence/triage_recurrence.py`.
Output: `evidence/triage_recurrence.json`.

## Definitions

For even n>=2, let A_n=(1+x)^n N_(n/2)(x^2) and
B_n=product_(i=1)^v2(n)(1+x^(2^i)) N_(n-2)(x).
Both have degree d(n), and N_n=A_n+B_n by the prior recurrence.
Write a_j=[x^j]A_n and b_j=[x^j]B_n. Define

    T_j(P) = p_j^2 - p_(j-1)*p_(j+1),
    C_(n,j) = 2*a_j*b_j - a_(j-1)*b_(j+1) - b_(j-1)*a_(j+1).

Direct expansion gives the exact algebraic identity

    T_j(N_n) = T_j(A_n) + T_j(B_n) + C_(n,j).

This identity alone is not a positivity theorem.

## Coverage and results

All arithmetic uses arbitrary-precision integers. No randomness or floating point.
The recurrence was constructed afresh; direct binary partition enumeration with
binomial-factor multiplication agrees for every n=0,...,16. Recurrence diagnostics
check every internal integer coefficient for every even n=2,...,128 (64 polynomials).
Adjacent odd polynomials are supplied by the known equality N_(2m+1)=N_(2m).
This is a new implementation in the same worker context, not a fresh-model audit.

- The sole failing even total polynomial in this range is N4. Its coefficients
  are [4,10,18,18,20,18,18,10,4], with T_3=-36. N5=N4 lies outside the target too.
- All tested A_n are log-concave.
- B_n fails log-concavity at even n=2,4,6,8,16.
- C_(n,j) has a negative entry at even n=2,4,6,8.
- The stronger separate inequalities a_j*b_j>=a_(j-1)*b_(j+1) and
  a_j*b_j>=b_(j-1)*a_(j+1) fail repeatedly, including all tested multiples of 4.
- The weaker **compensation invariant**

      T_j(A_n)>=0,  T_j(B_n)+C_(n,j)>=0

  holds for every even 10<=n<=128 and every 1<=j<d(n).
  Equivalently, T_j(N_n)>=T_j(A_n)>=0 in this finite range.
  There is no claimed universal proof of either inequality.

## Exact failure certificates for the stronger method

At n=6,j=1, the triples for A and B are (2,12,32) and (4,10,22).
One synchronization inequality fails: 12*10-4*32=-8.

At n=6,j=3, the triples are (32,52,62) and (22,28,38).
The second summand is not log-concave: 28^2-22*38=-52.

At n=6,j=5, the triples are (62,64,62) and (38,36,38).
Here T(A)=252, T(B)=-148, C=-104, and T(N6)=0.
Thus separate positivity of the summands or of C fails even though N6 is
log-concave. This rules out those stated all-n>=6 sufficient conditions;
it does not obstruct every recurrence proof or refute the original conjecture.
It also shows why strict log-concavity cannot silently replace the target.

## Research lead, not a result

The proposed delta beyond BBFM Theorem 4.7 is an all-n proof of the compensation
invariant for even n>=10. Together with the explicit N6,N8 checks and the known
odd-index equality, that would imply the entire frozen conjecture. N6 and N8
are base cases forced by observed failures of the stronger invariant, not a
change in the original range.

One next test: attack that precisely stated compensation invariant at the next
dyadic scales, computing all coefficients for even 130<=n<=512. On the first
negative value retain both triples and T(N_n), which distinguishes a method
failure from a counterexample to the original claim. If it survives, use the
same invariant for a symbolic induction attempt across v2(n) classes before any
further range extension. Finite success is not a proposed publication result.
