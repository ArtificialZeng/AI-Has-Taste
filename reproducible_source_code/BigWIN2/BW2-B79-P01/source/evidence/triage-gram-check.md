# Exact Gram screening calculation

This is a triage calculation, not a completed proof.

Put

\[
s_i=u_i^++u_i^-,\qquad d_i=u_i^+-u_i^-,\qquad
x_i=\langle u_i^+,u_i^-\rangle.
\]

Using only unit norm and the sixteen cross-pair entries (-1/3), direct
expansion gives

\[
\begin{aligned}
&\langle d_i,d_j\rangle=0 &&(i\ne j),\\
&\langle s_i,d_j\rangle=0 &&(1\le i,j\le4),\\
&d_i^2=2-2x_i,\qquad s_i^2=2+2x_i,\\
&\langle s_i,s_j\rangle=-4/3 &&(i\ne j).
\end{aligned}
\]

If the geometric halfspace lemma supplies (x_i\le-1), the four mutually
orthogonal (d_i) are positive and linearly independent.  They span a
positive (4)-space in (mathbb R^{4,1}), so their orthogonal complement is
a negative line.  Every (s_i) lies on this line.  Their common nonzero
pairwise product (-4/3) forces all four to have the same scalar coefficient
on that line, hence

\[
s_i^2=-4/3,qquad x_i=-5/3\quad(1\le i\le4).
\]

In facet order
((1+ ,1-,2+,2-,3+,3-,4+,4-)), the resulting matrix has diagonal (1),
opposite-pair entries (-5/3), and all other off-diagonal entries (-1/3).
Its spectrum is

\[
8/3\ (\text{multiplicity }4),\qquad
-8/3\ (\text{multiplicity }1),\qquad
0\ (\text{multiplicity }3).
\]

Thus it has rank (5) and Lorentzian signature ((4,1)) on the span.  It is
exactly the Gram matrix of the explicit endpoint normals

\[
w_i^\pm=(1/\sqrt3,\ \pm(2/\sqrt3)e_i),
\]

whose oriented halfspaces cut out the Klein cube ([-1/2,1/2]^4).

Remaining proof obligations are not encoded by the matrix arithmetic.  The
later bounded check in `triage-226b85b4cb78.md` supplies item 1 by a Lorentz
normal-form nesting argument; items 2--3 remain for the research phase:

1. rule out the (x_i\ge1) orientation for two disjoint supporting
   hyperplanes using irredundancy/nonempty interior;
2. construct the Lorentz isometry from equality of the spanning Gram
   configurations, including the three linear relations;
3. verify time orientation and equality of the complete halfspace
   intersections, rather than merely congruence of unoriented hyperplanes.
