# Research-pass resolution candidate

Provenance: `win-00086-p03-research-8b5997b41c8a`  
Date: 2026-09-10 (Asia/Shanghai)

## Exact theorem submitted for review

Over \(\mathbb F_{11}\), let \(f(x)=x^4\) and \(g(x)=x^8\), with
\(S_f,S_g\) and graph CCZ equivalence exactly as frozen in `source.md` and
interpreted in `problem.md`. Then \(S_f\) and \(S_g\) are projectively
equivalent, but \(\Gamma_f\) and \(\Gamma_g\) are not CCZ-equivalent.

## Projective certificate

Let
\[
M=\begin{pmatrix}1&0&0\\0&0&1\\0&1&0\end{pmatrix}.
\]
Its determinant is \(-1=10\ne0\) in \(\mathbb F_{11}\). It exchanges the
second and third coordinates, hence exchanges the affine zero point
\((0:0:1)\) and the added point \((0:1:0)\). For \(x\ne0\),
\[
M(x:x^4:1)=(x:1:x^4)=(x^{-3}:x^{-4}:1).
\]
Put \(u=x^{-3}\). Since \(\gcd(3,10)=1\), this substitution permutes
\(\mathbb F_{11}^{*}\), and \(u^8=x^{-24}=x^{-4}\), with exponents
reduced modulo 10. Hence the image is \((u:u^8:1)\), proving
\(M(S_f)=S_g\). The exact certificate lists all 12 images.

## CCZ invariant and separation

For any finite \(\Gamma\subset\mathbb F_{11}^2\), define
\[
\Delta_\Gamma(w)=\#\{(P,Q)\in\Gamma^2:P-Q=w\},\qquad w\ne0.
\]
If \(T(z)=Az+t\), where \(A\in\operatorname{GL}(2,11)\), then
\(T(P)-T(Q)=A(P-Q)\). The map on ordered pairs is a bijection, so
\(\Delta_{T\Gamma}(Aw)=\Delta_\Gamma(w)\). Because \(A\) permutes all
120 nonzero vectors, the 120-entry multiset is an affine-graph invariant.

For \(d\in\{4,8\}\), write \(\Delta_d=\Delta_{\Gamma_{x^d}}\). If
\(a\ne0\), substituting \(y=at\) into \((y+a)^d-y^d=b\) gives
\[
\Delta_d(a,b)=\#\{t\in\mathbb F_{11}:(t+1)^d-t^d=b/a^d\}.
\]
For \(a=0,b\ne0\), the count is zero. Direct evaluation for
\(t=0,1,\ldots,10\) gives
\[
((t+1)^4-t^4)_t=(1,4,10,10,6,0,5,1,1,7,10),
\]
with counts indexed by \(b=0,1,\ldots,10\)
\[
(1,3,0,0,1,1,1,1,0,0,3),
\]
and
\[
((t+1)^8-t^8)_t=(1,2,2,4,6,0,5,7,9,9,10),
\]
with indexed counts
\[
(1,1,2,0,1,1,1,1,0,2,1).
\]
For fixed \(a\ne0\), multiplication by \(a^{-d}\) permutes the 11 values
of \(b\). Adding the ten forced zeros at \(a=0,b\ne0\) gives
\[
\{0:50,\ 1:50,\ 3:20\}\quad(d=4),\qquad
\{0:30,\ 1:70,\ 2:20\}\quad(d=8).
\]
The histograms differ (their maxima are 3 and 2), so no affine permutation
maps \(\Gamma_f\) onto \(\Gamma_g\). Thus the functions are not
CCZ-equivalent.

`research_exact_certificate.json` freezes both full 120-entry tables and all
12 projective images. `research_independent_check.py` obtains the tables first
from the homogeneity identity, separately recomputes them by graph-pair
enumeration, and asserts entrywise equality. It imports no triage code and
uses no floating-point arithmetic or external package.

## Scope, prior form, and gap list

The projective half is already Example 2.11 of the cited primary paper. The
new-to-that-source step is the exact differential-spectrum obstruction to
CCZ equivalence. The multiset is the standard differential spectrum with ten
forced vertical zero entries adjoined; no novelty is claimed for the
invariant. The bounded live screen is in `research_literature_screen.md` and
is not a priority claim.

No mathematical gap is known in the frozen claim. It has not passed the
required fresh referee audit, so this is a resolution-paper candidate, not an
accepted result.

