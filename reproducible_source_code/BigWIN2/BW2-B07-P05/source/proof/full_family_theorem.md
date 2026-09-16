# Exact optimum of the full Comellas--Yebra parameter cube

## Statement

For (x,y,z\in[0,1]), let (C(x,y,z)) be the ordered ten-point
configuration

\[
\begin{split}
(&(x,0),(1-y,0),(0,x),(1,y),(1-z,z),(z,1-z),\\
 &(0,1-y),(1,1-x),(y,1),(1-x,1)).
\end{split}
\]

Repeated points are permitted in this parametrized family and simply give
minimum area zero.  Write (\delta(x,y,z)) for the minimum of its 120
unsigned triangle areas.  Let (z_0\in(3/10,1/3)) be the root of

\[
f(z)=12z^3-27z^2+20z-4
\]

and put

\[
x_0=z_0/2,\qquad y_0=(1-z_0)(1-2z_0),\qquad
A_0=\frac{5z_0^2-4z_0^3}{8}.
\]

**Partial theorem.**

\[
\max_{(x,y,z)\in[0,1]^3}\delta(x,y,z)=A_0.
\]

The real number (A_0) is the unique real root of

\[
3456A^3-1764A^2+268A-9=0
\]

and

\[
A_0=0.04653741958254177256161176810014551328871\ldots.
\]

The four parameter triples obtained from
((x_0,y_0,z_0)) by independently applying

\[
(x,y,z)\mapsto(1-y,1-x,z),\qquad
(x,y,z)\mapsto(x,y,1-z)
\]

are exactly the equality triples in the parameter cube.

This theorem concerns a proper three-dimensional family.  It does **not**
prove (\Delta_{10}=A_0) for arbitrary ten-point configurations.

## 1. Exact preliminaries

On ([0,1/2]),

\[
f'(z)=36z^2-54z+20>0.
\]

Moreover

\[
 f(31/100)=-4651/125000<0,qquad
 f(8/25)=444/15625>0.
\]

Thus (31/100<z_0<8/25).  Define the doubled target

\[
t_0=2A_0=\frac{5z_0^2-4z_0^3}{4}.
\]

The function ((5z^2-4z^3)/4) is increasing on ([0,1/2]), and direct
evaluation at (31/100) and (8/25) gives

\[
\frac9{100}<t_0<\frac1{10}.
\]

In particular, (9/200<A_0).

## 2. Normalization of the full cube

As unordered point multisets, direct inspection gives the two identities

\[
C(x,y,z)=C(1-y,1-x,z),\qquad C(x,y,z)=C(x,y,1-z).
\]

The first merely exchanges four boundary pairs, and the second exchanges the
two nonboundary points.  Hence every member of the full parameter cube has a
representative satisfying

\[
0\le z\le\frac12,\qquad x+y\le1. \tag{N}
\]

We split this normalized cell into three overlapping closed parts:

\[
x\ge y;\qquad x\le y\le z;\qquad x\le y\text{ and }z\le y. \tag{S}
\]

These parts cover (N), including every boundary case.

## 3. The ordered cell

Assume (0\le x\le y\le z\le1/2).  Three actual doubled triangle areas,
from triples (012,145,058), are

\[
P=x(1-x-y),\quad Q=y(1-2z),\quad
R=z(1-x+y)-y.
\]

They are nonnegative under the stated order.  Put
(t=\min(P,Q,R)).  We prove (t\le t_0).

There is nothing to prove if (t<t_0).  Otherwise (0<z<1/2).  Put

\[
d=1-2z,\qquad L=\frac{t}{d}.
\]

From (Q\ge t), (L\le y).  Replacing (y) by (L) can only increase
both (P) and (R), so

\[
P(x,L)\ge t,\qquad R(x,L,z)\ge t.
\]

The latter inequality gives

\[
x\le U=1-\frac{t+(1-z)L}{z}.
\]

The vertex of the concave quadratic (P(x,L)=x(1-x-L)) is
((1-L)/2), and direct simplification gives

