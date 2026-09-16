# Positivity through five increments: proposed finite-case result

Job: primary-20260913-fgn-positivity-research-1f1ccfebc1c5.
Date: 2026-09-13 (Asia/Shanghai).
This is a proof dossier for a result-note candidate, not a manuscript or an
independent referee acceptance. The frozen original all-n claim is unresolved.

## Exact proposed statement

For every real H in (1/2,1), define rho and Gamma exactly as in source.md
and problem.md. Then Gamma_n^k(H)>0 for all integers 2<=n<=5 and 2<=k<=n.
In particular the four coefficients of the projection of Delta_1 onto
Delta_2,Delta_3,Delta_4,Delta_5 are positive throughout the full H interval.

Put t=2H and let N_54(t) be the determinant of T_4=(rho_|i-j|)_(i,j=1)^4
with column 3 replaced by (rho_1,rho_2,rho_3,rho_4)^T. In addition, the
certificate proves the explicit bound

    16*N_54(t) / ((t-1)*(2-t)^3) > 27/10,   1<=t<=2,

where the quotient at either endpoint means its analytic continuation.
This continuation statement does not assert that the degenerate predictor
at H=1 is defined. No result for n>=6 is proposed.

## Covariance facts and the conditional edge argument

All facts needed below can be obtained directly from the defining rho.
For 0<t<2, set

    C_t = integral_0^infinity (1-cos u)*u^(-1-t) du > 0.

The integral converges at both endpoints. Scaling and taking a centered
second difference of |j|^t give, for every integer j including j=0,

    rho_|j| = C_t^(-1) integral_0^infinity
                         cos(j*u)*(1-cos u)*u^(-1-t) du.

Thus for a nonzero finite real vector v,

    sum_(i,j) v_i*v_j*rho_|i-j|
      = C_t^(-1) integral_0^infinity
          |sum_j v_j*exp(i*j*u)|^2*(1-cos u)*u^(-1-t) du > 0.

A nonzero trigonometric polynomial cannot vanish identically on an open
interval, and the weight is positive except at a discrete set. This proves
strict positive definiteness of every finite covariance matrix, including
all determinants and residual variances used below.

For 1<t<2, the centered second difference also gives, for j>=1,

    rho_j = t*(t-1)/2 * integral_(-1)^1
                      (1-|u|)*(j+u)^(t-2) du.

The possible endpoint singularity at j=1 is integrable. This representation
proves rho_j>rho_(j+1)>0 for j>=1. Also 0<rho_1=2^(t-1)-1<rho_0=1.
For j>=2, the function z^(t-2) is strictly log-convex on z>0. The strict
pointwise geometric-mean inequality in this integral, followed by
Cauchy--Schwarz, gives

    rho_j^2 < rho_(j-1)*rho_(j+1),   j>=2.

The remaining j=1 inequality follows from the exact identity

    rho_2-rho_1^2 = (rho_1-rho_3)/2 > 0.

Consequently the positive ratios rho_(j+1)/rho_j are strictly increasing
for all integers j>=0.

Suppose an entire row g_k=Gamma_n^k, 2<=k<=n, is positive. Use a centered
Gaussian vector (X_1,...,X_(n+1)) with this positive definite stationary
covariance; equivalently use orthogonal linear projections. Residualizing
X_2 against X_3,...,X_(n+1) shows that the sign of Gamma_(n+1)^2 is the
sign of

    rho_1 - sum_(k=2)^n g_k*rho_k
      = sum_(k=2)^n g_k*(rho_(k-2)-rho_k) > 0.

Here the equality is the l=2 equation for the n-th row, and the denominator
is a strictly positive residual variance. This uses positivity of the
preceding row explicitly, avoiding an unconditional weighted-sum inference.

Residualizing X_(n+1) against X_2,...,X_n, and using time reversal, gives

    Gamma_(n+1)^(n+1)
      = [rho_n-sum_(k=2)^n g_k*rho_(n+1-k)]
          / [1-sum_(k=2)^n g_k*rho_(k-1)].

The denominator is a strictly positive residual variance. The l=n equation
for the preceding row states rho_(n-1)=sum g_k*rho_(n-k). Hence the numerator
can be written as

    sum_(k=2)^n g_k*rho_(n-k) *
        [rho_n/rho_(n-1)-rho_(n+1-k)/rho_(n-k)] > 0,

