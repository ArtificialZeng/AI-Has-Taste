# A proof of the fixed-column Stirling transition, submitted for review

Job: `primary-20260914-stirling-transition-research-d94530e09967`.
Date: 2026-09-14. This is mathematical evidence for a proposed resolution;
it has not undergone the required fresh referee pass.

## 1. The original statement

Let c(n,k) be the number of permutations of n elements with k cycles, with
c(0,0)=1 and c(n,k)=0 outside 0<=k<=n. Put

    D_k(n)=c(n,k)^2-c(n-1,k)c(n+1,k), n>=1.

For every integer k>=1 there is an integer N_k such that D_k(n)>=0 for
1<=n<N_k and D_k(n)<=0 for n>=max(1,N_k). The argument below proves this
in the precise reading of `problem.md`; in fact the latter inequalities
are strict for the threshold constructed below.

## 2. An elementary preservation lemma

For t>0 define

    F_t(u,v)=u(1+t v)/(1+t u).

Suppose 0<=u<=v, h>=2u-v, and w>=2v-u, with w finite. Then

    F_t(w,v)-2F_t(v,u)+F_t(u,h)
      >= 2t^2(v-u)^3 / [(1+t u)(1+t v)(1+t(2v-u))] >= 0.    (3)

Indeed, for v>=0 the function w -> F_t(w,v) is increasing on w>=0,
as its derivative is (1+t v)/(1+t w)^2. The function h -> F_t(u,h)
is nondecreasing on the entire real line, with derivative t u/(1+t u).
Thus the left side is bounded below by

    F_t(2v-u,v)-2F_t(v,u)+F_t(u,2u-v).

Clearing the three positive denominators gives exactly the right side
of (3). The value 2u-v may be negative; this is harmless because the
second argument of F_t occurs only in its numerator. The same bound
holds for w=+infinity, interpreting F_t(+infinity,v)=v+1/t, by a limit.

Consequently, multiplication by (1+t z) preserves convexity of adjacent
coefficient ratios in the following form. Let a_0,...,a_m>0, m>=1,
and set R_0=0 and R_j=a_(j-1)/a_j for 1<=j<=m. Assume R_j is
nondecreasing and discretely convex on 0,...,m. Set a_(-1)=a_(m+1)=0
and b_j=a_j+t a_(j-1), 0<=j<=m+1. Then, with S_0=0,

    S_j=b_(j-1)/b_j=F_t(R_j,R_(j-1))       (1<=j<=m),
    S_(m+1)=R_m+1/t.

Extend the old ratios by R_(-1)=0 and R_(m+1)=+infinity.
For each center 1<=j<=m use (3) with

    (h,u,v,w)=(R_(j-2), R_(j-1), R_j, R_(j+1)).

All its hypotheses hold. At j=1, the inequality h>=2u-v is
0>=-R_1. At j=m, the infinity convention supplies the correct last
new ratio. Hence S_(j+1)-2S_j+S_(j-1)>=0 at every required center.
Moreover S_1>0; convexity starting with S_0=0 implies that all successive
differences are positive. This also establishes the nondecreasing hypothesis
needed for the next multiplication. For the base m=1, R_0=0<R_1 and
there are no convexity centers to check.

## 3. Elementary symmetric coefficients

For positive x_1,...,x_m, write e_j=e_j(x_1,...,x_m), the coefficient
of z^j in the product of (1+x_i z). Put e_0=1 and e_j=0 for j<0.
Induction from one factor using Section 2 proves that

    R_0=0, R_j=e_(j-1)/e_j (1<=j<=m)

is increasing and discretely convex. No real-rootedness theorem or
external symmetric-function inequality is required for this induction.
The preservation lemma is not asserted to be new in the literature.

Fix 1<=r<=m and set A=e_r, B=e_(r-1), C=e_(r-2), E=e_(r-3).
Here A,B>0. Define

    H=B^2-A C,
    U=B^2 C-2A C^2+A B E.

Then H>0. For r=1 this says H=1. For r>=2 it follows from
R_r>R_(r-1). Also U>=0: U=0 for r=1; for r=2, U=B^2-2A>=0
is exactly R_2-2R_1+R_0>=0 after multiplication by A B.
For r>=3,

    U/(A B C)=R_r-2R_(r-1)+R_(r-2)>=0.                       (4)

