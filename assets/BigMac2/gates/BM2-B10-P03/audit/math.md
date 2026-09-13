# Fresh mathematical referee report

## Frozen scope and verdict

I reviewed the exact `result-note` claim frozen by snapshot digest
`586eda8eef6f713c2b7cef9d8372b6e483ff29ebaef1a646cfa6f7844502ff67`.
The submitted scope is deliberately narrower than the original problem: it
claims the curvature formulas in all four shortest-path chambers, agreement on
their walls, the complete positive fixed-point set, and one exact non-uniform
stationary counterexample.  It expressly does not claim the omega limits of
non-fixed initial data.  I did not use a progress summary or an owner verdict.

**Verdict: accept the exact frozen scope as a result-note.**  The original
global phase-portrait problem remains unresolved.

## Reconstruction of the transport calculation

Let `epsilon = 1-alpha`.  For an oriented edge from `x` to `y`, write the
third point as `z`, put

\[
D=d(x,y),\qquad X=d(x,z),\qquad Y=d(y,z),
\]

and let the non-lazy probabilities from `x` to `y,z` be `p,1-p` and those
from `y` to `x,z` be `q,1-q`.  If `A=q-p`, the signed mass
`m_x-m_y` at `x,y,z` is

\[
1-\epsilon(1+q),\quad -1+\epsilon(1+p),\quad \epsilon A.
\]

For sufficiently small positive `epsilon`, the first entry is positive and
the second is negative.  If `A` is nonnegative, transport all mass at `z` to
`y` and all mass at `x` to `y`.  Its cost is

\[
D[1-\epsilon(1+q)]+\epsilon AY.
\]

The dual potential `f(y)=0`, `f(x)=D`, `f(z)=Y` has exactly the same value.
It is 1-Lipschitz because the only remaining condition is
`|D-Y| <= X`, the reverse triangle inequality.  If `A` is nonpositive, send
`-epsilon A` from `x` to `z` and the remaining source mass from `x` to `y`.
The cost is

\[
D[1-\epsilon(1+p)]-\epsilon AX,
\]

and it is certified by `f(y)=0`, `f(x)=D`, `f(z)=D-X`; here the remaining
Lipschitz condition is `|D-X| <= Y`.  Thus primal and dual values agree
exactly in both cases.  In particular, there is no unjustified limiting
exchange: the Wasserstein distance is affine in `epsilon` in a neighborhood
of zero.  Dividing its exact first-order deficit by `D>0` gives

\[
\kappa(x,y)=
\begin{cases}
1+q-A Y/D,&A\geq0,\\
1+p+A X/D,&A\leq0.
\end{cases}
\]

For the edge `a=23`, oriented from 2 to 3, direct use of the inverse-weight
kernel gives

\[
p={c\over a+c},\qquad q={b\over a+b},\qquad
A={a(b-c)\over(a+b)(a+c)},
\]

with `(D,X,Y)=(d_a,d_c,d_b)`.  Cyclic permutation handles the other two
edges.  These identities also cover `A=0`; the two transport formulas then
coincide.

In the triangle-inequality chamber, `D` and the other two distances are the
corresponding raw edge lengths.  If an edge has length `e` and the other
lengths are `M >= m`, substitution and collection over
`(e+M)(e+m)` gives

\[
\kappa_e={e^2+2eM+em+3Mm-M^2\over(e+M)(e+m)}.
\]

If instead `L >= u+v`, then the path distance across the long raw edge is
`u+v`; substitution for the long edge and the two short edges gives

\[
\kappa_L={S[L(u+v)+2uv]\over(L+u)(L+v)(u+v)},\qquad
\kappa_u={S\over L+u},\qquad
\kappa_v={S\over L+v},
\]

where `S=L+u+v`.  At `L=u+v`, substituting into both displays gives the same
three components.  All denominators used here are strictly positive on the
claimed positive domain.  The four chambers cover that domain, including
their walls.

## Fixed points

Because the normalized weights are positive and sum to one, the normalized
flow vanishes exactly when all three curvatures are equal.  Sort the raw
lengths as `L >= M >= m > 0`.

In the triangle-inequality chamber, direct subtraction of the preceding
formula yields

