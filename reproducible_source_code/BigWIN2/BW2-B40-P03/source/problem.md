# Precise reading of the frozen problem

## Statement

Let
\[
V=\{0,1\}^4\subset \mathbb R^4
\]
and assign a real variable \(x_v\ge 0\) to each of the sixteen vertices
\(v\in V\). All quantification below is simultaneous over
\(x=(x_v)_{v\in V}\in\mathbb R_{\ge0}^{16}\).

For an unordered five-element subset \(S=\{v_0,\ldots,v_4\}\subset V\),
define
\[
 \operatorname{Vol}(S)=4!\,\operatorname{vol}_4(\operatorname{conv}S)
 =\left|\det[v_1-v_0\;v_2-v_0\;v_3-v_0\;v_4-v_0]\right|.
\]
Thus \(\operatorname{Vol}(S)=0\) when the five vertices are affinely
dependent. The definition is independent of the displayed ordering of \(S\).

For \(i\in\{1,2,3,4\}\) and \(b\in\{0,1\}\), let
\[
 F_{i,b}=\{v\in V:v_i=b\}.
\]
These are precisely the eight facets, and the proposed inequality is
\[
 A(x)T(x)^3\le B(x),
\]
where
\[
 A(x)=\sum_{S\in\binom V5}\operatorname{Vol}(S)\prod_{v\in S}x_v,
 \qquad T(x)=\sum_{v\in V}x_v,
\]
and
\[
 B(x)=\prod_{i=1}^4\prod_{b=0}^1\left(\sum_{v\in F_{i,b}}x_v\right).
\]
Equivalently, the frozen claim is the copositivity assertion
\[
 H_4(x):=B(x)-A(x)T(x)^3\ge0
 \quad\text{for every }x\in\mathbb R_{\ge 0}^{16}.
\]
Both sides and \(H_4\) are homogeneous of degree eight. “Global
nonnegativity” is read as nonnegativity on the closed nonnegative orthant, not
on all of \(\mathbb R^{16}\). If one facet sum vanishes, all positive-support
vertices lie in the opposite three-dimensional facet; then every contributing
five-set has normalized four-volume zero, so both sides vanish. Hence a strict
counterexample must have all eight facet sums positive.

## What resolves this problem

A disproof is an explicitly indexed vector in
\(\mathbb Q_{\ge 0}^{16}\) for which the exact rational value
\(H_4(x)<0\). A proof must certify \(H_4(x)\ge0\) over the entire nonnegative
orthant; finite sampling, floating-point optimization, or an inexact SOS output
does not suffice. The scope is only \(d=4\), which is the paper's geometric
dimension \(n=d+1=5\); no assertion about every \(d\ge4\) is included.

## Source validation and nearest prior result

The primary arXiv HTML for version 1, retrieved 2026-09-06, defines
\(\operatorname{Vol}(S)=d!\operatorname{vol}(\operatorname{conv}S)\) and gives
the general hypercube inequality as equation (2), restated as equation (16) in
Section 4.4. Theorem 5.1 and Section 6 prove the preceding case \(d=3\)
(corresponding to \(n=4\)); Remark 6.1 gives an SOS-plus-nonnegative
certificate and Theorem 6.2 treats equality. Section 7.5 explicitly says that
the case \(d=4\), with sixteen variables and degree eight, remains open.

The frozen source's bibliographic attribution is inconsistent with the linked
record: arXiv:2608.14909v1 lists Gennadiy Averkov, Katherina von Dichter, and
Ivan Soprunov, rather than Shiri Artstein-Avidan and Yaron Sadovsky. This
metadata correction is recorded separately and does not modify `source.md` or
the unambiguous mathematical statement.

Primary record inspected:
https://arxiv.org/html/2608.14909v1 (especially Introduction contributions
(iii)--(v), Section 4.4, Section 6, and Section 7.5). An arXiv-domain search on
2026-09-06 found this record but no separate primary paper settling \(d=4\).
That limited search supports the label `open-supported`; it is not a claim of
exhaustive priority or literature coverage.
