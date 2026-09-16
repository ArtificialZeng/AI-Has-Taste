# Bounded recovery decision and new feasibility evidence

Job `newwin-00001-p20-triage-41e54da15a7f`; 2026-09-12.
Decision: **advance** to one bounded research pass. Workflow contribution
`none`; original status `unresolved`. This is no mathematical acceptance.

Both supplied handoffs were read. The three artifacts named in the recovery
handoff have their stated SHA256 hashes. Their algebra was rechecked from
the frozen definition; the old 4212 floating-point samples were inspected
but not rerun or promoted to certificates. The previous budget exhaustion
has no mathematical implication.

## New elementary route to the local remainder

Write
\[
q_{m,j}=4^{-m}\binom{2m}{m+j},\qquad
p_{m,j}=2^{-(2m-1)}\binom{2m-1}{m+j}.
\]
For admissible odd-binomial indices,
\(p_{m,j}=(1-j/m)q_{m,j}\), while even-binomial symmetry gives
\(q_{m,j}=q_{m,-j}\). For integers \(0\le r\le m\), the factorial
definition yields the exact product
\[
R_{m,r}:=q_{m,r}/q_{m,0}
=\prod_{\ell=1}^{r}\frac{1-(\ell-1)/m}{1+\ell/m}.
\]
If \(0\le r\le m/2\), the elementary estimate
\[
|\log(1+u)-u+u^2/2|\le\frac{2}{3}|u|^3
\quad (|u|\le1/2)
\]
follows by bounding the convergent logarithmic series from degree three.
Apply it separately to the numerator and denominator factors. Summing
their linear and quadratic terms gives
\[
\left|\log R_{m,r}+\frac{r^2}{m}-\frac{r^2}{2m^2}\right|
\le \frac{r^2(r^2+1)}{3m^3}. \tag{P}
\]
Here the exact identities used are
\(\sum_{\ell=1}^r(2\ell-1)=r^2\) and
\(\sum_{\ell=1}^r[(\ell-1)^3+\ell^3]=r^2(r^2+1)/2\).
Consequently, for fixed \(B>0\), \(m\ge\max(1,4B^2)\), and
\(r\le B\sqrt m\),
\[
\left|\log R_{m,r}+r^2/m\right|
\le \frac{5B^2/6+B^4/3}{m}.
\]
Thus a uniform displacement estimate is feasible without a global tail
theorem. Combining this elementary bound with a remainder bound for the
single central coefficient \(q_{m,0}\) is the concrete next route to
lemma (L) in `triage-symmetry.md`. This calculation is an elementary
feasibility lemma, with no claim of novelty or of a completed source theorem.

The separate exact script `triage-product-check.py` checks the product,
odd/even conversion, and power-sum algebra in its recorded finite ranges;
the analytic inequality (P) is justified by the displayed argument,
not by those finite checks.

## Coefficients and the remaining uniform estimate

The exact odd-center identity is
\(S_{m,-1}=1/2\), where
\(S_{m,d}=\Pr\{\mathrm{Bin}(2m-1,1/2)\le m+d\}\).
The upper branch is exactly
\[
E_{m,m+d}=S_{m,-d-2}/p_{m,d}+2m(d+1)/(m+d+1),\quad d\ge0.
\]
The lower branch is \(S_{m,d}/p_{m,d}\). These agree with the prior
artifact. Assuming its local lemma (L) with a uniform remainder, signed
trapezoidal summation gives (C); both positive and negative finite sums
have endpoint term \(h[f(0)+f(dh)]/2\), for \(h=m^{-1/2}\).
The local linear correction contributes
\(-h\int_0^{dh} t f(t)\,dt\), so the net first correction is
\(h f(dh)\), with \(f(t)=e^{-t^2}/\sqrt\pi\).

The proposed coefficients can therefore be written compactly as
\[
H(x)=\frac{\sqrt\pi}{2}e^{x^2}\operatorname{erfc}(|x|),\quad
x_+=\max(x,0),
\]
\[
F_0(x)=H(x)+2x_+,\qquad
F_1(x,\delta)=(2\delta+1)xH(x)+\delta+1-2x_+^2.
\]
Here \(\operatorname{erfc}(z)=2\pi^{-1/2}\int_z^\infty e^{-t^2}dt\).
These remain a conditional proposal until the complete error propagation
is supplied. In particular, a bare CDF error \(O(m^{-1/2})\) is too large
after division by a mass of order \(m^{-1/2}\).

The central branch jump is exactly
\(E_{m,m}-E_{m,m-1}=(m-1)/(m+1)\). At \(x=0\), the proposal has
\(F_0(0)=\sqrt\pi/2\) and \(F_1(0,0)=1\); approaching zero within the
left floor cell gives \(\delta\to-1\), as required. These boundary
identities do not themselves establish a uniform error.

## Admission and one next test

Nearest prior result: the exact expectation, outer bounds, and central
value in Corollary 7.2 of Insko--Johnson--Sullivan. Proposed delta: an
explicit two-term approximation over the whole bounded central window,
including the lattice correction and an absolute uniform error. The
published near-center question gives this short application value;
the general binomial method is classical. The later multi-lane theorem
has different conditioning and no such remainder (see the literature log).
No equivalent expansion was found in the bounded inspected material;
priority and the value of a short resulting note remain review questions.

**One next test:** use (P), a rigorous central-binomial Stirling remainder,
and signed trapezoidal bounds to prove (L) and (C) on
\(|j|\le(A+3)\sqrt m\); propagate the constants through both exact
branches to the proposed \(F_0,F_1\), including all floor-cell endpoints
and \(x=0\), with the frozen \(O_A(m^{-1/2})\) error. This proof test,
rather than additional numerical calibration, decides the named claim.
