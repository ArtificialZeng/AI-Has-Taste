# An explicit quotient for the Class 214 generating function

Proposer job: primary-20260913-inversion214-research-aabee08e3bf3.
Status: proposed result-note theorem, awaiting a fresh referee. This is a
formal generating-function result. The original non-algebraicity conjecture
remains unresolved. No analytic continuation or asymptotic assertion is made.

## Exact statement

Let a_n count the inversion sequences specified in source.md and problem.md,
including a_0=1, and let F(z)=sum_{n>=0} a_n z^n. All limits below are
coefficientwise formal limits for the z-adic topology. Define

    X=(1-2z-sqrt(1-4z))/(2z),  sqrt(1-4z)=1+O(z),
    q=X^2/(1+2X),
    T(u)=zu/(1-zu),
    H(u)=z(1+u)^2-u,
    R0(u)=-zu^2(1-z-zu)/(1-zu),
    R1(u)=u^2(1-z-zu)^2/(1-zu),
    b=X^3/((1+X)(1+2X)).

For every integer j>=0 put

    t_j = z^j q / (1-q sum_{r=1}^j z^r),
    D_j = product_{i=0}^j H(t_i),

where an empty sum is zero. Define the explicit sums

    A = sum_{j>=0} R0(t_j)/D_j,
    L = q + sum_{j>=0} R1(t_j)/D_j.

Then

    F(z) = (b-A)/(z L).                                      (Q)

The summands of A and L-q have exact orders j+4 and j+3 respectively,
and all belong to Z[[z]]. Moreover, L=z^2+O(z^3) and b-A=z^3+O(z^4),
so the displayed quotient is well-defined in Z[[z]]. Its constant term is 1.
There is no unknown counting or boundary series on the right side of (Q).

For m>=0 let A_m and L_m be the same expressions with j=0,...,m-1,
and put F_m=(b-A_m)/(z L_m). Each F_m is an explicit element of Q(z,X)
and, expanded at z=0, an element of Z[[z]]. The following sharper contact
statement also holds for EVERY integer m>=0:

    F_m-F = z^(m+3) + O(z^(m+4)).                            (C)

In particular F_m gives all coefficients of F through degree m+2, and
already m=max(0,N-2) terms suffice to determine F through degree N.
These assertions do not say F is algebraic: coefficientwise limits of
elements of Q(z,X) need not lie in that field.

## Prior dependency, kept distinct from the contribution

The published input is Britt and Beaton, *Completing the enumeration of
inversion sequences avoiding triples of relations*, arXiv:2512.21943v2,
Section 3.5, printed p.18, equations (3.31)-(3.33). The complete primary
PDF and its extracted text are retained at
evidence/external/britt-beaton-2512.21943v2.pdf and the corresponding .txt.
The PDF matches the frozen source's SHA256. The relevant primary statement
is also at https://arxiv.org/html/2512.21943v2#S3.SS5.

Specifically, the auxiliary class B permits the zero exceptions described
in problem.md. Its generating function B(z,x,y) marks length and the first
and second zero-run lengths p,s. Let V(x)=B(z,x,0). The published rule is

    root (0,0);
    (p,s) -> (p+1,s);
    (p,s) -> (p+1,s-1),                    s>0;
    (p,0) -> (p-ell,ell),                  0<=ell<=p-1;
    (p,0) -> (p-ell-1,ell),                0<=ell<=p-2.

The source identifies the desired objects as precisely the states (p,0)
with p<=2, hence F=[x^0]V+[x^1]V+[x^2]V. These facts are inherited,
not proposed as new theorems. The new contribution is solving the boundary
value explicitly by a convergent regularized iteration, including (C).

## Derivation of the boundary equation

Work initially in Q[x,y][[z]]. All coefficients of B are polynomials:
at length n both labels are at most n. In particular V is in Z[x][[z]],
[x^0]V=1, and its coefficient of z is x.

Multiplying published equation (3.33) by y-x gives

    0=(y+z)(y-x) - (y-zx-zxy)(y-x)B(x,y)
      +xz(1+y)V(y) - z(y+2xy-x^2)V(x).

Substitute y=T(x)=zx/(1-zx). This is legitimate in Q[x][[z]]: 1-zx
is a unit, T is divisible by z, and the substituted coefficients have
finite degree before substitution. The B term vanishes. The identities

    (T+2xT-x^2)/(x(1+T)) = H(x),
    -(T+z)(T-x)/(xz(1+T))
        = S(x):=(1+x-zx)(1-z-zx)/(1-zx)

are identities of rational functions whose simplified right sides belong
to Q[x][[z]]. Cancelling the nonzero common factor xz(1+T) in this
integral domain proves

    H(x)V(x) = V(T(x))-S(x).                               (K)

No substitution into a denominator that vanishes at a kernel root has
been made. The symbolic identities can also be checked by the retained
triage reproducer; the displayed algebra supplies the infinite argument.

Write c=[x]V and d=[x^2]V. Since

    S(x)=1-z+(1-2z)x-sum_{k>=2}(zx)^k,

the coefficient of x^2 in (K) is

    z d+(2z-1)c+z = z^2(c+d+1).

