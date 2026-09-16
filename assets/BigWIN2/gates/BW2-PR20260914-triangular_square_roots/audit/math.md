Verdict: **accept** the exact frozen **result-note**, with original status
**unresolved**. The submitted proof establishes every part of its Delannoy-square
theorem, including simplicity and the open uniform root enclosure. It does not
resolve the Eulerian-square component of the original conjunction.

Referee job: `primary-20260914-triangular-square-roots-referee-c2c3e371bec6`.
Review date: 2026-09-14. Snapshot digest:
`afcfb64162aef0f427a3122f208edb356ac2e15cb197a2f8cd8e56b437beea5b`.
The proposer job recorded in the frozen claim is
`primary-20260914-triangular-square-roots-research-8c4db654213f`.
This was a fresh referee context, with no delegated agents or other model
processes. A separate context is a separate review pass, not a claim of
statistical independence or external peer review.

The reviewed statement is precisely this: let D(n,k) count paths from (0,0)
to (n-k,k) with steps (1,0), (0,1), (1,1), with the stated zero extension and
empty-path convention. Let

    G_n(x) = sum_{k=0}^n sum_{i=k}^n D(n,i) D(i,k) x^k.

Then G_0=1; for every integer n>=1, G_n is monic of degree n and has n
distinct real roots in

    (a,c) = (-4-3 sqrt(2), -3+2 sqrt(2)).

The ordinary matrix product and its indexing agree with the frozen source.
No weaker interval, finite cutoff, multiplicity convention, or different
Delannoy array has been substituted for the claim.

The inputs consulted were source.md, problem.md, claim.json, audit/snapshot.json,
and its listed proof, code, data and source files. The listed source text was
read through its end; pages 10–11 were also extracted directly from the listed
PDF and compared with the live primary source. Both certificate JSON files
were parsed in full. No earlier referee verdict, job transcript, checkpoint,
state file or unlisted project history was used. The canonical digest of the
snapshot mapping and all 11 frozen file hashes matched, both before and after
the fresh verification. In particular, source.md retained SHA-256
`a1a75e5793dcd6534b63902eb3b6d415dfd60e8f129376f7af671b7b9401f1f3`.

The decisive proof can be reconstructed from the path definition. With
d_n(y)=sum_k D(n,k)y^k, last-step decomposition gives d_0=1, d_1=1+y and
d_n=(1+y)d_{n-1}+y d_{n-2}. If w,z solve t^2-(1+y)t-y=0 and are distinct,
the initial conditions and recurrence give

    d_n(y) = (w^(n+1)-z^(n+1))/(w-z).

For the distinct roots u,v of t^2-(1+x)t-x=0, finite summation of this identity
gives

    G_n(x) = [u d_n(u)-v d_n(v)]/(u-v).

The power n+1, including the two factors u and v in the last numerator, is
correct. There is no interchange of infinite limits or series. The path to
(0,n) is unique, so D(n,n)=1 and (D^2)(n,n)=1. This proves the degree assertion
without a root-count assumption. The empty path proves G_0=1.

For the first sign argument set b=-3-2 sqrt(2), u_0=-1-sqrt(2), N=n+1 and
theta_0=arccos((1+u_0)/(2 sqrt(-u_0))). Thus pi/2<theta_0<pi. For b<x<c,
take the outer root u with positive imaginary part, so v is its conjugate.
The identities u+conj(u)=1+x and |u|^2=-x imply |u+1|^2=2. As x decreases
from c to b, u follows the upper semicircle from sqrt(2)-1 to u_0. In particular
Re(u)>-3 and Im(u)>0. Therefore the imaginary part of u^2+6u+1 is strictly
positive. Its square root s with positive real and imaginary parts exists
continuously and is nonzero. For w=(1+u+s)/2 and z=(1+u-s)/2, Im(w)>0 and

    z=(1-w)/(1+w),    Im(z)=-2 Im(w)/|1+w|^2<0.

This also checks the denominator 1+w. Neither inner root is zero, since
wz=-u and u is nonzero.

