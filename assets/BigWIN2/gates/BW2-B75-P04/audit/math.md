# Fresh mathematical referee report

## Verdict and frozen scope

**Verdict: accept.**  I reviewed the exact frozen `result-note` claim while
preserving the original operator-level status as `unresolved`.  All seven
files in `audit/snapshot.json` have their recorded SHA-256 digests, and I
independently recomputed the canonical snapshot digest as
`503d7e296f12b32e3aeaae91e6611af6a7f15afef0936755e95b4f478f4600eb`.
In particular, `source.md` still has SHA-256
`3ee9ccc12ddcd0cbb40f14d0a3444709b13b398ca02d9176d49d28788c4bc99e`.

## Reconstruction of the decisive argument

Put \(A=\alpha+2\geq2\), \(h=p-A>0\), and
\(C_A=B(A-1,1+A/2)\).  Direct substitution and cancellation in the
displayed \(G\) give

\[
 G(A+h)=
 \frac{2(Ab+(b+1)h)(2A+h)}{(A+h)(A+2Ah+2h^2)}.
\]

The denominator tends to \(A^2>0\), while the numerator tends to
\(4A^2b\), proving \(G(A+h)\to4b\).  Subtracting \(4b\) gives the stated
factorization

\[
 G(A+h)-4b=
 -\frac{2h(4A^2b+8Abh-Ab-2A+4bh^2-bh-h)}
 {(A+h)(A+2Ah+2h^2)}.
\]

For \(0<h\leq1\), the numerator polynomial has absolute value at most
\(M=4A^2b+9Ab+2A+5b+1\), and the denominator is at least \(A^2\).
Thus \(|G-4b|\) is at most \(K h\), where \(K=2M/A^2\).  If
\(b>C_A/4\), then with \(\Delta=4b-C_A>0\), the submitted choice

\[
 \varepsilon=\min\left\{\frac12,\frac{A(1-b)}{2b},
                    \frac{\Delta}{2K}\right\}
\]

is positive.  Every \(0<h<\varepsilon\) has
\(b<A/(A+h)\) and \(G(A+h)>C_A\).  This checks both the endpoint
quantifier and admissibility, rather than taking a limit outside the source
domain.  The restriction \(b<1\) is necessary and sufficient for fixed
\(b\geq0\) to remain admissible arbitrarily near this endpoint.

I also checked the official arXiv v1 text of (3.38).  Its left side factors
exactly as

\[
 L_{A,b}(h)=\frac{Ab+(b+1)h}{h^2}
 \left(1-\frac1{2hB(A/(A+h),2h)}\right).
\]

Writing \(d=-h/(A+h)\), \(u=2h\), and
\(F(z)=\log\Gamma(1+z)\), the logarithm of the beta factor is

\[
 \Phi(h)=F(d)+F(u)-F(d+u),\qquad
 L_{A,b}(h)=\frac{Ab+(b+1)h}{h^2}(1-e^{-\Phi(h)}).
\]

For \(0<h\leq1/4\), all three arguments are in the disk of convergence of

\[
 F(z)=-\gamma z+\sum_{n\geq2}\frac{(-1)^n\zeta(n)}n z^n.
\]

The linear terms cancel.  The quadratic and cubic terms are respectively

\[
 -\zeta(2)du=\frac{\pi^2h^2}{3(A+h)},
 \qquad
 \zeta(3)(d^2u+du^2)
 =\zeta(3)h^3\left(\frac2{(A+h)^2}-\frac4{A+h}\right).
\]

Expanding their \(A+h\) denominators produces exactly the submitted
\(c_2\) and \(c_3\).  The derivative of \(2/s^2-4/s\) has magnitude at
most \(1/2\) for \(s\geq2\).  For the terms of degree at least four,
\(|d|\leq h/2\), \(|u|\leq2h\), and
\(|d+u|\leq2h\), so

\[
 |R_{\geq4}|\leq\frac12\sum_{n\geq4}
 \bigl((h/2)^n+2(2h)^n\bigr)
 \leq\frac{897}{28}h^4.
\]

Together with the quadratic and cubic denominator remainders, this proves
the claimed \(K_\Phi h^4\) bound.  The elementary exponential remainder
\(|1-e^{-y}-y|\leq e^{|y|}y^2/2\) then yields the displayed
\(K_L(A,b)h^2\) bound after multiplication by the prefactor.  Re-expanding
that multiplication gives

\[
 L_{A,b}(h)=\frac{\pi^2b}{3}+D(A,b)h+R_L(h),
 \quad |R_L(h)|\leq K_L(A,b)h^2,
\]

with

\[
 D(A,b)=\frac{\pi^2}{3A}-2b\zeta(3)\left(2-\frac1A\right),
\]

exactly as claimed.

Let \(b_*=3C_A/\pi^2\).  The beta integral gives \(0<C_A\leq1/2\),
so \(0<b_*<1\).  When \(b\ne b_*\), the constant term and the submitted
explicit remainder bound determine the strict sign of \(L-C_A\) on an
admissible punctured neighborhood.  At equality, the linear coefficient
is positive: after clearing positive factors this is

\[
 \pi^4>18C_A\zeta(3)(2A-1).
\]

Indeed, \(C_A\leq1/(A-1)\), \(\zeta(3)<5/4\), and
\((2A-1)/(A-1)\leq3\), making the right side at most \(67.5<81<\pi^4\).
The stated choice \(h<D(A,b_*)/(2K_L(A,b_*))\), also capped for
admissibility, therefore gives \(L-C_A>D(A,b_*)h/2>0\).  Hence the local
condition (3.38) holds exactly for \(0\leq b<3C_A/\pi^2\), with equality
correctly assigned to the failing side.

## Independent attacks and source comparison

I checked the current official arXiv HTML for arXiv:2609.04833v1 against
the frozen locators.  Equation (3.38) is the expression used above;
Theorem 3.4 says that β_α depends only on α and then quantifies over all
near-endpoint \(p\); and its proof explicitly appeals to Corollary 3.5 via
(3.41)--(3.42).  Thus, for any fixed admissible \(b\geq b_*\), the proved
failure of (3.38) near the endpoint really prevents that corollary route
from establishing the natural uniform-in-\(b\) reading.  Since (3.38) is
only sufficient, this supplies neither an operator-level counterexample nor
a disproof of the norm identity; the frozen claim states both limitations.

Both submitted programs ran successfully.  Separately from those programs,
I derived the source factorization and coefficients again and used a fresh
90-digit verifier over \(A\) from just above 2 through approximately
\(10^4\), including \(b=0\), values on both sides of \(b_*\), \(b=b_*\),
and \(b\) near 1.  It checked 9,092 instances of the quantitative remainder
bound and 100 direct comparisons with the unfactored source expression;
the largest observed error/bound ratio was about 0.187283.  These finite
checks are only error-detection support; the series estimates above prove
the quantified statement.

The nearest result is Corollary 3.5 in the same v1 paper.  The precise delta
is the explicit second-order endpoint expansion, the sharp fixed-\(b\)
classification including its previously undecided equality case, and the
resulting diagnosis of the theorem's stated proof route.  This is a
non-routine, usable correction target for a current theorem proof.  A fresh
exact-title/identifier search found v1 and no correction or equivalent
endpoint treatment as of 2026-09-09; this remains a bounded literature
screen, not a priority guarantee.

I found no unresolved mathematical gap inside the frozen claim's stated
scope.  The result-note contribution, correctness, quantifiers, and honest
operator-level limitation all pass.
