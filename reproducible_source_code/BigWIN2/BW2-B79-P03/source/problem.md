# Precise triage reading

## Frozen source and scope

The immutable statement is `source.md` (SHA-256
`8a681d075043033b8feb7527ed43fc357d34c2e93c1009b02f8a1d1ffae24b14`).
This file formalizes that statement; it does not replace or weaken it.  The
claim concerns only the explicit family below and the sample constructor in
Dean--Goldsmith Lemma 7.  It does not concern general MIMO decoding, the full
iterative lattice reduction, or the separate Lemma 6 method for initially
generating discrete-Gaussian samples.

Throughout, `log` is read as the natural logarithm.  Changing to any fixed
base greater than one changes only the finite cutoff, not this asymptotic
claim.  “Choose an integer M” is read in the stronger, standard arbitrary
sense: the conclusions must hold for every integer satisfying the displayed
lower bound (allowing `M=M(n)`).

## Definitions

For `r>0`, let

`D_(Z^n,r)(a) = exp(-pi*||a||_2^2/r^2) / rho_r(Z^n)` for `a in Z^n`.

Thus its coordinates are independent copies of the centered symmetric
one-dimensional discrete Gaussian.  Write
`nu_beta = N(0,beta^2/(2*pi))`.  A function is negligible if it is eventually
smaller than `n^(-C)` for every constant `C>0`; an event occurs with
overwhelming probability if its complement is negligible.

For each sufficiently large integer `n`, put

* `epsilon=2^(-n)`, `L=Z^n`, `A=I_n`;
* `r=k=n^2`, `alpha=1/2`, and `m=3n^5`;
* `M` an arbitrary integer with
  `M > m*2^(n log(log n)/log n)`;
* `c=2M*1_n`, `delta=e_1/4`, and `y=c+delta`.

The dual lattice is again `Z^n`.  One Lemma 7 sample is obtained independently
by drawing `v~D_(Z^n,r)` and `e~nu_alpha`, and returning

`a=(k/r)v=v`,

`b=k<v,A^(-1)y>/(rM)+(k/r)e
   =2 sum_(j=1)^n a_j + a_1/(4M)+e`.

Call this joint law `P_(n,M)`.  For a legal discrete-MIMO comparison, fix an
arbitrary secret
`s in Omega_M^n`, where `Omega_M=[0,M) intersect Z`, and an arbitrary
`beta in (0,alpha]`.  Its law `Q_(n,M,s,beta)` draws the same
`a~D_(Z^n,n^2)`, independently draws `e_beta~nu_beta`, and returns

`b=<a,s>/M+e_beta`.

“Distinguished from every legal distribution” means that there must exist one
polynomial sample bound `N(n)`, one polynomial-time test independent of `s`
and `beta`, and one negligible `mu(n)` such that, for every admissible `M`,

`Pr_(P^(N))[test says legal] <= mu(n)`

and, uniformly for every fixed (possibly `n`-dependent) legal pair `(s,beta)`,

`Pr_(Q^(N))[test says constructed] <= mu(n)`.

This is a composite-hypothesis guarantee, not a claim about adversarially
altered samples or arbitrary mixtures over secrets.  Arithmetic running time
is measured in the supplied input representation; the proposed statistic uses
`O(Nn)` arithmetic operations.

## Exact target

The frozen assertion asks for both of the following.

1. **Promise audit.**  Prove that the displayed `(L,A,r,k,alpha,m,M,y)` is a
   valid BDD input for every promise actually invoked by the Lemma 7 sample
   construction, including smoothing, the constellation bound, effective
   noise, the distance bound, and uniqueness.
2. **Uniform separation.**  For independent samples put
   `X_i=sum_j a_(i,j)` and, when the denominator is nonzero,
   `theta_hat=(sum_i X_i b_i)/(sum_i X_i^2)`.  Prove that the threshold test
   `theta_hat>3/2` (with a specified convention on a zero denominator) meets
   the preceding uniform overwhelming-probability definition for a polynomial
   `N(n)`.

## Triage checks already verified

These are exact algebraic checks, not yet the requested tail proof.

* `lambda_1(Z^n)=1`, the least eigenvalue of `A^T A` is `sigma=1`, and
  `dist(y,Z^n)=||delta||_2=1/4`.  The closest vector is uniquely `c`.
  Taking, for example, BDD radius `d_0=3/8` gives
  `1/4<d_0<lambda_1/2`.
