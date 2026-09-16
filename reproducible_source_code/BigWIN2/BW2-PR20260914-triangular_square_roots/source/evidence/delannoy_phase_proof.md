# Delannoy-square theorem submitted for mathematical review

Proposer: `primary-20260914-triangular-square-roots-research-8c4db654213f`.
Research date: 2026-09-14. This is a proof dossier, not an accepted manuscript.

## Exact scope

Let D(n,k) count paths from (0,0) to (n-k,k) with steps (1,0), (0,1),
and (1,1), and put D(n,k)=0 outside 0<=k<=n. Define

    d_n(y) = sum_{k=0}^n D(n,k)y^k,
    G_n(x) = sum_{k=0}^n (sum_{i=k}^n D(n,i)D(i,k))x^k.

**Theorem.** G_0=1. For every integer n>=1, G_n is monic of degree n
and has n distinct real roots, all in the open interval

    (-4-3 sqrt(2), -3+2 sqrt(2)).

This proves the D^2 part of Mao--Wang's Conjecture 4.1, with a uniform
root enclosure and simplicity. The A^2 part and strict consecutive
interlacing of G_n are not asserted here. The frozen original conjunction
therefore remains unresolved.

## 1. Two applications of a quadratic formula

Last-step decomposition of the paths gives

    d_0(y)=1, d_1(y)=1+y,
    d_n(y)=(1+y)d_{n-1}(y)+y d_{n-2}(y), n>=2.

If w,z are the distinct roots of t^2-(1+y)t-y, this recurrence gives

    d_n(y)=(w^{n+1}-z^{n+1})/(w-z).                 (1)

In particular, if u,v are the distinct roots of t^2-(1+x)t-x, ordinary
matrix multiplication and (1) give the exact divided difference

    G_n(x) = [u d_n(u)-v d_n(v)]/(u-v).             (2)

Indeed, G_n(x)=sum_i D(n,i)d_i(x); substitute (1) and sum the two powers.
These are polynomial identities on the indicated domains. No infinite
series or convergence argument is involved. Since D(n,n)=1, the ordinary
matrix square has (D^2)(n,n)=1, proving the degree and leading coefficient.

Write

    a=-4-3 sqrt(2), b=-3-2 sqrt(2), c=-3+2 sqrt(2),
    u_0=-1-sqrt(2),
    theta_0=arccos((1+u_0)/(2 sqrt(-u_0))).

Here a<b<c<0 and pi/2<theta_0<pi. Fix n>=1 and N=n+1.

## 2. Alternating signs in b<x<c

For x in (b,c), choose

    u=(1+x+i sqrt(-(x^2+6x+1)))/2, v=conjugate(u).

Thus Im(u)>0 and |u+1|^2=2. As x decreases from c to b, u moves
continuously along the upper semicircle from sqrt(2)-1 to u_0.
Its real part exceeds -3. Consequently

    Im(u^2+6u+1)=2 Im(u)(Re(u)+3)>0.

Let s be the square root of u^2+6u+1 having positive real and imaginary
parts, and set

    w=(1+u+s)/2, z=(1+u-s)/2, B=u/s.

These quantities vary continuously; Im(w)>0, s=w-z is nonzero, and u is
nonzero. The quadratic equation implies

    z=(1-w)/(1+w),

so Im(z)<0. The denominator 1+w is nonzero because Im(w)>0.

We need the strict inequality |w|>|z| throughout this arc. Suppose instead
that equality holds at an interior point. Neither root is zero. Then

    (w+z)^2/(wz) = 2+w/z+z/w belongs to [0,4].

The same expression equals -u-2-1/u. Its imaginary part can vanish for
Im(u)>0 only when |u|=1. Together with |u+1|^2=2 this forces Re(u)=0,
and hence u=i. But at u=i the expression is -2, a contradiction. There
is therefore no equality in the arc. At x=c the limiting u is positive,
and the real quadratic roots satisfy w>0>z and w+z=1+u>0; hence w>|z|.
Continuity establishes |w|>|z| everywhere in (b,c).

Use the continuous arguments arg(u) in (0,pi), arg(s) in (0,pi/2), and
arg(w) in (0,pi), and define the real continuous phase

    Phi(x) = N arg(w) + arg(u) - arg(s).

As x tends to c from below, all of u,s,w tend to positive real numbers,
so Phi(x) tends to 0. As x tends to b from above, u tends to u_0<0,
s tends to i sqrt(2+4 sqrt(2)), and

    w tends to (-sqrt(2)+i sqrt(2+4 sqrt(2)))/2
      = sqrt(-u_0) exp(i theta_0).

