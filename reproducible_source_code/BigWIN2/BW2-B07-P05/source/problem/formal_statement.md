# Formal statement (locked 2026-08-30)

## Primary quantity

Let \(S=[0,1]^2\subset\mathbb R^2\). For an ordered ten-tuple
\(p=(p_1,\ldots,p_{10})\in S^{10}\), where \(p_i=(x_i,y_i)\), put

\[
 a(p)=\min_{1\le i<j<k\le 10}
 \frac12\left|
 (x_j-x_i)(y_k-y_i)-(x_k-x_i)(y_j-y_i)
 \right|.
\]

Define

\[
 \Delta_{10}=\max_{p\in S^{10}} a(p).
\]

Equivalently, the maximum may be taken over ten-element subsets
\(P\subset S\): any tuple with a repeated point has \(a(p)=0\), whereas an
explicit configuration has \(a(p)>0\). Triangles are indexed by unordered
triples of distinct indices; collinear triples have area zero.  The boundary
of \(S\) is allowed.

The maximum exists. Indeed \(S^{10}\) is compact and \(a\) is the minimum of
finitely many continuous functions.  Relabelling the points and applying any
of the eight Euclidean symmetries of the square leave \(a\) invariant.

## Research target

Determine the exact real number \(\Delta_{10}\), by giving both:

1. an exact ten-point configuration of minimum triangle area \(A\); and
2. an unrestricted proof that every ten-point configuration in \(S\) has a
   triangle of area at most \(A\).

The decimal in the source statement is contextual evidence for a known lower
bound, not a formal assertion that it equals (\Delta_{10}).

## Named incumbent

Let \(z_0\) be the unique real root in \((3/10,1/3)\) of

\[
 f(z)=12z^3-27z^2+20z-4,
\]

and set

\[
 x_0=z_0/2,\qquad y_0=(1-z_0)(1-2z_0),\qquad
 A_0=\frac{5z_0^2}{8}-\frac{z_0^3}{2}.
\]

The Comellas--Yebra configuration is

\[
\begin{split}
C(x_0,y_0,z_0)=\{&(x_0,0),(1-y_0,0),(0,x_0),(1,y_0),
 (1-z_0,z_0),\\
 &(z_0,1-z_0),(0,1-y_0),(1,1-x_0),(y_0,1),(1-x_0,1)\}.
\end{split}
\]

The lower-bound claim to be certified separately is
\(a(C(x_0,y_0,z_0))=A_0\), hence \(\Delta_{10}\ge A_0\). Equality
\(\Delta_{10}=A_0\) remains the unrestricted target and is not assumed.

## Edge and endpoint conventions

- Coordinates and all algebraic inequalities are over the real numbers.
- Coincident points, collinear triples, square corners, and all boundary
  strata are included in the compact formulation.
- A numerical solver status, a finite search, or an optimum within a
  symmetry ansatz does not establish the unrestricted upper bound.
