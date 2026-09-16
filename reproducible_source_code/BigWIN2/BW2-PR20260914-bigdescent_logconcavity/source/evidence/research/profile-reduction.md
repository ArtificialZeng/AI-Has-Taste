# Event profiles and a finite reduction for fixed coefficient index

Research job: primary-20260914-bigdescent-logconcavity-research-ff87ce2dd87c.
Status: exact transfer identity and finite reduction, plus explicitly delimited computational verification. The all-index assertion below is an unproved working conjecture, not a qualified candidate.

## The strengthened assertion under test

For n>=1 and a binary word w of length n ending in 1, let E(w) be the subset of {2,...,n} containing the ending position of every 10 or 011 factor. At most one of these factors can end at a given position. Define

    F_n(t; z_2,...,z_n) = sum_w t^{|E(w)|} product_{i in E(w)} z_i
                       = sum_k f_{n,k}(z) t^k.

The working assertion is that, for every n>=1 and k>=1,

    f_{n,k}(z)^2 - f_{n,k-1}(z) f_{n,k+1}(z)

has only nonnegative monomial coefficients. Counts outside the support are zero. Specializing every z_i to 1 gives the exceptional three pairs in the original problem. More generally this assertion implies LC for every nonnegative assignment of position weights, a substantive strengthening in this class. It is not equivalent to the original 21-family assertion.

## Transfer identity

In suffix order A=ending 0, B=ending 01, C=ending 1 but not 01, write column vectors and

    P = [[1,0,0], [1,0,0], [0,0,1]],
    Q = [[0,1,1], [0,0,0], [0,1,0]],
    v = (1,0,1)^T,   u = (0,1,1)^T.

Appending at position i acts by P+t z_i Q. Therefore

    F_n = u^T (P+t z_n Q) ... (P+t z_2 Q) v.

This follows directly from the two possible appended letters in each suffix state, including the initial single-letter words 0 and 1. Matrix multiplication gives P^2=P and Q^3=0.

For a monomial profile e=(e_2,...,e_n) in {0,1,2}^{n-1}, the coefficient of z^e in F_n(x;z) F_n(y;z) is

    H_e(x,y) = (u tensor u)^T R_{e_n} ... R_{e_2} (v tensor v),

where R_0=P tensor P, R_1=x Q tensor P + y P tensor Q, and R_2=xy Q tensor Q. In each tensor state the first coordinate belongs to the first word. If sum e_i=2k, the coefficient of z^e in the LC difference is

    [x^k y^k] H_e - [x^{k-1} y^{k+1}] H_e.

Profiles with any exponent exceeding 2 do not occur. Both products in the LC difference are homogeneous of total z-degree 2k, so all other total degrees have coefficient zero. This proves that the profiles tested are the complete coefficient domain.

## Compression lemma and exhaustive coverage

Since R_0^2=R_0, every nonempty consecutive run of zeros in e can be replaced by a single zero without changing H_e. A profile of total degree 2k has at most 2k nonzero positions and at most 2k+1 zero runs. Thus its compressed length is at most 4k+1, including leading and trailing zero blocks. This proves: coefficientwise LC at a fixed index k for all word lengths is equivalent to checking all zero-compressed profiles of total degree 2k. In particular, the assertion has a finite test for each fixed k; this is stronger coverage than merely checking n up to a numerical cutoff.

A compressed nonempty profile consists of a list of l entries from {1,2}, with sum 2k, and independently optional single zeros in its l+1 gaps, including the two boundaries. Its count is

    N_k = sum_{l=k}^{2k} binom(l,2k-l) 2^{l+1}.

The recursive script profile_test.py enumerates exactly this parametrization. It starts with an optional leading zero and the first event, then chooses an optional zero before each later event, and finally tests both choices of trailing zero. It includes profiles whose count is zero. It tracks the number of first-word events using exact integers; the second-word number is fixed by the profile total. Its JSON records the completed k range and counts. This is an exhaustive finite certificate for the specified indices, conditional only on the transfer and compression proved above; it is not an all-k theorem or independent review.

## A two-dimensional structural simplification

On the image of P, vectors have the form (a,a,c). Identifying this vector with (a,c), the maps P Q and P Q^2 have matrices

    [[1,1],[1,0]]    and    [[1,0],[0,0]],

respectively. Runs of three consecutive events are impossible, and separated single events generate Fibonacci matrices. This supplies a possible route to a structural proof for arbitrary profiles. It does not yet prove the required central-versus-adjacent coefficient inequality.

## Precise remaining test

For the pair-profile matrices R_0,R_1,R_2, determine whether every boundary scalar H_e(x,y) is Schur-positive in two variables. This would imply the central-versus-adjacent inequality and is a stronger, falsifiable sufficient condition. First test every coefficient difference h_j-h_{j-1} for 1<=j<=floor(sum(e)/2) on the existing compressed-profile enumeration; reject this sufficient condition upon an exact failure. If it survives, exploit P^2=P and the two Fibonacci/projector blocks to seek a preservation proof. No claim of Schur positivity is made here.
