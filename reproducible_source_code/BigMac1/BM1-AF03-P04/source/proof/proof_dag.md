# Proof dependency graph

1. **D1 (direct-sum commutator).** Distinct summands of
   \(\mathfrak g^{\oplus n}\) commute.
2. **D2 (three expansions).** Apply D1 separately to
   \([R_{12},R_{13}]\), \([R_{12},R_{23}]\), and
   \([R_{13},R_{23}]\).
3. **D3 (component identity).** Sum D2 to obtain
   \[
   \operatorname{CYB}(R)=\sum_{j,i,k}\Phi_{j,i,k}
   T(a_{ij},a_{kj},a_{ki}).
   \]
4. **D4 (transitivity match).** The array axiom at \((k,i,j)\) gives
   \(a_{kj}\in\{a_{ij},a_{ki}\}\).
5. **D5 (relation substitution).** The transitive-CYBE hypothesis kills
   every summand of D3, using D4.
6. **Endpoint.** \(\operatorname{CYB}(R)=0\) for every \(n\ge1\), hence for
   \(n=5\).

Independent checks:

- `verifier/verify_symbolic_expansion.py` reconstructs D2 from all ordered
  pairs of the \(n^2\) terms of \(R\).
- `verifier/verify_certificate.py` reconstructs the finite array types and
  checks D4 for every residual component through \(n=5\).
- `experiments/exact_sl2_breaker.py` evaluates a noncommutative integral
  \(\mathfrak{sl}_2\) family on all one- and two-color \(n=5\) types.