by strict increase of the ratios. Both edge coefficients of the new row
are therefore positive. This conditional argument is a standard projection
recursion; no novelty for it is claimed.

## The n=4 middle coefficient and the inherited n=5 sign

Write

    q = rho_2+rho_2^2-rho_1^2-rho_1*rho_3,
    K = (1-rho_2)*(1-rho_4)-(rho_1-rho_3)^2.

Cramer's rule, or the exact polynomial determinant expansion in
certify_n5.py, gives

    Gamma_4^3 = (1-rho_2)*q/det(T_3),
    Gamma_5^3 = q*K/det(T_4).

For U=X_1-X_5 and V=X_2-X_4, their covariance is

    2 * [[1-rho_4, rho_1-rho_3],
         [rho_1-rho_3, 1-rho_2]].

The coefficient vectors of U,V are linearly independent; strict positive
definiteness of the five-variable covariance makes this matrix positive
definite. Its determinant is 4K, so K>0. This identity is also consistent
with the usual predictor reflection recursion; it is not proposed as a
new general prediction theorem.

Substitution of rho gives

    F(t):=4q = 9^t-8^t-2*6^t+4*4^t-2*2^t-1.

We recall a short form of the standard exponential Descartes rule. If
E(t)=sum c_i*exp(lambda_i*t), with increasing distinct real lambda_i and
nonzero c_i, then its real zeros, counted with multiplicity, number at most
the sign variations of the ordered coefficients. For zero variations the
assertion is immediate. Otherwise choose lambda strictly between two
consecutive exponents at a coefficient sign change. Differentiating
exp(-lambda*t)*E(t) changes the signs of all coefficients to the left of
lambda, and removes exactly that one variation. Induction and Rolle's
theorem, applied on any finite interval containing the proposed zeros,
give the bound, including multiplicities.

At increasing bases 1,2,4,6,8,9, the coefficients of F are
-1,-2,4,-2,-1,1, with three variations. Exactly,

    F(1)=F(2)=0, F(3)=24,
    F'(1)=2*log(27/16)>0,
    F'(2)=18*log(243/256)<0.

There is a zero in (2,3) because F is negative just right of 2 and positive
at 3. These three zeros exhaust the bound. Thus F has no zero in (1,2)
and is positive there, since F'(1)>0. This proves q>0 throughout the range.
The n=4 inequality was already stated in the 2025 paper; this argument
supplies an analytic global certificate, not priority for that statement.

## The remaining n=5 cofactor: exact interval certificate

Set P(t)=16*N_54(t). Its exact 30 pairs (base,coefficient) in the expansion
P(t)=sum_b c_b*b^t are recorded in n5-certificate.json. They are independently
recomputed by a standard-library polynomial determinant expansion in
certify_n5.py, not merely copied from the triage output. The same computation
verifies exactly

    P(1)=0, P(2)=P'(2)=P''(2)=0,
    P'(1)=80*log 2-48*log 3=16*log(32/27)>0.

For endpoint derivatives at 2 the code treats log 2, log 3 and log 5 as
formal independent variables, expands their powers, and checks that each
polynomial coefficient vanishes. Thus no approximate endpoint cancellation
is substituted for these identities.

Let x=2-t and define A_k=(-1)^k*P^(k)(2)/k!. The entire exponential series,
with its exact initial vanishing, gives

    P(2-x)=x^3*G(x),
    G(x)=sum_(k=3)^infinity A_k*x^(k-3),   G(1)=0.

On 0<=x<=1 the continued normalized cofactor is

    R(x) = G(x)/(1-x).

Take N=26 and G_N(x)=sum_(k=3)^N A_k*x^(k-3). Instead of dividing an
approximate zero, use the exactly divisible polynomial

    R_N(x) = [G_N(x)-G_N(1)]/(1-x)
           = -sum_(k=4)^N A_k*(1+x+...+x^(k-4)).

Its degree is 22. The error extends continuously to x=1 and satisfies

    |R(x)-R_N(x)| <= sum_(k=N+1)^infinity (k-3)*|A_k|.

All bases are <=108, their logarithms are <5, and
S=sum_b |c_b|*b^2=212096. Hence |A_k|<=S*5^k/k!. For k>=N+1 the ratio
of consecutive terms (k-3)*5^k/k! is at most 5/(N-2). Therefore uniformly,

    |R-R_N| <= S*(N-2)*5^(N+1)/(N+1)! / (1-5/(N-2))
             = 790119171142578125/179590728782941572096
             < 1/200.

