# A two-step bound for the hypercomb summands

Proposed partial theorem for fresh mathematical review; no independent acceptance
is claimed. Job: primary-20260914-hypercomb-unimodality-research-c86b16750561.
The frozen full-unimodality problem in `source.md` remains unresolved here.

## Statement and scope

Fix integers ell >= 3 and n >= 2. Put s=ell-2, t=ell-1=s+1, and

    a=(1+s*x)(1+t*x), b=x(1+t*x),
    z0=1+(t+1)*x,
    z1=(1+t*x)(a+2*x)
      =1+(3*ell-2)*x+3*t^2*x^2+s*t^2*x^3.

Let F0=0, F1=1, and Fj=a*F_(j-1)+b*F_(j-2) for j>=2. Define

    Wn=z1*Fn, Yn=z0*b*F_(n-1).

These are exactly the summands in Galvin--Sharpe, Section 2.5, equations
(28)--(30), and Cn=Wn+Yn is the frozen hypercomb polynomial.

For a nonzero polynomial P with nonnegative coefficients, let m(P) be its
**smallest** coefficient-maximizing index. The proposed theorem is

    m(Yn)-1 <= m(Wn) <= m(Yn)+2.                         (T)

In fact, the proof gives the two likelihood-ratio inequalities

    Wn <=_lr x^2*Yn,       Yn <=_lr x*Wn.              (S)

The order is defined below with zero extension, so the leading zero of Yn
and the unequal degrees are part of the statement.

Consequently, with r=min(m(Wn),m(Yn)) and q=max(m(Wn),m(Yn)),

    q-r <= 2,
    c_(n,ell,0) <= ... <= c_(n,ell,r),
    c_(n,ell,q) >= ... >= c_(n,ell,2n+1).

This replaces the prior possible O(sqrt(n)) interval by an interval of at
most **two index steps**, for every length and uniformity. The value two
is sharp for the separation of these particular summands. It is not a
claim that a two-step nonunimodal interval ever occurs for Cn itself.

## Elementary order facts, including zero coefficients

All sequences below are nonnegative, nonzero, finitely supported on an
integer interval, and extended by zero to all integers. Write P <=_lr Q if

    p_i*q_j - p_j*q_i >= 0  for every pair i<j.         (1)

No division by a zero coefficient is used. This is the usual likelihood-ratio
order, without probability normalization. The following facts suffice.

1. The order is transitive for the stated interval supports. Indeed (1)
forces both support endpoints of P to be no larger than the corresponding
endpoints of Q. If P <=_lr Q <=_lr R and p_j*r_i>0 for i<j, these endpoint
conditions put i,j inside the support of Q. Multiply
p_i*q_j>=p_j*q_i and q_i*r_j>=q_j*r_i, then divide by q_i*q_j>0.
If p_j*r_i=0, the desired inequality already holds.

2. The inequalities are linear in either polynomial separately. Thus
P <=_lr Q and P <=_lr R imply P <=_lr Q+R; and the analogous assertion
with a common upper bound holds. The sums used below have interval support.

3. If R is log-concave with interval support, then multiplication by R
preserves the order. Here is a proof. Log-concavity and zero extension give

    r_(i-u)*r_(j-v) - r_(j-u)*r_(i-v) >= 0
        whenever i<j and u<v.                         (2)

For positive coefficients this follows by multiplying the decreasing
successive coefficient ratios; if a factor is zero, interval support gives
the same inequality. Expanding and grouping terms with u<v gives

    (PR)_i*(QR)_j - (PR)_j*(QR)_i
      = sum_(u<v) (p_u*q_v-p_v*q_u)
          * (r_(i-u)*r_(j-v)-r_(j-u)*r_(i-v)).         (3)

The sum is finite, and each summand is nonnegative. This also proves the
usual closure of log-concavity under multiplication: a log-concave P has
P <=_lr x*P by the same ratio argument; (3) gives
PR <=_lr x*PR, whose adjacent minors are the log-concavity inequalities
for PR. Multiplication preserves interval support.

4. If P <=_lr Q, then m(P)<=m(Q). Otherwise put i=m(Q)<j=m(P).
Minimality of m(P) gives p_i<p_j, whereas q_i>=q_j and q_i>0.
Then p_i*q_j<p_j*q_i, contradicting (1). This deals with tied modes
without choosing a favorable one after seeing the inequalities.

The elementary order machinery is standard; the proposed contribution is
its recurrence invariant and the application to the hypercomb summands.

## Log-concavity of the factors

The polynomials a,b,z0 are products of linear polynomials and monomials,
and are log-concave with interval support. The polynomial
d=a+2*x=1+(s+t+2)*x+s*t*x^2 is log-concave because
(s+t+2)^2>s*t. Thus z1=(1+t*x)*d is log-concave too.

For y in [0,1], write

    a^2+4*y*b = (1+t*x)*R_y,
    R_y = 1+(2*s+t+4*y)*x+(s^2+2*s*t)*x^2+s^2*t*x^3.

