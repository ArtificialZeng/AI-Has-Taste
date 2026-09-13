# Exact finite certificate for the degree-four boundary

## Theorem certified

Let $K$ be any field and $I\subset K[x,y,z]$ an
$\mathfrak m=(x,y,z)$-primary monomial ideal whose unique minimal monomial
generating set has at most four elements, each of total degree at most four.
Then

\[
v(\overline I)\leq v(I).
\]

This document gives the completeness and algorithm-correctness argument for
the machine-readable records in `lp_results.json` and `facet_results.json`.
It uses no floating-point evidence.

## 1. Complete finite domain

Because $I$ is $\mathfrak m$-primary, a power of each variable lies in
$I$. A minimal generator dividing such a power is itself a pure power.
Thus $G(I)$ contains exactly one minimal pure power on each axis. There is at
most one remaining generator, so, with the variables still labeled, $I$ is
exactly one of

\[
(x^a,y^b,z^c),\qquad
(x^a,y^b,z^c,x^r y^s z^t),
\]

where $1\leq a,b,c\leq4$. In the second case, minimality is equivalent to

\[
0\leq r<a,\quad0\leq s<b,\quad0\leq t<c,
\quad r+s+t\leq4,
\quad |\{i:r_i>0\}|\geq2.
\]

Indeed, the three strict inequalities prevent a pure power from dividing the
mixed generator; support in at least two variables prevents the mixed
generator from dividing any pure power. The converse is immediate. Therefore
the literal nested loops in both enumerators cover the whole quantified class,
without a symmetry quotient. They independently give 64 three-generator and
453 four-generator labeled ideals, hence 517 ideals in total, with no duplicate
generator tuple.

For any of them, every exponent outside

\[
B=[0,a-1]\times[0,b-1]\times[0,c-1]
\]

belongs already to $I$, hence also to $\overline I$. Thus all standard
monomials lie in $B$, which has at most 64 points. Both runs evaluate the
larger grid $[0,a]\times[0,b]\times[0,c]$, so the three immediate successors
of every point of $B$ are also present.

## 2. First exact Newton-polyhedron decision

For the exponent vectors $A=\{a_1,\ldots,a_m\}$ of the minimal generators,
the first program uses

\[
u\in\operatorname{NP}(I)
\iff
\exists\lambda\in\mathbb R_{\geq0}^m:
\sum_i\lambda_i=1,
\quad \sum_i\lambda_i a_i\leq u
\quad\text{coordinatewise}.
\]

The feasible set is a compact rational polytope. If nonempty, it has a vertex.
Inside the affine hyperplane $\sum_i\lambda_i=1$, a vertex has $m-1$
linearly independent active inequalities chosen from the $m$ nonnegativity
and three coordinate inequalities. `enumerate_lp.py` tries every such choice,
solves the resulting square system by exact rational Gaussian elimination, and
then checks all original inequalities. Consequently it returns true exactly
when the displayed feasible set is nonempty.

It obtains $v(I)$ and $v(\overline I)$ by enumerating all $u\in B$ and
testing exactly whether $u\notin J$ while $u+e_1,u+e_2,u+e_3\in J$.

## 3. Independent exact Newton and v-number decisions

The second program uses the dual characterization

\[
u\in\operatorname{conv}(A)+\mathbb R_{\geq0}^3
\iff
w\mathbin{\cdot}u\geq\min_{a\in A}w\mathbin{\cdot}a
\quad\text{for every }w\in\mathbb R_{\geq0}^3.
\]

Necessity is direct. Sufficiency follows from separation: a separating linear
functional must be nonnegative on the recession cone
$\mathbb R_{\geq0}^3$. To reduce the universal dual test finitely, subdivide
the nonnegative $w$-orthant by the hyperplanes
$w_k=0$ and $w\cdot(a_i-a_j)=0$. On each resulting cone, the minimum is a
fixed linear form. Every extreme ray is the intersection of at least two of
these boundary hyperplanes. `enumerate_facets.py` forms all pairwise integer
cross products of their normals, normalizes every nonzero nonnegative ray, and
tests the dual inequality there. An arbitrary $w$ is a nonnegative
combination of the extreme rays of a cone containing it, so these exact integer
tests are necessary and sufficient.

This program does not use the neighbor-test implementation for both v-numbers.
For the input ideal it uses the closed-form socle

- $\{(a-1,b-1,c-1)\}$ if there is no mixed generator;
- for mixed exponent $q=(r,s,t)$, the points obtained, for each $q_i>0$,
  by putting coordinate $i$ equal to $q_i-1$ and the other two coordinates
  at their box maxima.

These are precisely the maximal points of $B$ that fail to dominate $q$.
For $\overline I$, the program constructs its complete standard down-set in
$B$ and finds its globally maximal elements by pairwise dominance, rather
than by checking three successors. The minimum total degree in either socle is
the required v-number.

## 4. Exhaustion result and reproducibility

Each exact method evaluated 31,922 expanded-grid exponents across all 517
ideals, containing all 13,270 possible standard-box exponents. The comparison
program found equality of every serialized input-ideal membership bit, every
integral-closure membership bit, both full socle lists, and both v-numbers.
The canonical record-list SHA-256 is

`ffdd460fb7212673c7d8168be996eb8498d0ad1654527ce3590164e718c4753c`.

The common distribution of $v(\overline I)-v(I)$ is

| difference | -6 | -5 | -4 | -3 | -2 | -1 | 0 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| ideals | 1 | 6 | 19 | 82 | 194 | 124 | 91 |

There are no positive differences. As a nonvacuity control, both implementations
also evaluate the nearby degree-five ideal
$(x^2,y^2,z^5,xyz)$ and independently return
$v(I)=2$, $v(\overline I)=3$, so the same tests detect the known direction
of failure just beyond the bounded class.

Run from the project directory with Python 3:

```text
python3 evidence/enumerate_lp.py evidence/lp_results.json
python3 evidence/enumerate_facets.py evidence/facet_results.json
python3 evidence/compare_runs.py evidence/lp_results.json evidence/facet_results.json evidence/verification.json
```

`verification.json` records the output hashes and the frozen `source.md` hash.
The computation depends only on integer exponent divisibility, rational convex
feasibility, and monomial socles, so the conclusion holds over every field and
has no characteristic dependence.
