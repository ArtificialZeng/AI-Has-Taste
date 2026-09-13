# Fresh mathematical referee report

## Frozen scope and integrity

I reviewed the exact `resolution-paper` claim frozen by snapshot digest
`7032172b209dfedee38fe1c802525ed47d607bca80262387017f426f5113d081`.
I recomputed every enumerated file hash and the canonical snapshot digest; all
match `audit/snapshot.json`.  The submitted scope is the full original claim:
it asserts a negative covariance at the exact interior point `(p,q)=(1,200)`
and also classifies every zero in the positive quadrant.  It is not a partial
claim presented as a resolution.

## Independent reconstruction

Put
\[
x=\sqrt p,\quad S=\sinh x,\quad C=\cosh x,\quad
A=xC-S,\quad B=A+qS.
\]
For the exponential local-time threshold, let
\(\phi=\Pr(\tau<\delta)\).  This transform can be recovered directly from
the probability model, rather than assumed from the submitted covariance
formula.  The radial function \(u(r)=\mathbb E_r e^{-p\tau}\) solves
\[
(\Delta-p)u=0\quad(0<r<1),\qquad
u_r(1)=q(1-u(1)),
\]
with the regular solution \(u(r)=c\sinh(xr)/r\).  The boundary condition gives
\(c=q/B\), and volume averaging gives
\[
\phi=3\int_0^1u(r)r^2\,dr=\frac{3qA}{x^2B}.
\tag{1}
\]
This also checks the factor dictated by the stated generator and local-time
normalization.  Since \(A(0)=0\) and \(A'(x)=x\sinh x>0\), one has
\(A>0\), hence \(B>0\), throughout the stated domain.

The moment identities can likewise be obtained without importing Appendix D.
Conditional survival is
\(\Pr(T>t\mid X)=e^{-pt-q\ell_t}\), while
\(\phi=\mathbb E(1-e^{-q\ell_\delta})\).  Tonelli and differentiation under
these exponentially dominated integrals give
\[
\mathbb ET=\frac{1-\phi}{p},\quad
\mathbb EL=\frac{\phi}{q},\quad
\mathbb ET^2=\frac{2(1-\phi)}{p^2}+\frac{2\phi_p}{p},\quad
\mathbb EL^2=\frac{2\phi}{q^2}-\frac{2\phi_q}{q}.
\tag{2}
\]
For completeness, with \(H_l=\inf\{t:\ell_t>l\}\), split the joint-survival
integral for \(\mathbb E(TL)\) into \(t<H_l\) and \(t>H_l\).  The two pieces
are respectively
\(\int_0^\infty\mathbb E[H_l e^{-pH_l-ql}]\,dl=-\phi_p/q\)
and
\(\int_0^\infty\mathbb E[\ell_t e^{-pt-q\ell_t}]\,dt=\phi_q/p\).
Thus
\[
\mathbb E(TL)=\frac{\phi_q}{p}-\frac{\phi_p}{q},\qquad
\operatorname{Cov}(T,L)
=\frac{-p\phi_p+q\phi_q+(\phi-1)\phi}{pq}.
\tag{3}
\]
Plateau endpoints of local time affect only null boundaries in these
nonnegative integrals.

Differentiating (1) independently yields
\[
\phi_q=\frac{3A^2}{x^2B^2},\qquad
\phi_p=\frac{3q\{xq(SC-x)-2AB\}}{2x^4B^2}.
\tag{4}
\]
Substitution in (3), followed only by \(B=A+qS\) and
\(AC-xS^2=x-SC\), gives
\[
\operatorname{Cov}(T,L)
=\frac{3}{4x^6B^2}\left[4x^2A^2
+q\{2x^3(x-SC)+12A^2\}\right].
\tag{5}
\]
Expanding the braces with the double-angle identities reproduces exactly the
frozen \(\xi_2(x^2)\), while \(4x^2A^2=\xi_1(x^2)\).  Hence (5) proves the
candidate's covariance formula with no possible zero or sign change hidden in
its prefactor.

## Global sign, zero set, and witness

Exact coefficient collection gives, for every \(x>0\),
\[
\xi_2(x^2)=-\sum_{n=5}^{\infty}
\frac{2^{2n-3}(2n-1)(2n-6)(2n-8)}{(2n)!}x^{2n}<0.
\tag{6}
\]
I checked the derivation: after the coefficients through degree eight cancel,
the coefficient at degree \(2n\) has polynomial factor
\[
-m(m-1)(m-2)-48m+12m(m-1)+48
=-(m-1)(m-6)(m-8),\quad m=2n.
\]
Every term in (6) is nonpositive and the first is strictly negative.
Meanwhile \(\xi_1=4x^2A^2>0\).  Therefore, for each \(p>0\), the affine
numerator has exactly one positive zero
\[
q_0(p)=-\frac{\xi_1(p)}{\xi_2(p)},
\]
is positive for \(0<q<q_0(p)\), and negative for \(q>q_0(p)\).  This is the
complete zero set because the denominator in (5) is strictly positive.

At \(p=1\), \(A=e^{-1}\).  Setting \(y=e^2\), direct exact algebra gives
\[
2y\{\xi_1(1)+200\xi_2(1)\}=8-200(y^2-4y-25).
\]
The positive exponential series gives
\[
e^2>\sum_{n=0}^{11}\frac{2^n}{n!}
=\frac{164591}{22275}>\frac{7389}{1000}.
\]
The function \(y^2-4y-25\) is increasing for \(y>2\), and its value at
\(7389/1000\) is \(41321/10^6>1/25\).  The displayed numerator is therefore
strictly negative, proving the exact counterexample
\(\operatorname{Cov}_{1,200}(T,L)<0\).

## Variances, edge cases, and evidence checks

The sign equivalence with Pearson correlation is valid.  Both second moments
are finite because \(0\le T\le\delta\) and
\(0\le L\le\widehat\ell\).  For any fixed \(t>0\), both
\(\Pr(T<t)>0\) and \(\Pr(T>t)>0\), so \(T\) is nonconstant.  Moreover
\(L=0\) with positive probability when the bulk clock rings before the first
boundary hit, while (1) gives \(\mathbb EL=\phi/q>0\); hence \(L\) is
nonconstant.  Thus both variances are strictly positive.  The audit uses only
\(p,q>0\); axes and limiting points are not inserted into the claim, and all
divisions above have positive denominators.

The submitted `evidence/verify_symbolic.py` could not be executed in this
environment because SymPy is not installed.  I treated that as an operational
limitation, not as evidence for or against the theorem.  Instead I wrote and
ran `audit/referee_verify.py`, which uses only the Python standard library and
independently checks the snapshot, exact formal-series identities through
degree 80 (together with the displayed general coefficient factorization), and
the rational counterexample certificate.

The frozen evidence enumerates `source.md` and `problem.md` but not the primary
PDF.  Accordingly, the source comparison here is to the exact frozen statement
and its transcribed formula: that source reports positivity only on an explored
range and supplies no full-quadrant theorem.  I do not certify broader
bibliographic novelty or the external PDF transcription in this mathematical
audit.  This is not a correctness dependency, because (1)--(5) reconstruct the
needed transform and covariance from the frozen probability model itself.  The
candidate makes no broader priority claim.

## Verdict

**Accept.**  The argument disproves the original universal assertion at an
exact point, proves the claimed covariance identity, verifies strictly positive
variances, and classifies the entire positive-quadrant zero set.  I found no
unresolved mathematical gap or mismatch in the frozen candidate scope.
