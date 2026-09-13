# Formal statement

## Ambient objects

Fix an integer \(n\ge 2\), and let \(T=(V,E)\) be a finite simple unrooted
tree with \(V=\{1,\ldots,n\}\).  Work over a characteristic-zero field; the
original dynamical systems are real, while the generic class is most cleanly
represented over the rational function field
\[
K_T=\mathbb Q(a_i\ (i\in V),b_e,c_e\ (e\in E)).
\]
For an oriented notation \(e=(i,k)\), \(i<k\), set
\(A_{ii}=a_i,A_{ik}=b_e,A_{ki}=c_e\).  The remaining entries of \(A_T\)
are the unique entries satisfying
\[
A_{ij}=A_{kj}\qquad(e=\{i,k\}\in E,\ j\notin\{i,k\}).
\]
The homogeneous Lotka--Volterra vector field attached to \(T\) is
\[
F_T(x)=\operatorname{diag}(x)A_Tx\in K_T[x_1,\ldots,x_n]^n.
\]
It is a \((3n-2)\)-parameter *generic class*, not a claim about every special
real specialization of those parameters.

For each edge \(e=\{i,k\}\), the additional linear Darboux polynomial is,
up to nonzero scalar,
\[
P_e=(A_{ki}-A_{ii})x_i+(A_{kk}-A_{ik})x_k.
\]
The generic nondegeneracy convention requires both displayed coefficients to
be nonzero and excludes specializations that create extra or
positive-dimensional families of linear Darboux polynomials.  The \(n\)
coordinate forms \(x_i\) and the \(n-1\) forms \(P_e\) are the distinguished
generic linear Darboux polynomials.

## Linear and class equivalence

For fixed parameter values over a common extension field, two homogeneous
quadratic vector fields \(F,G\) are linearly conjugate if there is
\(M\in\mathrm{GL}_n\) such that
\[
G(y)=M F(M^{-1}y).
\]
For generic tree classes, a parameter remapping means a birational
identification of their \((3n-2)\)-dimensional parameter fields.  We say the
classes \(LV(T_1)\) and \(LV(T_2)\) are *LV-equivalent* if, after such a
generic parameter identification, their generic vector fields are linearly
conjugate.  Equivalently for the finite procedure used in the source paper:
choose any \(n\) linearly independent generic linear Darboux forms as new
coordinates; the supports of the remaining \(n-1\) forms define an
LV-equivalent hypergraph.  Special lower-dimensional parameter strata do not
witness equivalence of general classes.

## Target endpoint

The order-nine finite endpoint is
\[
\forall T_1,T_2\text{ trees on nine vertices},\qquad
LV(T_1)\sim LV(T_2)\Longrightarrow T_1\cong T_2.
\]
Here \(\cong\) is ordinary unlabeled graph isomorphism.  There are no
zero-vertex, one-vertex, disconnected, looped, or multiple-edge cases in this
endpoint.  Relabeling vertices, rescaling individual Darboux forms, and
orientation choices for edges are normalizations, not distinct systems.

## Relation to the general conjecture

The general conjecture has the same implication for every integer \(n\ge2\).
A proof only for all 47 unlabeled trees of order nine is a certified finite
result, not a proof for arbitrary \(n\).  Conversely, one exact pair of
nonisomorphic order-nine trees together with a generic birational parameter
map and an invertible conjugating matrix disproves both the order-nine
endpoint and the general conjecture.

## Source-boundary correction

The prompt's phrase "允许的 linear transformation 与参数重映射" is made
precise above.  The latest arXiv v4 and the journal article explicitly study
intersections of *general* solution classes and disclaim classification of
special subclasses.  Therefore an isolated degenerate specialization cannot
serve as a counterexample to Conjecture 12.
