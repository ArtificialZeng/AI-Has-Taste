# Formal statement

## Definitions and quantifiers

Let \(n\ge 1\), let \(P(z)=\sum_{k=0}^n a_k z^k\in\mathbb C[z]\) have
exact degree \(n\), and let \(\mathbb D=\{z\in\mathbb C:|z|<1\}\).  The
polynomial is *self-inversive* when its multiset of zeros is invariant under
\(\zeta\mapsto 1/\overline\zeta\).  Equivalently (and this is the coefficient
form used in the project), there is a unimodular number \(\omega\) such that

\[
       a_k=\omega\,\overline{a_{n-k}}\qquad(0\le k\le n).
\]

In particular \(a_0a_n\ne0\).  Put \(A(P)=\max_{0\le k\le n}|a_k|\).
The covering assertion \(\mathsf C_n\) is

\[
  \forall P\text{ as above}\quad\exists c\in\mathbb C\quad
  \{w:|w-c|<A(P)\}\subseteq P(\mathbb D).
\]

The full Sheil-Small question asks whether \(\mathsf C_n\) holds for every
integer \(n\ge1\).  The requested finite frontier asks to decide
\(\mathsf C_n\) separately for \(n=2,3,4,5\) and to identify the least degree
of any counterexample if one exists.

Equivalently, for the Euclidean inradius

\[
 \rho(\Omega)=\sup_{c\in\Omega}\operatorname{dist}(c,\mathbb C\setminus\Omega),
\]

the assertion is \(\rho(P(\mathbb D))\ge A(P)\).  Because \(P(\mathbb D)\)
is a bounded nonempty domain, this supremum is attained after extending the
distance-to-the-complement function by zero to its compact closure.  Thus the
open-disk formulation and the non-strict inradius inequality agree.

## Normalizations and invariances

Multiplying \(P\) by \(\lambda\ne0\) multiplies both \(\rho\) and \(A\) by
\(|\lambda|\), while adding a constant translates the image but generally
does **not** preserve self-inversiveness.  We may therefore normalize
\(A(P)=1\), and use a scalar phase to put the coefficient relation into a
convenient phase convention.  Precomposition \(z\mapsto e^{i\theta}z\)
preserves \(\mathbb D\), the inradius, coefficient moduli, and the
self-inversive class (with a changed unimodular parameter).

## Edge cases and conventions

- Degree means exact degree; leading zero coefficients are not permitted.
- The zero polynomial and nonzero constants are excluded by \(n\ge1\).  If
  constants were admitted, every nonzero constant would trivially falsify
  the statement, so this endpoint must be explicit.
- Multiplicities are included in the zero-multiset invariance.
- Zeros on \(|z|=1\) are fixed by the involution and may have arbitrary
  multiplicity; repeated zeros and critical points are not excluded.
- “Contains a disk of radius \(A\)” means containment of the *open* Euclidean
  disk, with equality \(\rho=A\) allowed.
- The user and the supplied SciNet page explicitly use conjugate inversion
  \(\zeta\mapsto1/\overline\zeta\), which is the standard self-inversive
  convention and is the convention solved here.  The accessible 2018 source
  TeX for Hayman--Lingham Problem 4.24 literally prints \(1/\zeta\), without
  the conjugation.  No published erratum was located.  This discrepancy is
  not silently repaired: results in this project concern the user's standard
  conjugate-inversion formulation, not the distinct literal reciprocal-root
  class unless separately stated.