* Dean--Goldsmith Claim 2 gives
  `eta_(2^-n)(Z^n)<=sqrt(n)`.  Hence `r=n^2>sqrt(2)*eta_epsilon(Z^n)` for
  every `n>=2`.
* The main parameter inequality also holds:
  `m*alpha/k^2=(3/2)n>sqrt(n)`.  The Lemma 7 effective independent noise is
  `(k/r)e=e`, so its scale is `k*alpha/r=alpha` and is legal.
* The constellation inequality holds by the definition of `M`.  The Lemma 7
  distance ceiling is
  `M*sigma*alpha/(k^2*r*sqrt(2))=M/(2sqrt(2)n^6)`.
  Since `2^(n log(log n)/log n)` dominates every fixed power of `n`, the
  lower bound on `M` makes this ceiling tend to infinity; consequently it
  exceeds `d_0=3/8` for all sufficiently large `n`.
* If `X=sum_j a_j` and `V=E[a_1^2]>0`, coordinate independence and symmetry
  give `E[X^2]=nV` and `E[Xa_1]=V`.  Therefore the two population slopes are

  `E_P[Xb]/E[X^2]=2+1/(4Mn)>2`,

  `E_Q[Xb]/E[X^2]=(1/(Mn))*sum_j s_j <=(M-1)/M<1`.

  Thus the proposed threshold has a uniform population gap of at least
  `1/2`.  This does not by itself justify division by the random empirical
  denominator or overwhelming probability.

## Primary-literature triage (retrieved 2026-09-10)

* T. Dean and A. Goldsmith, *Physical-Layer Cryptography Through Massive
  MIMO*, arXiv:1310.1861, <https://arxiv.org/abs/1310.1861>.  Inspected the
  official PDF, Appendix A.B (discrete-MIMO definition, Eq. (14), and
  smoothing Claims 2--3) and Appendix A.C (Lemma 7 and Eq. (19)).  These give
  the promises and constructor normalized above.
* Y. Li, *Has MIMO decoding been proved hard from lattice problems?*,
  arXiv:2609.05013v1, <https://arxiv.org/html/2609.05013v1>.  Inspected
  Definition 2.9, Section 5 Lemma 7, Proposition 5.1, and Remark 5.3.
  Proposition 5.1 proves exact non-membership in the legal family when the BDD
  coefficient is outside the constellation or the offset is nonzero.  Remark
  5.3 explicitly leaves statistical detectability instance-dependent and notes
  that a large `M` does not suppress the coefficient-reduction term.
* Targeted searches for the exact assertion and for covariance/moment
  distinguishers for the Dean--Goldsmith BDD discrete-MIMO constructor found
  no primary source beyond Li's paper that states this explicit result.  This
  limited search is not evidence of priority.

Source status is **new-question**: the exact explicit-family separator is not
presented as an open problem or theorem in the inspected sources.  Suitability
is **advance**.  Nearest prior result: Li Proposition 5.1 (exact
non-membership).  Proposed delta: a uniform constant-gap, polynomial-sample
separator for the frozen admissible family.  Verification route: prove a
uniform empirical-covariance and Gaussian-noise concentration bound for the
displayed statistic, including the denominator-zero event.

## Remaining gap

The former finite-sample gap is closed in
`evidence/finite_sample_separator.md`.  With `N=n^8`, the threshold test uses
the convention that a zero denominator is classified as legal and has, under
either hypothesis, error probability at most

`2 n^9 exp(-pi n^2)
 + 2 n^2 exp(-exp(-2pi)n^2/1280000)
 + 2 exp(-49 pi exp(-pi)n^13/1600)`.

The bound is negligible and is uniform in every admissible `M`, every fixed
legal `s`, and every `0<beta<=1/2`.  The proof establishes an explicit
operator-norm event for the empirical covariance, proves the denominator is
positive on that event, bounds all legal noiseless slopes by `51/49`, bounds
the constructed noiseless slope below by `7/4`, and then conditions on the
public samples to control the Gaussian response noise.  Together with the
promise audit above, this resolves the frozen assertion positively.  The
mathematical argument has not yet received the required fresh referee audit.
