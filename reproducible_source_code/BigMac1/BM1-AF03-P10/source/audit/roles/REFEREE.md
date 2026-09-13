# Referee reconstruction from definitions

## Scope reconstructed

The theorem concerns generic \((3n-2)\)-parameter classes over a
characteristic-zero rational function field.  It does not concern arbitrary
special real parameter instances.

## Checks

1. **Matrix parametrization.**  Removing column vertex \(j\), the row-equality
   relations make column \(j\) constant on each component of \(T-j\).  This
   verifies Lemma 1 without using the intended conclusion.
2. **C2 support test.**  Two support components separated at \(j\) see two
   independent directed-edge parameters in column \(j\), so disconnected
   support is impossible generically.
3. **C3 obstruction.**  The three equations on \(p-q-r\) imply the nonidentity
   \(d_{p,q}+d_{r,q}-2a_q=0\).  The exact determinant was independently
   factored by `code/audit/check_three_vertex_boundary.py`.
4. **No zero division.**  The manuscript elimination can be written by
   multiplication and cancellation of nonzero field elements; it does not
   assume a numerical lower bound.
5. **Configuration normalization.**  The recursion for vertex scalings has no
   consistency cycle because the underlying graph is a tree.
6. **Graphic dependence.**  Cycle dependence is the signed incidence sum;
   forest independence follows by leaf elimination.  No external matroid
   classification theorem is needed.
7. **Reconstruction.**  Hypergraph degree at least two identifies precisely
   nonleaf coordinate forms.  Each remaining triple creates the correct
   internal edge or one fresh leaf.  The \(n=2\) case is separately closed.
8. **Conjugacy.**  Pullback by an invertible linear map bijects all projective
   linear DPs and preserves dependence in both directions.

## Adverse findings and resolution

The referee found one essential limitation: special parameter hypersurfaces
can have higher-support DPs.  The formal statement and title must therefore
retain the word “generic”; this has been enforced.  No fatal or major
mathematical gap remains in the stated endpoint.

## Verdict

Mathematical proof: pass, subject to the external source/citation and final
manuscript audits.  The finite order-nine certificate independently agrees
with the general proof.
