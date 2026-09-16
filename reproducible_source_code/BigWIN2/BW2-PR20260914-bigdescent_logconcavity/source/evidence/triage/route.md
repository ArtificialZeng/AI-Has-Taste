# Triage mathematics — 2026-09-14 Asia/Shanghai

Job: primary-20260914-bigdescent-logconcavity-triage-21d5b29238e0.
These are source reductions, a derived reformulation, and bounded exact tests.
There is no claimed new log-concavity theorem or independently reviewed result.

## Immediate coverage from the source

Elizalde–Rivera–Zhuang, DOI 10.1007/s00026-026-00805-1,
Theorems 1.1–1.2 give the equivalence classes listed in problem.md.
The following implications require no new enumeration theorem:

* For 123 and n >= 2, Theorem 2.13 gives
  b[n,k] = 2/(n+1) C(n+1,k+2) C(n-2,k).
  Each binomial factor is log-concave in k, so their product is; their
  supports are intervals. The rows n=0,1 are checked directly.
* For 231 and 312, Theorem 4.5 and reverse-complementation give real-rootedness,
  hence coefficient log-concavity for nonnegative coefficients.
* For {213,231}, {132,312}, {213,312}, {132,231}, Theorems 3.1/3.3 give
  b[n,k] = C(n,2k+1) for n >= 1. The consecutive ratios of a binomial
  row decrease, so their products over two consecutive steps decrease too;
  the odd subsequence is log-concave. The n=0 row is (1).
* Section 3.6 treats six pairs. The {123,231}/{123,312} and
  {132,321}/{213,321} classes have degree at most one. The {231,312}
  row is constant. For {123,321}, the only nonconstant rows are
  (2,2) at n=3 and (1,2,1) at n=4; rows n >= 5 vanish.

This covers 13 families. The other eight belong to four classes:
132/213; 321; {123,132}/{123,213}/{132,213}; {231,321}/{312,321}.
"Other" here means not settled by the source implications just given;
it is not an exhaustive current-literature claim.

## Positive formula for the exceptional class

Let f[n,k] count binary words of length n ending in 1, weighted by
occurrences of 10 plus occurrences of 011. By source Lemmas 3.6/3.9,
this equals the big-descent count for the exceptional three pairs.
Write C(a,b)=0 unless 0 <= b <= a, with a a nonnegative integer.
For n >= 1 and k >= 0 the following identity follows by run decomposition:

    f[n,k] = sum_{r=0}^{n-1} C(r+1,k+1-r) C(n-r-1,k).           (1)

Derivation: a word other than an all-ones word is uniquely

    1^a 0^{z_1}1^{o_1} ... 0^{z_r}1^{o_r},

where r >= 1, a >= 0, and all z_i,o_i >= 1. If exactly j of the o_i
are at least two, the statistic is r-1+j when a=0 and r+j when a>=1.
For fixed r,j, the two length generating functions, without the statistic
weight, are respectively

    C(r,j) x^{2r+j}/(1-x)^{r+j},
    C(r,j) x^{2r+j+1}/(1-x)^{r+j+1}.

The resulting contributions to coefficient k are

    [C(r,k+1-r) + C(r,k-r)] C(n-r-1,k)
      = C(r+1,k+1-r) C(n-r-1,k).

All-ones words contribute 1 at k=0 and are exactly the r=0 term of (1).
There cannot be n zero runs in a word of length n ending in 1, so the stated
range suffices. Empty permutations are handled separately by f[0,0]=1.
This derivation is a reformulation of the published enumeration, not a
novelty claim. In particular, positive summands alone do not prove LC.

## A rejected sufficient condition and a feasible alternate test

Let F_r(k) be the r-th summand in (1). The sufficient condition

    2 F_r(k)F_s(k) >= F_r(k-1)F_s(k+1) + F_r(k+1)F_s(k-1)

for every pair r,s is FALSE: at n=4, r=0, s=1, k=1 the summands are
(1,0,0) and (1,4,1), giving mixed determinant -1. The complete row
is (2,5,1), which is log-concave. This certificate rules out only the
specified termwise sufficient condition, not a general method class or
the original conjecture.

A three-state positive recurrence follows by appending a binary letter.
Let A_n, B_n, C_n enumerate words ending in 0, ending in 01, and ending
in 1 but not 01, respectively. The single letter 1 belongs to C_1.
These letters A,B,C are suffix polynomials, not the source's B_n(t;Pi).

    (A_1,B_1,C_1) = (1,0,1),
    A_{n+1} = A_n + t B_n + t C_n,
    B_{n+1} = A_n,
    C_{n+1} = t B_n + C_n,
    f_n(t) = B_n(t) + C_n(t).

This is equivalent to the source's Proposition 3.7. For polynomial P put
L_k(P)=p_k^2-p_{k-1}p_{k+1}; put
M_k(P,Q)=2p_kq_k-p_{k-1}q_{k+1}-p_{k+1}q_{k-1}.
Then L_k(B_n+C_n)=L_k(B_n)+L_k(C_n)+M_k(B_n,C_n).
Thus simultaneous nonnegativity of those three quantities would suffice.
It is not claimed that these inequalities alone define an invariant cone.

The exact script positive_formula.py compares (1) and this recurrence to
the published rational generating function for 1 <= n <= 80, 0 <= k <= n:
3,320 coefficients agree. For these actual suffix states, each state is
log-concave and M_k(B_n,C_n) >= 0 for every 1 <= k <= n-1 checked.
It also tests LC of all partial sums sum_{r=0}^R F_r(k) for
1 <= n <= 80 and 0 <= R <= n-1 (3,240 rows); no failure was found.
These strengthened finite checks differ from intake's checks of full rows.
They are leads, not a qualified new conjecture or a uniform theorem.

One next test: derive determinant recurrences for the actual suffix triple
and attempt a closed inductive system proving L_k(A_n), L_k(B_n),
L_k(C_n), and M_k(B_n,C_n) >= 0 for all n,k. Falsify each added
inequality against exact suffix rows before spending effort proving it.
The success criterion is a symbolic invariant with base cases and induction;
a larger finite range alone is not success.
