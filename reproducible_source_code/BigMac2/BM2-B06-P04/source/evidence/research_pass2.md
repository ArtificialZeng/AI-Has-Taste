# Research pass 2: a proved product identity and positivity for charge `(0,1)`

All generating functions and abacus coordinates use the conventions frozen in
`problem.md`.  This pass proves one branch of the conjunction; it does **not**
settle the charge `(0,3)` branch or the original conjunction.

## Theorem (subsidiary branch)

For every integer \(n\geq 0\),
\[
 [q^n]c_{6,(0,1)}(q)>0.
\]
More precisely, with \((a;q)_\infty=\prod_{m\geq0}(1-aq^m)\),
\[
 c_{6,(0,1)}(q)=
 \frac{(q^2;q^2)_\infty^3(q^6;q^6)_\infty^2
 (q^{12};q^{12})_\infty^2}{(q;q)_\infty^2}
 =\psi(q)^2c_3(q^2)\psi(q^6).                 \tag{2.1}
\]

## 1. The six abacus cosets

Pass 1 proved that the exponent attached to
\(a=(a_1,\ldots,a_6)\in\mathbb Z^6\), \(\sum a_i=0\), and a selected
runner \(j\in\{1,\ldots,6\}\) is
\[
 E(a,j)=6\sum_i a_i^2+2\sum_i i a_i+6a_j+j-1.       \tag{2.2}
\]
Put \(x=2a+e_j\), so \(\sum x_i=1\), and then put
\[
 r=(-3,-2,-1,0,1,2),\qquad z=3x+r=6a+3e_j+r.
\]
Thus \(z\) belongs to the root lattice
\(A_5=\{z\in\mathbb Z^6:\sum z_i=0\}\).  Direct expansion gives
\[
 E(a,j)=\frac{3\sum x_i^2+2\sum i x_i-5}{2},
 \qquad 3E(a,j)+5=\frac12\sum_i z_i^2.              \tag{2.3}
\]
Writing \(v_j=r+3e_j\) and
\(\Theta_{6A_5+v_j}(\tau)=\sum_{z\in6A_5+v_j}q^{(z,z)/2}\), (2.2)--(2.3)
give the exact formal identity
\[
 T(\tau):=q^5c_{6,(0,1)}(q^3)
   =\sum_{j=1}^6\Theta_{6A_5+v_j}(\tau).            \tag{2.4}
\]
The six cosets are distinct because
\(v_j-v_k=3(e_j-e_k)\notin6A_5\) for \(j\ne k\).

## 2. A common scalar modular group

Write \(w=(z_1,\ldots,z_5)^t\), so \(z_6=-\sum_{i=1}^5z_i\), and put
\(A_0=I_5+J_5\).  Then \((z,z)=w^tA_0w\),
\(\det A_0=6\), and \(A_0^{-1}=I_5-J_5/6\).

We take care over the factor \(1/2\) in (2.4).  In Shimura's elementary
theta notation set
\[
 A=36A_0,\qquad N=216,\qquad
 H_j=36(v_{j,1},\ldots,v_{j,5})^t.
\]
Then \(NA^{-1}=6A_0^{-1}=6I_5-J_5\) is integral and
\(AH_j\in N\mathbb Z^5\).  Moreover, putting \(X=36w\) gives exactly
\[
 \Theta_{6A_5+v_j}(\tau)
 =\sum_{X\equiv H_j\ (N)}q^{X^tAX/(2N^2)}.         \tag{2.5}
\]
Thus Proposition 2.2 of Kane--Kim, *Theta series of ternary quadratic
lattice cosets*, Selecta Math. (N.S.) 32 (2026), article 5, DOI
<https://doi.org/10.1007/s00029-025-01110-0> (the displayed elementary
theta transformation is due to Shimura), applies without changing the
quadratic-form normalization.

