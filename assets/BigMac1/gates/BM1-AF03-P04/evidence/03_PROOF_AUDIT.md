# Proof audit

Status: **PASS** (serial referee role; not external peer review).

Audit date: 2026-08-29.

## Reconstruction from definitions

1. Rewrote source formula (1.2) as
   \(R=\sum_{i,j}(r^{(a_{ij})})^{j,i}\) in
   \(\mathfrak g^{\oplus n}\otimes\mathfrak g^{\oplus n}\).
2. Expanded each of
   \([R_{12},R_{13}]\), \([R_{12},R_{23}]\), and
   \([R_{13},R_{23}]\) without assuming the intended conclusion.
3. Used only the defining direct-sum bracket to obtain the three support
   conditions.  The colors at output support \((j,i,k)\) are respectively
   \((a_{ij},a_{kj})\), \((a_{ij},a_{ki})\), and
   \((a_{kj},a_{ki})\).
4. Hence the coefficient is exactly
   \(T(a_{ij},a_{kj},a_{ki})\), with no sign or transpose change.
5. The array axiom at the ordered triple \((k,i,j)\) gives
   \(a_{kj}\in\{a_{ki},a_{ij}\}\), exactly the middle-color condition.

## Adversarial points checked

- **Repeated component indices:** permitted because the three target tensor
  factors are separate.  No independence of the maps \(\Phi_{j,i,k}\) is
  used.
- **Diagonal and constant cases:** no division, distinctness, genericity, or
  nonzero hypothesis occurs.
- **Infinite color set:** only the finite image of the matrix is used.
- **Field and dimension:** the manuscript retains the source's
  characteristic-zero convention and imposes no finite-dimensionality.
- **Definition match:** v1 Conjecture 1.4 and v2 Conjecture 1.5 have the same
  mathematical endpoint; only numbering changed.
- **Scope:** the identity is uniform in \(n\), so it strictly implies the
  requested \(n=5\) case.

## Independent computational cross-checks

- `verifier/verify_symbolic_expansion.py` starts from all ordered pairs of
  terms of \(R\), rather than importing the displayed component formula.
- `verifier/verify_certificate.py` independently reconstructs all finite
  equality types through \(n=5\).
- Six malformed/corrupt certificate variants are rejected fail closed.
- An integral noncommutative \(\mathfrak{sl}_2\) breaker found no residual in
  562,625 ordered size-five components.

## Gap disposition

All fatal and major items G01--G06 in `proof/gap_ledger.md` are closed.  The
finite enumeration is ancillary and is not used to justify the all-\(n\)
theorem.

## Proof assistant

No Lean, Coq, Isabelle, or other proof assistant was used.  No formalization
claim is made.
