# Breaker record

The breaker attempted the following genuinely different attacks.

## D1: hidden higher-support generic DP

For a length-two path \(p-q-r\), the exact C3 coefficient matrix has
determinant
\[
-(a_p-d_{q,p})(a_r-d_{q,r})(2a_q-d_{p,q}-d_{r,q}).
\]
Thus a 3-support DP does occur on the proper special hypersurface
\(2a_q=d_{p,q}+d_{r,q}\), but not at the generic point.  This is an important
near-counterexample and confirms that the special-subclass exclusion is
essential.  Independent SymPy audit:
`code/audit/check_three_vertex_boundary.py`.

## D2: Whitney/cycle-matroid collision

The breaker treated each DP configuration as the graphic matroid of the cone
over the tree and searched for nonisomorphic order-nine trees with indistinct
cycle data.  For every element it counted, exactly, the number of circuits of
each cardinality containing that element and then sorted these profiles.  All
47 order-nine signatures are distinct.  The same holds at every order 2--8.
This is a separate invariant from the proof's triangle reconstruction.

## D3: ambiguity between a leaf coordinate and an edge DP

Both have degree one in the triangle hypergraph.  Swapping them inside a
pendant triple merely exchanges which degree-one object is called the leaf and
which is called the edge; the reconstructed unlabeled graph still attaches
one leaf to the same internal vertex.  No nonisomorphic tree results.

## D4: singular and zero-coefficient strata

Vanishing edge-DP coefficients, coincident parameters, singular interaction
matrices, and the hypersurface in D1 can create extra or parametric families
of DPs.  They are genuine special strata.  They do not define birational
equivalence of the full \((3n-2)\)-parameter general classes and hence are not
counterexamples to the formal endpoint.

## Breaker conclusion

No generic counterexample survived exactification.  The closest attack
produced only an excluded codimension-one special family.