For
\(\gamma=\left(\begin{smallmatrix}p&b\\c&d\end{smallmatrix}\right)\)
with \(b\equiv0\pmod2\) and \(c\equiv0\pmod{432}\), that formula and the
standard half-integral slash operator give
\[
 \Theta_{6A_5+v_j}|_{5/2}\gamma
 =\chi_{12}(d)\Theta_{6A_5+p v_j}.                 \tag{2.6}
\]
Indeed, the exponential phase is
\(e(pb(v_j,v_j)/2)=1\), and the quadratic character is
\((2\det(A)/d)=(12/d)\), since \(\det(A)=36^5\cdot6\).
Here \(\chi_D(d)=(D/d)\) is the Kronecker character.  Since \(p\) is a
unit modulo \(6\), it is \(1\) or \(-1\) modulo \(6\).  The first case
fixes the coset, while in the second
\(\Theta_{6A_5-v_j}=\Theta_{6A_5+v_j}\) by negating every vector.

Formula (2.6) initially has \(b\) even.  Every exponent in (2.4) is an
integer, so these theta series are invariant under
\(T=\left(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right)\).  If an
element of \(\Gamma_0(432)\) has \(b\) odd, right multiplication by \(T\)
makes its upper-right entry even (its upper-left entry is odd), without
changing the lower-left entry; the new lower-right entry is congruent to
the old one modulo \(432\).  Hence (2.6) extends to all of
\(\Gamma_0(432)\), and
\[
 T\in M_{5/2}(\Gamma_0(432),\chi_{12}).             \tag{2.7}
\]

Now set
\[
 G(\tau)=\frac{\eta(6\tau)^3\eta(18\tau)^2
 \eta(36\tau)^2}{\eta(3\tau)^2}
 =q^5\frac{(q^6;q^6)_\infty^3(q^{18};q^{18})_\infty^2
 (q^{36};q^{36})_\infty^2}{(q^3;q^3)_\infty^2}.   \tag{2.8}
\]
To avoid any convention issue about half-integral eta multipliers, we compare
squares.  The ordinary integral-weight eta-quotient theorem applied to
\[
 G(\tau)^2=\frac{\eta(6\tau)^6\eta(18\tau)^4
 \eta(36\tau)^4}{\eta(3\tau)^4}
\]
gives
\[
 G^2\in M_5(\Gamma_0(36),\chi_{-4}).               \tag{2.9}
\]
Indeed, its two Newman congruence sums are
\[
 \sum\delta r_\delta=240\equiv0\pmod {24},\qquad
 \sum(36/\delta)r_\delta=0,
\]
and \(s=\prod\delta^{r_\delta}=6^{18}\) is a square, so the character is
\(((-1)^5s/d)=(-4/d)\) on odd \(d\).  Holomorphy is checked at every cusp,
not inferred from the expansion at infinity: for denominators
\(c=1,2,3,4,6,9,12,18,36\), the standard cusp-order formula gives
\[
 0,\;3/2,\;0,\;2,\;3/2,\;4,\;2,\;11/2,\;10,
\]
all nonnegative.  We use the integral-weight eta-quotient theorem in the
form proved in Savitt, *An elementary proof of Newman's eta-quotient
theorem*, Res. Number Theory 11 (2025), article 78, DOI
<https://doi.org/10.1007/s40993-025-00660-8>; the cusp formula is also
recorded in Lemke Oliver, *Eta-quotients and theta functions*, Adv. Math.
241 (2013), 1--17, DOI
<https://doi.org/10.1016/j.aim.2013.03.019>.

Squaring the transformation in (2.7) gives
\[
 T^2\in M_5(\Gamma_0(432),\chi_{-4}).              \tag{2.10}
\]
For completeness, \(\chi_{12}^2=1\), the squared Jacobi-symbol factor is
one, and the remaining \(\varepsilon_d^{-10}\) equals \((-4/d)\).
Thus \(T^2\) and \(G^2\) have the same weight and character on
\(\Gamma_0(432)\).  Its index is
\[
 [\mathrm{SL}_2(\mathbb Z):\Gamma_0(432)]
 =432(1+1/2)(1+1/3)=864.                           \tag{2.11}
\]

## 3. Exact Sturm comparison

The difference \(T^2-G^2\) is an integral-weight holomorphic modular form of
weight \(5\) on \(\Gamma_0(432)\) with character \(\chi_{-4}\).  Sturm's
theorem gives the bound
\[
 B=\frac{5}{12}[\mathrm{SL}_2(\mathbb Z):\Gamma_0(432)]=360.       \tag{2.12}
\]