The strict-modulus lemma is valid throughout the open arc. If |w|=|z|, then
w/z lies on the unit circle and

    (w+z)^2/(wz)=2+w/z+z/w is real and belongs to [0,4].

The same quantity is -u-2-1/u. Its imaginary part equals
Im(u)(1/|u|^2-1), which forces |u|=1. Intersecting this with |u+1|^2=2 and
Im(u)>0 forces u=i. At that point the quantity equals -2, a contradiction.
Thus equality never occurs. At the right endpoint c the limiting u is
positive and the limiting real roots satisfy w>0>z and w+z>0, which selects
|w|>|z| by continuity on the connected arc. No unproved uniform lower bound
on this strict inequality is needed.

Put B=u/s. All three arguments in

    Phi(x)=N arg(w)+arg(u)-arg(s)

have the continuous branches stated in the dossier. Their endpoint limits
give Phi(c-)=0 and Phi(b+)=N theta_0+pi/2. In particular,
u_0^2+6u_0+1=-2-4 sqrt(2) has the required sign, and the limiting argument
of w is theta_0. Conjugation in the divided difference gives

    G_n(x)=Im[B(w^N-z^N)]/Im(u).

At Phi=(j+1/2)pi, the first imaginary part has sign (-1)^j and absolute
value |B w^N|; the second has absolute value at most |B z^N|, which is
strictly smaller. Consequently the sign of G_n is (-1)^j.

For each integer 0<=j<N theta_0/pi the required phase level is strictly
between the endpoint limits. The first-passage selection is sound even if
Phi is not monotone: on a closed arc parametrized from c to b, continuity
gives a first hitting time for every level; reaching a higher level from 0
requires passing each lower level strictly earlier. Endpoint strictness
places all selected times in the open arc. This supplies the claimed order
of the first family of samples without adding a phase-monotonicity assumption.

For the second sign argument h(u)=u(u-1)/(u+1) maps (b,u_0) increasingly
onto (a,b). Indeed h(b)=a, h(u_0)=b, and
h'(u)=1-2/(u+1)^2>0 on that open interval. With v=(1-u)/(1+u), the identities
u+v=1+h(u), uv=-h(u) and

    b<u<u_0<v<-sqrt(2)<-1

hold. Hence these are distinct negative outer roots, both in (b,c).
The angle theta(t) defined by cos(theta(t))=(1+t)/(2 sqrt(-t)) is decreasing
in t: the derivative of its cosine is (1-t)/(4(-t)^(3/2))>0. Thus
pi/2<theta(v)<theta(u)<pi, and theta(u) increases from theta_0 to pi as
u decreases from u_0 to b. Both sine denominators are strictly positive.

The ordinary-row quadratic formula gives
d_n(t)=(-t)^(n/2) sin(N theta(t))/sin(theta(t)). Put
M(t)=(-t)^(n/2+1)/sin(theta(t)). Since -u>-v>0 and
sin(theta(u))<sin(theta(v)), M(u)>M(v)>0. The divided difference is therefore

    G_n(h(u)) = [-M(u) sin(N theta(u))+M(v) sin(N theta(v))]/(u-v).

At theta(u)=(j+1/2)pi/N the numerator's first term strictly dominates; the
negative denominator u-v changes its sign to (-1)^j. There is exactly one
sample for each index with N theta_0/pi<j+1/2<N. The samples decrease in x
as j increases. This checks the strict amplitude comparison and its sign,
including odd n, for which the positive real base -t makes the fractional
power unambiguous.

Finally let q=N theta_0/pi and m=ceil(q). Since 0<q<N, 1<=m<=N. For
j=0,...,m-1 one always has j<q, including the case q is an integer.
For j=m,...,N-1 one has q<j+1/2<N. These are exactly N=n+1 indices with
no gap or duplication. All samples in the first family are right of b;
all in the second family are left of b. Their signs alternate in the
combined strictly decreasing order. The n disjoint open intervals between
them each contain a root. A degree-n polynomial having n distinct real roots
has no remaining nonreal roots or multiplicities. Every such root lies in
(a,c), and c<0. For n=1 the lower family is empty and the same count applies.
No evaluation at the coalescing outer-root point b is used; b may be inside
one of the sign-change intervals. The argument does not divide by zero there
or assume that b is not a root.

