# Structural reduction and general-proof route

## Proven reductions

1. **Standardization.** Every finite alphabet of cardinality \(n\) is carried
   order-preservingly to \([n]\). All four K-Knuth moves depend only on strict
   order and equality, so standardization preserves equivalence and shape.
2. **Finite staircase.** In box \((i,j)\), strict row/column increase forces
   \(T(i,j)\ge i+j-1\). Hence a tableau on \([n]\) has shape inside
   \(\delta_n=(n,n-1,\ldots,1)\).
3. **Fixed boundary.** Proposition 2.43 of Gaetz et al. says equivalent initial
   tableaux have the same outer hook, including its entries. Thus every shape
   in one class has the same first-row length and the same number of rows. All
   shape variation is strictly southeast of box \((1,1)\), outside the first
   row and first column.
4. **Order-convex reformulation.** A shape set \(S\) is interval-complete iff
   \(\uparrow S\cap\downarrow S\subseteq S\). This is the independent
   verifier's exact bitset predicate.

## Local shape-filling lemma suggested by the data

The finite data through \(n=8\) support the following local statement.

> **Prescribed-cover filling lemma (conjectural).** Let \(T\equiv_K U\) be
> straight increasing tableaux with
> \(\lambda=\operatorname{sh}(T)\subseteq
> \nu=\operatorname{sh}(U)\). For every addable box \(b\) of \(\lambda\)
> satisfying \(\lambda\cup\{b\}\subseteq\nu\), there is a tableau
> \(V\equiv_K T\) of shape \(\lambda\cup\{b\}\).

This formulation is not merely sufficient: together with iteration it is
equivalent to Conjecture 7.6. Necessity follows by taking the intermediate cover
shape. Sufficiency follows by selecting a saturated Young-lattice chain from
\(\lambda\) to any \(\mu\subseteq\nu\) and applying the lemma at each cover,
always retaining \(U\) as the upper endpoint.

The certificate proves the lemma for all classes with alphabet size at most
eight, including every prescribed addable box, because it proves the stronger
full interval statement there.

## Unresolved general step

K-jdt equivalence gives sequences of forward and reverse slides between the
endpoint tableaux, but the current argument does not control the net shape
after truncating or reordering such a sequence. A slide can change several
boxes, and a single K-Knuth move can change insertion shape by more than one
box (the source paper's Section 7.4 counterexample). Therefore neither an
unproved “one move, one box” premise nor naive path interpolation can establish
the prescribed-cover lemma. This is the precise remaining gap for a general
proof.
