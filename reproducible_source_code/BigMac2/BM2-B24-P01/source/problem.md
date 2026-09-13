# Precise reading of the frozen problem

## Objects and conventions

- The ambient space is the Riemann sphere \(\widehat{\mathbb C}\), with
  convergence and equicontinuity understood in the spherical metric.
- The parameter is fixed once and for all at \(n=18\). Define
  \[
  p_{18}(z)=z(z^{18}-1),\qquad
  \mu_{18}=\{\zeta\in\mathbb C:\zeta^{18}=1\},
  \]
  so the complete root set is \(R=\{0\}\cup\mu_{18}\). These 19 roots are
  distinct.
- The map under study is the rational self-map of \(\widehat{\mathbb C}\)
  obtained by extending
  \[
  C_{18}(z)=
  \frac{z^{19}(12654z^{36}-684z^{18}-306)}
       {2(19z^{18}-1)^3}.
  \]
  Thus the zeros of \(19z^{18}-1\) are poles and the value at infinity is
  interpreted on the sphere. The displayed coefficients agree with the
  general formula in Equation (3) of the supplied source after setting
  \(n=18\): \(18\cdot19\cdot37=12654\),
  \(2\cdot18\cdot19=684\), and \(18\cdot17=306\).
- Write \(C_{18}^{m}\) for the \(m\)-fold iterate. Its Fatou set
  \(\mathcal F(C_{18})\) is the largest open subset of
  \(\widehat{\mathbb C}\) on which the family of iterates is normal
  (equivalently, equicontinuous in the spherical metric). The notation
  \(\pi_0(\mathcal F(C_{18}))\) means the set of connected components of
  this open set.
- For \(r\in R\), its full attracting basin is
  \[
  B(r)=\{z\in\widehat{\mathbb C}:C_{18}^{m}(z)\longrightarrow r
  \text{ as }m\to\infty\}.
  \]

## Exact target and quantifiers

The frozen claim is
\[
\boxed{
\forall U\in\pi_0(\mathcal F(C_{18}))\;\exists r\in R\;
\forall z\in U,\quad C_{18}^{m}(z)\longrightarrow r
\quad(m\to\infty).}
\]
The root \(r\) may depend on the Fatou component \(U\), but not on the point
\(z\) within that component. Equivalently, every Fatou point belongs to one
of the 19 root basins. Since an attracting fixed point's basin lies in the
Fatou set, this can also be written
\[
\mathcal F(C_{18})=\bigcup_{r\in R}B(r).
\]
Accordingly, a proof must exclude every Fatou component whose eventual
periodic component has non-root dynamics (for example a non-root attracting
or parabolic cycle or a rotation domain); preperiodic components are included
in the universal quantifier. The no-wandering-domain theorem may be invoked
only as a theorem for rational maps, not as a numerical observation.

## Scope and boundary cases

The claim concerns all points of every Fatou component, including components
not containing a root. It makes no assertion about points of the Julia set,
Lebesgue-exceptional starting points, convergence rate, or numerical stopping
criteria. It is only about \(n=18\): it neither proves the analogous statement
for another even \(n\ge18\), nor classifies Julia-set topology or basin
topology. A finite computation showing that free critical orbits become small
is not by itself the target theorem; the implication from the certified orbit
information to the above exhaustive Fatou-component statement must also be
proved.

No ambiguity affecting the truth value was found in the frozen statement.
In particular, “convergent” is read in the source's complex-dynamical
root-finding sense, not as convergence of every initial point on
\(\widehat{\mathbb C}\).

## Nearest supplied result and source status

The primary source is T. Nayak and P. Phogat, *Chebyshev's method applied to
polynomials with rotational symmetry*, arXiv:2609.02884v1,
<https://arxiv.org/abs/2609.02884>, submitted 2026-09-02 and retrieved
2026-09-09. The fixed local copy is
`literature/2609.02884v1.pdf` (SHA-256
`afe10caa52713e3a0bff4d5830751e7bebd151d666b1ad28dc98e6cab419f569`).
Its PDF p. 3 defines convergence and states Theorem D, which proves convergence
when \(n\le16\) or \(n\) is odd; hence that theorem does not cover \(n=18\).
Equation (3) on PDF p. 6 specializes to the displayed map. The concluding
question on PDF p. 27 asks whether convergence holds for every even
\(n\ge18\), while the \(n=18\) row on PDF p. 28 is expressly numerical.

Thus the frozen \(n=18\) instance is **open-supported by the supplied v1
source**, rather than already settled there. Exact-title, exact-question, and
formula-focused arXiv searches on 2026-09-09 found that source and no separate
resolution; this limited search is not a proof of priority or current open
status beyond the inspected sources.

## Proposed first research delta

Nearest prior result: convergence for \(n\le16\) or odd \(n\). Proposed delta:
resolve the first omitted value \(n=18\). First verification route: certify in
exact arithmetic the proposed second-iterate inequalities for a representative
free critical point and the comparison threshold \(t_*\), then separately
audit the complex-dynamical implication from that orbit certificate to the
exhaustive Fatou-component claim. This is a route to test, not an established
lemma.
