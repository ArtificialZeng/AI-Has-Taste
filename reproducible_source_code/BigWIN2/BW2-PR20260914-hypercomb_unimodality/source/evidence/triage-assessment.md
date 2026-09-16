# Bounded mathematical assessment

Reproduce with `python3 evidence/triage_checks.py` from the project directory.
Output: `evidence/triage-checks.json`. Arithmetic is exact integer arithmetic.

Seven direct subset enumerations use (n,ell)=(1,3),(2,3),(3,3),(4,3),
(1,4),(2,4),(1,5), covering 633,984 subsets in total. Every coefficient
agrees with the recurrence, including the distinct n=1 attachments.

The complete finite grid is recorded per ell in the JSON: n=1,...,120
for ell=3,...,40, extending to n=520 at ell=3,4,12,13; n=1,...,160
at ell=50,100; and n=1,...,80 at ell=1000. This totals 6,560 polynomials.
Every one is unimodal and log-concave. These are finite observations,
mostly validation within the authors' range, with limited extra coverage.
They do not prove any infinite assertion or constitute a publishable result.

Let a=(1+(ell-1)x)(1+(ell-2)x), b=x(1+(ell-1)x), and let
F_0=0, F_1=1, F_n=aF_(n-1)+bF_(n-2). The Section 2.5 summands are

    W_n=C_1 F_n,    Y_n=C_0 b F_(n-1),    C_n=W_n+Y_n  (n>=2).

This identity was checked coefficient by coefficient throughout the grid.
The journal factorization proves log-concavity of W_n and Y_n. Their sum
does not inherit log-concavity from that fact alone.

**A specific failed sufficient condition.** Modes of the two summands are
not always adjacent. At n=3, ell=5, their coefficient lists, starting at
degree zero, are

    W=[1,28,320,1937,6744,13632,14976,6912],
    Y=[0,1,16,95,248,240],
    C=[1,29,336,2032,6992,13872,14976,6912].

The unique modes are respectively 6,4,6. Thus an argument requiring mode
distance <=1 for these particular summands cannot cover all parameters.
C itself is log-concave in this example. This is neither a counterexample
to the original target nor a general impossibility result for decomposition
methods. The witness is an elementary diagnostic, not a result-note candidate.

**New test justified by the evidence.** Throughout the tested grid, the
minimum distance between a mode of W_n and a mode of Y_n never exceeded 2,
and 2 is attained above. Test the precise auxiliary claim:

    For all integers n>=2, ell>=3, there exist modes r of W_n and s of Y_n
    such that |r-s|<=2.

A proof would replace the possible O(sqrt(n)) interval by a uniform interval
of at most two index steps for every length and every uniformity. This
scope differs from the newly found eventual theorem with parameter-dependent
threshold. If the distance is two, full unimodality still requires ruling
out a valley at the one intermediate index. This is a single coherent route
to the frozen target, not a claim that either step has been established.
An exact pair with minimum mode distance >2 would refute only this auxiliary
claim and require changing the route.

Suggested bounded first proof attack: use the polynomial recurrence for F_n
or its explicit sum

    F_n = sum_(j=0)^floor((n-1)/2) binom(n-1-j,j) a^(n-1-2j) b^j

to seek coefficient-ratio comparisons between W_n and Y_n shifted by two.
Do not repeat an adjacent-mode conjecture or claim novelty for an eventual
fixed-uniformity theorem already asserted by the September preprint.

Triage recommendation: advance for one bounded research pass on the uniform
two-step mode bound. No mathematical candidate is accepted or released.
