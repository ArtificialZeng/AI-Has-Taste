# Modular-form proof certificate

Let

\[
 F(q)=\frac{f_4^8}{f_1^{16}f_2^8}=\sum_{n\geq0}a(n)q^n,
 \qquad U_5\!\left(\sum c(n)q^n\right)=\sum c(5n)q^n.
\]

We prove $U_5(F)\equiv1\pmod5$, which is precisely the frozen claim
because $a(0)=1$.

## Holomorphic eta quotient

Put

\[
 A(z)=\frac{\eta(4z)^8\eta(5z)^{120}}
 {\eta(z)^{16}\eta(2z)^8}.
\]

At level $N=20$, its nonzero eta exponents are

\[
 (r_1,r_2,r_4,r_5)=(-16,-8,8,120).
\]

Their sum is $104$, so the weight is $52$.  The two eta-quotient
congruence sums are

\[
 \sum_{\delta\mid20}\delta r_\delta=600\equiv0\pmod {24},
 \qquad
 \sum_{\delta\mid20}\frac{20}{\delta}r_\delta=120
 \equiv0\pmod {24}.
\]

Moreover

\[
 \prod_{\delta\mid20}\delta^{r_\delta}
 =2^8 5^{120}
\]

is a square, and the weight is even, so the associated quadratic character
is trivial.  For a cusp with denominator $d\mid20$, the invariant order is

\[
 v_d(A)=\frac{20}{24\gcd(d,20/d)}
 \sum_{\delta\mid20}
 \frac{\gcd(d,\delta)^2r_\delta}{d\delta}.
\]

Direct substitution gives

| $d$ | 1 | 2 | 4 | 5 | 10 | 20 |
|---:|---:|---:|---:|---:|---:|---:|
| $v_d(A)$ | 5 | 0 | 5 | 97 | 24 | 25 |

Thus the eta-quotient criterion gives

\[
 A\in M_{52}(\Gamma_0(20))
\]

with trivial character.  Since $5\mid20$, the standard $U_5$ operator
preserves this space; hence $U_5(A)\in M_{52}(\Gamma_0(20))$.

## Same-weight comparison

Let $E_4(z)=1+240\sum_{n\geq1}\sigma_3(n)q^n$, and define

\[
 C(z)=E_4(z)^2U_5(A)(z)-\Delta(z)^5.
\]

Both summands have weight $60$, level dividing $20$, and trivial
character.  They have integer Fourier coefficients, so

\[
 C\in M_{60}(\Gamma_0(20))\cap\mathbb Z[[q]].
\]

The index is

\[
 [\mathrm{SL}_2(\mathbb Z):\Gamma_0(20)]
 =20(1+1/2)(1+1/5)=36,
\]

and therefore the Sturm bound is

\[
 \left\lfloor\frac{60}{12}\,36\right\rfloor=180.
\]

The exact script `modular_sturm_certificate.py` constructs the two product
series directly in \(\mathbb F_5[[q]]\), through precisely the degree needed
for $U_5$, and verifies all coefficients of $C$ from degree $0$ through
degree $180$.  It reports no failures.  Sturm's theorem therefore gives

\[
 C\equiv0\pmod5.
\]

## Recovery of the frozen series

The eta shifts give the exact formal-series identities

\[
 A(q)=q^{25}f_5^{120}F(q)
      =\bigl(q^5f_1^{120}\bigr)(q^5)F(q),
 \qquad
 \Delta(q)^5=q^5f_1^{120}.
\]

For arbitrary formal series $D,F$, coefficient convolution gives

\[
 U_5(D(q^5)F(q))=D(q)U_5(F(q)).
\]

Consequently

\[
 U_5(A)=\Delta^5U_5(F).
\]

Finally, $E_4^2\equiv1\pmod5$, because every nonconstant coefficient of
$E_4$ is divisible by $240$.  Hence

\[
 0\equiv C\equiv\Delta^5\bigl(U_5(F)-1\bigr)\pmod5.
\]

Now \(\Delta^5=q^5f_1^{120}\), and $f_1^{120}$ is a unit in
\(\mathbb F_5[[q]]\).  The formal power-series ring is an integral domain, so

\[
 U_5(F)\equiv1\pmod5.
\]

It follows that $a(5n)\equiv0\pmod5$ for every integer $n\geq1$, as
claimed.
