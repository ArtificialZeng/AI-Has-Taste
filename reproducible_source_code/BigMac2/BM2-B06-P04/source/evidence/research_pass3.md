# Research pass 3: normalization audit of the `(0,1)` theorem

This pass closes the specific test requested in `state.json`: put the six
abacus coset theta series and the proposed eta product on a common scalar
modular group, compute a rigorous Sturm bound, and check the required finite
range exactly.  It is an owner-side research audit, not the fresh referee
required for acceptance.  The original conjunction remains unresolved because
no proof is supplied for charge `(0,3)`.

## Claim audited

With all conventions as fixed in `problem.md`,
\[
 c_{6,(0,1)}(q)=
 \frac{(q^2;q^2)_\infty^3(q^6;q^6)_\infty^2
 (q^{12};q^{12})_\infty^2}{(q;q)_\infty^2}
 =\psi(q)^2c_3(q^2)\psi(q^6).                    \tag{3.1}
\]
Consequently every coefficient of this series is positive.  The full proof is
in `research_pass2.md`; the checks below independently reproduce its delicate
normalizations and finite certificate.

## Exact cosets and elementary-theta normalization

For \(a\in\mathbb Z^6\), \(\sum a_i=0\), and selected runner \(j\), pass 1
gives
\[
 E(a,j)=6\sum_i a_i^2+2\sum_i i a_i+6a_j+j-1.
\]
Let
\[
 r=(-3,-2,-1,0,1,2),\qquad v_j=r+3e_j,\qquad
 z=6a+v_j.
\]
Then \(z\in A_5\), and direct expansion gives
\[
 3E(a,j)+5=(z,z)/2,
 \quad	ext{hence}\quad
 q^5c_{6,(0,1)}(q^3)=T(\tau):=
 \sum_{j=1}^6\Theta_{6A_5+v_j}(\tau).             \tag{3.2}
\]
The representatives have norms \(10,16,22,28,34,40\), and are pairwise
distinct modulo \(6A_5\).

In the basis \(e_i-e_6\), the Gram matrix of \(A_5\) is
\(A_0=I_5+J_5\), with \(A_0^{-1}=I_5-J_5/6\).  Shimura's elementary theta
series is used with
\[
 A=36A_0,\qquad N=216,\qquad H_j=36(v_{j,1},\ldots,v_{j,5})^t.
\]
Thus \(NA^{-1}=6I_5-J_5\) is integral, \(AH_j\in N\mathbb Z^5\), and the
substitution \(X=36(z_1,\ldots,z_5)^t\) gives exactly the exponent
\(X^tAX/(2N^2)=(z,z)/2\).  There is no hidden factor of two.

For
\(\gamma=\left(\begin{smallmatrix}p&b\\c&d\end{smallmatrix}\right)\)
with \(b\) even and \(c\equiv0\pmod {432}\), Proposition 2.2 of Kane--Kim,
*Theta series of ternary quadratic lattice cosets* (Selecta Math. 32 (2026),
article 5, DOI `10.1007/s00029-025-01110-0`) gives, after applying the standard
half-integral slash operator,
\[
 \Theta_{6A_5+v_j}|_{5/2}\gamma
 =\left(\frac{2\det A}{d}\right)
   \Theta_{6A_5+p v_j}
 =\left(\frac{12}{d}\right)
   \Theta_{6A_5+p v_j}.                            \tag{3.3}
\]
Indeed the exponential phase is
\(e(pb(v_j,v_j)/2)=1\), and
\(2\det A=12\cdot36^5\) has square class \(12\).  This explicitly checks
the character rather than inferring it from coefficients.

If \(b\) is odd, replace \(\gamma\) by \(\gamma T\).  Its upper-right entry
is even, its upper-left entry is still \(p\), and its lower-right entry is
\(c+d\equiv d\pmod {432}\).  Integral exponents make both coset theta series
\(T\)-invariant, so the slash group law extends (3.3) back to \(\gamma\).
Also \(p\) is a unit modulo \(6\), hence \(p\equiv\pm1\pmod6\); negation
bijections the cosets \(6A_5+v_j\) and \(6A_5-v_j\).  The standard
positive-definite elementary-theta theorem includes holomorphy at the cusps.
Therefore
\[
 T\in M_{5/2}(\Gamma_0(432),\chi_{12}).            \tag{3.4}
\]

## Eta square, character, cusps, and Sturm bound

Put
\[
 G(\tau)=\frac{\eta(6\tau)^3\eta(18\tau)^2
 \eta(36\tau)^2}{\eta(3\tau)^2}.
\]
For \(G^2\), the eta exponents at \(3,6,18,36\) are \(-4,6,4,4\).
The two Newman sums at level \(36\) are \(240\) and \(0\); the parameter
\(\prod\delta^{r_\delta}=6^{18}\).  Its character is consequently
\(\chi_{-4}\).  The exact cusp orders for denominators
\(1,2,3,4,6,9,12,18,36\) are
\[
 0,\ 3/2,\ 0,\ 2,\ 3/2,\ 4,\ 2,\ 11/2,\ 10,
\]
so \(G^2\in M_5(\Gamma_0(36),\chi_{-4})\), and hence also at level \(432\).
Squaring (3.4) gives the same character because
\(\varepsilon_d^{-10}=(-4/d)\).  Thus
\[
 T^2-G^2\in M_5(\Gamma_0(432),\chi_{-4}).          \tag{3.5}
\]
The index is
\(432(1+1/2)(1+1/3)=864\), so the integral-weight Sturm bound is exactly
\[
 \frac5{12}\,864=360.                             \tag{3.6}
\]

## Independent exact computation

`independent_theta_audit.py` shares no code with the pass-1 enumerator.  It
directly enumerates every vector in each \(6A_5+v_j\) capable of contributing
through \(q^{360}\): the norm bound forces every coordinate into
\([-26,26]\).  It separately expands \(G\) from its four Pochhammer factors,
and separately enumerates the abacus formula through charged degree \(118\).
The abacus box \([-7,7]^5\) is complete because a coordinate of absolute value
at least \(8\) forces the first core size above \(118\):
\(192-\sqrt{1120}>118\), certified by \(74^2>1120\).

The resulting `theta_audit_certificate.json` records no mismatch among the
direct coset theta series, the transformed charged series, and \(G\) through
\(q^{360}\), and no mismatch between their squares through the Sturm bound.
It also independently reproduces every cusp order, the index, the bound, and
the immutable source hash.  Hence Sturm's theorem gives \(T^2=G^2\).  Both
series lead with \(q^5\), so the integral-domain factorization
\((T-G)(T+G)=0\) gives \(T=G\), proving (3.1).

Finally, the all-degree positivity argument in pass 2 is exact: Legendre's
three-square theorem yields
\(n=x^2+y(y+1)+2z^2\) for every \(n\ge0\); Jacobi's
\(\psi(q)^2=\phi(q)\psi(q^2)\), an explicit 3-core of size \(z^2\), and the
constant term of \(\psi(q^6)\) then select a positive summand in (3.1).

## Scope and remaining test

This establishes a nontrivial subsidiary theorem suitable for a `result-note`
candidate.  It does not settle charge `(0,3)`, and therefore does not resolve
the frozen original conjunction.  The next decisive step is a fresh referee
audit of the abacus bijection, Shimura slash normalization and cusp
holomorphy, eta cusp orders, exact Sturm certificate, and the Legendre
representation argument at exactly this restricted scope.
