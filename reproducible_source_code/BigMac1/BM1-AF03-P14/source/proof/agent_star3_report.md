# Exact saturated-ideal classification of the ordered `star3` chamber

Date: 2026-08-29  
Role: independent exact prover  
Endpoint: the `star3` polynomial critical system with \(a_4=1\), saturated
away from zero coordinates, zero section numerator, and zero squared norm.

## Result

The saturated critical ideal has exactly 14 distinct complex roots, of which
8 are real.  It is radical and decomposes into four explicitly parametrized
components of degrees \(2,4,4,4\).  **None of its real roots lies in the
closure of the ordered positive `star3` chamber.**  In particular, the strict
ordered `star3` chamber contains no critical direction.

The serialized exact certificate is
`certificates/star3_decomposition.json`.  The no-import, fail-closed verifier
is `src/builder_verify_star3.py`.

## 1. System reconstructed from the box-spline formula

Let

\[
 a_0\ge a_1\ge a_2\ge a_3\ge a_4>0,
 \qquad T={1\over2}\sum_{i=0}^4a_i.
\]

In `star3`, the negative pair forms are exactly

\[
 N=\{01,02,03\},
\]

so the fourth-degree homogeneous numerator before projective normalization is

\[
 P=T^4-\sum_i(T-a_i)^4+\sum_{i<j}(T-a_i-a_j)^4
 -2\sum_{j=1}^3(T-a_0-a_j)^4.
\tag{1.1}
\]

Set \(a_4=1\), and write

\[
 S=a_0^2+a_1^2+a_2^2+a_3^2+1.
\]

After clearing the common harmless rational factor, (1.1) becomes

\[
\begin{aligned}
P={}&a_0^3-3a_0^2(a_1+a_2+a_3)
+3a_0(a_1^2+a_2^2+a_3^2)
+6a_0(a_1a_2+a_1a_3+a_2a_3)+a_0\\
&-a_1^3-a_2^3-a_3^3
-3(a_1^2a_2+a_1^2a_3+a_1a_2^2+a_1a_3^2
    +a_2^2a_3+a_2a_3^2)\\
&+18a_1a_2a_3-a_1-a_2-a_3.
\end{aligned}
\tag{1.2}
\]

The scale-invariant section function is a positive constant times
\(\sqrt S P/(a_0a_1a_2a_3)\).  Its exact critical equations are

\[
 G_i=a_iS\,\partial_iP+(a_i^2-S)P=0,
 \qquad 0\le i\le3.
\tag{1.3}
\]

Define

\[
 I=\langle G_0,G_1,G_2,G_3\rangle,
 \qquad
 M=a_0a_1a_2a_3PS,
 \qquad
 Q=I:M^\infty.
\tag{1.4}
\]

No numerical roots or discovery output enter (1.1)--(1.4).

## 2. Exact ideal decomposition

Put

\[
 q(s)=2s^4+5s^2-1.
\]

The following four ideals are in \(\mathbb Q[a_0,a_1,a_2,a_3]\):

\[
\begin{aligned}
J_0={}&\langle a_0-2a_3,\ a_1-a_3,\ a_2-a_3,\ 3a_3^2-1\rangle,\\
J_1={}&\langle a_0-a_1-a_2,\ a_2-a_3,
 2a_2a_1-a_2^2-1,\ q(a_2)\rangle,\\
J_2={}&\langle a_0-a_1-a_2,\ a_1-a_3,
 2a_1a_2-a_1^2-1,\ q(a_1)\rangle,\\
J_3={}&\langle a_0-a_1-a_3,\ a_1-a_2,
 2a_1a_3-a_1^2-1,\ q(a_1)\rangle.
\end{aligned}
\tag{2.1}
\]

Exact Gröbner reduction over \(\mathbb Q\) proves

\[
 \boxed{Q=J_0\cap J_1\cap J_2\cap J_3.}
\tag{2.2}
\]

The verifier reconstructs \(I,M\) from (1.1), computes the saturation in
Singular, constructs the intersection in (2.2), and checks both ideal
remainders are zero.  Both sides have dimension zero and vector-space
dimension 14.  The individual vector-space dimensions are

\[
 \dim_{\mathbb Q}\mathbb Q[a]/J_0=2,
 \qquad
 \dim_{\mathbb Q}\mathbb Q[a]/J_k=4\quad(k=1,2,3).
\]

The components have the following explicit parametrizations:

\[
\begin{array}{c|c|c}
\text{component}&\text{parameter equation}&(a_0,a_1,a_2,a_3)\\ \hline
J_0&3t^2-1=0&(2t,t,t,t)\\[1mm]
J_1&q(s)=0&(s+\ell,\ell,s,s)\\
J_2&q(s)=0&(s+\ell,s,\ell,s)\\
J_3&q(s)=0&(s+\ell,s,s,\ell),
\end{array}
\tag{2.3}
\]

where

\[
 \ell={s^2+1\over2s}.
\tag{2.4}
\]

Direct substitution reduces every \(G_i\) to zero modulo the displayed
parameter polynomial.  The saturation multiplier is a unit on every
component.  For example,