`certify_sturm.py` recomputes the required coefficients from (2.2), using
the proven exhaustive box bound from pass 1, and expands the other side by
exact integer polynomial arithmetic.  Only coefficients of
\(c_{6,(0,1)}(q)\) through degree
\(\lfloor(360-5)/3\rfloor=118\) are needed.  The complete enumeration uses
the box \([-7,7]^5\) (with the sixth coordinate fixed by sum zero) and
finds no mismatch.  It covers through exponent \(359\); exponent \(360\)
is zero on both sides because (2.8) has support congruent to \(5\bmod3\).
The script also squares the two transformed series and finds no mismatch
through \(q^{360}\); the exact output is `sturm_certificate.json`.
Sturm's theorem therefore gives \(T^2=G^2\).  Since
\((T-G)(T+G)=0\) in the integral domain of formal Laurent series and
\(T+G=2q^5+O(q^8)\ne0\), we have \(T=G\).  Undoing the substitution proves
the first equality in (2.1).  Gauss's product
\(\psi(q)=(q^2;q^2)_\infty^2/(q;q)_\infty\) and
\(c_3(q)=(q^3;q^3)_\infty^3/(q;q)_\infty\) give the second equality.

## 4. Positivity in every degree

Jacobi's product identities give
\[
 \psi(q)^2=\phi(q)\psi(q^2),\qquad
 \phi(q)=\sum_{x\in\mathbb Z}q^{x^2}.              \tag{2.13}
\]
Also, an explicit 3-abacus proves that \(c_3(z^2)>0\) for every
\(z\geq0\).  In the usual sum-zero 3-core coordinates, take
\[
 (b_1,b_2,b_3)=
 \begin{cases}
 (-k,2k,-k),&z=3k,\\
 (k+1,k,-2k-1),&z=3k+1,\\
 (-2k-1,k+1,k),&z=3k+2.
 \end{cases}
\]
Substitution in
\(|\lambda|=\frac32\sum b_i^2+\sum i b_i\) gives \(|\lambda|=z^2\).

It remains to cover every exponent.  For \(n\geq0\), put \(m=4n+1\).
Legendre's three-square theorem applied to \(2m\) gives
\(2m=A^2+B^2+C^2\), because \(2m\) is not of the excluded form
\(4^a(8b+7)\).  Modulo \(4\), exactly two of \(A,B,C\) are odd; relabel
so that \(A,B\) are odd and \(C\) is even.  With
\(U=(A+B)/2\), \(V=(A-B)/2\), and \(W=C/2\),
\[
 m=U^2+V^2+2W^2.
\]
As \(m\equiv1\pmod4\), \(W\) is even and exactly one of \(U,V\) is odd.
Writing the even one as \(2x\), the odd one as \(2y+1\), and \(W=2z\)
yields
\[
 n=x^2+y(y+1)+2z^2.                                \tag{2.14}
\]
Signs can be changed so that the triangular-number indices are nonnegative.
In (2.1), (2.13), use the \(x^2\) term of \(\phi(q)\), the
\(y(y+1)\) term of \(\psi(q^2)\), the displayed 3-core of size \(z^2\)
in \(c_3(q^2)\), and the constant term of \(\psi(q^6)\).  All coefficients
are nonnegative, so (2.14) supplies a positive contribution to every
coefficient.  This proves the theorem.

## Scope, audit status, and remaining kernel

The proof establishes the full `(0,1)` branch and has no known mathematical
gap.  It does not establish `(0,3)` positivity.  Equation (5.3) now gives the
exact difference
\[
 c_{6,(0,3)}(q)=\phi(q)c_3(q)^2-2q\,\psi(q)^2c_3(q^2)\psi(q^6),
\]
but subtraction is not a positive decomposition.  Gerber--Norton still lists
both branches as conjectural; targeted exact-formula searches on 2026-09-06
found no earlier occurrence of (2.1).  This is a bounded comparison, not a
priority claim, and the result still requires a fresh mathematical referee.
