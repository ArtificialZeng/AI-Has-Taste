# Mathematical referee report

## Frozen scope

The candidate is a `result-note`, not a resolution of the original strong
shift equivalence problem.  Its exact theorem concerns 2-by-2 nonnegative
integer shift-equivalence witnesses `(R,S)` between

\[
A=\begin{pmatrix}1&12\\11&1\end{pmatrix},\qquad
B=\begin{pmatrix}1&132\\1&1\end{pmatrix}.
\]

It asserts that their lag is at least 22, that lag 22 occurs, and hence that
any unrestricted SSE chain (if one exists) has at least 22 elementary links.
The candidate explicitly leaves the existence of an unrestricted SSE chain
unresolved.  I reviewed this exact scope; I did not reinterpret it as a result
about bounded intermediate dimensions or as a resolution of the source
problem.

## Reconstruction of the argument

Writing a general 2-by-2 matrix in each intertwining identity and comparing
entries gives, with no invertibility assumption,

\[
R=\begin{pmatrix}x&12z\\z&11x\end{pmatrix},\qquad
S=\begin{pmatrix}11u&12v\\v&u\end{pmatrix}
\]

for nonnegative integers `x,z,u,v`.  If

\[
A^L=\begin{pmatrix}a&12b\\11b&a\end{pmatrix},\qquad
a+b\sqrt{132}=(1+\sqrt{132})^L,
\]

and `(p,q,r,s)=(xu,zv,xv,zu)`, the product equations reduce exactly to

\[
11p+12q=a,\qquad r+s=b,\qquad pq=rs.
\]

Conversely, every nonnegative integral solution of these scalar equations
lifts to `x,z,u,v`: the nonnegative rank-one matrix
`[[p,r],[s,q]]` has an integral nonnegative outer factorization.  Direct
multiplication then gives both `RS=A^L` and `SR=B^L`, as well as the two
intertwining identities.  Thus the scalar reduction is an equivalence, not
only a necessary test.

Set `X=24q-a` and `Y=|r-s|`.  Completing the square yields

\[
X^2-132Y^2=(-131)^L.
\]

The reverse formulas

\[
q=(X+a)/24,\quad p=(a-12q)/11,\quad
r=(b+Y)/2,\quad s=(b-Y)/2
\]

show that the stated congruence, sign, and size filters recover precisely the
nonnegative scalar solutions.

I checked the completeness step in the quadratic ring rather than treating
the computation as a bounded search in `X` or `Y`.  For
`K=Q(sqrt(33))`, the ring of integers has discriminant 33.  Its Minkowski
bound is `sqrt(33)/2<3`; the two norm-2 prime ideals are principal because
`(5+sqrt(33))/2` has norm -2.  Hence the class number is one.  The conjugate
elements

\[
\lambda=1+2\sqrt{33},\qquad \bar\lambda=1-2\sqrt{33}
\]

generate the distinct primes above 131 and both have norm -131.  The least
positive unit greater than one is
`epsilon=23+4*sqrt(33)`: the equations `u^2-33v^2=+/-4` have no solution
for `1<=v<8`, and at `v=8` the norm-plus solution is `(u,v)=(46,8)` while
the norm-minus equation has none.  Standard real-quadratic unit cyclicity
therefore gives all norm-one units as `+/-epsilon^n`.

It follows from unique ideal factorization that every integral solution of the
norm equation is

\[
\pm\lambda^j\bar\lambda^{L-j}\epsilon^n,
\qquad 0\le j\le L,\ n\in\mathbb Z.
\]

The two reconstruction bounds imply that both real embeddings have magnitude
at most `(1+sqrt(132))^L`.  Each embedding of the nonunit factor has magnitude
greater than one, while `epsilon=23+2*sqrt(132)>1+sqrt(132)`.  Thus
`n>=L+1` violates one embedding bound and `n<=-L-1` violates the other.
The finite enumeration `0<=j<=L`, `-L<=n<=L`, with both signs, is therefore
exhaustive.

## Exact checks performed

The snapshot hashes of `claim.json` and every listed evidence file match
`audit/snapshot.json`; its digest is
`49a052feaeae6b3876006ac5ed12f5a9351fab520a15b89424a8ee069a18676b`.

I ran both supplied exact-arithmetic programs.  The main certificate returned
solution counts

\[
(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1)
\]

for lags 1 through 22 and verified all four lag-22 matrix identities.  The
triage checker independently verified the displayed similarity and lag-22
witness.

I also wrote and ran `audit/referee_check.py` (SHA-256
`33235edccb8872d58fffbab269cdbdb69c54ca095556effcc1f211954dce19f9`).
It independently implemented the quadratic-pair arithmetic, enumerated a
strictly wider exponent window `-L-5<=n<=L+5`, confirmed that every feasible
record lies in the proved window, reproduced the same 1-through-22 counts,
and rechecked the four endpoint identities using separately implemented
matrix arithmetic.

Finally, an SSE chain with `m` elementary links composes by taking the forward
product of the rectangular `R_i` and reverse product of the `S_i`.  Because
both endpoints are 2-by-2, these products are 2-by-2 and satisfy the SE
identities at lag `m`.  The established minimum lag therefore proves the
claimed 22-link lower bound even when intermediate SSE matrices have arbitrary
dimensions and entries.

## Source comparison and contribution

The inspected primary paper defines SE and explicitly gives the SSE-to-SE
composition.  For the same Baker family it proves SSE only through `k<=10`
and at `k=12`; for the remaining tested values it reports search failure as
nonproof.  Its discussion gives special lag-4 witnesses for `k=7,12` and only
preliminary, explicitly unproved evidence about which parameters admit lag 4.
It does not state or prove minimum lag 22 for the fixed `k=11` pair.  The
frozen literature screen reports a focused search finding no equivalent
fixed-instance minimum-lag theorem, while correctly declining to claim
priority.  Relative to the nearest cited result, the exact minimum-lag theorem
and its unconditional lower bound on all possible SSE-chain lengths are a
nontrivial, useful subsidiary result rather than a toy restriction or a claim
to have solved the original open problem.

## Verdict

**Accept.**  The candidate's exact partial theorem is correct at its frozen
scope, the exhaustive step is justified independently of the finite program,
the exact computations reproduce, the implication for arbitrary SSE chains is
valid, and the contribution is honestly separated from the unresolved
original question.  I found no mathematical gap requiring revision.
