# Precise problem reading

## Frozen data and definitions

Let \(n=34\), with all indices in \(\mathbb Z_{34}\). Decode the digits
\(0,1,2,3\) as \(1,i,-1,-i\), respectively, and fix

\[
A=2202202000022020222202000220200020,\qquad
B=1133303133112311101113211331303331.
\]

Both words have exactly 34 entries. For a word \(X\), \(r\in\mathbb Z_{34}\),
and \(k\in\mathbb Z_{34}^{\times}\), define

\[
(c_rX)_j=X_{j-r},\qquad (d_kX)_j=X_{jk^{-1}}.
\]

Thus \(c_r d_k\) means: apply \(d_k\), then \(c_r\). Put \(X^0=X\) and
\(X^1=\overline X\), with coordinatewise conjugation, and let
\(s(X,Y)=(Y,X)\). The finite set in the question is

\[
\Gamma_{34}(A,B)=
\left\{
s^e\!\left(\alpha c_r d_k(A^\varepsilon),
             \beta c_t d_k(B^\varepsilon)\right):
\begin{array}{l}
\alpha,\beta\in\{1,i,-1,-i\},\quad r,t\in\mathbb Z_{34},\\
k\in\mathbb Z_{34}^{\times},\quad \varepsilon,e\in\{0,1\}
\end{array}
\right\}.
\]

The phases and shifts are independent; decimation and conjugation are common
to both words. Repeated images are collapsed because \(\Gamma_{34}(A,B)\) is a
set. Since

\[
\mathbb Z_{34}^{\times}=
\{1,3,5,7,9,11,13,15,19,21,23,25,27,29,31,33\},
\]

the parameter domain before deduplication has
\(4^2\cdot34^2\cdot16\cdot2\cdot2=1{,}183{,}744\) tuples.

For a quaternary word \(X\), its Gray rows are the unique
\(p,q\in\{\pm1\}^{34}\) satisfying

\[
X=\frac{p+q}{2}+i\frac{p-q}{2};
\]

equivalently, \(p=\operatorname{Re}X+\operatorname{Im}X\) and
\(q=\operatorname{Re}X-\operatorname{Im}X\), coordinatewise. A binary row
\(x\) is reversible exactly when \(x_j=x_{-j}\) for every
\(j\in\mathbb Z_{34}\).

## Exact assertion and scope

Decide the truth value of

\[
\exists\,\alpha,\beta,r,t,k,\varepsilon,e
\quad\text{in the domains above such that all four Gray rows of}\quad
s^e\!\left(\alpha c_r d_k(A^\varepsilon),
             \beta c_t d_k(B^\varepsilon)\right)
\quad\text{are reversible}.
\]

A negative answer is only a statement about this explicitly frozen finite set.
It neither covers an unspecified “full qLP equivalence group” nor says that
other reversible qLPs of length 34 do not exist. In particular, the opposite
decimations available for binary Legendre pairs in equation (1.5) of
Bulutoglu--Baczkowski--Yauney are not included.

For scope checking, the qLP equations are

\[
\operatorname{PAF}(A,h)+\operatorname{PAF}(B,h)=-2
\quad(1\le h<34),\qquad
\operatorname{PAF}(X,h)=\sum_{j\in\mathbb Z_{34}}
X_j\overline{X_{j+h}}.
\]

Independent phase and shift preserve each PAF; common decimation permutes the
nonzero lags; simultaneous conjugation conjugates the summed PAF, whose value
is the real number \(-2\); and exchange swaps the summands. Hence the displayed
operations preserve the qLP equations. This does not assert that they form the
largest possible qLP equivalence group.

## Source status, nearest result, and proposed delta

Source status: **new-question**. The exact \(\Gamma_{34}\)-orbit assertion is a
frozen finite refinement, not a literature claim advertised as open.

The official [HTML](https://arxiv.org/html/2609.04589v1) and
[PDF](https://arxiv.org/pdf/2609.04589v1) of Lebedev, *Quaternary Legendre
Pairs of Lengths 42, 46, 52, 58, 66, 72, and 80*, arXiv:2609.04589v1, were
inspected on 2026-09-08.
Section 7 states only that the printed orientation is not reversible and says
an orbit argument over a full equivalence group was not carried out; Appendix A
prints exactly the two words above. Kotsireas--Koutschan--Winterhof,
[arXiv:2408.16318v2](https://arxiv.org/abs/2408.16318v2), establishes qLP
existence at length 34, not this orbit property. Bulutoglu--Baczkowski--Yauney,
[arXiv:2604.22423v1](https://arxiv.org/abs/2604.22423v1), concerns binary
Legendre-pair equivalence and does not settle the frozen quaternary assertion.
Exact-string and equivalent-language searches of primary arXiv records on
2026-09-08 found no separate decision of this named orbit; this limited search
is not evidence of priority.

- Nearest prior result \(X\): failure of reversibility in the literal printed
  orientation, arXiv:2609.04589v1, Section 7 and Appendix A.
- Proposed delta \(Y\): a complete yes/no decision for the explicitly defined
  \(\Gamma_{34}\)-orbit.
- Verification route \(Z\): reduce the question to exact cyclic-reflection
  tests, then independently reconstruct the frozen parameter domain and audit
  the reduction and qLP-preservation identities.

## Cheapest discriminating test

Because Gray decoding is coordinatewise bijective, both Gray rows of \(X\) are
reversible if and only if \(X_j=X_{-j}\) for every \(j\). Phase and conjugation
preserve equality. For \(Y=c_r d_k(X)\), set
\(u=(j-r)k^{-1}\); then

\[
Y_j=Y_{-j}
\quad\Longleftrightarrow\quad
X_u=X_{-u-2rk^{-1}}.
\]

Thus it suffices to test finitely many cyclic reflection axes. The exact
standard-library check in `evidence/triage_check.py` verifies all 33 qLP
equations and all \(4\cdot34\cdot16\cdot2=4{,}352\) phase/shift/decimation/
conjugation transforms of each word. Its rerun on 2026-09-08 found zero
transforms of \(A\) with both Gray rows reversible (and 256 for \(B\)); it also
found no cyclic reflection axis of either parity for \(A\). This is decisive
candidate evidence for a negative answer, but it has not passed a fresh
mathematical referee or independent implementation audit.
