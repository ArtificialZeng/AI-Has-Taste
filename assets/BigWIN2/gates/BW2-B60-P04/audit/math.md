# Fresh mathematical audit

Job: `win-00060-p04-referee-b16eff59ce1d`  
Frozen snapshot: `314940b1697a076f5c82d0c35556ea3a0ce9a8b08912a6beb2324093f5163b02`

## Frozen scope reviewed

I reviewed the exact `resolution-paper` statement in `claim.json`, the immutable source and precise reading, every file in the frozen snapshot, and the cited primary source at Definitions 3.1--3.3, Theorem 3.7, Algorithm 1 in Section 4.1, the first differential-parameter row in Section 4.2, and the conclusion. All frozen file hashes agree with `audit/snapshot.json`.

The candidate is expressly limited to the characteristic-zero, two-state, one-input affine-linear dense degree row, with algebraically independent derivation-constant model coefficients. I did not reinterpret it as a claim about nonlinear systems, variable model coefficients, positive characteristic, or a general sharp support theorem.

## Reconstruction of the decisive argument

Write
\[
x'=Ax+bu+c,\qquad y=p^Tx+q,
\]
and put \(\tau=\operatorname{tr}(A)\), \(\delta=\det(A)\). Because every model coefficient is a derivation constant,
\[
y'=p^TAx+p^Tb\,u+p^Tc,
\]
\[
y''=p^TA^2x+p^TAb\,u+p^TAc+p^Tb\,u'.
\]
Substitution of the two-by-two Cayley--Hamilton identity \(A^2-\tau A+\delta I=0\) gives, identically over the independent coefficient ring,
\[
E=y''-\tau y'+\delta y+p^T(\tau I-A)b\,u-p^Tb\,u'
  +p^T(\tau I-A)c-\delta q=0.
\]
No finite-field inference enters this identity.

To check minimality rather than merely vanishing, let
\[
O=\begin{pmatrix}p^T\\p^TA\end{pmatrix},\qquad
\Omega=\det O
=p_1^2a_{12}+p_1p_2(a_{22}-a_{11})-p_2^2a_{21}.
\]
This is not the zero polynomial. Over the input differential-function field,
\[
\binom{y-q}{y'-p^Tb\,u-p^Tc}=Ox.
\]
Thus \(\Omega\ne0\) makes \((y,y')\) an invertible affine coordinate system on the state plane. In particular \(y,y'\) are algebraically independent and the order cannot be below two. In these coordinates, \(y''\) is exactly the affine-linear function prescribed by \(E\). Polynomial division in the monic variable \(y''\) therefore gives the full kernel as \((E)\). Hence the image is the closed graph cut out by \(E\); the polynomial is primitive and irreducible because its \(y''\)-coefficient is one and its \(y''\)-degree is one. This matches Definition 3.3, not merely the existence of a differential consequence.

## Independent nonvanishing and support checks

I used a coefficient specialization different from the one in the submitted certificate:
\[
A=\begin{pmatrix}2&3\\5&7\end{pmatrix},\quad p^T=(1,2),\quad
b=(3,4)^T,\quad c=(5,6)^T,\quad q=7.
\]
At this point the six factors
\[
(\Omega,\tau,\delta,p^Tb,p^T(\tau I-A)b,
p^T(\tau I-A)c-\delta q)
\]
are
\[
(-7,9,-1,11,-5,-2).
\]
Their product is \(6930\ne0\). This independently proves that the stated polynomial \(P\) is nonzero and that its nonvanishing locus is nonempty. On that locus the coefficients of
\(y'',y',y,u',u,1\) are respectively
\[
1,-\tau,\delta,-p^Tb,p^T(\tau I-A)b,
p^T(\tau I-A)c-\delta q,
\]
so all six are nonzero. I also executed the frozen exact symbolic certificate with Python 3; it returned the zero universal identity, the stated observability determinant, seven support-bound candidates, and the six-term actual support.

For the specialized Theorem 3.7 inequalities, the total-degree inequality forces every candidate to be either the constant or one of the six individual variables \(u,u',u'',y,y',y''\). Direct substitution in the remaining inequalities retains all seven. The proved eliminant contains the other six and no \(u''\), so the missing monomial is exactly \(u''\) and every support exponent satisfies \(\ell_2=0\).

## Quantifier and source attacks

The only inversion in the order/defining-ideal argument is by \(\Omega\), which is explicitly nonzero on the claimed locus. The additional factors in \(P\) exclude every coefficient cancellation relevant to the exact six-term support. The monic normalization removes scalar ambiguity. Empty-locus, division-by-zero, hidden specialization, and lower-order-relation attacks therefore fail on the frozen scope. The constancy of the model coefficients is essential and is stated explicitly; differentiating time-varying coefficients would produce additional terms, but that case is outside the claim.

The primary source defines the eliminant as the primitive irreducible hypersurface equation, provides Theorem 3.7's support inequalities, and reports only the stable finite-field count \(7\to6\) for this row. It does not identify the missing monomial or give this symbolic row calculation in the inspected locations, and its conclusion leaves sharper differential-input support descriptions open in general. The candidate claims only the exact row-wise symbolic upgrade, not priority for a general theorem. The neighboring-literature descriptions in `problem.md` are metadata-level and were not needed for any mathematical inference in the proof.

## Verdict

**Accept.** The argument settles the immutable problem in its full frozen scope, proves the generic eliminant and order, identifies the exact six-term support and missing \(u''\), and supplies a valid nonempty Zariski-open certificate. I found no unresolved mathematical gap requiring a claim revision.