\[
\begin{array}{c|c|c}
&P&S\\ \hline
J_0&t(23t^2-1)&7t^2+1\\
J_1&11s(s^2+1)&(3s^2+1)^2/(2s^2),
\end{array}
\]

and the other quartic components are permutations of \(J_1\).  Their
numerators are relatively prime to the respective parameter polynomial.

Both \(3t^2-1\) and \(q(s)\) are squarefree.  Each parameter appears as an
actual coordinate in (2.3), so distinct parameter roots give distinct points.
The components have total degree 14, equal to the degree of \(Q\).  Hence
(2.2) is a radical 14-point decomposition, not a multiplicity count.

As a separate degeneracy check, the determinant of the Jacobian
\(\partial(G_0,G_1,G_2,G_3)/\partial(a_0,a_1,a_2,a_3)\) reduces to

\[
 -{16000\over243}
\]

on \(J_0\), and to

\[
 -{11979\over128}(1701s^2-335)
\]

on each quartic component.  The latter is relatively prime to \(q(s)\).
Thus all 14 roots are simple for the original four critical equations; there
are no hidden multiple or Jacobian-degenerate roots.

For comparison with a lexicographic elimination, the univariate eliminant in
\(a_3\) factors as

\[
 (3a_3^2-1)(2a_3^4+5a_3^2-1)(8a_3^4-13a_3^2-4).
\tag{2.5}
\]

The third factor describes the value \(\ell\) when the exceptional quartic
branch is viewed through the coordinate occupied by \(\ell\); it is not an
additional component.

## 3. Complete real-root classification

The quadratic component has two real roots

\[
 t\in(-2/3,-1/2)\quad\text{or}\quad t\in(1/2,2/3).
\]

The quartic \(q\) has exactly two real roots, isolated by

\[
 s\in(-1/2,-2/5)\quad\text{or}\quad s\in(2/5,1/2),
\]

and two nonreal roots.  Hence \(J_0\) contributes 2 real points and
\(J_1,J_2,J_3\) contribute 2 each, for 8 real roots in total.

The positive quartic root has the closed form

\[
 s^2={-5+\sqrt{33}\over4},
 \qquad 0<s<1,
\]

and (2.4) gives \(\ell>1\).  Its three positive real points consist of one
\(\ell\) and two copies of \(s\) among \(a_1,a_2,a_3\), with
\(a_0=s+\ell\).  The three negative conjugates have
\(a_0,a_1,a_2,a_3<0\).  The positive quadratic point is

\[
 (a_0,a_1,a_2,a_3,a_4)
 =(2/\sqrt3,1/\sqrt3,1/\sqrt3,1/\sqrt3,1),
\]

and its negative conjugate again fails positivity.

## 4. Ordered chamber and boundary audit

With \(a_4=1\), the closure of the ordered positive cone requires

\[
 a_0\ge a_1\ge a_2\ge a_3\ge1.
\tag{4.1}
\]

The strict `star3` pair inequalities reduce, by ordering, to

\[
\begin{aligned}
 a_0-a_1-a_2+a_3-1&>0 &&(a_0+a_3>T),\\
 -a_0+a_1+a_2+a_3-1&>0 &&(a_0+1<T),\\
 a_0-a_1-a_2+a_3+1&>0 &&(a_1+a_2<T).
\end{aligned}
\tag{4.2}
\]

No positive root even reaches (4.2), because all fail (4.1):

* on \(J_0\), \(a_3=t<2/3<1\);
* on every positive quartic point, two of \(a_1,a_2,a_3\) equal
  \(s<1/2<1\).

Thus there are zero roots not only in the strict chamber but also in its
ordered positive closure.

There are coordinate-equality faces in the algebraic zero set:
\(a_1=a_2=a_3\) on \(J_0\), and two of \(a_1,a_2,a_3\) coincide on each
quartic component.  These equalities do not create multiplicity, as the
Jacobian test above shows.  Exact gcd tests of every pair form
\(T-a_i-a_j\) with the relevant minimal polynomial show that none of the 14
complex roots, and hence none of the 8 real roots, lies on a subset-sum wall.
No coordinate, \(P\), or \(S\) vanishes at a component root, so saturation
has not silently discarded a boundary point of these components.

## 5. Certificate and fail-closed verification

The certificate records:

* chamber edges and normalization;
* a SHA-256 binding of the reconstructed integer system;
* the four component ideals and parametrizations;
* squarefree parameter polynomials and rational real-root isolators;
* expected complex/real counts and boundary classification.

Run from the project root:

```bash
python src/builder_verify_star3.py
```

The verifier independently rebuilds (1.1)--(1.4), verifies the hash,
substitutions, saturation units, Jacobian nondegeneracy, Sturm root counts,
pair-wall exclusions, component degrees, and both directions of (2.2).  It
then mutates, in turn, a chamber edge, a minimal-polynomial coefficient, a
component generator, and the system hash.  All four corrupted certificates
must be rejected before the verifier prints `PASS`.

Observed clean output:

```text
mutation rejected: removed_star_edge
mutation rejected: changed_minpoly_coefficient
mutation rejected: changed_component_generator
mutation rejected: changed_system_hash
star3 verifier: PASS
```

No floating-point root, numerical optimizer output, Lean, Coq, Isabelle, or
other proof assistant is used.
