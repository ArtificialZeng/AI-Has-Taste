# A rank-one commutator proof of the truncated-grid identity

Proposer job: primary-20260914-grid-narayana-research-12ef05d8a66f.
This is a complete proof candidate, submitted for a fresh mathematical referee.
No independent acceptance is asserted. The original statement is `source.md`;
its exact interpretation is `problem.md`. Known mathematical gaps: none.

## Statement

For every integer n>=1, with Q_n and H_n exactly as in source.md,

    H_n(t) = A_(n-1)(t) B_n(t).

All calculations below are formal polynomial or power-series calculations.
There are no analytic convergence, positivity, generic-parameter, or
large-n assumptions. Intermediate divisions by t can be performed over
Q(t); the final identities hold in Z[t], including t=0.

## 1. Exact transfer and a change of polynomial basis

Write a_i=x_(i,1), b_j=x_(j,2). Every ideal is precisely a pair of prefixes
of lengths (i,j), with 0<=i<=n and 0<=j<=min(i,n-1). Thus its constraint is

    U_i+V_j >= 0,
    U_i=i-sum_(k<=i)a_k,  V_j=j-sum_(k<=j)b_k.

Set U_0=V_0=0. After m complete columns put

    M_m=min(V_0,...,V_m), z=U_m+M_m, s=V_m-M_m.

Both z and s are nonnegative. If a,b are the next two coordinates, all
new ideal inequalities are equivalent to

    0<=a<=z+1,  0<=b<=z+s+2-a.

Indeed the inequalities with old upper prefix j<=m give the first bound;
the new upper prefix j=m+1 gives the second. With
delta=max(0,b-s-1), the state becomes

    (z+1-a-delta, max(0,s+1-b)),

and its support weight is t^([a>0]+[b>0]). The new running minimum is
M_(m+1)=M_m-delta, which verifies the stated state update. These are all
new constraints, so the transfer loses no information. Start at (0,0).
After n-1 complete columns, the last coordinate a_n has 0<=a_n<=z+1.

Let F_m(x,y) be the sum of the state weights times x^z y^s after m full
columns, and let alpha and beta describe the a and b half-steps. On
monomials they are

    alpha(x^z y^s) = (x^(z+1)+t sum_(r=0)^z x^r)y^s,
    beta(x^r y^s) = x^r(y^(s+1)+t sum_(h=0)^s y^h)
                    +t sum_(h=0)^(r-1) x^h.

The last sum is zero for r=0. The terms of beta correspond respectively
to b=0, 1<=b<=s+1, and s+2<=b<=s+1+r. Consequently

    F_m=(beta alpha)^m 1,  H_n=(alpha F_(n-1))(1,1).             (1)

Shift variables x=1+u, y=1+v. On Q[c,t][u,v], let U_i multiply by
the ith variable, D_i delete one power of it and kill constants, and E_i
set that variable equal to zero. Thus D_i U_i=I and U_i D_i=I-E_i.
For the moment c is an independent parameter. Define

    A=U_1+c+tD_1,
    B=U_2+c+tD_2+tD_1 E_2,  T=BA,  E=E_1 E_2.

At c=1+t these are exactly the shifted operators alpha,beta. For example
alpha f=(u+1+t)f+t(f-f(0,v))/u; the extra term of beta is
t(f(u,0)-f(0,0))/u. Let e=1 and let epsilon extract [u^0 v^0]. Then

    H_n(t)=epsilon A T^(n-1)e, evaluated at c=1+t.              (2)

The decisive operator identity is

    [B,A]=BA-AB=t E,  E=e epsilon.                             (3)

Only tD_1 E_2 fails to commute with A, and
[D_1,U_1]=E_1, proving (3).

## 2. A finite-rank trace calculation

Keep c,t independent and write h_n=epsilon A T^(n-1)e.
The operators are banded in the basis u^i v^j, i,j>=0. In particular,
each finite product has finite propagation. Every term containing E has
only finitely many nonzero matrix entries, so its trace and cyclic
permutations with banded operators are unambiguous finite sums.

From (3), [A,T]=-t EA, whence

    tr[A,T^n] = -t sum_(j=0)^(n-1) tr(T^j E A T^(n-1-j))
               = -nt h_n.                                   (4)

We now compute this finite-rank trace from the far horizontal boundary.
Let

    S(u)=u+c+t/u,
    J=U+c+tD  on Q[c,t][v],  E_v f=f(0),
    B_u=J+(t/u)E_v.

Far from horizontal index zero, horizontal shifts may be treated as
bilateral shifts. There A has Laurent symbol S(u), B has operator-valued
symbol B_u, and T^n has symbol S(u)^n B_u^n.

Here is an explicit justification of the boundary trace, including its sign.
For fixed vertical index j sum diagonal entries of [A,T^n] over horizontal
indices 0<=i<=N. Cancellation of adjacent terms leaves exactly

    t (T^n)_((N+1,j),(N,j)) - (T^n)_((N,j),(N+1,j)).

Take N>=2n+2. Each half-step moves the horizontal index by at most one,
so paths computing these entries cannot reach horizontal index zero.
The two entries therefore equal [u^1] and [u^(-1)], respectively, of
S(u)^n(B_u^n)_(j,j). Summing the displayed boundary expression is thus
-CT_u (u-t/u) S(u)^n times the appropriate vertical diagonal sum.