These statements remain true if A,B,C,E are all multiplied by the same
positive constant: H scales quadratically and U cubically.

## 4. The formerly unresolved numerator

The usual insertion of the largest element into a permutation yields

    c(n+1,k)=n c(n,k)+c(n,k-1).

Equivalently, induction gives the row polynomial

    sum_k c(n,k) z^k = z(z+1)...(z+n-1)
      = (n-1)! z product_(j=1)^(n-1)(1+z/j), n>=1.

Fix n>=k>=2 and put r=k-1, m=n-1. Thus

    (A,B,C,E)=(c(n,k),c(n,k-1),c(n,k-2),c(n,k-3))

is (n-1)! times the four coefficients of Section 3 at
(x_1,...,x_m)=(1,1/2,...,1/(n-1)). Hence H>0 and U>=0.
Set q_k(n)=c(n,k-1)/c(n,k). Two recurrence steps give

    Q1=n A+B,
    Q2=n(n+1) A+(2n+1) B+C,
    q_k(n+1)=(n B+C)/Q1,
    q_k(n+2)=[n(n+1)B+(2n+1)C+E]/Q2.

The denominator A Q1 Q2 is positive. Its cleared second-difference
numerator is the expression (2) in `evidence/ratio-reduction.md`:

    P=(n A+B)H+n(2B^3-3A B C+A^2 E)+U.

The decisive decomposition is

    P=(n A+B)H+(2n/B)H^2+(1+n A/B)U.                        (5)

It follows immediately by expanding
2B^3-3A B C+A^2 E = 2H^2/B+A U/B.
All coefficients in (5) are positive, H>0, and U>=0. Therefore

    q_k(n)-2q_k(n+1)+q_k(n+2)>0   (n>=k>=2).                (6)

For k=1 and n>=1, q_1(n)=0, so the corresponding weak inequality
holds identically. This proves the universal sufficient lemma selected
by triage, with its full domain and boundary conventions.

## 5. Sign transition and existence of a finite threshold

Fix k>=1. Define d_n=q_k(n)-q_k(n+1), n>=k. By (6) and its
k=1 boundary, d_n is nonincreasing. The set

    J_k={j>=k : d_j<1}

is nonempty: otherwise for every integer t>=0,

    q_k(k+t)=q_k(k)-sum_(j=k)^(k+t-1) d_j <= q_k(k)-t,

contradicting q_k(k+t)>=0 for an integer t>q_k(k).
Let j_0=min J_k and N_k=j_0+1. For n>=k+1 the recurrence gives

    D_k(n)/[c(n-1,k)c(n,k)]=q_k(n-1)-q_k(n)-1=d_(n-1)-1.   (7)

The denominator is positive. For k+1<=n<N_k, minimality of j_0
gives d_(n-1)>=1. For n>=N_k, monotonicity gives
d_(n-1)<=d_(j_0)<1. Hence D_k(n)>=0 before N_k on this support,
and D_k(n)<0 for every n>=N_k. Finally D_k(n)=0 for 1<=n<k
and D_k(k)=1, while N_k>=k+1. This proves the whole original assertion.
For k=1 this construction gives N_1=2. The optional k=0 boundary
has D_0(n)=0 for all n>=1.

## Dependencies, verification, and scope

The proof uses only the permutation recurrence, finite products, the
explicit rational identity (3), induction, and telescoping. All positivity
and endpoint assumptions used in division are stated above. No asymptotic
approximation, finite-table extrapolation, inaccessible theorem, or
unaudited literature statement is a mathematical dependency.

The accompanying exact script checks the identities and adversarial finite
instances as error detection, not as the proof of the quantified assertion.
The current primary-source comparison is recorded separately. In particular,
Fan and Wang (2026) report a related ratio-convexity result; this proof does
not claim priority for that general property. The proposed contribution is
the complete fixed-column sign transition stated by Liang and Sagan.

Known mathematical gaps in this proposed proof: none identified in this pass.
Fresh mathematical review and the literature assessment remain pending.
