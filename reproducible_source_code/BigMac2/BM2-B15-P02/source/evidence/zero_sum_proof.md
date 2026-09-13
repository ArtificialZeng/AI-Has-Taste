# Exact zero-sum proof of the critical first-failure asymptotic

## Claim proved

Let \(q=1/(1+\cosh a)\), \(a>0\), and

\[
 S_m(a)=(-1)^{m+1}\kappa_{2m}(q),\qquad
 m_*(a)=\min\{m\geq2:S_m(a)<0\}.
\]

The minimum exists for every \(a>0\). If

\[
 \beta=\arctan(a/\pi),\qquad t(a)=\frac{\pi}{4\beta},
\]

then, for all sufficiently small \(a>0\),

\[
                 t(a)<m_*(a)\leq \lceil t(a)+1\rceil<t(a)+2.       \tag{1}
\]

Consequently

\[
 \lim_{a\downarrow0}a\,m_*(a)=\frac{\pi^2}{4}.
\]

For the parametrization in source.md,
\(\cosh a=e^\varepsilon\) when
\(\Delta=\log2+\varepsilon\), so \(a/\sqrt\varepsilon\to\sqrt2\).
It follows that

\[
 \boxed{\displaystyle
 \lim_{\varepsilon\downarrow0}\sqrt\varepsilon\,
 m_*(\log2+\varepsilon)=\frac{\pi^2}{4\sqrt2}.}
\]

## Exact sign formula

Since \((1-q)/q=\cosh a\),

\[
 M_q(z)=\frac{\cosh z+\cosh a}{1+\cosh a}
 =\frac{\cosh((z+a)/2)\cosh((z-a)/2)}{\cosh^2(a/2)}.
\]

Put \(f(w)=\log\cosh w\), using the analytic germ at each real
argument. For every integer \(m\geq1\), differentiation gives

\[
 \kappa_{2m}(q)=2^{1-2m}f^{(2m)}(a/2).                         \tag{2}
\]

Euler's product

\[
 \cosh w=\prod_{k=0}^{\infty}
 \left(1+\frac{4w^2}{\pi^2(2k+1)^2}\right)
\]

(equivalently, the Euler product for cosine with imaginary argument)
may be differentiated term by term at real \(w\). For derivatives of
order at least two the resulting series is locally normally convergent.
Writing \(y_k=\pi(2k+1)/2\) gives

\[
 f^{(2m)}(x)=-(2m-1)!\sum_{k=0}^{\infty}
 \bigl((x-iy_k)^{-2m}+(x+iy_k)^{-2m}\bigr).                    \tag{3}
\]

At \(x=a/2\), define

\[
 \beta_k=\arctan\frac{a}{\pi(2k+1)}.
\]

The argument of \(x+iy_k\) is \(\pi/2-\beta_k\). Substitution in
(2)--(3), including all powers of two, yields the exact absolutely
convergent identity

\[
 \boxed{
 S_m(a)=4(2m-1)!\sum_{k=0}^{\infty}
 \frac{\cos(2m\beta_k)}
 {\bigl(a^2+\pi^2(2k+1)^2\bigr)^m}.}                            \tag{4}
\]

Thus no fixed-\(a\) big-O estimate is being used in the coupled regime.

Formula (4) also proves that the minimum exists for every \(a>0\),
without an appeal to the prior fixed-parameter result. For fixed \(a\),
the relative tail

\[
 \sum_{k\geq1}
 \left(\frac{a^2+\pi^2}{a^2+\pi^2(2k+1)^2}\right)^m
\]

tends to zero geometrically: bound every ratio except one power by the
strictly subunit \(k=1\) ratio, and sum the remaining powers, which form
a convergent \(O(k^{-2})\) series. Meanwhile there are infinitely many
integers \(m\) for which \(\cos(2m\beta_0)\leq-1/2\). If
\(\beta_0/\pi\) is irrational this follows from density of its multiples
modulo one; if it is rational, multiplication by its numerator permutes
the residue classes modulo its denominator, and a residue in
\([1/3,2/3]\) recurs periodically. Along this subsequence the negative
\(k=0\) term eventually dominates the tail, so \(S_m(a)<0\).

