# A 98-clause linear monotone NAE-4 equality gadget

## Explicit incidence structure

Let the 40 vertices be the one-dimensional subspaces of
\(\mathbb F_3^4\), represented by the lexicographically ordered normalized
vectors whose first nonzero coordinate is 1.  Every two-dimensional subspace
gives a four-point projective line.  These 130 lines form a linear 4-uniform
hypergraph: two different two-dimensional subspaces share at most one
one-dimensional subspace.

Order the lines lexicographically by their four point indices.  Let \(K\) be
the 99-line subhypergraph with line-index set

```text
0,2,3,4,5,6,7,8,9,11,12,13,17,18,19,20,21,22,24,26,27,28,30,31,
33,34,35,37,38,39,40,41,43,44,46,47,49,50,51,52,54,56,57,60,61,
63,64,65,66,67,68,70,71,73,74,75,76,77,80,81,82,83,84,85,88,91,
92,93,94,95,96,97,98,99,100,101,102,103,105,106,108,109,110,111,
112,113,114,115,116,117,118,119,120,121,122,123,127,128,129.
```

The first line is \(L=\{0,1,2,3\}\).  Define \(G=K\setminus\{L\}\).
The project-local script `evidence/gadget_certificate.py` independently
generates the projective points and lines from finite-field arithmetic, fixes
the displayed index set, and verifies all assertions below without a
third-party package.

## Exact local certificate

The script's exhaustive two-colour DPLL proves that \(K\) has no NAE
colouring.  Its pruning rule is exact: a clause already containing both colours
is satisfied; a clause with three assigned vertices of one colour forces its
last vertex to the other colour; every remaining unresolved variable is
branched both ways.  Consequently the reported UNSAT result covers all
\(2^{40}\) total assignments, with only sound forced branches suppressed.

On the other hand, the same verifier exhibits a colouring of \(G\) in which
all four vertices of \(L\) are 0.  Its complement gives the all-1 colouring.
If a colouring of \(G\) gave a nonmonochromatic pattern on \(L\), then \(L\)
itself would be NAE and this colouring would satisfy every clause of \(K\), a
contradiction.  Hence the exact terminal projection of \(G\) on
\((0,1,2,3)\) is

\[
\{(0,0,0,0),(1,1,1,1)\}.
\]

Thus, after identifying terminal 0 with a variable \(x\), terminal 1 with a
fresh occurrence variable \(y\), and treating terminals 2 and 3 as local
auxiliaries, \(G\) is an equality gadget: its satisfying assignments project
onto exactly \(x=y\).  Every clause has four distinct unnegated variables, and
any two gadget clauses intersect in at most one variable.

## Global replacement and composition

For every indexed occurrence of an original variable \(x\), introduce a fresh
variable \(y\), use \(y\) in the corresponding copied input clause, and attach
a fresh copy of \(G\) with terminals 0 and 1 identified with \(x,y\).  All
other vertices of this copy are fresh.  Do this for every occurrence, not only
the offending ones.

The resulting formula is linear:

1. copied input clauses are pairwise disjoint because all occurrence variables
   are fresh;
2. within one gadget, projective linearity gives intersections of size at most
   one;
3. gadgets for different original variables are disjoint;
4. two gadgets for the same original variable share only that variable; and
5. a copied input clause and any gadget clause share at most its one occurrence
   variable.

For an original satisfying assignment, assign each occurrence copy the value
of its original variable and use the displayed zero-terminal gadget witness or
its complement.  This extends the assignment and leaves every copied input
clause with exactly its original four values.  Conversely, every transformed
satisfying assignment has \(y=x\) in each occurrence gadget, so restriction to
the original variables satisfies every original clause.  This proves equality
of the projected satisfying-assignment sets, not merely equisatisfiability.

The certificate also instantiates two indexed clauses sharing respectively
2, 3, and 4 variables.  It mechanically checks every pair of transformed
clauses for linearity and checks the entire original truth table against the
canonical gadget extensions.

For each occurrence, the construction introduces 39 fresh variables (the
occurrence variable and the other 38 projective points) and 98 gadget clauses.
For an input with \(m\) clauses there are \(4m\) occurrences, so the output has
\(n+156m\) variables and \(m+392m=393m\) clauses.  Generation uses fixed
lookup data per occurrence and therefore takes linear time.  The requested
absolute local bound may be taken as \(B=98\).
