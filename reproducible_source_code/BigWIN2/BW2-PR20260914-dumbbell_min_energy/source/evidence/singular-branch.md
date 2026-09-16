# Singular energy minima of all-odd unit-gain dumbbells

Research argument, 2026-09-14. Proposer job:
`primary-20260914-dumbbell-min-energy-research-4c017c9f21aa`.
This is a partial result submitted for fresh review. The original minimum and
all switching classes for every triple remain unresolved. No fresh referee
has accepted these arguments.

## Scope and notation

Use exactly the graph, gains, and normalized real parts in `problem.md`.
Throughout, r,s >= 3 and ell >= 1 are odd, N=r+s+ell-1, and

    L=(ell-1)/2, R0=s+L, S0=r+L, eps=(-1)^(N/2),
    H(alpha,beta)=R0 alpha+S0 beta.

Write P(x;alpha,beta) for the monic Hermitian characteristic polynomial.
The source's polynomials Z,W,X,Y are positive for t>0. With

    A=Z-alpha beta W, B=alpha X+beta Y, C=A^2+B^2,
    I_alpha = integral_0^infinity (-beta W A+X B)/(t^2 C) dt,
    I_beta  = integral_0^infinity (-alpha W A+Y B)/(t^2 C) dt,
    J=alpha I_alpha+beta I_beta,

the energy is E=(1/pi) integral log(C)/t^2 dt. This is Huang--Pereyra,
Lemma 4.2. The polynomial formula can also be obtained directly by determinant
permutations as recorded in `triage-math.md`.

## A. Explicit singular derivative and corrected stationarity

**Theorem A.** On the closed parameter square,

    P(0)=eps(1-4 alpha beta),
    P_x(0)=-2 eps H(alpha,beta).                         (A1)

Every zero eigenvalue is simple: its locus is alpha beta=1/4, where H is
nonzero. At any interior point q=(alpha,beta) of this locus, E has the
following uniform expansion as h=(h_alpha,h_beta) tends to zero:

    E(q+h)=E(q)+(2/pi)(I_alpha h_alpha+I_beta h_beta)
                 +2 |beta h_alpha+alpha h_beta|/|H(q)|
                 +O(||h||^2).                          (A2)

In particular the displayed integrals exist but are the derivatives of the
smooth contribution from the nonzero eigenvalues, not generally derivatives
of E. Necessary conditions for q to be a local energy minimum are

    alpha I_alpha=beta I_beta,
    |J| <= pi/(2|H(q)|).                                (A3)

They are equivalent to all first directional derivatives being nonnegative.
If the first equality holds and the second inequality is strict, q is a
strict local energy minimum. The equality case in the second condition is
not classified here. Away from alpha beta=1/4, the usual necessary interior
conditions I_alpha=I_beta=0 are valid.

**Proof of (A1).** The graph D has exactly one perfect matching. Its two odd
cycles force the edges at both ends of the connector into that matching;
the remaining even paths have unique perfect matchings. D-C_r has odd order
s+2L and exactly s+L matchings leaving one vertex uncovered. To count these,
write its tail as a path of 2L new vertices attached to C_s. For L=0 an odd
cycle has s such matchings. Deleting the free tail end in the matching
recurrence yields the sum of (i) the one perfect matching after that end is
left uncovered, and (ii) the near-perfect matchings after its incident edge
is included and the two end vertices are removed. Thus the count increases
by one each time L increases by one. In (i), the remaining tail has odd
order, its edge into the cycle is forced, and the residual paths have unique
perfect matchings. D-C_s similarly has r+L near-perfect matchings. The empty
tail for L=0 causes no exception. Hence

    [x]m_(D-C_r)=(-1)^((N-r-1)/2)(s+L),
    [x]m_(D-C_s)=(-1)^((N-s-1)/2)(r+L).

The matching polynomials of D and P_(ell-1) are even. Substitution into the
four-term characteristic formula, with the two normalization signs retained,
gives both identities in (A1). On the singular locus alpha and beta have the
same nonzero sign, so H cannot vanish. This proves simplicity, including at
the four singular boundary points.

**Proof of (A2).** Fix an interior singular q. The implicit function theorem
gives an analytic simple eigenvalue lambda near q, with lambda(q)=0, and

    d lambda(q)[h]=-2(beta h_alpha+alpha h_beta)/H(q).     (A4)

