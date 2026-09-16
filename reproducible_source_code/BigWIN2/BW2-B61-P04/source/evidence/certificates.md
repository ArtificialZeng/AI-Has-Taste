# Exact resolution certificate

All fields and curves below are over \(\mathbb F _5\).  Write
\(E_{a,b}:y^2=x^3+ax+b\), and write \(F_E\) for geometric-torsion
Frobenius.  The primary source copied at `evidence/external/2609.02278.pdf`
uses the operation \(x*y=F_E x+(1-F_E)y\).  Its Theorem 4.2 and Corollary
4.3 say, in particular, that two such abstract quandles on \(E[\ell]\) are
isomorphic exactly when their Frobenius operators are similar over
\(\mathbb F_\ell\).

## Exact point counts and integral Frobenius polynomials

For a short Weierstrass equation in characteristic five, nonsingularity is
equivalent to \(4a^3+27b^2\ne0\).  In the table, `rhs` gives the five values
of \(x^3+ax+b\) for \(x=0,1,2,3,4\), and `multiplicities` gives the number of
solutions \(y\) to each corresponding equation.  Thus the point count is one
plus the sum of the multiplicities.  All entries are direct arithmetic in
\(\mathbb F _5\).

| label and equation | \(4a^3+27b^2\) | rhs | multiplicities | \(N=\#E(\mathbb F _5)\) | \(a_E=6-N\) | \(P_E(T)=T^2-a_ET+5\) |
|---|---:|---|---|---:|---:|---|
| \(E_{-4}:y^2=x^3+3x\) | 3 | 0,4,4,1,1 | 1,2,2,2,2 | 10 | -4 | \(T^2+4T+5\) |
| \(E_0:y^2=x^3+1\) | 2 | 1,2,4,3,0 | 2,0,2,0,1 | 6 | 0 | \(T^2+5\) |
| \(E_1:y^2=x^3+3x+2\) | 1 | 2,1,1,3,3 | 0,2,2,0,0 | 5 | 1 | \(T^2-T+5\) |
| \(E_{-2}:y^2=x^3+4x\) | 1 | 0,0,1,4,0 | 1,1,2,2,1 | 8 | -2 | \(T^2+2T+5\) |
| \(E_3:y^2=x^3+4x+2\) | 4 | 2,2,3,1,2 | 0,0,0,2,0 | 3 | 3 | \(T^2-3T+5\) |

Every displayed nonsingularity factor is nonzero.  Hence all five equations
define elliptic curves.  For an elliptic curve over \(\mathbb F _5\), the
point count gives the stated Frobenius trace and integral characteristic
polynomial.  For every \(\ell\ne5\), the characteristic polynomial of
\(F_E\) on \(E[\ell]\) is the reduction of this polynomial modulo \(\ell\).

## The three small-prime counterexamples

### \(\ell=2\)

Take \(E_{-4}\) and \(E_0\).  They have different integral Frobenius
polynomials, hence are not \(\mathbb F _5\)-isogenous.  Modulo two, both
Frobenius operators have characteristic polynomial
\[
 T^2+1=(T+1)^2.
\]
It remains important here not to infer similarity merely from this equality.
The roots in \(\mathbb F _5\) of the defining cubics are, respectively,
\[
 \{0\}\quad\hbox{and}\quad\{4\}.
\]
Thus each curve has exactly two rational 2-torsion points, including the
identity.  Consequently \(\ker(F_E-I)=E[2](\mathbb F _5)\) is one-dimensional
over \(\mathbb F _2\).  In particular, \(F_E\ne I\), so its minimal polynomial
is \((T+1)^2\), not \(T+1\).  Both rational canonical forms therefore consist
of the single companion block
\[
 C_2=\begin{pmatrix}0&1\\1&0\end{pmatrix},
 \qquad \det(TI-C_2)=T^2+1.
\]
The Frobenius operators are similar, so Corollary 4.3 gives isomorphic
Frobenius Alexander quandles.  This is an exact nonisogenous counterexample to
uniform sufficiency at two.

### \(\ell=3\)

Take the pair in the primary source's Example 4.9, namely \(E_1\) and
\(E_{-2}\).  Their point counts and integral polynomials were independently
recomputed in the table.  The traces \(1\) and \(-2\) differ, so the curves are
not \(\mathbb F _5\)-isogenous.  Both reduced characteristic polynomials are
\[
 T^2+2T+2\in\mathbb F _3[T].
\]
Its values at \(0,1,2\) are \(2,2,1\), so it is irreducible.  It is therefore
the minimal polynomial of either Frobenius, and both rational canonical forms
are the single block
\[
 C_3=\begin{pmatrix}0&1\\1&1\end{pmatrix},
 \qquad \det(TI-C_3)=T^2+2T+2.
\]
The Frobenius operators, and hence the quandles, are isomorphic.  This
rechecks the source's counterexample while supplying the requested point-count
and rational-canonical-form certificate.

### \(\ell=7\)

Take \(E_{-4}\) and \(E_3\).  Their traces \(-4\) and \(3\) differ, so their
distinct integral Frobenius polynomials show that they are not
\(\mathbb F _5\)-isogenous.  Since the traces are congruent modulo seven,
both reduced characteristic polynomials are
\[
 T^2-3T+5=T^2+4T+5\in\mathbb F _7[T].
\]
The discriminant is \(3\), which is not in the square set
\(\{0,1,2,4\}\subset\mathbb F _7\).  The polynomial is irreducible and hence
is the minimal polynomial of either Frobenius.  Both rational canonical forms
are the single block
\[
 C_7=\begin{pmatrix}0&2\\1&3\end{pmatrix},
 \qquad \det(TI-C_7)=T^2+4T+5.
\]
Thus the Frobenius operators are similar and the quandles are isomorphic,
giving an exact nonisogenous counterexample at seven.

## Uniform sufficiency and leastness

Let \(A,B/\mathbb F _5\) be arbitrary elliptic curves whose Frobenius
Alexander quandles at \(\ell=11\) are isomorphic.  By Corollary 4.3 their
Frobenius operators on 11-torsion are similar.  They therefore have equal
characteristic polynomials over \(\mathbb F _{11}\), and in particular
\[
 a_A\equiv a_B\pmod {11}.
\]
Hasse's bound and integrality give \(a_A,a_B\in\{-4,-3,\ldots,4\}\), so
\(|a_A-a_B|\le8<11\).  The congruence forces \(a_A=a_B\).  Their integral
Frobenius polynomials \(T^2-a_AT+5\) are equal, so the finite-field isogeny
criterion gives \(A\sim_{\mathbb F _5}B\).  This proves the required uniform
sufficiency at 11 (and is also the genus-one specialization of the primary
source's Corollary 4.5, since \(11>4\sqrt5\)).

The only rational primes below 11 different from 5 are 2, 3, and 7.  The
three certified pairs above show failure for each.  Therefore the least prime
with the frozen uniform property is exactly
\[
 \boxed{11}.
\]

## Reproduction

Run `python3 evidence/verify_certificates.py`.  The script enumerates every
affine fiber, checks each expected count, trace, cubic-root set, reduced
polynomial, irreducibility assertion, and companion-matrix characteristic
polynomial, and terminates with `ALL EXACT CERTIFICATE CHECKS PASSED`.
