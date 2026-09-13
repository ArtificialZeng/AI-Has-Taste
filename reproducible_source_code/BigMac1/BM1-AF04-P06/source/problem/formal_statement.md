# Formal statement

## Objects and quantifiers

Let \(N=105\), let \(G=\mathbb Z/N\mathbb Z\), and fix the primitive root
\(\zeta_N=\exp(2\pi i/N)\).  A *candidate of weight 20* is a subset
\(S\subseteq G\) with \(|S|=20\); thus all roots occur with coefficient zero
or one and repetitions are excluded.

The candidate is *vanishing* when

\[
  \sum_{s\in S}\zeta_N^s=0.
\]

It is *inclusion-minimal vanishing* when it is vanishing and, for every
subset \(T\) satisfying \(\varnothing\ne T\subsetneq S\),

\[
  \sum_{t\in T}\zeta_N^t\ne0.
\]

The research endpoint is to determine the finite quotient

\[
 \mathcal M_{20}/\!\sim,
 \qquad
 \mathcal M_{20}:=\{S\subseteq G: |S|=20,
 S\text{ is inclusion-minimal vanishing}\},
\]

where \(S\sim S'\) if and only if there exist \(a\in G\) and
\(u\in G^\times\) such that

\[
 S'=a+uS:=\{a+us\pmod {105}:s\in S\}.
\]

A complete answer is either (i) a proof that \(\mathcal M_{20}=\varnothing\),
or (ii) one explicit representative of every orbit, together with a proof
that the list is exhaustive and that every representative is minimal.

## Exact polynomial formulation

For \(S\subseteq G\), put \(f_S(X)=\sum_{s\in S}X^s\in\mathbb Z[X]\),
using the representatives \(0,\ldots,104\).  Since \(\zeta_N\) has minimal
polynomial \(\Phi_{105}\) of degree \(\varphi(105)=48\),

\[
 \sum_{s\in S}\zeta_N^s=0
 \quad\Longleftrightarrow\quad
 \Phi_{105}(X)\mid f_S(X)
 \quad\Longleftrightarrow\quad
 \sum_{s\in S}c_s=0\in\mathbb Z^{48},
\]

where \(c_s\) is the coefficient vector of
\(X^s\bmod\Phi_{105}(X)\).  Hence the classification is a finite exact
Boolean problem \(Ax=0\), \(x_s\in\{0,1\}\), \(\sum_sx_s=20\).

## Normalizations and completeness convention

Translation multiplies the complex sum by \(\zeta_N^a\), and multiplication
of exponents by a unit applies a cyclotomic Galois automorphism.  Both preserve
vanishing, cardinality, and inclusion-minimality.  Every nonempty orbit has an
image containing exponent zero, so discovery may impose \(x_0=1\).  This does
not choose a unique image; completeness still requires blocking or
canonicalizing all normalized affine images.

Every finite nonempty vanishing set contains an inclusion-minimal vanishing
subset.  Consequently a vanishing 20-set is nonminimal exactly when it contains
an inclusion-minimal vanishing subset of weight less than 20.  This implication
is valid only after the lower-weight catalog used as blockers is itself complete.

## Endpoints and degenerate cases

- The source statement omitted \(S\ne\varnothing\); weight 20 makes nonemptiness
  automatic.  For the replayed baseline at weights starting from zero, the empty
  set must be excluded explicitly.
- “Proper subset” means strictly smaller; the empty subset is excluded from the
  minimality test, and the full set is excluded because its sum is already zero.
- Singleton zero sums cannot occur because roots of unity are nonzero.
- Exponents are residues modulo 105, but a subset never contains a residue twice.
- No floating-point tolerance, modular image, timeout, or solver `unknown` result
  is accepted as a proof of vanishing, minimality, or exhaustiveness.