All other eigenvalues stay bounded away from zero in a sufficiently small
neighborhood. Their signed sums define a real analytic function F, even when
individual nonzero eigenvalues coincide: each sum is a contour integral of
x P_x/P around the positive or negative root group. Therefore E=F+|lambda|.
This statement can alternatively be obtained from spectral projections of
a smooth switching-normal-form Hermitian matrix; the interior condition
allows the gains a+i sqrt(1-a^2) and b+i sqrt(1-b^2) to be chosen smoothly.

To identify grad F without an invalid improper-integral differentiation,
factor P=(x-lambda)Q. Exactly,

    |t^N P(i/t)|^2=(1+t^2 lambda^2)|t^(N-1)Q(i/t)|^2.

The integral of log(1+t^2 lambda^2)/(pi t^2) is |lambda| (integration by
parts proves this also at lambda=0 by continuity). Thus F is the integral
for Q. Its parameter derivatives divided by t^2 are uniformly O(1) at zero
and O(t^-2) at infinity: Q is monic and real, and Q(0) stays nonzero.
On intermediate compact t intervals Q(i/t) stays nonzero by real-rootedness.
These facts justify differentiation for Q. At q the parameter derivative
of log(1+t^2 lambda^2) vanishes for every fixed t. Consequently

    grad F(q)=(2/pi)(I_alpha,I_beta).

Taylor expansion of F and lambda gives (A2), using the Lipschitz property
of the scalar absolute value. This also proves convergence of I_alpha and
I_beta at q. At a nonsingular point the same estimates apply to P itself,
so ordinary differentiation is valid there.

**Proof of necessity and sufficiency in (A3).** Set g=grad F(q) and
n=(beta,alpha). The directional derivatives in (A2) are nonnegative for
all h precisely when

    g=k n for some real k with |k| <= 2/|H(q)|.          (A5)

Indeed tangent directions with n.h=0 force g to be normal; the two normal
directions then give the stated scalar bound. Since alpha beta=1/4, (A5)
is exactly (A3).

For strict sufficiency use coordinates p=alpha beta and
u=(1/2)log(alpha/beta), with the fixed common sign. Near q,
alpha=sign(alpha(q)) sqrt(p)e^u and beta=sign(beta(q)) sqrt(p)e^-u.
The zero branch has the exact form

    lambda(p,u)=(p-1/4)a(p,u), a(q)=-2/H(q),
    E(p,u)=F(p,u)+|p-1/4|c(p,u), c=|a|>0.              (A6)

