# Fresh mathematical referee report

## Frozen scope and integrity

I reviewed the exact `result-note` claim frozen in `claim.json`: positivity in every degree for the charge `(0,1)` branch, together with the displayed eta/product identity.  The claim expressly leaves the charge `(0,3)` branch and therefore the original conjunction unresolved.  I did not treat the candidate as a resolution of the original problem.

The snapshot digest is `efff534371860ad775942b04e34a64d0a13309e1fa663e7c2d91b50fdef8b0ba`.  I recomputed every listed SHA-256 digest and the canonical snapshot digest; all matched.  The immutable `source.md` hash remained `97bdb917cf2f4aa04a1f5aa17323e3d6dc8422ee685c05eab1995f44b9a1ccd4`.

## Reconstruction of the decisive argument

Let `A=S(lambda^1,0)`.  The nesting `A subset A+6` makes `A` a charge-zero 6-core beta set.  On runner `i`, write its first gap as `g_i=i+6a_i`, where `sum a_i=0`.  Then `(A+6)\A` consists of the six `g_i`.  A beta set of charge one between `A` and `A+6` is uniquely `A union {g_j}`.  The standard abacus size formula and the change in size after adjoining one beta number give

\[
 E(a,j)=6\sum_i a_i^2+2\sum_i i a_i+6a_j+j-1.
\]

This parametrizes all and only the `(6,(0,1))`-core bipartitions, without multiplicity.  As a convention check independent of the abacus program, I generated ordinary partitions directly, formed their charged beta sets, tested both inclusions, and counted total sizes through 18.  The resulting coefficients

\[
1,2,2,4,5,6,8,8,11,12,16,20,17,20,24,24,25,28,30
\]

agree termwise with an independent finite expansion of the claimed product.

Put `r=(-3,-2,-1,0,1,2)`, `v_j=r+3e_j`, and `z=6a+v_j`.  Direct expansion gives `sum z_i=0` and

\[
 3E(a,j)+5=(z,z)/2,
 \qquad
 q^5 c_{6,(0,1)}(q^3)=T(\tau):=\sum_{j=1}^6\Theta_{6A_5+v_j}(\tau).
\]

The six cosets are distinct modulo `6A_5`.  In the basis `e_i-e_6`, the Gram matrix is `A_0=I_5+J_5`, with determinant 6 and inverse `I_5-J_5/6`.  I checked the elementary-theta realization with

\[
 A=36A_0,\qquad N=216,\qquad H_j=36v'_j.
\]

It satisfies `NA^{-1}=6I_5-J_5` integral and `AH_j in N Z^5`, and its exponent is exactly `(z,z)/2`; there is no normalization discrepancy.

I checked the cited elementary theta transformation formula in Kane--Kim, Proposition 2.2 (which reproduces Shimura's formula).  For `b` even and `c` divisible by 432, combining that formula with the stated half-integral slash operator gives

\[
 \Theta_{6A_5+v_j}|_{5/2}\gamma
 =\left(\frac{2\det A}{d}\right)\Theta_{6A_5+p v_j}
 =\left(\frac{12}{d}\right)\Theta_{6A_5+p v_j}.
\]

The exponential phase is one because `(v_j,v_j)/2` is integral.  Since `p` is a unit modulo 6, multiplication by `p` fixes the coset up to negation, and negation preserves its theta series.  If `b` is odd, right multiplication by the translation matrix makes it even; integral Fourier exponents and `c+d congruent d (mod 432)` extend the formula to all of `Gamma_0(432)`.  Positive-definite coset theta theory supplies cusp holomorphy.  Thus `T` has weight `5/2` and character `(12/d)` there.  Squaring the precise slash law yields the integral-weight character `epsilon_d^{-10}=(-4/d)`, so

\[
 T^2\in M_5(\Gamma_0(432),\chi_{-4}).
\]

For

\[
 G=\eta(6\tau)^3\eta(18\tau)^2\eta(36\tau)^2/\eta(3\tau)^2,
\]

the eta exponents of `G^2` are `(-4,6,4,4)` at `(3,6,18,36)`.  I recomputed the two Newman sums as 240 and 0, and `prod delta^{r_delta}=6^{18}`.  Newman's theorem therefore gives character `(-4/d)`.  The cusp orders for denominators `1,2,3,4,6,9,12,18,36` are respectively

\[
0,\ 3/2,\ 0,\ 2,\ 3/2,\ 4,\ 2,\ 11/2,\ 10,
\]

so `G^2` is holomorphic on `Gamma_0(36)`, hence also on `Gamma_0(432)`.

The index of `Gamma_0(432)` is 864, so the weight-5 Sturm bound is 360.  I reran the frozen direct coset/eta audit: direct enumeration of all six `A_5` cosets, direct Pochhammer expansion of `G`, and a separate abacus enumeration all agreed through exponent 360; their squares also had no mismatch through 360.  The box bounds in that verifier are sufficient: norm at most 720 forces every theta coordinate to have absolute value at most 26, and a charged coordinate of absolute value at least 8 forces the first core size above 118.  The rerun reproduced the frozen certificate byte-for-byte, and the snapshot remained current.

Sturm's theorem now gives `T^2=G^2`.  Since both have leading term `q^5` and formal Laurent series form an integral domain, `T=G`.  Undoing the substitution proves

\[
c_{6,(0,1)}(q)=
\frac{(q^2;q^2)_\infty^3(q^6;q^6)_\infty^2(q^{12};q^{12})_\infty^2}
{(q;q)_\infty^2}
=\psi(q)^2c_3(q^2)\psi(q^6).
\]

Finally, Jacobi's identity rewrites `psi(q)^2` as `phi(q)psi(q^2)`.  The displayed three-runner vectors in the evidence do give a 3-core of size `z^2` for every `z>=0`.  For arbitrary `n>=0`, Legendre's three-square theorem applied to `2(4n+1)` yields, after the parity change of variables recorded in the proof,

\[
n=x^2+y(y+1)+2z^2
\]

with `y,z>=0`.  Selecting these terms from `phi(q)`, `psi(q^2)`, and `c_3(q^2)`, and the constant term from `psi(q^6)`, gives a positive contribution to the coefficient of every `q^n`.  All factors in this representation have nonnegative coefficients, so cancellation is impossible.  The boundary case `n=0` is included.

## Source comparison and contribution

Gerber--Norton, arXiv:2609.03738v1, equation (5.3) states

\[
\phi(q)c_3(q)^2=c_{6,(0,3)}(q)+2q c_{6,(0,1)}(q),
\]

and the following sentence and Table 2 label the two separate `e=6` branches conjectural.  The submitted theorem therefore proves one exact branch left open by the nearest source; it is not a routine toy restriction and has a direct use in that source's `e=6` program.  A bounded exact-formula/statement search found no earlier occurrence of this charged-core identity.  This is only a literature screen, not a priority guarantee, consistent with the candidate's wording.

## Gaps and verdict

I found no mathematical gap in the frozen `(0,1)` identity or its all-degree positivity proof.  No conclusion about `(0,3)` follows from the subtraction in equation (5.3), so the original conjunction remains unresolved exactly as stated in the candidate.

**Verdict: accept the frozen `result-note` scope.**