Fresh computational checks were implemented in audit/referee_checks.py and
completed successfully with results in audit/referee_checks.json. The program
does not import or run either proposer script. It rebuilds the path counts
using endpoint-coordinate dynamic programming through degree 257, cross-checks
all entries through degree 32 by enumeration according to the number of
diagonal steps, and forms the required ordinary matrix products directly.
Every coefficient row in the serialized certificates matches. The program
evaluates the integer sum sum_k a_k p^k q^(n-k) at every serialized p/q,
separately from both proposer Horner implementations. All **530** signs,
strict orders and rational enclosure comparisons passed, at degrees
**1, 2, 3, 4, 5, 8, 16, 31, 64, 128, 257**.

SymPy exact rational root isolation also confirmed n simple roots inside the
claimed enclosure for every n=1,...,24. Symbolic checks verified the outer
and inner quadratic relations, h's endpoints and derivative, the divided
difference for n=0,...,12, and the four-term recurrence for n=4,...,32.
The two subsidiary failed-route examples were independently recomputed:
the transformed palindromic degree-six input has exactly four real roots
and is squarefree, and the cubic auxiliary polynomial has a root -7 while
G_4 has no root at or below -7. These observations have the limited scope
stated in the frozen dossier. None refutes the original conjecture. The
finite checks corroborate the submitted proof; the all-n conclusion comes
from the reconstructed argument above. No proof assistant was used.

The nearest primary source inspected is Mao and Wang, *The Narayana
transformation*. Its PDF Conjecture 4.1, p.11, is the same as HTML Conjecture
4.15. It conjectures the original conjunction; the preceding section supplies
the D-square recurrence and initial rows, which agree with the frozen inputs.
Its Corollary 3.6 concerns Pascal, Stirling and Narayana matrices and does not
include D. The live arXiv record inspected on the review date lists v1 only.
See the [primary paper](https://arxiv.org/html/2607.01572v1) and its
[version record](https://arxiv.org/abs/2607.01572).

The publisher's indexed abstract for Wang, Zheng and Chen, *Analytic aspects
of Delannoy numbers*, Discrete Mathematics 342(8) (2019), 2270–2277,
establishes the ordinary-row interval (b,c), density and asymptotic normality.
That comparison supports attribution of the ordinary-row background, not
novelty of the quadratic formula. See the
[publisher record](https://www.sciencedirect.com/science/article/pii/S0012365X19301141).
Both a DOI open and a direct publisher-page open returned internal access
errors during this pass; full-text noncontainment of a D-square result in
that paper has not been established by this review.

The bounded fresh searches included: `"Delannoy" "square" "real-rooted"`,
`"Delannoy" "matrix" "roots" "square"`,
`"Delannoy" "matrix square" roots`, and
`"Analytic aspects of Delannoy numbers"`, including a publisher/author-domain
search for the last title. Secondary search matches were discovery leads
only. No equivalent D-square theorem was found in the primary material
actually inspected. This is a bounded comparison, not a proof of priority
or an exhaustive exclusion of older general theorems.

The precise contribution is the all-degree D-square component with simplicity
and the stated uniform enclosure. It is a natural component of the published
question and has a concrete use: it certifies the zero geometry of every row
of this matrix product, giving a proved starting point for further interlacing
questions. The two-stage sign proof supplies substantive work beyond the
ordinary-row result; no applicable preserver theorem is being assumed. The
submitted scope is therefore a nontrivial result-note, rather than a finite
observation or arbitrary restriction. No overlapping note was submitted in
the frozen evidence for a merger decision.

No unresolved correctness gap or substantive claim repair remains in this
audit. Preserve the stated boundaries in any manuscript: A-square,
consecutive strict interlacing, endpoint optimality and a general Delannoy
preservation theorem remain outside the accepted statement. The publisher
access limitation must remain explicit if discussing novelty. The next
workflow step is the runner's check-math gate against this unchanged snapshot,
followed by writing at exactly the accepted scope. This report does not create
a manuscript or constitute publication, citation, build or visual acceptance.