After dividing the unit 1-z, this is z d=(1-z)c-z. Therefore

    F=1+c+d=c/z.                                         (E)

Here c=z+O(z^2), so the division by z is an ordinary formal series.

## Kernel boundary and regularized tail

The series X is the unique root of H(X)=0 with X=z+O(z^2);
it satisfies X=z(1+X)^2. Substitution x=X into (K) is legitimate in
Q[[z]] and is done BEFORE dividing by H(x). It gives

    V(T(X))=S(X),
    T(X)=X^2/(1+2X)=q,
    S(X)=1+X^3/((1+X)(1+2X))=1+b.                         (B)

The last two identities follow by replacing z with X/(1+X)^2.

Set W(x)=V(x)-1-cx. Then W is in z^2 x^2 Z[x][[z]], because labels
p cannot exceed length and at length 1 the only state is (1,0).
At length 2 the rule has exactly one state (2,0), so

    [z^2 x^2]W = 1.

More explicitly W=z^2 x^2+x^2 O(z^3); coefficients of z^2 have no
higher powers of x. Subtracting the constant and linear parts of (K)
gives the exact identity

    H(x)W(x)=W(T(x))+R0(x)+cR1(x).                        (R)

Indeed R0=1-S-H and R1=T-Hx, with the rational forms in the statement.

Direct induction gives t_j=T^j(q) with the stated nonrecursive formula.
Since q=z^2+O(z^3), t_j=z^(j+2)(1+O(z)) for every j>=0. Consequently

    H(t_j)=z(1+O(z)),
    D_j=z^(j+1)(1+O(z)),
    R0(t_j)=-z^(2j+5)(1+O(z)),
    R1(t_j)= z^(2j+4)(1+O(z)).

All leading units have integer coefficients and constant term 1; their
inverses do too. This proves the stated orders and integrality of the
summands without an analytic convergence assumption.

Let D_{-1}=1. Iterating (R) at t_0,...,t_{m-1} for any m>=0 gives

    W(q) = sum_{j=0}^{m-1} (R0(t_j)+cR1(t_j))/D_j
           + W(t_m)/D_{m-1}.                             (I_m)

The tail has EXACT order m+6 and leading coefficient 1, since

    W(t_m)=z^(2m+6)(1+O(z)),
    D_{m-1}=z^m(1+O(z)).

This also covers m=0, when the product is empty. In particular the tail
tends to zero. Taking the z-adic limit of (I_m) and using (B) yields

    b=cq+W(q)=A+cL,

which together with (E) proves (Q). The bounds on A,L,b also prove that
the normalized numerator and denominator after removing z^3 are integral
units. Thus the formula defines a single series with no unresolved
boundary choice.

For finite m, (I_m) instead gives

    b=A_m+c L_m+W(t_m)/D_{m-1}.

Hence

    F_m-F = W(t_m)/(D_{m-1} z L_m).

Because z L_m=z^3(1+O(z)), the preceding exact tail order proves (C),
including its leading coefficient and both m=0 and m=1 boundary cases.

## Uniqueness in the natural formal ring

Equation (K) has at most one solution V in Q[x][[z]], independently of
any finite coefficient checks. For the difference U of two solutions,
H(x)U(x)=U(T(x)). Setting x=0 gives (z-1)U(0)=0, hence U(0)=0.
If U is nonzero, let k be its smallest nonzero z-degree, with coefficient
u_k(x). Every coefficient of U is divisible by x. Thus U(T(x)) has
z-order at least k+1, whereas H(x)U(x) has z^k coefficient -x u_k(x),
which is nonzero in Q[x]. This is impossible. The combinatorial V is an
existing solution by the prior rule, and (Q) has just evaluated its c/z.
No claim that arbitrary rational functions in x can be substituted into
this uniqueness argument is needed.

## Reproducible attacks and limits

Run `python3 evidence/quotient-check.py` from the project directory.
It implements (Q) by truncated integer series operations, without using
coefficients of V or F as inputs, and compares with two other methods:
the published left-growth rule and a right-append dynamic program from
the original forbidden triple. The latter keeps the largest and second
largest previous entries, WITH multiplicity and padded by -1. Appending v
is allowed precisely when v exceeds the second largest entry and v<n.
Every new forbidden triple ends at v, so this DP covers all and only the
original sequences by induction on their length. A literal triple-loop
enumerator separately calibrates that implementation through length 9.

The three methods agree through degree 40. Degrees 17-20 are held out
relative to the fixed triage formula; the formula was not changed after
observing them. All computations here are from one worker and do not
constitute the required fresh mathematical review. The code also checks
the orders of all 40 summands, stability under adding two summands, and
the exact first-error degree and coefficient in (C) for m=0,...,20.

Known mathematical gaps for the precise formal theorem above: none
identified by the proposer. Fresh scrutiny is still required. Inherited
combinatorial input: the published rule and extraction statement on p.18.
The original non-algebraicity question, analytic singularities, and the
numerical asymptotic constant in the source are outside this theorem.
In particular an infinite sum of algebraic terms is not a transcendence
proof, and individual denominator zeros may cancel in the quotient.
Literature coverage and the limited novelty claim are recorded separately
in literature/research-live-screen.md.