The two interior log-concavity determinants of R_y are

    (2*s+t+4*y)^2-(s^2+2*s*t)
      = 3*s^2+2*s*t+t^2+16*s*y+8*t*y+16*y^2 > 0,

    (s^2+2*s*t)^2-(2*s+t+4*y)*s^2*t
      = s^2*(s^2+2*s*t+3*t^2-4*t*y)
      >= s^2*(6*s^2+4*s-1) > 0.                      (4)

For the last line use y<=1, t=s+1, and s>=1. Hence a^2+4*y*b
is log-concave. This supplies a direct algebraic verification of the
factor condition used by Galvin--Sharpe; no numerical minimization is needed.

The standard Fibonacci-polynomial factorization is

    Fn = a^(epsilon_n)
         * product_(j=1)^floor((n-1)/2)
             (a^2+4*b*cos^2(j*pi/n)),                 (5)

where epsilon_n=1 for even n and 0 for odd n; an empty product is 1.
This is a polynomial identity, including n=1 and n=2. For completeness,
the recurrence solution is Fn=(lambda^n-mu^n)/(lambda-mu), with
lambda+mu=a and lambda*mu=-b. Pairing the conjugate factors of
(lambda^n-mu^n)/(lambda-mu) gives (5), with the unpaired factor
lambda+mu when n is even. It is also the factorization underlying the
primary source's equations (29)--(30).

Every cosine square lies in [0,1], so (4), (5), and product closure prove
that Fn is log-concave for every n>=1. The recurrence, with a strictly
positive on degrees 0,1,2, shows that Fn has positive coefficients at
every degree 0,...,2n-2. Consequently Wn and Yn are log-concave with
positive supports [0,2n+1] and [1,2n-1], respectively.

## The recurrence invariant

We prove simultaneously, for every j>=2,

    F_(j-1) <=_lr Fj <=_lr b*F_(j-1).                (6)

The base is F1=1 <=_lr F2=a <=_lr b. The three potentially nontrivial
minors for a <=_lr b, at pairs (0,1),(0,2),(1,2), are respectively
1,t,t^2, all positive.

Assume (6). Since 1 <=_lr a and Fj is log-concave, multiplication by Fj
gives Fj <=_lr a*Fj. The right-hand inequality in (6) gives
Fj <=_lr b*F_(j-1). Adding these two upper polynomials proves

    Fj <=_lr a*Fj+b*F_(j-1) = F_(j+1).

For the other half, a <=_lr b and log-concavity of Fj give
a*Fj <=_lr b*Fj. The left-hand inequality in (6) and log-concavity of b
give b*F_(j-1) <=_lr b*Fj. Adding the lower polynomials proves

    F_(j+1) <=_lr b*Fj.

This completes the induction. In particular, no mode estimates or
asymptotic approximation enter (6).

## Applying the invariant to the initial factors

First, z1 <=_lr x^2*z0. For the only pair having both right-hand
coefficients positive, (i,j)=(2,3), the minor is

    3*t^2*(t+1)-s*t^2 = t^2*(3*(t+1)-s)>0.

All other pairs are nonnegative immediately from their supports. Applying
the right half of (6), then this initial-factor comparison, gives

    Wn=z1*Fn <=_lr z1*b*F_(n-1)
             <=_lr x^2*z0*b*F_(n-1)=x^2*Yn.          (7)

The convolution kernels in these two steps are z1 and b*F_(n-1),
respectively; both have already been proved log-concave.

For the other direction, z0 <=_lr d=a+2*x: the minors at (0,1),(0,2),
(1,2) are s+1, s*t, (t+1)*s*t. Multiply by the log-concave kernel
x*(1+t*x) to obtain z0*b <=_lr x*z1. The left half of (6) now gives

    Yn=z0*b*F_(n-1) <=_lr z0*b*Fn
                    <=_lr x*z1*Fn=x*Wn.             (8)

The kernels are z0*b and Fn. Transitivity proves (S). Applying the
smallest-mode order property to (7) and (8), and noting
m(x^h*P)=h+m(P), proves (T).

The coefficient sequence of a sum of two unimodal polynomials is
nondecreasing up to the smaller chosen mode and nonincreasing from the
larger. This proves the claimed two-step localization. For n=1 the
initial polynomial z1 is already log-concave.

## Sharpness, limitations, and review target

At n=3, ell=5, exact coefficient arrays from degree zero are

    W=[1,28,320,1937,6744,13632,14976,6912],
    Y=[0,1,16,95,248,240],
    C=[1,29,336,2032,6992,13872,14976,6912].

The unique summand modes are 6 and 4, so no universal separation bound
of one holds for these summands. The total C is log-concave in this
example, so this is not a counterexample to the original problem or a
sharpness example for nonunimodality of C.

If the two smallest modes are separated by two, the only possible
failure of full unimodality is a strict valley at their intermediate
index. This proof does not rule out that valley in general. Neither
all-parameter log-concavity nor full unimodality of C is asserted.

Known proof gaps in the **stated partial theorem**: none identified by
the proposer. This is not a fresh-context audit. The referee should
especially check (3) with zero extension, the simultaneous induction
(6), and that the stated consequence concerns index-step length, not a
completed solution of the frozen full-unimodality question.

The live September preprint on eventual strict log-concavity asserts a
fixed-weight, sufficiently-large-length result. It is acknowledged in
the literature report, and is not used as a proof dependency here.