Every coefficient enclosure used for R_N is rational. For p in {2,3,5},
put z=(p-1)/(p+1). The positive-series identity and tail bound are

    L_p = 2*sum_(j=0)^119 z^(2j+1)/(2j+1),
    0 < log(p)-L_p
        <= 2*z^241 / (241*(1-z^2)).

Outward rounding to denominator 10^30 gives the consecutive integer
numerator intervals

    log 2: [693147180559945309417232121458,
            693147180559945309417232121459] / 10^30,
    log 3: [1098612288668109691395245236922,
            1098612288668109691395245236923] / 10^30,
    log 5: [1609437912434100374600759333226,
            1609437912434100374600759333227] / 10^30.

Prime factorization gives log intervals for every base. For each k=3,...,26,
interval substitution in

    A_k = (-1)^k/k! * sum_b c_b*b^2*(log b)^k

followed by outward rational rounding to denominator 10^12 gives the
intervals in n5-certificate.json. No binary or decimal floating arithmetic
is used to generate any of these bounds.

Writing R_N(x)=sum_(j=0)^22 d_j*x^j, its degree-22 Bernstein coefficients are

    beta_i = sum_(j=0)^i [binom(i,j)/binom(22,j)]*d_j,
    d_j = -sum_(k=j+4)^26 A_k,      0<=i,j<=22.

The Bernstein basis binom(22,i)*x^i*(1-x)^(22-i) is nonnegative and sums
to one on [0,1]. The identity for beta follows by expanding x^j in this
basis. The following integers divided by 10^6 are certified lower bounds
for beta_0,...,beta_22, in order:

    27182814, 24620654, 22265492, 20109735, 18143415, 16355122,
    14732704, 13263778, 11936093, 10737778, 9657511, 8684622,
    7809147, 7021851, 6314230, 5678484, 5107496, 4594788,
    4134485, 3721266, 3350327, 3017335, 2718387.

Each exceeds 271/100. Consequently, including the two continued endpoints,

    R(x) > 271/100 - 1/200 = 541/200 > 27/10.

This proves the proposed cofactor bound, and P(t)>0 for every 1<t<2.
In particular Gamma_5^4=P/(16*det(T_4))>0. The certificate also encloses
A_3 between 27182814079941/10^12 and 27182814079942/10^12, confirming
the positive limit at t=2 directly.

## Assembly, adversarial checks and limits

The n=2 row is positive because Gamma_2^2=rho_1>0. The conditional edge
argument then supplies both coefficients of the n=3 row. It supplies the
two outer coefficients at n=4, and q>0 supplies the middle coefficient.
At n=5 it again supplies both outer coefficients; q*K>0 supplies Gamma_5^3,
and the certified P>0 supplies Gamma_5^4. This completes the finite-case
theorem without invoking unconditional all-n first-coefficient positivity.

Reproduce the decisive certificate with `python3 evidence/certify_n5.py`.
It uses only the Python standard library. Its finite arithmetic assertions,
together with the analytic remainder and covariance arguments above, are
the proposed computer-assisted proof. A successful execution alone is not
a substitute for checking those arguments.

A second same-worker computation, `python3 evidence/crosscheck_n5_arb.py`,
uses python-flint at 192 bits and a different organization. Taylor bounds
prove P'>0 on [1,17/16] and P'''<0 on [31/16,2]. The exact endpoint zeros
then give P>0 on the corresponding open endpoint intervals. It also proves
P>0 on each of the 112 contiguous cells of length 1/128 covering
[17/16,31/16], with explicit Taylor remainder bounds. The file
n5-arb-crosscheck.json records all cell enclosures and the endpoint bounds.
Thus this is another complete interval check, not a floating-point sweep.

Additionally, seven held-out dyadic parameters, including
t=1+2^(-30) and t=2-2^(-30), were evaluated directly by ball Cramer
determinants. All four coefficient enclosures are positive, and the
penultimate determinant agrees with the exponential sum. Those seven
finite checks are only supplementary and are not used as domain coverage.
The cross-check is not a separate model context or independent referee.

Known mathematical gap list for the proposed finite statement: empty.
Fresh referee scrutiny of the proof, finite certificate, scope and value
is still required. The original all-dimensions assertion, priority beyond
the inspected literature, and behavior at the excluded predictor endpoints
are not resolved here. The standard exponential zero count, Bernstein
basis, Taylor estimates and predictor recursion are not claimed as new.
