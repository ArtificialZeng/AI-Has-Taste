# Precise problem interpretation

## Provenance and governing correction

The immutable `source.md` says `>=0` and attributes arXiv:2609.03738v1 to
Rostam. The supplied pre-triage correction identifies both as transcription
errors. The paper is by Thomas Gerber and Emily Norton, and the source-backed
research question is **strict** positivity in every degree. The literal
non-strict inequalities in `source.md` would be automatic because the
coefficients count finite sets; they are not the governing target.

Primary source: Gerber--Norton, *Enumerating cores of charged
multipartitions*, arXiv:2609.03738v1 (3 September 2026), especially Definitions
2.8 and 2.14, Lemma 2.11, Conjecture 3.10, Theorem 5.6, and equation (5.3).

## Definitions and normalization

Let

\[
\mathbb N=\{0,1,2,\ldots\}.
\]

A partition \(\mu=(\mu_1,\mu_2,\ldots)\) is eventually zero, weakly
decreasing, and has size \(|\mu|=\sum_k\mu_k\). A bipartition is
\(\boldsymbol\lambda=(\lambda^{(1)},\lambda^{(2)})\), of size
\(|\boldsymbol\lambda|=|\lambda^{(1)}|+|\lambda^{(2)}|\). For a partition
\(\mu\) and charge \(t\in\mathbb Z\), use the paper's beta-set convention

\[
S(\mu,t)=\{\mu_k-k+1+t:k\geq1\}.
\]

For \(a\in\{1,3\}\), the bipartition \(\boldsymbol\lambda\) is a
\((6,(0,a))\)-core exactly when the extended two-row abacus is nested, i.e.

\[
S(\lambda^{(1)},0)\subseteq S(\lambda^{(2)},a)
\subseteq S(\lambda^{(1)},6).
\]

Let \(C_{6,(0,a)}\) be this set. The formal power series (not a numerical
inequality for a value of \(q\)) is

\[
c_{6,(0,a)}(q)
=\sum_{\boldsymbol\lambda\in C_{6,(0,a)}}q^{|\boldsymbol\lambda|}
=\sum_{n\geq0}c_{6,(0,a)}(n)q^n,
\]

where \(c_{6,(0,a)}(n)\) is the nonnegative integer number of such
bipartitions of size \(n\).

## Exact target and quantifiers

Prove or disprove the conjunction

\[
\forall n\in\mathbb N:\quad c_{6,(0,1)}(n)>0
\quad\text{and}\quad c_{6,(0,3)}(n)>0.
\]

Equivalently, for every nonnegative integer \(n\), there exists at least one
\((6,(0,1))\)-core bipartition of size \(n\), and at least one
\((6,(0,3))\)-core bipartition of size \(n\). A single zero coefficient
disproves its corresponding universally quantified assertion. A negative
coefficient cannot arise under the counting definition. Finite positive
expansion is evidence only, not an all-orders proof.

## Nearest source result and scope

Theorem 5.6 labels both series “conjecturally yes.” Equation (5.3) proves

\[
\phi(q)c_3(q)^2=c_{6,(0,3)}(q)+2q\,c_{6,(0,1)}(q),
\]

where \(\phi(q)=\sum_{m\in\mathbb Z}q^{m^2}\) and \(c_3(q)\) is the ordinary
3-core partition series. Positivity of this sum does not imply positivity of
its two summands separately. The paper states that the two strict positivity
claims are equivalent to its \(e=6\) case of Conjecture 3.10 and says only that
they appear true by computer calculation; it gives no coefficient cutoff,
algorithm, or code for that calculation.

As of the 2026-09-06 triage search, the exact assertion and equivalent-language
searches located the original arXiv v1 but no separate proof or disproof. This
supports source status `open-supported`, not a claim of priority. The proposed
delta is an all-orders proof of both strict claims or an exact zero coefficient;
the nested beta-set test supplies an exact finite verifier for candidate
coefficients.
