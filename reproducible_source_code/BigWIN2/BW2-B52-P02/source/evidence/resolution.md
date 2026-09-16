# Candidate resolution: \(\eta(P_3\square P_4)=19\)

## Theorem

With induced Abelian Cayley embedding and \(\eta\) as defined in `problem.md`,

\[
  \eta(P_3\square P_4)=19.
\]

## Upper certificate

Use \(\Gamma=\mathbb Z_{19}\),

\[
  S=\{\pm1,\pm4\}=\{1,4,15,18\},\qquad
  f(i,j)=-i-4j\pmod {19}.
\]

In row-major order on \(\{0,1,2\}\times\{0,1,2,3\}\), the twelve labels are

\[
  (0,15,11,7,\ 18,14,10,6,\ 17,13,9,5),
\]

which are distinct.  `order19_certificate.py` checks all 66 unordered vertex
pairs with exact modular arithmetic.  The signed differences of the 17 grid
edges are exactly \(S\), whereas the signed differences of all 49 nonedges are

\[
 \{2,3,5,6,7,8,9,10,11,12,13,14,16,17\},
\]

which is disjoint from \(S\).  Thus the displayed labeling is an induced
embedding and \(\eta(P_3\square P_4)\leq19\).

## Lower bound through order 15

Orders below 12 fail injectivity.  At order 12 the image is the whole host,
but every Cayley graph is regular while the grid is not.  For order 13,
deleting the one omitted host vertex from a regular graph leaves degrees in
two consecutive values, whereas the grid has degrees 2, 3, and 4;
`z13_no_host.md` gives the proof and an exact exhaustive check.

At order 14 the grid would be obtained by deleting two vertices from a
\(d\)-regular graph.  Its minimum and maximum degrees force \(d=4\), but the
28-edge host retains at least 20 edges, not 17.  At order 15 the corresponding
range forces \(d\in\{4,5\}\); the handshake lemma excludes \(d=5\), and a
4-regular host retains at least 18 edges after three deletions.  These arguments
are detailed in `z14_no_host.md` and `z15_no_host.md`.

## Exhaustive lower certificate for orders 16--18

Let an order-\(n\) Cayley host have degree \(d=|S|\), let \(U\) be the
\(n-12\) omitted vertices, and let \(e(U)\) be the number of host edges within
\(U\).  Deleting \(U\) removes \((n-12)d-e(U)\) edges, so a necessary equation
is

\[
  17=\frac{nd}{2}-(n-12)d+e(U).
\]

The target's maximum degree gives \(d\geq4\).  This equation gives the complete
possibility list

\[
\begin{array}{c|c}
n& (d,e(U))\\ \hline
16&(4,1)\\
17&(4,3)\\
18&(4,5),(5,2).
\end{array}
\]

For order 17, \(d\) is even because nonzero elements occur in inverse pairs.
For order 18 the equation itself excludes \(d\geq6\).  The finite Abelian group
classification gives five group types at order 16, one at order 17, and two at
order 18, precisely those listed in `problem.md`.

The scripts `z16_exact_search.py`, `z17_exact_search.py`, and
`z18_exact_search.py` enumerate every remaining case as follows.

1. Translate the labeling so the fixed corner \((0,0)\) has label zero.  The
   omitted set therefore ranges over every subset of the nonidentity elements
   of the required size.
2. Form the negation orbits in each group and enumerate every union of orbits
   having one of the forced cardinalities \(d\).  This is exactly every legal
   inverse-closed connection set of that degree.
3. Retain only omitted sets having the forced value of \(e(U)\), then retain
   only induced images with degree multiset \((2^4,3^6,4^2)\) and with the
   identity of degree two.
4. Run exhaustive backtracking over bijections from the grid to the image,
   fixing the chosen corner at the identity.  A branch is rejected only for an
   exact degree mismatch or an adjacency/nonadjacency mismatch with an already
   assigned vertex.  Hence every corner-fixed graph isomorphism is considered.

At order 16 the five type-specific numbers of connection sets are
21, 33, 33, 125, and 1365.  Pairing each with all
\(\binom{15}{4}=1365\) omitted sets gives 2,152,605 normalized cases and
137,792 final isomorphism checks, with zero isomorphisms.  At order 17 the
28 connection sets and \(\binom{16}{5}=4368\) omitted sets give 122,304 cases
and 3,552 isomorphism checks, again with zero isomorphisms.  At order 18, each
of the two group types has 56 eligible connection sets and
\(\binom{17}{6}=12376\) omitted sets; the combined 1,386,112 cases lead to
11,028 isomorphism checks and zero isomorphisms.  The JSON records contain all
type- and degree-specific counts.

The translation normalization loses no embedding because translation preserves
all group differences.  Image selection plus graph isomorphism represents all
injections onto that image.  Thus no Abelian Cayley host of order at most 18
works.  Combined with the order-19 certificate, this proves the theorem.

## Reproducibility and scope

All arithmetic is exact and the scripts use only the Python standard library.
The enumerations establish only the finite lower certificate described above;
their correctness and completeness remain subject to fresh mathematical and
computational audit.  The cited primary source supplies the definition,
difference criterion, prior order-20 construction, and surrounding grid problem,
but does not state this exact value.
