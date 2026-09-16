# Proof and reproducibility audit

Audit date: 2026-08-30 UTC.

## Statement reconstruction

The source problem asks for the unrestricted value \(\Delta_{10}\). The
proved endpoint is narrower:

\[
\max_{(x,y,z)\in[0,1]^3}\delta(C(x,y,z))=A_0.
\]

The manuscript title, abstract, theorem, introduction, and limitations all
state that this is a proper three-parameter family and that unrestricted
global optimality remains open. No reduction from arbitrary configurations is
asserted.

## Human proof audit

- The two point-set involutions were checked symbolically and cover every
  parameter triple by \(z\le1/2,\ x+y\le1\).
- The three closed cells cover that normalized domain, including equality
  boundaries.
- On the ordered cell, \(P,Q,R\ge0\); every division occurs only after
  \(t\ge t_0>0\), so \(z>0\) and \(1-2z>0\).
- The substitution \(y\mapsto L\le y\) increases both \(P\) and \(R\).
- The vertex numerator has a positive quadratic lower bound because its
  discriminant is strictly negative.
- The sign reversal at \(6z-4<0\) is correct, and the derivative identity for
  the envelope has the correct sign.
- Equality forces the unique normalized triple; the two involutions give the
  four and only four cube representatives.
- The \(x\ge y\) product argument uses three literal triangles and the exact
  separator \(81/5000>1/64\).
- The remaining cell includes all endpoints and degeneracies; it is closed by
  the exact finite cover.

No fatal or major gap remains in the partial theorem. Fatal gap G01 remains
for the original unrestricted equality, and the paper does not claim to close
it.

## Exact computations

Clean commands executed successfully:

1. python3 certificates/verify_incumbent_stdlib.py
   — PASS; vector cross products, custom cubic-field arithmetic and rational
   root intervals; 120 triangles, 16 equalities, 104 strict inequalities, 23
   area forms.
2. python3 certificates/verify_incumbent_sympy.py
   — PASS; independent SymPy CRootOf/shoelace implementation with the same
   counts.
3. python3 certificates/verify_analytic_identities.py
   — PASS; six algebraic identities, root/order checks, and both parameter
   involutions.
4. python3 certificates/verify_family_cover.py
   — PASS; 2,893 nodes, 1,447 leaves, 1,169 triangle leaves, 278 infeasible
   leaves, maximum depth 20.
5. Regeneration of family_cover.json followed by byte comparison
   — PASS.

The cover generator uses termwise exact rational polynomial intervals. The
checker derives determinants through a different formula and uses local
tensor Bernstein coefficients. This separates discovery/generation from
certification.

## Diagnostics excluded from proof

The 340-start SLSQP search is labeled diagnostic, uses two floating-point
determinant evaluators, and makes no global claim. Its failure to beat the
incumbent is not used in the theorem.

No Lean, Coq, Isabelle, or other proof assistant was used.

Mathematical/reproducibility gate for the partial theorem: **PASS**.
