# Carter 1972 binding for the \(D_9\) rank formula

## Primary theorem and exact location

R. W. Carter, *Conjugacy classes in the Weyl group*, *Compositio
Mathematica* **25** (1972), no. 1, 1--59, Lemma 2 on journal p. 3, defines
\(l(w)\) as the smallest number of root reflections in a factorization of
\(w\) and proves:

> \(l(w)\) is the number of eigenvalues of \(w\) on the reflection
> representation that are different from \(1\).

Equivalently,

\[
l(w)=\operatorname{codim}\operatorname{Fix}(w).
\]

The locally retained version-of-record PDF is
`literature/sources/carter-1972.pdf`, SHA-256
`9906164332f45299f337c5e95f8681c8ec02356a6b34d72aada16e7be0a3eaf5`.
The same use of Carter's result is stated by Gaetz--Gao in Section 2.2,
journal p. 793.

## Applicability to the formal \(D_9\) endpoint

The formal statement uses the standard real reflection representation of the
Weyl group \(W(D_9)\) on \(\mathbb R^9\).  Its root system is

\[
\Phi(D_9)=\{\pm e_i\pm e_j:1\leq i<j\leq9\}.
\]

The corresponding root reflections are exactly the 72 signed
transpositions listed in `problem/formal_statement.md`: for each \(i<j\),
one swaps \(e_i,e_j\), and the other sends \(e_i\mapsto-e_j\),
\(e_j\mapsto-e_i\).  Thus Carter's generating reflection set is exactly the
set \(T\) used to define \(\ell_T\), not a different Coxeter-simple length.

## From signed cycles to rank

On the coordinate subspace of one signed cycle, the fixed-vector equations
propagate one coordinate around the cycle.  If the cycle sign product is
positive, the propagated value returns unchanged and the fixed subspace on
that support is one-dimensional.  If the sign product is negative, the value
returns with its sign reversed, forcing it to be zero, so the fixed subspace
is zero-dimensional.  Disjoint cycle supports are a direct sum.

Therefore an element of signed cycle type \((\lambda,\mu)\), where
\(\lambda\) lists its positive cycles, satisfies

\[
\dim\operatorname{Fix}(w)=\ell(\lambda),\qquad
\ell_T(w)=9-\ell(\lambda).
\]

This proves the rank formula used at every node of the orbit quotient.  The
argument covers 1-cycles, repeated cycle lengths, the identity, and types
with no positive cycles; no division, genericity, or limiting assumption is
present.
