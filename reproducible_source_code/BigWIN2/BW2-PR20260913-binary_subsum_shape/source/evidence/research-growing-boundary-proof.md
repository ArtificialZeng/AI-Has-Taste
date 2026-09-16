# A growing range of boundary log-concavity

Job: `primary-20260913-binary-subsum-shape-research-9e631dc6dcdd`.
Proposed partial theorem for fresh review, not an accepted manuscript.
The original all-coefficient assertion remains unresolved.

## Exact statement

Use N_n, d(n), c_(n,j) and B(n) from `problem.md`; here B(n) denotes the
number of binary partitions, not the recurrence's polynomial summand.
For every real epsilon with 0<epsilon<1 there is an integer n_epsilon such
that, for every integer n>=n_epsilon, strict log-concavity holds at every
integer position

    1 <= j <= floor((1-epsilon)*sqrt(log_2(n)/2))

and at every reflected position d(n)-j. In particular, every fixed number
of boundary inequalities eventually holds. No assertion is made for the
remaining positions, for optimality of the constant, or for an explicit
optimal threshold n_epsilon.

An explicit sufficient test, proved below, avoids an unspecified asymptotic
threshold. Set

    M_n = min_(0<=K<=floor(log_2 n)) (n+2^(K+1)-K-2)/(K+1).

For n>=2 and an internal integer index 1<=j<=n, if j*M_n<n and

    binom(n,j)^2 * (1-j*M_n/n)^2
      > binom(n+j-2,j-1) * binom(n+j,j+1),                 (G1)

then c_(n,j)^2>c_(n,j-1)c_(n,j+1). All quantities in (G1) are rational
or integral. This is sufficient, not necessary. It may be conservative.

## 1. An elementary mean-multiplicity bound

Choose a binary partition lambda of n uniformly and write mu_q for the
mean multiplicity of its part q, where q is a power of two. Write mu=mu_1.
Removing r copies of q is a bijection between partitions with at least r
copies of q and binary partitions of n-rq. Hence, setting B(h)=0 for h<0,

    mu_q = sum_(r>=1) B(n-rq)/B(n).                         (G2)

The counts B(h) are nondecreasing for h>=0 by addition of a part 1.
Group the numerator sum defining mu into its first q-1 terms and the blocks
rq,...,(r+1)q-1, r>=1. Monotonicity gives

    mu <= q-1+q*mu_q.                                     (G3)

Taking expectations of the total weight of the partition gives
sum_(k>=0) 2^k mu_(2^k)=n. Sum the lower bounds in (G3) for k=0,...,K:

    n >= (K+1)*mu - (2^(K+1)-K-2).

This proves mu<=M_n. There is no asymptotic enumeration assumption here.
In particular, with L=log_2 n and K=floor(L-log_2 L), for n>=4,

    mu/n <= M_n/n <= (1+2/L)/(L-log_2 L) = (1+o(1))/L.     (G4)

Indeed K>=0, K<=floor L, 2^(K+1)<=2n/L and
K+1>=L-log_2 L>0. Dropping the nonpositive term -(K+2) in the numerator
of the bound proves (G4).

## 2. Coefficient envelopes

The summand h_(n,lambda) contains the factor (1+x)^(n-m_lambda(1));
its other factors have constant coefficient 1 and nonnegative coefficients.
Consequently, for 0<=j<=n,

    c_(n,j) >= B(n)*binom(n,j)*(1-j*mu/n).                 (G5)