One may first sum 0<=j<=L, with L>=n+2. This rectangle contains the
diagonal support of [A,T^n]: each of the finite-rank terms in (4) propagates
at most n vertical steps and at most 2n+1 horizontal steps from the origin.
For each j, subtracting (J^n)_(j,j) inside the Laurent constant term does
not change it, since

    CT_u (u-t/u)S(u)^n
       = CT_u (u d/du)S(u)^(n+1)/(n+1)=0.

Every term of B_u^n-J^n contains E_v, so its nonzero diagonal entries
have j<=n. The resulting vertical sum is finite and independent of L.
Comparison with (4) gives the exact identity

    nt h_n = CT_u (u-t/u) S(u)^n R_n(t/u),                     (5)
    R_n(y)=tr((J+yE_v)^n-J^n).

This calculation does not set the trace of an arbitrary infinite-matrix
commutator equal to zero. The nonzero boundary term is essential.

## 3. Evaluate the rank-one perturbation

Let M(q)=epsilon_v (I-qJ)^(-1)1. Its coefficients count one-dimensional
nonnegative Motzkin walks with up-weight 1, level-weight c, and
down-weight t. Decomposing a nonempty excursion at its first step and,
if that step is up, its matching first return, proves

    M=1+cqM+tq^2 M^2.

Set V=tqM. It is the unique series with constant term zero satisfying

    V=q(V^2+cV+t).                                           (6)

The finite-rank perturbation trace satisfies

    sum_(n>=1) R_n(y) q^n/n = -log(1-yqM(q)).                 (7)

For completeness, differentiate the left side with respect to y. Cyclicity
of the finite-rank terms gives q epsilon_v(I-q(J+yE_v))^(-1)1.
Expanding in insertions of the rank-one operator E_v makes this
qM/(1-yqM). Integrating from y=0 proves (7) coefficientwise; no infinite
trace of J^n itself is needed. Substituting y=t/u gives

    R_n(t/u)=-n[q^n]log(1-V(q)/u).

Using this in (5) and applying constant-term integration by parts yields

    t h_n
      =-[q^n]CT_u (u-t/u)S(u)^n log(1-V/u)
      =1/(n+1) [q^n]CT_u S(u)^(n+1) V/(u-V).                (8)

Indeed (u d/du)S^(n+1)=(n+1)(u-t/u)S^n and
(u d/du)log(1-V/u)=V/(u-V). Expand the latter fraction in powers of V/u;
each q coefficient is a finite Laurent polynomial, so all operations
and exchanges of coefficient extractions are justified formally.

Put C_(m,k)=[u^k]S(u)^m for all integers k. The formal Lagrange formula
for (6) is

    [q^n]V^k = k/n [w^(n-k)](w^2+cw+t)^n  (1<=k<=n).

This is the ordinary formal power-series inversion formula; it also follows
by substituting q=w/(w^2+cw+t) in the coefficient residue and integrating
the resulting derivative term by parts. For k>n the coefficient is zero.
Since S(t/u)=S(u), we have C_(n,-k)=t^k C_(n,k). Hence (8) becomes
the promised finite coefficient-extraction formula, valid for every n>=1:

    h_n = 1/(n(n+1)t)
          sum_(k=1)^n k t^k C_(n+1,k) C_(n,k).                (9)

## 4. The coefficient sum telescopes

Differentiating S(u)^(n+1) gives, for every integer k,

    k C_(n+1,k)=(n+1)(C_(n,k-1)-t C_(n,k+1)).

Consequently the numerator sum in (9) is

    (n+1) sum_(k>=1)
        (t^k C_(n,k-1) C_(n,k)-t^(k+1) C_(n,k) C_(n,k+1))
      = (n+1)t C_(n,0) C_(n,1).

All sums are finite since C_(n,k)=0 for k>n. This proves, for arbitrary
formal c,t,

    epsilon A(BA)^(n-1)1 = C_(n,0) C_(n,1)/n.               (10)

Finally specialize c=1+t. Then S(u)=(1+u)(1+t/u), and

    C_(n,0)=sum_(j=0)^n binom(n,j)^2 t^j = B_n(t),
    C_(n,1)/n
       =sum_(j=0)^(n-1) binom(n,j+1)binom(n,j)t^j/n
       =sum_(j=0)^(n-1) binom(n-1,j)binom(n,j)t^j/(j+1)
       =A_(n-1)(t).

Together with (2), this proves the frozen identity for every n>=1.
For n=1 it gives 1+t. Polynomial identity extends the calculation over
Q(t) to t=0; there is no excluded specialization.

## Evidence and scope

`research-verifier.py` and `research-verifier.json` check the original
transfer, the shifted operators, the generic two-parameter lemma, the
finite trace boundary, and the telescoping coefficient identity by exact
arithmetic over the documented finite ranges. They calibrate the proof;
the uniform argument is the one above. The verifier is in the same model
context, not an independent mathematical referee.

The source proposal is Athanasiadis--Chapoton, arXiv:2605.26916, Section
9.3 final paragraph. Its primary HTML is retained in
`evidence/external/2605.26916.html`. The current primary-source comparison
and search limits are in `literature/research-screen.md`. No assertion of
global priority is made. This proof uses the source only to identify the
proposed problem; no unproved claim from that paper enters the argument.
