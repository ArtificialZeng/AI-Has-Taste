# Algebraic reduction and a new discriminating argument

Provenance: newwin-00001-p18-triage-2060d7b82e53, 2026-09-12.
These are triage arguments for the next research pass, not an accepted result.
All calculations below are exact; the supplementary computation has finite scope.

## Formal series and the zero kernel

Fix a prime p, write P=x^(p-1)+x^(-1), and set

    Phi(Q)=sum_{n>=0} ct(P^n Q) z^n,
    a_j=(p^j-1)/(p-1),
    Y=sum_{j>=1} z^(a_j).

Frobenius gives Y=z(1+Y^p), and this equation uniquely determines the series
with zero constant coefficient. Its compositional inverse is f(x)=x/(1+x^p).
For r,n>=0 the formal residue change of variable z=f(x), whose derivative in
characteristic p is f'(x)=1/(1+x^p), gives

    [z^n]Y^r = Res_x x^r f(x)^(-n-1) f'(x) dx
              = [x^(n-r)](1+x^p)^n
              = ct(P^n x^r).

The substitution rule is for an invertible series with linear coefficient 1;
it holds integrally and hence after reduction modulo p. There is no division
by n in characteristic p. Thus Phi(x^r)=Y^r for every r>=0, including r=0.

The ring R=F_p[t,X]/(X^p-tX+1) is free over F_p[t], with basis
1,X,...,X^(p-1), because the defining polynomial is monic. In R the element
X is invertible, with inverse t-X^(p-1). The maps X->x, t->P and
x->X, x^(-1)->t-X^(p-1) are inverse ring maps between R and the Laurent
polynomial ring. Consequently each Laurent Q has a unique expression

    Q=sum_{r=0}^{p-1} f_r(P)x^r,  f_r in F_p[t].

If Phi(Q)=H(Y), then ct(Q)=H(0), and

    Phi(PQ)=(Phi(Q)-ct(Q))/z = L(H)(Y),
    L(H)(y)=(H(y)-H(0))(y^(-1)+y^(p-1)).

L maps polynomials to polynomials. For nonconstant H of degree d it preserves
the leading coefficient and has degree d+p-1. It kills constants. The images
of 1 and P^k x^r, with k>=0 and 1<=r<=p-1, are 1 and the monic polynomials
L^k(y^r), with distinct degrees 0 and r+k(p-1), covering all nonnegative
degrees exactly once. Therefore they form a triangular vector-space basis
of F_p[y]. Evaluation H->H(Y) is injective: the least nonzero term of H
has the same degree and coefficient after substitution Y=z+O(z^2).

This gives the proposed all-Q reduction and exact zero classification:

    Phi(Q)=H(Y) for a unique polynomial H,
    Phi(Q)=0 iff Q belongs to P F_p[P].

Here P F_p[P] means the subspace of polynomials in P with zero constant
coefficient, not the ideal P F_p[x,x^(-1)]. In module coordinates it means
f_r=0 for r>=1 and f_0(0)=0. This distinction is essential.

## The support condition that survives cancellation

For H of degree D, any n in the support of H(Y) occurs in some monomial
Y^r with a nonzero coefficient of H, 0<=r<=D. Thus n is a sum of r of the
positive integers a_j, with repetition allowed. For the base-p digit sum s_p,

    (p-1)n+r=sum_{i=1}^r p^(j_i),
    s_p((p-1)n+r)<=r<=D.

The r=0 term is possible only at n=0. Cancellation can remove support points
but cannot invalidate this containment. This is stronger information than
zero density. Denote its right-hand superset by

    S_{p,D}={n>=0: some r in {0,...,D} has s_p((p-1)n+r)<=D}.

## Proposed finite-sums obstruction: check this next

1. If a word u is recurrent and u_a is nonzero, there are positive integers
t_1,t_2,... such that u_(a+s)=u_a for every finite sum s of distinct t_i,
including the empty sum. Inductively, once t_1,...,t_m are chosen, choose a
later occurrence of the prefix through position a+t_1+...+t_m. Its starting
position can be t_(m+1), chosen larger than the previous sum. This copies
all already constructed positions, and proves the induction.

2. Every infinite sequence of positive integers has a nonempty consecutive
finite block whose sum is divisible by any prescribed p^K. Among p^K+1
partial sums of a tail, two have the same residue. This works after discarding
any finite initial segment, so it can be repeated with disjoint blocks.

3. Suppose a+FS(t_i) is contained in S_{p,D}. Use step 2 to construct D+1
disjoint block sums b_1,...,b_(D+1). Choose K_1 with
p^K_1>(p-1)a+D and b_1 divisible by p^K_1. After constructing b_i choose
K_(i+1) with p^K_(i+1)>(p-1)b_i and take b_(i+1) from a later unused
tail divisible by p^K_(i+1). The base-p digit supports of (p-1)b_i then
occupy disjoint, increasingly high intervals. Each is nonempty. They are
also disjoint from every low term (p-1)a+r, 0<=r<=D. Therefore for
n=a+b_1+...+b_(D+1), every such r satisfies

    s_p((p-1)n+r)
      =s_p((p-1)a+r)+sum_i s_p((p-1)b_i) >= D+1.

But n belongs to a+FS(t_i), a contradiction. Positivity ensures the upper
endpoint of each block is above its lower endpoint, so the K_i increase.
The same argument covers D=0; alternatively a nonzero constant H has only
one nonzero coefficient and its word is plainly nonrecurrent.

If all three steps and the reduction survive independent scrutiny, every
nonzero H produces a nonrecurrent word, giving the original iff assertion
and the above explicit kernel. This is a concrete proof route to examine,
not a novelty or acceptance claim. The next phase should first challenge
the recurrence-to-finite-sums induction, carry separation for all offsets,
and the characteristic-p residue substitution, instead of repeating a
search for density-zero implications.

## Small boundary check

For Q=x, support is exactly {a_j:j>=1} with coefficient 1. The adjacent
nonzero gaps are p,p^2,p^3,..., so the word 1 followed by p-1 zeros followed
by 1 occurs only at index 1. Q=1 gives (1,0,0,...), also nonrecurrent.
Q=P gives the zero word. These agree with the proposed classification.

## Relation to prior literature

Kohen's Question 20 motivates the fixed-P problem; Theorem 14 only supplies
density-one zeros. The residue/module computation and special digit argument
above were worked out here as a verification of the inherited route.
Byszewski–Konieczny's arid-set and finite-sums theory is relevant prior work;
its use of “sparse” sometimes means density zero. See the live source screen
for the exact statements inspected. No general assertion that all
density-zero recurrent words vanish is used or valid here.