To see this without any convexity assumption, choose a uniform j-element
subset of n labeled elements, of which m are forbidden. The probability
of meeting the forbidden set is at most j*m/n, by the union bound (or by
Markov's inequality for the number of forbidden elements selected). Thus
binom(n-m,j)>=binom(n,j)*(1-j*m/n), including cases when the right side
is nonpositive. Average over m=m_lambda(1).

A second version of the same bound is useful for asymptotics:

    c_(n,j) >= B(n)*n^j/j! * (1-delta_(n,j)),
    delta_(n,j) = j*mu/n+j(j-1)/(2n).                     (G6)

Draw j independent elements from n labels. By the union bound, the probability
of either a forbidden draw or a collision is at most j*m/n+binom(j,2)/n.
The number of ordered favorable tuples is j!*binom(n-m,j). Averaging proves
(G6). This remains valid when the lower bound is negative.

For an upper bound, use coefficientwise order of formal series. Each exponent
floor(n/2^k)-m_lambda(2^k) lies between 0 and n. Thus

    h_(n,lambda)(x) <=_coeff product_(k>=0) (1+x^(2^k))^n
                         = (1-x)^(-n).                  (G7)

The infinite product identity follows from unique finite binary expansions:
product_(k>=0)(1+x^(2^k))=(1-x)^(-1). It is an identity of formal series;
only finitely many factors affect any fixed coefficient. Therefore, for j>=0,

    c_(n,j) <= B(n)*binom(n+j-1,j)
             <= B(n)*n^j/j!*exp(j(j-1)/(2n)).             (G8)

The last inequality follows from product_(r=0)^(j-1)(1+r/n)
<=exp(sum r/n). Squaring (G5), using its positive lower bound when j*M_n<n,
and applying (G8)'s first bound at j-1,j+1 proves (G1).

## 3. Uniformity in the growing index

Fix epsilon and let alpha=1-epsilon. Put L=log_2 n and
J_n=floor(alpha*sqrt(L/2)). For n large these are internal indices and J_n<n:
the degree formula gives d(n)>=2*floor(n/2)>=n-1.

By (G4), uniformly for 1<=j<=J_n,

    delta_(n,j)=O(L^(-1/2))=o(1),
    j*delta_(n,j) <= alpha^2/2+o(1),
    j*delta_(n,j)^2=o(1),   j*(j^2-j+1)/n=o(1).          (G9)

For example, the two parts of j*delta are j^2*mu/n<=alpha^2/2+o(1)
and j^2(j-1)/(2n)=O(L^(3/2)/n). The stated uniform remainder bounds follow.
In particular 1-delta is positive. Combining (G6) and (G8) yields

    c_(n,j)^2/(c_(n,j-1)*c_(n,j+1))
       >= ((j+1)/j)*(1-delta_(n,j))^2
                       *exp(-(j^2-j+1)/n).              (G10)

All denominator coefficients are positive, as also follows from prior
Proposition 4.1. Take logs and multiply by j. The elementary bounds
log(1+x)>=x-x^2/2 for x>=0 and
log(1-y)>=-y-y^2/(2(1-y)) for 0<=y<1 imply, uniformly on this range,

    j*log(right side of (G10))
        >= 1-1/(2j)-alpha^2-o(1).                        (G11)

Choose a fixed integer J so that 1/(2J)<(1-alpha^2)/2. Equation (G11)
is positive for all J<=j<=J_n and all sufficiently large n. For the finitely
many 1<=j<J, the right side of (G10) tends to (j+1)/j>1. Increasing the
same n_epsilon handles all these indices too. This proves the uniform strict
inequality, not just a pointwise assertion with a threshold depending on j.
The prior palindromicity of N_n proves the reflected inequalities.

## Dependencies, contribution, and limits

The proof uses only the frozen partition-sum definition, elementary counting,
the union bound, formal power series, and elementary logarithm bounds. The
degree and reflection statements are BBFM Proposition 4.1; they also follow
directly because every summand is palindromic of the same degree.
No asymptotic theorem about binary partition counts is invoked.

The proposed contribution is an unbounded boundary range for the corrected
log-concavity question, together with the count-free finite criterion (G1).
The result is partial: the unresolved central range is not controlled. The
proof method and the numerical constant are not asserted to be optimal.
Bounded current literature comparisons are in
`literature/research-pass2-source-check.md`; priority is not certified.

`evidence/research_growing_boundary.py` checks the mean bound and coefficient
envelopes using exact rational arithmetic and separately reconstructs low
coefficients. Its finite checks calibrate the proof and do not prove its
infinite quantifiers. Gap list for the stated argument: no known gaps;
fresh mathematical and novelty review is still required.