Here F_p(q)=4J/pi, c(q)=2/|H(q)|, and F_u(q)=0 is the first condition
in (A3). Theorem B below proves strict convexity of E on the fixed-product
curve. Thus u(q) is its unique minimum on p=1/4. If |F_p(q)|<c(q),
continuity gives a small neighborhood and epsilon>0 with
c(p,u)-|F_p(p',u)| >= epsilon for all p,p' in that neighborhood.
The mean value theorem applied in p yields

    E(p,u)-E(1/4,u) >= epsilon |p-1/4|.

Together with the strict constrained minimum this proves the strict local
minimum in two variables. A negative or positive common sign makes no
difference. This proof makes no assertion in the threshold equality case.

The tangential condition in (A3) is also exactly the source's equation (118),
since alpha I_alpha-beta I_beta equals
integral (alpha^2 X^2-beta^2 Y^2)/(t^2 C). Thus (118) survives at singular
minima. Equation (119) must instead satisfy the interval bound for J.

## B. Unique fixed-product minimum and a length-based boundary criterion

**Theorem B.** For each 0<p<1, E on the positive fixed-product curve
alpha beta=p is strictly convex in u=(1/2)log(alpha/beta), on the complete
closed interval (1/2)log p <= u <= -(1/2)log p. It therefore has exactly
one constrained minimizer. At p=1 the curve is a singleton. The negative
curve has the simultaneous-negation companion minimum. In particular there
is exactly one positive constrained minimum on the singular hyperbola.

If r=s, this point is (sqrt(p),sqrt(p)). If r<s and p<1, its coordinates
satisfy alpha<beta. More explicitly, for all t>0,

    X(t)/Y(t) > (s+L)/(r+L).                            (B1)

It follows that if p >= (r+L)/(s+L), the unique constrained minimum is
(alpha,beta)=(p,1). In particular, if

    s+L >= 4(r+L),                                    (B2)

the unique positive singular-curve minimum is (1/4,1); no interior singular
point is a local energy minimum. The conclusions with the cycles exchanged
follow by exchanging coordinates. A constrained minimum at an endpoint need
not be a local or global minimum on the full square.

**Proof of convexity.** At fixed p write

    d=(Z-pW)^2+2pXY>0,
    z=pX^2 e^(2u)>0, w=pY^2 e^(-2u)>0, C=d+z+w.

Direct differentiation gives

    (log C)_uu=4[d(z+w)+4zw]/(d+z+w)^2>0.              (B3)

Integration of the strict convexity inequality proves strict convexity of E,
without interchanging a derivative and an integral. Continuity and compactness
give existence, and strict convexity gives uniqueness. The first and second
u derivatives may also be integrated: at zero they are O(t^(2 min(r,s)))
before division by t^2, while at infinity they are uniformly bounded.
For r=s, symmetry in u gives the stated minimum. For r<s, (B1) implies
E_u(p,0)>0, so the unique constrained minimizer has u<0 for p<1.

**Proof of (B1).** Put eta=asinh(1/(2t))>0. The path recurrence and the
cycle matching polynomial give, for every odd k,

    g_k(t^2)=2t^k sinh(k eta),
    f_(k-1)(t^2)=t^(k-1) cosh(k eta)/cosh(eta).

Also f_(ell-2)(t^2)=t^(ell-2)sinh((ell-1)eta)/cosh(eta), which remains
correct for ell=1 since f_-1=0. Substituting in X=2t^r R(t^2) and
Y=2t^s S(t^2) gives

    X/Y = [sinh(s eta)+c_eta cosh(s eta)] /
          [sinh(r eta)+c_eta cosh(r eta)],
    c_eta=sinh((ell-1)eta)/(2 cosh(ell eta)cosh(eta)).   (B4)

The recurrence formulas follow directly from its two characteristic roots
t exp(eta) and -t exp(-eta); they introduce no approximation.
One has 0<=c_eta<=L eta: tanh((ell-1)eta)<=(ell-1)eta and
cosh(ell eta)cosh(eta)>=cosh((ell-1)eta) prove this bound.
For any c>=0, the function

    z -> (sinh z+c cosh z)/(z+c)

is strictly increasing for z>0, since its derivative numerator is
z cosh z-sinh z+cz sinh z+c^2 sinh z>0. Consequently, for s>r,

    X/Y > (s+c_eta/eta)/(r+c_eta/eta)
        >= (s+L)/(r+L),

proving (B1). Since

    (log C)_u=2(alpha^2 X^2-beta^2 Y^2)/C,

if p>=(r+L)/(s+L), then at u=(1/2)log p, alpha=p and beta=1,
and pX>Y for every t. The energy derivative is already positive at this
left endpoint and increases strictly with u. This proves the boundary
criterion, including equality in (B2).

## C. Exact D_(3,3,1) test and the source correction

For this graph alpha=a and beta=b, and

    P=x^6-7x^4+11x^2-1-2(alpha+beta)(x^3-3x)+4alpha beta.

The complete closed-square global proof is given in `triage-math.md`,
Section 3, and was rechecked directly in this pass. Its essential details
are included here so the correction does not depend on a numerical minimum.
With Z=1+7t^2+11t^4+t^6, X=Y=2t^3(1+3t^2), W=4t^6, one has
ZW-X^2=4t^8(1+t^2)^2>0. Expansion of C-Z^2 excludes all nonzero points
with alpha beta<=0. At a positive product,

    C(alpha,beta)-C(sqrt(alpha beta),sqrt(alpha beta))
      =X^2(alpha-beta)^2.

After simultaneous negation, every remaining minimizer must be (c,c),
0<=c<=1. There

    P=(x^3-x^2-3x+1-2c)(x^3+x^2-3x-1-2c).

Both cubics are real-rooted as factors of the Hermitian characteristic
polynomial. For c<1/2 the first has one negative root -U, the second one
positive root v, and E=2+2(U+v). Indeed the first cubic has negative root
product and positive trace, forcing exactly one negative root; the second
has positive root product and negative trace, forcing two negative roots.
For h(z)=z^3+z^2-3z, U,v>1, h(U)=1-2c, h(v)=1+2c, and h' strictly
increases on z>=1. Thus E'=4(1/h'(v)-1/h'(U))<0 for 0<c<1/2.
For c>1/2 each cubic has one positive root, respectively w>2 and v>1:
the first has positive root product and negative pairwise-root sum, and the
second has positive root product and negative trace. Hence E=2(w+v) and
E'=4/(3w^2-2w-3)+4/(3v^2+2v-3)>0. Continuity covers c=1/2 and c=0.
Therefore the global minimizers are exactly (+1/2,+1/2), (-1/2,-1/2),
with the eight oriented cycle-product switching lifts in `problem.md`.
Their common value 2+sqrt(13)+sqrt(5) is already source Proposition 4.9.

At q=(1/2,1/2), H=3 and

    P=x(x+2)(x^2-x-3)(x^2-x-1).

Define the exact smooth diagonal derivative

    G=-2/5-2 sqrt(13)/39+2 sqrt(5)/5,  0<G<2/3.

Differentiating the preceding cubic extreme-root formulas gives the left
and right diagonal energy derivatives G-2/3 and G+2/3. Their jump is 4/3,
exactly as (A2) predicts. Symmetry gives F_alpha=F_beta=G/2, so
I_alpha=I_beta=pi G/4. The condition (A3) holds strictly, and Theorem A
therefore certifies a strict local minimum independently of the global
monotonicity argument. The irrational inequality above follows, for example,
from 11/5<sqrt(5)<9/4 and 18/5<sqrt(13)<37/10.

At q, each integrand numerator in source (117) is exactly

    -W(Z-W/4)/2+X^2=2t^6(1+5t^2+7t^4)>0.

After division by t^2 C this is O(t^4) at zero and O(t^-2) at infinity.
Thus each integral is positive, contradicting its asserted zero value at
this proven interior global minimizer. The source already recognizes the
zero-root cusp near Figure 2; that observation and the energy value are
not claimed as new. The proposed correction is the uniform explicit
replacement (A1)--(A6), with the branch structure and length criterion in B.

**A contrasting exact test: D_(3,3,5).** At the same half-diagonal point,
H=5 and the simple zero has diagonal derivative -2/5. Nevertheless this
point is not a local energy minimum. Here the half-diagonal polynomial and
its derivative with respect to the diagonal parameter c are

    Q=x(x+2)(x^4-x^3-5x^2+3x+5)(x^4-x^3-3x^2+x+1),
    P_c=-4(x^7-7x^5-x^4+13x^3+3x^2-5x-1).

All ten roots of Q are simple. For its nine nonzero roots define

    G335 = sum_(Q(z)=0,z!=0) -sign(z) P_c(z)/Q'(z).

The exact certificate in `research-checks.json` isolates every root of Q
in a rational interval (the roots -2 and 0 are exact singletons). Their
multiplicities sum to degree ten; gcd(Q,Q')=1 and interval root counts
verify completeness and simplicity. Rational interval Horner evaluation of
P_c and Q' encloses each summand, with every denominator interval excluding
zero. Adding these intervals proves

    407/1000 < G335 < 408/1000.

The formula is the implicit derivative for each simple root, so G335 is the
smooth diagonal derivative F_c. By (A2), the directional energy derivative
along (-1,-1) is -G335+2/5, strictly between -8/1000 and -7/1000. This is
an exact descent certificate, and illustrates why the normal inequality is
substantive even when the fixed-product minimum and a cusp are present.
The source's numerical D335 improvement at c approximately 0.197754 was
already known; that observation was not used as proof of this local sign.

## Dependencies, verification, and limits

Decisive primary text: Huang and Pereyra, arXiv:2604.27785v2, especially
Lemma 4.2, Theorem 4.7, Proposition 4.9, and the Figure 2 discussion.
The original supplied PDF and its text extraction are copied unchanged into
`evidence/external/` for the candidate. Live theorem-scope and literature
checks are recorded in `literature/research-screen.md`.

`research_checks.py` separately counts matchings, checks the two coefficients
for 125 triples, verifies three algebraic Hermitian characteristic polynomials
on the singular locus, and checks the D331 cusp and five kernel-ratio cases
exactly. It also supplies the complete D335 root-isolation and rational
interval descent certificate. Results: `research-checks.json`. These are finite implementation
checks. The all-length assertions depend on the arguments above.
`research_diagnostics.py` and `research-diagnostics.json` provide explicitly
floating, held-out directional checks; they are not certificates.

Known mathematical gap list for the stated partial theorems: none identified
by the proposer. Independent correctness and significance review is pending.
Unclaimed questions: the equality case of (A3), sufficiency at singular
boundary endpoints, which triples have a singular global minimum, and the
complete original all-odd minimum/equality classification. No claim of
worldwide priority is made. No theorem here is inferred from a timeout,
finite census, numerical fit, or successful verifier status.
