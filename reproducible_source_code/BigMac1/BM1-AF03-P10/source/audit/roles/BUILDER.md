# Builder record

## Proposed endpoint

The builder proves the full generic conjecture for every \(n\ge2\), not only
the requested order-nine case.  The dependency chain is L01--L08 in
`proof/proof_dag.md`.

## Critical construction

1. Express every generic tree-matrix entry by the first edge seen in its
   column.
2. Use C2 to force DP support connected.
3. Use the three C3 equations on a length-two path to exclude every connected
   support of size at least three at the generic point.
4. Normalize the remaining \(2n-1\) projective forms to the reduced incidence
   configuration of the cone over the tree.
5. Reconstruct the tree from the three-element projective circuits.

## Builder self-check

No numerical inference, compactness claim, optimization step, or division by
a parameter specialization is used.  All nonzero statements occur in a
rational function field on algebraically independent parameters.  The proof
states and excludes the special algebraic boundary where extra DPs arise.