## All earlier orders have the required sign

The angles satisfy \(0<\beta_k\leq\beta_0=\beta\), strictly for
\(k\geq1\). If \(m\leq t(a)=\pi/(4\beta)\), then
\(0<2m\beta_k\leq\pi/2\). Every summand in (4) is nonnegative, and at
least the terms with \(k\geq1\) are strictly positive even in the
equality case. Hence

\[
                         S_m(a)>0\quad(m\leq t(a)).              \tag{5}
\]

In particular, any strict failure must satisfy \(m_*(a)>t(a)\).

## A failing order within two lattice steps

Let

\[
 n(a)=\lceil t(a)+1\rceil.
\]

Then

\[
 \frac\pi2+2\beta\leq2n(a)\beta<\frac\pi2+4\beta.
\]

For sufficiently small \(a\) (so in particular \(\beta<\pi/8\)), this
interval lies in \((\pi/2,\pi)\), and therefore

\[
                         \cos(2n(a)\beta)\leq-\sin(2\beta).      \tag{6}
\]

Normalize the absolute contribution of all \(k\geq1\) terms in (4) by
the \(k=0\) weight. When \(a\leq\pi\),

\[
 \begin{aligned}
 R_m(a)
 &:=\sum_{k=1}^{\infty}
 \left(\frac{a^2+\pi^2}{a^2+\pi^2(2k+1)^2}\right)^m\\
 &\leq
 \left(\frac29\right)^{m-1}
 \sum_{k=1}^{\infty}\frac{2}{(2k+1)^2}
 =\left(\frac29\right)^{m-1}\left(\frac{\pi^2}{4}-2\right).   \tag{7}
 \end{aligned}
\]

Now \(n(a)\asymp1/\beta\), so the last expression in (7), evaluated at
\(m=n(a)\), is \(o(\beta)\), whereas
\(\sin(2\beta)\sim2\beta\). Hence, for all sufficiently small \(a\),

\[
                         R_{n(a)}(a)<\sin(2\beta).               \tag{8}
\]

Equations (4), (6), and (8) show \(S_{n(a)}(a)<0\). Together with (5),
this proves (1).

Finally, (1) implies \(\beta m_*(a)\to\pi/4\), and
\(a/\beta\to\pi\), proving the asserted \(a\)-limit. The elementary
expansions \(e^\varepsilon=1+\varepsilon+O(\varepsilon^2)\) and
\(\cosh a=1+a^2/2+O(a^4)\) give the stated conversion to the frozen
\(\varepsilon\)-normalization.

## Exact computational cross-check (not used as proof)

The script evidence/exact_recurrence.py evaluates the moment--cumulant
recurrence for \(q_N=N/(2N+1)\) using integer numerators and independently
cross-checks a prefix with Python Fraction. The first failures for
\(N=20,100,1000,2000\) are respectively \(8,18,56,79\); the corresponding
values of \(\operatorname{arcosh}(1+1/N)m_*\) are approximately
\(2.5193980528,2.5434678507,2.5041874821,2.4980952716\), consistent with
\(\pi^2/4\approx2.4674011003\). Exact signs, rather than these displayed
floats, determine every reported first failure. The larger run through
\(N=100000\) is recorded in evidence/exact_sequence.tsv.

## Literature comparison and gap list

Sheng Chun Yu, *A note on Ursell functions for the Blume--Capel model*,
arXiv:2609.04610v1 (2026), Proposition 4 and equations (8)--(9), proves
existence of a failing order for each fixed \(a>0\) using the nearest four
zeros. Its displayed error estimate is fixed-parameter and it does not
state the first-failure critical asymptotic or the two-lattice-step bound
(1). A bounded arXiv/web search on 2026-09-08 using the title, the proposed
constant, and combinations of “Blume--Capel”, “Ursell”, “first failure”,
and “cumulant” found that paper but no equivalent result. This is a search
report, not a priority claim.

Known proof gaps: none. The external mathematical dependencies are the
classical Euler product for cosine/cosh and the elementary density theorem
for irrational rotations; both are used explicitly above.