Thus Phi(x) tends to N theta_0+pi/2 at b. No assertion that Phi is
monotone is needed.

Equation (2), followed by (1), gives

    G_n(x)= Im[B(w^N-z^N)] / Im(u).               (3)

At any point where Phi(x)=(j+1/2)pi, the imaginary part of B w^N is
(-1)^j |B w^N|. Since |B z^N|<|B w^N| and Im(u)>0, (3) proves

    sign G_n(x)=(-1)^j.                           (4)

For each integer j with 0<=j<N theta_0/pi, the level (j+1/2)pi lies
strictly between the two endpoint limits of Phi. Such points can be chosen
in decreasing order of x for increasing j: parametrize the closed arc
from c to b, extend Phi by its limits, and take the first time each level
is reached. Continuity makes these first times exist and strictly increase.
They lie in the open arc. This first-passage argument does not require
phase monotonicity.

## 3. Alternating signs in a<x<b

Set h(t)=t(t-1)/(t+1). For u in (b,u_0), set

    x=h(u), v=(1-u)/(1+u).

Here h maps (b,u_0) increasingly and bijectively onto (a,b):

    h(b)=a, h(u_0)=b,
    h'(u)=1-2/(u+1)^2>0 in the open interval.

The numbers u,v satisfy u+v=1+x and uv=-x, and thus are precisely the
two outer quadratic roots in (2). Also

    b<u<u_0<v<-sqrt(2)<-1.

(As u decreases from u_0 to b, v increases from u_0 to -sqrt(2).)
Both lie in (b,c), the oscillatory interval for the ordinary d_n.
Define theta(t) in (0,pi) on this interval by

    cos theta(t) = (1+t)/(2 sqrt(-t)).

For the present u,v, pi/2<theta(v)<theta(u)<pi. As u decreases from
u_0 to b, theta(u) increases continuously and strictly from theta_0 to pi.
Formula (1) now has conjugate roots sqrt(-t) exp(+-i theta(t)), giving

    d_n(t)=(-t)^(n/2) sin(N theta(t))/sin theta(t).

Put M(t)=(-t)^(n/2+1)/sin theta(t)>0. Since -u>-v>0 and
0<sin theta(u)<sin theta(v), we have M(u)>M(v). Equation (2) becomes

    G_n(x) = [-M(u) sin(N theta(u))
                +M(v) sin(N theta(v))]/(u-v).     (5)

If theta(u)=(j+1/2)pi/N, then the dominant first term in the numerator,
together with u-v<0, gives sign G_n(x)=(-1)^j. For every j satisfying

    N theta_0/pi < j+1/2 < N,

there is exactly one such u, and these x values decrease as j increases.
The strict amplitude inequality ensures none of these values is zero.

## 4. Count n roots; handle the join without an endpoint assumption

Let m=ceil(N theta_0/pi); since 0<theta_0<pi, 1<=m<=N.

For j=0,...,m-1 use the samples from Section 2. The strict requirement
j<N theta_0/pi holds even when N theta_0/pi is an integer.
For j=m,...,n use the samples from Section 3. Here
j+1/2>N theta_0/pi and j+1/2<N, as required. Either group may be empty
only as allowed by these ranges. Every sample in the first group is to
the right of b; every sample in the second group is to the left of b.

We therefore have n+1 strictly decreasing points

    c>x_0>x_1>...>x_n>a,
    sign G_n(x_j)=(-1)^j.

The intermediate value theorem yields a root in each of the n disjoint
open intervals (x_{j+1},x_j). Since G_n has degree n, these are all its
roots, each has multiplicity one, and all lie in (a,c). The excluded join
x=b needs no sign evaluation and may itself be a root; the argument does
not assume otherwise. G_0=1 follows directly from the empty path. QED.

## Dependencies, limits, and gap list

The proof uses only the last-step recurrence, the quadratic formula,
elementary complex arithmetic and continuous arguments on explicit arcs,
and the intermediate value theorem. Finite computations are verification
aids, not the all-n justification. The decisive primary source is copied
in `evidence/external/2607.01572v1.pdf` (definitions on p.10 and Conjecture
4.1 on p.11). There is no known gap in this proposed D^2 argument;
independent mathematical review is still required. No proof of A^2,
consecutive interlacing, endpoint optimality, or a general Delannoy
preservation theorem is claimed.
