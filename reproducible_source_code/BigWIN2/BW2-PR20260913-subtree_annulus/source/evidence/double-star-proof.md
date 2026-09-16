# Shifted annulus for double stars: proof submitted for scrutiny

Research job: primary-20260913-subtree-annulus-research-bac30ce160a8.
Date: 2026-09-13 +08. This is a proof dossier, not an accepted manuscript.

## Exact scope

Let D(a,b), for integers a,b>=1, consist of an edge uv, a additional leaves
adjacent to u, and b additional leaves adjacent to v. Put q=a+b, n=q+2, and
c=(q+1)^(1/(q+1)). The claimed theorem is that every nonzero zero z of its
subtree polynomial satisfies the two STRICT inequalities

    1/2 < |z+1/2| < 1/2+c.

The zero z=0 is simple and lies on the inner boundary. Consequently the full
closed shifted-annulus conjecture holds for every tree of diameter at most
three and order n>=2. In that class, the only inner-boundary root is zero;
an outer-boundary root exists exactly for stars of even order, and that root
is uniquely z=-1-(n-1)^(1/(n-1)). The star formula and the corresponding
boundary observation are elementary prior material; the proposed new part
is the uniform two-parameter double-star result.

The original statement for arbitrary trees remains unresolved. No assertion
for diameter four or higher follows from this proof.

## Counting identity

Write w=1+z. A connected induced vertex set either is one of the q single
leaves, contains u but not v, contains v but not u, or contains both centres.
The four generating polynomials are qz, z w^a, z w^b, and z^2 w^q.
Therefore

    Phi_D(z)=z Q(z),   Q(z)=q+w^a+w^b+z w^q.                 (1)

Here Q is monic of degree q+1 and Q(0)=q+2, so zero is a simple zero of
Phi_D. Each subset is counted once, without quotienting by automorphisms.

## Exclusion of the closed inner disk for Q

For |z+1/2|<=1/2, both |z|<=1 and |w|<=1, and Re w>=0. If q>=4,

    |w^a+w^b+z w^q| <= 3 < q.

If q=3, the same estimate is strict away from z=0 and z=-1: the inner
disk intersects each of the circles |z|=1 and |w|=1 only at z=-1 and
z=0, respectively, and otherwise both moduli are less than one. At those
two exceptional points Q(0)=q+2 and Q(-1)=q, both positive. Thus (1) has
no zero in the closed disk for q>=3.

If q=2, necessarily a=b=1 and

    Q(z)=2+2w+z w^2.

The estimate |2+2w|>=Re(2+2w)>=2>1>=|z w^2| proves nonvanishing on the
same closed disk. This direct estimate removes any need for a cubic
stability theorem in the proof. As a separate exact check, the previously
used transform is H(x)=4x^3+9x^2+8x+2; its cubic Hurwitz determinants are
9, 64, 128. The earlier P4 calculation was correct.

## A scalar lemma on a shifted circle

Fix real c>0 and K=2c^2+2c+1. On |z+1/2|=c+1/2, let t=|z+1| and
s=|z|. Squaring the two moduli gives

    s^2+t^2=K,   c<=t<=c+1,   s=sqrt(K-t^2)>=c.             (2)

For every real k>=1, define f_k(t)=t^(-k)/(K-t^2)^(1/2). On this interval
all denominators are positive. Direct differentiation gives

    (log f_k)''=k/t^2+(K+t^2)/(K-t^2)^2>0,
    f_k''=f_k [((log f_k)')^2+(log f_k)'']>0.

Hence each f_k is strictly convex. Any sum of these functions with
nonnegative coefficients is convex, so its value is at most the greater of
its two endpoint values. Moreover

    f_k(c)=c^(-k)/(c+1),
    f_k(c+1)=(c+1)^(-k)/c,
    f_k(c+1)/f_k(c)=(c/(c+1))^(k-1)<=1.                    (3)

Thus every such sum attains a maximum at t=c. This is an analytic statement
on the entire interval, with no sampling premise.

## Strict domination on the outer circle

Now use c=(q+1)^(1/(q+1)), where q>=2, and the circle in (2). In particular
c>1. For fixed t>1, the function h(x)=t^x+t^(q-x) has
h''(x)=(log t)^2 h(x)>0. On 1<=x<=q-1 it is bounded above by its equal
endpoint values, so

    t^a+t^b <= t+t^(q-1).                                 (4)

For q=2 this also holds, since the interval is a single point. By (1)-(4),

    |q+w^a+w^b|/|z w^q|
       <= [q+t^a+t^b]/[s t^q]
       <= f_(q-1)(t)+f_1(t)+q f_q(t)
       <= [c+c^(q-1)+q]/[(c+1)c^q] =: F(c).              (5)

Every exponent in this use of the scalar lemma is at least one. Using
c^(q+1)=q+1 gives the exact endpoint margin

    1-F(c)=(c-1)(q+1-c^2)/[c(c+1)(q+1)] > 0.             (6)

To check the sign, c>1 and c^2=(q+1)^(2/(q+1))<q+1, because q+1>1 and
0<2/(q+1)<1. All denominator factors are positive. This handles q=2,
arbitrarily unbalanced a,b, and arbitrarily large q without an asymptotic
exception. The positive margin may tend to zero with q; no uniform positive
constant over all q is asserted.

Equations (5)-(6) prove |q+w^a+w^b|<|z w^q| everywhere on the outer circle.
Rouche's theorem applies to the entire polynomials Q and z(z+1)^q on its
interior and boundary. The comparison polynomial has one zero at 0 and q
zeros at -1, counted with multiplicity, all strictly inside because both
centres have distance 1/2 from -1/2. Thus Q has q+1 zeros strictly inside.
Its degree is q+1, so these are all its zeros. The additional simple zero
of Phi_D at zero is also inside. This proves strict outer containment and
completes the double-star theorem.

## Diameter at most three and equality

A tree of diameter one or two is a star. If its diameter is three, choose
a path x-u-v-y of length three. Every component attached to u or v away
from this path has depth at most one: otherwise the path from a vertex at
depth two to the opposite endpoint x or y has length at least four. An
attachment at x or y would also create a path of length four. Uniqueness of
paths in a tree rules out other attachments. Therefore all other vertices
are leaves at u or v, with at least one on each side, and the tree is D(a,b).

For a star K_(1,m), m=n-1>=1, the already known elementary formula is

    Phi(z)=z[(z+1)^m+m].

A nonzero root has w=z+1 satisfying w^m=-m and |w|=d=m^(1/m). If m>=2,
then d>1, so |z+1/2|=|w-1/2|>=d-1/2>1/2. If m=1, the sole nonzero
root is -2, whose shifted modulus is 3/2. Also |w-1/2|<=d+1/2; equality
holds precisely when w=-d, which solves w^m=-m exactly when m is odd.
The resulting root -1-d is unique on that circle. This proves the stated
diameter-at-most-three corollary and all its boundary cases, including n=2.

## Dependencies and limits

Dependencies: the counting argument above; elementary complex modulus
identities and inequalities; convexity from differentiation; Rouche's
theorem in its usual polynomial form. No cited radial tree theorem is used
as a mathematical premise. Literature sources establish the original scope,
prior boundary and comparison, rather than fill any proof step.

Known mathematical gaps in the stated family argument: none identified in
this research pass. Fresh referee verification of correctness, novelty and
value is still required. Exact finite checks are supplementary diagnostics;
the quantified assertion is proved analytically above. No new general tree
census, full original resolution, priority certification or review acceptance
is claimed.
