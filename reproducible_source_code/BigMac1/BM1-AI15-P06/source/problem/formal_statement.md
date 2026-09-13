# Formal statement

## Definitions and quantifiers

For an integer \(n\ge 1\), a finite set \(S\subset\mathbb R^n\) is
**equilateral in \(\ell_1^n\)** if there is a real number \(\delta>0\) such
that

\[
  \sum_{k=1}^n |x_k-y_k|=\delta
  \qquad\text{for every two distinct }x,y\in S.
\]

Write

\[
e(\ell_1^n)=\max\{|S|:S\subset\mathbb R^n\text{ is finite and
equilateral in }\ell_1^n\}.
\]

This maximum is well defined.  After normalizing the common distance to one
and translating one point to the origin, all centers lie in the unit ball.
The open norm balls of radius \(1/2\) about them are pairwise disjoint and
lie in the ball of radius \(3/2\).  Comparing Lebesgue volumes gives the
elementary finite bound \(|S|\le3^n\).

The target decision problem is

\[
  \nexists x_1,\ldots,x_{11}\in\mathbb R^5\quad
  \forall\,1\le r<s\le 11:\quad
  \|x_r-x_s\|_1=1. \tag{T}
\]

The common distance is written as \(1\) without loss of generality.  The
points in (T) are automatically pairwise distinct.  The standard cross
polytope \(\{\pm e_1,\ldots,\pm e_5\}\) has all pairwise \(\ell_1\)-distances
equal to \(2\), so \(e(\ell_1^5)\ge 10\).  By the preceding finiteness
argument, (T) is equivalent to the assertion \(e(\ell_1^5)=10\).

The literal source also states the all-dimensional Kusner conjecture
\(e(\ell_1^n)=2n\).  This project asks only for its \(n=5\) instance.

## Normalizations

Given a putative configuration of common distance \(\delta>0\), translate
all points by \(-x_{11}\) and multiply all coordinates by \(1/\delta\).
Thus one may impose

\[
  x_{11}=0,\qquad \|x_r-x_s\|_1=1\quad(r<s).
\]

Simultaneous relabeling of the eleven points, permutation of the five
coordinates, reversal of any coordinate, and coordinatewise translation are
symmetries.  General rotations are not \(\ell_1\)-isometries and are not used.

## Exact finite order-type formulation

Let \(m=11\).  For each coordinate \(k\), choose a permutation
\(\pi_k\in S_m\) and nonnegative gaps \(g_{k,t}\ge0\),
\(1\le t<m\).  Define the cut

\[
C_{k,t}=\{\pi_k(1),\ldots,\pi_k(t)\}.
\]

Then (T) has a solution if and only if some five permutations and fifty
nonnegative real gaps solve the rational linear system

\[
\sum_{k=1}^{5}\sum_{t=1}^{10}
  g_{k,t}\,\mathbf 1\bigl(|\{r,s\}\cap C_{k,t}|=1\bigr)=1
  \qquad(1\le r<s\le11). \tag{LP}
\]

For the forward implication, sort the eleven values in each coordinate and
take consecutive gaps; ties are represented by zero gaps.  For the reverse
implication, set the value at \(\pi_k(1)\) to zero and recover successive
coordinate values by cumulative sums of the gaps.  Hence no generic-position
assumption is present.  Because (LP) has integer coefficients, every
nonempty branch has a rational basic feasible solution.  It follows in
particular that a real counterexample exists if and only if a rational one
exists.  Simultaneous point relabeling permits \(\pi_1=\mathrm{id}\).

## Edge cases

- The case \(\delta=0\) is excluded; otherwise repeated points would give a
  vacuous degenerate configuration.
- Coordinate ties are allowed and correspond exactly to zero gaps in (LP).
- A coordinate may be constant; then all ten of its gaps are zero.
- Boundary points of the nonnegative LP cone are retained.
- The project does not assume integral coordinates.  Rational coordinates
  are a consequence of rational-polyhedron feasibility, not an extra search
  restriction.