\[
\kappa_M-\kappa_m=
-{2L(M-m)\over(L+M)(L+m)}.
\]

Equality therefore forces `M=m=x`.  For this specialization,

\[
\kappa_L-\kappa_x={ (L-x)(L-2x)\over2x(L+x)}.
\]

Since this chamber imposes `x <= L <= 2x`, equality occurs only for `L=x`
or `L=2x`.  These are the uniform point and the three permutations of the
wall ratio `2:1:1`.

In a long-edge chamber, equality of the short-edge curvatures
`S/(L+M)` and `S/(L+m)` forces `M=m=x`.  Conversely, when `M=m=x` the long
formula simplifies to `S/(L+x)`, the same value as both short curvatures, for
every `L >= 2x`.  After normalization, the complete positive fixed set is
therefore

\[
\{(1/3,1/3,1/3)\}\ \cup\
\bigcup_{\sigma\in S_3}
\left\{\sigma\left({r\over r+2},{1\over r+2},{1\over r+2}\right):r\ge2\right\}.
\]

The sorting argument is exhaustive, and the converse was checked, so this is
a classification rather than merely a family of examples.

## Exact counterexample and ODE point

At `(a,b,c)=(2/3,1/6,1/6)` the long-to-short ratio is 4, so the point lies
strictly inside a long-edge chamber.  The long-chamber formulas give all
three curvatures as `6/5`.  Hence `K=6/5` and every component of the
normalized vector field is zero.  The vector field is smooth in a
neighborhood of this strict-chamber point, so ordinary local uniqueness
applies; the constant solution extends for every nonnegative time and cannot
spontaneously leave the fixed point.  Its omega-limit set is exactly that
singleton, not the uniform point.  This is an exact positive counterexample
to the universal uniform-convergence subclaim.

## Independent checks performed

I ran the frozen exact checker.  It reported successful `Fraction` checks for
13,824 positive integer triples, including 456 fixed triples.

I also recomputed the Wasserstein distance by a separate generic dual method,
not by equation (2): after fixing one potential to zero, I imposed all six
pairwise 1-Lipschitz half-plane inequalities, enumerated every pairwise
intersection, retained feasible vertices, and maximized the dual objective
using exact rational arithmetic.  With `epsilon=1/101`, this independently
matched the asserted chamber formulas and fixed-point criterion on all 1,728
triples in `{1,...,12}^3`; 120 were fixed.  It also returned curvature
`(6/5,6/5,6/5)` for ratio `(4,1,1)`.  These finite checks are sanity checks,
not substitutes for the exact primal/dual and algebraic proof above.

I specifically checked quantifiers and edge cases: positivity rules out zero
metric denominators; the sign split includes equality; the shortest-path
walls have componentwise agreement; no boundary vector field is asserted;
and no conclusion about a non-fixed trajectory or a complete global
phase portrait is smuggled into the statement.

## Source comparison, value, and remaining limitations

The frozen source comparison says that the cited Bai--Hua results concern
finite trees and leave cyclic graphs open; the cited general weighted-graph
long-time result assumes that every raw edge stays a shortest route; and the
cited static triangle calculation uses a uniform-neighbor kernel rather than
the inverse-weight kernel.  The strict-long-edge fixed ray found here lies
outside the shortest-edge hypothesis and on the precise cyclic model posed by
the source.  Moreover, classification of all interior fixed points answers an
explicit component of the original question, and the exact stationary point
decides its universal-convergence subclaim.  This is a nontrivial useful
partial result, not an arbitrary toy restriction or a routine consequence of
the nearest results as described in the frozen record.

Under this job's frozen-evidence restriction, I did not reopen external
literature PDFs.  Accordingly, this verdict does not upgrade the record's
bounded literature search into a claim of priority.  The submitted claim
itself makes no absolute novelty claim, and `problem.md` already labels exact
priority as unverified.  That honest literature limitation does not affect
the exact mathematical result or its demonstrated relevance to the source.

The major unresolved gap is the one expressly excluded from the candidate:
global existence/uniqueness through all walls and the omega-limit
classification for arbitrary non-fixed positive initial data.  Resolving it
would be a substantive new claim requiring a new snapshot and fresh review;
it is not needed for acceptance of this result-note's frozen scope.