\[
\frac{1-L}{2}-U=
\frac{N}{2z(1-2z)},\qquad
N=t(4-7z)+2z^2-z.
\]

Because (4-7z>0) and (t\ge t_0), it suffices to bound

\[
N\ge 2z^2-(1+7t_0)z+4t_0.
\]

The discriminant of the quadratic on the right is

\[
49t_0^2-18t_0+1
<49(1/10)^2-18(9/100)+1=-13/100<0.
\]

Therefore (U) lies strictly before the vertex.  Since (x\le U) and
(P(x,L)\ge t), monotonicity up to the vertex implies (P(U,L)\ge t).
Another direct simplification is

\[
P(U,L)-t=\frac{tH}{z^2(1-2z)},
\quad H=(6z-4)t+2z^3-5z^2+2z.
\]

Thus (H\ge0).  Since (6z-4<0),

\[
t\le h(z):=\frac{2z^3-5z^2+2z}{4-6z}.
\]

Finally,

\[
h'(z)=-\frac{f(z)}{2(3z-2)^2}.
\]

The polynomial (f) is strictly increasing on ([0,1/2]) and changes sign
only at (z_0).  Hence (h) has its unique maximum there.  Reduction by
(f(z_0)=0) gives (h(z_0)=t_0), proving (t\le t_0).

At equality, every inequality in the chain is forced to equality.  The strict
vertex inequality gives (x=U), strict decrease in the substituted (y)
gives (y=L), and the unique maximum of (h) gives (z=z_0).  Consequently
(x=x_0) and (y=y_0).  The exact 120-triangle certificate verifies that
(C(x_0,y_0,z_0)) actually has minimum area (A_0).

## 4. The cell (x\ge y)

Assume (N) and (x\ge y).  Then (0\le y,z\le1/2).  Three actual doubled
triangle areas, from triples (145,014,149), are

\[
q=y(1-2z),\qquad w=z(1-x-y),\qquad |q-w|.
\]

They are nonnegative except for the displayed absolute value.  If all three
were greater than (T=9/100), then one of (q,w) would exceed (2T), so
(qw>2T^2).  On the other hand,

\[
qw=yz(1-2z)(1-x-y)
\le y(1-2y)z(1-2z)\le\frac1{64},
\]

because (u(1-2u)\le1/8) on ([0,1/2]).  But

\[
2T^2=81/5000>1/64,
\]

a contradiction.  This cell therefore contains a triangle of area at most
(9/200<A_0).

## 5. Exact finite cover of the remaining nonordered cell

It remains to treat

\[
D=\{(x,y,z):0\le x,y\le1, 0\le z\le1/2, x\le y, z\le y, x+y\le1\}.
\]

The machine-readable certificate `certificates/family_cover.json` partitions
the root box into a complete dyadic binary tree.  It has 2,893 nodes and 1,447
leaves, of maximum depth 20.  At 278 leaves the entire box misses (D), as
proved by one of

\[
\underline x>\overline y,qquad
\underline z>\overline y,qquad
\underline x+\underline y>1.
\]

At each of the other 1,169 leaves, the certificate names one of the 120
triangles.  Exact rational interval evaluation puts its signed determinant
throughout ([-9/100,9/100]).  Hence its area is at most (9/200<A_0).

The independent checker `certificates/verify_family_cover.py` validates that
the leaf paths form a complete prefix tree, reconstructs every dyadic box,
re-derives each named determinant from the shoelace formula, changes to local
box coordinates, and bounds it by exact tensor-product Bernstein
coefficients.  It does not use the generator's termwise global-coordinate
interval evaluator.

This closes (D) exactly.  Combining Sections 2--5 proves the stated maximum
over the full parameter cube.  The two normalization involutions give the
four equality parameter triples.

## 6. Evidence boundary

The result proves exact optimality only inside the displayed affine
three-parameter ansatz.  There is no proved reduction taking an arbitrary
ten-point configuration in the square to this ansatz.  Therefore the fatal
gap for the unrestricted equality (\Delta_{10}=A_0) remains open.
