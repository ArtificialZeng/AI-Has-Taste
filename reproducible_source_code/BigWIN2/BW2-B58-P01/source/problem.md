# Precise reading

## Frozen claim

Let \(v\in[0,1)\). For real \(x\), write
\(\{x\}=x-\lfloor x\rfloor\in[0,1)\), and interpret ``mod 1'' as the
unique representative in \([0,1)\). Define

\[
\alpha_v=\{20v\},\qquad \beta_v=\{41v\},\qquad
\gamma_v=\{40v\},\qquad z(y)=(1/2-y)\bmod 1
\]

for \(0\le y<1\), and

\[
h_v(y)=2\lfloor20v\rfloor-\lfloor41v\rfloor
 +2\mathbf 1_{z(y)<\alpha_v}-\mathbf 1_{z(y)<v}
 +\mathbf 1_{y>\beta_v}.
\]

The quantity \(\gamma_v\) is part of the source's surrounding notation but
does not occur in the identity under investigation.

To make the continuum multiset precise, put
\(X=[0,1)\times\mathbb Z_{\ge0}\), equip it with Lebesgue measure in the
first coordinate and counting measure in the second, and set

\[
c_v(y,r)=h_v(y)+2r.
\]

For every real \(s\ge0\), interpret the source's “integral of the lowest
\(s\) units of mass” as

\[
K_v(s)=\inf\left\{\int_A c_v\,d\mu:
 A\subseteq X\text{ measurable and }\mu(A)=s\right\}.
\]

Equivalently, if \(\lambda_v\) is the nondecreasing generalized quantile of
the costs \(c_v\), then \(K_v(s)=\int_0^s\lambda_v(t)\,dt\). Portions of a
positive-measure tie may be selected arbitrarily; their common cost makes
the value independent of that choice. Strict versus non-strict inequalities
at the finitely many \(y\)-endpoints change only null sets and hence do not
change \(K_v\).

The universally quantified claim is

\[
\boxed{\quad
\forall v\in[0,1)\ \forall n\in\mathbb Z_{\ge1},\qquad
K_v(n+v)=n^2+K_v(1+v)-1.
\quad}
\]

The case \(n=1\) is tautological. The first nontrivial case is \(n=2\).
Parameter values at which a floor, fractional part, interval endpoint, or
ordering changes remain inside the universal quantifier and must be checked,
not discarded as measure-zero values of the parameter \(v\).

## Step-function and verification scope

For fixed \(v\), \(h_v\) is constant away from the sorted distinct points

\[
0,\ 1,\ \tfrac12,\ \beta_v,\
(\tfrac12-\alpha_v)\bmod1,\
(\tfrac12-v)\bmod1.
\]

Thus an exact disproof consists of a rational \(v\), an integer \(n\ge2\),
the complete interval/mass/cost ledger, and unequal rational values of the
two sides. An exact proof must cover every parameter cell and every parameter
breakpoint and justify the claimed quantile periodicity; finite sampling is
not sufficient.

If the identity fails, the downstream audit is deliberately narrower than
the paper's main headline: equation (6.11) invokes (6.10) directly;
(6.17)--(6.18), Proposition 6.3 and its constant \(c_{\rm odd}\), Proposition
9.5, and Theorem 9.1 then use the resulting small-prime formula. The final
Theorem 1.1 invokes Theorem 9.1. Failure of this local lemma would invalidate
that displayed dependency chain as written, but would neither prove Catalan's
constant rational nor rule out a repaired irrationality proof.

## Source status and target contribution

Source status: **status-uncertain**. Z.-W. Sun,
*Catalan's constant is irrational*, arXiv:2609.04176v1 (submitted 2026-09-03),
Section 6, equations (6.2)--(6.10), states the claim as Lemma 6.6. Its printed
proof says the ordering is constant on a later breakpoint partition and calls
the conclusion an exact finite verification, but does not publish the cell
ledger or a checker. The arXiv record and HTML were inspected on 2026-09-07:
https://arxiv.org/abs/2609.04176 and
https://arxiv.org/html/2609.04176v1 . A narrow exact-phrase/equivalent-language
search of arXiv on 2026-09-07 found no separate proof or critique; that is not
a priority or open-status claim.

Nearest prior result X: Lemma 6.6 asserts the full identity, with the decisive
finite verification omitted. Proposed delta Y: either an exact counterexample
with a scoped dependency audit, or an independently reproducible universal
cell certificate (preferably exposing a reusable quantile-shift criterion).
Verification route Z: exact rational breakpoint enumeration, exact interval
mass/cost sorting, and symbolic certification of
\(\lambda_v(s+1)=\lambda_v(s)+2\) on all cells and boundary parameters.

